import os
import re

def main():
    repo_dir = '/opt/build/repo'
    updated_count = 0
    html_files = []
    
    for root, dirs, files in os.walk(repo_dir):
        if '.git' in root or '.netlify' in root:
            continue
        for f in files:
            if f.endswith('.html'):
                full_path = os.path.join(root, f)
                if full_path == os.path.join(repo_dir, 'index.html'):
                    continue
                html_files.append(full_path)
    
    # Let's match any <link> tag that has rel="canonical" and an href
    # We will search for <link ... href="..." ...> and if it contains rel="canonical", we fix it.
    
    link_pattern = re.compile(r'(<link\s+[^>]*href=["\'](https://deirdrekuvaas\.com/[^"\']+)["\'][^>]*>)', re.IGNORECASE)
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            
        def replacer(match):
            full_tag = match.group(1)
            url = match.group(2)
            
            if 'rel="canonical"' in full_tag.lower() or "rel='canonical'" in full_tag.lower():
                if not url.endswith('/'):
                    # add slash to url
                    new_tag = full_tag.replace(f'href="{url}"', f'href="{url}/"')
                    new_tag = new_tag.replace(f"href='{url}'", f"href='{url}/'")
                    # Also replace exact user request: from ">" to "/>" if it's missing trailing slash.
                    # Wait, the user specifically says: from `/>` to `/>`.
                    # I'll just fix the url first.
                    if new_tag != full_tag:
                        return new_tag
            return full_tag
            
        new_content = link_pattern.sub(replacer, content)
        
        # User requested to change:
        # <link rel="canonical" href="https://deirdrekuvaas.com/[page-path]"/>
        # To: <link rel="canonical" href="https://deirdrekuvaas.com/[page-path]/"/>
        # Let's also ensure they are properly self-closed if the user specifically asked for `/>` format.
        # But wait, changing the format entirely might break other attributes. Just fixing the URL is usually enough.
        # Let's do a post-pass to enforce the self-closing slash if it's canonical.
        def enforce_slash(match):
            tag = match.group(1)
            if 'rel="canonical"' in tag.lower():
                if not tag.endswith('/>'):
                    # Change > to />
                    tag = tag[:-1].rstrip() + '/>'
            return tag
            
        link_pattern2 = re.compile(r'(<link\s+[^>]*rel=["\']canonical["\'][^>]*>)', re.IGNORECASE)
        new_content2 = link_pattern2.sub(enforce_slash, new_content)

        if new_content2 != content:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content2)
            updated_count += 1
            print(f"Updated {filepath}")

if __name__ == '__main__':
    main()
