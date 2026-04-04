import re
from bs4 import BeautifulSoup
import json

with open('/opt/build/repo/personal-addiction-counseling/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Update Title and Meta
title = soup.find('title')
if title:
    title.string = "High-Functioning Addiction Counseling & LADC Support"

meta_desc = soup.find('meta', {'name': 'description'})
if meta_desc:
    meta_desc['content'] = "Online addiction counseling for high-functioning adults and professionals. LADC expertise with trauma-informed EMDR. Regain control of your life."

# Update OG
og_title = soup.find('meta', {'property': 'og:title'})
if og_title:
    og_title['content'] = "High-Functioning Addiction Counseling & LADC Support"
og_desc = soup.find('meta', {'property': 'og:description'})
if og_desc:
    og_desc['content'] = "Online addiction counseling for high-functioning adults and professionals. LADC expertise with trauma-informed EMDR."

twitter_title = soup.find('meta', {'name': 'twitter:title'})
if twitter_title:
    twitter_title['content'] = "High-Functioning Addiction Counseling & LADC Support"
twitter_desc = soup.find('meta', {'name': 'twitter:description'})
if twitter_desc:
    twitter_desc['content'] = "Online addiction counseling for high-functioning adults and professionals. LADC expertise with trauma-informed EMDR."

# Schema Modification
script_tag = soup.find('script', {'type': 'application/ld+json'})
if script_tag:
    data = json.loads(script_tag.string)
    
    # Add Service schema
    service_schema = {
      "@type": "Service",
      "serviceType": "Addiction Counseling / LADC Services",
      "provider": {
        "@id": "https://deirdrekuvaas.com/#person"
      },
      "offers": {
        "@type": "Offer",
        "description": "Specialized 'Dual Diagnosis' (Trauma + Substance Use) approach."
      }
    }
    
    # Add FAQ Schema
    faq_schema = {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is 'High-Functioning' addiction?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "High-functioning addiction refers to individuals who appear to be managing their lives, careers, and responsibilities successfully on the outside, but are secretly struggling with substance use to cope with stress or trauma. It can be especially isolating because the external success masks the internal pain."
          }
        },
        {
          "@type": "Question",
          "name": "Is my privacy protected as a professional in counseling?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Absolutely. Confidentiality is a cornerstone of my practice. As a licensed professional, I adhere to strict HIPAA regulations and ethical guidelines to ensure your privacy is completely protected, allowing you a safe space to discuss the unique stakes of your career without fear of judgment or exposure."
          }
        },
        {
          "@type": "Question",
          "name": "How does EMDR help with cravings or triggers?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "EMDR (Eye Movement Desensitization and Reprocessing) helps by targeting the underlying emotional distress and traumatic memories that drive the urge to use substances. By reprocessing these hidden traumas, EMDR reduces the intensity of triggers and cravings, addressing the root cause rather than just managing the symptoms."
          }
        }
      ]
    }
    
    data['@graph'].append(service_schema)
    data['@graph'].append(faq_schema)
    script_tag.string = "\n" + json.dumps(data, indent=2) + "\n"

# Update Hero Banner
hero = soup.find('section', class_='page-banner')
if hero:
    hero.clear()
    hero['style'] = "position: relative; overflow: hidden;"
    if 'fetchpriority' in hero.attrs:
        del hero['fetchpriority']
    if 'role' in hero.attrs:
        del hero['role']
    if 'aria-label' in hero.attrs:
        del hero['aria-label']
    if 'loading' in hero.attrs:
        del hero['loading']

    # We use a parsed snippet to avoid manual bs4 building
    hero_snippet = BeautifulSoup('''
    <picture style="position: absolute; inset: 0; width: 100%; height: 100%; z-index: -1;">
      <source srcset="/images/hero-banner-leaves.webp" type="image/webp">
      <img src="/images/hero-banner-leaves.webp" alt="Lush green leaves macro shot representing growth and mental wellness." loading="eager" fetchpriority="high" style="width: 100%; height: 100%; object-fit: cover;">
    </picture>
    <div class="container" style="position: relative; z-index: 1;">
      <h1 class="page-banner__title">High-Functioning Addiction Counseling &amp; LADC Support</h1>
    </div>
    ''', 'html.parser')
    for child in hero_snippet.children:
        hero.append(child)

