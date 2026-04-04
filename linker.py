import os
import re
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self, links, filepath):
        super().__init__(convert_charrefs=False)
        self.links = links
        self.filepath = filepath
        self.output = []
        self.ignore_tags = {'script', 'style', 'a', 'title', 'meta', 'link'}
        self.current_ignored_tags = []
        self.links_added = 0
        self.used_keywords = set()

    def handle_starttag(self, tag, attrs):
        if tag in self.ignore_tags:
            self.current_ignored_tags.append(tag)
        
        attr_str = ""
        for k, v in attrs:
            if v is None:
                attr_str += f' {k}'
            else:
                # We need to correctly quote the attributes. Using simple quotes for simplicity, 
                # but it might differ from original. The standard library HTMLParser unfortunately 
                # doesn't preserve exact original quoting. We might need a safer approach to not rewrite all HTML.
                pass
        
        # Actually, using HTMLParser to rewrite the whole document will mess up formatting, void elements, etc.
        # It's better to use regex but be smarter: track opened <script>, <style>, <a> tags.
        pass

# Since standard HTMLParser rewriting can change formatting, let's stick to regex but with a simple state machine.

def process_html_file(filepath, links_config):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to tokenize HTML into tags, comments, and text.
    # This matches <!-- comment --> or <tag> or text
    tokens = re.split(r'(<!--.*?-->|<[^>]+>)', content, flags=re.DOTALL)
    
    in_ignore_tag = None
    ignore_tags = ['script', 'style', 'a', 'title', 'head']
    
    links_added = 0
    used_keywords = set()
    
    for i in range(len(tokens)):
        token = tokens[i]
        if token.startswith('<!--'):
            continue
        elif token.startswith('<'):
            # It's a tag
            tag_match = re.match(r'<\s*(/?)\s*([a-zA-Z0-9\-]+)', token)
            if tag_match:
                is_closing = tag_match.group(1) == '/'
                tag_name = tag_match.group(2).lower()
                
                if not is_closing and tag_name in ignore_tags:
                    if not in_ignore_tag:
                        in_ignore_tag = tag_name
                elif is_closing and tag_name == in_ignore_tag:
                    in_ignore_tag = None
        else:
            # It's text
            if not in_ignore_tag and links_added < 3 and token.strip():
                text = token
                for pattern, target in links_config:
                    if target in filepath: # don't link to self
                        continue
                    if pattern in used_keywords:
                        continue
                    
                    # check if the word is in the text
                    # We only match whole words
                    # Also we shouldn't replace inside words
                    match = re.search(pattern, text, re.IGNORECASE)
                    if match:
                        matched_text = match.group(0)
                        replacement = f'<a href="{target}">{matched_text}</a>'
                        # Replace only the first occurrence
                        new_text = re.sub(pattern, replacement, text, count=1, flags=re.IGNORECASE)
                        if new_text != text:
                            text = new_text
                            links_added += 1
                            used_keywords.add(pattern)
                            if links_added >= 3:
                                break
                tokens[i] = text

    new_content = ''.join(tokens)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, links_added
    return False, 0

links = [
    (r'\b(childhood trauma)\b', '/counseling-for-trauma'),
    (r'\b(Cognitive Processing Therapy)\b', '/cognitive-processing-therapy'),
    (r'\b(people-pleasing)\b', '/people-pleasing'),
    (r'\b(virtual therapy)\b', '/telehealth'),
    (r'\b(substance use)\b', '/personal-addiction-counseling'),
    (r'\b(anxiety)\b', '/counseling-for-anxiety'),
    (r'\b(worry)\b', '/counseling-for-anxiety'),
    (r'\b(trauma)\b', '/counseling-for-trauma'),
    (r'\b(PTSD)\b', '/ptsd'),
    (r'\b(EMDR)\b', '/emdr'),
    (r'\b(CPT)\b', '/cognitive-processing-therapy'),
    (r'\b(fawning)\b', '/people-pleasing'),
    (r'\b(boundaries)\b', '/people-pleasing'),
    (r'\b(telehealth)\b', '/telehealth'),
    (r'\b(Minnesota)\b', '/minnesota-telehealth-therapy'),
    (r'\b(addiction)\b', '/personal-addiction-counseling')
]

html_files = []
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

total_changed = 0
total_links = 0
for filepath in html_files:
    changed, count = process_html_file(filepath, links)
    if changed:
        print(f"Changed {filepath} - Added {count} links")
        total_changed += 1
        total_links += count

print(f"Total files: {total_changed}, Links added: {total_links}")
