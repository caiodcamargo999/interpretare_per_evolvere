import os
from PIL import Image, ImageDraw, ImageFont

font_bold_path = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
font_reg_path = '/System/Library/Fonts/Supplemental/Arial.ttf'
font_title_path = '/System/Library/Fonts/Supplemental/Trebuchet MS Bold.ttf'
font_italic_path = '/System/Library/Fonts/Supplemental/Arial Italic.ttf'
if not os.path.exists(font_italic_path):
    font_italic_path = font_reg_path

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

# 1. Create Italian School Test Paper (eb3fee05)
# "Classe 2ª - Verifica di Italiano | Voto: 4 (insufficiente)"
def create_italian_test_sheet():
    w, h = 1024, 600  # High-res 2x (will downscale to 512x300)
    img = Image.new('RGB', (w, h), color='#fbfbf8')
    draw = ImageDraw.Draw(img)
    
    # Paper grid / lines background
    for y in range(40, h, 36):
        draw.line([(30, y), (w-30, y)], fill='#e8ebf0', width=1)
    
    # Red left margin line
    draw.line([(120, 20), (120, h-20)], fill='#fecaca', width=2)
    
    # Header box on test paper
    draw.rectangle([140, 45, w-60, 220], outline='#374151', width=3)
    
    f_header = get_font(font_bold_path, 34)
    draw.text((160, 65), 'VERIFICA DI ITALIANO', font=f_header, fill='#1f2937')
    
    f_meta = get_font(font_reg_path, 28)
    draw.text((160, 115), 'Classe: 2ª Elementare     Sez: B', font=f_meta, fill='#374151')
    draw.text((160, 160), 'Alunno: _______________________', font=f_meta, fill='#374151')
    
    # Voto Box with Red Grade "4" (Insufficiente in Italian grading system)
    draw.rectangle([w-320, 60, w-80, 205], outline='#374151', width=2, fill='#ffffff')
    draw.text((w-300, 75), 'VOTO:', font=get_font(font_bold_path, 30), fill='#374151')
    
    # Handwritten style Red Mark "4" / "4,5"
    f_grade = get_font(font_title_path, 76)
    draw.text((w-200, 80), '4', font=f_grade, fill='#dc2626')
    
    # Teacher red comment
    f_note = get_font(font_italic_path, 28)
    draw.text((w-295, 160), '(Non sufficiente)', font=f_note, fill='#dc2626')
    draw.line([(w-210, 150), (w-150, 150)], fill='#dc2626', width=4)
    
    # Exercise 1 text
    f_ex_title = get_font(font_bold_path, 28)
    draw.text((140, 250), 'Esercizio 1: Leggi il testo e rispondi alle domande.', font=f_ex_title, fill='#1f2937')
    
    f_ex_text = get_font(font_reg_path, 26)
    draw.text((140, 295), '«Il piccolo scoiattolo raccoglieva le ghiande nel bosco prima dell\'inverno...»', font=f_ex_text, fill='#4b5563')
    
    draw.text((140, 360), '1. Perché lo scoiattolo raccoglie le ghiande?', font=get_font(font_bold_path, 26), fill='#1f2937')
    draw.text((160, 405), 'Risposta: Non lo so / Non ho capito il testo', font=get_font(font_italic_path, 26), fill='#6b7280')
    
    # Red X cross mark on the question
    draw.line([(135, 400), (155, 435)], fill='#dc2626', width=4)
    draw.line([(155, 400), (135, 435)], fill='#dc2626', width=4)
    draw.text((140, 455), '❌ "Testo non compreso. Rileggere con attenzione!"', font=get_font(font_italic_path, 26), fill='#dc2626')
    
    # Scale down for smooth anti-aliasing
    final_img = img.resize((512, 300), Image.Resampling.LANCZOS)
    
    final_img.save('images/eb3fee05-db30-4bd8-8399-9b02593f5a96-misc-src.png')
    final_img.resize((300, 176), Image.Resampling.LANCZOS).save('images/eb3fee05-db30-4bd8-8399-9b02593f5a96-misc-src_1.png')
    final_img.save('images/eb3fee05-db30-4bd8-8399-9b02593f5a96-misc-src_2.png')
    print('Created Italian School Test Sheet (eb3fee05)!')

# 2. Create Italian WhatsApp Success Bubble (dc4fa02a)
def create_italian_whatsapp_bubble():
    w, h = 1024, 600  # High-res 2x (will downscale to 512x300)
    img = Image.new('RGB', (w, h), color='#efeae2')
    draw = ImageDraw.Draw(img)
    
    # Subtle WhatsApp pattern / wallpaper feel
    draw.rectangle([0, 0, w, h], fill='#efeae2')
    
    # White WhatsApp message bubble
    draw.rounded_rectangle([30, 30, w-30, h-30], radius=32, fill='#ffffff')
    
    # Little bubble tail on the left
    draw.polygon([(30, 70), (10, 50), (30, 90)], fill='#ffffff')
    
    f_msg = get_font(font_reg_path, 34)
    line_spacing = 52
    lines = [
        'Ho iniziato a usare le schede con mio',
        'figlio la settimana scorsa e ho già notato',
        'una grande differenza. Prima si bloccava su',
        'qualsiasi testo, si innervosiva e diceva che non',
        'capiva nulla. Ora legge, fa le domande e mi',
        'chiama persino per mostrarmi cosa è riuscito',
        'a fare da solo. Non l\'avevo mai visto così sicuro!'
    ]
    
    for i, line in enumerate(lines):
        draw.text((60, 60 + i * line_spacing), line, font=f_msg, fill='#111827')
        
    # Timestamp & double blue checkmark
    f_time = get_font(font_reg_path, 26)
    draw.text((w-160, h-75), '19:00', font=f_time, fill='#6b7280')
    # Double checkmark
    draw.text((w-85, h-75), '✓✓', font=get_font(font_bold_path, 26), fill='#3b82f6')
    
    final_img = img.resize((512, 300), Image.Resampling.LANCZOS)
    
    final_img.save('images/dc4fa02a-691a-42a1-9a5c-26446c7bc6f6-misc-src.png')
    final_img.save('images/dc4fa02a-691a-42a1-9a5c-26446c7bc6f6-misc-src_1.png')
    final_img.resize((300, 176), Image.Resampling.LANCZOS).save('images/dc4fa02a-691a-42a1-9a5c-26446c7bc6f6-misc-src_2.png')
    print('Created Italian WhatsApp Bubble (dc4fa02a)!')

create_italian_test_sheet()
create_italian_whatsapp_bubble()
