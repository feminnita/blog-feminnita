from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import os

BASE = "C:/Users/chris/Downloads/BLOG/imagens/"
OUT  = "C:/Users/chris/Downloads/BLOG/imagens/prontas/"
os.makedirs(OUT, exist_ok=True)

# ─── Carrega imagens ───────────────────────────────────────────────
familia    = Image.open(BASE + "Gemini_Generated_Image_ce0kp2ce0kp2ce0k.png").convert("RGB")
mulher     = Image.open(BASE + "Hailuo_Image_vista a modelo de rosto com a _491150116295061510 (1).jpg").convert("RGB")
lilas_tec  = Image.open(BASE + "WhatsApp Image 2026-03-27 at 12.10.13.jpeg").convert("RGB")
branco_tec = Image.open(BASE + "WhatsApp Image 2026-03-27 at 12.10.13 (1).jpeg").convert("RGB")
azul_flat  = Image.open(BASE + "WhatsApp Image 2026-03-27 at 12.32.15.jpeg").convert("RGB")
lilas_flat = Image.open(BASE + "WhatsApp Image 2026-03-27 at 12.32.15 (1).jpeg").convert("RGB")

print("Família:", familia.size)
print("Mulher preta:", mulher.size)
print("Lilás tecido:", lilas_tec.size)
print("Branco corações:", branco_tec.size)
print("Azul gatinho:", azul_flat.size)
print("Lilás flat lay:", lilas_flat.size)

def crop_center(img, w, h):
    """Recorta do centro na proporção desejada."""
    iw, ih = img.size
    ratio_dest = w / h
    ratio_src  = iw / ih
    if ratio_src > ratio_dest:
        new_w = int(ih * ratio_dest)
        left  = (iw - new_w) // 2
        img   = img.crop((left, 0, left + new_w, ih))
    else:
        new_h = int(iw / ratio_dest)
        top   = (ih - new_h) // 2
        img   = img.crop((0, top, iw, top + new_h))
    return img.resize((w, h), Image.LANCZOS)

def salvar(img, nome, q=88):
    path = OUT + nome
    img.save(path, "JPEG", quality=q, optimize=True)
    kb = os.path.getsize(path) // 1024
    print(f"  OK {nome} - {img.size[0]}x{img.size[1]}px - {kb}KB")

# ══════════════════════════════════════════════════════════════════
# 1. HERO DA HOME  (900×860)
#    → Família lifestyle — sem watermark, mostra linha completa
# ══════════════════════════════════════════════════════════════════
print("\n[1] Hero da home...")
hero = crop_center(familia, 900, 860)
salvar(hero, "hero-home.jpg", q=85)

# ══════════════════════════════════════════════════════════════════
# 2. MULHER PRETA — remove watermark cortando rodapé  (800×450)
#    O watermark fica nos últimos ~120px da imagem
# ══════════════════════════════════════════════════════════════════
print("\n[2] Mulher pijama preto (remove watermark)...")
mw, mh = mulher.size
corte  = int(mh * 0.93)          # mantém 93% do topo (sem watermark)
mulher_limpa = mulher.crop((0, 0, mw, corte))
card_mulher  = crop_center(mulher_limpa, 800, 450)
salvar(card_mulher, "card-mulher-preta.jpg")

# ══════════════════════════════════════════════════════════════════
# 3. FLAT LAY LILÁS — crop para remover fundo bagunçado  (800×450)
#    Cabos no canto sup-esq, cadeira amarela sup-dir, cadeira rosa inf-esq
# ══════════════════════════════════════════════════════════════════
print("\n[3] Flat lay conjunto lilás...")
lw, lh = lilas_flat.size
# Corta margens: 14% topo, 8% baixo, 10% esq, 10% dir
t = int(lh * 0.14)
b = int(lh * 0.92)
l = int(lw * 0.10)
r = int(lw * 0.90)
lilas_crop = lilas_flat.crop((l, t, r, b))
card_lilas = crop_center(lilas_crop, 800, 450)
salvar(card_lilas, "card-lilas-flatlay.jpg")

# ══════════════════════════════════════════════════════════════════
# 4. FLAT LAY AZUL GATINHO — crop fundo  (800×450)
# ══════════════════════════════════════════════════════════════════
print("\n[4] Flat lay conjunto azul...")
aw, ah = azul_flat.size
t = int(ah * 0.04)
b = int(ah * 0.96)
l = int(aw * 0.04)
r = int(aw * 0.96)
azul_crop = azul_flat.crop((l, t, r, b))
card_azul = crop_center(azul_crop, 800, 450)
salvar(card_azul, "card-azul-flatlay.jpg")

# ══════════════════════════════════════════════════════════════════
# 5. MONTAGEM HEADER ARTIGO TECIDOS  (1200×480)
#    Esquerda: tecido lilás  |  Direita: tecido branco corações
#    Linha divisória dourada no centro
# ══════════════════════════════════════════════════════════════════
print("\n[5] Header artigo tecidos (montagem dupla)...")
BORGONHA  = (140, 47, 57)
CHAMPAGNE = (212, 169, 86)

header = Image.new("RGB", (1200, 480))

# Metade esquerda — lilás (tecido da camiseta)
esq = crop_center(lilas_tec, 600, 480)
# Levanta um pouco o brilho
esq = ImageEnhance.Brightness(esq).enhance(1.08)
header.paste(esq, (0, 0))

# Metade direita — branco corações (tecido do shorts)
dir_ = crop_center(branco_tec, 600, 480)
dir_ = ImageEnhance.Brightness(dir_).enhance(1.05)
header.paste(dir_, (600, 0))

# Linha divisória dourada no centro
draw = ImageDraw.Draw(header)
draw.rectangle([596, 0, 603, 480], fill=CHAMPAGNE)

# Overlay escuro suave nos dois lados (para texto futuro)
overlay = Image.new("RGBA", (1200, 480), (0, 0, 0, 0))
ov_draw = ImageDraw.Draw(overlay)
ov_draw.rectangle([0, 380, 1200, 480], fill=(0, 0, 0, 80))
header = header.convert("RGBA")
header = Image.alpha_composite(header, overlay).convert("RGB")

salvar(header, "artigo-tecidos-header.jpg", q=90)

# ══════════════════════════════════════════════════════════════════
# 6. CLOSE-UP TECIDO LILÁS  (800×450)  — para usar dentro do artigo
# ══════════════════════════════════════════════════════════════════
print("\n[6] Close-up tecido lilás...")
close_lilas = crop_center(lilas_tec, 800, 450)
close_lilas = ImageEnhance.Brightness(close_lilas).enhance(1.1)
close_lilas = ImageEnhance.Contrast(close_lilas).enhance(1.05)
salvar(close_lilas, "close-lilas.jpg")

# ══════════════════════════════════════════════════════════════════
# 7. CLOSE-UP TECIDO BRANCO CORAÇÕES  (800×450)
# ══════════════════════════════════════════════════════════════════
print("\n[7] Close-up tecido branco corações...")
close_bco = crop_center(branco_tec, 800, 450)
close_bco = ImageEnhance.Brightness(close_bco).enhance(1.1)
salvar(close_bco, "close-coracoes.jpg")

# ══════════════════════════════════════════════════════════════════
# 8. MONTAGEM COMUNIDADE / CARD FAMÍLIA  (800×450)
#    Família — já está boa, só redimensiona
# ══════════════════════════════════════════════════════════════════
print("\n[8] Card família...")
card_familia = crop_center(familia, 800, 450)
salvar(card_familia, "card-familia.jpg")

print("\nTodas as montagens concluidas!")
print(f"Arquivos salvos em: {OUT}")
