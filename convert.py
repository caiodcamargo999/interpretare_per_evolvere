import html.parser
import re

with open('kit-interpretar-para-evoluir.html', 'r', encoding='utf-8') as f:
    raw_html = f.read()

body = re.search(r'<body[^>]*>(.*?)</body>', raw_html, flags=re.DOTALL).group(1)
body_clean = re.sub(r'<style[^>]*>.*?</style>', '', body, flags=re.DOTALL)
body_clean = re.sub(r'<script[^>]*>.*?</script>', '', body_clean, flags=re.DOTALL)

class CustomJSXParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.output = []
        self.void_tags = {'img', 'br', 'hr', 'input', 'source'}

    def handle_starttag(self, tag, attrs):
        attr_list = []
        for k, v in attrs:
            if k == 'class':
                attr_list.append(f'className="{v}"')
            elif k == 'style':
                pairs = [p.strip() for p in v.split(';') if p.strip()]
                props = []
                for p in pairs:
                    if ':' in p:
                        sk, sv = p.split(':', 1)
                        sk = sk.strip()
                        sv = sv.strip()
                        parts = sk.split('-')
                        camel_sk = parts[0] + ''.join(x.capitalize() for x in parts[1:])
                        props.append(f"{camel_sk}: '{sv}'")
                attr_list.append(f'style={{{{ {", ".join(props)} }}}}')
            elif k == 'srcset':
                attr_list.append(f'srcSet="{v}"')
            elif k == 'fetchpriority':
                attr_list.append(f'fetchPriority="{v}"')
            elif k == 'viewbox':
                attr_list.append(f'viewBox="{v}"')
            elif k == 'for':
                attr_list.append(f'htmlFor="{v}"')
            elif k == 'autocomplete':
                attr_list.append(f'autoComplete="{v}"')
            elif k == 'tabindex':
                attr_list.append(f'tabIndex={{{v}}}')
            elif k == 'xmlns:xlink':
                attr_list.append(f'xmlnsXlink="{v}"')
            elif k == 'xlink:href':
                attr_list.append(f'xlinkHref="{v}"')
            elif k == 'clip-rule':
                attr_list.append(f'clipRule="{v}"')
            elif k == 'fill-rule':
                attr_list.append(f'fillRule="{v}"')
            elif k == 'stroke-width':
                attr_list.append(f'strokeWidth="{v}"')
            elif k == 'stroke-linecap':
                attr_list.append(f'strokeLinecap="{v}"')
            elif k == 'stroke-linejoin':
                attr_list.append(f'strokeLinejoin="{v}"')
            else:
                attr_list.append(f'{k}="{v}"')

        attrs_rendered = (' ' + ' '.join(attr_list)) if attr_list else ''
        if tag in self.void_tags:
            self.output.append(f'<{tag}{attrs_rendered} />')
        else:
            self.output.append(f'<{tag}{attrs_rendered}>')

    def handle_endtag(self, tag):
        if tag not in self.void_tags:
            self.output.append(f'</{tag}>')

    def handle_data(self, data):
        data_clean = data.replace('{', "{'{'}").replace('}', "{'}'}")
        self.output.append(data_clean)

    def handle_comment(self, data):
        self.output.append(f'{{/* {data} */}}')

# We'll replace the static accordion in body_clean before parsing to JSX
# Or parse body_clean and then do the replacement

parser = CustomJSXParser()
parser.feed(body_clean)
body_jsx = ''.join(parser.output)

accordion_jsx = """{/* accordion - h1ns7x */}
              <div className="a-ac-c a-i-e-cont a-ac">
                {faqs.map((faq, index) => {
                  const isOpen = openFaq === index;
                  return (
                    <div className="a-ac-i" key={index}>
                      <h3
                        className={`a-g-s-h a-ac-t atomicat-title ${isOpen ? 'a-ac-t-active' : ''}`}
                        onClick={() => toggleFaq(index)}
                        style={{ cursor: 'pointer' }}
                      >
                        <div>{faq.q}</div>
                        <div className="a-ac-tg">
                          <div className={isOpen ? '' : 'atomicat-hidden'}>
                            <div className="atomicat-svg-container">
                              <svg
                                aria-hidden="true"
                                focusable="false"
                                data-prefix="fas"
                                data-icon="minus"
                                className="svg-inline--fa fa-minus"
                                role="img"
                                xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 448 512"
                                alt="active icon"
                              >
                                <path
                                  fill="currentColor"
                                  d="M432 256c0 17.7-14.3 32-32 32L48 288c-17.7 0-32-14.3-32-32s14.3-32 32-32l352 0c17.7 0 32 14.3 32 32z"
                                />
                              </svg>
                            </div>
                          </div>
                          <div className={isOpen ? 'atomicat-hidden' : ''}>
                            <div className="atomicat-svg-container">
                              <svg
                                aria-hidden="true"
                                focusable="false"
                                data-prefix="fas"
                                data-icon="plus"
                                className="svg-inline--fa fa-plus"
                                role="img"
                                xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 448 512"
                                alt="inactive icon"
                              >
                                <path
                                  fill="currentColor"
                                  d="M256 80c0-17.7-14.3-32-32-32s-32 14.3-32 32V224H48c-17.7 0-32 14.3-32 32s14.3 32 32 32H192V432c0 17.7 14.3 32 32 32s32-14.3 32-32V288H400c17.7 0-32-32-32-32H256V80z"
                                />
                              </svg>
                            </div>
                          </div>
                        </div>
                      </h3>
                      <div className={`atomicat-content a-ac-ct ${isOpen ? '' : 'a-c-inactive'}`}>
                        <div
                          className="a-c-text a-g-s-t"
                          dangerouslySetInnerHTML={{ __html: faq.a }}
                        />
                      </div>
                    </div>
                  );
                })}
              </div>"""

