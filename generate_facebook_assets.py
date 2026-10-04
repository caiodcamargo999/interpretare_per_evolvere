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
        radius = r if i % 2 == 0 else r * 0.45
        px = cx + radius * math.cos(angle)
        py = cy + radius * math.sin(angle)
        points.append((px, py))
    draw.polygon(points, fill=color)

def draw_checkmark(draw, x, y, size=20, color='#00d26a', width=3):
    p1 = (x, y + size * 0.5)
    p2 = (x + size * 0.35, y + size * 0.85)
    p3 = (x + size * 0.9, y + size * 0.15)
    draw.line([p1, p2], fill=color, width=width)
    draw.line([p2, p3], fill=color, width=width)

def draw_arrow(draw, x, y, size=16, color='#ffffff', width=3):
    draw.line([(x, y + size//2), (x + size, y + size//2)], fill=color, width=width)
    draw.line([(x + size - size//3, y), (x + size, y + size//2)], fill=color, width=width)
    draw.line([(x + size - size//3, y + size), (x + size, y + size//2)], fill=color, width=width)

# ==========================================
# 1. FACEBOOK PROFILE PICTURE (1080x1080)
# ==========================================
def generate_fb_profile():
    w, h = 1080, 1080
    img = Image.new('RGB', (w, h), color='#1e1438')
    draw = ImageDraw.Draw(img)
    
    # Modern Gradient background
    for y in range(h):
        r = int(30 + (y / h) * 25)
        g = int(20 + (y / h) * 30)
        b = int(65 + (y / h) * 60)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
        
    cx, cy = w // 2, h // 2
    
    # Outer Circle border (Safe inside 1080 circle)
    r_outer = 480
    draw.ellipse([cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer], outline='#ffb703', width=12)
    draw.ellipse([cx - r_outer + 20, cy - r_outer + 20, cx + r_outer - 20, cy + r_outer - 20], fill='#271b4a', outline='#6366f1', width=6)
    
    # Top Stars
    draw_star(draw, cx - 80, cy - 260, r=16, color='#ffdd00')
    draw_star(draw, cx, cy - 285, r=24, color='#ffdd00')
    draw_star(draw, cx + 80, cy - 260, r=16, color='#ffdd00')
    
    # Open Book Illustration
    bw, bh = 220, 140
    # Left page
    draw.polygon([
        (cx - 12, cy - 100),
        (cx - bw, cy - 140),
        (cx - bw, cy + bh - 140),
        (cx - 12, cy + bh - 100)
    ], fill='#ffffff')
    # Right page
    draw.polygon([
        (cx + 12, cy - 100),
        (cx + bw, cy - 140),
        (cx + bw, cy + bh - 140),
        (cx + 12, cy + bh - 100)
    ], fill='#f1f5f9')
    
    # Lines on open book pages
    for i in range(4):
        py = cy - 100 + (i + 1) * 22
        draw.line([(cx - bw + 35, py), (cx - 30, py + 14)], fill='#94a3b8', width=4)
        draw.line([(cx + 30, py + 14), (cx + bw - 35, py)], fill='#94a3b8', width=4)
        
    # Main Brand Name inside circle
    f_title = get_font(font_treb, 54)
    bbox_t = draw.textbbox((0, 0), 'IMPARARE & CAPIRE', font=f_title)
    tw = bbox_t[2] - bbox_t[0]
    draw.text((cx - tw//2, cy + 90), 'IMPARARE & CAPIRE', font=f_title, fill='#ffffff')
    
    # Badge Pill
    draw.rounded_rectangle([cx - 230, cy + 180, cx + 230, cy + 245], radius=22, fill='#ffb703')
    f_pill = get_font(font_bold, 30)
    bbox_p = draw.textbbox((0, 0), 'EDUCAZIONE PRIMARIA', font=f_pill)
    pw = bbox_p[2] - bbox_p[0]
    draw.text((cx - pw//2, cy + 196), 'EDUCAZIONE PRIMARIA', font=f_pill, fill='#1e1438')
    
    # Subtitle
    f_sub = get_font(font_bold, 26)
    bbox_s = draw.textbbox((0, 0), 'METODO COMPRENSIONE 2.0', font=f_sub)
    sw = bbox_s[2] - bbox_s[0]
    draw.text((cx - sw//2, cy + 275), 'METODO COMPRENSIONE 2.0', font=f_sub, fill='#38bdf8')
    
    img.save(os.path.join(out_dir, 'facebook_profile_picture.png'))
    img.save(os.path.join(out_dir, 'facebook_profile_picture.jpg'), quality=95)
    img.save('public/images/facebook_profile_picture.png')
    print('Generated Refined Facebook Profile Picture!')

# ==========================================
# 2. FACEBOOK COVER / WALLPAPER (1640x624)
# ==========================================
def generate_fb_cover():
    w, h = 1640, 624
    # Clean white/light-indigo background for maximum contrast with the 3D Mockup
    img = Image.new('RGB', (w, h), color='#ffffff')
    draw = ImageDraw.Draw(img)
    
    # Soft background gradient from left to right
    for x in range(w):
        r = int(248 + (x / w) * 7)
        g = int(250 + (x / w) * 5)
        b = int(255)
        draw.line([(x, 0), (x, h)], fill=(r, g, b))
        
    # Top subtle decorative banner bar
    draw.rectangle([0, 0, w, 10], fill='#4361ee')
    
    # Left Content Area (Text & Benefits)
    # Badge
    draw.rounded_rectangle([70, 45, 470, 95], radius=25, fill='#251a4a')
    draw_star(draw, 100, 70, r=12, color='#fde047')
    draw.text((125, 57), 'METODO DIDATTICO 2026', font=get_font(font_bold, 24), fill='#ffdd00')
    draw_star(draw, 440, 70, r=12, color='#fde047')
    
    # Main Headline
    draw.text((70, 115), 'KIT COMPRENSIONE', font=get_font(font_treb, 54), fill='#1e293b')
    draw.text((70, 175), 'DEL TESTO 2.0', font=get_font(font_treb, 54), fill='#00a1e6')
    
    # Subtitle
    draw.text((70, 255), '587 Attività Didattiche Progressive per Bambini dai 7 ai 12 Anni', font=get_font(font_bold, 24), fill='#334155')
    draw.text((70, 290), 'Impara a comprendere ogni testo e a studiare in piena autonomia.', font=get_font(font_reg, 22), fill='#64748b')
    
    # 3 Checkmark bullets
    bullets = [
        'Pronto da Stampare (File PDF ad Alta Risoluzione)',
        'Soluzioni Complete Incluse per i Genitori',
        '4 Bonus Esclusivi per un Apprendimento Completo'
    ]
    for i, b in enumerate(bullets):
        by = 345 + i * 42
        draw_checkmark(draw, 75, by + 4, size=18, color='#059669', width=3)
        draw.text((105, by), b, font=get_font(font_bold, 21), fill='#1e293b')
        
    # CTA Pill
    draw.rounded_rectangle([70, 490, 490, 560], radius=20, fill='#0284c7')
    draw.text((105, 508), 'ACCESSO IMMEDIATO · €27', font=get_font(font_bold, 24), fill='#ffffff')
    draw_arrow(draw, 440, 514, size=20, color='#ffffff', width=3)
    
    # Right Side: 3D Bundle Mockup
    mockup_path = 'public/images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src.png'
    if os.path.exists(mockup_path):
        bundle = Image.open(mockup_path).convert('RGBA')
        bw = 670
        bh = int(bundle.height * (bw / bundle.width))
        bundle_resized = bundle.resize((bw, bh), Image.Resampling.LANCZOS)
        img.paste(bundle_resized, (w - bw - 20, h//2 - bh//2 + 10), bundle_resized)
        
    img.save(os.path.join(out_dir, 'facebook_cover_wallpaper.png'))
    img.save(os.path.join(out_dir, 'facebook_cover_wallpaper.jpg'), quality=95)
    img.save('public/images/facebook_cover_wallpaper.png')
    print('Generated Refined Facebook Cover Wallpaper!')

if __name__ == '__main__':
    generate_fb_profile()
    generate_fb_cover()
    print('All refined Facebook assets generated!')
