import re
import glob
import os
import json
import urllib.request
from urllib.parse import urlparse

# 1. Read primary schema from index.html
with open('/opt/build/repo/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Extract comprehensive schema
m = re.search(r'<script type="application/ld\+json">\s*\{\s*"@context":\s*"https://schema\.org",\s*"@graph":\s*\[\s*\{\s*"@type":\s*"MedicalBusiness".*?"name":\s*"Deirdre Kuvaas".*?\}\s*\]\s*\}\s*</script>', idx_content, re.DOTALL)
if not m:
    print("Could not find primary schema in index.html")
else:
    primary_schema = m.group(0)
    print("Found primary schema, length:", len(primary_schema))
