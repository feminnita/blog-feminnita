# Spec Completo Angè → Feminnita
Medido diretamente em useange.com.br — 2026-05-09
Screenshots salvos em sessão Claude.
**ATUALIZADO 2026-05-09** — medições via JS `getBoundingClientRect()` + `getComputedStyle()` confirmadas na sessão.

---

## 1. ELEMENTOS GLOBAIS (todas as páginas da loja)

### ANNOUNCE BAR
- Altura: **30px**
- Background: `#F0F0F0`
- Cor texto: `#727272`
- Font: Montserrat 13px, weight 400
- Layout: flex, center, gap 12px
- Ícone: caminhão SVG (stroke, 18px)
- Texto: "**FRETE GRÁTIS** acima de R$199" (bold nas 2 primeiras palavras)
- Separador entre itens: `·`
- Seletor Feminnita: `.announce`

### HEADER (loja — não checkout)
- Altura: **75px**
- Background: `#FFFFFF`
- Position: `sticky top: 0; z-index: 9999`
- Shadow ao scroll: `box-shadow: 0 2px 8px rgba(0,0,0,.08)`
- Layout interno: `display: flex; align-items: center; justify-content: space-between; max-width: 1400px; margin: 0 auto; padding: 0 40px`

**Logo:**
- Angè usa imagem SVG centralizada
- Feminnita: texto "Feminnita", Cormorant Garamond italic, 34px, #1A1A1A
- Centralizado com flexbox

**Nav (esquerda no Angè, esquerda na Feminnita):**
- Itens: PRODUTOS / LANÇAMENTOS / MAIS VENDIDOS / OUTLET
- Font: Montserrat 15px, weight 400
- Cor: `#777777`
- Text-transform: **UPPERCASE**
- Letter-spacing: normal
- Padding por link: 15px
- Hover: color `#1A1A1A`
- Sem underline, sem border

**Ícones (direita):**
- Busca: input oval com placeholder "O que você está procurando?", border-radius 30px, border 1px #ccc, width ~280px
- Conta: ícone pessoa SVG 22px
- Favoritos: ícone coração SVG 22px
- Sacola: ícone bolsa SVG 22px com badge contador
- Todos cor #777, hover #1A1A1A

### HERO BANNER (homepage)
- Altura: **599px** (desktop)
- Width: 100% full bleed
- Carousel: **owl-carousel** (Feminnita: CSS scroll-snap ou Splide)
- **6 slides** — alternando imagem fotográfica + vídeo
- Cada slide tem **texto sobreposto** (Angè tem):
  - Título grande em fonte cursiva/script (ex: "flowing")
  - Subtítulo menor
  - Link "compre agora →"
- Dots: 6 bullets, circulares, borda `#8C2F39`, ativo = filled
- Autoplay: 5s
- Setas laterais: ← →, circulares, bg branco, shadow
- Fundo: imagem fotográfica ocupa 100% (sem overlay escuro)

**Texto do hero (estilo Angè):**
- Título (script font): ~80px, branco, font cursiva
- Subtítulo: ~16px, branco/transparente
- CTA "compre agora →": sem background, apenas texto + seta

### SEÇÕES DE PRODUTO (homepage)

**Container:**
- Max-width: **1421px** (Angè usa 1421px)
- Margin: 0 auto
- Padding lateral: 50px (desktop)

**Section Title (h2):**
- Font: Montserrat 27px, weight 400
- Cor: `#222222`
- Text-transform: none (ex: "flowing", "Lançamentos", "Mais vendidos", "ÚLTIMOS LANÇAMENTOS")
- Variações: normal case OU UPPERCASE
- Margin-bottom: ~24px

**"flowing" (nome de coleção):**
- Fonte especial: "Flowing" script font → Feminnita: Cormorant Garamond italic
- Font-size: ~50px
- Cor: #222

**Carousel de produtos:**
- 4 colunas desktop (item width 293px com gap 20px em 1421px)
- Scroll horizontal com setas ← →
- Dots de navegação abaixo: 3–4 bullets
- Gap: 20px entre cards

**Grid "ÚLTIMOS LANÇAMENTOS":**
- Layout: carousel horizontal (também owl-carousel)
- 4 colunas visíveis desktop
- Mesmos dots e setas

