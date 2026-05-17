# Spec de Design — Angè → Feminnita
Medido diretamente em useange.com.br em 2026-05-09

---

## PALETA DE CORES

| Elemento | Cor Angè | CSS Var Feminnita |
|---|---|---|
| Background body | #FFFFFF | — |
| Texto body padrão | rgb(177,174,166) = #B1AEA6 | — |
| Texto escuro | rgb(34,34,34) = #222222 | — |
| Texto médio | rgb(119,119,119) = #777777 | — |
| Texto suave | rgb(65,65,65) = #414141 | — |
| Announce bar bg | rgb(240,240,240) = #F0F0F0 | manter cinza claro |
| Cor primária Feminnita | — | --borgonha: #8C2F39 |
| Cor secundária Feminnita | — | --champagne: #C9965A |
| Borda suave | — | --borda: #E6E2DE |

---

## TIPOGRAFIA

| Uso | Fonte Angè | Fonte Feminnita | Tamanho | Peso |
|---|---|---|---|---|
| Corpo geral | "Muli Regular" | Montserrat | 16px | 400 |
| Logo | imagem | Cormorant Garamond italic | — | — |
| Nav links | "Muli Regular" | Montserrat | 16px | 400 |
| Section title (h2) | "Muli Regular" | Montserrat | 27px | 400 |
| Card nome produto | "Muli Regular" | Montserrat | 14px | 400 |
| Card preço (PIX) | "Muli Regular" | Montserrat | 22px | **700** |
| Card PIX label | "Muli Regular" | Montserrat | 12px | 400 |
| Card parcelamento | "Muli Regular" | Montserrat | 12px | 400 |
| Card ref | "Muli Regular" | Montserrat | 12px | 400 |
| Hover "Comprar" | "Muli Regular" | Montserrat | 15.5px | 400 |

---

## ANNOUNCE BAR

- **Seletor**: `section.first-header` → Feminnita: `div.announce`
- **Altura**: 30px
- **Background**: #F0F0F0
- **Cor texto**: #727272
- **Font-size**: 13px
- **Conteúdo Feminnita**: ícone caminhão + "FRETE GRÁTIS acima de R$199"
- **Layout**: flex, center, gap 24px
- **Separador**: `·` entre itens

---

## HEADER

- **Altura total**: 75px (sem announce)
- **Background**: #FFFFFF (branco sólido)
- **Position**: `sticky top:0` com `z-index: 9999`
- **Shadow ao scroll**: `0 2px 8px rgba(0,0,0,.08)`
- **Layout interno**: `display: flex; align-items: center; justify-content: space-between; padding: 0 40px; max-width: 1400px; margin: 0 auto`

### Logo
- Angè usa imagem. Feminnita usa texto: "Feminnita"
- Font: Cormorant Garamond, italic
- Font-size: ~32px
- Color: #1A1A1A

### Nav links
- Font: Montserrat, 16px, weight 400
- Color: #777777
- Text-transform: UPPERCASE
- Letter-spacing: normal
- Padding: 15px (cada link)
- Hover: color #1A1A1A (escurece)
- **Sem border-bottom, sem underline**

### Ícones header (busca, favoritos, sacola)
- Stroke icons, 24px, color #777
- Sacola: contador badge borgonha

---

## HERO SLIDER (Banner Principal)

- **Altura**: 599px (viewport width)
- **Width**: 100% (full bleed — sem padding lateral)
- **Slides**: 8 slides alternando VIDEO + IMAGEM (Angè usa ambos)
- **Carousel**: usar CSS puro ou JS simples com autoplay 5s
- **Dots**: bullets circulares na parte inferior central
- **Transição**: fade ou slide
- **Sem overlay de texto** sobre o banner (Angè: imagens/vídeos sem texto sobreposto)
- **Aspect ratio imagem hero**: ~8:3 (1521×594px) → manter 100% width, height 599px fixed

---

## SEÇÕES DE PRODUTOS

### Section Title (h2)
- Font: Montserrat, 27px, weight 400
- Color: #222222
- Text-transform: none
- Margin-bottom: ~20px
- **Padding seção**: 40px 0 (vertical) + padding lateral do container
- **Exemplos**: "Destaques", "Lançamentos"

### Container width
- Max-width: ~1400px
- Margin: 0 auto
- Padding: 0 20px

---

## CARD DE PRODUTO (article.product-shortview)

### Dimensões
- **Largura**: 293px (owl carousel item)
- **Altura total**: 560px
- **Imagem**: 293×439px → proporção **2:3** (ratio 1.5)
- **Figcaption** (texto abaixo da foto): altura 121px, padding 10px 0

