import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

mockup_path = 'public/images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src.png'
font_bold = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
font_reg = '/System/Library/Fonts/Supplemental/Arial.ttf'
font_treb = '/System/Library/Fonts/Supplemental/Trebuchet MS Bold.ttf'

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

def draw_checkmark(draw, x, y, size=20, color='#ffffff', width=3):
    p1 = (x, y + size * 0.5)
    p2 = (x + size * 0.35, y + size * 0.85)
    p3 = (x + size * 0.9, y + size * 0.15)
    draw.line([p1, p2], fill=color, width=width)
    draw.line([p2, p3], fill=color, width=width)

def create_paggins_image():
    w, h = 1200, 1200
    # Clean, subtle modern gradient background
    img = Image.new('RGB', (w, h), color='#f8fafc')
    draw = ImageDraw.Draw(img)
    
    # Soft radial background glow
    for r in range(600, 0, -20):
        color = (int(240 + (r/600)*15), int(244 + (r/600)*11), int(255))
        draw.ellipse([w//2 - r, h//2 - r, w//2 + r, h//2 + r], fill=color)
        
    # Top Header Badge
    draw.rounded_rectangle([w//2 - 300, 45, w//2 + 300, 110], radius=32, fill='#251a4a')
    draw_star(draw, w//2 - 250, 78, r=14, color='#fde047')
    draw.text((w//2 - 220, 62), 'METODO EDUCATIVO 2026', font=get_font(font_bold, 26), fill='#ffdd00')
    draw_star(draw, w//2 + 220, 78, r=14, color='#fde047')
    
    # Main Title
    draw.text((w//2 - 470, 135), 'KIT COMPRENSIONE DEL TESTO 2.0', font=get_font(font_treb, 50), fill='#1e293b')
    draw.text((w//2 - 380, 200), '587 Schede Pratiche + 4 Bonus Esclusivi Inclusi', font=get_font(font_bold, 28), fill='#64748b')
    
    # Paste the 3D bundle mockup in the center
    if os.path.exists(mockup_path):
        bundle = Image.open(mockup_path).convert('RGBA')
        bw = 960
        bh = int(bundle.height * (bw / bundle.width))
        bundle_resized = bundle.resize((bw, bh), Image.Resampling.LANCZOS)
        img.paste(bundle_resized, (w//2 - bw//2, 270), bundle_resized)
        
    # Bottom Benefit Bar
    draw.rounded_rectangle([60, h - 130, w - 60, h - 45], radius=24, fill='#0284c7')
    
    # Benefit 1
    draw_checkmark(draw, 110, h - 98, size=20, color='#ffffff', width=3)
    draw.text((140, h - 100), 'Accesso Immediato', font=get_font(font_bold, 24), fill='#ffffff')
    
    # Benefit 2
    draw_checkmark(draw, 470, h - 98, size=20, color='#ffffff', width=3)
    draw.text((500, h - 100), 'PDF Pronto da Stampare', font=get_font(font_bold, 24), fill='#ffffff')
    
    # Benefit 3
    draw_checkmark(draw, 880, h - 98, size=20, color='#ffffff', width=3)
    draw.text((910, h - 100), 'Garanzia di 7 Giorni', font=get_font(font_bold, 24), fill='#ffffff')
    
    # Save in both png and jpg formats
    img.save('paggins_product_cover.png')
    img.save('paggins_product_cover.jpg', quality=95)
    img.save('public/images/paggins_product_cover.png')
    img.save('public/images/paggins_product_cover.jpg', quality=95)
    print('Refined Paggins Product Cover (PNG and JPG)!')

create_paggins_image()
