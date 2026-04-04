import json
import re

with open('/opt/build/repo/about/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title and H1
content = re.sub(r'<title>.*?</title>', '<title>Deirdre Kuvaas | Trauma &amp; Addiction Specialist</title>', content)
content = re.sub(r'<h1 class="page-banner__title">.*?</h1>', '<h1 class="page-banner__title">Deirdre Kuvaas | Trauma &amp; Addiction Specialist</h1>', content)

# 2. Update Headshot to picture with LCP optimization
old_img = '''<div class="about-intro__image">
            <img src="/images/deirdre-kuvaas-headshot.webp" alt="Deirdre Kuvaas, LPCC, LADC, LCMHC - Telehealth Trauma Specialist." loading="lazy" width="600" height="400">
          </div>'''
new_img = '''<div class="about-intro__image">
            <picture>
              <source srcset="/images/deirdre-kuvaas-headshot.webp" type="image/webp">
              <img src="/images/deirdre-kuvaas-headshot.webp" alt="Deirdre Kuvaas, LPCC, LADC, LCMHC - Telehealth Trauma Specialist." loading="eager" fetchpriority="high" width="600" height="400">
            </picture>
          </div>'''
content = content.replace(old_img, new_img)

# 3. Semantic Content Injection
old_my_style_end = '''    </section>

    <!-- Specific Ways I Can Help You -->'''
new_high_achiever_section = '''    </section>

    <!-- A Specialized Approach for the High-Achiever -->
    <section class="section">
      <div class="container">
        <h2>A Specialized Approach for the High-Achiever</h2>
        <p>My mission is clear: helping driven professionals navigate the complex intersection of high-pressure careers and hidden trauma. For over 9 years, I have specialized in guiding high-achievers who look like they have it all together on the outside, but are struggling with perfectionism, anxiety, or burnout underneath.</p>
        <p>Using my "Mind-Body-Logic" framework—a highly effective integration of EMDR or CPT—we work together to process the root causes of distress without getting lost in endless talk therapy. This approach honors your intellect while safely addressing the nervous system.</p>
      </div>
    </section>

    <!-- Specific Ways I Can Help You -->'''
content = content.replace(old_my_style_end, new_high_achiever_section)

# 4. The Credential Cloud
old_education = '''    <!-- Education -->
    <section class="section">
      <div class="container" style="max-width:800px;">
        <h2>About Deirdre's Education</h2>
        <ul>
          <li>Bachelor of Science in Psychology from East Stroudsburg University of Pennsylvania (2010)</li>
          <li>Master of Science in Counseling from University of Mary, Fargo, North Dakota (2017)</li>
          <li>Licensed Alcohol and Drug Counselor in Minnesota</li>
          <li>Licensed Professional Clinical Counselor in North Dakota, Minnesota and Ohio</li>
          <li>Licensed Clinical Mental Health Counselor in Utah</li>
          <li>Experience working with mental health, substance use, in inpatient, residential and outpatient settings.</li>
        </ul>
        <p><strong>Offering services in:</strong> Minnesota | North Dakota | Ohio | Utah</p>
      </div>
    </section>'''
new_education = '''    <!-- Education & Credentials -->
    <section class="section">
      <div class="container" style="max-width:800px;">
        <h2>Education &amp; Verified Credentials</h2>
        <ul>
          <li><strong>M.S. in Counseling:</strong> University of Mary, Fargo, North Dakota (2017)</li>
          <li><strong>B.S. in Psychology:</strong> East Stroudsburg University of Pennsylvania (2010)</li>
        </ul>
        <h3 style="margin-top: 1.5rem;">Licenses</h3>
        <ul class="credential-cloud" style="list-style-type: none; padding: 0; display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 1.5rem;">
          <li style="background: #e9ecef; padding: 5px 12px; border-radius: 20px; font-size: 0.9em; color: #333;"><strong>LPCC:</strong> Licensed Professional Clinical Counselor (ND, MN, OH)</li>
          <li style="background: #e9ecef; padding: 5px 12px; border-radius: 20px; font-size: 0.9em; color: #333;"><strong>LCMHC:</strong> Licensed Clinical Mental Health Counselor (UT)</li>
          <li style="background: #e9ecef; padding: 5px 12px; border-radius: 20px; font-size: 0.9em; color: #333;"><strong>LADC:</strong> Licensed Alcohol and Drug Counselor (MN)</li>
        </ul>
        <p><strong>Currently Licensed &amp; Offering Telehealth Services In:</strong> <br>North Dakota (ND) | Minnesota (MN) | Ohio (OH) | Utah (UT)</p>
      </div>
    </section>'''
content = content.replace(old_education, new_education)

# 5. Person Schema update
old_person_schema = '''    {
      "@type": "Person",
      "@id": "https://deirdrekuvaas.com/#person",
      "name": "Deirdre Kuvaas",
      "jobTitle": "Licensed Professional Clinical Counselor",
      "worksFor": {
        "@id": "https://deirdrekuvaas.com/#organization"
      },
      "hasCredential": {
        "@type": "EducationalOccupationalCredential",
        "credentialCategory": "license",
        "name": "LPCC"
      },
      "knowsAbout": [
        "Trauma therapy",
        "EMDR",
        "CPT",
        "Anxiety"
      ],
      "sameAs": [
        "https://npiregistry.cms.hhs.gov/provider-view/1881112399",
        "https://www.psychologytoday.com/us/therapists/deirdre-kuvaas-horace-nd/1073735"
      ]
    }'''
new_person_schema = '''    {
      "@type": "Person",
      "@id": "https://deirdrekuvaas.com/#person",
      "name": "Deirdre Kuvaas",
      "jobTitle": "Licensed Professional Clinical Counselor",
      "worksFor": {
        "@id": "https://deirdrekuvaas.com/#organization"
      },
      "hasCredential": [
        {
          "@type": "EducationalOccupationalCredential",
          "credentialCategory": "license",
          "name": "Licensed Professional Clinical Counselor (LPCC)"
        },
        {
          "@type": "EducationalOccupationalCredential",
          "credentialCategory": "license",
          "name": "Licensed Alcohol and Drug Counselor (LADC)"
        },
        {
          "@type": "EducationalOccupationalCredential",
          "credentialCategory": "license",
          "name": "Licensed Clinical Mental Health Counselor (LCMHC)"
        }
      ],
      "knowsAbout": [
        "EMDR Therapy",
        "Cognitive Processing Therapy",
        "Addiction Recovery",
        "Trauma-Informed Care"
      ],
      "sameAs": [
        "https://npiregistry.cms.hhs.gov/provider-view/1881112399",
        "https://www.psychologytoday.com/us/therapists/deirdre-kuvaas-maple-grove-mn/1073735",
        "https://www.linkedin.com/in/deirdre-kuvaas"
      ]
    }'''
content = content.replace(old_person_schema, new_person_schema)

# 6. FAQ Section
old_contact_placeholder = '''    <!-- Contact Form Placeholder -->
    <section class="section section--cream">'''
new_faq = '''    <!-- Frequently Asked Questions -->
    <section class="section section--sage">
      <div class="container" style="max-width:800px;">
        <h2 style="text-align: center;">Frequently Asked Questions</h2>
        <div class="faq-list">
          <div class="faq-item" style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;">What is your therapeutic philosophy?</h3>
            <p>I believe therapy should be straightforward, collaborative, and deeply rooted in science. My "Mind-Body-Logic" framework focuses on uncovering the root causes of distress—like hidden trauma that fuels perfectionism and burnout—using evidence-based tools like EMDR or CPT. You are the expert on your life; my role is to help you map the patterns that keep you stuck and guide you toward authentic healing without relying on generic affirmations.</p>
          </div>
          <div class="faq-item" style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;">How do I know if we are a good fit?</h3>
            <p>We are likely a great fit if you are a driven, high-functioning professional who looks like you have it all together on the outside but struggles with anxiety, people-pleasing, or the lasting impacts of past trauma on the inside. I provide a real, human space where you can drop the need to impress. If you're ready to do the deeper work to reclaim your energy and boundaries, we will work well together.</p>
          </div>
          <div class="faq-item" style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;">What states are you currently licensed to practice in?</h3>
            <p>I am a fully licensed telehealth therapist providing counseling services to residents of North Dakota (LPCC), Minnesota (LPCC, LADC), Ohio (LPCC), and Utah (LCMHC).</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Form Placeholder -->
    <section class="section section--cream">'''
content = content.replace(old_contact_placeholder, new_faq)

with open('/opt/build/repo/about/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated /about/index.html")
