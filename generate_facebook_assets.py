import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

out_dir = 'facebook_assets'
os.makedirs(out_dir, exist_ok=True)
os.makedirs('public/images', exist_ok=True)

font_bold = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
font_reg = '/System/Library/Fonts/Supplemental/Arial.ttf'
font_treb = '/System/Library/Fonts/Supplemental/Trebuchet MS Bold.ttf'
font_georgia = '/System/Library/Fonts/Supplemental/Georgia Bold.ttf'

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def draw_star(draw, cx, cy, r, color='#facc15'):
    points = []
    for i in range(10):
        angle = i * math.pi / 5 - math.pi / 2
        radius = r if i % 2 == 0 else r * 0.42
        px = cx + radius * math.cos(angle)
        py = cy + radius * math.sin(angle)
        points.append((px, py))
    draw.polygon(points, fill=color)

def draw_checkmark(draw, x, y, size=18, color='#10b981', width=3):
    p1 = (x, y + size * 0.5)
    p2 = (x + size * 0.38, y + size * 0.85)
    p3 = (x + size * 0.92, y + size * 0.15)
    draw.line([p1, p2], fill=color, width=width)
    draw.line([p2, p3], fill=color, width=width)

def draw_arrow(draw, x, y, size=16, color='#ffffff', width=3):
    draw.line([(x, y + size//2), (x + size, y + size//2)], fill=color, width=width)
    draw.line([(x + size - size//3, y), (x + size, y + size//2)], fill=color, width=width)
    draw.line([(x + size - size//3, y + size), (x + size, y + size//2)], fill=color, width=width)

# ==========================================
# 1. ULTRA-PREMIUM FACEBOOK PROFILE (1080x1080)
# ==========================================
def generate_fb_profile():
    w, h = 1080, 1080
    img = Image.new('RGB', (w, h), color='#0b1120')
    draw = ImageDraw.Draw(img)
    
    # Rich Luxury Radial/Vertical Gradient
    cx, cy = w // 2, h // 2
    for y in range(h):
        ratio = y / h
        r = int(11 + ratio * 14)
        g = int(17 + ratio * 20)
        b = int(32 + ratio * 50)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
        
    # Ambient glowing central circle
    glow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    for r_glow in range(400, 50, -10):
        alpha = int((1 - r_glow / 400) * 45)
        glow_draw.ellipse([cx - r_glow, cy - r_glow - 30, cx + r_glow, cy + r_glow - 30], fill=(56, 189, 248, alpha))
    glow = glow.filter(ImageFilter.GaussianBlur(35))
    img.paste(glow, (0, 0), glow)
    draw = ImageDraw.Draw(img)

    # Outer Circular Luxury Frame (Safe circular avatar)
    r_outer = 485
    draw.ellipse([cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer], outline='#f59e0b', width=4)
    draw.ellipse([cx - r_outer + 12, cy - r_outer + 12, cx + r_outer - 12, cy + r_outer - 12], outline='#38bdf8', width=2)
    
    # 5 Luxury Stars at Top
    star_xs = [cx - 90, cx - 45, cx, cx + 45, cx + 90]
    star_ys = [cy - 275, cy - 290, cy - 298, cy - 290, cy - 275]
    star_sizes = [13, 16, 20, 16, 13]
    for sx, sy, sr in zip(star_xs, star_ys, star_sizes):
        draw_star(draw, sx, sy, r=sr, color='#fbbf24')

    # Stylized Luxury Open Book & Knowledge Spark
    spine_x = cx
    spine_top = cy - 180
    spine_bot = cy - 40
    
    # Left Wing of Book
    draw.polygon([
        (spine_x - 10, spine_top + 15),
        (cx - 170, spine_top - 20),
        (cx - 170, spine_bot - 20),
        (spine_x - 10, spine_bot + 15)
    ], fill='#ffffff')
    
    # Left Page 2
    draw.polygon([
        (spine_x - 10, spine_top + 20),
        (cx - 150, spine_top - 10),
        (cx - 150, spine_bot - 10),
        (spine_x - 10, spine_bot + 20)
    ], fill='#f8fafc')
    
    # Right Wing of Book
    draw.polygon([
        (spine_x + 10, spine_top + 15),
        (cx + 170, spine_top - 20),
        (cx + 170, spine_bot - 20),
        (spine_x + 10, spine_bot + 15)
    ], fill='#e2e8f0')
    
    # Right Page 2
    draw.polygon([
        (spine_x + 10, spine_top + 20),
        (cx + 150, spine_top - 10),
        (cx + 150, spine_bot - 10),
        (spine_x + 10, spine_bot + 20)
    ], fill='#cbd5e1')

    # Lines representing text on the pages
    for i in range(4):
        ly = spine_top + 25 + i * 18
        draw.line([(cx - 145, ly - 5), (cx - 30, ly + 6)], fill='#64748b', width=4)
        draw.line([(cx + 30, ly + 6), (cx + 145, ly - 5)], fill='#64748b', width=4)
        
    # Knowledge Spark / Star emerging from the book
    draw_star(draw, cx, spine_top - 28, r=28, color='#38bdf8')
    draw_star(draw, cx, spine_top - 28, r=16, color='#ffffff')

    # Brand Title: INTERPRETARE
    f_title1 = get_font(font_treb, 56)
    t1 = 'INTERPRETARE'
    bbox1 = draw.textbbox((0, 0), t1, font=f_title1)
    w1 = bbox1[2] - bbox1[0]
    draw.text((cx - w1//2, cy + 35), t1, font=f_title1, fill='#ffffff')

    # Sub Title: PER EVOLVERE
    f_title2 = get_font(font_treb, 48)
    t2 = 'PER EVOLVERE'
    bbox2 = draw.textbbox((0, 0), t2, font=f_title2)
    w2 = bbox2[2] - bbox2[0]
    draw.text((cx - w2//2, cy + 105), t2, font=f_title2, fill='#38bdf8')

    # Luxury Badge Pill: METODO DIDATTICO 2.0
    pill_w = 440
    pill_h = 58
    px1, py1 = cx - pill_w//2, cy + 190
    px2, py2 = cx + pill_w//2, cy + 190 + pill_h
    draw.rounded_rectangle([px1, py1, px2, py2], radius=29, fill='#f59e0b')
    
    f_pill = get_font(font_bold, 27)
    tp = 'METODO DIDATTICO 2.0'
    bbox_p = draw.textbbox((0, 0), tp, font=f_pill)
    wp = bbox_p[2] - bbox_p[0]
    draw.text((cx - wp//2, py1 + 14), tp, font=f_pill, fill='#070b19')

    # Bottom Tagline
    f_tag = get_font(font_bold, 24)
    tag = 'AUTONOMIA NELLO STUDIO DAI 7 AI 12 ANNI'
    bbox_tag = draw.textbbox((0, 0), tag, font=f_tag)
    wtag = bbox_tag[2] - bbox_tag[0]
    draw.text((cx - wtag//2, cy + 275), tag, font=f_tag, fill='#94a3b8')

    img.save(os.path.join(out_dir, 'facebook_profile_picture.png'), 'PNG')
    img.save(os.path.join(out_dir, 'facebook_profile_picture.jpg'), 'JPEG', quality=95)
    img.save('public/images/facebook_profile_picture.png', 'PNG')
    print('Generated Ultra-Premium Facebook Profile Picture!')

# ==========================================
# 2. ULTRA-PREMIUM FACEBOOK COVER (1640x624)
# NO PRICE - LUXURY SHOWCASE
# ==========================================
def generate_fb_cover():
    w, h = 1640, 624
    img = Image.new('RGB', (w, h), color='#070b19')
    draw = ImageDraw.Draw(img)
    
    # Modern Dark Luxury Slate Gradient Background
    for x in range(w):
        rx = x / w
        r = int(8 + rx * 14)
        g = int(14 + rx * 20)
        b = int(32 + rx * 45)
        draw.line([(x, 0), (x, h)], fill=(r, g, b))
        
    # Ambient glows
    glow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    # Blue glow on left behind headline
    gdraw.ellipse([50, 40, 750, 560], fill=(56, 189, 248, 25))
    # Amber/indigo glow on right behind 3D bundle
    gdraw.ellipse([880, 80, 1620, 590], fill=(99, 102, 241, 35))
    glow = glow.filter(ImageFilter.GaussianBlur(55))
    img.paste(glow, (0, 0), glow)
    draw = ImageDraw.Draw(img)

    # Top accent line
    for x in range(w):
        ratio = x / w
        cr = int(56 + ratio * (245 - 56))
        cg = int(189 + ratio * (158 - 189))
        cb = int(248 + ratio * (11 - 248))
        draw.line([(x, 0), (x, 5)], fill=(cr, cg, cb))

    # --- LEFT SECTION: VALUE PROPOSITION (NO PRICE) ---
    # 1. Authority Tag Pill (Extra wide to never clip stars)
    draw.rounded_rectangle([70, 40, 540, 84], radius=22, fill='#1e293b', outline='#38bdf8', width=2)
    draw_star(draw, 96, 62, r=10, color='#fbbf24')
    draw.text((118, 51), 'METODO DIDATTICO VALIDATO · 2026', font=get_font(font_bold, 20), fill='#f8fafc')
    draw_star(draw, 514, 62, r=10, color='#fbbf24')

    # 2. Main High-Impact Headline
    draw.text((70, 104), 'KIT COMPRENSIONE', font=get_font(font_treb, 54), fill='#ffffff')
    draw.text((70, 164), 'DEL TESTO 2.0', font=get_font(font_treb, 54), fill='#38bdf8')

    # 3. Subheadline
    draw.text((70, 242), '587 Attività Didattiche Progressive + 4 Bonus Esclusivi', font=get_font(font_bold, 24), fill='#fbbf24')
    draw.text((70, 280), 'Insegna a tuo figlio a comprendere ogni testo e studiare da solo.', font=get_font(font_reg, 21), fill='#cbd5e1')

    # 4. Feature Checklist with Emerald Badges
    features = [
        '587 Schede Progressive Pronte da Stampare (PDF)',
        'Soluzioni Complete Incluse per Genitori',
        '4 Guide Didattiche Bonus di Approfondimento',
        'Garanzia Totale di 7 Giorni Soddisfatti o Rimborsati'
    ]
    for i, feat in enumerate(features):
        fy = 328 + i * 36
        draw.ellipse([70, fy + 2, 92, fy + 24], fill='#064e3b', outline='#10b981', width=1)
        draw_checkmark(draw, 74, fy + 5, size=14, color='#34d399', width=2)
        draw.text((105, fy), feat, font=get_font(font_bold, 20), fill='#f1f5f9')

    # 5. Luxury CTA Button (NO PRICE - spacious padding)
    btn_x1, btn_y1 = 70, 498
    btn_x2, btn_y2 = 530, 568
    # Emerald Gradient Button
    for by in range(btn_y1, btn_y2):
        bratio = (by - btn_y1) / (btn_y2 - btn_y1)
        br = int(16 + bratio * (5 - 16))
        bg = int(185 + bratio * (150 - 185))
        bb = int(129 + bratio * (105 - 129))
        draw.line([(btn_x1, by), (btn_x2, by)], fill=(br, bg, bb))
    draw.rounded_rectangle([btn_x1, btn_y1, btn_x2, btn_y2], radius=18, outline='#6ee7b7', width=2)
    
    f_btn = get_font(font_bold, 22)
    btn_text = 'SCOPRI IL METODO COMPLETO'
    draw.text((btn_x1 + 35, btn_y1 + 20), btn_text, font=f_btn, fill='#ffffff')
    draw_arrow(draw, btn_x1 + 420, btn_y1 + 26, size=20, color='#ffffff', width=3)

    # --- RIGHT SECTION: TRANSPARENT 3D BUNDLE MOCKUP & TRUST SEALS ---
    mockup_path = 'public/images/bundle_floodfill_transparent.png'
    if os.path.exists(mockup_path):
        bundle = Image.open(mockup_path).convert('RGBA')
        bw = 710
        bh = int(bundle.height * (bw / bundle.width))
        bundle_resized = bundle.resize((bw, bh), Image.Resampling.LANCZOS)
        
        # Add realistic ambient shadow beneath the bundle
        shadow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        sdraw = ImageDraw.Draw(shadow)
        bx = w - bw - 20
        by = h//2 - bh//2 + 5
        sdraw.ellipse([bx + 30, by + bh - 50, bx + bw - 30, by + bh + 30], fill=(0, 0, 0, 220))
        shadow = shadow.filter(ImageFilter.GaussianBlur(30))
        img.paste(shadow, (0, 0), shadow)
        
        # Paste transparent 3D bundle
        img.paste(bundle_resized, (bx, by), bundle_resized)

        # Floating Trust Badge 1 (Top Right of bundle)
        badge1_x1, badge1_y1 = w - 265, 40
        badge1_x2, badge1_y2 = w - 40, 102
        draw.rounded_rectangle([badge1_x1, badge1_y1, badge1_x2, badge1_y2], radius=14, fill='#1e293b', outline='#f59e0b', width=2)
        draw_star(draw, badge1_x1 + 22, badge1_y1 + 31, r=12, color='#fbbf24')
        draw.text((badge1_x1 + 45, badge1_y1 + 13), 'ACCESSO 100%', font=get_font(font_bold, 17), fill='#ffffff')
        draw.text((badge1_x1 + 45, badge1_y1 + 33), 'DIGITALE IMMEDIATO', font=get_font(font_bold, 14), fill='#38bdf8')

        # Floating Trust Badge 2 (Bottom Right)
        badge2_x1, badge2_y1 = w - 275, 520
        badge2_x2, badge2_y2 = w - 40, 582
        draw.rounded_rectangle([badge2_x1, badge2_y1, badge2_x2, badge2_y2], radius=14, fill='#064e3b', outline='#10b981', width=2)
        draw_checkmark(draw, badge2_x1 + 18, badge2_y1 + 18, size=18, color='#34d399', width=3)
        draw.text((badge2_x1 + 48, badge2_y1 + 14), 'GARANZIA 7 GIORNI', font=get_font(font_bold, 17), fill='#ffffff')
        draw.text((badge2_x1 + 48, badge2_y1 + 33), '100% SODDISFATTI', font=get_font(font_bold, 14), fill='#a7f3d0')

    img.save(os.path.join(out_dir, 'facebook_cover_wallpaper.png'), 'PNG')
    img.save(os.path.join(out_dir, 'facebook_cover_wallpaper.jpg'), 'JPEG', quality=95)
    img.save('public/images/facebook_cover_wallpaper.png', 'PNG')
    print('Generated Ultra-Premium Facebook Cover Wallpaper (NO PRICE)!')

if __name__ == '__main__':
    generate_fb_profile()
    generate_fb_cover()
    print('All upgraded Facebook assets generated successfully!')
