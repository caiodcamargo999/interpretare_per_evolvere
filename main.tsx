import React from 'react';
import ReactDOM from 'react-dom/client';
import KitInterpretarParaEvoluir, {
  HOTMART_CHECKOUT_URL,
  PAGGINS_CHECKOUT_URL,
  isHotmartRoute,
} from './index';

const checkoutUrl = isHotmartRoute() ? HOTMART_CHECKOUT_URL : PAGGINS_CHECKOUT_URL;

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <KitInterpretarParaEvoluir checkoutUrl={checkoutUrl} />
  </React.StrictMode>
);
