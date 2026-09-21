import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('images', exist_ok=True)

font_bold_path = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
font_title_path = '/System/Library/Fonts/Supplemental/Trebuchet MS Bold.ttf'
if not os.path.exists(font_title_path):
    font_title_path = '/System/Library/Fonts/Helvetica.ttc'

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

fan_img_path = '/Users/lenovo/.gemini/antigravity-ide/brain/3e0048c1-edfe-449f-bee5-218b2c9c2e7c/hero_sheets_fan_1789962098459.jpg'
stack_img_path = '/Users/lenovo/.gemini/antigravity-ide/brain/3e0048c1-edfe-449f-bee5-218b2c9c2e7c/offer_stack_mockup_1789962143857.jpg'

# 1. PROCESS DESKTOP HERO (1200x724)
def make_desktop_hero():
    W, H = 1200, 724
    canvas = Image.new('RGB', (W, H), '#ffffff')
    draw = ImageDraw.Draw(canvas)
    
    # Load AI fan image
    fan = Image.open(fan_img_path).convert('RGBA')
    # Resize and paste on right side
    # Crop borders if white
    fan_w, fan_h = fan.size
    fan_resized = fan.resize((680, 508), Image.Resampling.LANCZOS)
    canvas.paste(fan_resized, (510, 40))
    
    # Left typography
    x_left = 50
    y_start = 125
    
    f_h1_large = get_font(font_title_path, 52)
    f_h1_mid = get_font(font_title_path, 33)
    
    draw.text((x_left, y_start), '587 ATTIVITÀ', font=f_h1_large, fill='#be868c')
    draw.text((x_left, y_start + 65), 'DI COMPRENSIONE', font=f_h1_mid, fill='#887396')
    draw.text((x_left, y_start + 108), 'DEL TESTO PER ALLENARSI', font=f_h1_mid, fill='#887396')
    draw.text((x_left, y_start + 151), 'TUTTI I GIORNI E', font=f_h1_mid, fill='#887396')
    draw.text((x_left, y_start + 200), 'SUPERARE LE DIFFICOLTÀ', font=f_h1_mid, fill='#be868c')
    draw.text((x_left, y_start + 248), 'IN TUTTE LE DISCIPLINE', font=f_h1_mid, fill='#887396')
    
    # Bottom purple bar
    bar_x1, bar_y1, bar_x2, bar_y2 = 45, 600, 1155, 665
    draw.rounded_rectangle([bar_x1, bar_y1, bar_x2, bar_y2], radius=26, fill='#887396')
    
    f_bar = get_font(font_bold_path, 18)
    bar_text = '⭐ PER BAMBINI DAI 7 AI 12 ANNI ⭐ FACILE E PRATICO DA STAMPARE ⭐ PROGRAMMA DIDATTICO PROGRESSIVO'
    bbox = draw.textbbox((0, 0), bar_text, font=f_bar)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text(((W - tw) // 2, bar_y1 + (bar_y2 - bar_y1 - th) // 2 - 2), bar_text, font=f_bar, fill='#ffffff')
    
    canvas.save('images/dppDQD5163414.webp', quality=95)
    canvas.resize((300, 181)).save('images/dppDQD5163414_1.webp', quality=90)
    canvas.resize((768, 463)).save('images/dppDQD5163414_2.webp', quality=90)
    canvas.resize((1024, 618)).save('images/dppDQD5163414_3.webp', quality=90)
    canvas.save('images/dppDQD5163414_4.webp', quality=95)
    print('Processed Desktop Hero dppDQD5163414.webp!')

# 2. PROCESS MOBILE HERO (1080x1920)
def make_mobile_hero():
    W, H = 1080, 1920
    canvas = Image.new('RGB', (W, H), '#ffffff')
    draw = ImageDraw.Draw(canvas)
    
    # Top Headline
    f_h1_large = get_font(font_title_path, 80)
    f_h1_mid = get_font(font_title_path, 52)
    
    bbox1 = draw.textbbox((0, 0), '587 ATTIVITÀ', font=f_h1_large)
    draw.text(((W - (bbox1[2]-bbox1[0])) // 2, 90), '587 ATTIVITÀ', font=f_h1_large, fill='#be868c')
    
    lines = [
        ('DI COMPRENSIONE DEL TESTO', '#887396'),
        ('PER ALLENARSI OGNI GIORNO E', '#887396'),
        ('SUPERARE LE DIFFICOLTÀ', '#be868c'),
        ('IN TUTTE LE DISCIPLINE', '#887396')
    ]
    for idx, (txt, col) in enumerate(lines):
        bb = draw.textbbox((0, 0), txt, font=f_h1_mid)
        draw.text(((W - (bb[2]-bb[0])) // 2, 190 + idx * 72), txt, font=f_h1_mid, fill=col)
        
    # Center Fan Image
    fan = Image.open(fan_img_path).convert('RGBA')
    fan_resized = fan.resize((1000, 746), Image.Resampling.LANCZOS)
    canvas.paste(fan_resized, (40, 580))
    
    # Bottom purple bar
    bar_x1, bar_y1, bar_x2, bar_y2 = 40, 1480, 1040, 1740
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
        
    canvas.save('images/WReKdb5163414.webp', quality=95)
    canvas.resize((300, 533)).save('images/WReKdb5163414_1.webp', quality=90)
    canvas.resize((768, 1365)).save('images/WReKdb5163414_2.webp', quality=90)
    canvas.resize((1024, 1820)).save('images/WReKdb5163414_3.webp', quality=90)
    canvas.save('images/WReKdb5163414_4.webp', quality=95)
    print('Processed Mobile Hero WReKdb5163414.webp!')

# 3. PROCESS OFFER STACK MOCKUP (1200x900)
def make_offer_stack():
    W, H = 1200, 900
    stack = Image.open(stack_img_path).convert('RGB')
    stack_resized = stack.resize((W, H), Image.Resampling.LANCZOS)
    
    stack_resized.save('images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src.png')
    stack_resized.resize((1200, 900)).save('images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src_1.png')
    stack_resized.resize((1024, 768)).save('images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src_2.png')
    stack_resized.resize((768, 576)).save('images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src_3.png')
    stack_resized.resize((300, 225)).save('images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src_4.png')
    print('Processed Offer Stack d597bf16...!')

make_desktop_hero()
make_mobile_hero()
make_offer_stack()
