import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

out_dir = 'public/images'
os.makedirs(out_dir, exist_ok=True)

font_bold = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
font_reg = '/System/Library/Fonts/Supplemental/Arial.ttf'
font_italic = '/System/Library/Fonts/Supplemental/Arial Italic.ttf'
font_bold_italic = '/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf'
font_treb = '/System/Library/Fonts/Supplemental/Trebuchet MS Bold.ttf'
font_georgia = '/System/Library/Fonts/Supplemental/Georgia.ttf'
font_georgia_bold = '/System/Library/Fonts/Supplemental/Georgia Bold.ttf'
font_verdana = '/System/Library/Fonts/Supplemental/Verdana.ttf'
font_verdana_bold = '/System/Library/Fonts/Supplemental/Verdana Bold.ttf'

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def wrap_text(draw, text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = []
    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    return lines

def draw_checkmark(draw, x, y, size=20, color='#3b82f6', width=3):
    # checkmark shape
    p1 = (x, y + size * 0.5)
    p2 = (x + size * 0.35, y + size * 0.85)
    p3 = (x + size * 0.9, y + size * 0.15)
    draw.line([p1, p2], fill=color, width=width)
    draw.line([p2, p3], fill=color, width=width)

def draw_double_checkmarks(draw, x, y, size=18, color='#3b82f6', width=3):
    draw_checkmark(draw, x, y, size, color, width)
    draw_checkmark(draw, x + size * 0.45, y, size, color, width)

def draw_heart(draw, cx, cy, size=20, color='#ef4444'):
    # Vector heart
    r = size // 2
    # Left and right circles
    draw.ellipse([cx - r, cy - r//2, cx, cy + r//2], fill=color)
    draw.ellipse([cx, cy - r//2, cx + r, cy + r//2], fill=color)
    # Triangle bottom
    draw.polygon([(cx - r + 1, cy), (cx + r - 1, cy), (cx, cy + r)], fill=color)

def draw_cross_mark(draw, cx, cy, size=20, color='#dc2626', width=4):
    r = size // 2
    draw.line([(cx - r, cy - r), (cx + r, cy + r)], fill=color, width=width)
    draw.line([(cx + r, cy - r), (cx - r, cy + r)], fill=color, width=width)

def draw_avatar_badge(draw, cx, cy, r, text, bg_color, text_color='#ffffff'):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=bg_color)
    f = get_font(font_bold, int(r * 0.9))
    bbox = draw.textbbox((0, 0), text, font=f)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((cx - tw//2, cy - th//2 - 2), text, font=f, fill=text_color)

def draw_star(draw, cx, cy, r, color='#facc15'):
    points = []
    for i in range(10):
        angle = i * math.pi / 5 - math.pi / 2
        radius = r if i % 2 == 0 else r * 0.45
        px = cx + radius * math.cos(angle)
        py = cy + radius * math.sin(angle)
        points.append((px, py))
    draw.polygon(points, fill=color)

# ==========================================
# 1. COMPARISON LEFT: ITALIAN SCHOOL TEST SHEET
# ==========================================
def generate_italian_test_sheet():
    w, h = 1024, 600
    img = Image.new('RGB', (w, h), color='#fbfbf8')
    draw = ImageDraw.Draw(img)
    
    # Notebook lined paper background
    for y in range(45, h, 38):
        draw.line([(30, y), (w-30, y)], fill='#e2e8f0', width=1)
    
    # Red margin line
    draw.line([(130, 20), (130, h-20)], fill='#f87171', width=2)
    
    # Header box on test paper
    draw.rectangle([150, 45, w-50, 225], outline='#475569', width=2, fill='#ffffff')
    
    f_header = get_font(font_bold, 32)
    draw.text((175, 65), 'VERIFICA DI ITALIANO', font=f_header, fill='#1e293b')
    
    f_meta = get_font(font_reg, 26)
    draw.text((175, 115), 'Classe: 2ª Primaria     Sezione: B', font=f_meta, fill='#475569')
    draw.text((175, 160), 'Alunno: _______________________', font=f_meta, fill='#475569')
    
    # Red Grade Box
    draw.rectangle([w-310, 60, w-70, 210], outline='#dc2626', width=2, fill='#fef2f2')
    draw.text((w-290, 75), 'VOTO:', font=get_font(font_bold, 28), fill='#991b1b')
    
    f_grade = get_font(font_treb, 72)
    draw.text((w-190, 75), '4', font=f_grade, fill='#dc2626')
    
    f_note = get_font(font_bold_italic, 24)
    draw.text((w-290, 160), '(Non sufficiente)', font=f_note, fill='#dc2626')
    
    # Question 1
    f_ex_title = get_font(font_bold, 26)
    draw.text((150, 255), 'Esercizio 1: Leggi il brano e rispondi alla domanda.', font=f_ex_title, fill='#1e293b')
    
    f_ex_text = get_font(font_georgia, 24)
    draw.text((150, 300), '«Il piccolo scoiattolo raccoglieva le ghiande nel bosco prima dell\'inverno...»', font=f_ex_text, fill='#334155')
    
    draw.text((150, 360), 'Domanda: Perché lo scoiattolo raccoglie le ghiande?', font=get_font(font_bold, 24), fill='#1e293b')
    
    # Student Wrong Answer with drawn red cross
    draw_cross_mark(draw, 165, 415, size=24, color='#dc2626', width=4)
    draw.text((190, 402), 'Risposta: Non lo so / Non ho capito il testo', font=get_font(font_italic, 24), fill='#64748b')
    
    # Teacher feedback banner
    draw.rounded_rectangle([150, 460, w-50, 520], radius=8, fill='#fee2e2', outline='#f87171', width=1)
    draw_cross_mark(draw, 175, 490, size=20, color='#dc2626', width=3)
    draw.text((195, 477), 'Nota dell\'insegnante: Testo non compreso. Rileggere con attenzione!', font=get_font(font_bold_italic, 22), fill='#b91c1c')
    
    res = img.resize((512, 300), Image.Resampling.LANCZOS)
    res.save(os.path.join(out_dir, 'eb3fee05-db30-4bd8-8399-9b02593f5a96-misc-src.png'))
    res.save(os.path.join(out_dir, 'eb3fee05-db30-4bd8-8399-9b02593f5a96-misc-src_2.png'))
    res.resize((300, 176), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'eb3fee05-db30-4bd8-8399-9b02593f5a96-misc-src_1.png'))
    print('Generated Italian Test Sheet (eb3fee05)')

# ==========================================
# 2. COMPARISON RIGHT: ITALIAN WHATSAPP BUBBLE
# ==========================================
def generate_italian_whatsapp_bubble():
    w, h = 1024, 600
    img = Image.new('RGB', (w, h), color='#efeae2')
    draw = ImageDraw.Draw(img)
    
    # WhatsApp message bubble
    draw.rounded_rectangle([35, 35, w-35, h-35], radius=28, fill='#ffffff')
    draw.polygon([(35, 80), (15, 60), (35, 100)], fill='#ffffff')
    
    f_msg = get_font(font_reg, 32)
    line_spacing = 48
    lines = [
        "Ho iniziato a usare le schede con mio",
        "figlio la settimana scorsa e ho già notato",
        "una grande differenza. Prima si bloccava su",
        "qualsiasi testo, si innervosiva e diceva che non",
        "capiva nulla. Ora legge, risponde alle domande",
        "e mi chiama persino per farmi vedere cosa è riuscito",
        "a fare da solo. Non l'avevo mai visto così sicuro di sé!"
    ]
    
    for i, line in enumerate(lines):
        draw.text((65, 65 + i * line_spacing), line, font=f_msg, fill='#111827')
        
    f_time = get_font(font_reg, 26)
    draw.text((w-165, h-75), '19:00', font=f_time, fill='#6b7280')
    draw_double_checkmarks(draw, w-90, h-70, size=20, color='#3b82f6', width=3)
    
    res = img.resize((512, 300), Image.Resampling.LANCZOS)
    res.save(os.path.join(out_dir, 'dc4fa02a-691a-42a1-9a5c-26446c7bc6f6-misc-src.png'))
    res.save(os.path.join(out_dir, 'dc4fa02a-691a-42a1-9a5c-26446c7bc6f6-misc-src_1.png'))
    res.resize((300, 176), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'dc4fa02a-691a-42a1-9a5c-26446c7bc6f6-misc-src_2.png'))
    print('Generated Italian WhatsApp Bubble (dc4fa02a)')

# ==========================================
# 3. STEP 1 - ITALIAN MEMBER PLATFORM MOCKUP
# ==========================================
def generate_italian_member_platform():
    w, h = 1024, 630
    img = Image.new('RGB', (w, h), color='#131826')
    draw = ImageDraw.Draw(img)
    
    # Top navbar
    draw.rectangle([0, 0, w, 80], fill='#1e293b')
    draw.text((40, 24), 'KIT COMPRENSIONE DEL TESTO 2.0  ·  AREA FAMIGLIE', font=get_font(font_bold, 24), fill='#ffffff')
    draw.rounded_rectangle([w-230, 18, w-30, 62], radius=12, fill='#3b82f6')
    draw.text((w-205, 27), 'SCARICA I FILE', font=get_font(font_bold, 18), fill='#ffffff')
    
    # Welcome banner
    draw.rounded_rectangle([40, 110, w-40, 210], radius=16, fill='#1e1b4b', outline='#6366f1', width=2)
    draw.text((70, 130), 'Benvenuto nel Programma Didattico!', font=get_font(font_bold, 28), fill='#facc15')
    draw.text((70, 170), 'Scegli il modulo del giorno, scarica il PDF e inizia subito con tuo figlio.', font=get_font(font_reg, 20), fill='#e2e8f0')
    
    # 4 Modules cards
    modules = [
        ('MODULO 1', '150 Attività di Lettura Rapida', '#4361ee'),
        ('MODULO 2', '120 Testi & Domande Dirette', '#3a0ca3'),
        ('MODULO 3', '117 Esercizi di Vocabolario', '#7209b7'),
        ('MODULO 4', '200 Schede Interdisciplinari', '#0284c7')
    ]
    
    card_w = 215
    for i, (m_tag, m_title, m_color) in enumerate(modules):
        cx = 40 + i * (card_w + 30)
        cy = 240
        draw.rounded_rectangle([cx, cy, cx + card_w, cy + 340], radius=16, fill='#1f293d', outline=m_color, width=2)
        draw.rounded_rectangle([cx, cy, cx + card_w, cy + 60], radius=16, fill=m_color)
        draw.text((cx + 20, cy + 18), m_tag, font=get_font(font_bold, 20), fill='#ffffff')
        
        lines = wrap_text(draw, m_title, get_font(font_bold, 18), card_w - 30)
        for j, line in enumerate(lines):
            draw.text((cx + 15, cy + 85 + j * 26), line, font=get_font(font_bold, 18), fill='#ffffff')
            
        draw.rounded_rectangle([cx + 15, cy + 270, cx + card_w - 15, cy + 315], radius=10, fill='#22c55e')
        draw.text((cx + 35, cy + 282), 'SCARICA PDF', font=get_font(font_bold, 16), fill='#ffffff')
        
    res = img.resize((512, 315), Image.Resampling.LANCZOS)
    res.save(os.path.join(out_dir, 'bca575f3-70fc-4dca-a646-42e0af0d9f2f-misc-src.png'))
    res.save(os.path.join(out_dir, 'bca575f3-70fc-4dca-a646-42e0af0d9f2f-misc-src_2.png'))
    res.resize((300, 185), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'bca575f3-70fc-4dca-a646-42e0af0d9f2f-misc-src_1.png'))
    print('Generated Italian Member Platform (bca575f3)')

# ==========================================
# 4. STEP 3 - ITALIAN PRINT WORKSHEETS & ANSWERS
# ==========================================
def generate_italian_worksheets():
    w, h = 1024, 630
    img = Image.new('RGB', (w, h), color='#f8fafc')
    draw = ImageDraw.Draw(img)
    
    # Left sheet - Worksheet
    draw.rectangle([50, 40, 500, 590], fill='#ffffff', outline='#cbd5e1', width=2)
    draw.rectangle([50, 40, 500, 110], fill='#3b82f6')
    draw.text((70, 55), 'SCHEDA 1: IL PICCOLO SCOIATTOLO', font=get_font(font_bold, 20), fill='#ffffff')
    draw.text((70, 85), 'Comprensione del Testo · Scuola Primaria', font=get_font(font_reg, 16), fill='#e0f2fe')
    
    draw.text((70, 130), 'Leggi attentamente il testo e rispondi:', font=get_font(font_bold, 18), fill='#1e293b')
    story_lines = [
        "Nel fitto bosco di querce, lo scoiattolo Leo",
        "lavorava ogni giorno per raccogliere le provviste.",
        "Sapeva che l'inverno sarebbe arrivato presto e",
        "voleva proteggere la sua famiglia dal freddo..."
    ]
    for i, line in enumerate(story_lines):
        draw.text((70, 170 + i * 28), line, font=get_font(font_georgia, 17), fill='#334155')
        
    draw.text((70, 310), '1. Chi è il protagonista del racconto?', font=get_font(font_bold, 17), fill='#1e293b')
    draw.text((90, 345), 'A) Un leprotto     B) Lo scoiattolo Leo     C) Un orso', font=get_font(font_reg, 16), fill='#475569')
    
    draw.text((70, 400), '2. Perché raccoglie le provviste nel bosco?', font=get_font(font_bold, 17), fill='#1e293b')
    draw.text((90, 435), 'A) Per gioco       B) Per l\'inverno         C) Per viaggiare', font=get_font(font_reg, 16), fill='#475569')
    
    draw.rounded_rectangle([70, 500, 480, 550], radius=10, fill='#eff6ff', outline='#93c5fd', width=1)
    draw.text((90, 515), 'Valutazione: Ottimo lavoro di comprensione!', font=get_font(font_bold, 16), fill='#1d4ed8')
    
    # Right sheet - Answer Keys / Solutions for parents
    draw.rectangle([530, 40, 970, 590], fill='#ffffff', outline='#cbd5e1', width=2)
    draw.rectangle([530, 40, 970, 110], fill='#059669')
    draw.text((550, 55), 'SOLUZIONI COMPLETE PER I GENITORI', font=get_font(font_bold, 20), fill='#ffffff')
    draw.text((550, 85), 'Chiavi di Risposta Dettagliate · Modulo 1', font=get_font(font_reg, 16), fill='#d1fae5')
    
    solutions = [
        ("Scheda 1", "Domanda 1: B (Leo) | Domanda 2: B (Inverno)"),
        ("Scheda 2", "Domanda 1: C (Bosco) | Domanda 2: A (Amicizia)"),
        ("Scheda 3", "Domanda 1: A (Scienze) | Domanda 2: C (Natura)"),
        ("Scheda 4", "Domanda 1: B (Storia) | Domanda 2: B (Autonomia)"),
        ("Scheda 5", "Domanda 1: A (Vocabolario) | Domanda 2: A (Sinonimo)")
    ]
    
    for i, (sch, sol) in enumerate(solutions):
        sy = 140 + i * 80
        draw.rounded_rectangle([550, sy, 950, sy + 65], radius=8, fill='#f8fafc', outline='#e2e8f0', width=1)
        draw.text((565, sy + 10), f'{sch}', font=get_font(font_bold, 17), fill='#065f46')
        draw_checkmark(draw, 565 + 85, sy + 12, size=16, color='#059669', width=2)
        draw.text((565, sy + 35), sol, font=get_font(font_reg, 15), fill='#334155')
        
    res = img.resize((512, 315), Image.Resampling.LANCZOS)
    res.save(os.path.join(out_dir, 'mFPujI8456037.png'))
    res.save(os.path.join(out_dir, 'mFPujI8456037_1.png'))
    res.resize((300, 185), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'mFPujI8456037_2.png'))
    print('Generated Italian Worksheets & Solutions (mFPujI8456037)')

# ==========================================
# 5. BONUS CARDS (1 to 4) & HIGHLIGHTS
# ==========================================
def generate_italian_bonus_cards():
    cards = [
        ('ghnuyA5473914', 'BONUS 1', 'Kit Calligrafia Perfetta', 'Scrittura Chiara, Postura e Alfabeto (40 Pagine)', '#f72585'),
        ('zCyQDE5473914', 'BONUS 2', 'Ora di Lettura', '24 Testi Coinvolgenti per Bambini (42 Pagine)', '#4cc9f0'),
        ('cmIaGY5473914', 'BONUS 3', 'Matematica Semplificata', '120 Esercizi Pratici con Soluzioni (31 Pagine)', '#ffb703'),
        ('HpBKtY5473914', 'BONUS 4', 'Soluzioni & Certificato', 'Chiavi Complete per Genitori + Attestato Ufficiale', '#06d6a0'),
        
        ('gcdBCn5473914', 'BONUS INCLUSO', 'Kit Calligrafia Perfetta', 'Impugnatura Corretta, Lettere e Numeri', '#f72585'),
        ('vDHxvY5473914', 'BONUS INCLUSO', 'Matematica Semplificata', 'Addizioni, Tabelline e Problemi Pratici', '#2a9d8f')
    ]
    
    for base_name, tag, title, desc, color in cards:
        w, h = 512, 315
        img = Image.new('RGB', (w, h), color='#ffffff')
        draw = ImageDraw.Draw(img)
        
        draw.rounded_rectangle([10, 10, w-10, h-10], radius=20, fill=color)
        draw.rounded_rectangle([18, 18, w-18, h-18], radius=16, fill='#ffffff')
        
        # Tag header
        draw.rounded_rectangle([18, 18, w-18, 90], radius=16, fill=color)
        draw.rectangle([18, 60, w-18, 90], fill=color)
        draw_star(draw, 45, 54, r=12, color='#fde047')
        draw.text((65, 34), tag, font=get_font(font_bold, 28), fill='#ffffff')
        
        # Title & desc
        draw.text((35, 115), title, font=get_font(font_treb, 24), fill='#1f2937')
        
        desc_lines = wrap_text(draw, desc, get_font(font_reg, 19), w - 70)
        for j, line in enumerate(desc_lines):
            draw.text((35, 160 + j * 28), line, font=get_font(font_reg, 19), fill='#4b5563')
            
        # PDF Badge
        draw.rounded_rectangle([35, 235, w-35, 285], radius=12, fill='#f3f4f6')
        draw.text((50, 248), 'Formato PDF Pronto da Stampare · Valore €29', font=get_font(font_bold, 16), fill='#374151')
        
        img.save(os.path.join(out_dir, f'{base_name}.png'))
        img.save(os.path.join(out_dir, f'{base_name}_1.png'))
        img.resize((260, 160), Image.Resampling.LANCZOS).save(os.path.join(out_dir, f'{base_name}_2.png'))
        print(f'Generated Italian Bonus Card ({base_name})')

# ==========================================
# 6. TESTIMONIAL 1: INSTAGRAM DM (zBPGty6014358)
# ==========================================
def generate_instagram_dm():
    w, h = 1179, 985
    img = Image.new('RGB', (w, h), color='#ffffff')
    draw = ImageDraw.Draw(img)
    
    # Top bar
    draw.text((w//2 - 40, 25), '22:40', font=get_font(font_bold, 28), fill='#111827')
    
    # User profile circle with nice monogram
    draw_avatar_badge(draw, 105, 135, 45, 'LB', '#ec4899', '#ffffff')
    
    # Message 1
    draw.rounded_rectangle([180, 90, 420, 170], radius=30, fill='#f3f4f6')
    draw.text((215, 115), 'Buonasera!', font=get_font(font_reg, 32), fill='#111827')
    
    # Message 2 - Big testimonial bubble
    msg2_text = "Ho acquistato il Kit Comprensione del Testo per mia figlia e sono rimasta incantata da tutto il materiale. Che cura e attenzione in ogni singolo dettaglio! Mia figlia è entusiasta e non vede l'ora di fare le schede ogni pomeriggio. Sono sicura che farà passi da gigante e migliorerà tantissimo."
    
    lines = wrap_text(draw, msg2_text, get_font(font_reg, 32), 800)
    bubble_h = 100 + len(lines) * 48
    draw.rounded_rectangle([180, 200, 1050, 200 + bubble_h], radius=32, fill='#f3f4f6')
    
    for i, line in enumerate(lines):
        draw.text((215, 235 + i * 48), line, font=get_font(font_reg, 32), fill='#111827')
        
    # Heart reaction
    draw.ellipse([200, 200 + bubble_h - 20, 270, 200 + bubble_h + 50], fill='#ffffff', outline='#f3f4f6', width=3)
    draw_heart(draw, 235, 200 + bubble_h + 15, size=24, color='#ef4444')
    
    # Bottom chat bar
    bar_y = h - 140
    draw.rounded_rectangle([50, bar_y, w-50, bar_y + 90], radius=45, fill='#f3f4f6')
    draw.text((90, bar_y + 26), 'Scrivi un messaggio...', font=get_font(font_reg, 30), fill='#9ca3af')
    
    img.save(os.path.join(out_dir, 'zBPGty6014358.jpeg'))
    img.save(os.path.join(out_dir, 'zBPGty6014358_1.jpeg'))
    img.resize((300, 250), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'zBPGty6014358_2.jpeg'))
    img.resize((1024, 855), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'zBPGty6014358_3.jpeg'))
    img.resize((768, 641), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'zBPGty6014358_4.jpeg'))
    print('Generated Italian Instagram DM (zBPGty6014358)')

# ==========================================
# 7. TESTIMONIAL 2: WHATSAPP VOICE NOTE TRANSCRIPTION (vrAnob5260946)
# ==========================================
def generate_whatsapp_voice_transcription():
    w, h = 942, 829
    img = Image.new('RGB', (w, h), color='#efeae2')
    draw = ImageDraw.Draw(img)
    
    # Voice note bubble
    draw.rounded_rectangle([40, 40, w-40, h-40], radius=28, fill='#ffffff')
    
    # Voice player top part
    draw.polygon([(80, 80), (80, 130), (125, 105)], fill='#4b5563') # Play icon
    for k in range(25):
        vx = 160 + k * 22
        vh = 15 + (k * 7) % 35
        draw.rounded_rectangle([vx, 105 - vh//2, vx + 8, 105 + vh//2], radius=4, fill='#3b82f6' if k < 10 else '#94a3b8')
    
    draw.text((160, 140), '0:21 / 1:15', font=get_font(font_reg, 24), fill='#6b7280')
    draw.text((w-180, 140), '16:54', font=get_font(font_reg, 24), fill='#6b7280')
    
    # Profile picture badge
    draw_avatar_badge(draw, w-95, 100, 35, 'MT', '#3b82f6', '#ffffff')
    
    # Divider line
    draw.line([(70, 185), (w-70, 185)], fill='#f1f5f9', width=2)
    
    # Audio transcription
    trans_text = "«Ciao! Volevo dirti che all'inizio ero un po' scettica, pensavo fosse il solito materiale generico... e invece mi sono dovuta ricredere! Il kit è strutturato benissimo. Mio figlio di 8 anni ha iniziato dal livello base e ora sta già passando a quello avanzato. Sono felicissima nel vederlo così fiero quando riesce a fare le schede da solo. Ne è valsa davvero la pena!»"
    
    lines = wrap_text(draw, trans_text, get_font(font_reg, 28), w - 160)
    for i, line in enumerate(lines):
        draw.text((70, 215 + i * 44), line, font=get_font(font_reg, 28), fill='#1e293b')
        
    # Bottom transcription feedback
    draw.text((70, h - 110), 'Hai trovato utile la trascrizione vocale?', font=get_font(font_bold, 24), fill='#475569')
    draw_checkmark(draw, 70, h - 70, size=20, color='#059669', width=3)
    draw.text((100, h - 72), 'Sì, utilissima · Trascrizione automatica verificata', font=get_font(font_bold, 22), fill='#059669')
    
    img.save(os.path.join(out_dir, 'vrAnob5260946.webp'))
    img.resize((300, 264), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'vrAnob5260946_1.webp'))
    img.save(os.path.join(out_dir, 'vrAnob5260946_2.webp'))
    img.resize((768, 676), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'vrAnob5260946_3.webp'))
    print('Generated Italian WhatsApp Voice Transcription (vrAnob5260946)')

# ==========================================
# 8. TESTIMONIAL 3: WHATSAPP DARK MODE (MFPLzd5360958)
# ==========================================
def generate_whatsapp_dark_mode():
    w, h = 1086, 1448
    img = Image.new('RGB', (w, h), color='#0b141a')
    draw = ImageDraw.Draw(img)
    
    # Status bar
    draw.text((60, 30), '11:38', font=get_font(font_bold, 32), fill='#ffffff')
    draw.text((w-160, 30), '5G 94%', font=get_font(font_bold, 28), fill='#ffffff')
    
    # Top chat header
    draw.rectangle([0, 80, w, 200], fill='#1f2c34')
    draw.text((40, 120), '<', font=get_font(font_bold, 44), fill='#ffffff')
    draw_avatar_badge(draw, 150, 140, 40, 'RV', '#00a884', '#ffffff')
    
    draw.text((215, 105), 'Renata V.', font=get_font(font_bold, 36), fill='#ffffff')
    draw.text((215, 150), 'Ultimo accesso oggi alle 11:32', font=get_font(font_reg, 24), fill='#8696a0')
    
    # Date Pill
    draw.rounded_rectangle([w//2 - 80, 230, w//2 + 80, 280], radius=15, fill='#182229')
    draw.text((w//2 - 30, 242), 'Oggi', font=get_font(font_bold, 24), fill='#8696a0')
    
    # Message bubble
    msg_bubble_text = [
        "Ciao, buongiorno!",
        "",
        "Volevo scriverti un attimo per dirti una cosa che mi ha resa davvero felicissima!",
        "",
        "Avevo provato altre schede didattiche prima, ma non funzionavano... Mio figlio si rifiutava di leggere.",
        "",
        "Questo kit è tutta un'altra cosa, davvero!",
        "",
        "In sole 3 settimane mia figlia riesce a riassumere qualsiasi testo. Non l'avevo mai vista capire così a fondo e lavorare in totale autonomia.",
        "",
        "Grazie di cuore per tutto!"
    ]
    
    bw = 920
    by = 310
    draw.rounded_rectangle([50, by, 50 + bw, by + 820], radius=24, fill='#1f2c34')
    draw.polygon([(50, by + 30), (25, by + 15), (50, by + 50)], fill='#1f2c34')
    
    curr_y = by + 30
    for para in msg_bubble_text:
        if not para:
            curr_y += 18
            continue
        plines = wrap_text(draw, para, get_font(font_reg, 32), bw - 80)
        for line in plines:
            draw.text((85, curr_y), line, font=get_font(font_reg, 32), fill='#e9edef')
            curr_y += 44
            
    # Timestamp inside bubble
    draw.text((50 + bw - 170, by + 760), '11:28', font=get_font(font_reg, 24), fill='#8696a0')
    draw_double_checkmarks(draw, 50 + bw - 90, by + 765, size=18, color='#53bdeb', width=2)
    
    # Bottom input bar
    draw.rectangle([0, h-120, w, h], fill='#1f2c34')
    draw.rounded_rectangle([40, h-100, w-40, h-20], radius=25, fill='#2a3942')
    draw.text((80, h-72), 'Scrivi un messaggio...', font=get_font(font_reg, 28), fill='#8696a0')
    
    img.save(os.path.join(out_dir, 'MFPLzd5360958.webp'))
    img.resize((300, 400), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'MFPLzd5360958_1.webp'))
    img.resize((768, 1024), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'MFPLzd5360958_2.webp'))
    img.resize((1024, 1365), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'MFPLzd5360958_3.webp'))
    img.save(os.path.join(out_dir, 'MFPLzd5360958_4.webp'))
    print('Generated Italian WhatsApp Dark Mode (MFPLzd5360958)')

# ==========================================
# 9. TESTIMONIAL 4: WHATSAPP BUBBLE (JeslyJ6014358)
# ==========================================
def generate_whatsapp_bubble_single():
    w, h = 1599, 754
    img = Image.new('RGB', (w, h), color='#efeae2')
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([60, 50, w-60, h-50], radius=36, fill='#ffffff')
    draw.polygon([(60, 110), (30, 80), (60, 140)], fill='#ffffff')
    
    t_text = "Volevo davvero ringraziarvi di cuore. Ho iniziato a usare le attività didattiche con mio figlio la scorsa settimana e oggi, dopo aver finito la scheda, mi ha detto: 'Mamma, adesso ho capito davvero il testo!'... Mi sono quasi commossa. Non lo avevo mai visto così sicuro e sereno nello studio."
    
    lines = wrap_text(draw, t_text, get_font(font_reg, 44), w - 240)
    for i, line in enumerate(lines):
        draw.text((110, 95 + i * 65), line, font=get_font(font_reg, 44), fill='#111827')
        
    draw.text((w-240, h-120), '12:40', font=get_font(font_reg, 36), fill='#6b7280')
    draw_double_checkmarks(draw, w-130, h-112, size=24, color='#3b82f6', width=4)
    
    img.save(os.path.join(out_dir, 'JeslyJ6014358.png'))
    img.resize((300, 141), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'JeslyJ6014358_1.png'))
    img.resize((768, 362), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'JeslyJ6014358_2.png'))
    img.save(os.path.join(out_dir, 'JeslyJ6014358_3.png'))
    img.resize((1536, 724), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'JeslyJ6014358_4.png'))
    img.resize((1024, 483), Image.Resampling.LANCZOS).save(os.path.join(out_dir, 'JeslyJ6014358_5.png'))
    print('Generated Italian WhatsApp Bubble (JeslyJ6014358)')

