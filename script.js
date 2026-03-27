/* ============================================================
   BLOG FEMINNITA — script.js
   Versão: 1.0 | 2026
   Filtro de artigos, modal de captura, navbar mobile,
   newsletter, tempo de leitura, formulário comunidade
   ============================================================ */

/* ── Utilitário: executar após o DOM estar pronto ─────────── */
document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initFiltros();
  initCalcularTempoLeitura();
  initNewsletterForm();
  initComunidadeForm();
  initScrollNavbar();
  initBreadcrumb();
});


/* ══════════════════════════════════════════════════
   NAVBAR — hamburguer mobile
══════════════════════════════════════════════════ */
function initNavbar() {
  const hamburger = document.getElementById('hamburger');
  const menu      = document.getElementById('navMenu');

  if (!hamburger || !menu) return;

  hamburger.addEventListener('click', () => {
    const aberto = menu.classList.toggle('aberto');
    hamburger.classList.toggle('aberto', aberto);
    hamburger.setAttribute('aria-expanded', aberto.toString());
  });

  /* Fecha menu ao clicar em um link */
  menu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      menu.classList.remove('aberto');
      hamburger.classList.remove('aberto');
      hamburger.setAttribute('aria-expanded', 'false');
    });
  });

  /* Fecha menu ao clicar fora */
  document.addEventListener('click', (e) => {
    if (!hamburger.contains(e.target) && !menu.contains(e.target)) {
      menu.classList.remove('aberto');
      hamburger.classList.remove('aberto');
      hamburger.setAttribute('aria-expanded', 'false');
    }
  });
}


/* ══════════════════════════════════════════════════
   SCROLL — leve fundo extra na navbar ao rolar
══════════════════════════════════════════════════ */
function initScrollNavbar() {
  const navbar = document.querySelector('.navbar');
  if (!navbar) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.style.boxShadow = '0 4px 28px rgba(92,26,34,0.35)';
    } else {
      navbar.style.boxShadow = '0 2px 20px rgba(92,26,34,0.3)';
    }
  }, { passive: true });
}


/* ══════════════════════════════════════════════════
   FILTROS DE ARTIGOS — client-side, sem reload
   Suporta: .filtro-pill + .card-artigo (páginas antigas)
            .filtro-ed   + .editorial-card (homepage editorial)
══════════════════════════════════════════════════ */
function initFiltros() {
  /* Detecta qual conjunto de elementos existe na página */
  const pills = document.querySelectorAll('.filtro-ed').length
    ? document.querySelectorAll('.filtro-ed')
    : document.querySelectorAll('.filtro-pill');

  const cards = document.querySelectorAll('.editorial-card[data-cat]').length
    ? document.querySelectorAll('.editorial-card[data-cat]')
    : document.querySelectorAll('.card-artigo[data-cat]');

  const nenhumAviso = document.getElementById('nenhumArtigo');

  if (!pills.length || !cards.length) return;

  pills.forEach(pill => {
    pill.addEventListener('click', () => {
      /* Atualiza estado dos botões */
      pills.forEach(p => {
        p.classList.remove('ativo');
        p.setAttribute('aria-pressed', 'false');
      });
      pill.classList.add('ativo');
      pill.setAttribute('aria-pressed', 'true');

      const catSelecionada = pill.dataset.cat;
      let visiveis = 0;

      /* Mostra/oculta cards */
      cards.forEach(card => {
        const matchTodos = catSelecionada === 'todos';
        const matchCateg = card.dataset.cat === catSelecionada;

        if (matchTodos || matchCateg) {
          card.classList.remove('oculto');
          /* Garante que o card esteja visível (editorial-card usa classe .visivel) */
          if (card.classList.contains('editorial-card')) {
            requestAnimationFrame(() => card.classList.add('visivel'));
          } else {
            card.style.opacity = '0';
            card.style.transform = 'translateY(8px)';
            requestAnimationFrame(() => {
              card.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
              card.style.opacity = '1';
              card.style.transform = 'translateY(0)';
            });
          }
          visiveis++;
        } else {
          card.classList.add('oculto');
          card.style.opacity = '';
          card.style.transform = '';
          card.style.transition = '';
        }
      });

      /* Aviso quando não há artigos na categoria */
      if (nenhumAviso) {
        nenhumAviso.style.display = visiveis === 0 ? 'block' : 'none';
      }
    });
  });
}


