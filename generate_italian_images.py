import os
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

def save_variants(base_img, name_pattern, ext='webp'):
    # save main
    main_name = f'images/{name_pattern}.{ext}'
    base_img.save(main_name)
    print(f'Saved {main_name}')

# 1. Generate Desktop Hero Banner (1200x724)
def create_desktop_hero():
    w, h = 1200, 724
    img = Image.new('RGB', (w, h), color='#1e1438')
    draw = ImageDraw.Draw(img)
    
    # Background gradient / decorative shapes
    for y in range(h):
        r = int(35 + (y / h) * 20)
        g = int(20 + (y / h) * 25)
        b = int(70 + (y / h) * 45)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
        
    # Decorative header elements
    draw.rounded_rectangle([60, 40, 420, 85], radius=22, fill='#ffb703')
    f_badge = get_font(font_bold_path, 20)
    draw.text((80, 52), '⭐ METODO EDUCATIVO 2026', font=f_badge, fill='#1e1438')
    
    # Main Headline
    f_title = get_font(font_title_path, 54)
    draw.text((60, 110), 'KIT COMPRENSIONE', font=f_title, fill='#ffffff')
    draw.text((60, 175), 'DEL TESTO 2.0', font=f_title, fill='#00d26a')
    
    # Subtitle
    f_sub = get_font(font_bold_path, 24)
    draw.text((60, 260), '587 Attività Pratiche per Allenare la Lettura ogni Giorno', font=f_sub, fill='#f3f4f6')
    draw.text((60, 295), 'e Superare le Difficoltà in Tutte le Materie Scolastiche.', font=f_sub, fill='#f3f4f6')
    
    # 4 Key Features Pill badges
    f_pill = get_font(font_bold_path, 18)
    pills = [
        '✅ Per Bambini dai 7 ai 12 Anni',
        '✅ Pronto da Stampare o Usare a Schermo',
        '✅ Risultati Visibili in 15 Minuti al Giorno',
        '✅ Con Soluzioni Complete per i Genitori'
    ]
    for i, pill in enumerate(pills):
        py = 360 + i * 50
        draw.rounded_rectangle([60, py, 620, py + 40], radius=10, fill='#2c2250', outline='#4a3b7a', width=2)
        draw.text((75, py + 9), pill, font=f_pill, fill='#ffffff')

    # Right side 3D book mockup / graphic box
    draw.rounded_rectangle([680, 60, 1140, 660], radius=25, fill='#251a4a', outline='#f72585', width=4)
    
    # Inner card
    draw.rounded_rectangle([710, 90, 1110, 630], radius=20, fill='#ffffff')
    draw.rounded_rectangle([710, 90, 1110, 220], radius=20, fill='#4361ee')
    
    f_card_title = get_font(font_title_path, 32)
    draw.text((735, 115), '587 SCHEDE', font=f_card_title, fill='#ffdd00')
    draw.text((735, 160), 'DIDATTICHE PRATICHE', font=f_card_title, fill='#ffffff')
    
    f_card_body = get_font(font_bold_path, 20)
    card_items = [
        '📘 Modulo 1: Lettura Rapida',
        '📙 Modulo 2: Domande & Inferenze',
        '📗 Modulo 3: Vocabolario Attivo',
        '📕 Modulo 4: Testi Interdisciplinari',
        '🎁 4 Bonus Esclusivi Inclusi'
    ]
    for i, item in enumerate(card_items):
        draw.text((740, 250 + i * 50), item, font=f_card_body, fill='#333333')
        
    draw.rounded_rectangle([735, 530, 1085, 600], radius=15, fill='#00a1e6')
    f_cta = get_font(font_bold_path, 22)
    draw.text((760, 550), 'ACCESSO IMMEDIATO · €27', font=f_cta, fill='#ffffff')
    
    # Save main & responsive sizes
    img.save('images/dppDQD5163414.webp')
    img.resize((300, 181)).save('images/dppDQD5163414_1.webp')
    img.resize((768, 463)).save('images/dppDQD5163414_2.webp')
    img.resize((1024, 618)).save('images/dppDQD5163414_3.webp')
    img.save('images/dppDQD5163414_4.webp')
    print('Created Italian Desktop Banner!')

