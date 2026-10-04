import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

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

def draw_star(draw, cx, cy, r, color='#fbbf24'):
    points = []
    for i in range(10):
        angle = i * math.pi / 5 - math.pi / 2
        radius = r if i % 2 == 0 else r * 0.42
        px = cx + radius * math.cos(angle)
        py = cy + radius * math.sin(angle)
        points.append((px, py))
    draw.polygon(points, fill=color)

def generate_upgraded_mobile_hero():
    W, H = 1080, 1920
    canvas = Image.new('RGB', (W, H), color='#ffffff')
    draw = ImageDraw.Draw(canvas)
    
    # Soft modern background gradient
    for y in range(H):
        ratio = y / H
        r = int(255 - ratio * 8)
        g = int(255 - ratio * 6)
        b = int(255)
        draw.line([(0, y), (W, y)], fill=(r, g, b))
        
    # Top Tagline Pill
    tag_w, tag_h = 560, 60
    tx1, ty1 = (W - tag_w) // 2, 70
    draw.rounded_rectangle([tx1, ty1, tx1 + tag_w, ty1 + tag_h], radius=30, fill='#0f172a')
    draw_star(draw, tx1 + 35, ty1 + 30, r=12, color='#fbbf24')
    draw_star(draw, tx1 + tag_w - 35, ty1 + 30, r=12, color='#fbbf24')
    
    f_tag = get_font(font_bold_path, 26)
    t_tag = 'METODO DIDATTICO 2026'
    bb_t = draw.textbbox((0, 0), t_tag, font=f_tag)
    draw.text(((W - (bb_t[2]-bb_t[0])) // 2, ty1 + 16), t_tag, font=f_tag, fill='#f8fafc')

    # Top Headline
    f_h1_large = get_font(font_title_path, 92)
    f_h1_mid = get_font(font_title_path, 54)
    f_h1_sub = get_font(font_bold_path, 36)
    
    t_587 = '587 ATTIVITÀ'
    bbox1 = draw.textbbox((0, 0), t_587, font=f_h1_large)
    draw.text(((W - (bbox1[2]-bbox1[0])) // 2, 160), t_587, font=f_h1_large, fill='#0284c7')
    
    t_comp = 'DI COMPRENSIONE DEL TESTO'
    bb_comp = draw.textbbox((0, 0), t_comp, font=f_h1_mid)
    draw.text(((W - (bb_comp[2]-bb_comp[0])) // 2, 275), t_comp, font=f_h1_mid, fill='#0f172a')

    t_sub1 = 'PER ALLENARSI OGNI GIORNO E'
    bb_s1 = draw.textbbox((0, 0), t_sub1, font=f_h1_sub)
    draw.text(((W - (bb_s1[2]-bb_s1[0])) // 2, 355), t_sub1, font=f_h1_sub, fill='#475569')

    t_sub2 = 'SUPERARE LE DIFFICOLTÀ'
    bb_s2 = draw.textbbox((0, 0), t_sub2, font=f_h1_mid)
    draw.text(((W - (bb_s2[2]-bb_s2[0])) // 2, 410), t_sub2, font=f_h1_mid, fill='#dc2626')

    t_sub3 = 'IN TUTTE LE DISCIPLINE'
    bb_s3 = draw.textbbox((0, 0), t_sub3, font=f_h1_sub)
    draw.text(((W - (bb_s3[2]-bb_s3[0])) // 2, 485), t_sub3, font=f_h1_sub, fill='#475569')

    # Center Fan Image
    fan_img_path = 'scratch_sheets.png'
    if not os.path.exists(fan_img_path):
        fan_img_path = 'assets interpretar para evoluir/scratch_sheets.png'
    if os.path.exists(fan_img_path):
        fan = Image.open(fan_img_path).convert('RGBA')
        fw = 1000
        fh = int(fan.height * (fw / fan.width))
        fan_resized = fan.resize((fw, fh), Image.Resampling.LANCZOS)
        
        # Add shadow behind fan
        shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        sdraw = ImageDraw.Draw(shadow)
        fx = (W - fw) // 2
        fy = 560
        sdraw.ellipse([fx + 80, fy + fh - 60, fx + fw - 80, fy + fh + 40], fill=(0, 0, 0, 100))
        shadow = shadow.filter(ImageFilter.GaussianBlur(30))
        canvas.paste(shadow, (0, 0), shadow)
        canvas.paste(fan_resized, (fx, fy), fan_resized)
        
    # Bottom Luxury Gradient Card
    bar_x1, bar_y1, bar_x2, bar_y2 = 45, 1420, 1035, 1780
    
    # Draw card with subtle border and gradient
    draw.rounded_rectangle([bar_x1, bar_y1, bar_x2, bar_y2], radius=32, fill='#0f172a', outline='#38bdf8', width=2)
    
    mob_items = [
        'PER BAMBINI DAI 7 AI 12 ANNI',
        'FORMATO PDF PRONTO DA STAMPARE',
        'LIVELLI PROGRESSIVI 1, 2 E 3'
    ]
    f_bar_mob = get_font(font_bold_path, 34)
    
    for idx, itm in enumerate(mob_items):
        item_y = bar_y1 + 45 + idx * 105
        bb = draw.textbbox((0, 0), itm, font=f_bar_mob)
        tw = bb[2] - bb[0]
        tx = (W - tw) // 2
        
        draw_star(draw, tx - 45, item_y + 18, r=16, color='#fbbf24')
        draw.text((tx, item_y), itm, font=f_bar_mob, fill='#ffffff')
        draw_star(draw, tx + tw + 45, item_y + 18, r=16, color='#fbbf24')
        
        if idx < len(mob_items) - 1:
            draw.line([(bar_x1 + 60, item_y + 80), (bar_x2 - 60, item_y + 80)], fill='#334155', width=1)

    # Save to public/images and images/
    for folder in ['public/images', 'images']:
        os.makedirs(folder, exist_ok=True)
        canvas.save(f'{folder}/WReKdb5163414.webp', quality=95)
        canvas.resize((300, 533), Image.Resampling.LANCZOS).save(f'{folder}/WReKdb5163414_1.webp', quality=90)
        canvas.resize((768, 1365), Image.Resampling.LANCZOS).save(f'{folder}/WReKdb5163414_2.webp', quality=90)
        canvas.resize((1024, 1820), Image.Resampling.LANCZOS).save(f'{folder}/WReKdb5163414_3.webp', quality=90)
        canvas.save(f'{folder}/WReKdb5163414_4.webp', quality=95)
        
    print('Generated upgraded mobile hero image without square boxes!')

if __name__ == '__main__':
    generate_upgraded_mobile_hero()
