// Função para alternar tema
function toggleTheme() {
    const html = document.documentElement;
    const isDarkMode = html.classList.contains('light-mode');
    
    if (isDarkMode) {
        html.classList.remove('light-mode');
        localStorage.setItem('theme', 'dark');
    } else {
        html.classList.add('light-mode');
        localStorage.setItem('theme', 'light');
    }
    
    updateToggleButton();
}

// Função para atualizar o visual do botão
function updateToggleButton() {
    const toggle = document.querySelector('.toggle-switch');
    const isDarkMode = !document.documentElement.classList.contains('light-mode');
    
    if (isDarkMode) {
        toggle.classList.remove('active');
    } else {
        toggle.classList.add('active');
    }
}

// Função para carregar tema salvo ou usar padrão
function loadTheme() {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    const html = document.documentElement;
    
    if (savedTheme === 'light') {
        html.classList.add('light-mode');
    } else {
        html.classList.remove('light-mode');
    }
    
    updateToggleButton();
}

// Carregar tema quando a página carrega
document.addEventListener('DOMContentLoaded', function() {
    loadTheme();
    
    // Adicionar evento de clique ao toggle
    const themeToggle = document.querySelector('.theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }
});