# 2. Generate Mobile Hero Banner (1080x1920)
def create_mobile_hero():
    w, h = 1080, 1920
    img = Image.new('RGB', (w, h), color='#1e1438')
    draw = ImageDraw.Draw(img)
    
    for y in range(h):
        r = int(35 + (y / h) * 20)
        g = int(20 + (y / h) * 25)
        b = int(70 + (y / h) * 45)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
        
    draw.rounded_rectangle([80, 70, 600, 140], radius=35, fill='#ffb703')
    f_badge = get_font(font_bold_path, 32)
    draw.text((120, 88), '⭐ METODO EDUCATIVO 2026', font=f_badge, fill='#1e1438')
    
    f_title = get_font(font_title_path, 74)
    draw.text((80, 180), 'KIT COMPRENSIONE', font=f_title, fill='#ffffff')
    draw.text((80, 270), 'DEL TESTO 2.0', font=f_title, fill='#00d26a')
    
    f_sub = get_font(font_bold_path, 36)
    draw.text((80, 390), '587 Attività Pratiche per Allenare', font=f_sub, fill='#f3f4f6')
    draw.text((80, 445), 'la Lettura e Superare le Difficoltà', font=f_sub, fill='#f3f4f6')
    draw.text((80, 500), 'in Tutte le Materie Scolastiche.', font=f_sub, fill='#f3f4f6')
    
    # Big Mockup Box
    draw.rounded_rectangle([70, 600, 1010, 1420], radius=40, fill='#ffffff', outline='#f72585', width=6)
    draw.rounded_rectangle([70, 600, 1010, 850], radius=40, fill='#4361ee')
    
    f_card_title = get_font(font_title_path, 54)
    draw.text((120, 640), '587 SCHEDE DIDATTICHE', font=f_card_title, fill='#ffdd00')
    draw.text((120, 720), 'IN FORMATO PDF', font=f_card_title, fill='#ffffff')
    
    f_card_body = get_font(font_bold_path, 36)
    items = [
        '📘 150 Schede di Comprensione Rapida',
        '📙 120 Testi con Domande & Inferenze',
        '📗 117 Esercizi di Vocabolario Attivo',
        '📕 200 Attività Interdisciplinari',
        '🎁 4 Bonus Esclusivi Inclusi'
    ]
    for i, it in enumerate(items):
        draw.text((120, 910 + i * 85), it, font=f_card_body, fill='#333333')
        
    draw.rounded_rectangle([110, 1470, 970, 1590], radius=25, fill='#2c2250', outline='#4a3b7a', width=3)
    f_pill = get_font(font_bold_path, 32)
    draw.text((150, 1510), '🎯 Per Bambini dai 7 ai 12 Anni (Elementari e Medie)', font=f_pill, fill='#ffffff')
    
    draw.rounded_rectangle([110, 1630, 970, 1780], radius=30, fill='#00a1e6')
    f_cta = get_font(font_bold_path, 42)
    draw.text((180, 1680), 'SCARICA SUBITO · €27', font=f_cta, fill='#ffffff')
    
    img.save('images/WReKdb5163414.webp')
    img.resize((300, 533)).save('images/WReKdb5163414_1.webp')
    img.resize((768, 1365)).save('images/WReKdb5163414_2.webp')
    img.resize((1024, 1820)).save('images/WReKdb5163414_3.webp')
    img.save('images/WReKdb5163414_4.webp')
    print('Created Italian Mobile Banner!')