### NEWSLETTER (homepage e carrinho)
- Box: bg `#F5F5F5`, border-radius 12px, padding ~40px
- Layout: `display: flex; align-items: center; gap: 40px`
- Texto: "CADASTRE-SE PARA RECEBER TODAS AS NOVIDADES" — Montserrat 14px, uppercase, bold
- Inputs: Nome + E-mail, estilo minimalista (apenas border-bottom), inline
- Botão: seta → (apenas ícone)

---

## 2. CARD DE PRODUTO

### Dimensões exatas (medidas no Angè)
- Width: **293px** por card (4 colunas em 1421px)
- Altura total: **560px**
- Imagem: **293 × 439px** → aspect-ratio **2:3** (ratio 1.5)
- Figcaption: altura **121px**, padding `10px 0`
- Todo o texto: **text-align: center**

### Estrutura e CSS

```
article.product-card (293 × 560px)
├── figure (293 × 439px, overflow hidden)
│   ├── .card-overlay (position absolute, inset 0, opacity 0 → 1 no hover)
│   │   ├── .ov-main ("Comprar · Favoritar")
│   │   └── .ov-atacado (tamanhos + qty stepper)
│   ├── .card-badge (position absolute, top 10px, left 10px)
│   └── img.card-img (100% × 100%, object-fit cover, zoom 1.04 no hover)
└── figcaption (padding: 10px 0, text-align center)
    ├── p.prod__ref (12px, #414141)
    ├── h3.p-name (14px, weight 400, #000)
    └── .card-prices
        ├── p.price-old (12px, #999, line-through) — se desconto
        ├── p.boleto.p-price (22px, weight 700, #000)
        ├── span.price__span "via PIX ou Boleto" (12px, #414141)
        └── span.price__span "em até Nx de R$ X,XX sem juros" (12px, #414141)
```

### Hover Overlay
- Background: `rgba(255,255,255,.88)`
- Transition: `opacity .3s`
- "Comprar" e "Favoritar": 15.5px, weight 400, #000, separados por " · "
- Atacado (Feminnita específico): tamanhos P M G GG GGG + qty stepper

### Badge
- Position: absolute, top 10px, left 10px
- Background: `#8C2F39` (borgonha)
- Color: #fff
- Font: 10px, weight 700, uppercase, letter-spacing .08em
- Padding: 3px 7px
- Border-radius: 0 (sem arredondamento)

### Size Badge (tamanho no carrinho)
- Fundo: `#000000` (preto)
- Cor: `#FFFFFF`
- Width: ~31px, height: ~39px
- Font: 18px, weight 600
- Border-radius: 5px

---

## 3. PDP — PÁGINA DO PRODUTO

### Layout Geral
- Breadcrumb: altura 46px, padding `15px 50px`, font 13px, cor `#B1AEA6`
- **`.product-row`**: `display: flex; width: 1421px`
  - Coluna esquerda `.photo-view.left`: **569px** de largura
  - Coluna direita `.full-details_text.right`: **600px** de largura, `position: sticky; top: 0`

### Coluna Esquerda — Galeria de Imagens

**Thumbnails verticais (slick-vertical):**
- Seletor: `.caroussel.slick-vertical`
- Width: **75px**, height: **411px**
- Cada slide: **75 × 127px** (ratio 1.5 = 2:3)
- Scroll vertical com setas ↑ ↓
- Margem do slide ativo: border ou highlight
- 12 slides no total (fotos + vídeos)

**Imagem principal (owl-carousel horizontal):**
- Seletor: `.thumb-product_list`
- Width: **1382px** (escondido atrás de overflow hidden no container ~490px)
- Cada item: **316 × 594px** (ratio 1.5 = 2:3)
- 12 slides — navega clicando nos thumbs laterais
- Ao clicar thumbnail: muda imagem principal
- **VÍDEO**: alguns slides são vídeos (`<video autoplay muted loop>`)

### Coluna Direita — Painel de Info (sticky)

**Título (h1):**
- Classe: `.p-name`
- Font-size: **18px**, font-weight: **600**
- Color: `#000000`
- Text-transform: **UPPERCASE**
- Font-family: Montserrat

**Referência:**
- Tag: `<small class="ref">`
- Font-size: **14px**, weight: **600**
- Color: `#838383`
- Text-transform: UPPERCASE

