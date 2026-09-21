import re

# Read current index.tsx as starting base or kit-interpretar-para-evoluir.html
with open('index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update FAQ list in React state
faq_italian = """interface FaqItem {
  q: string;
  a: string;
}

const faqs: FaqItem[] = [
  {
    q: 'Come ricevo il materiale dopo l\\'acquisto?',
    a: 'Subito dopo la conferma del pagamento, riceverai un\\'email con il link di accesso immediato. Potrai scaricare tutti i file PDF e iniziare a stampare le prime schede già da oggi.'
  },
  {
    q: 'È adatto all\\'età di mio figlio?',
    a: 'Sì, le attività sono studiate appositamente per bambini dai 7 ai 12 anni (scuola primaria e primo anno della secondaria di primo grado), con livelli di difficoltà progressivi e stimolanti.'
  },
  {
    q: 'Devo stampare tutto il materiale contemporaneamente?',
    a: 'No. Puoi stampare solo le schede del giorno (1 o 2 pagine alla volta) oppure far svolgere gli esercizi guardando il PDF e scrivendo le risposte direttamente sul quaderno.'
  },
  {
    q: 'E se non dovesse fare al caso nostro?',
    a: 'Hai 7 giorni di garanzia totale soddisfatti o rimborsati. Se ritieni che il materiale non sia adatto a tuo figlio, ti rimborseremo il 100% dell\\'importo speso, senza complicazioni.'
  },
  {
    q: 'Quali sono i metodi di pagamento disponibili?',
    a: '<p>Puoi pagare comodamente e in totale sicurezza con qualsiasi Carta di Credito, Debito, Prepagata (Postepay compresa) o tramite PayPal. La transazione è protetta e certificata.</p>'
  }
];"""

# Replace the faqs definition in code
code = re.sub(r'interface FaqItem \{.*?const faqs: FaqItem\[\] = \[.*?\];', faq_italian, code, flags=re.DOTALL)

# 2. Text replacements for the whole page
translations = [
    # Top comparison
    ("Quando o seu filho tenta estudar e não entende nada…", "Quando tuo figlio prova a studiare e non capisce nulla…"),
    ("Quando o seu filho treina com as atividades e já começa a melhorar", "Quando tuo filho si allena con le schede e inizia subito a migliorare"),
    
    # Pricing & CTAs
    ("De <s style={{ color: '#a70002' }}>R$539</s> por apenas <strong style={{ color: '#00c738' }}>R$67</strong> — ou <strong>9x de R$8,80</strong>", "Da <s style={{ color: '#a70002' }}>€97</s> a soli <strong style={{ color: '#00c738' }}>€27</strong>"),
    ("De <s style={{ color: '#a70002' }}>R$539</s> por apenas <strong style={{ color: '#00c738' }}>R$67</strong>", "Da <s style={{ color: '#a70002' }}>€97</s> a soli <strong style={{ color: '#00c738' }}>€27</strong>"),
    ("QUERO DESTRAVAR A LEITURA DO MEU FILHO", "VOGLIO MIGLIORARE LA LETTURA DI MIO FIGLIO"),
    ("GARANTIR AGORA · R$67", "ACQUISTA ORA · €27"),
    ("GARANTIR AGORA · €27", "ACQUISTA ORA · €27"),
    ("GARANTIR O ACESSO AGORA", "ACCEDI SUBITO AL KIT COMPLETO"),
    ("QUERO O KIT COM DESCONTO", "VOGLIO IL KIT A SOLI €27"),
    ("GARANTA SEU ACESSO AGORA", "ACCEDI AL KIT A SOLI €27"),
    
    # Guarantees & security pills
    ("✅ Acesso imediato após a compra · 🛡️ Garantia de 7 dias", "✅ Accesso immediato dopo l'acquisto · 🛡️ Garanzia di 7 giorni"),
    ("🛡️ Pagamento seguro · Acesso imediato · Garantia incondicional de 7 dias", "🛡️ Pagamento sicuro al 100% · Accesso immediato · Garanzia di 7 giorni"),
    
    # Problems checklist
    ("O que você nota no dia a dia:", "Cosa noti ogni giorno quando fa i compiti:"),
    ("Lê o texto inteiro, mas quando você pergunta o que ele entendeu, ele não sabe responder", "Legge tutto il testo, ma quando gli chiedi cosa ha capito, non sa cosa rispondere"),
    ("Demora horas para fazer uma tarefa simples de interpretação", "Impiega ore per svolgere un semplice compito di comprensione o riassunto"),
    ("Erra questões de outras matérias (como Matemática e Ciências) simplesmente porque não entendeu o enunciado", "Sbaglia le domande di altre materie (come Matematica e Scienze) semplicemente perché non ha capito la consegna"),
    ("Tem preguiça ou desânimo na hora da leitura", "Mostra ansia, frustrazione o demotivazione ogni volta che deve leggere"),
    
    # Solutions checklist
    ("E o que muda com o método:", "E cosa cambia grazie a questo metodo:"),
    ("Começa a ler com autonomia e responder as perguntas com facilidade", "Inizia a leggere con reale autonomia e a rispondere alle domande con sicurezza"),
    ("Faz as tarefas escolares muito mais rápido e sem estresse", "Svolge i compiti pomeridiani molto più velocemente e senza capricci o stress"),
    ("Melhora as notas em todas as matérias porque passa a compreender o que está lendo", "Migliora i voti in tutte le materie perché comprende finalmente ciò che legge"),
    ("Ganha confiança e passa a gostar de ler", "Acquisisce autostima, sicurezza e riscopre il piacere della lettura"),
    
    # Transition section
    ("Você não precisa de horas de estudo para ver resultados...", "Non servono ore di studio estenuanti per vedere progressi reali..."),
    ("Com apenas 15 minutos por dia, o seu filho desenvolve a habilidade mais importante da vida escolar: interpretar o que lê.", "Con soli 15 minuti al giorno di esercizi mirati, tuo figlio sviluppa l'abilità fondamentale per tutto il percorso scolastico: comprendere ciò che legge."),
    
    # Modules presentation
    ("O que está incluído no Kit Interpretar Para Evoluir 2.0", "Cosa è incluso nel Kit Comprensione del Testo 2.0"),
    ("587 Atividades práticas divididas em 4 módulos:", "587 Attività pratiche suddivise in 4 moduli completi:"),
    ("150 Atividades de Leitura e Compreensão Rápida", "150 Attività di Lettura e Comprensione Rapida"),
    ("Textos curtos com perguntas diretas para treinar a atenção e o foco.", "Testi brevi ed efficaci con domande dirette per allenare concentrazione e memoria."),
    ("120 Textos com Perguntas Diretas e Indiretas", "120 Testi con Domande Dirette e Inferenze"),
    ("Para ensinar a criança a pensar sobre o texto e não apenas repetir palavras.", "Per insegnare al bambino a riflettere sul significato profondo e non solo a ripetere parole."),
    ("117 Exercícios de Vocabulário e Contexto", "117 Esercizi di Vocabolario e Contesto"),
    ("Para acabar com a dúvida de \"não sei o que essa palavra significa\".", "Per ampliare il lessico ed eliminare il blocco del \"non so cosa significa questa parola\"."),
    ("200 Atividades de Interpretação em Outras Disciplinas", "200 Attività di Comprensione Interdisciplinare"),
    ("História, Geografia, Ciências e Matemática — porque interpretar é a base de tudo.", "Storia, Geografia, Scienze e Matematica — perché comprendere è la base di ogni materia."),
    
    # Testimonials header
    ("O que dizem as mães e professoras que já usam o método:", "Cosa dicono i genitori e gli insegnanti che lo stanno già usando:"),
    ("Depoimentos reais de quem viu a transformação na prática:", "Messaggi reali di chi ha visto la trasformazione nei propri figli:"),
    
    # Bonuses section
    ("Bônus Exclusivos Inclusos Hoje:", "4 Bonus Esclusivi Inclusi Gratuitamente Oggi:"),
    ("BÔNUS 1: Guia Rápido de Leitura em Família", "BONUS 1: Guida Pratica per Genitori"),
    ("Como ajudar o seu filho a ler melhor sem estresse e sem cobrança excessiva.", "Come supportare tuo figlio nello studio a casa favorendo concentrazione e serenità."),
    ("BÔNUS 2: Cronograma de 15 Minutos por Dia", "BONUS 2: Piano di Studio Giornaliero di 15 Minuti"),
    ("Um plano simples para manter a rotina sem cansar a criança.", "Un calendario guidato per mantenere la costanza senza appesantire il pomeriggio."),
    ("BÔNUS 3: Jogos de Vocabulário para Imprimir", "BONUS 3: Mappe Mentali e Schemi Visivi"),
    ("Atividades lúdicas para fixar o aprendizado brincando.", "Strumenti visivi efficaci per imparare a riassumere i testi e prepararsi alle verifiche."),
    ("BÔNUS 4: Gabarito Completo de Todas as Atividades", "BONUS 4: Soluzioni Complete per i Genitori"),
    ("Para você corrigir as tarefas em segundos, sem precisar ler tudo.", "Tutte le risposte dettagliate per verificare le attività in pochi secondi."),
    
    # Guarantee section
    ("Garantia Incondicional de 7 Dias", "Garanzia Incondizionata di 7 Giorni"),
    ("Se por qualquer motivo você achar que o material não é para o seu filho, basta enviar um e-mail em até 7 dias que devolvemos 100% do seu dinheiro. Sem perguntas, sem burocracia.", "Hai 7 giorni interi per provare il Kit con tuo figlio. Se per qualsiasi motivo non sarai soddisfatto dei suoi progressi, basta inviarci un'email e ti restituiremo il 100% dell'importo speso, subito e senza complicazioni."),
    
    # FAQ Title
    ("Perguntas Frequentes", "Domande Frequenti"),
    ("Dúvidas Comuns:", "Domande Frequenti:"),
]

for src, trg in translations:
    code = code.replace(src, trg)

# Remove the photo of Camila Medeiros
# In the original code:
# <div className="a-img-ele-382c700 atomicat-image a-img-ele a-r a-e-cont atomicat-element-container-382c700"><img loading="lazy" ... src="images/382c7002-1565-47e7-864c-ec3eb038e3fe-misc-src.jpeg#588038" ... /></div>
# Let's replace that image block and translate the Specialist Section
code = re.sub(
    r'<div class(?:Name)?=[\"\'][^\"\']*a-img-ele-382c700[^\"\']*[\"\'].*?<\/div><\/div>',
    '</div>',
    code,
    flags=re.DOTALL
)

# Also update Camila Medeiros text
camila_old_pattern = r'Quem é Camila\?.*?Prazer, eu sou Camila Medeiros.*?(?=<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/div>)'
specialist_italian = """Chi ha ideato questo metodo?</h3></div></div><div className="a-c-cont a-c-cont-7833f39 a-r"><div className="atomicat-heading-title-7833f39 atomicat-text-7833f39 a-e-cont atomicat-element-container-7833f39 a-r atomicat-heading-title"><h3 className="a-i-e-cont"><p>Un team di specialisti in <strong>psicopedagogia infantile e apprendimento scolastico</strong>.</p><p><br /></p><p>Nel corso degli anni, affiancando centinaia di studenti e le loro famiglie, abbiamo riscontrato una difficoltà comune: il bambino riesce a leggere le parole, ma non comprende a fondo il senso di ciò che legge.</p><p><br /></p><p>Questo genera frustrazione, insicurezza e voti bassi anche in materie come matematica e scienze. Da questa esperienza nasce il <strong>Kit Comprensione del Testo 2.0</strong>: un percorso strutturato, graduale e stimolante per dare a ogni bambino gli strumenti per comprendere, imparare con entusiasmo e superare ogni difficoltà scolastica.</p></h3></div>"""

code = re.sub(r'Quem é Camila\?.*?Prazer, eu sou Camila Medeiros.*?(?=<div class="a-b-o-cont|<!-- container - nr6for)', specialist_italian, code, flags=re.DOTALL)
# Try also matching JSX className
code = re.sub(r'Quem é Camila\?.*?Prazer, eu sou Camila Medeiros.*?(?=<div className="a-b-o-cont|{/\*  container - nr6for)', specialist_italian, code, flags=re.DOTALL)

# Let's also ensure any remaining Portuguese strings or prices are cleaned up
code = code.replace("R$539", "€97")
code = code.replace("R$67", "€27")
code = code.replace("R$ 67", "€27")
code = code.replace("R$ 539", "€97")
code = code.replace("R$8,80", "€9,00")
code = code.replace("R$ 8,80", "€9,00")
code = code.replace("psicopedagoga e mãe", "specialisti in psicopedagogia infantile")
code = code.replace("Camila Medeiros", "Metodo Comprensione del Testo 2.0")
code = code.replace("Camila", "il Nostro Metodo")

with open('index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print('Updated index.tsx with Italian translations!')
