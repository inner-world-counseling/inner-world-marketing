import re

with open('about/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

breadcrumb_script = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": "https://deirdrekuvaas.com/about/#breadcrumb",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://deirdrekuvaas.com/" },
    { "@type": "ListItem", "position": 2, "name": "About", "item": "https://deirdrekuvaas.com/about/" }
  ]
}
</script>
"""

# Insert the breadcrumb script before the closing </head>
if "<!-- Structured Data: MedicalBusiness + Person -->" in content:
    content = content.replace("<!-- Structured Data: MedicalBusiness + Person -->", breadcrumb_script + "\n  <!-- Structured Data: MedicalBusiness + Person -->")
    with open('about/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added BreadcrumbList to about/index.html")
