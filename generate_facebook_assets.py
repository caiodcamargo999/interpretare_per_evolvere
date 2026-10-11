import os, math, shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter

out_dir = 'facebook_assets'
os.makedirs(out_dir, exist_ok=True)
os.makedirs('public/images', exist_ok=True)

artifact_dir = '/Users/lenovo/.gemini/antigravity-ide/brain/4f6a13cf-788b-43b9-a736-315fad1def3a'
ai_wallpaper_path = os.path.join(artifact_dir, 'fb_cover_edu_wallpaper_1791587758847.jpg')

font_bold = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
font_reg = '/System/Library/Fonts/Supplemental/Arial.ttf'
font_treb = '/System/Library/Fonts/Supplemental/Trebuchet MS Bold.ttf'
font_georgia = '/System/Library/Fonts/Supplemental/Georgia Bold.ttf'

def get_font(path, size, index=0):
    try:
        return ImageFont.truetype(path, size, index=index)
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
# OPTION 1: HIGH-CONVERTING ADVERTISING SHOWCASE (1640x624)
# ==========================================
def generate_cover_option_1():
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
    gdraw.ellipse([50, 40, 750, 560], fill=(56, 189, 248, 25))
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

    # --- LEFT SECTION: VALUE PROPOSITION (SAFE FROM AVATAR OVERLAY) ---
    # 1. Authority Tag Pill
    draw.rounded_rectangle([70, 40, 540, 84], radius=22, fill='#1e293b', outline='#38bdf8', width=2)
    draw_star(draw, 96, 62, r=10, color='#fbbf24')
    draw.text((118, 51), 'METODO DIDATTICO VALIDATO · 2026', font=get_font(font_bold, 20), fill='#f8fafc')
    draw_star(draw, 514, 62, r=10, color='#fbbf24')

    # 2. Main High-Impact Headline
    draw.text((70, 104), 'KIT COMPRENSIONE', font=get_font(font_treb, 54), fill='#ffffff')
    draw.text((70, 164), 'DEL TESTO 2.0', font=get_font(font_treb, 54), fill='#38bdf8')

    # 3. Subheadline
    draw.text((70, 242), '587 Attivita Didattiche Progressive + 4 Bonus Esclusivi', font=get_font(font_bold, 24), fill='#fbbf24')
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

    # 5. Luxury CTA Button
    btn_x1, btn_y1 = 70, 498
    btn_x2, btn_y2 = 530, 568
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
        
        # Shadow
        shadow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        sdraw = ImageDraw.Draw(shadow)
        bx = w - bw - 20
        by = h//2 - bh//2 + 5
        sdraw.ellipse([bx + 30, by + bh - 50, bx + bw - 30, by + bh + 30], fill=(0, 0, 0, 220))
        shadow = shadow.filter(ImageFilter.GaussianBlur(30))
        img.paste(shadow, (0, 0), shadow)
        img.paste(bundle_resized, (bx, by), bundle_resized)

        # Badges
        badge1_x1, badge1_y1 = w - 265, 40
        badge1_x2, badge1_y2 = w - 40, 102
        draw.rounded_rectangle([badge1_x1, badge1_y1, badge1_x2, badge1_y2], radius=14, fill='#1e293b', outline='#f59e0b', width=2)
        draw_star(draw, badge1_x1 + 22, badge1_y1 + 31, r=12, color='#fbbf24')
        draw.text((badge1_x1 + 45, badge1_y1 + 13), 'ACCESSO 100%', font=get_font(font_bold, 17), fill='#ffffff')
        draw.text((badge1_x1 + 45, badge1_y1 + 33), 'DIGITALE IMMEDIATO', font=get_font(font_bold, 14), fill='#38bdf8')

        badge2_x1, badge2_y1 = w - 275, 520
        badge2_x2, badge2_y2 = w - 40, 582
        draw.rounded_rectangle([badge2_x1, badge2_y1, badge2_x2, badge2_y2], radius=14, fill='#064e3b', outline='#10b981', width=2)
        draw_checkmark(draw, badge2_x1 + 18, badge2_y1 + 18, size=18, color='#34d399', width=3)
        draw.text((badge2_x1 + 48, badge2_y1 + 14), 'GARANZIA 7 GIORNI', font=get_font(font_bold, 17), fill='#ffffff')
        draw.text((badge2_x1 + 48, badge2_y1 + 33), '100% SODDISFATTI', font=get_font(font_bold, 14), fill='#a7f3d0')

    img.save(os.path.join(out_dir, 'facebook_cover_option_1_ad_showcase.png'), 'PNG')
    img.save(os.path.join(out_dir, 'facebook_cover_option_1_ad_showcase.jpg'), 'JPEG', quality=95)
    img.save(os.path.join(out_dir, 'facebook_cover_wallpaper.png'), 'PNG')
    img.save(os.path.join(out_dir, 'facebook_cover_wallpaper.jpg'), 'JPEG', quality=95)
    shutil.copy(os.path.join(out_dir, 'facebook_cover_option_1_ad_showcase.jpg'), os.path.join(artifact_dir, 'facebook_cover_option_1_ad_showcase.jpg'))
    print('Generated Option 1: Ad Showcase!')

