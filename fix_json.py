import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # UPDATE 1 & 2
    good_therapy_badge = """
<!-- GoodTherapy Verified Seal -->
<div style="margin-top:0.5rem;">
  <a href="https://www.goodtherapy.org/therapists/profile/deirdre-kuvaas-20260425-counselor" target="_blank" rel="noopener noreferrer">
    <img src="https://www.goodtherapy.org/graph/seals/verified_seal2.svg" alt="Deirdre Kuvaas, Licensed Professional Clinical Counselor verified by GoodTherapy.org" style="width:100px; height:auto;" loading="lazy">
  </a>
</div>

<!-- EMDRIA Member Link -->
<div style="margin-top:0.5rem; font-size:0.8125rem;">
  <a href="https://www.emdria.org/directory/people/deirdre-kuvaas/" target="_blank" rel="noopener noreferrer">
    Member, EMDR International Association (EMDRIA)
  </a>
</div>"""
    
    pt_seal_div = '<div id="pt-verified-seal"></div>'
    if pt_seal_div in content and "GoodTherapy Verified Seal" not in content:
        # preserve indentation
        match = re.search(r'([ \t]+)<div id="pt-verified-seal"></div>', content)
        indent = match.group(1) if match else "          "
        replacement = pt_seal_div + "\n" + "\n".join([indent + line if line.strip() else line for line in good_therapy_badge.split('\n')])
        content = content.replace(pt_seal_div, replacement)

    # UPDATE 3: Update sameAs on Person
    # Find "sameAs": [\n ... ] inside Person entity
    # Because there are two "sameAs" (one for MedicalBusiness, one for Person), we can find it by looking for Person block
    
    # We can use a regex to find the Person entity, and then replace its sameAs array
    def replacer_person(match):
        # match.group(1) is everything from "@type": "Person" to "sameAs": [ ... ]
        # wait, it's easier to find the exact block for Person
        person_str = match.group(0)
        
        # Replace sameAs inside this person block
        new_same_as = '''"sameAs": [
        "https://npiregistry.cms.hhs.gov/provider-view/1881112399",
        "https://www.psychologytoday.com/us/therapists/deirdre-kuvaas-fargo-nd/1073735",
        "https://www.linkedin.com/in/deirdre-kuvaas",
        "https://www.emdria.org/directory/people/deirdre-kuvaas/",
        "https://www.goodtherapy.org/therapists/profile/deirdre-kuvaas-20260425-counselor"
      ]'''
        
        # This regex replaces the sameAs array
        updated_person = re.sub(r'"sameAs":\s*\[\s*"https://npiregistry\.cms\.hhs\.gov/provider-view/1881112399",\s*"https://www\.psychologytoday\.com/us/therapists/deirdre-kuvaas-horace-nd/1073735"(?:,\s*"https://www\.linkedin\.com/in/deirdre-kuvaas")?\s*\]', new_same_as, person_str)
        return updated_person

    # Match @type: Person and its entire block until the end of the object
    content = re.sub(r'"@type":\s*"Person".*?"sameAs":\s*\[.*?\]', replacer_person, content, flags=re.DOTALL)

    # UPDATE 4: Add hasCredential to MedicalBusiness
    # Find areaServed inside MedicalBusiness
    # The block looks like:
    #       "areaServed": [
    #         "ND",
    #         "MN",
    #         "OH",
    #         "UT"
    #       ],
    
    has_credential_block = '''"areaServed": [
        "ND",
        "MN",
        "OH",
        "UT"
      ],
      "hasCredential": {
        "@type": "EducationalOccupationalCredential",
        "name": "EMDR Trained Professional",
        "credentialCategory": "Professional Training",
        "recognizedBy": {
          "@type": "Organization",
          "name": "EMDR International Association",
          "url": "https://www.emdria.org"
        },
        "url": "https://www.emdria.org/directory/people/deirdre-kuvaas/"
      },'''

    # only replace if not already there
    if '"hasCredential": {' not in content.split('"@type": "Person"')[0]: # making sure we look at MedicalBusiness roughly
        # just replace the areaServed block globally, as it is only in MedicalBusiness
        old_area_served_regex = r'"areaServed":\s*\[\s*"ND",\s*"MN",\s*"OH",\s*"UT"\s*\],\n'
        def replace_area_served(m):
            return has_credential_block + '\n'
            
        content = re.sub(old_area_served_regex, has_credential_block + '\n', content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))
