with open('landing.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Marker
marker = '/* =================================================== */\n/* LUXURY & SOPHISTICATED MODERN DESIGN SYSTEM 2026 */\n/* =================================================== */'

if marker in css:
    css = css[:css.index(marker)].strip()

modern_luxury_css = """
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
  scroll-margin-top: 30px;
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
   OFFERTA SECTION - HIGH CONTRAST & LUXURY
------------------------------------------- */
#offerta, 
.atomicat-container-4868b0f {
  background: radial-gradient(circle at 50% 0%, #1e295d 0%, #0c1229 60%, #060913 100%) !important;
  border: 1.5px solid rgba(56, 189, 248, 0.25) !important;
  border-radius: 32px !important;
  box-shadow: 0 30px 80px -15px rgba(0, 0, 0, 0.8), 0 0 50px rgba(56, 189, 248, 0.12) !important;
  padding: 50px 35px !important;
  margin-top: 45px !important;
  margin-bottom: 45px !important;
  position: relative !important;
  overflow: hidden !important;
  color: #ffffff !important;
}

#offerta::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #38bdf8 0%, #10b981 50%, #f59e0b 100%);
  pointer-events: none;
}

/* Headline inside offer */
#offerta .atomicat-heading-title-3ec6468,
#offerta .atomicat-text-3ec6468,
#offerta .atomicat-heading-title-3ec6468 * {
  color: #ffffff !important;
  font-size: 1.45rem !important;
  font-weight: 700 !important;
  line-height: 1.55 !important;
  text-align: center !important;
}

/* 3D Mockup inside offer */
#offerta .atomicat-element-container-62a91ff img,
#offerta .a-img-ele-62a91ff img {
  max-width: 100% !important;
  height: auto !important;
  background: transparent !important;
  filter: drop-shadow(0 20px 35px rgba(0, 0, 0, 0.7)) !important;
  transition: transform 0.4s ease !important;
}

#offerta .atomicat-element-container-62a91ff img:hover,
#offerta .a-img-ele-62a91ff img:hover {
  transform: translateY(-4px) scale(1.02) !important;
}

/* Item breakdown list container */
#offerta .atomicat-container-1f5bdec {
  display: flex !important;
  flex-direction: column !important;
  gap: 12px !important;
  margin: 25px 0 !important;
}

/* Each item in offer list */
#offerta .a-c-cont-79e3499,
#offerta .a-c-cont-fb79da7,
#offerta .a-c-cont-5733e0c,
#offerta .a-c-cont-bd2ac2e,
#offerta .a-c-cont-78b58c6 {
  background: rgba(255, 255, 255, 0.06) !important;
  border: 1px solid rgba(255, 255, 255, 0.12) !important;
  border-radius: 14px !important;
  padding: 14px 20px !important;
  transition: all 0.25s ease !important;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
}

#offerta .a-c-cont-79e3499:hover,
#offerta .a-c-cont-fb79da7:hover,
#offerta .a-c-cont-5733e0c:hover,
#offerta .a-c-cont-bd2ac2e:hover,
#offerta .a-c-cont-78b58c6:hover {
  background: rgba(255, 255, 255, 0.1) !important;
  border-color: rgba(56, 189, 248, 0.4) !important;
  transform: translateX(4px) !important;
}

#offerta .atomicat-heading-title-79e3499,
#offerta .atomicat-heading-title-fb79da7,
#offerta .atomicat-heading-title-5733e0c,
#offerta .atomicat-heading-title-bd2ac2e,
#offerta .atomicat-heading-title-78b58c6 {
  color: #f8fafc !important;
  font-size: 1.05rem !important;
  font-weight: 600 !important;
}

#offerta .atomicat-heading-title-79e3499 *,
#offerta .atomicat-heading-title-fb79da7 *,
#offerta .atomicat-heading-title-5733e0c *,
#offerta .atomicat-heading-title-bd2ac2e *,
#offerta .atomicat-heading-title-78b58c6 * {
  color: #f8fafc !important;
}

/* Strikethrough value tags */
#offerta s, 
#offerta s * {
  color: #f87171 !important;
  text-decoration: line-through !important;
  font-weight: 700 !important;
  margin-left: 6px !important;
}

/* Total Value Heading */
#offerta .atomicat-heading-title-a67ff93,
#offerta .atomicat-text-a67ff93,
#offerta .atomicat-heading-title-a67ff93 * {
  color: #cbd5e1 !important;
  font-size: 1.35rem !important;
  font-weight: 700 !important;
  text-align: center !important;
  margin-top: 15px !important;
}

/* Big Price: €27,00 */
#offerta .atomicat-heading-title-3e7a759,
#offerta .atomicat-text-3e7a759,
#offerta .atomicat-heading-title-3e7a759 * {
  color: #22c55e !important;
  font-size: 4rem !important;
  font-weight: 900 !important;
  text-align: center !important;
  letter-spacing: -0.03em !important;
  line-height: 1.05 !important;
  text-shadow: 0 4px 25px rgba(34, 197, 94, 0.45) !important;
  font-family: 'Outfit', sans-serif !important;
}

/* Promo text: Risparmi €164 */
#offerta .atomicat-heading-title-fcc1184,
#offerta .atomicat-text-fcc1184,
#offerta .atomicat-heading-title-fcc1184 * {
  color: #cbd5e1 !important;
  font-size: 1.08rem !important;
  line-height: 1.6 !important;
  text-align: center !important;
  max-width: 650px !important;
  margin: 10px auto 25px auto !important;
}

/* Offer Button */
#offerta .atomicat-checkout-button {
  font-size: 1.25rem !important;
  padding: 22px 36px !important;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
  color: #ffffff !important;
  box-shadow: 0 12px 30px -5px rgba(16, 185, 129, 0.5), 0 0 25px rgba(16, 185, 129, 0.3) !important;
}

#offerta .atomicat-checkout-button:hover {
  background: linear-gradient(135deg, #34d399 0%, #059669 100%) !important;
  box-shadow: 0 18px 40px -5px rgba(16, 185, 129, 0.65), 0 0 35px rgba(16, 185, 129, 0.45) !important;
}

/* -------------------------------------------
   OTHER SECTIONS: CARDS & TESTIMONIALS
------------------------------------------- */
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
   100% MOBILE RESPONSIVENESS
------------------------------------------- */
@media (max-width: 768px) {
  #offerta, 
  .atomicat-container-4868b0f {
    padding: 35px 18px !important;
    border-radius: 22px !important;
    margin-top: 30px !important;
    margin-bottom: 30px !important;
  }
  
  #offerta .atomicat-heading-title-3ec6468,
  #offerta .atomicat-text-3ec6468,
  #offerta .atomicat-heading-title-3ec6468 * {
    font-size: 1.2rem !important;
  }
  
  #offerta .atomicat-heading-title-3e7a759,
  #offerta .atomicat-text-3e7a759,
  #offerta .atomicat-heading-title-3e7a759 * {
    font-size: 3.2rem !important;
  }
  
  #offerta .atomicat-heading-title-79e3499,
  #offerta .atomicat-heading-title-fb79da7,
  #offerta .atomicat-heading-title-5733e0c,
  #offerta .atomicat-heading-title-bd2ac2e,
  #offerta .atomicat-heading-title-78b58c6 {
    font-size: 0.95rem !important;
  }
  
  .a-btn, 
  .atomicat-checkout-button, 
  .atomicat-anchor-button {
    font-size: 0.95rem !important;
    padding: 16px 20px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  
  img {
    max-width: 100% !important;
    height: auto !important;
  }
}
"""

with open('landing.css', 'w', encoding='utf-8') as f:
    f.write(css + '\n\n' + modern_luxury_css)

print('Updated landing.css with modern high-contrast offer styling!')
