/**
 * feminnita-config.js
 * Script incluído em TODAS as páginas front-end.
 * Busca /api/config e aplica configurações dinâmicas à página.
 *
 * Uso:
 *   <script src="/feminnita-config.js"></script>
 *   (adicione antes do </body> em cada página)
 */

(function () {
  'use strict';

  const API = '/api/config';

  /* ── Helpers ──────────────────────────────────────────────────────────────── */

  /** Define um texto num elemento por seletor (não quebra se não existir) */
  function setText(sel, txt) {
    const el = document.querySelector(sel);
    if (el && txt !== undefined && txt !== null) el.textContent = txt;
  }

  /** Define um atributo href num elemento */
  function setHref(sel, href) {
    const el = document.querySelector(sel);
    if (el) el.href = href;
  }

  /** Define innerHTML num elemento */
  function setHtml(sel, html) {
    const el = document.querySelector(sel);
    if (el && html !== undefined) el.innerHTML = html;
  }

  /** Aplica variável CSS em :root */
  function setCssVar(name, val) {
    if (val) document.documentElement.style.setProperty(name, val);
  }

  /* ── Announce Bar ─────────────────────────────────────────────────────────── */
  function applyAnnounce(cfg) {
    const bar = document.querySelector('.announce');
    if (!bar || !cfg) return;
    if (!cfg.ativo) { bar.style.display = 'none'; return; }
    if (!cfg.itens || !cfg.itens.length) return;

    // Estilo Angè: fundo cinza, ícone caminhão + texto bold
    bar.style.background = '#f2f2f2';
    bar.style.borderBottom = 'none';

    const truckSVG = `<svg viewBox="0 0 24 24" style="width:18px;height:18px;stroke:currentColor;stroke-width:1.5;fill:none;flex-shrink:0;vertical-align:middle"><rect x="1" y="3" width="15" height="13" rx="1"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>`;

    const sep = '<span class="announce-sep">·</span>';
    bar.innerHTML = cfg.itens.map((txt, i) => {
      // Primeiro item: ícone caminhão + texto com primeira palavra em bold
      if (i === 0) {
        const partes = txt.split(' ');
        const bold = partes.slice(0, 2).join(' ');
        const resto = partes.slice(2).join(' ');
        return `${truckSVG}<span><strong style="font-weight:800;text-transform:uppercase;letter-spacing:.04em">${bold}</strong>${resto ? ' ' + resto : ''}</span>`;
      }
      return `<span>${txt}</span>`;
    }).join(sep);
  }

  /* ── Logo ─────────────────────────────────────────────────────────────────── */
  function applyLoja(cfg) {
    if (!cfg) return;

    // Logo em todas as variações de seletor usadas nas páginas
    const logoSels = ['.logo', '#fnt-logo', '.fnt-logo'];
    logoSels.forEach(sel => setText(sel, cfg.nome));

    // Título da aba
    if (cfg.nome && cfg.slogan) {
      document.title = `${cfg.nome} — ${cfg.slogan}`;
    }

    // Cores CSS
    setCssVar('--borgonha', cfg.corPrimaria);
    setCssVar('--champagne', cfg.corSecundaria);
    setCssVar('--champanhe', cfg.corSecundaria);
  }

  /* ── Nav ──────────────────────────────────────────────────────────────────── */
  function applyNav(itens) {
    const nav = document.querySelector('.hdr-nav, nav.main-nav');
    if (!nav || !itens || !itens.length) return;

    // Preserva classes ativas se existirem
    nav.innerHTML = itens.map(item =>
      `<a href="${item.href}">${item.label}</a>`
    ).join('');
  }

  /* ── Hero ─────────────────────────────────────────────────────────────────── */
  function applyHero(slides) {
    const track = document.querySelector('.hero-track');
    if (!track || !slides || !slides.length) return;

    track.innerHTML = slides.map((sl, i) => {
      // Suporta foto (img) ou gradiente (bg)
      const bgStyle = sl.img
        ? `background-image:url('${sl.img}');background-size:cover;background-position:center`
        : `background:${sl.bg || 'var(--borgonha)'}`;
      return `
      <div class="hero-slide" style="${bgStyle}">
        <div class="hero-content">
          <p class="hero-eyebrow" style="color:rgba(255,255,255,.8);font-size:13px;letter-spacing:.12em;text-transform:uppercase;margin-bottom:12px;font-family:Montserrat,sans-serif">${sl.eyebrow || ''}</p>
          <h2 class="hero-title">${sl.titulo || ''}</h2>
          <p class="hero-sub">${sl.subtitulo || ''}</p>
          <a href="${sl.ctaHref || '#'}" class="hero-cta">
            ${sl.cta || 'Ver coleção'} →
          </a>
        </div>
      </div>
    `;}).join('');

    // Reconstrói dots
    const dotsWrap = document.querySelector('.hero-dots');
    if (dotsWrap) {
      dotsWrap.innerHTML = slides.map((_, i) =>
        `<button class="hdot${i === 0 ? ' on' : ''}" onclick="goSlide(${i})"></button>`
      ).join('');
    }
  }

  /* ── Rodapé ───────────────────────────────────────────────────────────────── */
  function applyRodape(cfg) {
    if (!cfg) return;
    setText('.footer-copy, .rodape-copy', cfg.copyright);
    setText('.footer-cnpj, .rodape-cnpj', cfg.cnpj ? `CNPJ: ${cfg.cnpj}` : '');
    setText('.footer-end, .rodape-end', cfg.endereco);
  }

  /* ── Main ─────────────────────────────────────────────────────────────────── */
  function applyConfig(cfg) {
    try { applyLoja(cfg.loja); }     catch(e) { console.warn('[fnt-cfg] loja:', e); }
    try { applyAnnounce(cfg.announce); } catch(e) { console.warn('[fnt-cfg] announce:', e); }
    try { applyNav(cfg.nav); }       catch(e) { console.warn('[fnt-cfg] nav:', e); }
    try { applyHero(cfg.hero); }     catch(e) { console.warn('[fnt-cfg] hero:', e); }
    try { applyRodape(cfg.rodape); } catch(e) { console.warn('[fnt-cfg] rodape:', e); }

    // Dispara evento para outras partes da página poderem reagir
    document.dispatchEvent(new CustomEvent('fnt:config', { detail: cfg }));
  }

  /* ── Fetch com fallback localStorage ─────────────────────────────────────── */
  function loadConfig() {
    fetch(API)
      .then(r => {
        if (!r.ok) throw new Error('API offline');
        return r.json();
      })
      .then(cfg => {
        // Cache local para modo offline
        try { localStorage.setItem('fnt_cfg_cache', JSON.stringify(cfg)); } catch(e) {}
        applyConfig(cfg);
      })
      .catch(() => {
        // Fallback: usa cache local ou valores padrão
        try {
          const cached = localStorage.getItem('fnt_cfg_cache');
          if (cached) { applyConfig(JSON.parse(cached)); return; }
        } catch(e) {}
        // Fallback mínimo: garante que o logo apareça
        const nome = localStorage.getItem('fnt_logo_name') || 'Feminnita';
        document.querySelectorAll('.logo, #fnt-logo').forEach(el => el.textContent = nome);
        console.info('[fnt-cfg] API offline — usando valores padrão');
      });
  }

  // Executa quando o DOM estiver pronto
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadConfig);
  } else {
    loadConfig();
  }

  // Expõe API pública para uso pelo admin
  window.FntConfig = {
    load: loadConfig,
    save: function(patch) {
      return fetch(API, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(patch)
      }).then(r => r.json());
    },
    saveSection: function(section, data) {
      return fetch(`${API}/${section}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      }).then(r => r.json());
    }
  };

}());
