/**
 * feminnita-cart.js
 * Gerenciador global do carrinho — localStorage com eventos.
 * Incluir em todas as páginas: <script src="/feminnita-cart.js"></script>
 */
(function () {
  'use strict';

  const KEY = 'fnt_cart';

  /* ── Persistência ─────────────────────────────────────────────────────── */
  function read() {
    try { return JSON.parse(localStorage.getItem(KEY)) || []; }
    catch(e) { return []; }
  }

  function save(items) {
    try { localStorage.setItem(KEY, JSON.stringify(items)); }
    catch(e) {}
    emit();
  }

  function emit() {
    const items = read();
    const qty = items.reduce((sum, i) => sum + (i.qty || 1), 0);
    // Atualiza badges de carrinho na página
    document.querySelectorAll('[data-cart-badge], .cart-badge, .hdr-cart-count, .bag-count').forEach(el => {
      el.textContent = qty;
      el.style.display = qty > 0 ? '' : 'none';
    });
    // Dispara evento para a página reagir
    document.dispatchEvent(new CustomEvent('fnt:cart', { detail: { items, qty } }));
  }

  /* ── API pública ──────────────────────────────────────────────────────── */
  window.FntCart = {

    get: read,

    count: function() {
      return read().reduce((s, i) => s + (i.qty || 1), 0);
    },

    total: function() {
      return read().reduce((s, i) => s + (i.preco || 0) * (i.qty || 1), 0);
    },

    /** Adiciona ou incrementa item */
    add: function(item) {
      const items = read();
      // item = { id, nome, tamanho, cor, qty, preco, imagem, ref }
      const key = item.id + '|' + (item.tamanho || '') + '|' + (item.cor || '');
      const idx = items.findIndex(i =>
        i.id + '|' + (i.tamanho || '') + '|' + (i.cor || '') === key
      );
      if (idx >= 0) {
        items[idx].qty = (items[idx].qty || 1) + (item.qty || 1);
      } else {
        items.push({ ...item, qty: item.qty || 1 });
      }
      save(items);
      return items;
    },

    /** Remove item pelo índice */
    remove: function(index) {
      const items = read();
      items.splice(index, 1);
      save(items);
      return items;
    },

    /** Remove item pelo id+tamanho+cor */
    removeByKey: function(id, tamanho, cor) {
      const key = id + '|' + (tamanho || '') + '|' + (cor || '');
      const items = read().filter(i =>
        i.id + '|' + (i.tamanho || '') + '|' + (i.cor || '') !== key
      );
      save(items);
      return items;
    },

    /** Atualiza quantidade */
    setQty: function(index, qty) {
      const items = read();
      if (!items[index]) return items;
      if (qty <= 0) { items.splice(index, 1); }
      else { items[index].qty = qty; }
      save(items);
      return items;
    },

    clear: function() {
      save([]);
    }
  };

  /* ── Inicialização ────────────────────────────────────────────────────── */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', emit);
  } else {
    emit();
  }

}());
