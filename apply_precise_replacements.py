import re

with open('index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Basta scegliere una scheda...
old_basta_pattern = r'<p><strong>Basta scegliere 1 scheda, stamparla \(o usarla a schermo\), consegnarla a tuo figlio e vedere i progressi giorno dopo giorno\. <\/strong><strong style=\{\{ color: \'#fff\' \}\}>Nessuna preparazione richiesta\. Scegli, assegni e alleni la mente\.<\/strong><\/p>'
new_basta = "<p><strong>Basta scegliere una scheda, stamparla — oppure utilizzarla sullo schermo —, consegnarla a tuo figlio e osservare i suoi progressi giorno dopo giorno. </strong><strong style={{ color: '#fff' }}>Non è necessaria alcuna preparazione. Scegli, assegna e allena la mente.</strong></p>"

code = re.sub(old_basta_pattern, new_basta, code)

# Fallback direct string replacement for Basta scegliere
code = code.replace(
    'Basta scegliere 1 scheda, stamparla (o usarla a schermo), consegnarla a tuo figlio e vedere i progressi giorno dopo giorno.',
    'Basta scegliere una scheda, stamparla — oppure utilizzarla sullo schermo —, consegnarla a tuo figlio e osservare i suoi progressi giorno dopo giorno.'
)
code = code.replace(
    'Nessuna preparazione richiesta. Scegli, assegni e alleni la mente.',
    'Non è necessaria alcuna preparazione. Scegli, assegna e allena la mente.'
)

# 2. Offerta promozionale unica...
old_promo_pattern = r'<p><strong>Offerta promozionale unica:<\/strong> <strong>soli €27 in pagamento unico \(nessun abbonamento\)<\/strong><\/p><p>Risparmi oltre <strong>€160<\/strong> e hai <strong>accesso immediato<\/strong> subito dopo l\'acquisto\.<\/p>'
new_promo = "<p><strong>Offerta promozionale unica: soli €27, con un unico pagamento e nessun abbonamento. Risparmi €164 e ottieni l'accesso immediatamente dopo l'acquisto.</strong></p>"
code = re.sub(old_promo_pattern, new_promo, code)

# 3. Chi ha ideato questo metodo?
old_specialist_pattern = r'<h3 className=\"a-i-e-cont\"><p><strong>Chi ha ideato questo metodo\?<\/strong><\/p><\/h3><\/div><\/div><div className=\"a-c-cont a-r a-c-cont-7833f39 a-s-d-j3527x\"><div className=\"a-e-cont atomicat-text-7833f39 atomicat-element-container-7833f39 atomicat-heading-title-7833f39 a-r atomicat-heading-title\"><h3 className=\"a-i-e-cont\">.*?<\/h3><\/div><\/div>'

new_specialist = """<h3 className="a-i-e-cont"><p><strong>Chi ha ideato questo metodo?</strong></p></h3></div></div><div className="a-c-cont a-r a-c-cont-7833f39 a-s-d-j3527x"><div className="a-e-cont atomicat-text-7833f39 atomicat-element-container-7833f39 atomicat-heading-title-7833f39 a-r atomicat-heading-title"><h3 className="a-i-e-cont"><p>Il metodo è stato ideato da un team di professionisti specializzati in psicopedagogia e nell'apprendimento infantile.</p><p><br /></p><p>Nel corso degli anni, seguendo da vicino centinaia di studenti e supportando numerose famiglie, abbiamo individuato un problema comune a tantissimi bambini: riescono a leggere le parole ad alta voce, ma non sempre comprendono pienamente ciò che leggono.</p><p><br /></p><p>Quando manca una comprensione profonda, il bambino può iniziare a commettere errori, perdere fiducia in sé e dipendere continuamente dall'aiuto degli altri.</p><p><br /></p><p>Per questo abbiamo creato il Kit Comprensione del Testo 2.0: un percorso strutturato, progressivo e semplice da applicare, pensato per aiutare i genitori a sviluppare nei propri figli una maggiore capacità di comprensione, con metodo, serenità e risultati concreti.</p><p><br /></p><p>Il nostro obiettivo è offrirti uno strumento chiaro, efficace e pronto all'uso, senza complicazioni.</p></h3></div></div>"""

code = re.sub(old_specialist_pattern, new_specialist, code, flags=re.DOTALL)

# 4. 5 Value / Bonus List Items
code = code.replace(
    '👉 587 Schede Didattiche di Comprensione Rapida - ',
    '587 schede didattiche di comprensione rapida — '
)
code = code.replace(
    '👉 BONUS 1: Kit Calligrafia Perfetta (40 Pagine) - ',
    'Bonus 1: Kit calligrafia perfetta (40 pagine) — '
)
code = code.replace(
    '👉 BONUS 2: Ora di Lettura - 24 Testi Coinvolgenti (42 Pagine) - ',
    'Bonus 2: Ora di lettura — 24 testi coinvolgenti (42 pagine) — '
)
code = code.replace(
    '👉 BONUS 3: Matematica Semplificata (31 Pagine) - ',
    'Bonus 3: Matematica semplificata (31 pagine) — '
)
code = code.replace(
    '👉 BONUS 4: Soluzioni Complete per i Genitori & Attestato Ufficiale - ',
    'Bonus 4: Soluzioni complete per i genitori e attestato ufficiale — '
)

# 5. Clean punctuation spacing
code = re.sub(r'([a-zA-Z0-9\.\)\]])\s+:', r'\1:', code)
code = re.sub(r'([a-zA-Z0-9\.\)\]])\s+,', r'\1,', code)
code = re.sub(r'([a-zA-Z0-9\.\)\]])\s+\?', r'\1?', code)
code = re.sub(r'([a-zA-Z0-9\.\)\]])\s+!', r'\1!', code)

with open('index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print('Applied precise replacements in index.tsx!')
