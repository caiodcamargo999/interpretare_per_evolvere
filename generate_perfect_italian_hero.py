import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

os.makedirs('images', exist_ok=True)

font_bold_path = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
font_reg_path = '/System/Library/Fonts/Supplemental/Arial.ttf'
font_title_path = '/System/Library/Fonts/Supplemental/Trebuchet MS Bold.ttf'
if not os.path.exists(font_title_path):
    font_title_path = '/System/Library/Fonts/Helvetica.ttc'

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def draw_sheet(w=260, h=350, border_color='#ff8c00', title_text='DESAFIO 1', header_bg='#ffb703', category='STORIA & SCIENZE', has_stars=True):
    sheet = Image.new('RGBA', (w, h), (255, 255, 255, 0))
    d = ImageDraw.Draw(sheet)
    
    # White card with border
    d.rounded_rectangle([0, 0, w-1, h-1], radius=12, fill='#ffffff', outline=border_color, width=4)
    
    # Top header badge
    d.rounded_rectangle([15, 12, 120, 36], radius=6, fill=header_bg)
    f_badge = get_font(font_bold_path, 13)
    d.text((22, 17), title_text, font=f_badge, fill='#000000')
    
    if has_stars:
        f_star = get_font(font_bold_path, 16)
        d.text((w - 35, 14), '⭐', font=f_star, fill='#ffb703')
        
    # Content area / title
    f_cat = get_font(font_bold_path, 11)
    d.text((15, 45), category, font=f_cat, fill='#887396')
    
    # Illustration box placeholder / graphic
    d.rounded_rectangle([15, 62, w - 15, 170], radius=8, fill='#f4f0f5', outline='#e6e8ea', width=1)
    
    # Inner graphic icon/mini illustration
    d.rounded_rectangle([25, 72, w - 25, 160], radius=6, fill=border_color)
    d.rounded_rectangle([28, 75, w - 28, 157], radius=5, fill='#ffffff')
    
    # Educational text lines
    f_text = get_font(font_reg_path, 10)
    lines = [
        'Leggi il testo e rispondi con attenzione:',
        'Nel bosco antico viveva una piccola volpe...',
        '1. Dove si trova la tana della volpe?',
        '2. Quale animale ha incontrato al fiume?',
        '3. Spiega il significato della parola evidenziata.'
    ]
    for idx, line in enumerate(lines):
        y_pos = 185 + idx * 18
        if y_pos < h - 40:
            d.text((15, y_pos), line[:38], font=f_text, fill='#363636')
            
    # Bottom lines / answer boxes
    for b_idx in range(3):
        by = h - 55 + b_idx * 14
        d.line([(15, by), (w - 15, by)], fill='#d1d5db', width=1)
        
    return sheet

