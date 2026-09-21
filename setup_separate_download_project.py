import os, shutil, subprocess, json

dest = os.path.abspath("../02_download-area-interpretare-per-evolvere")
os.makedirs(dest, exist_ok=True)
os.makedirs(os.path.join(dest, 'src'), exist_ok=True)
os.makedirs(os.path.join(dest, 'public'), exist_ok=True)
os.makedirs(os.path.join(dest, 'images'), exist_ok=True)
os.makedirs(os.path.join(dest, 'fonts'), exist_ok=True)

# 1. Copy PDFs to public/
for pdf in ['Interpretare_per_Evolvere.pdf', 'Kit_Calligrafia_Perfetta.pdf', 'Ora_di_Lettura.pdf', 'Semplificando_la_Matematica_di_Base.pdf']:
    src_pdf = os.path.join('public', pdf)
    if os.path.exists(src_pdf):
        shutil.copy2(src_pdf, os.path.join(dest, 'public', pdf))
        print(f'Copied {pdf} to separate project public/')

# 2. Copy fonts and images
shutil.copytree('fonts', os.path.join(dest, 'fonts'), dirs_exist_ok=True)
shutil.copytree('images', os.path.join(dest, 'images'), dirs_exist_ok=True)
shutil.copy2('landing.css', os.path.join(dest, 'src', 'landing.css'))
shutil.copy2('DownloadPage.tsx', os.path.join(dest, 'src', 'App.tsx'))

# 3. Create package.json
pkg = {
  "name": "download-area-interpretare-per-evolvere",
  "private": True,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@types/react": "^18.3.5",
    "@types/react-dom": "^18.3.0",
    "@vitejs/plugin-react": "^4.3.1",
    "typescript": "^5.5.3",
    "vite": "^5.4.2"
  }
}
with open(os.path.join(dest, 'package.json'), 'w') as f:
    json.dump(pkg, f, indent=2)

# 4. Create vite.config.ts
vite_config = """import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3005,
    host: true
  }
});
"""
with open(os.path.join(dest, 'vite.config.ts'), 'w') as f:
    f.write(vite_config)

# 5. Create index.html
index_html = """<!DOCTYPE html>
<html lang="it" dir="ltr">
  <head>
    <meta charset="utf-8" />
    <title>Area Riservata & Download — Interpretare per Evolvere</title>
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover"
    />
    <meta name="description" content="Scarica tutti i materiali didattici del Kit Interpretare per Evolvere in formato PDF." />
    <meta name="theme-color" content="#887396" />
    <link rel="shortcut icon" type="image/png" href="/images/favicon.png" />
    <link rel="icon" type="image/png" href="/images/favicon.png" />
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  </head>
  <body class="atomicat-disable-selection">
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
"""
with open(os.path.join(dest, 'index.html'), 'w') as f:
    f.write(index_html)

# 6. Create src/main.tsx
main_tsx = """import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
"""
with open(os.path.join(dest, 'src', 'main.tsx'), 'w') as f:
    f.write(main_tsx)

# 7. Create vercel.json
vercel_json = {
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}
with open(os.path.join(dest, 'vercel.json'), 'w') as f:
    json.dump(vercel_json, f, indent=2)

# 8. Create .gitignore
gitignore = """node_modules/
dist/
.DS_Store
*.log
"""
with open(os.path.join(dest, '.gitignore'), 'w') as f:
    f.write(gitignore)

# 9. Create README.md
readme = """# Area Riservata & Download — Interpretare per Evolvere

Progetto indipendente per l'Area di Download / Membri da distribuire come sottodominio su Vercel (es. `download.tuodominio.com` o `membros.tuodominio.com`).

## Deploy su Vercel
1. Carica questa cartella su un nuovo repository GitHub (es. `caiodcamargo999/download-interpretare-per-evolvere`)
2. Connetti il repository a un nuovo progetto su Vercel
3. Collega il sottodominio desiderato nel tab **Settings > Domains** di Vercel.
"""
with open(os.path.join(dest, 'README.md'), 'w') as f:
    f.write(readme)

print("Separate download project created successfully in:", dest)
