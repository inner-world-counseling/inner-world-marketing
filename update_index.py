import json
import re
from bs4 import BeautifulSoup

def process_file():
    with open('/opt/build/repo/index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Task 1: The "Midwest" Local Anchor
    footer = soup.find('footer', class_='site-footer')
    if footer:
        midwest_section = soup.new_tag('section', id='serving-midwest', **{'class': 'section section--cream'})
        container = soup.new_tag('div', **{'class': 'container'})
        container['style'] = 'text-align:center; max-width:800px;'
        
        h2 = soup.new_tag('h2')
        h2.string = "Serving Clients Locally Across the Midwest"
        
        p = soup.new_tag('p')
        p.string = "Providing specialized telehealth services for high-functioning adults residing in North Dakota (Fargo, Bismarck, Grand Forks) and Minnesota (Minneapolis, St. Paul, Rochester, Duluth)."
        
        container.append(h2)
        container.append(p)
        midwest_section.append(container)
        footer.insert_before(midwest_section)
        
    # Task 2: Enhance MedicalBusiness schema
    for script in soup.find_all('script', type='application/ld+json'):
        try:
            data = json.loads(script.string)
            modified = False
            
            if '@graph' in data:
                for item in data['@graph']:
                    if item.get('@type') == 'MedicalBusiness':
                        item['knowsAbout'] = [
                            "EMDR Therapy",
                            "Cognitive Processing Therapy (CPT)",
                            "Trauma-Informed Care",
                            "Anxiety Treatment for Professionals"
                        ]
                        modified = True
            elif data.get('@type') == 'MedicalBusiness':
                data['knowsAbout'] = [
                    "EMDR Therapy",
                    "Cognitive Processing Therapy (CPT)",
                    "Trauma-Informed Care",
                    "Anxiety Treatment for Professionals"
                ]
                modified = True
                
            if modified:
                script.string = chr(10) + json.dumps(data, indent=2) + chr(10)
        except Exception as e:
            pass

    # Task 3: Invisible Breadcrumb & Entity Fixes
    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [{
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://deirdrekuvaas.com/"
        }]
    }
    breadcrumb_script = soup.new_tag('script', type='application/ld+json')
    breadcrumb_script.string = chr(10) + json.dumps(breadcrumb_schema, indent=2) + chr(10)
    
    first_script = soup.find('script')
    if first_script:
        first_script.insert_before(breadcrumb_script)
    else:
        soup.head.append(breadcrumb_script)
    
    # Heading Hierarchy
    h1 = soup.find('h1')
    if h1:
        h1.string = "Online Trauma Therapy & EMDR Counseling in North Dakota & Minnesota | Deirdre Kuvaas, LPCC"

    # List Cleanup
    for li in soup.find_all('li'):
        h3 = li.find('h3')
        if h3:
            strong = soup.new_tag('strong')
            strong.append(BeautifulSoup(h3.decode_contents(), 'html.parser'))
            
            ul = li.find_parent('ul')
            if ul and ul.has_attr('style'):
                ul['style'] = ul['style'].replace('list-style: none;', '').replace('padding-left: 0;', '').strip()
                
            h3.replace_with(strong)
            
    # Task 4: AI Voice & Summarization (Speakable schema)
    hero_section = soup.find('section', class_='hero')
    if hero_section:
        hero_ps = hero_section.find_all('p')
        if hero_ps:
            hero_ps[0]['id'] = 'hero-description'
            
    webpage_schema = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "@id": "https://deirdrekuvaas.com/#webpage",
        "url": "https://deirdrekuvaas.com/",
        "name": "Online Trauma Therapy & EMDR Counseling in North Dakota & Minnesota | Deirdre Kuvaas, LPCC",
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": ["#hero-description", "#serving-midwest"]
        }
    }
    webpage_script = soup.new_tag('script', type='application/ld+json')
    webpage_script.string = chr(10) + json.dumps(webpage_schema, indent=2) + chr(10)
    if first_script:
        first_script.insert_before(webpage_script)
    else:
        soup.head.append(webpage_script)

    # Task 5: Technical Maintenance - Move inline styles
    style_blocks = []
    style_counter = 1
    
    for tag in soup.find_all(True):
        if tag.has_attr('style'):
            style_content = tag['style'].strip()
            if not style_content:
                del tag['style']
                continue
                
            class_name = f"extracted-style-{style_counter}"
            style_counter += 1
            
            style_blocks.append(f".{class_name} {{ {style_content} }}")
            
            classes = tag.get('class', [])
            if isinstance(classes, str):
                classes = [classes]
            classes.append(class_name)
            tag['class'] = classes
            del tag['style']
            
    if style_blocks:
        style_tag = soup.find('style')
        if not style_tag:
            style_tag = soup.new_tag('style')
            soup.head.append(style_tag)
        
        existing_styles = style_tag.string or ""
        new_styles = chr(10) + chr(10).join(style_blocks) + chr(10)
        style_tag.string = existing_styles + new_styles
        
    with open('/opt/build/repo/index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == "__main__":
    process_file()