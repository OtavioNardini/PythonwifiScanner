# Implementação de Tema Claro/Escuro

## Resumo das Mudanças

Foi implementada uma funcionalidade completa de alternância entre tema claro e escuro (light mode) para o site Wi-Fi Scanner com um botão toggle estilizado na navbar.

## Arquivos Criados

### 1. **CSS de Tema** (`app_wifi_scanner/static/css/theme.css`)
- Define variáveis CSS (custom properties) para cores de ambos os temas
- Modo escuro como padrão (`:root`)
- Modo claro com classe `light-mode` no elemento `html`
- Estilos reutilizáveis para componentes da UI
- Transições suaves entre temas

**Variáveis disponíveis:**
- `--bg-primary`: Background principal
- `--bg-secondary`: Background secundário
- `--bg-tertiary`: Background do header/cards semitransparente
- `--bg-card`: Cards de conteúdo
- `--text-primary`: Texto principal
- `--text-secondary`: Texto secundário
- `--text-tertiary`: Texto terciário (labels)
- `--border-color`: Bordas principais
- `--border-light`: Bordas mais claras
- `--accent-color`: Cor de destaque (azul)
- `--accent-dark`: Cor de destaque escura
- `--warning-color`: Cor de aviso (vermelho)
- `--success-color`: Cor de sucesso (verde)
- `--input-bg`: Background de inputs
- `--input-bg-focus`: Background de inputs no foco

### 2. **JavaScript de Tema** (`app_wifi_scanner/static/js/theme.js`)
- Função `toggleTheme()`: Alterna entre os temas
- Função `loadTheme()`: Carrega o tema salvo no localStorage
- Persistência do tema selecionado usando localStorage
- Automático ao carregar a página
- Sem necessidade de recarga

## Componente UI: Toggle Switch

### Estrutura HTML
```html
<div class="theme-toggle">
    <span class="theme-icon">🌙</span>
    <div class="toggle-switch">
        <div class="toggle-circle">☀️</div>
    </div>
</div>
```

### Características
- ✨ Animação suave de 0.3s
- 🎨 Mudança de cor de fundo quando ativo
- 📱 Responsivo
- ♿ Acessível com cursor pointer

### Estilos do Toggle
- Largura: 50px
- Altura: 26px
- Cor padrão: `var(--border-light)`
- Cor ativa: `var(--accent-color)`
- Círculo se move 24px para a direita quando ativo

## Arquivos Modificados

### Templates (com `{% load static %}` adicionado)
1. **home.html**
   - Link para `css/theme.css`
   - Toggle switch na navbar (lado direito)
   - Script `js/theme.js` no final
   - Estilos específicos usando variáveis CSS

2. **login.html**
   - Link para `css/theme.css`
   - Estilos atualizados com variáveis CSS
   - Script `js/theme.js` no final

3. **cadastro.html**
   - Link para `css/theme.css`
   - Estilos atualizados com variáveis CSS
   - Script `js/theme.js` no final

4. **historico.html**
   - Link para `css/theme.css`
   - Toggle switch na navbar
   - Script `js/theme.js` no final
   - Estilos atualizados com variáveis CSS

5. **editar.html**
   - Link para `css/theme.css`
   - Estilos atualizados com variáveis CSS
   - Script `js/theme.js` no final

6. **usuarios.html**
   - Link para `css/theme.css`
   - Toggle switch na navbar
   - Script `js/theme.js` no final
   - Estilos atualizados com variáveis CSS

## Como Funciona

1. **Carregamento Inicial**
   - O arquivo `theme.js` carrega quando a página é inicializada
   - Verifica `localStorage` para o tema salvo
   - Se não houver tema salvo, usa o padrão (dark mode)
   - Aplica a classe `light-mode` ao elemento `html` se necessário

2. **Alternância de Tema**
   - Clique no toggle ativa a função `toggleTheme()`
   - Alterna a classe `light-mode` no `html`
   - Salva a preferência no `localStorage`
   - Transições CSS suaves fazem a mudança parecer natural

3. **Persistência**
   - LocalStorage com chave `theme` (valores: 'light' ou 'dark')
   - Persiste através de recargas de página

## Cores do Modo Claro

| Elemento | Cor |
|----------|-----|
| Background Principal | #f5f7fa |
| Background Cards | rgba(255, 255, 255, 0.9) |
| Texto Principal | #1a1f2e |
| Texto Secundário | rgba(26, 31, 46, 0.6) |
| Cor de Destaque | #2563eb |
| Bordas | rgba(26, 31, 46, 0.1) |

## Cores do Modo Escuro

| Elemento | Cor |
|----------|-----|
| Background Principal | #1a1f2e |
| Background Cards | rgba(30, 35, 48, 0.8) |
| Texto Principal | #ffffff |
| Texto Secundário | rgba(255, 255, 255, 0.6) |
| Cor de Destaque | #4a9eff |
| Bordas | rgba(255, 255, 255, 0.1) |

## Compatibilidade

- ✅ Chrome/Edge (88+)
- ✅ Firefox (87+)
- ✅ Safari (14+)
- ✅ Mobile browsers
- ✅ LocalStorage suportado

## Testando a Funcionalidade

1. Abra qualquer página do site
2. Procure pelo toggle na navbar (ícone 🌙/☀️)
3. Clique para alternar entre temas claro e escuro
4. Recarregue a página - o tema selecionado permanece

## Notas Técnicas

- Todas as cores foram convertidas para variáveis CSS
- Transições de 0.3s foram adicionadas para transições suaves
- O tema é aplicado no nível do elemento `<html>` para afeta toda a página
- Nenhuma dependência externa (vanilla JavaScript + CSS)
- Performance: sem overhead significativo

## Próximas Melhorias Possíveis

- [ ] Detectar preferência do sistema operacional
- [ ] Adicionar mais temas (sepia, alto contraste, etc)
- [ ] Sincronização entre abas do navegador
- [ ] Animações de transição mais sofisticadas
- [ ] Customização de cores pelo usuário
