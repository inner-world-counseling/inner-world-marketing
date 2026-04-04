import json
from bs4 import BeautifulSoup
import re

file_path = '/opt/build/repo/people-pleasing/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

# 1. Update Meta/H1
title_tag = soup.find('title')
if title_tag:
    title_tag.string = "Therapy for People Pleasing & Boundary Setting"

og_title = soup.find('meta', property='og:title')
if og_title:
    og_title['content'] = "Therapy for People Pleasing & Boundary Setting | ND, MN, OH, UT"

twitter_title = soup.find('meta', attrs={'name': 'twitter:title'})
if twitter_title:
    twitter_title['content'] = "Therapy for People Pleasing & Boundary Setting | ND, MN, OH, UT"

# 2. Hero performance fixes
banner_section = soup.find('section', class_='page-banner')
if banner_section:
    # Remove old inline styles and attributes
    if 'style' in banner_section.attrs:
        del banner_section['style']
    if 'fetchpriority' in banner_section.attrs:
        del banner_section['fetchpriority']
    if 'role' in banner_section.attrs:
        del banner_section['role']
    if 'aria-label' in banner_section.attrs:
        del banner_section['aria-label']
    if 'loading' in banner_section.attrs:
        del banner_section['loading']

    banner_section['style'] = "position: relative; overflow: hidden;"
    
    # Create picture element
    picture_tag = soup.new_tag('picture', style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;")
    img_tag = soup.new_tag('img', src="/images/hero-banner-leaves.webp", alt="Lush green leaves macro shot representing growth and mental wellness.", style="width: 100%; height: 100%; object-fit: cover;", loading="eager", fetchpriority="high")
    picture_tag.append(img_tag)
    
    banner_section.insert(0, picture_tag)
    
    container = banner_section.find('div', class_='container')
    if container:
        container['style'] = "position: relative; z-index: 1;"
        h1_tag = container.find('h1')
        if h1_tag:
            h1_tag.string = "Therapy for People Pleasing & Boundary Setting"

# 3. Semantic Content Injection
h2_fawning = soup.find('h2', string="The Reality of Fawning")
if h2_fawning:
    h2_fawning.string = "The Fawn Response: When 'Nice' is a Survival Skill"
    
    # Next p tags
    p1 = h2_fawning.find_next_sibling('p')
    p2 = p1.find_next_sibling('p')
    
    # Update p2 to explain nervous system creating safety, fawning, over-functioning, burnout
    # Create new p3 for the "Now, as an adult..." part
    
    p2_content = """People-pleasing is often a way the nervous system tries to create safety. In the clinical world, this is called the <strong>fawn response</strong>. It is a protective response where you minimize your own presence to secure safety, avoid conflict, or maintain connection. You learned early on that being helpful, quiet, or easy was the most effective way to stay safe and valued."""
    
    p3_content = """This constant need to manage everyone else's emotions leads to <strong>over-functioning</strong>. You take on the responsibilities and emotional burdens of others, which inevitably leads to severe burnout and a profound loss of self. Now, as an adult, that survival habit shows up as:"""
    
    # We replace p2 and add p3 before the ul
    p2.clear()
    p2.append(BeautifulSoup(p2_content, 'html.parser'))
    
    p3 = soup.new_tag('p')
    p3.append(BeautifulSoup(p3_content, 'html.parser'))
    p2.insert_after(p3)

# 4. The "Boundary Work" Block
h3_dismantling = soup.find('h3', string="Dismantling the Burden")
if h3_dismantling:
    h3_dismantling.string = "Boundary Work: Protecting Your Peace"
    
    p_d1 = h3_dismantling.find_next_sibling('p')
    p_d2 = p_d1.find_next_sibling('p')
    
    p_d1_content = """In our sessions, you do not have to be the perfect client or work to keep me comfortable. We will not just talk about your week; we are going to look at the roots of that chronic guilt. Boundary setting is not just about "saying no"—it is fundamentally about <strong>Protecting your Peace</strong>."""
    
    p_d2_content = """Using <a href="/emdr">EMDR</a> and <a href="/cognitive-processing-therapy">CPT</a>, we work to quiet the inner critic that tells you that setting a boundary is mean or dangerous. EMDR specifically helps process the underlying emotional memories that drive the fawn response, significantly reducing the intense guilt associated with asserting your own needs."""
    
    p_d3_content = """The goal is not to turn you into someone who does not care. It is to help you become a human being who can confidently protect your peace and say “yes” to a life that actually belongs to you."""
    
    p_d1.clear()
    p_d1.append(BeautifulSoup(p_d1_content, 'html.parser'))
    
    p_d2.clear()
    p_d2.append(BeautifulSoup(p_d2_content, 'html.parser'))
    
    p_d3 = soup.new_tag('p')
    p_d3.append(BeautifulSoup(p_d3_content, 'html.parser'))
    p_d2.insert_after(p_d3)

# 5. FAQ Integration (Semantic & Schema)
faq_html = """
<div class="faq-section" style="margin-top: 3rem;">
  <h2>Frequently Asked Questions</h2>
  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" style="margin-bottom: 1.5rem;">
    <h3 itemprop="name" style="margin-bottom: 0.5rem;">Why do I feel so guilty saying no?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">Guilt when saying no often stems from childhood conditioning where your safety or worth was tied to accommodating others. Your nervous system interprets setting a boundary as a threat to your relationships, triggering a disproportionate guilt response.</p>
    </div>
  </div>
  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" style="margin-bottom: 1.5rem;">
    <h3 itemprop="name" style="margin-bottom: 0.5rem;">Is people-pleasing actually a trauma response?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">Yes, in many cases, chronic people-pleasing is a trauma response known as "fawning." It is an unconscious survival strategy designed to pacify threats and avoid conflict by abandoning one's own needs to appease others.</p>
    </div>
  </div>
  <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" style="margin-bottom: 1.5rem;">
    <h3 itemprop="name" style="margin-bottom: 0.5rem;">How can EMDR help me set better boundaries?</h3>
    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">EMDR helps you set better boundaries by targeting and reprocessing the root memories and negative core beliefs that make boundary-setting feel dangerous. By resolving this underlying trauma, EMDR reduces the intense emotional activation and guilt, allowing you to establish and maintain healthy boundaries with confidence.</p>
    </div>
  </div>
</div>
"""
# Insert FAQ before the "Get in Touch" div
get_in_touch = soup.find('div', style=lambda value: value and 'text-align:center; margin-top:2rem;' in value.replace(' ', ''))
if get_in_touch:
    get_in_touch.insert_before(BeautifulSoup(faq_html, 'html.parser'))
else:
    print("Could not find 'Get in Touch' div.")

# 6. JSON-LD for Service & FAQ Schema
script_tags = soup.find_all('script', type='application/ld+json')
for script in script_tags:
    try:
        data = json.loads(script.string)
        if '@graph' in data:
            # Add Service Schema
            data['@graph'].append({
              "@type": "Service",
              "serviceType": "Counseling for People Pleasing & Boundaries",
              "audience": {
                "@type": "Audience",
                "audienceType": "High-achievers, over-functioners, professionals."
              },
              "provider": {
                "@id": "https://deirdrekuvaas.com/#person"
              },
              "url": "https://deirdrekuvaas.com/people-pleasing/"
            })
            
            # Add FAQ Schema
            data['@graph'].append({
              "@type": "FAQPage",
              "mainEntity": [
                {
                  "@type": "Question",
                  "name": "Why do I feel so guilty saying no?",
                  "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Guilt when saying no often stems from childhood conditioning where your safety or worth was tied to accommodating others. Your nervous system interprets setting a boundary as a threat to your relationships, triggering a disproportionate guilt response."
                  }
                },
                {
                  "@type": "Question",
                  "name": "Is people-pleasing actually a trauma response?",
                  "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Yes, in many cases, chronic people-pleasing is a trauma response known as \"fawning.\" It is an unconscious survival strategy designed to pacify threats and avoid conflict by abandoning one's own needs to appease others."
                  }
                },
                {
                  "@type": "Question",
                  "name": "How can EMDR help me set better boundaries?",
                  "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "EMDR helps you set better boundaries by targeting and reprocessing the root memories and negative core beliefs that make boundary-setting feel dangerous. By resolving this underlying trauma, EMDR reduces the intense emotional activation and guilt, allowing you to establish and maintain healthy boundaries with confidence."
                  }
                }
              ]
            })
            
            script.string = json.dumps(data, indent=2)
            break
    except Exception as e:
        print(f"Error parsing JSON-LD: {e}")

# Save the file
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Updated successfully.")
