import os
import glob
import re
import json

new_script = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "MedicalBusiness",
      "@id": "https://deirdrekuvaas.com/#organization",
      "name": "Inner World Counseling Services",
      "url": "https://deirdrekuvaas.com",
      "logo": "https://deirdrekuvaas.com/images/android-chrome-512x512.png",
      "image": "https://deirdrekuvaas.com/images/deirdre-kuvaas-headshot.webp",
      "description": "Specialized online trauma therapy and EMDR counseling for adults in ND, MN, OH, and UT.",
      "telecom": {
        "@type": "ContactPoint",
        "telephone": "+1-701-566-0322",
        "contactType": "customer service"
      },
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Horace",
        "addressRegion": "ND",
        "addressCountry": "US"
      },
      "areaServed": ["ND", "MN", "OH", "UT"],
      "founder": { "@id": "https://deirdrekuvaas.com/#person" },
      "sameAs": [
        "https://maps.app.goo.gl/MdUY176SzWX2Cpk48",
        "https://www.zocdoc.com/practice/inner-world-counseling-services-pllc-169362"
      ]
    },
    {
      "@type": "Person",
      "@id": "https://deirdrekuvaas.com/#person",
      "name": "Deirdre Kuvaas",
      "jobTitle": "Licensed Professional Clinical Counselor",
      "worksFor": { "@id": "https://deirdrekuvaas.com/#organization" },
      "hasCredential": {
        "@type": "EducationalOccupationalCredential",
        "credentialCategory": "license",
        "name": "LPCC"
      },
      "knowsAbout": ["Trauma therapy", "EMDR", "CPT", "Anxiety"],
      "sameAs": [
        "https://npiregistry.cms.hhs.gov/provider-view/1881112399",
        "https://www.psychologytoday.com/us/therapists/deirdre-kuvaas-horace-nd/1073735"
      ]
    }
  ]
}
</script>"""

html_files = glob.glob('**/*.html', recursive=True)
pattern = re.compile(r'<script\s+type="application/ld\+json">(.*?)</script>', re.DOTALL | re.IGNORECASE)

for filepath in html_files:
    if 'node_modules' in filepath or '.git' in filepath:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    matches = list(pattern.finditer(content))
    updated = False
    
    for m in reversed(matches):
        inner_text = m.group(1)
        if ('"MedicalBusiness"' in inner_text or '"Organization"' in inner_text) and 'Inner World Counseling Services' in inner_text:
            start, end = m.span()
            new_content = new_content[:start] + new_script + new_content[end:]
            updated = True

    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