# 3. Generate 7-Day Guarantee Badge in Italian (1200x900)
def create_guarantee_badge():
    w, h = 1200, 900
    img = Image.new('RGB', (w, h), color='#f9fafb')
    draw = ImageDraw.Draw(img)
    
    # Outer box
    draw.rounded_rectangle([50, 50, 1150, 850], radius=35, fill='#ffffff', outline='#e5e7eb', width=4)
    
    # Gold Seal / Shield
    draw.ellipse([450, 120, 750, 420], fill='#eab308', outline='#ca8a04', width=8)
    draw.ellipse([475, 145, 725, 395], fill='#fef08a', outline='#ca8a04', width=4)
    
    f_g_num = get_font(font_title_path, 110)
    draw.text((545, 170), '7', font=f_g_num, fill='#854d0e')
    f_g_days = get_font(font_bold_path, 34)
    draw.text((530, 305), 'GIORNI', font=f_g_days, fill='#854d0e')
    
    f_g_title = get_font(font_title_path, 48)
    draw.text((250, 470), 'GARANZIA INCONDIZIONATA', font=f_g_title, fill='#1f2937')
    draw.text((370, 540), '100% SODDISFATTI O RIMBORSATI', font=get_font(font_bold_path, 30), fill='#15803d')
    
    f_g_desc = get_font(font_reg_path, 26)
    draw.text((150, 620), 'Hai 7 giorni interi per provare il Kit con tuo figlio. Se per qualsiasi motivo', font=f_g_desc, fill='#4b5563')
    draw.text((140, 665), 'non sarai soddisfatto dei suoi progressi, basta inviarci un’email e ti restituiremo', font=f_g_desc, fill='#4b5563')
    draw.text((260, 710), 'il 100% dell’importo speso, subito e senza alcuna domanda.', font=f_g_desc, fill='#4b5563')
    
    img.save('images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src.png')
    img.save('images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src_1.png')
    img.resize((727, 545)).save('images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src_2.png')
    img.resize((545, 409)).save('images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src_3.png')
    img.resize((213, 160)).save('images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src_4.png')
    print('Created Italian Guarantee Badge!')

