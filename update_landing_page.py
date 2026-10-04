import re

# 1. READ INDEX.TSX
with open('index.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Add id="offerta" to the offer container
code = code.replace(
    'className="atomicat-container-4868b0f a-b-o-cont--legacy-margin a-b-o-cont a-s-d-gx6nod"',
    'id="offerta" className="atomicat-container-4868b0f a-b-o-cont--legacy-margin a-b-o-cont a-s-d-gx6nod"'
)

# ----------------------------------------------------
# BUTTON 1 (Hero Comparison Section)
# Replace price text above Button 1 with strong value headline
# Replace checkout link with #offerta anchor
# ----------------------------------------------------
# Old heading: Da <s style={{ color: '#a70002' }}>€97</s> a soli <strong style={{ color: '#00c738' }}>€27</strong>
code = code.replace(
    'Da <s style={{ color: \'#a70002\' }}>€97</s> a soli <strong style={{ color: \'#00c738\' }}>€27</strong>',
    'Aiuta tuo figlio a comprendere ogni testo e a studiare in piena autonomia'
)

# Button 1 link
old_btn1_match = re.search(
    r'<div className=\"a-btn atomicat-element-container-e634791.*?<a href=\"[^\"]*\" className=\"atomicat-checkout-button a-b-a a-btn\">.*?<span>VOGLIO MIGLIORARE LA LETTURA DI MIO FIGLIO</span></a></div>',
    code,
    re.DOTALL
)
if old_btn1_match:
    new_btn1 = old_btn1_match.group(0).replace(
        'href="https://www.paggins.com/checkout/378673e6-08ae-42ff-a6f5-c71c3dd91454"',
        'href="#offerta"'
    ).replace('atomicat-checkout-button', 'atomicat-anchor-button')
    code = code.replace(old_btn1_match.group(0), new_btn1)
else:
    print('Warning: Button 1 regex not matched, trying direct string replace')
    code = re.sub(
        r'<a href=\"https://www\.paggins\.com/checkout/378673e6-08ae-42ff-a6f5-c71c3dd91454\" className=\"atomicat-checkout-button a-b-a a-btn\">(.*?)<span>VOGLIO MIGLIORARE LA LETTURA DI MIO FIGLIO</span></a>',
        r'<a href="#offerta" className="atomicat-anchor-button a-b-a a-btn">\1<span>VOGLIO MIGLIORARE LA LETTURA DI MIO FIGLIO</span></a>',
        code
    )

# ----------------------------------------------------
# BUTTON 2 (Bonus Section Bottom)
# Remove price from heading: Tutte le <strong>587 attività + i 4 bonus inclusi</strong> a soli <strong style={{ color: '#00c738' }}>€27</strong>
# Button 2 link -> #offerta anchor
# ----------------------------------------------------
code = code.replace(
    'Tutte le <strong>587 attività + i 4 bonus inclusi</strong> a soli <strong style={{ color: \'#00c738\' }}>€27</strong>',
    'Tutte le <strong>587 attività didattiche + i 4 bonus esclusivi inclusi</strong>'
)

old_btn2_match = re.search(
    r'<div className=\"atomicat-element-container-8e2ac92.*?<a href=\"[^\"]*\" className=\"a-b-a a-btn atomicat-checkout-button\">.*?<span>VOGLIO IL KIT COMPLETO A €27</span></a></div>',
    code,
    re.DOTALL
)
if old_btn2_match:
    new_btn2 = old_btn2_match.group(0).replace(
        'href="https://www.paggins.com/checkout/378673e6-08ae-42ff-a6f5-c71c3dd91454"',
        'href="#offerta"'
    ).replace('atomicat-checkout-button', 'atomicat-anchor-button').replace(
        '<span>VOGLIO IL KIT COMPLETO A €27</span>',
        '<span>SCOPRI L\'OFFERTA COMPLETA & I 4 BONUS</span>'
    )
    code = code.replace(old_btn2_match.group(0), new_btn2)
else:
    print('Warning: Button 2 regex not matched, trying direct string replace')
    code = re.sub(
        r'<a href=\"https://www\.paggins\.com/checkout/378673e6-08ae-42ff-a6f5-c71c3dd91454\" className=\"a-b-a a-btn atomicat-checkout-button\">(.*?)<span>VOGLIO IL KIT COMPLETO A €27</span></a>',
        r'<a href="#offerta" className="atomicat-anchor-button a-b-a a-btn">\1<span>SCOPRI L\'OFFERTA COMPLETA & I 4 BONUS</span></a>',
        code
    )

# ----------------------------------------------------
# BUTTON 3 (Main Offer / Pricing Breakdown Section #offerta)
# Ensure direct checkout link is present with clear offer text
# ----------------------------------------------------
# In Button 3:
# Currently text is: <span>VOGLIO MIGLIORARE LA LETTURA DI MIO FIGLIO</span>
# Let's make it: <span>SÌ, VOGLIO IL KIT COMPLETO A €27</span>
old_btn3_match = re.search(
    r'<div className=\"atomicat-button atomicat-element-container-0720760.*?<a href=\"[^\"]*\" className=\"a-btn a-b-a atomicat-checkout-button\">.*?<span>VOGLIO MIGLIORARE LA LETTURA DI MIO FIGLIO</span></a></div>',
    code,
    re.DOTALL
)
if old_btn3_match:
    new_btn3 = old_btn3_match.group(0).replace(
        '<span>VOGLIO MIGLIORARE LA LETTURA DI MIO FIGLIO</span>',
        '<span>SÌ, VOGLIO IL KIT COMPLETO A €27</span>'
    )
    code = code.replace(old_btn3_match.group(0), new_btn3)

# ----------------------------------------------------
# BUTTON 4 (Two Paths Section Bottom)
# Replace direct checkout link with #offerta anchor
# ----------------------------------------------------
old_btn4_match = re.search(
    r'<div className=\"a-e-cont atomicat-element-container-802f06e.*?<a href=\"[^\"]*\" className=\"a-b-a a-btn atomicat-checkout-button\">.*?<span>VOGLIO INIZIARE SUBITO A SOLI €27</span></a></div>',
    code,
    re.DOTALL
)
if old_btn4_match:
    new_btn4 = old_btn4_match.group(0).replace(
        'href="https://www.paggins.com/checkout/378673e6-08ae-42ff-a6f5-c71c3dd91454"',
        'href="#offerta"'
    ).replace('atomicat-checkout-button', 'atomicat-anchor-button').replace(
        '<span>VOGLIO INIZIARE SUBITO A SOLI €27</span>',
        '<span>VOGLIO INIZIARE SUBITO</span>'
    )
    code = code.replace(old_btn4_match.group(0), new_btn4)

# ----------------------------------------------------
# BUTTON 5 (Author / Presentation Section)
# Replace direct checkout link with #offerta anchor
# ----------------------------------------------------
old_btn5_match = re.search(
    r'<div className=\"a-btn-40c1c0c.*?<a href=\"[^\"]*\" className=\"a-btn a-b-a atomicat-checkout-button\">.*?<span>SÌ, VOGLIO INIZIARE SUBITO A SOLI €27</span></a></div>',
    code,
    re.DOTALL
)
if old_btn5_match:
    new_btn5 = old_btn5_match.group(0).replace(
        'href="https://www.paggins.com/checkout/378673e6-08ae-42ff-a6f5-c71c3dd91454"',
        'href="#offerta"'
    ).replace('atomicat-checkout-button', 'atomicat-anchor-button').replace(
        '<span>SÌ, VOGLIO INIZIARE SUBITO A SOLI €27</span>',
        '<span>VOGLIO ACCEDERE AL METODO COMPLETO</span>'
    )
    code = code.replace(old_btn5_match.group(0), new_btn5)

# ----------------------------------------------------
# BUTTON 6 (Page Bottom after FAQ & Guarantee)
# Retains direct checkout link to Paggins
# ----------------------------------------------------
# Text: <span>ACQUISTA ORA IL KIT COMPLETO · €27</span>
code = code.replace(
    '<span>ACQUISTA ORA · €27</span>',
    '<span>ACQUISTA ORA IL KIT COMPLETO · €27</span>'
)

# Smooth scroll anchor click handler in useEffect
useEffect_handler = """  useEffect(() => {
    // Smooth scroll for all anchor links pointing to #offerta
    const handleAnchorClick = (e: MouseEvent) => {
      const target = (e.target as HTMLElement).closest('a[href^="#"]');
      if (target) {
        const href = target.getAttribute('href');
        if (href && href.startsWith('#')) {
          e.preventDefault();
          const elem = document.querySelector(href);
          if (elem) {
            elem.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        }
      }
    };
    document.addEventListener('click', handleAnchorClick);

    // Propagate UTM query parameters to checkout links
    if (typeof window !== 'undefined') {
      const searchParams = window.location.search;
      if (searchParams) {
        const checkoutLinks = document.querySelectorAll<HTMLAnchorElement>('.atomicat-checkout-button');
        checkoutLinks.forEach(link => {
          const href = link.getAttribute('href');
          if (href && (href.includes('paggins.com') || href.includes('pay.hotmart.com'))) {
            try {
              const url = new URL(href);
              const currentParams = new URLSearchParams(searchParams);
              currentParams.forEach((val, key) => {
                if (!url.searchParams.has(key)) {
                  url.searchParams.set(key, val);
                }
              });
              link.setAttribute('href', url.toString());
            } catch (e) {
              // ignore url parsing error
            }
          }
        });
      }
    }

    return () => {
      document.removeEventListener('click', handleAnchorClick);
    };
  }, []);"""

code = re.sub(
    r'  useEffect\(\(\) => \{.*?\}, \[\]\);',
    useEffect_handler,
    code,
    flags=re.DOTALL
)

with open('index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print('Updated index.tsx with smooth anchor buttons and exclusive price anchoring on offer section!')
