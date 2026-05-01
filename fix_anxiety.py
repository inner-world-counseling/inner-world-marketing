import re
with open('./counseling-for-anxiety/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

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

# find <div id="pt-verified-seal">\n       </div>
if '<div id="pt-verified-seal">' in content and "GoodTherapy Verified Seal" not in content:
    # match including the closing div
    content = re.sub(r'<div id="pt-verified-seal">\s*</div>', '<div id="pt-verified-seal">\n       </div>' + good_therapy_badge, content)
    
    with open('./counseling-for-anxiety/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
