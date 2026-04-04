import os
import re

directory = '.'
modified_files = []

def process_file(file_path):
    if 'node_modules' in file_path or '.git' in file_path or '.netlify' in file_path or file_path.endswith('apply_replacements.py') or file_path.endswith('apply_replacements.js'):
        return

    ext = os.path.splitext(file_path)[1].lower()
    if ext not in ['.html', '.css', '.js', '.py', '.txt', '.xml', '.json', '.toml'] and ext != '':
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception:
        return

    content = original_content

    # First replace the longer phrase
    content = content.replace('specializing in EMDR and CPT', 'utilizing evidence-based modalities such as EMDR or CPT')
    
    # Then the shorter phrase
    content = content.replace('EMDR and CPT', 'EMDR or CPT')
    
    # Finally the other phrase
    # Replace EMDR Specialist (case sensitive exact match)
    content = content.replace('EMDR Specialist', 'Trained in EMDR')
    # Replace EMDR specialist (lowercase s)
    content = content.replace('EMDR specialist', 'Trained in EMDR')
    # Replace emdr specialist (lowercase)
    content = content.replace('emdr specialist', 'trained in emdr')

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        modified_files.append(file_path)

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        process_file(file_path)

result_path = os.path.join('.netlify', 'results.md')

lines = [
    "The requested clinical terminology updates have been applied across all project files.",
    "",
    "The replacements made were:",
    "- 'specializing in EMDR and CPT' replaced with 'utilizing evidence-based modalities such as EMDR or CPT'",
    "- 'EMDR and CPT' replaced with 'EMDR or CPT'",
    "- 'EMDR Specialist' replaced with 'Trained in EMDR'",
    "",
    "Here is the list of files modified:"
]
for f in modified_files:
    lines.append("- " + f)

with open(result_path, 'w', encoding='utf-8') as f:
    f.write(chr(10).join(lines))

print("Modified files:")
for f in modified_files:
    print(f)
