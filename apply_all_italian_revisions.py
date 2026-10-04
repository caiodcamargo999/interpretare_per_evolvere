import re, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

print('--- STEP 1: Updating Bundle Mockup with ATTESTATO UFFICIALE DI MERITO ---')
bundle_orig_path = 'public/images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src.png'
if os.path.exists(bundle_orig_path):
    img = Image.open(bundle_orig_path).convert('RGBA')
    
    pw, ph = 230, 64
    patch = Image.new('RGBA', (pw, ph), (251, 250, 246, 255))
    pdraw = ImageDraw.Draw(patch)

    font_bold = '/System/Library/Fonts/Supplemental/Trebuchet MS Bold.ttf'
    f1 = ImageFont.truetype(font_bold, 18)
    f2 = ImageFont.truetype(font_bold, 18)

    t1 = 'ATTESTATO UFFICIALE'
    t2 = 'DI MERITO'
    bbox1 = pdraw.textbbox((0,0), t1, font=f1)
    bbox2 = pdraw.textbbox((0,0), t2, font=f2)
    pdraw.text((pw//2 - (bbox1[2]-bbox1[0])//2, 8), t1, font=f1, fill='#11273c')
    pdraw.text((pw//2 - (bbox2[2]-bbox2[0])//2, 34), t2, font=f2, fill='#11273c')

    angle = 14.5
    patch_rot = patch.rotate(-angle, expand=True, resample=Image.Resampling.BICUBIC)
    img.paste(patch_rot, (808, 218), patch_rot)

    img.save(bundle_orig_path, 'PNG')
    img.resize((1200, 900)).save('public/images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src_1.png')
    img.resize((768, 576)).save('public/images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src_2.png')
    img.resize((512, 384)).save('public/images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src_3.png')
    img.resize((300, 225)).save('public/images/d597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src_4.png')
    
    # Also update floodfill transparent bundle
    img_flood = img.copy()
    ImageDraw.floodfill(img_flood, (0, 0), (0, 0, 0, 0), thresh=15)
    ImageDraw.floodfill(img_flood, (img.width-1, 0), (0, 0, 0, 0), thresh=15)
    ImageDraw.floodfill(img_flood, (0, img.height-1), (0, 0, 0, 0), thresh=15)
    ImageDraw.floodfill(img_flood, (img.width-1, img.height-1), (0, 0, 0, 0), thresh=15)
    img_flood.save('public/images/bundle_floodfill_transparent.png', 'PNG')
    print('Updated all bundle images with ATTESTATO UFFICIALE DI MERITO!')

# Re-run facebook asset generator
os.system('python3 generate_facebook_assets.py')

print('--- STEP 2: Updating index.tsx with exact Italian copy & consistency ---')
with open('index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update FAQ React State
faq_replacement = """const faqs: FaqItem[] = [
  {
    q: 'Come ricevo il materiale dopo l\\'acquisto?',
    a: 'Subito dopo la conferma del pagamento, riceverai un\\'email con un link per accedere immediatamente al materiale. Potrai scaricare tutti i file PDF e iniziare a stampare le prime schede già da oggi.'
  },
  {
    q: 'È adatto all\\'età di mio figlio?',
    a: 'Sì, le attività sono studiate appositamente per bambini dai 7 ai 12 anni, dalla scuola primaria al primo anno della scuola secondaria di primo grado, con livelli di difficoltà progressivi e stimolanti.'
  },
  {
    q: 'Devo stampare tutto il materiale contemporaneamente?',
    a: 'No. Puoi stampare solo le schede del giorno — una o due pagine alla volta — oppure far svolgere gli esercizi a tuo figlio seguendo il PDF e scrivendo le risposte direttamente sul quaderno.'
  },
  {
    q: 'E se non dovesse fare al caso nostro?',
    a: 'Hai una garanzia di rimborso di 7 giorni. Se il materiale non dovesse fare al caso tuo o di tuo figlio, ti rimborseremo il 100% dell\\'importo speso, senza complicazioni.'
  },
  {
    q: 'Quali sono i metodi di pagamento disponibili?',
    a: '<p>Puoi pagare comodamente e in totale sicurezza con qualsiasi carta di credito, carta di debito o carta prepagata — inclusa Postepay — oppure tramite PayPal. La transazione è protetta e sicura.</p>'
  }
];"""

code = re.sub(r'const faqs: FaqItem\[\] = \[.*?\];', faq_replacement, code, flags=re.DOTALL)

# 2. Mandatory Text Replacements
replacements = [
    # Bullets header
    ("Con il giusto allenamento, in poche settimane si trasforma in:", "Con il giusto allenamento, in poche settimane tuo figlio può diventare:"),
    
    # 4 Steps section text
    ("Basta scegliere 1 scheda, stamparla (o usarla a schermo), consegnarla a tuo figlio e vedere i progressi giorno dopo giorno. Nessuna preparazione richiesta. Scegli, assegni e alleni la mente.",
     "Basta scegliere una scheda, stamparla — oppure utilizzarla sullo schermo —, consegnarla a tuo figlio e osservare i suoi progressi giorno dopo giorno. Non è necessaria alcuna preparazione. Scegli, assegna e allena la mente."),
     
    ("Con le 587 Attività di Comprensione pronte all'uso, ti basta:",
     "Con le 587 attività di comprensione pronte all'uso, ti basta:"),
     
    ("2 - Zero stress: nessun esercizio da inventare o cercare online",
     "2 - Niente stress: nessun esercizio da inventare o cercare online"),
     
    ("4 - Vedere tuo figlio sicuro, preparato e pronto per ogni materia",
     "4 - Vedere tuo figlio più sicuro, preparato e pronto per ogni materia"),
     
    # Psychopedagogical section
    ("È il frutto di mesi di progettazione psicopedagogica per strutturare esercizi progressivi e ad alto impatto didattico per la scuola primaria e media.",
     "È il risultato di mesi di progettazione psicopedagogica, con esercizi progressivi e ad alto valore didattico, pensati per la scuola primaria e secondaria di primo grado."),
     
    # Bonus section header
    ("👉 Oltre alle 587 attività riceverai anche questi 4 Bonus:",
     "Oltre alle 587 attività, riceverai anche questi quattro bonus:"),
    ("Oltre alle 587 attività riceverai anche questi 4 Bonus:",
     "Oltre alle 587 attività, riceverai anche questi quattro bonus:"),
     
    # Target audience bullet
    ("Hai bisogno di materiale pronto all'uso da iniziare subito oggi stesso",
     "Hai bisogno di materiale pronto all'uso da utilizzare subito, già oggi"),
     
    # Testimonials
    ("In sole 3 settimane mia figlia riesce a riassumere qualsiasi brano. Non l'avevo mai vista così autonoma e serena nello studio.",
     "In sole tre settimane, mia figlia riesce a riassumere qualsiasi brano. Non l'avevo mai vista così autonoma e serena nello studio."),
     
    ("Abbiamo iniziato la scorsa settimana e mio figlio ora mi chiama orgoglioso per farmi vedere gli esercizi completati. Molto più sicuro di sé!",
     "Abbiamo iniziato la scorsa settimana e ora mio figlio mi chiama con orgoglio per mostrarmi gli esercizi che ha completato. È molto più sicuro di sé!"),
     
    # Value transition
    ("Tutto questo materiale didattico ha un valore reale molto più alto, ma vogliamo che tu possa TRASFORMARE LO STUDIO DI TUO FIGLIO in modo pratico, accessibile ed efficace per ogni famiglia.",
     "Tutto questo materiale didattico ha un valore reale molto più alto, ma vogliamo aiutarti a trasformare il modo in cui tuo figlio studia, con un metodo pratico, accessibile ed efficace per tutta la famiglia."),
    ("Tutto questo materiale didattico ha un valore reale molto più alto, ma vogliamo che tu possa <span style={{ color: '#90768a' }}>TRASFORMARE LO STUDIO DI TUO FIGLIO</span> in modo pratico, accessibile ed efficace per ogni famiglia.",
     "Tutto questo materiale didattico ha un valore reale molto più alto, ma vogliamo aiutarti a trasformare il modo in cui tuo figlio studia, con un metodo pratico, accessibile ed efficace per tutta la famiglia."),

    # Promo description
    ("Offerta promozionale unica: soli €27 in pagamento unico (nessun abbonamento)Risparmi oltre €160 e hai accesso immediato subito dopo l'acquisto.",
     "Offerta promozionale unica: soli €27, con un unico pagamento e nessun abbonamento. Risparmi €164 e ottieni l'accesso immediatamente dopo l'acquisto."),
    ("Offerta promozionale unica: soli €27 in pagamento unico (nessun abbonamento) Risparmi oltre €160 e hai accesso immediato subito dopo l'acquisto.",
     "Offerta promozionale unica: soli €27, con un unico pagamento e nessun abbonamento. Risparmi €164 e ottieni l'accesso immediatamente dopo l'acquisto."),
    ("Offerta promozionale unica: soli €27 in pagamento unico (nessun abbonamento) · Risparmi oltre €160 e hai accesso immediato subito dopo l'acquisto.",
     "Offerta promozionale unica: soli €27, con un unico pagamento e nessun abbonamento. Risparmi €164 e ottieni l'accesso immediatamente dopo l'acquisto."),

    # Security pill
    ("Pagamento protetto e sicuro al 100% · Consegna immediata via email",
     "Pagamento sicuro al 100% · Consegna immediata via email"),
    ("🔒 Pagamento protetto e sicuro al 100% · Consegna immediata via email",
     "🔒 Pagamento sicuro al 100% · Consegna immediata via email"),

    # Two paths section
    ("Tuo figlio continuerà a bloccarsi nella lettura, perdendo autostima e dipendendo sempre da te o da costose ripetizioni per ogni singolo compito.",
     "Tuo figlio continuerà ad avere difficoltà nella lettura, perderà fiducia in sé e avrà sempre bisogno del tuo aiuto o di costose ripetizioni."),
     
    ("In pochi minuti svolge la prima scheda e impara a comprendere da solo, con più sicurezza, autonomia e voti migliori.",
     "In pochi minuti, tuo figlio potrà completare la prima scheda e iniziare a comprendere i testi in modo più autonomo, con maggiore sicurezza e risultati migliori."),
     
    # Final call to action section
    ("Questo materiale è lo strumento pratico che cercavi per dare una SVOLTA all'istruzione di tuo figlio. Tra 5 minuti potrai già scaricare la prima scheda e vedere i primi miglioramenti.",
     "Questo materiale è lo strumento pratico che cercavi per dare una svolta al percorso scolastico di tuo figlio. Tra cinque minuti potrai scaricare la prima scheda e iniziare a vedere i primi miglioramenti."),

    # Guarantee Section
    ("Garanzia Incondizionata di 7 Giorni",
     "Garanzia di rimborso di 7 giorni"),
    ("Acquista con totale tranquillità. Se entro 7 giorni ritieni che il materiale non faccia al caso di tuo figlio, ti basterà inviare un'email e ti rimborseremo il 100% dell'importo speso — senza domande e senza burocrazia. Il rischio è interamente nostro.",
     "Acquista con totale tranquillità. Se entro 7 giorni ritieni che il materiale non faccia al caso di tuo figlio, ti basterà inviare un'email e ti rimborseremo il 100% dell'importo speso — senza domande e senza burocrazia. Il rischio è interamente nostro."),
    ("Hai 7 giorni interi per provare il Kit con tuo figlio. Se per qualsiasi motivo non sarai soddisfatto dei suoi progressi, basta inviarci un'email e ti restituiremo il 100% dell'importo speso, subito e senza complicazioni.",
     "Acquista con totale tranquillità. Se entro 7 giorni ritieni che il materiale non faccia al caso di tuo figlio, ti basterà inviare un'email e ti rimborseremo il 100% dell'importo speso — senza domande e senza burocrazia. Il rischio è interamente nostro."),
    ("Se entro 7 giorni ritieni che il materiale non sia adatto a tuo figlio",
     "Se entro 7 giorni ritieni che il materiale non faccia al caso di tuo figlio"),
     
    # Guarantee pill badges
    ("🛡️ Garanzia di 7 giorni", "🛡️ Garanzia di rimborso di 7 giorni"),
    ("Garanzia di 7 giorni", "Garanzia di rimborso di 7 giorni"),
    
    # FAQ Title
    ("Domande Frequenti", "Domande frequenti"),
]

for src, trg in replacements:
    code = code.replace(src, trg)

# 3. Rewrite "Chi ha ideato questo metodo?" completely
specialist_section_regex = r'Chi ha ideato questo metodo\?.*?<\/p><\/h3><\/div>'
specialist_replacement = """Chi ha ideato questo metodo?</h3></div></div><div className="a-c-cont a-c-cont-7833f39 a-r"><div className="atomicat-heading-title-7833f39 atomicat-text-7833f39 a-e-cont atomicat-element-container-7833f39 a-r atomicat-heading-title"><h3 className="a-i-e-cont"><p>Il metodo è stato ideato da un team di professionisti specializzati in psicopedagogia e nell'apprendimento infantile.</p><p><br /></p><p>Nel corso degli anni, seguendo da vicino centinaia di studenti e supportando numerose famiglie, abbiamo individuato un problema comune a tantissimi bambini: riescono a leggere le parole ad alta voce, ma non sempre comprendono pienamente ciò che leggono.</p><p><br /></p><p>Quando manca una comprensione profonda, il bambino può iniziare a commettere errori, perdere fiducia in sé e dipendere continuamente dall'aiuto degli altri.</p><p><br /></p><p>Per questo abbiamo creato il Kit Comprensione del Testo 2.0: un percorso strutturato, progressivo e semplice da applicare, pensato per aiutare i genitori a sviluppare nei propri figli una maggiore capacità di comprensione, con metodo, serenità e risultati concreti.</p><p><br /></p><p>Il nostro obiettivo è offrirti uno strumento chiaro, efficace e pronto all'uso, senza complicazioni.</p></h3></div>"""

code = re.sub(
    r'Chi ha ideato questo metodo\?<\/h3><\/div><\/div><div className=\"a-c-cont a-c-cont-7833f39 a-r\">.*?<\/div><\/div><\/div><\/div><\/div><div className=\"atomicat-container-40c1c0c',
    specialist_replacement + '</div></div></div></div><div className="atomicat-container-40c1c0c',
    code,
    flags=re.DOTALL
)

# 4. Exact Value Breakdown & Consistent Math (€191 Total -> €27)
code = code.replace('👉 587 Schede Didattiche di Comprensione Rapida - Valore €47', '587 schede didattiche di comprensione rapida — Valore €47')
code = code.replace('👉 BONUS 1: Kit Calligrafia Perfetta (40 Pagine) - Valore €29', 'Bonus 1: Kit calligrafia perfetta (40 pagine) — Valore €29')
code = code.replace('👉 BONUS 2: Ora di Lettura - 24 Testi Coinvolgenti (42 Pagine) - Valore €29', 'Bonus 2: Ora di lettura — 24 testi coinvolgenti (42 pagine) — Valore €29')
code = code.replace('👉 BONUS 3: Matematica Semplificata (31 Pagine) - Valore €37', 'Bonus 3: Matematica semplificata (31 pagine) — Valore €37')
code = code.replace('👉 BONUS 4: Soluzioni Complete per i Genitori & Attestato Ufficiale - Valore €49', 'Bonus 4: Soluzioni complete per i genitori e attestato ufficiale — Valore €49')

# Value overall text
code = code.replace('Valore complessivo: <s>€97</s>... ma oggi puoi averlo a soli:', 'Valore complessivo: €191… ma oggi puoi averlo a soli:')
code = code.replace('Valore complessivo: €97... ma oggi puoi averlo a soli:', 'Valore complessivo: €191… ma oggi puoi averlo a soli:')
code = code.replace('<s>€97</s>', '<s>€191</s>')
code = code.replace('Da €97 a soli €27', 'Da €191 a soli €27')

# 5. Clean up improper spacing before punctuation across entire file
code = re.sub(r'\s+:', ':', code)
code = re.sub(r'\s+,', ',', code)
code = re.sub(r'\s+\?', '?', code)
code = re.sub(r'\s+!', '!', code)

with open('index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print('Updated index.tsx with all requested corrections!')
