import React, { useState } from 'react';
import './landing.css';

interface DownloadItem {
  id: string;
  isMain?: boolean;
  tag: string;
  title: string;
  subtitle: string;
  description: string;
  pages: string;
  size: string;
  filename: string;
  features?: string[];
  badgeColor?: string;
}

const mainProduct: DownloadItem = {
  id: 'main',
  isMain: true,
  tag: 'MATERIALE PRINCIPALE · 195 PAGINE',
  title: 'Interpretare per Evolvere — Percorso di Comprensione del Testo 2.0',
  subtitle: '587 Attività Didattiche Progressive (Livelli 1, 2 e 3)',
  description:
    'Il manuale didattico completo con 90 schede strutturate per bambini dai 7 ai 12 anni. Include la guida metodologica per genitori, il test di livello iniziale, tutte le chiavi di risposta dettagliate e l\'attestato ufficiale di merito.',
  pages: '195 Pagine (PDF)',
  size: '19.7 MB',
  filename: '/Interpretare_per_Evolvere.pdf',
  badgeColor: '#887396',
  features: [
    '3 Livelli progressivi per scuola primaria e secondaria (7-12 anni)',
    'Lettura rapida, comprensione diretta, inferenze e vocabolario attivo',
    'Testi interdisciplinari (Italiano, Storia, Scienze, Geografia e Matematica)',
    'Tutte le chiavi di risposta complete + Attestato Finale di Merito'
  ]
};

const bonusItems: DownloadItem[] = [
  {
    id: 'bonus1',
    tag: 'BONUS 1 · INCLUSO',
    title: 'Kit Calligrafia Perfetta',
    subtitle: 'Guida Pratica per una Scrittura Chiara e Fluida',
    description:
      'Schede progressive per correggere l\'impugnatura, la postura e la fluidità del corsivo con soli 10 minuti di allenamento al giorno.',
    pages: '40 Pagine (PDF)',
    size: '233 KB',
    filename: '/Kit_Calligrafia_Perfetta.pdf',
    badgeColor: '#be868c'
  },
  {
    id: 'bonus2',
    tag: 'BONUS 2 · INCLUSO',
    title: 'Ora di Lettura',
    subtitle: '24 Testi con Cronometro e Autovalutazione',
    description:
      '24 testi coinvolgenti divisi in 3 livelli di lunghezza, con sfide a tempo e autovalutazione a stelle per stimolare concentrazione e costanza.',
    pages: '42 Pagine (PDF)',
    size: '2.3 MB',
    filename: '/Ora_di_Lettura.pdf',
    badgeColor: '#887396'
  },
  {
    id: 'bonus3',
    tag: 'BONUS 3 · INCLUSO',
    title: 'Semplificando la Matematica di Base',
    subtitle: '120 Esercizi Pratici e Problemi Guidati',
    description:
      'Percorso graduale con addizioni, sottrazioni, tabelline, divisioni e problemi guidati con soluzioni per dare sicurezza con i numeri.',
    pages: '31 Pagine (PDF)',
    size: '85 KB',
    filename: '/Semplificando_la_Matematica_di_Base.pdf',
    badgeColor: '#be868c'
  }
];

