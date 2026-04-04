import os
import re

pattern = re.compile(
    r'(<li[^>]*>\s*<a[^>]*>\s*Who I Help\s*</a>\s*<ul[^>]*>.*?</ul>\s*</li>)',
    re.IGNORECASE | re.DOTALL
)

def check_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = pattern.findall(content)
    print(f"{filepath}: found {len(matches)} matches")

check_file('index.html')
check_file('counseling-for-anxiety/index.html')
check_file('faqs/index.html')