# Search for the exact accordion in body_jsx
# The accordion starts with {/*  accordion - h1ns7x  */} or {/* accordion - h1ns7x */} and <div className="a-ac-c a-i-e-cont a-ac">
# and ends right after the 5th item closing </div></div></div></div>
target_start = body_jsx.find('a-ac-c a-i-e-cont a-ac')
# backtrack to the comment
comment_start = body_jsx.rfind('{/*', 0, target_start)
# find the end of the last faq item text
last_faq_text = "processado pela Hotmart.</p></div></div></div></div>"
target_end = body_jsx.find(last_faq_text, target_start) + len(last_faq_text)

print('Target replacement slice:', comment_start, target_end)
print('Replacing snippet starting with:', body_jsx[comment_start:comment_start+80])
print('Replacing snippet ending with:', body_jsx[target_end-80:target_end])

body_jsx_modified = body_jsx[:comment_start] + accordion_jsx + body_jsx[target_end:]

full_tsx = f'''import React, {{ useState, useEffect }} from 'react';
import './landing.css';

interface FaqItem {{
  q: string;
  a: string;
}}

const faqs: FaqItem[] = [
  {{
    q: 'Como recebo o material depois da compra?',
    a: 'Assim que o pagamento é confirmado, o acesso chega no seu e-mail na hora. Você baixa e já pode imprimir a primeira atividade no mesmo dia.'
  }},
  {{
    q: 'Serve para a idade do meu filho?',
    a: 'As atividades são pensadas para crianças de 7 a 12 anos e organizadas por nível de dificuldade, alinhadas à BNCC.'
  }},
  {{
    q: 'Preciso imprimir tudo?',
    a: 'Não. Você pode imprimir ou fazer as atividades direto no caderno, do jeito que for melhor pra você.'
  }},
  {{
    q: 'E se eu não gostar?',
    a: 'Você tem 7 dias de garantia. Se sentir que não é para o seu filho, devolvemos 100% do valor, sem perguntas e sem burocracia.'
  }},
  {{
    q: 'Como funciona o pagamento?',
    a: '<p>Você pode pagar por Pix ou cartão em até 9x. O pagamento é 100% seguro, processado pela Hotmart.</p>'
  }}
];

export default function KitInterpretarParaEvoluir() {{
  const [openFaq, setOpenFaq] = useState<number | null>(0);

  const toggleFaq = (index: number) => {{
    setOpenFaq(prev => (prev === index ? null : index));
  }};

  useEffect(() => {{
    // Propagate UTM query parameters to checkout links
    if (typeof window !== 'undefined') {{
      const searchParams = window.location.search;
      if (searchParams) {{
        const checkoutLinks = document.querySelectorAll<HTMLAnchorElement>('.atomicat-checkout-button');
        checkoutLinks.forEach(link => {{
          const href = link.getAttribute('href');
          if (href && href.includes('pay.hotmart.com')) {{
            try {{
              const url = new URL(href);
              const currentParams = new URLSearchParams(searchParams);
              currentParams.forEach((val, key) => {{
                if (!url.searchParams.has(key)) {{
                  url.searchParams.set(key, val);
                }}
              }});
              link.setAttribute('href', url.toString());
            }} catch (e) {{
              // ignore url parsing error
            }}
          }}
        }});
      }}
    }}
  }}, []);

  return (
    {body_jsx_modified}
  );
}}
'''

with open('index.tsx', 'w', encoding='utf-8') as f:
    f.write(full_tsx)

print('Generated index.tsx successfully! Length:', len(full_tsx))
