import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import KitInterpretarParaEvoluir from './index';
import DownloadPage from './DownloadPage';

function App() {
  const [currentPath, setCurrentPath] = useState(window.location.pathname);

  useEffect(() => {
    const handlePopState = () => {
      setCurrentPath(window.location.pathname);
    };
    window.addEventListener('popstate', handlePopState);
    return () => window.removeEventListener('popstate', handlePopState);
  }, []);

  const normalized = currentPath.toLowerCase().replace(/\/$/, '');

  if (normalized === '/download') {
    return <DownloadPage />;
  }

  return <KitInterpretarParaEvoluir />;
}

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