def generate_desktop_hero():
    W, H = 1200, 724
    img = Image.new('RGB', (W, H), '#ffffff')
    draw = ImageDraw.Draw(img)
    
    # --- LEFT COLUMN: TYPOGRAPHY ---
    f_h1_large = get_font(font_title_path, 54)
    f_h1_mid = get_font(font_title_path, 34)
    f_h1_sub = get_font(font_title_path, 30)
    
    x_left = 60
    y_start = 120
    
    # Line 1: 587 ATTIVITÀ
    draw.text((x_left, y_start), '587 ATTIVITÀ', font=f_h1_large, fill='#be868c')
    
    # Line 2: DI COMPRENSIONE DELLO STUDIO
    draw.text((x_left, y_start + 68), 'DI COMPRENSIONE', font=f_h1_mid, fill='#887396')
    draw.text((x_left, y_start + 112), 'DEL TESTO PER ALLENARSI', font=f_h1_mid, fill='#887396')
    draw.text((x_left, y_start + 156), 'TUTTI I GIORNI E', font=f_h1_mid, fill='#887396')
    
    # Line 3: SUPERARE LE DIFFICOLTÀ
    draw.text((x_left, y_start + 208), 'SUPERARE LE DIFFICOLTÀ', font=f_h1_mid, fill='#be868c')
    
    # Line 4: IN TUTTE LE MATERIE
    draw.text((x_left, y_start + 256), 'IN TUTTE LE DISCIPLINE', font=f_h1_mid, fill='#887396')
    
    # Subtitle guarantee note
    f_note = get_font(font_bold_path, 17)
    draw.text((x_left, y_start + 325), 'Dai 7 ai 12 anni · Scuola Primaria e Media', font=f_note, fill='#7a7a7a')

    # --- RIGHT COLUMN: FANNED WORKSHEETS (NO SPECIALIST WOMAN) ---
    sheets_configs = [
        {'angle': -22, 'pos': (620, 80), 'border': '#e63946', 'title': 'ATTIVITÀ 15', 'bg': '#ffd166', 'cat': 'STORIA & MITI'},
        {'angle': -12, 'pos': (700, 40), 'border': '#3a86ff', 'title': 'ATTIVITÀ 28', 'bg': '#a8dadc', 'cat': 'SCIENZE & NATURA'},
        {'angle': 0,   'pos': (790, 25), 'border': '#ffbe0b', 'title': 'ATTIVITÀ 42', 'bg': '#ffeedd', 'cat': 'LETTURA & COMPRENSIONE'},
        {'angle': 12,  'pos': (880, 45), 'border': '#8338ec', 'title': 'ATTIVITÀ 65', 'bg': '#e2afff', 'cat': 'INFERENZE & LOGICA'},
        {'angle': 24,  'pos': (960, 95), 'border': '#fb5607', 'title': 'ATTIVITÀ 90', 'bg': '#ffcbf2', 'cat': 'PRODUZIONE SCRITTA'}
    ]
    
    for cfg in sheets_configs:
        sheet = draw_sheet(w=260, h=370, border_color=cfg['border'], title_text=cfg['title'], header_bg=cfg['bg'], category=cfg['cat'])
        # Add shadow
        rot_sheet = sheet.rotate(cfg['angle'], resample=Image.BICUBIC, expand=True)
        img.paste(rot_sheet, cfg['pos'], rot_sheet)
        
    # Front Showcase Card overlapping
    front_sheet = draw_sheet(w=290, h=390, border_color='#00c738', title_text='SCHEDA SPECIALE', header_bg='#00c738', category='COMPRENSIONE DEL TESTO 2.0')
    rot_front = front_sheet.rotate(4, resample=Image.BICUBIC, expand=True)
    img.paste(rot_front, (780, 160), rot_front)
    
    # --- BOTTOM PURPLE BAR ---
    bar_x1, bar_y1, bar_x2, bar_y2 = 50, 620, 1150, 685
    draw.rounded_rectangle([bar_x1, bar_y1, bar_x2, bar_y2], radius=30, fill='#887396')
    
    f_bar = get_font(font_bold_path, 19)
    bar_text = '⭐ PER BAMBINI DAI 7 AI 12 ANNI ⭐ FACILE E PRATICO DA STAMPARE ⭐ LIVELLI PROGRESSIVI 1, 2 E 3'
    # Center text in bar
    bbox = draw.textbbox((0, 0), bar_text, font=f_bar)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    draw.text(((W - text_w) // 2, bar_y1 + (bar_y2 - bar_y1 - text_h) // 2 - 2), bar_text, font=f_bar, fill='#ffffff')
    
    # Save variants
    img.save('images/dppDQD5163414.webp', quality=95)
    img.resize((300, 181)).save('images/dppDQD5163414_1.webp', quality=90)
    img.resize((768, 463)).save('images/dppDQD5163414_2.webp', quality=90)
    img.resize((1024, 618)).save('images/dppDQD5163414_3.webp', quality=90)
    img.save('images/dppDQD5163414_4.webp', quality=95)
    print('Generated Desktop Hero dppDQD5163414.webp on white background with fanned sheets!')

def generate_mobile_hero():
    W, H = 1080, 1920
    img = Image.new('RGB', (W, H), '#ffffff')
    draw = ImageDraw.Draw(img)
    
    # TOP HEADLINE
    f_h1_large = get_font(font_title_path, 80)
    f_h1_mid = get_font(font_title_path, 54)
    
    # Line 1: 587 ATTIVITÀ
    bbox1 = draw.textbbox((0, 0), '587 ATTIVITÀ', font=f_h1_large)
    draw.text(((W - (bbox1[2]-bbox1[0])) // 2, 90), '587 ATTIVITÀ', font=f_h1_large, fill='#be868c')
    
    # Lines: DI COMPRENSIONE DEL TESTO...
    lines = [
        ('DI COMPRENSIONE DEL TESTO', '#887396'),
        ('PER ALLENARSI OGNI GIORNO E', '#887396'),
        ('SUPERARE LE DIFFICOLTÀ', '#be868c'),
        ('IN TUTTE LE DISCIPLINE', '#887396')
    ]
    for idx, (txt, col) in enumerate(lines):
        bb = draw.textbbox((0, 0), txt, font=f_h1_mid)
        draw.text(((W - (bb[2]-bb[0])) // 2, 190 + idx * 75), txt, font=f_h1_mid, fill=col)
        
    # MIDDLE FANNED WORKSHEETS
    sheets_configs = [
        {'angle': -18, 'pos': (120, 680), 'border': '#e63946', 'title': 'ATTIVITÀ 15', 'bg': '#ffd166', 'cat': 'STORIA & MITI'},
        {'angle': -8,  'pos': (280, 620), 'border': '#3a86ff', 'title': 'ATTIVITÀ 28', 'bg': '#a8dadc', 'cat': 'SCIENZE & NATURA'},
        {'angle': 8,   'pos': (480, 630), 'border': '#8338ec', 'title': 'ATTIVITÀ 42', 'bg': '#e2afff', 'cat': 'INFERENZE & LOGICA'},
        {'angle': 20,  'pos': (640, 700), 'border': '#fb5607', 'title': 'ATTIVITÀ 65', 'bg': '#ffcbf2', 'cat': 'LETTURA & ANALISI'}
    ]
    for cfg in sheets_configs:
        sheet = draw_sheet(w=380, h=520, border_color=cfg['border'], title_text=cfg['title'], header_bg=cfg['bg'], category=cfg['cat'])
        rot_sheet = sheet.rotate(cfg['angle'], resample=Image.BICUBIC, expand=True)
        img.paste(rot_sheet, cfg['pos'], rot_sheet)
        
    front_sheet = draw_sheet(w=440, h=600, border_color='#00c738', title_text='SCHEDA SPECIALE', header_bg='#00c738', category='COMPRENSIONE DEL TESTO 2.0')
    rot_front = front_sheet.rotate(2, resample=Image.BICUBIC, expand=True)
    img.paste(rot_front, (320, 780), rot_front)
    
    # BOTTOM PURPLE BAR
    bar_x1, bar_y1, bar_x2, bar_y2 = 40, 1580, 1040, 1820
    draw.rounded_rectangle([bar_x1, bar_y1, bar_x2, bar_y2], radius=35, fill='#887396')
    
    f_bar_mob = get_font(font_bold_path, 34)
    mob_items = [
        '⭐ PER BAMBINI DAI 7 AI 12 ANNI ⭐',
        '⭐ FACILE E PRATICO DA STAMPARE ⭐',
        '⭐ LIVELLI PROGRESSIVI 1, 2 E 3 ⭐'
    ]
    for idx, itm in enumerate(mob_items):
        bb = draw.textbbox((0, 0), itm, font=f_bar_mob)
        draw.text(((W - (bb[2]-bb[0])) // 2, bar_y1 + 32 + idx * 68), itm, font=f_bar_mob, fill='#ffffff')
        
    # Save variants
    img.save('images/WReKdb5163414.webp', quality=95)
    img.resize((300, 533)).save('images/WReKdb5163414_1.webp', quality=90)
    img.resize((768, 1365)).save('images/WReKdb5163414_2.webp', quality=90)
    img.resize((1024, 1820)).save('images/WReKdb5163414_3.webp', quality=90)
    img.save('images/WReKdb5163414_4.webp', quality=95)
    print('Generated Mobile Hero WReKdb5163414.webp on white background with fanned sheets!')

generate_desktop_hero()
generate_mobile_hero()
