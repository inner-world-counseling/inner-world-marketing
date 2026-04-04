import json
import re

file_path = '/opt/build/repo/ptsd/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title and Meta
content = content.replace(
    '<title>PTSD Treatment Online | EMDR &amp; CPT | ND, MN, OH, UT</title>',
    '<title>Evidence-Based PTSD Treatment for Adults | EMDR &amp; CPT | Online</title>'
)
content = content.replace(
    '<meta name="description" content="Online PTSD treatment with EMDR and Cognitive Processing Therapy. Serving adults in ND, MN, OH &amp; UT via telehealth.">',
    '<meta name="description" content="Specialized evidence-based PTSD treatment for adults using EMDR and Cognitive Processing Therapy. Online trauma therapy in ND, MN, OH, and UT.">'
)

content = content.replace(
    '<meta property="og:title" content="PTSD Treatment Online | EMDR &amp; CPT | ND, MN, OH, UT">',
    '<meta property="og:title" content="Evidence-Based PTSD Treatment for Adults | EMDR &amp; CPT | Online">'
)
content = content.replace(
    '<meta property="og:description" content="Online PTSD treatment with EMDR and Cognitive Processing Therapy. Serving adults in ND, MN, OH &amp; UT via telehealth.">',
    '<meta property="og:description" content="Specialized evidence-based PTSD treatment for adults using EMDR and Cognitive Processing Therapy. Online trauma therapy in ND, MN, OH, and UT.">'
)
content = content.replace(
    '<meta name="twitter:title" content="PTSD Treatment Online | EMDR &amp; CPT | ND, MN, OH, UT">',
    '<meta name="twitter:title" content="Evidence-Based PTSD Treatment for Adults | EMDR &amp; CPT | Online">'
)
content = content.replace(
    '<meta name="twitter:description" content="Online PTSD treatment with EMDR and Cognitive Processing Therapy. Serving adults in ND, MN, OH &amp; UT via telehealth.">',
    '<meta name="twitter:description" content="Specialized evidence-based PTSD treatment for adults using EMDR and Cognitive Processing Therapy. Online trauma therapy in ND, MN, OH, and UT.">'
)


# 2. Hero Optimization
old_banner = """  <!-- ========== PAGE BANNER ========== -->
  <section class="page-banner" style="background-image: url('/images/hero-banner-leaves.webp');" fetchpriority="high" role="img" aria-label="Lush green leaves macro shot representing growth and mental wellness." loading="eager" fetchpriority="high">
    <div class="container">
      <h1 class="page-banner__title">PTSD Treatment</h1>
    </div>
  </section>"""

new_banner = """  <!-- ========== PAGE BANNER ========== -->
  <section class="page-banner" style="position: relative; overflow: hidden;">
    <picture style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;">
      <source srcset="/images/hero-banner-leaves.webp" type="image/webp">
      <img src="/images/hero-banner-leaves.webp" alt="Lush green leaves macro shot representing growth and mental wellness." loading="eager" fetchpriority="high" style="width: 100%; height: 100%; object-fit: cover;">
    </picture>
    <div class="container" style="position: relative; z-index: 2;">
      <h1 class="page-banner__title">Evidence-Based PTSD Treatment for Adults</h1>
    </div>
  </section>"""

content = content.replace(old_banner, new_banner)

# 3. Content Injection
old_content = """          <h2>How Can Treatment Help?</h2>
          <p>There are a variety of treatments that can be used to treat PTSD. However, there are three specific techniques that are consistently gaining research-based evidence of their effectiveness in successfully treating PTSD.</p>
          <h3>Cognitive Processing Therapy</h3>
          <p>This modality focuses on how a person perceives a traumatic event and processes it. A therapist can help their client work through stuck points, which are certain thoughts related to the trauma that prevents the person from recovering.</p>
          <h3>EMDR</h3>
          <p>EMDR stands for eye movement desensitization and reprocessing. This technique uses bilateral sensory input such as side-to-side eye movements to stimulate the brain to process difficult thoughts, memories, and emotions.</p>
          <p>If you or a loved one suffer from PTSD and would like to explore treatment options, please reach out to me. I have personally seen amazing transformation through therapy and want to offer the help you need to enjoy life again.</p>"""