### Estrutura HTML do card
```
<article class="product-card">
  <figure>
    <!-- hover overlay (Comprar + Favoritar) -->
    <div class="card-overlay">
      <a class="btn-comprar">Comprar</a>
      <a class="btn-favoritar">Favoritar</a>
      <!-- Atacado: seletor tamanho + qty stepper -->
    </div>
    <!-- Badge NOVO / SALE etc -->
    <span class="card-badge">NOVO</span>
    <!-- Imagem principal -->
    <img class="card-img" src="..." alt="...">
  </figure>
  <figcaption>
    <p class="prod__ref">FNT2301/ROSA</p>
    <h3 class="p-name">Pijama Longo Regata Floral Rosê</h3>
    <div class="card-prices">
      <!-- Preço antigo (riscado, se existir) -->
      <p class="price-old">R$ 109,90</p>
      <!-- Preço principal (PIX/Boleto) -->
      <p class="boleto p-price">R$ 89,90</p>
      <span class="price__span">via PIX ou Boleto</span>
      <!-- Parcelamento -->
      <span class="price__span">em até <strong>3x de R$ 29,97</strong> sem juros</span>
    </div>
  </figcaption>
</article>
```

### CSS do card
```css
.product-card {
  width: 100%;
  cursor: pointer;
}
.product-card figure {
  position: relative;
  overflow: hidden;
  aspect-ratio: 2/3;  /* imagem ocupa 2/3 */
  margin: 0;
}
.product-card .card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform .4s ease;
}
.product-card:hover .card-img {
  transform: scale(1.04);
}
.product-card figcaption {
  padding: 10px 0;
  text-align: center;
}
.prod__ref {
  font-size: 12px;
  color: #414141;
  margin: 0 0 2px;
}
.p-name {
  font-size: 14px;
  font-weight: 400;
  color: #000;
  margin: 0 0 6px;
  line-height: 1.3;
}
.price-old {
  font-size: 12px;
  color: #999;
  text-decoration: line-through;
  margin: 0;
}
.p-price {
  font-size: 22px;
  font-weight: 700;
  color: #000;
  margin: 2px 0 0;
}
.price__span {
  display: block;
  font-size: 12px;
  color: #414141;
  margin: 1px 0;
}
```

### Hover Overlay
```css
.card-overlay {
  position: absolute;
  inset: 0;
  background: rgba(255,255,255,0.85);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  opacity: 0;
  transition: opacity .3s;
}
.product-card:hover .card-overlay { opacity: 1; }
.btn-comprar, .btn-favoritar {
  font-size: 15.5px;
  font-weight: 400;
  color: #000;
  text-decoration: none;
  letter-spacing: .05em;
}
```

### Atacado Overlay (específico Feminnita — sobrepõe ao hover padrão)
```css
/* Tamanhos */
.ov-sizes { display: flex; gap: 6px; flex-wrap: wrap; justify-content: center; }
.ov-sz {
  min-width: 34px; height: 34px; border: 1px solid #ccc;
  background: #fff; font-size: 11px; cursor: pointer; border-radius: 2px;
}
.ov-sz.on { border-color: #8C2F39; color: #8C2F39; }
/* Qty stepper */
.ov-qty { display: flex; align-items: center; gap: 10px; }
.ov-qbtn {
  width: 28px; height: 28px; border: 1px solid #ccc; background: #fff;
  font-size: 16px; cursor: pointer; border-radius: 50%;
}
.ov-qnum { font-size: 14px; min-width: 20px; text-align: center; }
```

---

## CAROUSEL DE PRODUTOS

- **Biblioteca Angè**: owl-carousel
- **Feminnita**: usar CSS scroll-snap (mais simples, sem dependência)
- **Item width**: ~293px (4 items visíveis em desktop 1400px com 20px gap)
- **Gap entre cards**: 20px
- **Setas**: ← → sobrepostas, bordas arredondadas
- **Dots**: opcionais

### Layout CSS
```css
.carousel-wrap { position: relative; overflow: hidden; }
.carousel-track {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scrollbar-width: none;
  padding-bottom: 8px;
}
.carousel-track::-webkit-scrollbar { display: none; }
.carousel-track .product-card {
  flex: 0 0 calc(25% - 15px);  /* 4 col em 1400px */
  scroll-snap-align: start;
}
```

---

## FOOTER

- Background: escuro ou claro (verificar)
- Layout: 3-4 colunas
- Links: font 14px, color cinza
- Copyright na base

---

## OBSERVAÇÕES FEMINNITA

1. **Fonte substituta**: Angè usa "Muli Regular" (Google Fonts: Muli). Feminnita usa Montserrat — visual muito similar.
2. **Parcelamento**: Feminnita = **3x sem juros** (Angè usa 10x). Fórmula: `(preço / 3).toFixed(2)`
3. **PIX**: Angè mostra preço com desconto PIX. Feminnita: mostrar preço direto como "PIX ou Boleto"
4. **Preço antigo**: riscado acima do preço principal (se `precoAntigo` existir)
5. **Badge**: posição absolute no canto superior esquerdo da figura. Sem border-radius, fundo #8C2F39, texto branco, 11px uppercase
6. **Hero**: por ora usar apenas imagens (sem vídeo) — banco de imagens Unsplash. Vídeo pode ser adicionado depois.
7. **Cores swatches**: bolinhas de cor (8px) podem ser omitidas na vitrine, presentes apenas no PDP