# ==========================================
# OPTION 2: PHOTOREALISTIC WARM STUDY BACKDROP WITH 3D BUNDLE (1640x624)
# ==========================================
def generate_cover_option_2():
    w, h = 1640, 624
    if not os.path.exists(ai_wallpaper_path):
        print('AI wallpaper not found, skipping option 2')
        return

    base_ai = Image.open(ai_wallpaper_path).convert('RGB')
    
    # Crop to 1640x624 with artistic center-crop
    target_ratio = w / h
    img_ratio = base_ai.width / base_ai.height
    if img_ratio > target_ratio:
        new_w = int(base_ai.height * target_ratio)
        offset = (base_ai.width - new_w) // 2
        cropped = base_ai.crop((offset, 0, offset + new_w, base_ai.height))
    else:
        new_h = int(base_ai.width / target_ratio)
        offset = (base_ai.height - new_h) // 2
        cropped = base_ai.crop((0, offset, base_ai.width, offset + new_h))
        
    bg = cropped.resize((w, h), Image.Resampling.LANCZOS)
    
    # Add subtle luxury vignette and dark overlay on the left to make text pop
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    
    # Left dark gradient panel for high readability
    for x in range(int(w * 0.65)):
        ratio = 1.0 - (x / (w * 0.65))
        alpha = int(ratio * 210)
        odraw.line([(x, 0), (x, h)], fill=(7, 11, 25, alpha))
        
    # Top & bottom subtle shade
    for y in range(80):
        alpha = int((1.0 - y / 80) * 120)
        odraw.line([(0, y), (w, y)], fill=(0, 0, 0, alpha))
        odraw.line([(0, h - 1 - y), (w, h - 1 - y)], fill=(0, 0, 0, alpha))

    # Glassmorphism Card for Left Content
    odraw.rounded_rectangle([50, 35, 780, 580], radius=24, fill=(11, 17, 32, 185), outline=(56, 189, 248, 140), width=2)
    
    bg = Image.alpha_composite(bg.convert('RGBA'), overlay).convert('RGBA')

    # --- RIGHT SECTION: 3D BUNDLE ---
    mockup_path = 'public/images/bundle_floodfill_transparent.png'
    if os.path.exists(mockup_path):
        bundle = Image.open(mockup_path).convert('RGBA')
        bw = 700
        bh = int(bundle.height * (bw / bundle.width))
        bundle_resized = bundle.resize((bw, bh), Image.Resampling.LANCZOS)
        
        # Soft glowing back-illumination
        glow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow)
        bx = w - bw - 20
        by = h//2 - bh//2 + 5
        gdraw.ellipse([bx + 50, by + 40, bx + bw - 50, by + bh - 20], fill=(245, 158, 11, 55))
        glow = glow.filter(ImageFilter.GaussianBlur(50))
        bg = Image.alpha_composite(bg, glow)
        
        # Shadow
        shadow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        sdraw = ImageDraw.Draw(shadow)
        sdraw.ellipse([bx + 30, by + bh - 55, bx + bw - 30, by + bh + 25], fill=(0, 0, 0, 240))
        shadow = shadow.filter(ImageFilter.GaussianBlur(25))
        bg = Image.alpha_composite(bg, shadow)
        
        bg.paste(bundle_resized, (bx, by), bundle_resized)

    # Convert to RGB for drawing
    bg = bg.convert('RGB')
    draw = ImageDraw.Draw(bg)

    # 1. Authority Tag Pill
    draw.rounded_rectangle([75, 55, 525, 98], radius=21, fill='#1e293b', outline='#38bdf8', width=2)
    draw_star(draw, 98, 76, r=10, color='#fbbf24')
    draw.text((118, 65), 'METODO DIDATTICO VALIDATO · 2026', font=get_font(font_bold, 19), fill='#f8fafc')
    draw_star(draw, 502, 76, r=10, color='#fbbf24')

    # 2. Headline
    draw.text((75, 118), 'KIT COMPRENSIONE', font=get_font(font_treb, 50), fill='#ffffff')
    draw.text((75, 172), 'DEL TESTO 2.0', font=get_font(font_treb, 50), fill='#38bdf8')

    # 3. Subheadline
    draw.text((75, 245), '587 Attivita Didattiche + 4 Bonus Esclusivi', font=get_font(font_bold, 22), fill='#fbbf24')
    draw.text((75, 280), 'Comprensione del testo autonoma per bambini 7-12 anni.', font=get_font(font_reg, 19), fill='#e2e8f0')

    # 4. Feature Checklist
    features = [
        '587 Schede Stampabili ad Alta Risoluzione',
        'Soluzioni Complete per Autoverifica e Genitori',
        '4 Quaderni Didattici Esclusivi Inclusi',
        'Garanzia Soddisfatti o Rimborsati 7 Giorni'
    ]
    for i, feat in enumerate(features):
        fy = 328 + i * 36
        draw.ellipse([75, fy + 2, 97, fy + 24], fill='#064e3b', outline='#10b981', width=1)
        draw_checkmark(draw, 79, fy + 5, size=14, color='#34d399', width=2)
        draw.text((108, fy), feat, font=get_font(font_bold, 19), fill='#f8fafc')

    # 5. CTA Button
    btn_x1, btn_y1 = 75, 495
    btn_x2, btn_y2 = 490, 560
    for by in range(btn_y1, btn_y2):
        bratio = (by - btn_y1) / (btn_y2 - btn_y1)
        btn_r = int(16 + bratio * (5 - 16))
        btn_g = int(185 + bratio * (150 - 185))
        btn_b = int(129 + bratio * (105 - 129))
        draw.line([(btn_x1, by), (btn_x2, by)], fill=(btn_r, btn_g, btn_b))
    draw.rounded_rectangle([btn_x1, btn_y1, btn_x2, btn_y2], radius=16, outline='#6ee7b7', width=2)
    draw.text((btn_x1 + 30, btn_y1 + 18), 'ACCEDI AL METODO COMPLETO', font=get_font(font_bold, 20), fill='#ffffff')
    draw_arrow(draw, btn_x1 + 380, btn_y1 + 24, size=18, color='#ffffff', width=3)

    if os.path.exists(mockup_path):
        # Top Badge
        badge1_x1, badge1_y1 = w - 265, 40
        badge1_x2, badge1_y2 = w - 40, 102
        draw.rounded_rectangle([badge1_x1, badge1_y1, badge1_x2, badge1_y2], radius=14, fill='#1e293b', outline='#f59e0b', width=2)
        draw_star(draw, badge1_x1 + 22, badge1_y1 + 31, r=12, color='#fbbf24')
        draw.text((badge1_x1 + 45, badge1_y1 + 13), 'ACCESSO 100%', font=get_font(font_bold, 17), fill='#ffffff')
        draw.text((badge1_x1 + 45, badge1_y1 + 33), 'DIGITALE IMMEDIATO', font=get_font(font_bold, 14), fill='#38bdf8')

        # Bottom Badge
        badge2_x1, badge2_y1 = w - 275, 520
        badge2_x2, badge2_y2 = w - 40, 582
        draw.rounded_rectangle([badge2_x1, badge2_y1, badge2_x2, badge2_y2], radius=14, fill='#064e3b', outline='#10b981', width=2)
        draw_checkmark(draw, badge2_x1 + 18, badge2_y1 + 18, size=18, color='#34d399', width=3)
        draw.text((badge2_x1 + 48, badge2_y1 + 14), 'GARANZIA 7 GIORNI', font=get_font(font_bold, 17), fill='#ffffff')
        draw.text((badge2_x1 + 48, badge2_y1 + 33), '100% SODDISFATTI', font=get_font(font_bold, 14), fill='#a7f3d0')

    bg.save(os.path.join(out_dir, 'facebook_cover_option_2_warm_study_bundle.png'), 'PNG')
    bg.save(os.path.join(out_dir, 'facebook_cover_option_2_warm_study_bundle.jpg'), 'JPEG', quality=95)
    shutil.copy(os.path.join(out_dir, 'facebook_cover_option_2_warm_study_bundle.jpg'), os.path.join(artifact_dir, 'facebook_cover_option_2_warm_study_bundle.jpg'))
    print('Generated Option 2: Warm Study Bundle!')

