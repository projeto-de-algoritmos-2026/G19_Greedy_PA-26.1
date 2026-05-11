function inicializarNavScroll() {
    const barra = document.querySelector('.highlight-bar');
    const links = document.querySelectorAll('.nav-links a[href^="#"]');
    const secoes = document.querySelectorAll('section[id]');

    window.addEventListener('scroll', () => {
        const scrollTotal = document.documentElement.scrollHeight - window.innerHeight;
        const progresso = scrollTotal > 0 ? window.scrollY / scrollTotal : 0;
        barra.style.transform = `scaleX(${progresso})`;

        let secaoAtiva = '';
        secoes.forEach(sec => {
            if (window.scrollY >= sec.offsetTop - 120) {
                secaoAtiva = sec.getAttribute('id');
            }
        });

        links.forEach(link => {
            link.classList.toggle('ativo', link.getAttribute('href') === `#${secaoAtiva}`);
        });
    });
}

function inicializarObserver() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visivel');
            }
        });
    }, { threshold: 0.12 });

    document.querySelectorAll('.fade-in, .passo').forEach(el => observer.observe(el));
}

function inicializarTabs() {
    document.querySelectorAll('.tabs').forEach(grupo => {
        const tabs = grupo.querySelectorAll('.tab');
        const container = grupo.closest('[data-tabs]') || grupo.parentElement;

        tabs.forEach(tab => {
            tab.addEventListener('click', () => {
                const alvo = tab.dataset.tab;
                tabs.forEach(t => t.classList.remove('ativo'));
                tab.classList.add('ativo');

                container.querySelectorAll('.tab-conteudo').forEach(c => {
                    c.classList.toggle('ativo', c.dataset.tab === alvo);
                });
            });
        });
    });
}

function inicializarCopiar() {
    document.querySelectorAll('.cmd').forEach(cmd => {
        cmd.addEventListener('click', () => {
            const texto = cmd.dataset.cmd;
            if (!texto) return;
            navigator.clipboard.writeText(texto).then(() => {
                cmd.classList.add('copiado');
                setTimeout(() => cmd.classList.remove('copiado'), 1800);
            });
        });
    });
}

document.addEventListener('DOMContentLoaded', () => {
    inicializarNavScroll();
    inicializarObserver();
    inicializarTabs();
    inicializarCopiar();
});