# 4. Generate 4 Italian WhatsApp Testimonials
def create_whatsapp_testimonials():
    # Chat 1: zBPGty6014358 (1179x985)
    w, h = 1179, 985
    im1 = Image.new('RGB', (w, h), color='#efeae2')
    d1 = ImageDraw.Draw(im1)
    # Header
    d1.rectangle([0, 0, w, 140], fill='#075e54')
    f_name = get_font(font_bold_path, 40)
    d1.text((160, 35), 'Laura M. (Mamma di Matteo - 8 anni)', font=f_name, fill='#ffffff')
    d1.text((160, 85), 'online', font=get_font(font_reg_path, 26), fill='#dcf8c6')
    # Avatar
    d1.ellipse([40, 25, 130, 115], fill='#128c7e')
    d1.text((70, 45), 'LM', font=get_font(font_bold_path, 34), fill='#ffffff')
    
    # Message bubble 1
    d1.rounded_rectangle([60, 180, 1050, 460], radius=20, fill='#ffffff')
    f_msg = get_font(font_reg_path, 32)
    d1.text((90, 210), 'Ciao! Volevo ringraziarti di cuore per il Kit! 🙏❤️', font=f_msg, fill='#111111')
    d1.text((90, 260), 'Matteo prima piangeva ogni volta che doveva leggere', font=f_msg, fill='#111111')
    d1.text((90, 310), 'e non rispondeva a nessuna domanda del testo...', font=f_msg, fill='#111111')
    d1.text((90, 360), 'Dopo 2 settimane con queste schede legge con piacere', font=f_msg, fill='#111111')
    d1.text((90, 410), 'e ieri la maestra gli ha fatto i complimenti in classe!', font=f_msg, fill='#111111')
    
    # Message bubble 2
    d1.rounded_rectangle([60, 490, 950, 720], radius=20, fill='#ffffff')
    d1.text((90, 520), 'La sera fa 15 minuti di attività senza che debba', font=f_msg, fill='#111111')
    d1.text((90, 570), 'ripeterglielo mille volte. È cambiato tutto!', font=f_msg, fill='#111111')
    d1.text((90, 620), 'Materiale favoloso, lo consiglio a tutte le mamme!', font=f_msg, fill='#111111')
    
    # Reply bubble
    d1.rounded_rectangle([250, 750, 1120, 910], radius=20, fill='#dcf8c6')
    d1.text((280, 780), 'Che meravigliosa notizia Laura! Felicissima per Matteo!', font=f_msg, fill='#111111')
    d1.text((280, 835), 'Continuate così, la costanza è la chiave! ✨', font=f_msg, fill='#111111')
    
    im1.save('images/zBPGty6014358.jpeg')
    im1.save('images/zBPGty6014358_1.jpeg')
    im1.resize((191, 160)).save('images/zBPGty6014358_2.jpeg')
    im1.resize((652, 545)).save('images/zBPGty6014358_3.jpeg')
    im1.resize((489, 409)).save('images/zBPGty6014358_4.jpeg')

    # Chat 2: vrAnob5260946 (942x829)
    w2, h2 = 942, 829
    im2 = Image.new('RGB', (w2, h2), color='#efeae2')
    d2 = ImageDraw.Draw(im2)
    d2.rectangle([0, 0, w2, 130], fill='#075e54')
    d2.text((150, 30), 'Chiara F. (Insegnante Primaria)', font=get_font(font_bold_path, 36), fill='#ffffff')
    d2.text((150, 75), 'online', font=get_font(font_reg_path, 24), fill='#dcf8c6')
    d2.ellipse([40, 20, 120, 100], fill='#128c7e')
    d2.text((65, 40), 'CF', font=get_font(font_bold_path, 30), fill='#ffffff')
    
    d2.rounded_rectangle([50, 160, 880, 480], radius=20, fill='#ffffff')
    f_msg2 = get_font(font_reg_path, 30)
    d2.text((80, 190), 'Buonasera! Ho acquistato il kit per usarlo', font=f_msg2, fill='#111111')
    d2.text((80, 240), 'in classe con i miei alunni di 4ª elementare.', font=f_msg2, fill='#111111')
    d2.text((80, 290), 'Le schede sono strutturate in modo impeccabile,', font=f_msg2, fill='#111111')
    d2.text((80, 340), 'stimolanti e molto chiare.', font=f_msg2, fill='#111111')
    d2.text((80, 390), 'Anche i bambini con più difficoltà partecipano felici!', font=f_msg2, fill='#111111')
    d2.text((80, 435), 'I progressi nella comprensione sono evidenti 👏', font=f_msg2, fill='#111111')
    
    d2.rounded_rectangle([180, 520, 890, 740], radius=20, fill='#dcf8c6')
    d2.text((210, 550), 'Grazie mille per il feedback Chiara!', font=f_msg2, fill='#111111')
    d2.text((210, 600), 'Sapere che aiuta anche in classe è una', font=f_msg2, fill='#111111')
    d2.text((210, 650), 'soddisfazione grandissima! Buona continuazione!', font=f_msg2, fill='#111111')
    
    im2.save('images/vrAnob5260946.webp')
    im2.resize((182, 160)).save('images/vrAnob5260946_1.webp')
    im2.save('images/vrAnob5260946_2.webp')
    im2.resize((465, 409)).save('images/vrAnob5260946_3.webp')

    # Chat 3: MFPLzd5360958 (1086x1448)
    w3, h3 = 1086, 1448
    im3 = Image.new('RGB', (w3, h3), color='#efeae2')
    d3 = ImageDraw.Draw(im3)
    d3.rectangle([0, 0, w3, 140], fill='#075e54')
    d3.text((160, 35), 'Francesca B. (Mamma di Sofia - 10 anni)', font=get_font(font_bold_path, 38), fill='#ffffff')
    d3.text((160, 85), 'online', font=get_font(font_reg_path, 26), fill='#dcf8c6')
    d3.ellipse([40, 25, 130, 115], fill='#128c7e')
    d3.text((65, 45), 'FB', font=get_font(font_bold_path, 34), fill='#ffffff')
    
    d3.rounded_rectangle([60, 180, 1020, 550], radius=20, fill='#ffffff')
    f_msg3 = get_font(font_reg_path, 32)
    d3.text((90, 215), 'Sofia sbagliava continuamente i problemi di', font=f_msg3, fill='#111111')
    d3.text((90, 270), 'matematica e le domande di scienze, non perché', font=f_msg3, fill='#111111')
    d3.text((90, 325), 'non sapesse le formule ma perché non capiva il testo.', font=f_msg3, fill='#111111')
    d3.text((90, 380), 'Con il Modulo 4 di comprensione interdisciplinare', font=f_msg3, fill='#111111')
    d3.text((90, 435), 'ha finalmente sbloccato il ragionamento!', font=f_msg3, fill='#111111')
    d3.text((90, 490), 'Ieri ha preso 9 nella verifica scritta! 🥳🎉', font=f_msg3, fill='#111111')
    
    d3.rounded_rectangle([60, 580, 960, 820], radius=20, fill='#ffffff')
    d3.text((90, 615), 'È il miglior acquisto che potessi fare per la sua', font=f_msg3, fill='#111111')
    d3.text((90, 670), 'scuola. Meno ansia, più voti alti e tanta serenità.', font=f_msg3, fill='#111111')
    d3.text((90, 725), 'Grazie davvero!', font=f_msg3, fill='#111111')
    
    d3.rounded_rectangle([200, 860, 1020, 1080], radius=20, fill='#dcf8c6')
    d3.text((230, 900), 'Che risultato incredibile Francesca! Sofia è', font=f_msg3, fill='#111111')
    d3.text((230, 955), 'stata bravissima. Questo dimostra che comprendere', font=f_msg3, fill='#111111')
    d3.text((230, 1010), 'è la base di ogni materia! 🌟', font=f_msg3, fill='#111111')

    im3.save('images/MFPLzd5360958.webp')
    im3.resize((120, 160)).save('images/MFPLzd5360958_1.webp')
    im3.resize((307, 409)).save('images/MFPLzd5360958_2.webp')
    im3.resize((409, 545)).save('images/MFPLzd5360958_3.webp')
    im3.save('images/MFPLzd5360958_4.webp')

    # Chat 4: JeslyJ6014358 (1599x754)
    w4, h4 = 1599, 754
    im4 = Image.new('RGB', (w4, h4), color='#efeae2')
    d4 = ImageDraw.Draw(im4)
    d4.rectangle([0, 0, w4, 140], fill='#075e54')
    d4.text((160, 35), 'Elena R. (Mamma di Leonardo - 9 anni)', font=get_font(font_bold_path, 42), fill='#ffffff')
    d4.text((160, 85), 'online', font=get_font(font_reg_path, 28), fill='#dcf8c6')
    d4.ellipse([40, 25, 130, 115], fill='#128c7e')
    d4.text((70, 45), 'ER', font=get_font(font_bold_path, 34), fill='#ffffff')
    
    d4.rounded_rectangle([60, 180, 1500, 450], radius=20, fill='#ffffff')
    f_msg4 = get_font(font_reg_path, 34)
    d4.text((100, 220), 'Buongiorno! Leonardo ha finito il primo modulo di 150 schede.', font=f_msg4, fill='#111111')
    d4.text((100, 280), 'Non ha più quell’ansia quando vede un testo lungo e risponde subito a tono.', font=f_msg4, fill='#111111')
    d4.text((100, 340), 'Compiti finiti in metà tempo senza discussioni in famiglia! Grazie di cuore! ❤️', font=f_msg4, fill='#111111')
    
    d4.rounded_rectangle([350, 490, 1500, 680], radius=20, fill='#dcf8c6')
    d4.text((390, 540), 'Fantastico Elena! Vedere i bambini ritrovare fiducia e autonomia', font=f_msg4, fill='#111111')
    d4.text((390, 600), 'nello studio è la gioia più grande! Complimenti a Leonardo!', font=f_msg4, fill='#111111')
    
    im4.save('images/JeslyJ6014358.png')
    im4.resize((299, 141)).save('images/JeslyJ6014358_1.png')
    im4.resize((768, 362)).save('images/JeslyJ6014358_2.png')
    im4.save('images/JeslyJ6014358_3.png')
    im4.resize((1536, 724)).save('images/JeslyJ6014358_4.png')
    im4.resize((1024, 483)).save('images/JeslyJ6014358_5.png')
    print('Created Italian WhatsApp testimonials!')