# ==========================================
# 10. TESTIMONIAL WIDE BANNERS (kbvgHh, pQfwEt, iWnJvw, YGvXxb)
# ==========================================
def generate_testimonial_banners():
    banners = [
        ('kbvgHh6486611', "Confesso che all'inizio ero un po' diffidente, ma già dopo la prima settimana ho visto una grande differenza. Ora riesce a spiegare i testi con parole sue! Prima diceva solo 'non so'. Davvero grazie di cuore.", 841),
        ('pQfwEt6486611', "Mio figlio ha 10 anni e si bloccava sempre nella comprensione del testo. Pensavo fosse distrazione, ma non era così. Ora legge e commenta insieme a me, spiega i concetti ed esprime la sua opinione... Sono entusiasta di questi progressi!", 837),
        ('iWnJvw6486611', "Spendavamo oltre 250€ al mese in ripetizioni private senza grandi risultati. Con questo materiale didattico ha fatto più progressi in 2 settimane che in tutto l'ultimo anno scolastico.", 706),
        ('YGvXxb6486611', "Davvero incredibile! Ho stampato le prime schede e le ha svolte tutte con entusiasmo. La cosa che mi ha sorpreso di più è vedere che finalmente CAPISCE ciò che legge. Era esattamente ciò che cercavamo!", 706)
    ]
    
    for base_name, text, bh in banners:
        w, h = 1600, bh
        img = Image.new('RGB', (w, h), color='#efeae2')
        draw = ImageDraw.Draw(img)
        
        draw.rounded_rectangle([60, 40, w-60, h-40], radius=36, fill='#ffffff')
        draw.polygon([(60, 100), (30, 70), (60, 130)], fill='#ffffff')
        
        lines = wrap_text(draw, text, get_font(font_reg, 46), w - 240)
        for i, line in enumerate(lines):
            draw.text((110, 85 + i * 68), line, font=get_font(font_reg, 46), fill='#111827')
            
        draw.text((w-240, h-110), '18:15', font=get_font(font_reg, 36), fill='#6b7280')
        draw_double_checkmarks(draw, w-130, h-102, size=24, color='#3b82f6', width=4)
        
        img.save(os.path.join(out_dir, f'{base_name}.png'))
        img.resize((300, int(300 * h / w)), Image.Resampling.LANCZOS).save(os.path.join(out_dir, f'{base_name}_1.png'))
        img.save(os.path.join(out_dir, f'{base_name}_2.png'))
        img.resize((768, int(768 * h / w)), Image.Resampling.LANCZOS).save(os.path.join(out_dir, f'{base_name}_3.png'))
        img.resize((1024, int(1024 * h / w)), Image.Resampling.LANCZOS).save(os.path.join(out_dir, f'{base_name}_4.png'))
        img.resize((1536, int(1536 * h / w)), Image.Resampling.LANCZOS).save(os.path.join(out_dir, f'{base_name}_5.png'))
        print(f'Generated Testimonial Banner ({base_name})')

if __name__ == '__main__':
    generate_italian_test_sheet()
    generate_italian_whatsapp_bubble()
    generate_italian_member_platform()
    generate_italian_worksheets()
    generate_italian_bonus_cards()
    generate_instagram_dm()
    generate_whatsapp_voice_transcription()
    generate_whatsapp_dark_mode()
    generate_whatsapp_bubble_single()
    generate_testimonial_banners()
    print('ALL ITALIAN ASSETS CREATED SUCCESSFULLY!')