**Preço PIX/Boleto (principal):**
- Classe: `.boleto.p-price`
- Font-size: **22px**, weight: **700**
- Color: `#000000`
- (No PDP: preço já com desconto PIX aplicado)

**"10% de desconto via PIX ou Boleto":**
- Classe: `.__porcentagemDesconto2`
- Font-size: **12px**, weight: 400
- Color: `#838383`

**Parcelamento:**
- "ou R$ X,XX em até **10x de R$ Y,YY** sem juros"
- Font-size: 14px, color `#B1AEA6`
- Valor em bold: 14px, weight **700**, #000

**"TAMANHO:" label:**
- Tag: `<label>`
- Font-size: 14px, weight **600**, UPPERCASE, #000

**Botões de tamanho:**
- Classe: `.btn-tamanho`
- Width: **40px**, height: **40px**
- Border: `0.8px solid #000`
- Border-radius: 8px
- Background: #fff
- Font: 15px, weight 500
- Selecionado: bg #000 (ou cor primária), color #fff

**Links auxiliares (Experimentar / Provador Virtual / Tabela de medidas):**
- Font-size: **13.5px**, weight: **600**, color: `#838383`
- Com ícone SVG à esquerda
- Display: inline-flex, gap 6px

**Botão COMPRAR:**
- Width: **480px** (aprox, preenche coluna)
- Height: **50px**
- Background: `#45A89C` (verde/teal Angè) → Feminnita: `#8C2F39` (borgonha)
- Color: `#FFFFFF`
- Font: Montserrat 15px, weight 600, UPPERCASE
- Border-radius: **30px** (pill shape)
- Letter-spacing: .1em
- Border: none

**"Frete grátis acima de R$ 299":**
- Com ícone caminhão SVG
- Font: 13px, color #777
- Display: inline-flex, gap 8px

**Share icon:** ícone compartilhar (→ com curva), 20px, #777, top-right

### Seção Descrição (abaixo do fold)
- Font: 14px, color `#B1AEA6`, line-height 24px
- Padding-bottom: 29px
- **"Especificações técnicas:"** — bold, #222, seguido de lista

### Seção Avaliações
- Título: "AVALIAÇÃO" — uppercase
- Estrelas: ★★★★★ (amarelas/pretas)
- Reviews: avatar circular, nome, data, texto, estrelas

### "Compre o Look" (seção na página)
- Duas imagens grandes lado a lado: produto atual + sugestão
- Separadas por símbolo "+"  entre e "=" à direita
- À direita: mini cards de cada produto com tamanho + price
- "Total:" + preço grande
- Título: "Compre o Look" — 27px, weight 400, #222

### Modal "COMPRE O LOOK COMPLETO" (ao clicar COMPRAR sem selecionar tamanho)
- Fundo: header preto, `#000`, texto branco
- Título: "COMPRE O LOOK COMPLETO" — 22px, weight 400, white, UPPERCASE
- Layout 2 colunas: lista de produtos (esq) + imagem look completo (dir)
- Produto item: thumbnail 150px + nome 20px + "Você já está comprando!" / "Escolha seu tamanho"
- Price: `.price.valor-atual` — 22px, weight 400, #000
- Total: bold, grande, direita
- Fechar: × no canto superior direito

### Carousels no PDP
- "Mais desse look": carousel horizontal, owl-carousel, 4 cards visíveis, mesmo estilo que homepage
- "PRODUTOS SIMILARES": mesmo carousel, título UPPERCASE, tracking .05em

---

## 4. CARRINHO

### Header do Carrinho
- Igual ao header da loja (announce bar + header completo)

### Título da Página
- "MEU CARRINHO (CÓDIGO)" — font 16px, weight 700, UPPERCASE
- "COMPRA 100% SEGURA" à direita — com shield icon, bold

### Tabela de Itens
- Colunas: **PRODUTO | TAMANHO | QUANTIDADE | PREÇO | TOTAL | REMOVER**
- Headers: Montserrat, 12-13px, UPPERCASE, weight 600, bg cinza claro
- Border-bottom entre linhas: 1px solid #eee

