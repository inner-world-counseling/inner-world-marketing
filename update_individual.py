from bs4 import BeautifulSoup
import json

with open('individual-therapy/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 1. Hero Optimization: Update Meta/H1
title = soup.find('title')
if title:
    title.string = "Individual Therapy for High-Functioning Adults | ND, MN, OH, UT"

for meta in soup.find_all('meta'):
    if meta.get('name') == 'description':
        meta['content'] = "Individual therapy for high-functioning adults and professionals. Address the root cause of burnout, anxiety, and the 'strong one' mask with Deirdre Kuvaas, LPCC in ND, MN, OH & UT."
    elif meta.get('property') == 'og:title':
        meta['content'] = "Individual Therapy for High-Functioning Adults | ND, MN, OH, UT"
    elif meta.get('property') == 'og:description':
        meta['content'] = "Individual therapy for high-functioning adults and professionals. Address the root cause of burnout, anxiety, and the 'strong one' mask with Deirdre Kuvaas, LPCC in ND, MN, OH & UT."
    elif meta.get('name') == 'twitter:title':
        meta['content'] = "Individual Therapy for High-Functioning Adults | ND, MN, OH, UT"
    elif meta.get('name') == 'twitter:description':
        meta['content'] = "Individual therapy for high-functioning adults and professionals. Address the root cause of burnout, anxiety, and the 'strong one' mask with Deirdre Kuvaas, LPCC in ND, MN, OH & UT."

# H1 and Picture tag
banner = soup.find('section', class_='page-banner')
if banner:
    # Clear existing banner content
    banner.clear()
    banner['style'] = "position: relative;"
    
    picture_html = """
    <picture style="position: absolute; inset: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none;">
      <source srcset="/images/hero-banner-leaves.webp" type="image/webp">
      <img src="/images/hero-banner-leaves.webp" alt="Lush green leaves macro shot representing growth and mental wellness." style="width: 100%; height: 100%; object-fit: cover;" loading="eager" fetchpriority="high">
    </picture>
    <div class="container" style="position: relative; z-index: 1;">
      <h1 class="page-banner__title">Individual Therapy for High-Functioning Adults</h1>
    </div>
    """
    banner.append(BeautifulSoup(picture_html, 'html.parser'))
    
    # Remove old attributes from section that are no longer needed
    if 'fetchpriority' in banner.attrs:
        del banner['fetchpriority']
    if 'loading' in banner.attrs:
        del banner['loading']
    if 'role' in banner.attrs:
        del banner['role']
    if 'aria-label' in banner.attrs:
        del banner['aria-label']

# 2. Semantic Content Injection & FAQ Integration
main = soup.find('main')
cta_section = soup.find('section', class_='section--sage')

if main and cta_section:
    new_content_html = """
    <section class="section" style="background-color: #fdfdfd; border-top: 1px solid #eaeaea;">
      <div class="container">
        <div class="content-area">
          <h2>Beyond General Support: A Partnership in Growth</h2>
          <p>Many of the people I work with are successful professionals, caregivers, or high-achievers who are used to being the "strong one" for everyone else. You might be carrying a pervasive belief that "I should be able to handle this" and feeling increasingly exhausted by the effort it takes to keep it all together.</p>
          <p>Individual therapy is your dedicated space to finally set down that mask. We move beyond generic support or simple venting. Instead, we form a partnership to understand and update the underlying survival systems that served you well in the past but are now causing burnout, anxiety, and disconnectedness.</p>
          <h3>An Integrative, Mind-Body Approach</h3>
          <p>Talk therapy is helpful, but sometimes it isn't enough to reach the deep, bodily roots of anxiety and trauma. That is why I integrate <strong>EMDR (Eye Movement Desensitization and Reprocessing)</strong> and <strong>CPT (Cognitive Processing Therapy)</strong> into our individual sessions. By addressing both the cognitive narratives ("I have to be perfect") and the physiological responses (the nervous system's fight-or-flight reactions), we use a holistic, mind-body approach that promotes lasting healing.</p>
        </div>
      </div>
    </section>
    
    <section class="section faq-section" aria-labelledby="faq-heading">
      <div class="container">
        <div class="content-area">
          <h2 id="faq-heading">Frequently Asked Questions</h2>
          <div itemscope itemprop="mainEntity" itemtype="https://schema.org/FAQPage">
            <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" style="margin-bottom: 1.5rem;">
              <h3 itemprop="name" style="font-size: 1.25rem; font-weight: 600;">What can I expect in our first individual session?</h3>
              <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                <div itemprop="text">
                  <p>In our first session, known as a Psychiatric Diagnostic Evaluation, we focus on understanding your story, your current struggles, and your goals. It's a structured but conversational space where we explore what brings you to therapy and begin mapping out a customized plan that fits your unique needs and lifestyle.</p>
                </div>
              </div>
            </div>
            
            <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" style="margin-bottom: 1.5rem;">
              <h3 itemprop="name" style="font-size: 1.25rem; font-weight: 600;">Do you work with high-achieving professionals specifically?</h3>
              <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                <div itemprop="text">
                  <p>Yes. I specialize in working with high-functioning adults, professionals, and caregivers who often look like they have everything together on the outside but feel overwhelmed, anxious, or burnt out on the inside. We focus on dismantling the pressure of perfectionism and the "strong one" mask.</p>
                </div>
              </div>
            </div>
            
            <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" style="margin-bottom: 1.5rem;">
              <h3 itemprop="name" style="font-size: 1.25rem; font-weight: 600;">Is online therapy as effective as in-person for deep work?</h3>
              <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                <div itemprop="text">
                  <p>Absolutely. Research consistently shows that online therapy is just as effective as in-person therapy. With the convenience of a secure, confidential video connection, you can engage in deep work—including specialized modalities like EMDR or CPT—from the comfort and safety of your own environment.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
    cta_section.insert_before(BeautifulSoup(new_content_html, 'html.parser'))

# 3. AI Discovery (Schema): Add JSON-LD for Service & FAQ
script_tag = soup.find('script', type='application/ld+json')
if script_tag:
    try:
        data = json.loads(script_tag.string)
        if '@graph' in data:
            data['@graph'].append({
                "@type": "Service",
                "serviceType": "Individual Psychotherapy",
                "areaServed": ["North Dakota", "Minnesota", "Ohio", "Utah"],
                "provider": {
                    "@id": "https://deirdrekuvaas.com/#person"
                },
                "url": "https://deirdrekuvaas.com/individual-therapy"
            })
            
            data['@graph'].append({
                "@type": "FAQPage",
                "@id": "https://deirdrekuvaas.com/individual-therapy/#faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "What can I expect in our first individual session?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "In our first session, known as a Psychiatric Diagnostic Evaluation, we focus on understanding your story, your current struggles, and your goals. It's a structured but conversational space where we explore what brings you to therapy and begin mapping out a customized plan that fits your unique needs and lifestyle."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Do you work with high-achieving professionals specifically?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Yes. I specialize in working with high-functioning adults, professionals, and caregivers who often look like they have everything together on the outside but feel overwhelmed, anxious, or burnt out on the inside. We focus on dismantling the pressure of perfectionism and the \"strong one\" mask."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Is online therapy as effective as in-person for deep work?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Absolutely. Research consistently shows that online therapy is just as effective as in-person therapy. With the convenience of a secure, confidential video connection, you can engage in deep work—including specialized modalities like EMDR or CPT—from the comfort and safety of your own environment."
                        }
                    }
                ]
            })
            
            script_tag.string = json.dumps(data, indent=2)
    except Exception as e:
        print(f"Error parsing JSON-LD: {e}")

with open('individual-therapy/index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Done")
