import os
import re

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Pattern for '<a href="/privacy">Privacy</a>' possibly with newlines
    # and '<a href="/terms">Terms</a>'
    
    # Let's just find the closing tag for the Terms link and add the new link there.
    # We will search for <a href="/terms">Terms</a> or <a href="/terms.html">Terms</a>
    # or similar and replace it.
    
    pattern = r'(<a[^>]*href="/terms(?:\.html)?"[^>]*>\s*Terms\s*</a>)'
    replacement = r'\1\n<a href="/assets/privacy-practices-2.pdf" target="_blank" rel="noopener noreferrer">Notice of Privacy Practices (Updated Feb 2026)</a>'
    
    # Wait, check if it's already there
    if 'Notice of Privacy Practices (Updated Feb 2026)' in content:
        return
        
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('/opt/build/repo'):
    if '.git' in root or 'node_modules' in root or '.netlify' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))
