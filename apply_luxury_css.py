with open('landing.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Check if luxury section is already appended
marker = '/* =================================================== */\n/* LUXURY & SOPHISTICATED MODERN DESIGN SYSTEM 2026 */\n/* =================================================== */'

if marker in css:
    css = css[:css.index(marker)].strip()

luxury_css = """
/* =================================================== */
/* LUXURY & SOPHISTICATED MODERN DESIGN SYSTEM 2026 */
/* =================================================== */

html {
  scroll-behavior: smooth !important;
}

body, button, input, select, textarea, .atomicat-text, .atomicat-heading-title, .a-g-s-t, .a-g-s-h {
  font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h1, h2, h3, h4, .atomicat-title {
  font-family: 'Outfit', 'Plus Jakarta Sans', sans-serif !important;
  letter-spacing: -0.02em;
}

/* Offset for smooth scrolling to offer */
#offerta, .atomicat-container-4868b0f {
  scroll-margin-top: 40px;
}

/* -------------------------------------------
   HIGH-CONVERTING SOPHISTICATED CTA BUTTONS
------------------------------------------- */
.a-btn, 
.atomicat-checkout-button, 
.atomicat-anchor-button {
  position: relative !important;
  overflow: hidden !important;
  text-decoration: none !important;
  cursor: pointer !important;
  font-family: 'Outfit', 'Plus Jakarta Sans', sans-serif !important;
  font-weight: 700 !important;
  letter-spacing: 0.02em !important;
  text-transform: uppercase !important;
  border-radius: 50px !important;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
  box-shadow: 0 10px 25px -4px rgba(0, 199, 56, 0.4), 0 4px 10px -2px rgba(0, 0, 0, 0.1) !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 12px !important;
}

/* Subtle Shimmer Sheen Sweep */
.atomicat-checkout-button::after,
.atomicat-anchor-button::after {
  content: '' !important;
  position: absolute !important;
  top: -50% !important;
  left: -60% !important;
  width: 45% !important;
  height: 200% !important;
  background: linear-gradient(
    60deg,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.28) 50%,
    rgba(255, 255, 255, 0) 100%
  ) !important;
  transform: rotate(25deg) !important;
  animation: btnSweep 4.5s infinite ease-in-out !important;
  pointer-events: none !important;
}

@keyframes btnSweep {
  0% { left: -60%; }
  22% { left: 140%; }
  100% { left: 140%; }
}

.a-btn:hover, 
.atomicat-checkout-button:hover, 
.atomicat-anchor-button:hover {
  transform: translateY(-3px) scale(1.015) !important;
  box-shadow: 0 18px 35px -5px rgba(0, 199, 56, 0.55), 0 8px 15px -3px rgba(0, 0, 0, 0.15) !important;
  filter: brightness(1.06) !important;
}

.a-btn:active, 
.atomicat-checkout-button:active, 
.atomicat-anchor-button:active {
  transform: translateY(0) scale(0.985) !important;
}

/* -------------------------------------------
   LUXURY CARD & OFFER CONTAINER ELEVATION
------------------------------------------- */
#offerta, 
.atomicat-container-4868b0f {
  border-radius: 28px !important;
  background: linear-gradient(150deg, #090e1a 0%, #151d36 100%) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  box-shadow: 0 30px 70px -15px rgba(0, 0, 0, 0.6), 0 0 40px rgba(56, 189, 248, 0.08) !important;
  position: relative !important;
  overflow: hidden !important;
}

#offerta::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #38bdf8 0%, #10b981 50%, #f59e0b 100%);
  pointer-events: none;
}

/* Two Paths Container Cards */
.atomicat-container-1502162, 
.atomicat-container-0234c9c {
  border-radius: 20px !important;
  transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}

.atomicat-container-1502162:hover, 
.atomicat-container-0234c9c:hover {
  transform: translateY(-2px) !important;
}

/* Testimonial Cards */
.atomicat-container-460acd2, 
.atomicat-container-1ba1bf3 {
  border-radius: 20px !important;
  background: #ffffff !important;
  border: 1px solid rgba(0, 0, 0, 0.06) !important;
  box-shadow: 0 10px 30px -8px rgba(0, 0, 0, 0.06) !important;
  transition: all 0.3s ease !important;
}

.atomicat-container-460acd2:hover, 
.atomicat-container-1ba1bf3:hover {
  transform: translateY(-4px) !important;
  box-shadow: 0 18px 40px -10px rgba(0, 0, 0, 0.1) !important;
  border-color: rgba(99, 102, 241, 0.2) !important;
}

/* -------------------------------------------
   FAQ ACCORDION SOPHISTICATION
------------------------------------------- */
.a-ac-c {
  display: flex !important;
  flex-direction: column !important;
  gap: 14px !important;
}

.a-ac-i {
  border: 1px solid #e2e8f0 !important;
  border-radius: 16px !important;
  background: #ffffff !important;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02) !important;
  overflow: hidden !important;
}

.a-ac-i:hover {
  border-color: #cbd5e1 !important;
  box-shadow: 0 8px 20px -4px rgba(0, 0, 0, 0.06) !important;
}

.a-ac-t {
  padding: 20px 24px !important;
  font-weight: 700 !important;
  color: #0f172a !important;
  font-size: 1.1rem !important;
  line-height: 1.4 !important;
  transition: color 0.2s ease !important;
}

.a-ac-t:hover {
  color: #2563eb !important;
}

.a-ac-t-active {
  color: #2563eb !important;
  background: #f8fafc !important;
  border-bottom: 1px solid #f1f5f9 !important;
}

.a-ac-d {
  padding: 20px 24px !important;
  color: #475569 !important;
  font-size: 1.02rem !important;
  line-height: 1.65 !important;
  background: #ffffff !important;
}

/* -------------------------------------------
   RESPONSIVENESS & POLISH
------------------------------------------- */
@media (max-width: 768px) {
  .a-btn, 
  .atomicat-checkout-button, 
  .atomicat-anchor-button {
    font-size: 0.95rem !important;
    padding: 16px 20px !important;
    width: 100% !important;
  }
  
  #offerta, 
  .atomicat-container-4868b0f {
    border-radius: 20px !important;
    padding: 15px !important;
  }
}
"""

with open('landing.css', 'w', encoding='utf-8') as f:
    f.write(css + '\n\n' + luxury_css)

print('Appended Luxury Design System to landing.css successfully!')
