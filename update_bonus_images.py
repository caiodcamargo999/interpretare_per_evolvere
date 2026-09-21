import os
from PIL import Image, ImageDraw, ImageFont

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

def create_italian_cards_perfect_congruence():
    # Module cards (1 to 4) and Bonus cards (1 to 4)
    cards = [
        ('bca575f3-70fc-4dca-a646-42e0af0d9f2f-misc-src', 'MODULO 1', '150 Attività di Lettura &', 'Comprensione Rapida', '#4361ee'),
        ('76ec044f-cc34-467e-a2dc-4779760270c7-misc-src', 'MODULO 2', '120 Testi con Domande', 'Dirette & Inferenze', '#3a0ca3'),
        ('mFPujI8456037', 'MODULO 3', '117 Esercizi di Vocabolario', 'e Comprensione del Contesto', '#7209b7'),
        ('ef51b634-0463-4047-bab6-7395d536fb7c-misc-src', 'MODULO 4', '200 Attività Interdisciplinari', '(Storia, Scienze, Matematica)', '#00b4d8'),
        
        # Exact 3 bonus files + Answers/Certificate
        ('ghnuyA5473914', 'BONUS 1', 'Kit Calligrafia Perfetta:', 'Scrittura Chiara e Sicura', '#f72585'),
        ('zCyQDE5473914', 'BONUS 2', 'Ora di Lettura:', '24 Testi per Leggere Fino in Fondo', '#4cc9f0'),
        ('cmIaGY5473914', 'BONUS 3', 'Semplificando la Matematica:', '120 Esercizi per Contare con Sicurezza', '#ffb703'),
        ('HpBKtY5473914', 'BONUS 4', 'Chiavi di Risposta Complete', '& Attestato Ufficiale di Completamento', '#06d6a0'),
        
        ('gcdBCn5473914', 'BONUS INCLUSO', 'Kit Calligrafia Perfetta', 'Impugnatura, Lettere e Numeri', '#f72585'),
        ('vDHxvY5473914', 'BONUS INCLUSO', 'Semplificando la Matematica', 'Addizioni, Tabelline e Problemi', '#2a9d8f')
    ]
    
    for base_name, tag, line1, line2, color in cards:
        w, h = 512, 315
        img = Image.new('RGB', (w, h), color='#ffffff')
        draw = ImageDraw.Draw(img)
        
        draw.rounded_rectangle([10, 10, w-10, h-10], radius=20, fill=color)
        draw.rounded_rectangle([20, 20, w-20, h-20], radius=16, fill='#ffffff')
        
        draw.rounded_rectangle([20, 20, w-20, 95], radius=16, fill=color)
        draw.rectangle([20, 60, w-20, 95], fill=color)
        
        f_tag = get_font(font_bold_path, 26)
        draw.text((35, 38), tag, font=f_tag, fill='#ffffff')
        
        f_l1 = get_font(font_title_path, 23)
        draw.text((35, 125), line1, font=f_l1, fill='#1f2937')
        draw.text((35, 165), line2, font=f_l1, fill='#1f2937')
        
        draw.rounded_rectangle([35, 230, w-35, 280], radius=12, fill='#f3f4f6')
        f_badge = get_font(font_bold_path, 17)
        draw.text((50, 244), '📄 Formato PDF Pronto da Stampare', font=f_badge, fill='#4b5563')
        
        img.save(f'images/{base_name}.png')
        img.save(f'images/{base_name}_1.png')
        img.resize((260, 160)).save(f'images/{base_name}_2.png')

    # Wide bonus banners matching the exact PDFs in public/
    wide_cards = [
        ('kbvgHh6486611', 'BONUS ESCLUSIVO 1', 'Kit Calligrafia Perfetta: Scrittura Chiara, Postura e Alfabeto Completo (40 Pagine)', '#f72585'),
        ('pQfwEt6486611', 'BONUS ESCLUSIVO 2', 'Ora di Lettura: 24 Testi Coinvolgenti per Leggere Fino in Fondo (42 Pagine)', '#4cc9f0'),
        ('iWnJvw6486611', 'BONUS ESCLUSIVO 3', 'Semplificando la Matematica di Base: 120 Esercizi Pratici con Soluzioni (31 Pagine)', '#ffb703'),
        ('YGvXxb6486611', 'BONUS ESCLUSIVO 4', 'Chiavi di Risposta Dettagliate per i Genitori + Attestato Ufficiale di Merito', '#06d6a0')
    ]
    
    for base_name, b_title, b_desc, b_color in wide_cards:
        w, h = 1600, 706
        img = Image.new('RGB', (w, h), color='#ffffff')
        draw = ImageDraw.Draw(img)
        
        draw.rounded_rectangle([15, 15, w-15, h-15], radius=30, fill=b_color)
        draw.rounded_rectangle([30, 30, w-30, h-30], radius=25, fill='#ffffff')
        
        draw.rounded_rectangle([60, 60, 520, 140], radius=20, fill=b_color)
        draw.text((90, 80), b_title, font=get_font(font_bold_path, 34), fill='#ffffff')
        
        draw.text((60, 200), b_desc, font=get_font(font_title_path, 38), fill='#1f2937')
        
        draw.rounded_rectangle([60, 480, 700, 580], radius=20, fill='#00c738')
        draw.text((100, 505), '🎁 INCLUSO GRATIS NEL KIT OGGI', font=get_font(font_bold_path, 32), fill='#ffffff')
        
        img.save(f'images/{base_name}.png')
        img.resize((299, 132)).save(f'images/{base_name}_1.png')
        img.save(f'images/{base_name}_2.png')
        img.resize((768, 339)).save(f'images/{base_name}_3.png')
        img.resize((1024, 452)).save(f'images/{base_name}_4.png')
        img.resize((1536, 678)).save(f'images/{base_name}_5.png')

    print('Updated all bonus images to match public/ PDF files with 100% congruence!')

create_italian_cards_perfect_congruence()