/* ══════════════════════════════════════════════════
   MODAL DE CAPTURA DE E-MAIL
══════════════════════════════════════════════════ */
/* Variável para lembrar qual material foi solicitado */
let materialAtual = '';

/* Abre o modal — chamado pelos botões "Baixar grátis" */
function abrirModal(nomeMaterial) {
  materialAtual = nomeMaterial || 'material';

  const overlay   = document.getElementById('modalCaptura');
  const subtitulo = document.getElementById('modalSubtitulo');
  const form      = document.getElementById('formCaptura');
  const sucesso   = document.getElementById('mensagemSucessoModal');
  const aviso     = overlay ? overlay.querySelector('.modal__aviso') : null;

  if (!overlay) return;

  /* Reseta o modal para o estado inicial */
  if (form)    form.style.display    = '';
  if (sucesso) sucesso.classList.remove('visivel');
  if (aviso)   aviso.style.display   = '';

  if (subtitulo) {
    subtitulo.textContent =
      `Preencha e receba "${nomeMaterial}" gratuitamente no seu e-mail.`;
  }

  overlay.classList.add('aberto');
  document.body.style.overflow = 'hidden';

  /* Foco no primeiro campo para acessibilidade */
  setTimeout(() => {
    const primeiroInput = overlay.querySelector('input');
    if (primeiroInput) primeiroInput.focus();
  }, 100);
}

/* Fecha o modal */
function fecharModal() {
  const overlay = document.getElementById('modalCaptura');
  if (!overlay) return;
  overlay.classList.remove('aberto');
  document.body.style.overflow = '';
}

/* Fecha ao clicar no overlay (fora do modal) */
function fecharModalFora(event) {
  if (event.target.id === 'modalCaptura') {
    fecharModal();
  }
}

/* Fecha com ESC */
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') fecharModal();
});

/* Submissão do formulário de captura */
function submeterCaptura(event) {
  event.preventDefault();

  const form    = document.getElementById('formCaptura');
  const sucesso = document.getElementById('mensagemSucessoModal');
  const aviso   = document.querySelector('.modal__aviso');
  const nome    = document.getElementById('capturaNome');
  const email   = document.getElementById('capturaEmail');

  /* Simulação de envio — aqui você integra com sua plataforma de e-mail */
  console.log('Lead capturado:', {
    nome:     nome ? nome.value : '',
    email:    email ? email.value : '',
    material: materialAtual,
  });

  /* Mostra mensagem de sucesso */
  if (form)    form.style.display = 'none';
  if (aviso)   aviso.style.display = 'none';
  if (sucesso) sucesso.classList.add('visivel');

  /* Fecha o modal automaticamente após 3s */
  setTimeout(() => fecharModal(), 3000);
}


/* ══════════════════════════════════════════════════
   NEWSLETTER — homepage e outras páginas
══════════════════════════════════════════════════ */
function initNewsletterForm() {
  const form = document.getElementById('formNewsletter');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    submeterNewsletter(e);
  });
}

function submeterNewsletter(event) {
  if (event) event.preventDefault();

  const form = document.getElementById('formNewsletter');
  const msg  = document.getElementById('msgNewsletter');
  const btn  = form ? form.querySelector('button[type="submit"]') : null;

  if (!form) return;

  const emailInput = form.querySelector('input[type="email"]');
  console.log('Newsletter:', emailInput ? emailInput.value : '');

  /* Feedback visual */
  if (btn) {
    btn.textContent = 'Enviando...';
    btn.disabled = true;
  }

  setTimeout(() => {
    if (form)    form.style.display = 'none';
    if (msg)     msg.style.display  = 'block';
  }, 800);
}


/* ══════════════════════════════════════════════════
   FORMULÁRIO DA COMUNIDADE (comunidade.html)
══════════════════════════════════════════════════ */
function initComunidadeForm() {
  const form    = document.getElementById('formComunidade');
  const sucesso = document.getElementById('sucessoComunidade');

  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const dados = {
      nome:      form.querySelector('#comNome')?.value,
      email:     form.querySelector('#comEmail')?.value,
      cidade:    form.querySelector('#comCidade')?.value,
      profissao: form.querySelector('#comProfissao')?.value,
      tema:      form.querySelector('#comTema')?.value,
      mensagem:  form.querySelector('#comMensagem')?.value,
    };

    console.log('Proposta de autor recebida:', dados);

    /* Mostra mensagem de sucesso */
    form.style.display = 'none';
    if (sucesso) {
      sucesso.classList.add('visivel');
      sucesso.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  });
}