# Replace Content
main = soup.find('main')
section = main.find('section')

content_snippet = BeautifulSoup('''
      <div class="container">
        <div class="content-area">
          <h2>When 'Copied' Becomes 'Caught'</h2>
          <p>For the driven professional, using substances often starts as a way to "unwind" from high-pressure days. You may be highly successful at work, managing teams, or running a business, while quietly relying on a drink or a substance to transition out of "work mode." But what starts as a copied behavior from high-stress work cultures eventually becomes a trap. When you're managing your life effectively on the outside but struggling with substance use in secret, this "High-Functioning" use is frequently linked to underlying, hidden trauma. Real recovery is not about simply "stopping a habit"&mdash;it is about regaining control of your life and nervous system.</p>

          <h3>The "LADC + Trauma" Block</h3>
          <p>As a dual-credentialed professional, I am both a Licensed Alcohol and Drug Counselor (LADC) and trained in EMDR. Treating the addiction without treating the trauma is the exact reason why many people "relapse" into old patterns. Addiction is rarely just about the substance itself; it's a symptom of an overwhelmed nervous system trying to find relief. By combining LADC strategies with trauma-informed EMDR, we address both the behavioral coping mechanisms and the root pain driving them.</p>

        <div style="text-align:center; margin-top:2rem;">
          <h3>Get in Touch</h3>
          <p>(701) 404-7895 | <a href="mailto:deirdre@innerworldcounselingservices.com" aria-label="Email Deirdre Kuvaas">deirdre@innerworldcounselingservices.com</a></p>
          <p style="font-size:0.9375rem; color:var(--color-taupe); margin-bottom:1rem;">Offering services in: Minnesota | North Dakota | Ohio | Utah</p>
          <a href="/appointment-request" class="btn btn--primary">Request Appointment</a>
          <a href="/contact" class="btn btn--outline" style="margin-left:0.5rem;">Send a Message</a>
        </div>
        </div>
      </div>
''', 'html.parser')

if section:
    section.clear()
    for child in content_snippet.children:
        section.append(child)

# Add FAQ Section after CTA section
faq_snippet = BeautifulSoup('''
    <!-- FAQ Section -->
    <section class="section section--light" style="background-color: #f4f6f5;">
      <div class="container" style="max-width:800px;">
        <h2 style="text-align: center; margin-bottom: 2rem;">Frequently Asked Questions</h2>
        
        <div class="faq-item" style="margin-bottom: 1.5rem;">
          <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;">What is "High-Functioning" addiction?</h3>
          <p>High-functioning addiction refers to individuals who appear to be managing their lives, careers, and responsibilities successfully on the outside, but are secretly struggling with substance use to cope with stress or trauma. It can be especially isolating because the external success masks the internal pain.</p>
        </div>

        <div class="faq-item" style="margin-bottom: 1.5rem;">
          <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;">Is my privacy protected as a professional in counseling?</h3>
          <p>Absolutely. Confidentiality is a cornerstone of my practice. As a licensed professional, I adhere to strict HIPAA regulations and ethical guidelines to ensure your privacy is completely protected, allowing you a safe space to discuss the unique stakes of your career without fear of judgment or exposure.</p>
        </div>

        <div class="faq-item" style="margin-bottom: 1.5rem;">
          <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;">How does EMDR help with cravings or triggers?</h3>
          <p>EMDR (Eye Movement Desensitization and Reprocessing) helps by targeting the underlying emotional distress and traumatic memories that drive the urge to use substances. By reprocessing these hidden traumas, EMDR reduces the intensity of triggers and cravings, addressing the root cause rather than just managing the symptoms.</p>
        </div>
      </div>
    </section>
''', 'html.parser')

cta_section = soup.find('section', class_='section--sage')
if cta_section:
    cta_section.insert_after(faq_snippet)

html_out = soup.encode(formatter="html5").decode('utf-8')
html_out = html_out.replace('&amp;mdash;', '&mdash;')

with open('/opt/build/repo/personal-addiction-counseling/index.html', 'w', encoding='utf-8') as f:
    f.write(html_out)