# 5. Generate Italian Module Cards & Bonus Mockups
def create_italian_cards():
    cards = [
        ('bca575f3-70fc-4dca-a646-42e0af0d9f2f-misc-src', 'MODULO 1', '150 Attività di Lettura &', 'Comprensione Rapida', '#4361ee'),
        ('76ec044f-cc34-467e-a2dc-4779760270c7-misc-src', 'MODULO 2', '120 Testi con Domande', 'Dirette & Inferenze', '#3a0ca3'),
        ('mFPujI8456037', 'MODULO 3', '117 Esercizi di Vocabolario', 'e Comprensione del Contesto', '#7209b7'),
        ('ef51b634-0463-4047-bab6-7395d536fb7c-misc-src', 'MODULO 4', '200 Attività Interdisciplinari', '(Storia, Scienze, Geografia)', '#00b4d8'),
        ('ghnuyA5473914', 'BONUS 1', 'Guida Rapida Genitori:', 'Come Aiutare nello Studio', '#f72585'),
        ('zCyQDE5473914', 'BONUS 2', 'Piano di Studio Giornaliero:', '15 Minuti al Giorno', '#4cc9f0'),
        ('cmIaGY5473914', 'BONUS 3', 'Mappe Concettuali e', 'Giochi di Vocabolario', '#ffb703'),
        ('HpBKtY5473914', 'BONUS 4', 'Soluzioni Complete e', 'Guida di Correzione', '#06d6a0'),
        ('gcdBCn5473914', 'MATERIALE EXTRA', 'Schede di Lettura', 'per la Scuola Media', '#fb8500'),
        ('vDHxvY5473914', 'MATERIALE EXTRA', 'Attività di Logica e', 'Comprensione Matematica', '#2a9d8f')
    ]
    
    for base_name, tag, line1, line2, color in cards:
        w, h = 512, 315
        img = Image.new('RGB', (w, h), color='#ffffff')
        draw = ImageDraw.Draw(img)
        
        # Background
        draw.rounded_rectangle([10, 10, w-10, h-10], radius=20, fill=color)
        draw.rounded_rectangle([20, 20, w-20, h-20], radius=16, fill='#ffffff')
        
        # Header banner
        draw.rounded_rectangle([20, 20, w-20, 95], radius=16, fill=color)
        draw.rectangle([20, 60, w-20, 95], fill=color)
        
        f_tag = get_font(font_bold_path, 28)
        draw.text((40, 38), tag, font=f_tag, fill='#ffffff')
        
        f_l1 = get_font(font_title_path, 26)
        draw.text((40, 125), line1, font=f_l1, fill='#1f2937')
        draw.text((40, 165), line2, font=f_l1, fill='#1f2937')
        
        draw.rounded_rectangle([40, 230, w-40, 280], radius=12, fill='#f3f4f6')
        f_badge = get_font(font_bold_path, 18)
        draw.text((60, 243), '📄 Formato PDF Pronto da Stampare', font=f_badge, fill='#4b5563')
        
        img.save(f'images/{base_name}.png')
        img.save(f'images/{base_name}_1.png')
        img.resize((260, 160)).save(f'images/{base_name}_2.png')

    # Bonus wide mockups (1600x706 / 1599x841)
    wide_cards = [
        ('kbvgHh6486611', 'BONUS ESCLUSIVO 1', 'Guida Pratica per Genitori: Come Sviluppare la Comprensione del Testo a Casa', '#3a0ca3'),
        ('pQfwEt6486611', 'BONUS ESCLUSIVO 2', 'Piano di Studio di 15 Minuti: Routine Strutturata Giorno per Giorno', '#7209b7'),
        ('iWnJvw6486611', 'BONUS ESCLUSIVO 3', 'Mappe Mentali e Schemi Visivi per Imparare a Riassumere', '#0077b6'),
        ('YGvXxb6486611', 'BONUS ESCLUSIVO 4', 'Tutte le Soluzioni Dettagliate per la Verifica Immediata', '#0096c7')
    ]
    
    for base_name, b_title, b_desc, b_color in wide_cards:
        w, h = 1600, 706
        img = Image.new('RGB', (w, h), color='#ffffff')
        draw = ImageDraw.Draw(img)
        
        draw.rounded_rectangle([15, 15, w-15, h-15], radius=30, fill=b_color)
        draw.rounded_rectangle([30, 30, w-30, h-30], radius=25, fill='#ffffff')
        
        draw.rounded_rectangle([60, 60, 500, 140], radius=20, fill=b_color)
        draw.text((90, 80), b_title, font=get_font(font_bold_path, 34), fill='#ffffff')
        
        draw.text((60, 200), b_desc, font=get_font(font_title_path, 42), fill='#1f2937')
        
        draw.rounded_rectangle([60, 480, 700, 580], radius=20, fill='#00c738')
        draw.text((100, 505), '🎁 INCLUSO GRATIS NEL KIT OGGI', font=get_font(font_bold_path, 32), fill='#ffffff')
        
        img.save(f'images/{base_name}.png')
        img.resize((299, 132)).save(f'images/{base_name}_1.png')
        img.save(f'images/{base_name}_2.png')
        img.resize((768, 339)).save(f'images/{base_name}_3.png')
        img.resize((1024, 452)).save(f'images/{base_name}_4.png')
        img.resize((1536, 678)).save(f'images/{base_name}_5.png')

    print('Created all Italian cards and bonus mockups!')

create_desktop_hero()
create_mobile_hero()
create_guarantee_badge()
create_whatsapp_testimonials()
create_italian_cards()