/* ══════════════════════════════════════════════════
   FILTROS DA PÁGINA DE TREINAMENTO
══════════════════════════════════════════════════ */
function initFiltrosTreinamento() {
  const pills   = document.querySelectorAll('.filtro-pill-treinamento');
  const cards   = document.querySelectorAll('.card-material[data-cat]');

  if (!pills.length || !cards.length) return;

  pills.forEach(pill => {
    pill.addEventListener('click', () => {
      pills.forEach(p => {
        p.classList.remove('ativo');
        p.setAttribute('aria-pressed', 'false');
      });
      pill.classList.add('ativo');
      pill.setAttribute('aria-pressed', 'true');

      const cat = pill.dataset.cat;

      cards.forEach(card => {
        const visivel = cat === 'todos' || card.dataset.cat === cat;

        if (visivel) {
          card.closest('.card-material-wrapper')?.classList.remove('oculto');
          card.classList.remove('oculto');
        } else {
          card.closest('.card-material-wrapper')?.classList.add('oculto');
          card.classList.add('oculto');
        }
      });
    });
  });
}


/* ══════════════════════════════════════════════════
   TEMPO DE LEITURA — calculado pelo texto do artigo
══════════════════════════════════════════════════ */
function initCalcularTempoLeitura() {
  const corpo = document.querySelector('.artigo-body');
  const badge = document.querySelector('.js-tempo-leitura');

  if (!corpo || !badge) return;

  const palavras = corpo.innerText.trim().split(/\s+/).length;
  const minutos  = Math.max(1, Math.ceil(palavras / 200)); /* 200 ppm de leitura média */

  badge.textContent = `${minutos} min de leitura`;
}


/* ══════════════════════════════════════════════════
   BREADCRUMB — destaca a página atual
══════════════════════════════════════════════════ */
function initBreadcrumb() {
  /* Nada a fazer além de garantir que o HTML renderize corretamente */
}


/* ══════════════════════════════════════════════════
   SMOOTH SCROLL — âncoras internas
══════════════════════════════════════════════════ */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    const alvo = document.querySelector(anchor.getAttribute('href'));
    if (alvo) {
      e.preventDefault();
      const offsetNavbar = 68 + 8; /* altura da navbar + folga */
      const top = alvo.getBoundingClientRect().top + window.scrollY - offsetNavbar;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});


/* ══════════════════════════════════════════════════
   ANIMAÇÃO DE ENTRADA DOS CARDS (Intersection Observer)
══════════════════════════════════════════════════ */
(function initAnimacaoCards() {
  /* Verifica suporte */
  if (!('IntersectionObserver' in window)) return;

  const estilo = document.createElement('style');
  estilo.textContent = `
    .card-animado {
      opacity: 0;
      transform: translateY(20px);
      transition: opacity 0.45s ease, transform 0.45s ease;
    }
    .card-animado.visivel {
      opacity: 1;
      transform: translateY(0);
    }
  `;
  document.head.appendChild(estilo);

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visivel');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  /* Aplica nos cards de artigo, download, comunidade e material */
  document.querySelectorAll(
    '.card-artigo, .card-download, .card-comunidade, .card-material, .card-depoimento, .card-perfil'
  ).forEach(card => {
    card.classList.add('card-animado');
    observer.observe(card);
  });

  /* Editorial cards usam .visivel diretamente (sem .card-animado) */
  document.querySelectorAll('.editorial-card').forEach(card => {
    observer.observe(card);
  });
})();


/* ══════════════════════════════════════════════════
   EXPOR funções globais usadas pelo HTML inline
══════════════════════════════════════════════════ */
window.abrirModal         = abrirModal;
window.fecharModal        = fecharModal;
window.fecharModalFora    = fecharModalFora;
window.submeterCaptura    = submeterCaptura;
window.submeterNewsletter = submeterNewsletter;

/* Inicializa filtros de treinamento se a página tiver */
document.addEventListener('DOMContentLoaded', () => {
  initFiltrosTreinamento();
});
