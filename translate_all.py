import re

with open('index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

replacements = [
    # Top comparison
    ("Quando o seu filho tenta estudar e não entende nada…", "Quando tuo figlio prova a studiare e non capisce nulla…"),
    ("Quando tuo filho si allena con le schede e inizia subito a melhorar", "Quando tuo figlio si allena con le schede e inizia subito a migliorare"),
    
    # Problem list
    ("Seu filho odeia ler e escrever", "Tuo figlio odia leggere e scrivere"),
    ("Lê e não consegue explicar com as próprias palavras", "Legge ma non riesce a spiegare con le proprie parole"),
    ("Não consegue estudar sozinho", "Non riesce a studiare da solo"),
    ("Leitura pausada ou com pouca fluência", "Lettura lenta, frammentata o con poca fluidità"),
    ("Sente dificuldade em várias disciplinas", "Incontra difficoltà in diverse materie scolastiche"),
    
    # Solution list
    ("Com o treino certo, em poucas semanas isso vira:", "Con il giusto allenamento, in poche settimane si trasforma in:"),
    ("Seu filho lê com mais vontade e menos resistência", "Tuo figlio legge con più entusiasmo e meno resistenza"),
    ("Entende o que leu e explica com as próprias palavras", "Comprende ciò che legge e lo rispiega con le proprie parole"),
    ("Consegue estudar sozinho, com mais autonomia", "Riesce a studiare in autonomia, senza bisogno di aiuto continuo"),
    ("Leitura mais fluente e segura", "Lettura più fluida, rapida e sicura"),
    ("Mais confiança e notas melhores em todas as disciplinas", "Maggiore autostima e voti più alti in tutte le materie"),
    
    # Middle section
    ("Você não precisa gastar uma fortuna com reforço escolar para o seu filho compreender os textos e estudar sozinho…", "Non serve spendere una fortuna in ripetizioni per insegnare a tuo figlio a comprendere i testi e studiare da solo…"),
    ("Basta escolher 1 atividade, imprimir, entregar para o seu filho realizar e ver a mágica acontecer.", "Basta scegliere 1 scheda, stamparla (o usarla a schermo), consegnarla a tuo figlio e vedere i progressi giorno dopo giorno."),
    ("Não precisa pensar. É só escolher e entregar.", "Nessuna preparazione richiesta. Scegli, assegni e alleni la mente."),
    ("Com as 587 Atividades de Interpretação de Textos prontas, você apenas precisa:", "Con le 587 Attività di Comprensione pronte all'uso, ti basta:"),
    ("1 - Abrir e escolher o conteúdo do dia", "1 - Aprire il PDF e scegliere la scheda del giorno"),
    ("2 - Não precisa pensar demais nem inventar nada", "2 - Zero stress: nessun esercizio da inventare o cercare online"),
    ("3 - Imprimir (ou realizar no caderno, sem imprimir)", "3 - Stampare (o svolgere direttamente sul quaderno)"),
    ("4 - Ver o seu filho preparado para todas as disciplinas e futuro profissional", "4 - Vedere tuo figlio sicuro, preparato e pronto per ogni materia"),
    
    # Educational validation
    ("⚠️ Não é um pacote de atividades genéricas para qualquer idade...", "⚠️ Non è una raccolta generica di schede scaricate a caso..."),
    ("Foram meses de estudos e testes de atividades para organizar e catalogar os exercícios que proporcionam os melhores resultados, alinhado com o BNCC.", "È il frutto di mesi di progettazione psicopedagogica per strutturare esercizi progressivi e ad alto impatto didattico per la scuola primaria e media."),
    
    # Target audience
    ("O Kit Inter Evoluir 2.0 é pra você que:", "Il Kit Comprensione del Testo 2.0 è perfetto per te se:"),
    ("Tem um filho de 7 a 12 anos que lê, mas não entende o que leu", "Hai un figlio dai 7 ai 12 anni che legge ma fatica a comprendere il testo"),
    ("Quer que ele estude sozinho, sem você sentar do lado em toda tarefa", "Vuoi che impari a fare i compiti da solo, senza che tu debba stargli sempre accanto"),
    ("Cansou de gastar com reforço e material que não dá resultado", "Sei stanco di spendere soldi in ripetizioni costose o materiale poco chiaro"),
    ("Precisa de algo pronto pra aplicar hoje, sem ter que criar nada", "Hai bisogno di materiale pronto all'uso da iniziare subito oggi stesso"),
    ("Quer notas melhores em todas as disciplinas, não só em português", "Desideri voti più alti in tutte le materie: italiano, matematica, scienze e storia"),
    
    # Testimonials
    ("O que as mães estão dizendo 💬", "Cosa dicono le mamme e gli insegnanti 💬"),
    ("Em 3 semanas minha filha já consegue resumir o que leu. Nunca tinha visto ela entender e fazer sozinha.", "In sole 3 settimane mia figlia riesce a riassumere qualsiasi brano. Non l'avevo mai vista così autonoma e serena nello studio."),
    ("— Renata O.", "— Laura B."),
    ("Comecei semana passada e meu filho já me chama pra mostrar o que conseguiu. Mais confiante do que nunca.", "Abbiamo iniziato la scorsa settimana e mio figlio ora mi chiama orgoglioso per farmi vedere gli esercizi completati. Molto più sicuro di sé!"),
    ("— Cliente verificada", "— Mamma verificata"),
    
    # Pricing stack
    ("Todos estes longos meses de estudo poderiam custar muito mais, mas eu quero que você consiga", "Tutto questo materiale didattico ha un valore reale molto più alto, ma vogliamo che tu possa"),
    ("MUDAR O FUTURO DO SEU FILHO", "TRASFORMARE LO STUDIO DI TUO FIGLIO"),
    ("de uma forma prática, e democratizar a educação para todos.", "in modo pratico, accessibile ed efficace per ogni famiglia."),
    ("👉 587 Atividades Ultra Eficientes -", "👉 587 Schede Didattiche di Comprensione Rapida -"),
    ("👉 Caderno de Interpretação de textos com letra cursiva -", "👉 Modulo 2: Testi con Domande Dirette e Inferenze -"),
    ("👉 Atividades de interpretação de textos em vídeo, com letra cursiva -", "👉 Modulo 3: Esercizi di Vocabolario Attivo -"),
    ("👉 Cards de Interpretação de textos para praticar -", "👉 Modulo 4: Comprensione Interdisciplinare (Matematica, Scienze, Storia) -"),
    ("👉 Superbônus: Análise individual do nível de interpretação de textos -", "👉 4 Super Bonus Esclusivi (Guide per Genitori, Piano 15 Minuti, Mappe & Soluzioni) -"),
    ("👉Além das atividades você vai receber de bônus:", "👉 Oltre alle 587 attività riceverai anche questi 4 Bonus:"),
    ("587 atividades + todos os bônus", "587 attività + tutti i 4 bonus inclusi"),
    ("por apenas", "a soli"),
    ("QUERO GARANTIR AGORA", "VOGLIO IL KIT COMPLETO A €27"),
    ("Tudo isso deveria custar", "Valore complessivo:"),
    ("... mas hoje você leva por apenas:", "... ma oggi accedi a tutto con soli:"),
    ("9x de €9,00", "Offerta promozionale unica"),
    ("€27,00 à vista", "€27 in pagamento unico (nessun abbonamento)"),
    ("Você economiza", "Risparmi oltre"),
    ("e tem", "e hai"),
    ("acesso imediato", "accesso immediato"),
    ("após a compra.", "subito dopo l'acquisto."),
    ("🔒 Compra 100% segura · Pix e cartão em até 9x · Acesso enviado na hora pela Hotmart", "🔒 Pagamento protetto e sicuro al 100% · Consegna immediata via email"),
    
    # Two paths
    ("Agora você tem dois caminhos:", "Adesso hai due strade davanti a te:"),
    ("❌ Continuar como está", "❌ Rimanere nella situazione attuale"),
    ("Seu filho seguir travando na leitura, perdendo confiança e dependendo de você (ou de reforço caro) em cada tarefa.", "Tuo figlio continuerà a bloccarsi nella lettura, perdendo autostima e dipendendo sempre da te o da costose ripetizioni per ogni singolo compito."),
    ("✅ Começar hoje por €27", "✅ Iniziare oggi con soli €27"),
    ("Em poucos minutos ele faz a primeira atividade e começa a interpretar sozinho, com mais confiança e notas melhores.", "In pochi minuti svolge la prima scheda e impara a comprendere da solo, con più sicurezza, autonomia e voti migliori."),
    ("Você já sabe qual é a escolha mais inteligente.", "Sai già quale scelta farà davvero la differenza per il suo futuro scolastico."),
    ("QUERO COMEÇAR AGORA POR €27", "VOGLIO INIZIARE SUBITO A SOLI €27"),
    
    # Specialist section text cleanup
    ("Quem é il Nostro Metodo?", "Chi ha ideato questo metodo?"),
    ("Quem é Camila?", "Chi ha ideato questo metodo?"),
    ("Prazer, eu sou", "Un team di professionisti specializzati in psicopedagogia e apprendimento infantile."),
    ("Metodo Comprensione del Testo 2.0,", ""),
    ("specialisti in psicopedagogia infantile.", ""),
    ("Ao longo dos anos, acompanhando crianças e suas dificuldades de aprendizagem,", "Nel corso degli anni, seguendo da vicino centinaia di studenti e supportando le famiglie,"),
    ("percebi um problema que se repete em muitas casas", "abbiamo individuato la radice del problema comune a tantissimi bambini"),
    (": a criança até lê, mas não consegue entender de verdade o que leu. E quando a interpretação não acontece, ela começa a", ": riescono a leggere le parole ad alta voce, ma non comprendono il senso di ciò che leggono. E quando manca la comprensione profonda, il bambino inizia a"),
    ("errar", "sbagliare"),
    ("perder a confiança", "perdere autostima"),
    ("depender cada vez mais de ajuda.", "dipendere continuamente dall'aiuto degli altri."),
    ("Foi por isso que criei o", "Per questo abbiamo creato il"),
    ("KIT INTER EVOLUIR 2.0", "KIT COMPRENSIONE DEL TESTO 2.0"),
    (": um material prático, progressivo e fácil de aplicar,", ": un percorso strutturato, progressivo e semplice da applicare,"),
    ("para ajudar mães a desenvolverem a interpretação dos filhos", "per aiutare i genitori a sviluppare la comprensione dei propri figli"),
    ("com mais clareza, leveza e resultado no dia a dia.", "con metodo, serenità e risultati concreti ogni giorno."),
    ("Meu objetivo é", "Il nostro obiettivo è"),
    ("te entregar uma forma simples de começar, sem complicação e sem fazer você se sentir perdida.", "fornirti uno strumento chiaro ed efficace, pronto all'uso e senza complicazioni."),
    
    # Final CTA section
    ("Você já sabe o que quer. Só precisa de um empurrão.", "Sai già di cosa ha bisogno tuo figlio. Ora serve solo fare il primo passo."),
    ("Esse material é o atalho que você procurava para VIRAR A CHAVE da educação do seu filho. Nos próximos 5 minutos você já pode começar a primeira atividade e ver tudo mudar.", "Questo materiale è lo strumento pratico che cercavi per dare una SVOLTA all'istruzione di tuo figlio. Tra 5 minuti potrai già scaricare la prima scheda e vedere i primi miglioramenti."),
    ("SIM, QUERO COMEÇAR AGORA POR €27", "SÌ! VOGLIO IL KIT COMPLETO A SOLI €27"),
    
    # Guarantee box
    ("Garantia incondicional de 7 dias", "Garanzia Incondizionata di 7 Giorni"),
    ("Compre sem medo. Se em até 7 dias você sentir que o material não é para o seu filho, é só enviar uma mensagem e", "Acquista con totale tranquillità. Se entro 7 giorni ritieni che il materiale non faccia al caso di tuo figlio, ti basterà inviare un'email e"),
    ("devolvemos 100% do seu dinheiro", "ti restituiremo il 100% dell'importo speso"),
    ("— sem perguntas, sem burocracia. O risco é todo meu.", "— senza domande, senza burocrazia. Il rischio è interamente nostro."),
    
    # FAQ Title
    ("Perguntas frequentes", "Domande Frequenti"),
    
    # Remaining price values
    ("R$137", "Valore €47"),
    ("R$59", "Valore €29"),
    ("R$69", "Valore €29"),
    ("R$87", "Valore €37"),
    ("R$187", "Valore €49"),
    ("R$472", "€160"),
    ("R$ 137", "Valore €47"),
    ("R$ 59", "Valore €29"),
    ("R$ 69", "Valore €29"),
    ("R$ 87", "Valore €37"),
    ("R$ 187", "Valore €49"),
    ("R$ 472", "€160")
]

for src, trg in replacements:
    code = code.replace(src, trg)

# Remove any remaining specialist photo container completely if present
code = re.sub(
    r'<div class(?:Name)?=[\"\'][^\"\']*a-img-ele-382c700[^\"\']*[\"\'].*?<\/div><\/div>',
    '',
    code,
    flags=re.DOTALL
)

with open('index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print('Done full text replacement!')
