import os
import re

base_dir = '/opt/build/repo'

descriptions = {
    '/': "Deirdre Kuvaas, LPCC offers virtual telehealth therapy for anxiety, trauma, PTSD, EMDR, and substance use in Minnesota, North Dakota, Ohio, and Utah. Book your session today.",
    '/about': "Meet Deirdre Kuvaas, LPCC \u2013 licensed counselor with 10+ years specializing in trauma, addiction, and anxiety therapy via secure online sessions in ND, MN, OH, UT.",
    '/services': "Virtual counseling services including EMDR, CPT, anxiety treatment, trauma recovery, people-pleasing support, and addiction counseling \u2013 telehealth in MN, ND, OH, UT.",
    '/faqs': "Answers to common questions about online therapy, telehealth process, insurance, rates, and trauma-informed counseling with Deirdre Kuvaas, LPCC.",
    '/contact': "Contact Deirdre Kuvaas for virtual therapy in Minnesota, North Dakota, Ohio, and Utah. Call (701) 404-7895 or use our secure form for anxiety and trauma support.",
    '/appointment-request': "Request a free 15-minute consultation or schedule your online therapy session for anxiety, trauma, or addiction \u2013 serving ND, MN, OH, UT.",
    '/blog': "Mental health blog by Deirdre Kuvaas: insights on trauma responses, fawning/people-pleasing, boundaries, empathy myths, and healing."
}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine path
    rel_path = os.path.relpath(filepath, base_dir)
    rel_path = rel_path.replace('\\\\', '/')
    if rel_path == 'index.html':
        url_path = '/'
    elif rel_path.endswith('/index.html'):
        url_path = '/' + rel_path[:-11]
    else:
        url_path = '/' + rel_path.replace('.html', '')
        
    canonical_url = f"https://deirdrekuvaas.com{url_path}"

    # Extract title to generate generic description if needed
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else "Therapy Services"
    # remove trailing " | Inner World Counseling" if present
    title = re.sub(r'\s*\|\s*Inner World Counseling(?: Services)?.*$', '', title, flags=re.IGNORECASE)

    if url_path in descriptions:
        desc = descriptions[url_path]
    else:
        desc = f"Explore {title} \u2013 specialized virtual telehealth therapy with Deirdre Kuvaas, LPCC in MN, ND, OH, and UT."

    # Remove ALL existing canonical and description tags
    content = re.sub(r'<link\s+rel=["\']canonical["\'].*?>\s*', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+name=["\']description["\'].*?>\s*', '', content, flags=re.IGNORECASE)

    # Insert new tags
    new_tags = f'\n  <meta name="description" content="{desc}">\n  <link rel="canonical" href="{canonical_url}">\n'
    
    if '<title>' in content:
        content = re.sub(r'(<title>.*?</title>)', r'\1' + new_tags, content, flags=re.IGNORECASE | re.DOTALL)
    elif '<head>' in content:
        content = re.sub(r'(<head.*?>)', r'\1' + new_tags, content, flags=re.IGNORECASE | re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for root, dirs, files in os.walk(base_dir):
    if '.git' in root or '.netlify' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

print("SEO update complete.")