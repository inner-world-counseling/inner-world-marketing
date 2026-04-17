import os
import glob

html_files = glob.glob('/opt/build/repo/**/*.html', recursive=True)
sitemap_file = '/opt/build/repo/sitemap.xml'

replacements = {
    'href="/im-an-empath-and-other-lies-we-tell-ourselves-to-avoid-boundaries"': 'href="/im-an-empath-and-other-lies-we-tell-ourselves-to-avoid-boundaries/"',
    'href="/the-big-myth-do-i-have-to-talk-about-trauma-to-heal-it"': 'href="/the-big-myth-do-i-have-to-talk-about-trauma-to-heal-it/"',
    'href="/your-people-pleasing-side-hustle-is-actually-traumas-full-time-job"': 'href="/your-people-pleasing-side-hustle-is-actually-traumas-full-time-job/"'
}

sitemap_replacements = {
    '<loc>https://deirdrekuvaas.com/im-an-empath-and-other-lies-we-tell-ourselves-to-avoid-boundaries</loc>': '<loc>https://deirdrekuvaas.com/im-an-empath-and-other-lies-we-tell-ourselves-to-avoid-boundaries/</loc>',
    '<loc>https://deirdrekuvaas.com/the-big-myth-do-i-have-to-talk-about-trauma-to-heal-it</loc>': '<loc>https://deirdrekuvaas.com/the-big-myth-do-i-have-to-talk-about-trauma-to-heal-it/</loc>',
    '<loc>https://deirdrekuvaas.com/your-people-pleasing-side-hustle-is-actually-traumas-full-time-job</loc>': '<loc>https://deirdrekuvaas.com/your-people-pleasing-side-hustle-is-actually-traumas-full-time-job/</loc>'
}


modified_html_count = 0
for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for old, new in replacements.items():
            new_content = new_content.replace(old, new)
            
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            modified_html_count += 1
            print(f"Modified HTML: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

try:
    with open(sitemap_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = content
    for old, new in sitemap_replacements.items():
        new_content = new_content.replace(old, new)
        
    if content != new_content:
        with open(sitemap_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Modified Sitemap: {sitemap_file}")
    else:
        print(f"No changes needed for Sitemap: {sitemap_file}")
except Exception as e:
    print(f"Error processing {sitemap_file}: {e}")

print(f"Total HTML files modified: {modified_html_count}")