**Item row:**
- Thumbnail: ~80×120px (ratio 2:3)
- Nome produto: 14-16px, UPPERCASE, weight 600, #000
- Ref: 12px, #777
- Size badge: `<small class="tamanho">` — bg #000, color #fff, 31×39px, font 18px, border-radius 5px
- Qty stepper: botões `-` e `+` (35×30px), input numérico no centro
- Preço: 18px, weight 700, `#676767` (classe `.subtotal-`)
- "via PIX ou Boleto": 12px, #B1AEA6
- Total: igual ao preço
- Remover: ícone lixeira SVG, 20px, #777

### FRETE
- Label: "FRETE" — 13px, UPPERCASE, weight 600
- Input CEP: 200px, height 42px, border 1px #ccc, border-radius 4px
- Botão CALCULAR: bg #555, color #fff, height 42px, 100px, UPPERCASE
- "Não sei meu CEP ▶": link pequeno, 12px, #777
- Progress bar: barra cinza → ícone caminhão à direita
- Texto: "Faltam R$ X,XX para ganhar frete grátis"

### CUPOM DE DESCONTO
- Label: "CUPOM DE DESCONTO"
- Input + botão VALIDAR (mesmo estilo que CALCULAR)

### TOTAL DO PEDIDO
- Label: "TOTAL DO PEDIDO" — bold, 16px
- Linhas de pagamento (direita):
  - "VIA PIX OU BOLETO COM 10% DE DESCONTO" → valor bold
  - "À VISTA NO CARTÃO" → valor
  - "OPÇÕES DE PARCELAMENTO" → "10X de R$ X,XX **SEM JUROS**"

### Botões de ação (rodapé do carrinho)
- **CONTINUAR COMPRANDO**: bg `#555555` (cinza escuro), color #fff, height 50px, ~50% width, UPPERCASE, font 14px, letter-spacing .1em
- **FINALIZAR COMPRA**: bg `#45A89C` (teal/verde) → Feminnita `#8C2F39`, color #fff, mesmas dimensões

### Newsletter no Carrinho
- Mesma do homepage: box cinza, inline inputs, seta

---

## 5. CHECKOUT

### Header Checkout (simplificado)
- **Sem announce bar**
- **Sem nav links**
- Apenas logo centralizado
- Altura: 75px
- Logo: imagem SVG "angè" centralizada

### Topo da Página
- Esquerda: "FINALIZAR COMPRA" — font 16px, weight 700, UPPERCASE
- Direita: shield icon + "COMPRA 100% SEGURA"

### Layout de 3 Colunas
```
[DADOS PESSOAIS 350px] [ENDEREÇO 350px] [PAGAMENTO + RESUMO 370px]
```
- Gap: ~50px entre colunas
- Max-width: 1421px, centralizado

### Section Headers (boxes)
- Background: `#E8E8E8` (cinza claro)
- Padding: 10px 20px
- Font: 13px, weight 600, UPPERCASE, #555
- Com ícone à esquerda (pessoa, localização, cartão)

### DADOS PESSOAIS
- Box: border 1px #eee, border-radius 8px, padding 24px
- Mostra: email, nome, telefone
- Botão "EDITAR INFORMAÇÕES": outline, border 1px #ccc, border-radius 30px, 100% width, height 42px, font 13px UPPERCASE

### ENDEREÇO
- "ENDEREÇO DE ENTREGA" — 16px, weight 600, UPPERCASE
- Endereço card: border 1px #ccc, border-radius 8px, padding 16px, radio button à esquerda
- Ícone lixeira para remover
- Botão "ENTREGAR NESTE ENDEREÇO": bg #555, color #fff, height 48px, 100% width, border-radius 4px, UPPERCASE

