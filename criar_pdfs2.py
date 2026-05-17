# -*- coding: utf-8 -*-
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas as rl_canvas

BORGONHA     = colors.HexColor('#8C2F39')
BORGONHA_ESC = colors.HexColor('#5C1A22')
CHAMPAGNE    = colors.HexColor('#D4A956')
CREME        = colors.HexColor('#FAF6F2')
BRANCO       = colors.white
PRETO        = colors.HexColor('#1A1A1A')
VERDE_WA     = colors.HexColor('#2E7D32')
VERDE_WA_BG  = colors.HexColor('#E8F5E9')

OUTPUT = r"C:\Users\chris\Downloads\BLOG\downloads"
os.makedirs(OUTPUT, exist_ok=True)

W, H = A4

def draw_header(c, titulo_pdf):
    c.setFillColor(BORGONHA)
    c.rect(0, H - 16*mm, W, 16*mm, fill=1, stroke=0)
    c.setFillColor(CHAMPAGNE)
    c.rect(0, H - 16*mm, W, 2*mm, fill=1, stroke=0)
    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(W/2, H - 11*mm, titulo_pdf)

def draw_footer(c, page_num):
    c.setFillColor(BORGONHA)
    c.rect(0, 0, W, 10*mm, fill=1, stroke=0)
    c.setFillColor(BRANCO)
    c.setFont("Helvetica", 8)
    c.drawString(15*mm, 3.5*mm, "Feminnita  |  blog.feminnita.com.br  |  Material gratuito")
    c.drawRightString(W - 15*mm, 3.5*mm, f"Pagina {page_num}")

def draw_capa(c, titulo, subtitulo, icone):
    c.setFillColor(BORGONHA_ESC)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(CHAMPAGNE)
    c.rect(0, H - 6*mm, W, 6*mm, fill=1, stroke=0)
    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 26)
    c.drawCentredString(W/2, H - 38*mm, "Feminnita")
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor('#AAAAAA'))
    c.drawCentredString(W/2, H - 46*mm, "BLOG  |  Nova Friburgo, RJ")
    c.setStrokeColor(CHAMPAGNE)
    c.setLineWidth(1.5)
    c.line(W/2 - 25*mm, H - 51*mm, W/2 + 25*mm, H - 51*mm)
    c.setFont("Helvetica", 44)
    c.setFillColor(CHAMPAGNE)
    c.drawCentredString(W/2, H - 80*mm, icone)
    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 19)
    words = titulo.split()
    lines, line = [], []
    for w in words:
        line.append(w)
        if len(' '.join(line)) > 30:
            lines.append(' '.join(line[:-1]))
            line = [w]
    if line:
        lines.append(' '.join(line))
    y = H - 105*mm
    for ln in lines:
        c.drawCentredString(W/2, y, ln)
        y -= 11*mm
    c.setFont("Helvetica", 11)
    c.setFillColor(CHAMPAGNE)
    words2 = subtitulo.split()
    lines2, line2 = [], []
    for w in words2:
        line2.append(w)
        if len(' '.join(line2)) > 42:
            lines2.append(' '.join(line2[:-1]))
            line2 = [w]
    if line2:
        lines2.append(' '.join(line2))
    y2 = y - 6*mm
    for ln in lines2:
        c.drawCentredString(W/2, y2, ln)
        y2 -= 8*mm
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor('#888888'))
    c.drawCentredString(W/2, 18*mm, "blog.feminnita.com.br  |  Material 100% gratuito")

def wrap_text(text, max_chars):
    words = text.split()
    lines, line = [], []
    for w in words:
        line.append(w)
        if len(' '.join(line)) > max_chars:
            lines.append(' '.join(line[:-1]))
            line = [w]
    if line:
        lines.append(' '.join(line))
    return lines

