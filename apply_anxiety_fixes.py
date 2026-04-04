import json
from bs4 import BeautifulSoup
import re

# Update index.html
index_path = '/opt/build/repo/index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

soup_idx = BeautifulSoup(index_html, 'html.parser')
hidden_trauma_h2 = soup_idx.find('h2', string=re.compile(r'Trauma Therapy for High-Achieving Professionals', re.I))
if hidden_trauma_h2:
    section = hidden_trauma_h2.find_parent('section')
    if section:
        section['id'] = 'hidden-trauma'

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(str(soup_idx))

# Update counseling-for-anxiety/index.html
anxiety_path = '/opt/build/repo/counseling-for-anxiety/index.html'
with open(anxiety_path, 'r', encoding='utf-8') as f:
    anxiety_html = f.read()

soup = BeautifulSoup(anxiety_html, 'html.parser')

# 1. Update Meta Title and H1
title_tag = soup.find('title')
if title_tag:
    title_tag.string = "High-Functioning Anxiety Therapy Online | Professionals"

og_title = soup.find('meta', property='og:title')
if og_title:
    og_title['content'] = "High-Functioning Anxiety Therapy Online | Professionals"

twitter_title = soup.find('meta', attrs={'name': 'twitter:title'})
if twitter_title:
    twitter_title['content'] = "High-Functioning Anxiety Therapy Online | Professionals"

# 2. LCP Fixes & H1 Update
banner = soup.find('section', class_='page-banner')
if banner:
    banner['style'] = "position: relative; overflow: hidden; display: flex; align-items: center; justify-content: center;"
    
    if 'background-image' in banner.get('style', ''):
        pass
    for attr in ['fetchpriority', 'role', 'aria-label', 'loading']:
        if attr in banner.attrs:
            del banner[attr]
            
    picture_html = """
    <picture style="position: absolute; inset: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none;">
      <source media="(max-width: 600px)" srcset="/.netlify/images?url=/images/hero-banner-leaves.webp&w=600">
      <img src="/images/hero-banner-leaves.webp" alt="Lush green leaves macro shot representing growth and mental wellness." loading="eager" fetchpriority="high" style="width: 100%; height: 100%; object-fit: cover;">
    </picture>
    """
    pic_soup = BeautifulSoup(picture_html, 'html.parser')
    banner.insert(0, pic_soup.picture)
    
    h1_tag = banner.find('h1')
    if h1_tag:
        h1_tag.string = "High-Functioning Anxiety Therapy for Professionals"
    
    container = banner.find('div', class_='container')
    if container:
        container['style'] = "position: relative; z-index: 1;"

# 3. Add semantic content injection
content_area = soup.find('div', class_='content-area')
if content_area:
    h2_what = content_area.find('h2', string=re.compile(r'What We Will Address Together', re.I))
    if h2_what:
        new_section_html = """
        <h2>When Anxiety Looks Like Success</h2>
        <p>If you are a high-achiever who is always "on," an over-thinker, or a perfectionist, your <a href="/#hidden-trauma">constant worry</a> may look like success to everyone else. However, simply "managing" symptoms isn't the same as "healing" the root cause. We use evidence-based approaches like <a href="/emdr">EMDR</a> to help address the underlying reasons for your perfectionism and burnout, rather than just treating the surface-level symptoms.</p>
        """
        new_sec_soup = BeautifulSoup(new_section_html, 'html.parser')
        h2_what.insert_before(new_sec_soup)

# 4. JSON-LD Update (Service & FAQ)
script_tag = soup.find('script', type='application/ld+json')
if script_tag:
    try:
        data = json.loads(script_tag.string)
        if '@graph' in data:
            data['@graph'].append({
                "@type": "Service",
                "serviceType": "High-Functioning Anxiety Therapy",
                "description": "Specialized anxiety treatment for professionals using EMDR or CPT to address the root causes of perfectionism and burnout.",
                "provider": {
                    "@id": "https://deirdrekuvaas.com/#person"
                }
            })
            
            data['@graph'].append({
                "@type": "FAQPage",
                "mainEntity": [
                    {
                      "@type": "Question",
                      "name": "What is high-functioning anxiety?",
                      "acceptedAnswer": {
                        "@type": "Answer",
                        "text": 'High-functioning anxiety is when you experience intense anxiety, overthinking, and worry, but you still manage to excel in your career and daily life. It often presents as perfectionism, the inability to relax, and being always "on," masking the internal struggle.'
                      }
                    },
                    {
                      "@type": "Question",
                      "name": "Will therapy make me lose my drive or motivation?",
                      "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "No. Healing from anxiety doesn't mean losing your edge. Therapy helps you transition from being driven by fear and panic to being driven by purpose and passion, allowing you to achieve success without the cost of burnout and exhaustion."
                      }
                    },
                    {
                      "@type": "Question",
                      "name": "How does EMDR help with physical symptoms of anxiety?",
                      "acceptedAnswer": {
                        "@type": "Answer",
                        "text": 'EMDR helps process the underlying trauma and stress that keep your nervous system in a constant state of "fight or flight." By addressing these root causes, EMDR can significantly reduce physical symptoms like muscle tension, racing heart, and sleep disruption.'
                      }
                    }
                ]
            })
        script_tag.string = json.dumps(data, indent=2)
    except Exception as e:
        print("Error parsing JSON:", e)

# 5. FAQ HTML integration
main_tag = soup.find('main')
if main_tag:
    semantic_defs = main_tag.find('section', class_='semantic-definitions')
    faq_html = """
    <section class="section section--faq" aria-labelledby="faq-heading" style="padding: 3rem 0; background-color: #fff;">
      <div class="container">
        <h2 id="faq-heading">Frequently Asked Questions</h2>
        <div class="faq-list">
          <div class="faq-item" style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;">What is high-functioning anxiety?</h3>
            <p>High-functioning anxiety is when you experience intense anxiety, overthinking, and worry, but you still manage to excel in your career and daily life. It often presents as perfectionism, the inability to relax, and being always "on," masking the internal struggle.</p>
          </div>
          <div class="faq-item" style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;">Will therapy make me lose my drive or motivation?</h3>
            <p>No. Healing from anxiety doesn't mean losing your edge. Therapy helps you transition from being driven by fear and panic to being driven by purpose and passion, allowing you to achieve success without the cost of burnout and exhaustion.</p>
          </div>
          <div class="faq-item">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;">How does EMDR help with physical symptoms of anxiety?</h3>
            <p>EMDR helps process the underlying trauma and stress that keep your nervous system in a constant state of "fight or flight." By addressing these root causes, EMDR can significantly reduce physical symptoms like muscle tension, racing heart, and sleep disruption.</p>
          </div>
        </div>
      </div>
    </section>
    """
    faq_soup = BeautifulSoup(faq_html, 'html.parser')
    if semantic_defs:
        semantic_defs.insert_before(faq_soup)
    else:
        main_tag.append(faq_soup)

with open(anxiety_path, 'w', encoding='utf-8') as f:
    f.write(soup.prettify(formatter="html5"))
print("Done")
