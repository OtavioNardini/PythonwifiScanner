# Guia de Internacionalização (i18n) - Django

## ✅ Configurações Aplicadas

### 1. Settings.py
- ✅ `USE_I18N = True` - Ativado
- ✅ `LANGUAGE_CODE = 'pt-br'` - Idioma padrão: Português Brasil
- ✅ `TIME_ZONE = 'America/Sao_Paulo'` - Fuso horário do Brasil
- ✅ `LocaleMiddleware` - Adicionado na posição correta
- ✅ `LANGUAGES` - Configurado (PT-BR, EN, ES)
- ✅ `LOCALE_PATHS` - Definido para '/locale'

### 2. URLs.py
- ✅ Adicionado `i18n_patterns` para URLs com prefixo de idioma
- ✅ Rota `/i18n/` para troca de idioma

### 3. Estrutura de Diretórios
- ✅ Pasta `locale/` criada

## 📋 Próximos Passos

### Passo 1: Marcar Textos para Tradução

Nos seus templates HTML, envolva os textos que deseja traduzir com as tags de tradução:

```django
{% load i18n %}

<!-- Para textos simples -->
<h1>{% trans "Wi-Fi Networks Dashboard" %}</h1>

<!-- Para textos em blocos -->
{% blocktrans %}
    Bem-vindo ao sistema de scanner Wi-Fi
{% endblocktrans %}

<!-- Em variáveis Python (views.py) -->
from django.utils.translation import gettext as _

def minha_view(request):
    mensagem = _("Olá, mundo!")
    return render(request, 'template.html', {'mensagem': mensagem})
```

### Passo 2: Gerar Arquivos de Tradução

Execute os comandos no terminal (na pasta wifi_scanner):

```bash
# Para criar arquivos de tradução em inglês
python manage.py makemessages -l en

# Para criar arquivos de tradução em espanhol
python manage.py makemessages -l es

# Para ignorar o ambiente virtual
python manage.py makemessages -l en --ignore=.venv
```

Isso criará:
- `locale/en/LC_MESSAGES/django.po`
- `locale/es/LC_MESSAGES/django.po`

### Passo 3: Traduzir os Textos

Edite os arquivos `.po` gerados:

```po
# locale/en/LC_MESSAGES/django.po

msgid "Wi-Fi Networks Dashboard"
msgstr "Wi-Fi Networks Dashboard"

msgid "Salvar Scan"
msgstr "Save Scan"

msgid "Ver Histórico"
msgstr "View History"
```

### Passo 4: Compilar as Traduções

```bash
python manage.py compilemessages
```

Isso criará os arquivos `.mo` (binários) que o Django usa.

### Passo 5: Adicionar Seletor de Idioma nos Templates

No arquivo `home.html`, adicione dentro da navbar:

```django
{% load i18n %}

<div class="nav-right">
    <!-- Seletor de Idioma -->
    <div class="language-selector">
        <form action="{% url 'set_language' %}" method="post">
            {% csrf_token %}
            <input name="next" type="hidden" value="{{ request.path }}">
            <select name="language" onchange="this.form.submit()">
                {% get_current_language as LANGUAGE_CODE %}
                {% get_available_languages as LANGUAGES %}
                {% for lang_code, lang_name in LANGUAGES %}
                    <option value="{{ lang_code }}" {% if lang_code == LANGUAGE_CODE %}selected{% endif %}>
                        {{ lang_name }}
                    </option>
                {% endfor %}
            </select>
        </form>
    </div>
    
    <!-- Toggle de Tema -->
    <div class="theme-toggle">
        ...
    </div>
    
    <!-- Usuário -->
    <div class="user">
        ...
    </div>
</div>
```

## 🎨 Exemplo Prático - home.html

Substitua os textos fixos por traduções:

```django
{% load i18n %}
{% load static %}
<!DOCTYPE html>
<html lang="{{ LANGUAGE_CODE }}">
<head>
    <title>{% trans "Wi-Fi Networks Dashboard" %}</title>
    ...
</head>
<body>
    <h1>{% trans "Wi-Fi Networks Dashboard" %}</h1>
    
    <button class="btn btn-save">
        💾 {% trans "Salvar Scan" %}
    </button>
    
    <button class="btn btn-history">
        📋 {% trans "Ver Histórico" %}
    </button>
    
    <div class="stat-card">
        <div class="stat-label">{% trans "Total Networks" %}</div>
        ...
    </div>
</body>
</html>
```

## 🌐 Como Funciona

1. **Usuário acessa**: `http://127.0.0.1:8000/` (padrão: pt-br)
2. **Troca para inglês**: `http://127.0.0.1:8000/en/`
3. **Troca para espanhol**: `http://127.0.0.1:8000/es/`

Ou usando o seletor de idioma que criamos.

## 📦 Arquivos Criados

- ✅ `wifi_scanner/locale/` - Diretório de traduções
- ✅ `templates/usuarios/language_selector.html` - Componente seletor

## 🔧 Comandos Úteis

```bash
# Criar/Atualizar arquivos de tradução
python manage.py makemessages -l en --ignore=.venv
python manage.py makemessages -l es --ignore=.venv

# Compilar traduções
python manage.py compilemessages

# Ver todos os idiomas disponíveis
python manage.py diffsettings | grep LANGUAGE

# Executar servidor
python manage.py runserver
```

## 📝 Textos Sugeridos para Traduzir

### Home (Dashboard)
- "Wi-Fi Networks Dashboard"
- "Salvar Scan"
- "Ver Histórico"
- "Total Networks"
- "Average Signal"
- "Most Used Channel"
- "Hidden Networks"
- "Detected Networks"
- "Networks Overview"
- "Strong Signal"
- "Weak Signal"
- "Recommended Channel"
- "Top 5 Strongest Networks"

### Login
- "Login"
- "Email"
- "Password"
- "Remember me"
- "Forgot password?"
- "Don't have an account?"
- "Register"

### Cadastro
- "User Registration"
- "Username"
- "Register"
- "Already have an account?"

### Usuários
- "Users List"
- "Add User"
- "Search users..."
- "Username"
- "Status"
- "Actions"
- "Edit"
- "Delete"
- "Active"

### Histórico
- "Histórico de Scans"
- "Voltar ao Dashboard"
- "Total de Redes"
- "Sinal Médio"
- "Canal"

## 🎯 Benefícios

✅ Site multilíngue (PT-BR, EN, ES)
✅ URLs com prefixo de idioma (/en/, /es/, /pt-br/)
✅ Seletor de idioma integrado
✅ Compatível com o tema claro/escuro
✅ Tradução dinâmica sem recarregar

## ⚠️ Importante

1. **Sempre use `{% load i18n %}` no topo dos templates**
2. **Rode `makemessages` após adicionar novos textos**
3. **Rode `compilemessages` após traduzir**
4. **Reinicie o servidor após compilar**

## 🚀 Teste Agora

1. Adicione `{% load i18n %}` em um template
2. Envolva um texto com `{% trans "..." %}`
3. Execute: `python manage.py makemessages -l en --ignore=.venv`
4. Edite o arquivo `.po` gerado
5. Execute: `python manage.py compilemessages`
6. Acesse: `http://127.0.0.1:8000/en/`