# ═══════════════════════════════════════════════
# PDF 1 — CALENDÁRIO
# ═══════════════════════════════════════════════
def criar_calendario():
    path = os.path.join(OUTPUT, "calendario-datas-2026.pdf")
    c = rl_canvas.Canvas(path, pagesize=A4)

    draw_capa(c, "Calendario de Datas Sazonais 2026", "As datas que movem as vendas de pijamas suede - com estrategias de abordagem", "📅")
    c.showPage()

    meses = [
        ("JANEIRO", "Liquidacao pos-festas", "Conjuntos suede / pecas avulsas", "1a semana do mes", "Oi [nome]! Comecei o ano com novidades! Veja os lancamentos Feminnita com preco especial"),
        ("FEVEREIRO", "Carnaval", "Pijamas confortaveis para viagem e descanso", "2 semanas antes", "Carnaval chegando! Nada melhor que um pijama suede macio para descansar entre os blocos"),
        ("MARCO", "Dia da Mulher (8/3) ESTRELA", "Kits especiais - camisola + robe suede", "3 semanas antes", "O Dia da Mulher esta chegando! Que tal se presentear com um pijama suede Feminnita?"),
        ("ABRIL", "Pascoa - Kits Presente", "Kit presenteavel: pijama + embalagem kraft", "3 semanas antes", "Pascoa diferente! Alem do chocolate, um kit pijama suede Feminnita para presentear"),
        ("MAIO", "Dia das Maes (11/5) - DATA OURO", "Todos os modelos - kits premium suede", "4 semanas antes", "Sua mae merece o melhor presente! Pijamas suede Feminnita - macio, quentinho e elegante"),
        ("JUNHO", "Dia dos Namorados (12/6) - DATA OURO", "Conjuntos suede + kits para ela", "4 semanas antes", "Surpreenda sua namorada no Dia dos Namorados com um pijama suede Feminnita!"),
        ("JULHO", "Ferias de Inverno", "Pijamas longos suede - foco no calor e conforto", "Inicio do mes", "No frio de julho, nada melhor que nosso pijama suede! Quentinho do jeito certo"),
        ("AGOSTO", "Dia dos Pais (10/8)", "Robes / conjuntos masculinos suede", "3 semanas antes", "Para o pai que merece conforto! Robe suede Feminnita - o presente que ele nao esperava"),
        ("SETEMBRO", "Inicio da Primavera", "Conjuntos mais leves, cores da estacao", "1a semana do mes", "A primavera chegou! Novos modelos Feminnita com as cores da estacao"),
        ("OUTUBRO", "Dia das Criancas (12/10)", "Pijamas infantis suede / presentes para maes", "3 semanas antes", "Dia das Criancas chegando! Que tal um pijama quentinho suede para os pequenos?"),
        ("NOVEMBRO", "Black Friday (ultima sexta) - DATA OURO", "Todos os modelos com desconto / kits", "2 semanas antes", "Black Friday Feminnita! Pijamas suede com condicoes especiais - nao vai perder, ne?"),
        ("DEZEMBRO", "Natal - DATA OURO + Ano Novo", "Kits presente premium - embalagem especial", "4 semanas antes", "O presente mais gostoso do Natal e um pijama suede Feminnita! Clientes ja reservando!"),
    ]

    page_num = 2
    CARDS_POR_PAG = 3
    card_h = 70*mm
    margin = 12*mm
    top_content = H - 22*mm

    for i, (mes, data, produto, quando, msg) in enumerate(meses):
        if i % CARDS_POR_PAG == 0:
            if i > 0:
                draw_footer(c, page_num)
                c.showPage()
                page_num += 1
            draw_header(c, "CALENDARIO DE DATAS SAZONAIS 2026 - FEMINNITA")
            y = top_content

        # Fundo do card
        c.setFillColor(CREME)
        c.roundRect(margin, y - card_h, W - 2*margin, card_h, 4*mm, fill=1, stroke=0)
        c.setStrokeColor(CHAMPAGNE)
        c.setLineWidth(1)
        c.roundRect(margin, y - card_h, W - 2*margin, card_h, 4*mm, fill=0, stroke=1)

        # Cabecalho do card
        c.setFillColor(BORGONHA)
        c.roundRect(margin, y - 13*mm, W - 2*margin, 13*mm, 4*mm, fill=1, stroke=0)
        c.rect(margin, y - 13*mm, W - 2*margin, 6*mm, fill=1, stroke=0)
        c.setFillColor(BRANCO)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(margin + 5*mm, y - 9*mm, mes)
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(CHAMPAGNE)
        c.drawRightString(W - margin - 5*mm, y - 9*mm, data)

        # Linhas de info
        yi = y - 19*mm
        for lbl, val in [("Produto:", produto), ("Quando divulgar:", quando)]:
            c.setFillColor(BORGONHA)
            c.setFont("Helvetica-Bold", 8.5)
            c.drawString(margin + 5*mm, yi, lbl)
            c.setFillColor(PRETO)
            c.setFont("Helvetica", 8.5)
            c.drawString(margin + 42*mm, yi, val)
            yi -= 7*mm

        # Box WhatsApp
        box_top = yi - 1*mm
        box_h = 20*mm
        c.setFillColor(VERDE_WA_BG)
        c.roundRect(margin + 3*mm, box_top - box_h, W - 2*margin - 6*mm, box_h, 2*mm, fill=1, stroke=0)
        c.setFillColor(VERDE_WA)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(margin + 7*mm, box_top - 5*mm, "Sugestao de mensagem WhatsApp:")
        c.setFillColor(PRETO)
        c.setFont("Helvetica", 8)
        linhas_msg = wrap_text(msg, 88)
        for li, ln in enumerate(linhas_msg[:2]):
            c.drawString(margin + 7*mm, box_top - 11*mm - li*6*mm, ln)

        y -= card_h + 4*mm

    draw_footer(c, page_num)
    c.save()
    print(f"OK: {path}")