# ==========================================
# OPTION 3: PURE PHOTOREALISTIC WARM WALLPAPER (1640x624)
# ==========================================
def generate_cover_option_3():
    w, h = 1640, 624
    if not os.path.exists(ai_wallpaper_path):
        return

    base_ai = Image.open(ai_wallpaper_path).convert('RGB')
    target_ratio = w / h
    img_ratio = base_ai.width / base_ai.height
    if img_ratio > target_ratio:
        new_w = int(base_ai.height * target_ratio)
        offset = (base_ai.width - new_w) // 2
        cropped = base_ai.crop((offset, 0, offset + new_w, base_ai.height))
    else:
        new_h = int(base_ai.width / target_ratio)
        offset = (base_ai.height - new_h) // 2
        cropped = base_ai.crop((0, offset, base_ai.width, offset + new_h))
        
    bg = cropped.resize((w, h), Image.Resampling.LANCZOS)
    bg.save(os.path.join(out_dir, 'facebook_cover_option_3_photorealistic_warm_wallpaper.png'), 'PNG')
    bg.save(os.path.join(out_dir, 'facebook_cover_option_3_photorealistic_warm_wallpaper.jpg'), 'JPEG', quality=95)
    shutil.copy(os.path.join(out_dir, 'facebook_cover_option_3_photorealistic_warm_wallpaper.jpg'), os.path.join(artifact_dir, 'facebook_cover_option_3_photorealistic_warm_wallpaper.jpg'))
    print('Generated Option 3: Clean Wallpaper!')

if __name__ == '__main__':
    generate_cover_option_1()
    generate_cover_option_2()
    generate_cover_option_3()
    print('All wallpaper & cover options created successfully!')
