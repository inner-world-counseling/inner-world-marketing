from bs4 import BeautifulSoup
import json

with open('/opt/build/repo/index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

for i, script in enumerate(soup.find_all('script', type='application/ld+json')):
    try:
        json.loads(script.string)
        print(f"Script {i} valid")
    except Exception as e:
        print(f"Script {i} INVALID: {e}")