criar_calendario()

# ═══════════════════════════════════════════════
# PDF 2 — 50 MENSAGENS WHATSAPP
# ═══════════════════════════════════════════════
def criar_mensagens():
    path = os.path.join(OUTPUT, "50-mensagens-whatsapp.pdf")
    c = rl_canvas.Canvas(path, pagesize=A4)

    draw_capa(c, "50 Mensagens Prontas para WhatsApp", "Scripts testados por revendedoras reais para vender pijamas suede Feminnita", "💬")
    c.showPage()

    categorias = [
        ("Abordagem Inicial", "Primeiro contato com cliente novo", [
            "Oi [nome]! Tudo bem? Sou [seu nome] e trabalho com pijamas suede Feminnita, fabricado em Nova Friburgo, RJ. Posso te mostrar algumas opcoes?",
            "Ola [nome]! Vi que voce curte moda conforto. Trabalho com pijamas suede de fabrica - qualidade incrivel com preco de atacado. Posso mandar algumas fotos?",
            "Oi [nome]! Indicacao da [nome amiga]. Trabalho com pijamas suede Feminnita - macio, quentinho, elegante. Tenho modelos lindos pra te mostrar!",
            "Ola! Sou revendedora Feminnita, pijamas suede direto de fabrica (Nova Friburgo). Qualidade premium, preco justo. Posso te mandar o catalogo?",
            "Oi [nome]! Tudo bem? Voce ja conhece os pijamas suede Feminnita? Sao incriveis! Posso te mostrar os modelos mais vendidos?",
        ]),
        ("Apresentacao do Produto", "Descrever o suede e a qualidade Feminnita", [
            "O suede e um tecido premium - incrivelmente macio, quentinho e com um caimento elegante. Uma vez que voce experimenta, nao quer mais saber de outro!",
            "Os pijamas Feminnita sao fabricados com suede de alta qualidade. Lavavel na maquina, nao deforma, nao desfia. Dura muito mais que pijama comum.",
            "Olha que detalhe: o suede Feminnita fica mais macio a cada lavagem! E o tecido que suas clientes vao amar e recomendar pra todo mundo.",
            "Sobre a qualidade: Feminnita fabrica em Nova Friburgo, RJ, com controle rigoroso de qualidade. E por isso que nossas revendedoras tem pouquissimas trocas.",
            "O diferencial do suede e a sensacao na pele. Nao e grossa como moletom, nem fina como malha. E no ponto certo - macio, encorpado, perfeito pra dormir.",
            "Tenho modelos femininos em varios tamanhos (P ao GG). As cores sao escolhidas toda estacao - sempre modernas e elegantes.",
            "Os kits sao uma opcao incrivel: camisola + robe suede numa embalagem presenteavel. Seus clientes amam receber como presente!",
            "Posso te mandar um video mostrando a textura do tecido? Voce vai entender por que as clientes amam tanto o suede Feminnita.",
        ]),
        ("Dia das Maes", "Mensagens especiais para maio", [
            "Dia das Maes chegando! Sua mae merece um presente especial. Pijama suede Feminnita - macio, elegante e quentinho. Posso montar um kit presenteavel pra voce?",
            "Oi [nome]! Ja pensou no presente da sua mae? Um kit pijama suede Feminnita com embalagem caprichada - ela vai amar! Tenho opcoes de R$80 a R$250.",
            "Presente de Dia das Maes: pijama suede Feminnita. Preco justo, qualidade premium, embalagem linda. Sua mae vai se sentir uma rainha!",
            "Faltam [X] dias pro Dia das Maes! Ainda da tempo de garantir um kit suede Feminnita. Embalagem presenteavel incluida, entrega ate o dia 10/5.",
            "Para a mae que gosta de conforto: pijama suede Feminnita. Para a mae que gosta de elegancia: pijama suede Feminnita. Pra todo tipo de mae!",
            "Ultimo dia para garantir o kit Dia das Maes! Pijama suede Feminnita com embalagem presenteavel. Me chame agora que ainda consigo entregar a tempo!",
        ]),
        ("Dia dos Namorados", "Mensagens para junho", [
            "Dia dos Namorados em [data]! Que tal surpreender com um pijama suede Feminnita? Elegante, macio e diferente de tudo que ela ja recebeu.",
            "Presente diferente pro Dia dos Namorados: kit pijama suede Feminnita. Ela vai usar todo dia e lembrar de voce com carinho!",
            "Oi [nome]! Ja pensou no presente da namorada? Conjunto suede Feminnita - um presente que ela vai realmente usar e adorar. Posso montar um kit especial?",
            "Para quem nao sabe o que dar no Dia dos Namorados: pijama suede Feminnita! Presente pratico, bonito e que ela realmente vai usar. Posso te ajudar a escolher?",
            "Ela ja falou que queria um pijama gostoso? Entao ta! Kit suede Feminnita com embalagem presenteavel - o presente que ela queria e voce vai dar!",
        ]),
        ("Natal", "Mensagens para dezembro", [
            "Natal chegando! Kit pijama suede Feminnita - o presente que todo mundo quer receber. Mainho, quentinho e com embalagem linda. Encomende ja!",
            "Para o amigo secreto, para a mae, para a irma - pijama suede Feminnita e presenca certa no Natal! Varios modelos e faixas de preco.",
            "Ceia de Natal + pijama suede novo = Natal perfeito! Kits Feminnita a partir de R$80. Posso montar seu pedido?",
            "Oi [nome]! Natal eh daqui [X] dias. Ainda da tempo de garantir kits suede Feminnita com embalagem de presente. Posso te ajudar a montar?",
            "Presenteie com o que ela realmente vai usar! Kit pijama suede Feminnita - elegante, macio, quentinho. Perfeito pro inverno e pras noites frias.",
        ]),
        ("Follow-up e Recuperacao", "Para clientes que nao responderam", [
            "Oi [nome]! Estou por aqui caso queira ver os pijamas suede. Acabou de chegar uma nova colecao - posso te mandar as fotos?",
            "Oi [nome]! Lembra que conversamos sobre os pijamas suede? Queria saber se voce teve alguma duvida que eu possa ajudar.",
            "Ola [nome]! So passando pra avisar que o modelo que voce gostou ainda tem no estoque, mas esta acabando. Posso reservar pra voce?",
            "Oi [nome]! Tudo bem? Fiz um kit novo que lembrei de voce - posso te mandar a foto? Acho que vai gostar!",
            "Oi [nome]! Chegaram cores novas de suede aqui. Sei que voce gosta de [cor/modelo]. Posso te mostrar?",
            "Ola [nome]! Tenho uma promocao especial essa semana. Lembrei de voce! Posso te mandar os detalhes?",
        ]),
        ("Pos-venda e Fidelizacao", "Agradecer e pedir indicacao", [
            "Oi [nome]! Como voce esta gostando do pijama suede? Ele fica ainda mais macio apos a lavagem! Qualquer duvida, estou aqui.",
            "Ola [nome]! Faz um tempo que compramos juntas. Tem alguma amiga que adoraria conhecer os pijamas suede Feminnita? Indicacao sua tem desconto especial!",
            "Voce indicou [nome] e ela comprou! Muito obrigada! Como combinei, voce tem um desconto especial na proxima compra.",
            "Oi [nome]! Obrigada pela confianca de sempre! Sao clientes como voce que fazem esse trabalho valer a pena. Tem algo novo que posso te mostrar?",
            "Lembrei de voce porque chegou um modelo novo que combina muito com seu estilo! Posso mandar a foto?",
            "Oi [nome]! Minha lista de melhores clientes do mes - e voce esta nela! Tenho uma condicao especial so pra voce essa semana.",
            "Obrigada pela compra, [nome]! Se voce gostar, conta pra suas amigas. Cada indicacao que vira cliente, voce ganha um mimo especial!",
        ]),
        ("Contornando Objecoes", "Para 'ta caro' e 'vou pensar'", [
            "Entendo! O suede parece mais caro mesmo a primeira vista. Mas pensa: voce vai usar todo dia por anos. Da pra R$0,50 por uso. Vale muito!",
            "Faz sentido querer pensar! So lembrando que o estoque e limitado e esse modelo pode acabar. Se quiser, posso reservar por 24h sem compromisso.",
            "Eu mesma achei caro antes de comprar o meu. Depois que experimentei o suede Feminnita, entendi o preco. A qualidade e incomparavel!",
            "Posso te mostrar uma opcao mais em conta? Tenho kits a partir de R$80 que sao incriveis. Qual e sua faixa de preco confortavel?",
            "Claro, pensa com calma! Mas se ajudar: tenho opcao de 2x sem juros pelo pix. Fica mais facil assim!",
            "A diferenca de preco do suede pra um pijama comum e pequena, mas a diferenca de qualidade e enorme. Voce sente na primeira noite!",
            "Que tal ver o suede pessoalmente antes? Posso te levar uma amostra do tecido sem compromisso. Depois voce decide com mais seguranca.",
            "Entendo a duvida! Posso te contar que 90% das minhas clientes que compram uma peca voltam pra comprar mais. O suede fideliza muito!",
        ]),
    ]

    page_num = 2
    margin = 15*mm
    MSG_POR_PAG = 6

    for cat_idx, (cat_nome, cat_desc, msgs) in enumerate(categorias):
        # Cabecalho de categoria - nova pagina
        draw_header(c, "50 MENSAGENS PRONTAS PARA WHATSAPP - FEMINNITA")
        y = H - 22*mm

        # Titulo da categoria
        c.setFillColor(BORGONHA)
        c.rect(margin, y - 14*mm, W - 2*margin, 14*mm, fill=1, stroke=0)
        c.setFillColor(BRANCO)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(margin + 5*mm, y - 9*mm, f"Categoria: {cat_nome}")
        c.setFillColor(CHAMPAGNE)
        c.setFont("Helvetica", 10)
        c.drawRightString(W - margin - 5*mm, y - 9*mm, cat_desc)
        y -= 18*mm

        for msg_idx, msg in enumerate(msgs):
            msg_num = sum(len(categorias[ci][2]) for ci in range(cat_idx)) + msg_idx + 1
            box_h = 22*mm
            c.setFillColor(CREME)
            c.roundRect(margin, y - box_h, W - 2*margin, box_h, 3*mm, fill=1, stroke=0)
            c.setStrokeColor(CHAMPAGNE)
            c.setLineWidth(0.8)
            c.roundRect(margin, y - box_h, W - 2*margin, box_h, 3*mm, fill=0, stroke=1)
            # Numero
            c.setFillColor(BORGONHA)
            c.circle(margin + 8*mm, y - box_h/2, 5*mm, fill=1, stroke=0)
            c.setFillColor(BRANCO)
            c.setFont("Helvetica-Bold", 9)
            c.drawCentredString(margin + 8*mm, y - box_h/2 - 2.5*mm, str(msg_num))
            # Texto
            c.setFillColor(PRETO)
            c.setFont("Helvetica", 8.5)
            linhas = wrap_text(msg, 90)
            text_y = y - 7*mm
            for ln in linhas[:3]:
                c.drawString(margin + 16*mm, text_y, ln)
                text_y -= 6*mm
            y -= box_h + 3*mm

            if msg_idx < len(msgs) - 1 and y < 25*mm:
                draw_footer(c, page_num)
                c.showPage()
                page_num += 1
                draw_header(c, "50 MENSAGENS PRONTAS PARA WHATSAPP - FEMINNITA")
                y = H - 22*mm

        draw_footer(c, page_num)
        c.showPage()
        page_num += 1

    c.save()
    print(f"OK: {path}")