new_content = """          <h2>Beyond the Diagnosis: Understanding Your Nervous System</h2>
          <p>PTSD is more than just bad memories; it is a physiological response that keeps your nervous system trapped in survival mode. Healing requires expanding what experts call the <strong>"Window of Tolerance"</strong>&mdash;the optimal zone where you can process emotions without feeling overwhelmed or disconnected.</p>
          <p>When trauma occurs, the body's alarm system becomes hyper-sensitive. You may find yourself constantly on edge, experiencing <strong>hyper-vigilance</strong> (a state of high alert, panic, or anger) or falling into <strong>numbing</strong> (a state of shut down, disconnection, or depression). Specialized therapy helps your brain and body recalibrate, gently expanding your Window of Tolerance so you can restore balance and reclaim your life.</p>

          <h2>The "Gold Standard" Treatments</h2>
          <p>There are a variety of treatments that can be used to treat PTSD. However, when it comes to evidence-based recovery, <a href="/emdr">EMDR</a> and <a href="/cognitive-processing-therapy">Cognitive Processing Therapy (CPT)</a> are widely recognized as the two most researched and effective treatments for PTSD.</p>
          <h3>Cognitive Processing Therapy (CPT)</h3>
          <p>This modality focuses on how a person perceives a traumatic event and processes it. A therapist can help their client work through stuck points, which are certain thoughts related to the trauma that prevents the person from recovering. <a href="/cognitive-processing-therapy">Learn more about CPT.</a></p>
          <h3>EMDR</h3>
          <p>EMDR stands for Eye Movement Desensitization and Reprocessing. This technique uses bilateral sensory input such as side-to-side eye movements to stimulate the brain to process difficult thoughts, memories, and emotions safely. <a href="/emdr">Learn more about EMDR.</a></p>
          <p>If you or a loved one suffer from PTSD and would like to explore treatment options, please reach out to me. I have personally seen amazing transformation through therapy and want to offer the help you need to enjoy life again.</p>

          <h2 style="margin-top: 3rem;">Frequently Asked Questions</h2>
          <div class="faq-item" tabindex="0" onclick="this.classList.toggle('is-open')" onkeypress="if(event.key === 'Enter') this.classList.toggle('is-open')">
            <h3 class="faq-item__question">What is the difference between Trauma and PTSD?</h3>
            <div class="faq-item__answer">
              <p>While trauma refers to a deeply distressing event or series of events, PTSD is a specific clinical diagnosis that can develop after experiencing trauma. Not everyone who experiences trauma will develop PTSD. PTSD involves persistent symptoms like flashbacks, avoidance, hyper-vigilance, and negative changes in mood or thinking that last long after the event has passed.</p>
            </div>
          </div>
          <div class="faq-item" tabindex="0" onclick="this.classList.toggle('is-open')" onkeypress="if(event.key === 'Enter') this.classList.toggle('is-open')">
            <h3 class="faq-item__question">Do I have to relive the event to treat PTSD?</h3>
            <div class="faq-item__answer">
              <p>No. Evidence-based treatments like EMDR or CPT do not require you to "relive" your trauma in a re-traumatizing way. EMDR allows you to process distressing memories while remaining safely grounded in the present moment. CPT focuses on how the trauma has affected your current beliefs and thoughts rather than recounting the details of the event itself.</p>
            </div>
          </div>
          <div class="faq-item" tabindex="0" onclick="this.classList.toggle('is-open')" onkeypress="if(event.key === 'Enter') this.classList.toggle('is-open')">
            <h3 class="faq-item__question">How long does evidence-based PTSD treatment take?</h3>
            <div class="faq-item__answer">
              <p>The length of treatment varies depending on the individual, the complexity of the trauma, and the specific approach used. However, both EMDR or CPT are often considered short-term therapies. Many clients begin to experience significant relief and noticeable changes in symptoms within 8 to 12 sessions, though some may choose longer-term support depending on their unique needs and goals.</p>
            </div>
          </div>"""

content = content.replace(old_content, new_content)

# 4. Schema update
schema_start = content.find('<script type="application/ld+json">')
schema_end = content.find('</script>', schema_start) + len('</script>')
schema_str = content[schema_start:schema_end]

# Extract JSON
json_start = schema_str.find('{')
json_end = schema_str.rfind('}') + 1
json_data = json.loads(schema_str[json_start:json_end])

json_data['@graph'].append({
    "@type": "Service",
    "serviceType": "PTSD Treatment / Trauma Recovery",
    "description": "Specialized PTSD therapy using EMDR or CPT for professionals and high-achieving adults.",
    "provider": {
        "@id": "https://deirdrekuvaas.com/#person"
    }
})

json_data['@graph'].append({
    "@type": "FAQPage",
    "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the difference between Trauma and PTSD?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "While trauma refers to a deeply distressing event or series of events, PTSD is a specific clinical diagnosis that can develop after experiencing trauma. Not everyone who experiences trauma will develop PTSD. PTSD involves persistent symptoms like flashbacks, avoidance, hyper-vigilance, and negative changes in mood or thinking that last long after the event has passed."
          }
        },
        {
          "@type": "Question",
          "name": "Do I have to relive the event to treat PTSD?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. Evidence-based treatments like EMDR or CPT do not require you to \"relive\" your trauma in a re-traumatizing way. EMDR allows you to process distressing memories while remaining safely grounded in the present moment. CPT focuses on how the trauma has affected your current beliefs and thoughts rather than recounting the details of the event itself."
          }
        },
        {
          "@type": "Question",
          "name": "How long does evidence-based PTSD treatment take?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The length of treatment varies depending on the individual, the complexity of the trauma, and the specific approach used. However, both EMDR or CPT are often considered short-term therapies. Many clients begin to experience significant relief and noticeable changes in symptoms within 8 to 12 sessions, though some may choose longer-term support depending on their unique needs and goals."
          }
        }
    ]
})

new_schema_str = '<script type="application/ld+json">\n' + json.dumps(json_data, indent=2) + '\n</script>'
content = content.replace(schema_str, new_schema_str)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