export default function DownloadPage() {
  const [downloadedList, setDownloadedList] = useState<string[]>([]);
  const [isDownloadingAll, setIsDownloadingAll] = useState(false);

  const handleDownload = (item: DownloadItem) => {
    if (!downloadedList.includes(item.id)) {
      setDownloadedList(prev => [...prev, item.id]);
    }
  };

  const handleDownloadAll = () => {
    setIsDownloadingAll(true);
    const allFiles = [mainProduct, ...bonusItems];
    allFiles.forEach((item, index) => {
      setTimeout(() => {
        const link = document.createElement('a');
        link.href = item.filename;
        link.download = item.filename.replace('/', '');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);

        if (!downloadedList.includes(item.id)) {
          setDownloadedList(prev => [...prev, item.id]);
        }
        if (index === allFiles.length - 1) {
          setIsDownloadingAll(false);
        }
      }, index * 450);
    });
  };

  return (
    <div
      style={{
        minHeight: '100vh',
        backgroundColor: '#f7f8fa',
        color: '#363636',
        fontFamily: 'Roboto, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
        display: 'flex',
        flexDirection: 'column',
        WebkitFontSmoothing: 'antialiased'
      }}
    >
      {/* Top Brand Notification Banner */}
      <div
        style={{
          background: '#887396',
          color: '#ffffff',
          textAlign: 'center',
          padding: '10px 16px',
          fontSize: '14px',
          fontWeight: 600,
          fontFamily: 'Poppins, sans-serif',
          letterSpacing: '0.3px'
        }}
      >
        ✨ Accesso a Vita Garantito · Salva questa pagina tra i preferiti del tuo browser
      </div>

      {/* Main Header */}
      <header
        style={{
          background: '#ffffff',
          borderBottom: '1.5px solid #e6e8ea',
          padding: '48px 20px 40px 20px',
          textAlign: 'center'
        }}
      >
        <div style={{ maxWidth: '860px', margin: '0 auto' }}>
          <div
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '8px',
              background: 'rgba(136, 115, 150, 0.12)',
              border: '1.5px solid #887396',
              color: '#887396',
              fontWeight: 700,
              fontSize: '12px',
              padding: '6px 18px',
              borderRadius: '20px',
              letterSpacing: '0.8px',
              marginBottom: '20px',
              textTransform: 'uppercase',
              fontFamily: 'Poppins, sans-serif'
            }}
          >
            <span>🔒</span>
            <span>Area Riservata Clienti · Download Immediato</span>
          </div>

          <h1
            style={{
              fontSize: 'clamp(28px, 4vw, 42px)',
              fontWeight: 700,
              lineHeight: '1.25',
              marginBottom: '14px',
              color: '#363636',
              fontFamily: 'Poppins, sans-serif'
            }}
          >
            I Tuoi Materiali Didattici
          </h1>

          <p
            style={{
              fontSize: '17px',
              color: '#6b6b6b',
              maxWidth: '680px',
              margin: '0 auto 28px auto',
              lineHeight: '1.6'
            }}
          >
            Congratulazioni per il tuo acquisto! Tutti i file PDF del <strong style={{ color: '#887396' }}>Kit Comprensione del Testo 2.0</strong> e i rispettivi <strong style={{ color: '#be868c' }}>Bonus Esclusivi</strong> sono pronti per essere scaricati e stampati.
          </p>

          {/* Quick 1-Click Download All Button */}
          <button
            onClick={handleDownloadAll}
            disabled={isDownloadingAll}
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '12px',
              background: '#00a1e6',
              color: '#ffffff',
              fontWeight: 700,
              fontSize: '17px',
              padding: '16px 36px',
              borderRadius: '14px',
              border: 'none',
              cursor: isDownloadingAll ? 'wait' : 'pointer',
              boxShadow: '0 8px 24px rgba(0, 161, 230, 0.35)',
              transition: 'transform 0.2s ease, box-shadow 0.2s ease',
              textTransform: 'uppercase',
              fontFamily: 'Poppins, sans-serif'
            }}
            onMouseOver={e => {
              e.currentTarget.style.transform = 'translateY(-2px)';
              e.currentTarget.style.boxShadow = '0 12px 28px rgba(0, 161, 230, 0.45)';
            }}
            onMouseOut={e => {
              e.currentTarget.style.transform = 'translateY(0)';
              e.currentTarget.style.boxShadow = '0 8px 24px rgba(0, 161, 230, 0.35)';
            }}
          >
            <svg
              style={{ width: '20px', height: '20px' }}
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2.5"
                d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"
              />
            </svg>
            <span>{isDownloadingAll ? 'Download in corso...' : 'Scarica Tutti i File in 1 Clic (4 PDF)'}</span>
          </button>
        </div>
      </header>

      {/* Main Content Area */}
      <main style={{ maxWidth: '1040px', margin: '0 auto', padding: '44px 20px', width: '100%', flex: 1 }}>
        {/* Main Product Card */}
        <section style={{ marginBottom: '44px' }}>
          <div
            style={{
              background: '#ffffff',
              border: '2.5px solid #887396',
              borderRadius: '20px',
              padding: 'clamp(24px, 4vw, 36px)',
              boxShadow: '0 8px 30px rgba(136, 115, 150, 0.12)',
              position: 'relative'
            }}
          >
            {/* Tag Badge */}
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', marginBottom: '16px' }}>
              <span
                style={{
                  background: '#887396',
                  color: '#ffffff',
                  fontWeight: 700,
                  fontSize: '12px',
                  padding: '5px 14px',
                  borderRadius: '8px',
                  textTransform: 'uppercase',
                  letterSpacing: '0.5px',
                  fontFamily: 'Poppins, sans-serif'
                }}
              >
                {mainProduct.tag}
              </span>
              <span
                style={{
                  background: 'rgba(0, 199, 56, 0.12)',
                  color: '#00963a',
                  border: '1px solid #00c738',
                  fontWeight: 700,
                  fontSize: '12px',
                  padding: '5px 14px',
                  borderRadius: '8px',
                  fontFamily: 'Poppins, sans-serif'
                }}
              >
                Completo & Aggiornato 2026
              </span>
            </div>

            <h2
              style={{
                fontSize: 'clamp(22px, 3vw, 28px)',
                fontWeight: 700,
                color: '#363636',
                marginBottom: '6px',
                lineHeight: '1.3',
                fontFamily: 'Poppins, sans-serif'
              }}
            >
              {mainProduct.title}
            </h2>

            <p
              style={{
                color: '#887396',
                fontSize: '16px',
                fontWeight: 600,
                marginBottom: '16px',
                fontFamily: 'Poppins, sans-serif'
              }}
            >
              {mainProduct.subtitle}
            </p>

            <p style={{ color: '#555555', fontSize: '15px', lineHeight: '1.6', marginBottom: '22px' }}>
              {mainProduct.description}
            </p>

            {/* Checklist features */}
            <div
              style={{
                background: '#f7f8fa',
                border: '1.5px solid #e6e8ea',
                borderRadius: '14px',
                padding: '20px',
                marginBottom: '26px'
              }}
            >
              <div
                style={{
                  fontWeight: 700,
                  fontSize: '14px',
                  color: '#363636',
                  marginBottom: '12px',
                  fontFamily: 'Poppins, sans-serif',
                  textTransform: 'uppercase',
                  letterSpacing: '0.4px'
                }}
              >
                Cosa include questo manuale:
              </div>
              <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '10px' }}>
                {mainProduct.features?.map((feat, idx) => (
                  <li key={idx} style={{ display: 'flex', alignItems: 'flex-start', gap: '10px', fontSize: '15px', color: '#363636' }}>
                    <svg
                      style={{ width: '20px', height: '20px', color: '#00c738', flexShrink: 0, marginTop: '2px' }}
                      fill="currentColor"
                      viewBox="0 0 512 512"
                    >
                      <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM369 209L241 337c-9.4 9.4-24.6 9.4-33.9 0l-64-64c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.4 33.9 0l47 47L335 175c9.4-9.4 24.6-9.4 33.9 0s9.4 24.6 0 33.9z" />
                    </svg>
                    <span>{feat}</span>
                  </li>
                ))}
              </ul>
            </div>

            {/* Action Bar */}
            <div
              style={{
                display: 'flex',
                flexWrap: 'wrap',
                alignItems: 'center',
                justifyContent: 'space-between',
                gap: '16px',
                paddingTop: '8px',
                borderTop: '1px solid #e6e8ea'
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '16px', flexWrap: 'wrap' }}>
                <span
                  style={{
                    fontSize: '14px',
                    fontWeight: 600,
                    color: '#6b6b6b',
                    background: '#f4f0f5',
                    padding: '6px 12px',
                    borderRadius: '8px'
                  }}
                >
                  📄 {mainProduct.pages}
                </span>
                <span
                  style={{
                    fontSize: '14px',
                    fontWeight: 600,
                    color: '#6b6b6b',
                    background: '#f4f0f5',
                    padding: '6px 12px',
                    borderRadius: '8px'
                  }}
                >
                  💾 {mainProduct.size}
                </span>
              </div>

              <a
                href={mainProduct.filename}
                download="Interpretare_per_Evolvere.pdf"
                onClick={() => handleDownload(mainProduct)}
                style={{
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '10px',
                  background: downloadedList.includes(mainProduct.id) ? '#00963a' : '#00a1e6',
                  color: '#ffffff',
                  fontWeight: 700,
                  fontSize: '16px',
                  padding: '14px 28px',
                  borderRadius: '14px',
                  textDecoration: 'none',
                  boxShadow: downloadedList.includes(mainProduct.id)
                    ? '0 6px 18px rgba(0, 150, 58, 0.3)'
                    : '0 6px 18px rgba(0, 161, 230, 0.35)',
                  transition: 'all 0.2s ease',
                  textTransform: 'uppercase',
                  fontFamily: 'Poppins, sans-serif'
                }}
              >
                <svg
                  style={{ width: '18px', height: '18px' }}
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2.5"
                    d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"
                  />
                </svg>
                <span>{downloadedList.includes(mainProduct.id) ? 'Scaricato ✅ (Riscarica)' : 'Scarica Manuale (PDF)'}</span>
              </a>
            </div>
          </div>
        </section>

        {/* Bonus Section Title */}
        <div style={{ textAlign: 'center', marginBottom: '28px' }}>
          <div
            style={{
              display: 'inline-block',
              background: 'rgba(190, 134, 140, 0.14)',
              border: '1.5px solid #be868c',
              color: '#be868c',
              fontWeight: 700,
              fontSize: '12px',
              padding: '5px 16px',
              borderRadius: '20px',
              letterSpacing: '0.8px',
              marginBottom: '12px',
              textTransform: 'uppercase',
              fontFamily: 'Poppins, sans-serif'
            }}
          >
            I Tuoi 3 Bonus Esclusivi
          </div>
          <h2
            style={{
              fontSize: 'clamp(24px, 3.2vw, 32px)',
              fontWeight: 700,
              color: '#363636',
              fontFamily: 'Poppins, sans-serif'
            }}
          >
            Materiali Integrativi Gratuiti
          </h2>
          <p style={{ color: '#6b6b6b', fontSize: '16px', marginTop: '6px' }}>
            Inclusi gratuitamente nel tuo ordine per potenziare ogni aspetto dello studio.
          </p>
        </div>

        {/* 3 Bonus Cards Grid */}
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
            gap: '24px',
            marginBottom: '48px'
          }}
        >
          {bonusItems.map((bonus) => {
            const isDownloaded = downloadedList.includes(bonus.id);
            return (
              <div
                key={bonus.id}
                style={{
                  background: '#ffffff',
                  border: `2px solid ${bonus.badgeColor || '#887396'}`,
                  borderRadius: '18px',
                  padding: '28px 24px',
                  boxShadow: '0 6px 20px rgba(0, 0, 0, 0.05)',
                  display: 'flex',
                  flexDirection: 'column',
                  justifyContent: 'space-between',
                  transition: 'transform 0.2s ease, box-shadow 0.2s ease'
                }}
              >
                <div>
                  {/* Tag */}
                  <div style={{ marginBottom: '14px' }}>
                    <span
                      style={{
                        background: bonus.badgeColor || '#887396',
                        color: '#ffffff',
                        fontWeight: 700,
                        fontSize: '11px',
                        padding: '4px 10px',
                        borderRadius: '6px',
                        textTransform: 'uppercase',
                        letterSpacing: '0.4px',
                        fontFamily: 'Poppins, sans-serif'
                      }}
                    >
                      {bonus.tag}
                    </span>
                  </div>

                  <h3
                    style={{
                      fontSize: '20px',
                      fontWeight: 700,
                      color: '#363636',
                      marginBottom: '6px',
                      lineHeight: '1.3',
                      fontFamily: 'Poppins, sans-serif'
                    }}
                  >
                    {bonus.title}
                  </h3>

                  <p
                    style={{
                      color: bonus.badgeColor || '#887396',
                      fontSize: '14px',
                      fontWeight: 600,
                      marginBottom: '12px',
                      fontFamily: 'Poppins, sans-serif'
                    }}
                  >
                    {bonus.subtitle}
                  </p>

                  <p style={{ color: '#666666', fontSize: '14px', lineHeight: '1.55', marginBottom: '20px' }}>
                    {bonus.description}
                  </p>
                </div>

                <div>
                  {/* Meta */}
                  <div
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: '10px',
                      marginBottom: '16px',
                      fontSize: '13px',
                      color: '#777777',
                      background: '#f7f8fa',
                      padding: '8px 12px',
                      borderRadius: '8px'
                    }}
                  >
                    <span>📄 {bonus.pages}</span>
                    <span>·</span>
                    <span>💾 {bonus.size}</span>
                  </div>

                  {/* Download Button */}
                  <a
                    href={bonus.filename}
                    download={bonus.filename.replace('/', '')}
                    onClick={() => handleDownload(bonus)}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      gap: '8px',
                      background: isDownloaded ? '#00963a' : '#00a1e6',
                      color: '#ffffff',
                      fontWeight: 700,
                      fontSize: '14px',
                      padding: '13px 18px',
                      borderRadius: '12px',
                      textDecoration: 'none',
                      boxShadow: isDownloaded
                        ? '0 4px 14px rgba(0, 150, 58, 0.25)'
                        : '0 4px 14px rgba(0, 161, 230, 0.3)',
                      transition: 'all 0.2s ease',
                      textTransform: 'uppercase',
                      fontFamily: 'Poppins, sans-serif',
                      width: '100%',
                      boxSizing: 'border-box'
                    }}
                  >
                    <svg
                      style={{ width: '16px', height: '16px' }}
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2.5"
                        d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"
                      />
                    </svg>
                    <span>{isDownloaded ? 'Scaricato ✅' : 'Scarica PDF'}</span>
                  </a>
                </div>
              </div>
            );
          })}
        </div>

        {/* Instructions & Printing Guide Section */}
        <section
          style={{
            background: '#ffffff',
            border: '1.5px solid #e6e8ea',
            borderRadius: '20px',
            padding: '36px 28px',
            marginBottom: '44px',
            boxShadow: '0 4px 16px rgba(0, 0, 0, 0.04)'
          }}
        >
          <div style={{ textAlign: 'center', marginBottom: '28px' }}>
            <h3
              style={{
                fontSize: '22px',
                fontWeight: 700,
                color: '#363636',
                fontFamily: 'Poppins, sans-serif',
                marginBottom: '8px'
              }}
            >
              💡 Consigli per l'Uso e la Stampa dei Materiali
            </h3>
            <p style={{ color: '#6b6b6b', fontSize: '15px' }}>
              Tre semplici passaggi per ottenere i massimi risultati senza alcuno stress.
            </p>
          </div>

          <div
            style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))',
              gap: '20px'
            }}
          >
            <div
              style={{
                background: '#f7f8fa',
                border: '1.5px solid #e6e8ea',
                borderRadius: '14px',
                padding: '22px'
              }}
            >
              <div
                style={{
                  fontSize: '24px',
                  marginBottom: '10px'
                }}
              >
                🖨️
              </div>
              <h4
                style={{
                  fontSize: '16px',
                  fontWeight: 700,
                  color: '#363636',
                  fontFamily: 'Poppins, sans-serif',
                  marginBottom: '8px'
                }}
              >
                1. Stampa Solo al Bisogno
              </h4>
              <p style={{ fontSize: '14px', color: '#666666', lineHeight: '1.5' }}>
                Non serve stampare 195 pagine in una volta! Stampa solo 1 o 2 schede al giorno per mantenere l'allenamento leggero e piacevole.
              </p>
            </div>

            <div
              style={{
                background: '#f7f8fa',
                border: '1.5px solid #e6e8ea',
                borderRadius: '14px',
                padding: '22px'
              }}
            >
              <div
                style={{
                  fontSize: '24px',
                  marginBottom: '10px'
                }}
              >
                📱
              </div>
              <h4
                style={{
                  fontSize: '16px',
                  fontWeight: 700,
                  color: '#363636',
                  fontFamily: 'Poppins, sans-serif',
                  marginBottom: '8px'
                }}
              >
                2. Utilizzo su Tablet o Schermo
              </h4>
              <p style={{ fontSize: '14px', color: '#666666', lineHeight: '1.5' }}>
                Se preferisci non stampare, tuo figlio può leggere i testi direttamente da tablet o computer e scrivere le risposte sul proprio quaderno.
              </p>
            </div>

            <div
              style={{
                background: '#f7f8fa',
                border: '1.5px solid #e6e8ea',
                borderRadius: '14px',
                padding: '22px'
              }}
            >
              <div
                style={{
                  fontSize: '24px',
                  marginBottom: '10px'
                }}
              >
                🔑
              </div>
              <h4
                style={{
                  fontSize: '16px',
                  fontWeight: 700,
                  color: '#363636',
                  fontFamily: 'Poppins, sans-serif',
                  marginBottom: '8px'
                }}
              >
                3. Soluzioni Dettagliate
              </h4>
              <p style={{ fontSize: '14px', color: '#666666', lineHeight: '1.5' }}>
                Al fondo di ogni volume trovi le chiavi di correzione complete per verificare le risposte in pochi secondi con tuo figlio.
              </p>
            </div>
          </div>
        </section>

        {/* Support & Guarantee Purple Card */}
        <section
          style={{
            background: '#887396',
            color: '#ffffff',
            borderRadius: '20px',
            padding: '32px',
            textAlign: 'center',
            boxShadow: '0 8px 24px rgba(136, 115, 150, 0.25)'
          }}
        >
          <div style={{ fontSize: '32px', marginBottom: '12px' }}>🛡️</div>
          <h3
            style={{
              fontSize: '22px',
              fontWeight: 700,
              color: '#ffffff',
              fontFamily: 'Poppins, sans-serif',
              marginBottom: '10px'
            }}
          >
            Hai Bisogno di Assistenza o Hai Smarrito i File?
          </h3>
          <p
            style={{
              fontSize: '15px',
              color: 'rgba(255, 255, 255, 0.92)',
              maxWidth: '640px',
              margin: '0 auto 20px auto',
              lineHeight: '1.6'
            }}
          >
            Il tuo acquisto include l'accesso a vita a tutti gli aggiornamenti futuri del materiale. Se hai qualsiasi domanda o difficoltà con i download, il nostro supporto è a tua completa disposizione.
          </p>
          <div
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '8px',
              background: 'rgba(255, 255, 255, 0.18)',
              border: '1px solid rgba(255, 255, 255, 0.35)',
              padding: '8px 20px',
              borderRadius: '20px',
              fontSize: '14px',
              fontWeight: 600,
              fontFamily: 'Poppins, sans-serif'
            }}
          >
            ✉️ Supporto via Email: risposte entro 24 ore lavorative
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer
        style={{
          background: '#ffffff',
          borderTop: '1.5px solid #e6e8ea',
          padding: '32px 20px',
          textAlign: 'center',
          fontSize: '14px',
          color: '#888888',
          fontFamily: 'Roboto, sans-serif'
        }}
      >
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <p style={{ marginBottom: '8px' }}>
            © {new Date().getFullYear()} Interpretare per Evolvere — Tutti i diritti riservati.
          </p>
          <p style={{ fontSize: '13px', color: '#aaaaaa' }}>
            Kit Didattico di Comprensione del Testo 2.0 per Scuola Primaria e Secondaria di Primo Grado.
          </p>
        </div>
      </footer>
    </div>
  );
}