### FORMA DE ENTREGA
- Radio options: cada opção em box (border 1px #eee, border-radius 8px, padding 12px 16px, height ~60px)
- Layout: nome + dias úteis à esquerda, preço à direita
- Opção selecionada: radio preenchido, bg levemente destacado

### INPUTS DE FORMULÁRIO (novo endereço)
- Height: 42px
- Border: 1px solid #ccc
- Border-radius: 4px
- Font: 14px
- Padding: 0 12px
- Placeholder: cor #aaa

### RESUMO DO PEDIDO (coluna direita)
- Width: **370px**, altura variável
- Sem border (bg transparente, apenas separadores linha)
- **"Pagamento"**: 15px, weight 600, #555
- Opções de pagamento: "Pix", "Cartão de crédito", etc. — 13px, weight 600
- Total PIX: 14px, weight 700
- Linhas separadoras: `border-bottom: 1px solid #eee`

### Footer Checkout (simplificado)
- **Sem links de navegação** (INSTITUCIONAL, ATENDIMENTO, etc.)
- **Apenas a barra de pagamentos**:
  - "Formas de pagamento": PIX, VISA, Mastercard, Amex, Elo, Diners, PagBank, PayPal, Boleto — ícones
  - "Segurança": Google Safe Browsing, ReclameAqui
  - "Forma de envio": Correios
  - Cabeçalhos: 14px, weight 700
- Base: CNPJ + aviso de cookies — 12px, #777

---

## 6. RODAPÉ DA LOJA (3 colunas + barra)

### Rodapé principal
- Background: `#F0F0F0` (cinza muito claro) — *NÃO é preto*
- **3 colunas**:
  1. **INSTITUCIONAL**: links (Central de Ajuda, Trocas, Envio, Como Comprar, Política de Privacidade, Procon RJ)
  2. **ATENDIMENTO**: WhatsApp, telefone, email, Horários (Seg-Qui 8-18h, Sex 8-17h)
  3. **SIGA NOSSAS REDES SOCIAIS**: ícones Instagram, Facebook, TikTok, Pinterest, YouTube, Blog, Spotify + box "angè vip"

**Cabeçalhos colunas:**
- Font: Montserrat 13px, weight 600-700, UPPERCASE, letter-spacing .08em, #333
- Margin-bottom: 16px

**Links:**
- Font: Montserrat 13-15px, weight 400, color #414141
- Hover: color #000

**Padding rodapé:** 60px 50px (vertical/horizontal)

### Barra inferior do rodapé
- Background: branco ou cinza muito claro (separado por linha `border-top: 1px solid #E0E0E0`)
- **3 grupos**:
  1. Formas de pagamento: PIX, VISA, MC, Amex, Elo, Diners, PagBank, PayPal, Boleto (2 linhas)
  2. Segurança: Google Safe Browsing, ReclameAqui
  3. Forma de envio: Correios
- Cabeçalhos: 14px, weight 700, #000

### Base (copyright)
- "Ao navegar... cookies..." — 12px, #777, text-align center
- CNPJ completo + endereço — 12px, #777

---

## 7. ADAPTAÇÕES FEMINNITA vs ANGÈ

| Elemento | Angè | Feminnita |
|---|---|---|
| Cor primária | #45A89C (teal) | #8C2F39 (borgonha) |
| Cor secundária | — | #C9965A (champagne) |
| Logo | Imagem SVG | Texto Cormorant Garamond italic |
| Fonte principal | "Muli Regular" | Montserrat |
| Parcelamento | 10x sem juros | **3x sem juros** |
| PIX desconto | 10% | Mostrar preço direto |
| Frete grátis | acima R$299 | acima R$199 |
| Botão COMPRAR | teal pill | borgonha pill |
| Footer | cinza claro | **preto #1A1A1A** (decisão anterior) |
| Categoria | Fitness/Esporte | Pijamas/Íntima |
| Swatches de cor | não visível no card | omitir no card, mostrar no PDP |
| Vídeo no hero | SIM (vídeos reais) | começar com imagens |

---

## 8. TIPOGRAFIA RESUMIDA

| Elemento | px | weight | transform |
|---|---|---|---|
| Logo | 34px | 400 italic | — |
| Nav links | 15px | 400 | UPPERCASE |
| Announce | 13px | 400 | normal |
| Hero título | 60-80px | 400 | normal (script) |
| Section h2 | 27px | 400 | varies |
| Card nome | 14px | 400 | normal |
| Card ref | 12px | 400 | normal |
| Card preço | **22px** | **700** | normal |
| Card PIX label | 12px | 400 | normal |
| Card parcela | 12px | 400 | normal |
| Hover Comprar | 15.5px | 400 | normal |
| PDP título h1 | 18px | **600** | UPPERCASE |
| PDP ref | 14px | 600 | UPPERCASE |
| PDP preço | 22px | 700 | normal |
| PDP parcela | 14px | 400/700 | normal |
| PDP label Tam | 14px | 600 | UPPERCASE |
| PDP btn Comprar | 15px | 600 | UPPERCASE |
| Carrinho título | 16px | 700 | UPPERCASE |
| Checkout título | 16px | 700 | UPPERCASE |
| Rodapé heads | 13-15px | 600-700 | UPPERCASE |
| Rodapé links | 13-15px | 400 | normal |
| Copyright | 12px | 400 | normal |

---

## 9. PALETA COMPLETA

```css
:root {
  /* Feminnita */
  --borgonha: #8C2F39;
  --champagne: #C9965A;
  --creme: #F7F4F1;
  --borda: #E6E2DE;
  --preto: #1A1A1A;
  --cinza: #6B6B6B;

  /* Angè measurements */
  --text-dark: #222222;
  --text-medium: #777777;
  --text-soft: #414141;
  --text-light: #B1AEA6;
  --bg-announce: #F0F0F0;
  --bg-section: #F5F5F5;
  --border-light: #E6E2DE;
}
```

---

## 10. MEDIÇÕES REAIS CONFIRMADAS (getBoundingClientRect + getComputedStyle)

> Extraídas via JavaScript direto no useange.com.br em 2026-05-09.
> Estas corrigem/complementam estimativas anteriores.

### PDP — Produto: Top Rose Harmonia

| Elemento | Medição Real |
|---|---|
| Coluna esquerda `.photo-view` | **569px** wide |
| Thumbnails verticais `.caroussel` | **75px** wide × **411px** tall |
| Imagem principal `.thumb-product_list` | **1382px** wide (overflow hidden no container ~490px) |
| H1 produto | 18px, weight 600, UPPERCASE |
| Preço PIX `.p-price` | **30px**, weight 700, #000 |
| Ref produto | 16px, weight 400, #000, transform: none |
| Coluna direita `.full-details_text` | **600px** wide, `position: sticky` |
| Botão COMPRAR | **360px** × **50px**, bg teal `rgb(76,166,134)` → Feminnita: `#8C2F39`, border-radius **30px** (pill), font **18px**, weight **500**, UPPERCASE |
| Botões de tamanho | ~**35×30px**, border: 0.8px solid #bababab, border-radius 10px (canto esquerdo) |

### CARRINHO

| Elemento | Medição Real |
|---|---|
| Thumbnail produto | **100×150px** (ratio 2:3) |
| Stepper botão − / + | **35×30px**, bg #fff, border: none |
| Botão CONTINUAR COMPRANDO | **226×40px**, bg `rgb(77,77,77)`, border-radius **5px**, font 12px weight 600 |
| Botão FINALIZAR COMPRA | **226×40px**, bg `rgb(76,166,134)` → Feminnita: `#8C2F39`, border-radius **5px** |
| Título "MEU CARRINHO" | 16px, weight 400 |
| "COMPRA 100% SEGURA" | shield icon + texto |
| Colunas tabela | PRODUTO / TAMANHO / QUANTIDADE / PREÇO / TOTAL / REMOVER |

### FOOTER

| Elemento | Medição Real |
|---|---|
| Background | `rgb(240,240,240)` = **#F0F0F0** (cinza claro, NÃO escuro) |
| Newsletter bg | `rgb(240,240,240)` = `#F0F0F0`, altura 150px |
| Colunas | INSTITUCIONAL / ATENDIMENTO / SIGA NOSSAS REDES SOCIAIS |
| Links INSTITUCIONAL | Central de Ajuda · Trocas e Devoluções · Envio e Entrega · Como Comprar · Política de Privacidade · Procon RJ |
| ATENDIMENTO | WhatsApp 22 99616.4303 · Tel 22 2523.4791 · contato@useange.com.br |
| REDES SOCIAIS | Instagram · Facebook · TikTok · Pinterest · YouTube · Blog · Spotify |
| Bônus | "ACESSE NOSSO CANAL VIP" → angè vip |

### NEWSLETTER BOX

| Elemento | Medição Real |
|---|---|
| Background | `#F0F0F0` (mesmo do footer) |
| Texto | "CADASTRE-SE PARA RECEBER TODAS AS NOVIDADES" — bold, uppercase |
| Layout | flex row: texto + input Nome (border-bottom only) + input E-mail (border-bottom only) + botão → |
| Botão | apenas seta → (sem background, sem border) |

### HOMEPAGE CAROUSEL (seção "flowing" + "ÚLTIMOS LANÇAMENTOS")

| Elemento | Medição Real |
|---|---|
| Dots "flowing" | 3 bullets (1 ativo = outline, 2 inativos = preenchidos) |
| Dots "ÚLTIMOS LANÇAMENTOS" | 4 bullets |
| Título "flowing" | fonte especial script, ~50px |
| Título "ÚLTIMOS LANÇAMENTOS" | Montserrat, UPPERCASE, sem background (bg branco) |
| Parcelamento cards | "em até **10x** de R$ X,XX" → Feminnita: **3x** |
| Card preço label | "via PIX ou Boleto" |

### HERO BANNER (homepage)

| Elemento | Medição Real |
|---|---|
| Slides | 6 slides (dots = 6 bullets circulares) |
| Texto slide 1 | fundo escuro + texto "quando tudo foi, existe presença" (cursivo) + "flowing" + "compre agora →" |
| Texto slide 2 | "RUNDROP" (uppercase bold) + "NEW IN" + "→ COMPRE AGORA" |
| Setas laterais | ← → visíveis nas bordas do hero |
| Height | ~600px viewport |

### PLP (página de listagem)

| Elemento | Medição Real |
|---|---|
| Breadcrumb | HOME > PRODUTOS > CATEGORIA |
| Controles | FILTRAR ▼ · ORDENAR ▼ (esq) + toggle grid (dir) |
| Título categoria | centralizado, maiúsculo |
| Colunas desktop | **3 colunas** (não 4 como no home) |

### CHECKOUT (medições reais confirmadas)

| Elemento | Medição Real |
|---|---|
| Header | **75px**, logo centralizado, SEM nav, SEM announce bar |
| Topo | "FINALIZAR COMPRA" (esq, 16px bold UPPERCASE) + shield + "COMPRA 100% SEGURA" (dir) |
| Layout | **3 colunas** lado a lado |
| Col 1 "DADOS PESSOAIS" | email, nome, tel + btn "EDITAR INFORMAÇÕES" |
| Col 2 "ENDEREÇO" | "ENDEREÇO DE ENTREGA" 16px 600 + card endereço (radio + CEP + rua) + "ENTREGAR NESTE ENDEREÇO" (298×35px, bg `rgb(112,112,112)` cinza, border-radius 25px) + "FORMA DE ENTREGA" + radio options |
| FORMA DE ENTREGA radio | cada opção: nome + prazo (esq) + preço (dir), border 1px, border-radius, height ~60px |
| Col 3 "PAGAMENTO" + "RESUMO DO PEDIDO" | section headers bg cinza, resumo: Subtotal, ENTREGA (frete selecionado), TOTAL |
| TOTAL linha | "Pix ou Boleto R$ X,XX" / "Cartão de crédito R$ Y,YY" |
| EDITAR INFORMAÇÕES btn | outline, border 1px #ccc, border-radius 30px (pill), 100% width col, height ~42px |
| Footer checkout | apenas barra de pagamentos — sem nav INSTITUCIONAL/ATENDIMENTO |

### MEDIÇÕES GERAIS CORRETAS (corrigindo spec anterior onde diverge)

| Elemento | Spec Anterior | **Real Medido** |
|---|---|---|
| PDP preço | 22px | **30px** weight 700 |
| PDP ref | 14px 600 #838383 UPPERCASE | **16px 400 #000 sem transform** |
| PDP COMPRAR btn width | 480px | **360px** |
| PDP COMPRAR btn height | 50px | **50px** ✓ |
| PDP COMPRAR btn radius | 30px | **30px** (pill) ✓ |
| PDP COMPRAR btn font | 15px 600 | **18px weight 500** |
| PDP size buttons | 40×40px | **35×30px** |
| Cart thumbnail | 80×120px | **100×150px** (ratio 2:3) |
| Cart action btn height | 50px | **40px** |
| Cart action btn radius | 4px | **5px** |
| Cart FINALIZAR width | ~50% | **226px** (lado a lado) |
| Checkout ENTREGAR btn | 48px | **35px** height, 298px width |
| Checkout ENTREGAR radius | 4px | **25px** (semi-pill) |
