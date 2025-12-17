from django.shortcuts import render, redirect
from .models import Usuario, WifiScan
from .utils.wifi_scanner import scan_wifi_windows
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.translation import gettext_lazy as _

def home(request):
    # Verificar se o usuário está logado (via sessão)
    if 'usuario_id' not in request.session:
        return redirect('login')
    return render(request, 'usuarios/home.html')
        
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        erro = None
        
        # Verificar se já existe usuário com o mesmo nome
        if Usuario.objects.filter(nome=nome).exists():
            erro = f"Username '{nome}' já existe. Escolha outro."
        # Verificar se já existe usuário com o mesmo email
        elif Usuario.objects.filter(email=email).exists():
            erro = f"Email '{email}' já está registrado."
        else:
            # Se passou na validação, criar o usuário
            novo_usuario = Usuario.objects.create(nome=nome, email=email, senha=senha)
            novo_usuario.save()
            return render(request, 'usuarios/cadastro.html', {'sucesso': 'Usuário cadastrado com sucesso!'})
    
    return render(request, 'usuarios/cadastro.html', {'erro': erro})

def usuarios(request):
    # Verificar se o usuário está logado (via sessão)
    if 'usuario_id' not in request.session:
        return redirect('login')
    usuarios = {'usuarios': Usuario.objects.all()}
    return render(request, 'usuarios/usuarios.html', usuarios)

def login(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')
    else:
        email = request.POST.get('email', '').strip()
        senha = request.POST.get('password', '').strip()
        
        # Validar se os campos foram preenchidos
        if not email or not senha:
            return render(request, 'usuarios/login.html', {'erro': 'Email e senha são obrigatórios.'})
        
        # Verificar se o usuário existe com email e senha
        usuario = Usuario.objects.filter(email=email, senha=senha).first()
        if usuario:
            request.session['usuario_id'] = usuario.id_usuario
            request.session['usuario_nome'] = usuario.nome
            request.session['usuario_email'] = usuario.email
            request.session.set_expiry(86400)  # Sessão de 24 horas
            return redirect('home')
        else: 
            return render(request, 'usuarios/login.html', {'erro': 'Email ou senha inválidos.'})
    
    
def wifi_scan(request):
    data = scan_wifi_windows()
    return JsonResponse({"networks": data})


@csrf_exempt
def save_wifi_scan(request):
    """Salva o scan de Wi-Fi com data e hora"""
    if 'usuario_id' not in request.session:
        return JsonResponse({'erro': 'Usuário não autenticado'}, status=401)
    
    if request.method == 'POST':
        try:
            # Pega os dados do scan atual
            networks_data = scan_wifi_windows()
            
            # Calcula estatísticas
            validSignals = [int(n['signal']) for n in networks_data if n.get('signal')]
            avg_signal = sum(validSignals) // len(validSignals) if validSignals else 0
            
            # Salva no banco de dados
            usuario = Usuario.objects.get(id_usuario=request.session['usuario_id'])
            wifi_scan_obj = WifiScan.objects.create(
                usuario=usuario,
                redes=networks_data,
                total_networks=len(networks_data),
                avg_signal=avg_signal
            )
            
            return JsonResponse({
                'sucesso': True,
                'mensagem': 'Scan salvo com sucesso!',
                'id': wifi_scan_obj.id,
                'data_hora': wifi_scan_obj.data_hora.strftime('%d/%m/%Y %H:%M:%S')
            })
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=500)
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)


def historico_scans(request):
    """Exibe o histórico de scans salvos"""
    if 'usuario_id' not in request.session:
        return redirect('login')
    
    usuario = Usuario.objects.get(id_usuario=request.session['usuario_id'])
    scans = WifiScan.objects.filter(usuario=usuario)
    
    return render(request, 'usuarios/historico.html', {'scans': scans})


def editar_usuario(request, id_usuario):
    """Edita um usuário existente"""
    if 'usuario_id' not in request.session:
        return redirect('login')
    
    try:
        usuario = Usuario.objects.get(id_usuario=id_usuario)
    except Usuario.DoesNotExist:
        return redirect('usuarios')
    
    if request.method == 'GET':
        return render(request, 'usuarios/editar.html', {'usuario': usuario})
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        erro = None
        
        # Verificar se já existe usuário com o mesmo nome (exceto o próprio)
        if Usuario.objects.filter(nome=nome).exclude(id_usuario=id_usuario).exists():
            erro = f"Username '{nome}' já existe. Escolha outro."
        # Verificar se já existe usuário com o mesmo email (exceto o próprio)
        elif Usuario.objects.filter(email=email).exclude(id_usuario=id_usuario).exists():
            erro = f"Email '{email}' já está registrado."
        else:
            # Atualizar o usuário
            usuario.nome = nome
            usuario.email = email
            if senha:  # Só atualiza a senha se foi fornecida
                usuario.senha = senha
            usuario.save()
            return redirect('usuarios')
        
        return render(request, 'usuarios/editar.html', {'usuario': usuario, 'erro': erro})


def deletar_usuario(request, id_usuario):
    """Deleta um usuário"""
    if 'usuario_id' not in request.session:
        return redirect('login')
    
    if request.method == 'POST':
        try:
            usuario = Usuario.objects.get(id_usuario=id_usuario)
            # Não permitir que o usuário delete a si mesmo
            if usuario.id_usuario == request.session['usuario_id']:
                return JsonResponse({'erro': 'Você não pode deletar sua própria conta.'}, status=400)
            usuario.delete()
            return JsonResponse({'sucesso': True, 'mensagem': 'Usuário deletado com sucesso!'})
        except Usuario.DoesNotExist:
            return JsonResponse({'erro': 'Usuário não encontrado.'}, status=404)
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)