criar_mensagens()

# ═══════════════════════════════════════════════
# PDF 3 — PRECIFICACAO
# ═══════════════════════════════════════════════
def criar_precificacao():
    path = os.path.join(OUTPUT, "planilha-precificacao.pdf")
    c = rl_canvas.Canvas(path, pagesize=A4)

    draw_capa(c, "Guia de Precificacao e Lucro", "Calcule o preco ideal e saiba exatamente quanto voce vai lucrar com seus pijamas suede", "💰")
    c.showPage()

    # Pagina 2 — Explicacao e formula
    draw_header(c, "GUIA DE PRECIFICACAO E LUCRO - FEMINNITA")
    y = H - 25*mm
    margin = 15*mm

    def titulo_secao(c, texto, y):
        c.setFillColor(BORGONHA)
        c.rect(margin, y - 10*mm, W - 2*margin, 10*mm, fill=1, stroke=0)
        c.setFillColor(BRANCO)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(margin + 5*mm, y - 7*mm, texto)
        return y - 14*mm

    def texto(c, linha, y, bold=False, cor=PRETO, tamanho=9):
        c.setFillColor(cor)
        c.setFont("Helvetica-Bold" if bold else "Helvetica", tamanho)
        c.drawString(margin + 5*mm, y, linha)
        return y - 6.5*mm

    y = titulo_secao(c, "1. Os 4 componentes do preco", y)
    itens = [
        ("Custo do produto:", "Valor que voce paga pelo pijama no atacado Feminnita"),
        ("Frete:", "Custo de envio ao comprar o lote (divida pelo numero de pecas)"),
        ("Embalagem:", "Saco, papel seda, caixa, lacos, tags - calcule por peca"),
        ("Margem de lucro:", "O percentual de ganho sobre o preco de venda (minimo 40%)"),
    ]
    for titulo_item, desc in itens:
        c.setFillColor(CHAMPAGNE)
        c.circle(margin + 8*mm, y + 1*mm, 2.5*mm, fill=1, stroke=0)
        c.setFillColor(BORGONHA)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(margin + 13*mm, y, titulo_item)
        c.setFillColor(PRETO)
        c.setFont("Helvetica", 9)
        c.drawString(margin + 13*mm + len(titulo_item)*5.5, y, desc)
        y -= 8*mm

    y -= 5*mm
    y = titulo_secao(c, "2. A Formula do Markup", y)
    c.setFillColor(colors.HexColor('#FFF8E1'))
    c.roundRect(margin + 10*mm, y - 22*mm, W - 2*margin - 20*mm, 22*mm, 3*mm, fill=1, stroke=0)
    c.setStrokeColor(CHAMPAGNE)
    c.setLineWidth(1.5)
    c.roundRect(margin + 10*mm, y - 22*mm, W - 2*margin - 20*mm, 22*mm, 3*mm, fill=0, stroke=1)
    c.setFillColor(BORGONHA)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(W/2, y - 8*mm, "Preco de Venda = Custo Total / (1 - Margem)")
    c.setFillColor(CINZA)
    c.setFillColor(colors.HexColor('#555555'))
    c.setFont("Helvetica", 9)
    c.drawCentredString(W/2, y - 17*mm, "Exemplo: custo R$45, margem 50% -> R$45 / (1 - 0,50) = R$90 de preco de venda")
    y -= 28*mm

    y = titulo_secao(c, "3. Tabela de Precificacao Sugerida - Pecas Avulsas", y)
    c.setFillColor(BORGONHA)
    c.rect(margin, y - 10*mm, W - 2*margin, 10*mm, fill=1, stroke=0)
    col_w = [(W - 2*margin) / 4] * 4
    headers = ["Peca", "Custo Medio", "Preco Sugerido", "Lucro por Peca"]
    for hi, h_txt in enumerate(headers):
        x_col = margin + sum(col_w[:hi])
        c.setFillColor(BRANCO)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(x_col + col_w[hi]/2, y - 7*mm, h_txt)
    y -= 10*mm
    rows = [
        ("Camisola suede", "R$ 38 - 48", "R$ 80 - 95", "R$ 35 - 45"),
        ("Conjunto curto suede", "R$ 45 - 55", "R$ 90 - 110", "R$ 40 - 55"),
        ("Pijama longo suede", "R$ 55 - 70", "R$ 110 - 140", "R$ 50 - 70"),
        ("Robe suede", "R$ 60 - 75", "R$ 120 - 150", "R$ 55 - 70"),
    ]
    for ri, row in enumerate(rows):
        bg = CREME if ri % 2 == 0 else BRANCO
        c.setFillColor(bg)
        c.rect(margin, y - 9*mm, W - 2*margin, 9*mm, fill=1, stroke=0)
        for ci, cell in enumerate(row):
            x_col = margin + sum(col_w[:ci])
            c.setFillColor(BORGONHA if ci == 0 else PRETO)
            c.setFont("Helvetica-Bold" if ci == 0 else "Helvetica", 9)
            c.drawCentredString(x_col + col_w[ci]/2, y - 6*mm, cell)
        y -= 9*mm
    y -= 8*mm

    y = titulo_secao(c, "4. Tabela de Kits - Por que o Kit tem Margem Maior", y)
    c.setFillColor(BORGONHA)
    c.rect(margin, y - 10*mm, W - 2*margin, 10*mm, fill=1, stroke=0)
    col_w2 = [(W - 2*margin) / 4] * 4
    h2 = ["Kit", "Custo Total", "Preco Sugerido", "Lucro do Kit"]
    for hi, h_txt in enumerate(h2):
        x_col = margin + sum(col_w2[:hi])
        c.setFillColor(BRANCO)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(x_col + col_w2[hi]/2, y - 7*mm, h_txt)
    y -= 10*mm
    kits = [
        ("Kit Essencial (camisola)", "R$ 48 - 58", "R$ 99 - 120", "R$ 45 - 60"),
        ("Kit Mimo (conj.+ caixa)", "R$ 60 - 75", "R$ 130 - 160", "R$ 65 - 85"),
        ("Kit Premium (3 pecas)", "R$ 95 - 120", "R$ 200 - 250", "R$ 100 - 130"),
    ]
    for ri, row in enumerate(kits):
        bg = colors.HexColor('#F3E8FF') if ri % 2 == 0 else BRANCO
        c.setFillColor(bg)
        c.rect(margin, y - 9*mm, W - 2*margin, 9*mm, fill=1, stroke=0)
        for ci, cell in enumerate(row):
            x_col = margin + sum(col_w2[:ci])
            c.setFillColor(BORGONHA if ci == 0 else PRETO)
            c.setFont("Helvetica-Bold" if ci == 0 else "Helvetica", 9)
            c.drawCentredString(x_col + col_w2[ci]/2, y - 6*mm, cell)
        y -= 9*mm

    draw_footer(c, 2)
    c.showPage()

    # Pagina 3 — Calculadora + Dicas
    draw_header(c, "GUIA DE PRECIFICACAO E LUCRO - FEMINNITA")
    y = H - 25*mm

    y = titulo_secao(c, "5. Sua Calculadora (preencha a mao!)", y)
    linhas_calc = [
        ("Peca / produto:", "________________"),
        ("Custo do produto (R$):", "________________"),
        ("Frete rateado por peca (R$):", "________________"),
        ("Embalagem por peca (R$):", "________________"),
        ("CUSTO TOTAL = soma dos itens acima:", "________________"),
        ("Margem desejada (ex: 50% = 0,50):", "________________"),
        ("PRECO DE VENDA = custo / (1 - margem):", "________________"),
        ("Lucro por peca = preco - custo:", "________________"),
    ]
    for lbl, campo in linhas_calc:
        c.setFillColor(BORGONHA if 'CUSTO TOTAL' in lbl or 'PRECO' in lbl else PRETO)
        c.setFont("Helvetica-Bold" if 'CUSTO TOTAL' in lbl or 'PRECO' in lbl else "Helvetica", 9)
        c.drawString(margin + 5*mm, y, lbl)
        c.setFillColor(CINZA)
        c.setFillColor(colors.HexColor('#AAAAAA'))
        c.setFont("Helvetica", 9)
        c.drawRightString(W - margin - 5*mm, y, campo)
        c.setStrokeColor(colors.HexColor('#DDDDDD'))
        c.setLineWidth(0.5)
        c.line(margin + 5*mm, y - 2*mm, W - margin - 5*mm, y - 2*mm)
        y -= 10*mm

    y -= 5*mm
    y = titulo_secao(c, "6. Dicas para Nao Errar na Precificacao", y)
    dicas = [
        "Sempre inclua o frete no custo - divida o valor total do frete pelo numero de pecas do pedido",
        "Embalagem conta! Saco plastico, papel seda, caixa kraft, laco: some tudo e divida por peca",
        "Margem minima recomendada: 40%. Abaixo disso, voce perde dinheiro com imprevistos",
        "Kit sempre tem margem maior: o cliente percebe mais valor e paga mais, mesmo que o custo extra seja pequeno",
        "Nao compare seu preco com o de bazares: suede Feminnita e qualidade premium - cobre o valor justo",
        "Revisao de preco: atualize seus precos a cada pedido novo, conforme variacoes de custo e frete",
        "Preco psicologico funciona: R$99 vende mais que R$100, R$119 mais que R$120",
    ]
    for di, dica in enumerate(dicas):
        c.setFillColor(CHAMPAGNE)
        c.circle(margin + 8*mm, y + 1.5*mm, 3*mm, fill=1, stroke=0)
        c.setFillColor(BORGONHA_ESC)
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(margin + 8*mm, y - 0.5*mm, str(di + 1))
        c.setFillColor(PRETO)
        c.setFont("Helvetica", 8.5)
        linhas_dica = wrap_text(dica, 90)
        for li, ln in enumerate(linhas_dica[:2]):
            c.drawString(margin + 14*mm, y - li*6*mm, ln)
        y -= (len(linhas_dica[:2]) * 6 + 5)*mm

    draw_footer(c, 3)
    c.save()
    print(f"OK: {path}")

criar_precificacao()
print("TODOS OS PDFs CRIADOS!")
