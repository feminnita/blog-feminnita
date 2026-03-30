#!/usr/bin/env python3
"""
Script de publicação automática — Blog Feminnita
Roda via GitHub Actions todo dia às 03h BRT.
Lê schedule.json, publica posts com data <= hoje.
"""

import json
import os
import shutil
import sys
from datetime import date, datetime

DRY_RUN = '--dry-run' in sys.argv
TODAY = date.today().isoformat()
DRAFTS_DIR = '_drafts/artigos'
SCHEDULE_FILE = 'schedule.json'
ARTIGOS_FILE = 'artigos.html'
INSERT_MARKER = '    <!-- SCHEDULED-POSTS-INSERT -->'

MONTHS_PT = {
    1: 'jan', 2: 'fev', 3: 'mar', 4: 'abr', 5: 'mai', 6: 'jun',
    7: 'jul', 8: 'ago', 9: 'set', 10: 'out', 11: 'nov', 12: 'dez'
}

def fmt_date(date_str):
    """'2026-04-06' → '06 abr 2026'"""
    d = datetime.strptime(date_str, '%Y-%m-%d')
    return f"{d.day:02d} {MONTHS_PT[d.month]} {d.year}"

def build_card(post):
    """Gera o HTML do editorial-card para inserir no artigos.html."""
    date_pt = fmt_date(post['publishDate'])
    return f"""
      <!-- ── AUTO-PUBLICADO {post['publishDate']} ── {post['categoryLabel']} ─── -->
      <article class="editorial-card" data-cat="{post['category']}" role="listitem">
        <img src="{post['image']}"
             alt="{post['imageAlt']}"
             loading="lazy"
             onerror="this.style.display='none'" />
        <div class="editorial-card__ov"></div>
        <div class="editorial-card__body">
          <span class="editorial-card__tag {post['tagClass']}">
            <i class="fa-solid {post['categoryIcon']}" aria-hidden="true"></i> {post['categoryLabel']}
          </span>
          <h3 class="editorial-card__titulo">
            <a href="{post['slug']}.html" style="color:inherit;text-decoration:none;">
              {post['title']}
            </a>
          </h3>
          <p class="editorial-card__resumo">
            {post['excerpt']}
          </p>
          <div class="editorial-card__meta">
            <span>{post['author']}</span>
            <span class="editorial-card__meta-sep">·</span>
            <span>{date_pt}</span>
            <span class="editorial-card__meta-sep">·</span>
            <span><i class="fa-regular fa-clock" aria-hidden="true"></i> {post['readTime']} min</span>
          </div>
          <a href="{post['slug']}.html" class="editorial-card__ler">
            Ler artigo <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
          </a>
        </div>
      </article>
"""

def insert_card_in_artigos(card_html):
    """Insere o card HTML no artigos.html antes do marker."""
    with open(ARTIGOS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    if INSERT_MARKER not in content:
        print(f'  ⚠️  Marker "{INSERT_MARKER}" não encontrado em {ARTIGOS_FILE}.')
        print('     O card não foi inserido. Adicione o marker manualmente.')
        return False

    updated = content.replace(INSERT_MARKER, card_html + INSERT_MARKER)
    with open(ARTIGOS_FILE, 'w', encoding='utf-8') as f:
        f.write(updated)
    return True

def main():
    print(f"📅  Data de hoje: {TODAY}")
    if DRY_RUN:
        print("🔍  Modo DRY RUN — nenhuma mudança será salva.\n")

    # Carregar schedule.json
    with open(SCHEDULE_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    posts = data['posts']
    published_count = 0

    for post in posts:
        if post['status'] != 'scheduled':
            continue

        pub_date = post['publishDate']
        slug = post['slug']

        if pub_date > TODAY:
            print(f"⏳  [{pub_date}] {slug} — ainda não está na hora.")
            continue

        print(f"\n🚀  Publicando: {slug} (data: {pub_date})")

        # Verificar se o arquivo draft existe
        src = os.path.join(DRAFTS_DIR, f"{slug}.html")
        dst = f"{slug}.html"

        if not os.path.exists(src):
            print(f"  ❌  Draft não encontrado: {src}")
            continue

        if DRY_RUN:
            print(f"  ✅  [DRY RUN] Copiaria {src} → {dst}")
            print(f"  ✅  [DRY RUN] Inseriria card no artigos.html")
            published_count += 1
            continue

        # Copiar draft para raiz
        shutil.copy2(src, dst)
        print(f"  ✅  Arquivo copiado: {src} → {dst}")

        # Inserir card no artigos.html
        card_html = build_card(post)
        if insert_card_in_artigos(card_html):
            print(f"  ✅  Card inserido no artigos.html")

        # Atualizar status no schedule.json
        post['status'] = 'published'
        published_count += 1

    if published_count == 0:
        print("\n✨  Nenhum post para publicar hoje.")
    else:
        print(f"\n🎉  {published_count} post(s) publicado(s)!")

    if not DRY_RUN and published_count > 0:
        with open(SCHEDULE_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("💾  schedule.json atualizado.")

if __name__ == '__main__':
    main()
