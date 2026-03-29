#!/usr/bin/env python3
"""
publish.py — Feminnita Blog Auto-Publisher
Executa toda terça e sexta via GitHub Actions.
Lê _drafts/schedule.json, publica o artigo do dia em index.html.
"""

import json, os, shutil, re
from datetime import datetime, timezone, timedelta

# Timezone Brasil (UTC-3)
BRT = timezone(timedelta(hours=-3))
today = datetime.now(BRT).strftime('%Y-%m-%d')

print(f"[publish.py] Data hoje (BRT): {today}")

# Carrega calendário
with open('_drafts/schedule.json', encoding='utf-8') as f:
    schedule = json.load(f)

# Filtra artigos de hoje com status scheduled
posts_hoje = [p for p in schedule if p['date'] == today and p['status'] == 'scheduled']

if not posts_hoje:
    print("[publish.py] Nenhum artigo agendado para hoje. Encerrando.")
    exit(0)

for post in posts_hoje:
    slug = post['slug']
    filename = post['filename']
    draft_path = f"_drafts/artigos/{filename}"

    print(f"[publish.py] Publicando: {post['title']}")

    # 1. Copia artigo de _drafts/artigos/ para raiz
    if not os.path.exists(draft_path):
        print(f"[ERRO] Arquivo não encontrado: {draft_path}")
        continue

    shutil.copy(draft_path, filename)
    print(f"[publish.py] Arquivo copiado: {filename}")

    # 2. Monta o card HTML para inserir no index.html
    pub_date = datetime.strptime(post['date'], '%Y-%m-%d')
    months_pt = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
    date_str = f"{pub_date.day} {months_pt[pub_date.month-1]} {pub_date.year}"

    card_html = f"""
        <!-- ── Card — {post['tag_label']} — {post['date']} ── -->
        <article class="editorial-card" data-cat="{post['category']}" role="listitem">
          <img
            src="imagens/prontas/{post['card_image']}"
            alt="{post['title']}"
            loading="lazy"
            onerror="this.style.background='var(--creme)';this.style.minHeight='220px'"
          />
          <div class="editorial-card__ov"></div>
          <div class="editorial-card__body">
            <span class="editorial-card__tag {post['tag_class']}">
              <i class="{post['icon']}" aria-hidden="true"></i> {post['tag_label']}
            </span>
            <h3 class="editorial-card__titulo">
              <a href="{filename}" style="color:inherit;text-decoration:none;">
                {post['title']}
              </a>
            </h3>
            <p class="editorial-card__resumo">{post['resumo']}</p>
            <div class="editorial-card__meta">
              <span>{post['author']}</span>
              <span class="editorial-card__meta-sep">·</span>
              <span>{date_str}</span>
              <span class="editorial-card__meta-sep">·</span>
              <span><i class="fa-regular fa-clock" aria-hidden="true"></i> {post['read_time']} min</span>
            </div>
            <a href="{filename}" class="editorial-card__ler">
              Ler artigo <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
            </a>
          </div>
        </article>"""

    # 3. Insere o card no index.html logo após a abertura do editorial-grid
    with open('index.html', encoding='utf-8') as f:
        index_content = f.read()

    marker = '<div class="editorial-grid"'
    marker_pos = index_content.find(marker)
    if marker_pos == -1:
        print("[ERRO] Marcador editorial-grid não encontrado no index.html")
        continue

    # Encontra o fim da tag de abertura do div
    end_of_opening_tag = index_content.find('>', marker_pos) + 1

    new_content = (
        index_content[:end_of_opening_tag]
        + '\n' + card_html
        + index_content[end_of_opening_tag:]
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"[publish.py] Card inserido no index.html")

    # 4. Atualiza status no schedule.json
    post['status'] = 'published'

# Salva schedule atualizado
with open('_drafts/schedule.json', 'w', encoding='utf-8') as f:
    json.dump(schedule, f, ensure_ascii=False, indent=2)

print("[publish.py] Publicação concluída com sucesso!")
