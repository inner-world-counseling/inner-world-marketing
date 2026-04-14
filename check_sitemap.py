import os
import xml.etree.ElementTree as ET

def main():
    repo_dir = '/opt/build/repo'
    sitemap_path = os.path.join(repo_dir, 'sitemap.xml')
    
    # Parse sitemap
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [url.find('ns:loc', namespace).text for url in root.findall('ns:url', namespace)]
    
    sitemap_paths = [url.replace('https://deirdrekuvaas.com', '') for url in urls]
    sitemap_paths = set(p if p != '' else '/' for p in sitemap_paths)
    
    # Find all HTML files
    html_files = []
    for r, d, f in os.walk(repo_dir):
        if '.git' in r or '.netlify' in r:
            continue
        for file in f:
            if file.endswith('.html'):
                rel_path = os.path.relpath(os.path.join(r, file), repo_dir)
                html_files.append(rel_path)
                
    missing = []
    for f in html_files:
        if f == 'index.html':
            url = '/'
        elif f.endswith('/index.html'):
            url = '/' + f[:-11]
        else:
            url = '/' + f  # e.g., /privacy.html
            
        if url not in sitemap_paths:
            # Let's also check if Netlify pretty URLs maps it to /filename (without extension)
            pretty_url = '/' + f[:-5] if f.endswith('.html') and not f.endswith('index.html') else url
            if pretty_url not in sitemap_paths:
                missing.append(f)
            else:
                # If the pretty url is in the sitemap, but wait! Does the sitemap point to the .html or the directory?
                # If there's ALSO an index.html, then this is a duplicate.
                dir_version = f[:-5] + '/index.html'
                if dir_version in html_files:
                    missing.append(f + " (duplicate of " + dir_version + ")")
                
    for m in sorted(missing):
        print(f"- {m}")

if __name__ == '__main__':
    main()
