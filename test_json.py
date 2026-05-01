import json
import os
import re
import sys

has_error = False
for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            for match in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', content, flags=re.DOTALL):
                try:
                    json.loads(match.group(1))
                except json.JSONDecodeError as e:
                    print(f"JSON Error in {filepath}: {e}")
                    has_error = True

if not has_error:
    print("All JSON-LD blocks are valid JSON.")
else:
    sys.exit(1)
