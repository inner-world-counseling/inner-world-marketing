import os
import re

html_pattern = re.compile(
    r'(<li[^>]*>\s*<a[^>]*>\s*Who I Help\s*</a>\s*<ul[^>]*>.*?</ul>\s*</li>)',
    re.IGNORECASE | re.DOTALL
)

replacement = r'\1\n          <li class="main-nav__item">\n            <a href="https://deirdre-kuvaas.clientsecure.me" class="main-nav__link main-nav__cta spwidget-button" data-spwidget-scope-id="2fc241c4-0b68-49a2-96dc-4239833e7127" data-spwidget-scope-uri="deirdre-kuvaas" data-spwidget-application-id="7c72cb9f9a9b913654bb89d6c7b4e71a77911b30192051da35384b4d0c6d505b" data-spwidget-type="OAR" data-spwidget-scope-global data-spwidget-autobind rel="noopener noreferrer">Request Consultation</a>\n          </li>'

def update_html():
    for root, dirs, files in os.walk('.'):
        if 'node_modules' in root or '.git' in root or '.netlify' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if already added
                if 'Request Consultation' in content and 'main-nav__cta' in content:
                    print(f"Skipping {filepath}, already has CTA.")
                    continue
                
                new_content, count = html_pattern.subn(replacement, content, count=1)
                
                if count > 0:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")
                else:
                    print(f"No match found in {filepath}")

def append_css():
    css_path = 'css/style.css'
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    
    if 'main-nav__cta' not in css:
        new_css = """
/* Global Header CTA */
.main-nav__item .main-nav__cta {
  background-color: var(--color-sage);
  color: #fff !important;
  font-weight: 700;
  padding: 0.5rem 1rem !important;
  border-radius: 4px;
  border: none;
  box-shadow: none;
  display: inline-block;
  margin-left: 0.5rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  transition: background-color 0.25s ease;
}
.main-nav__item .main-nav__cta:hover {
  background-color: var(--color-sage-dark);
}

@media (max-width: 1024px) {
  .main-nav__item .main-nav__cta {
    margin-left: 0;
    margin-top: 0.5rem;
    display: block;
    text-align: center;
  }
}
"""
        with open(css_path, 'a', encoding='utf-8') as f:
            f.write(new_css)
        print("Updated css/style.css")

if __name__ == '__main__':
    update_html()
    append_css()
