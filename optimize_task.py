import os
import re

def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # SimplePractice widget check:
    # Ensure it has defer or async.
    content = re.sub(
        r'(<script[^>]*src="https://widget-cdn\.simplepractice\.com/[^"]*"[^>]*>)',
        lambda m: m.group(1) if 'defer' in m.group(1) or 'async' in m.group(1) else m.group(1).replace('<script', '<script defer'),
        content
    )

    def process_img(m):
        img_tag = m.group(0)
        # Determine if it's a hero image.
        is_hero = 'hero' in img_tag.lower() or 'fetchpriority="high"' in img_tag or 'loading="eager"' in img_tag or 'deirdre-kuvaas-trauma-specialist' in img_tag
        
        if is_hero:
            # Remove loading="lazy" if present
            img_tag = re.sub(r"""\s+loading=["']lazy["']""", '', img_tag)
            # Add loading="eager" if not present
            if 'loading="eager"' not in img_tag and 'loading=' not in img_tag:
                img_tag = img_tag.replace('<img ', '<img loading="eager" ')
            # Add fetchpriority="high" if not present
            if 'fetchpriority="high"' not in img_tag:
                img_tag = img_tag.replace('<img ', '<img fetchpriority="high" ')
        else:
            # Not a hero image, ensure loading="lazy"
            if 'loading=' not in img_tag:
                img_tag = img_tag.replace('<img ', '<img loading="lazy" ')
            elif 'loading="eager"' in img_tag:
                # If it's explicitly eager but not identified as hero, we shouldn't change it unless we are sure it's not hero. 
                pass
        return img_tag

    # Update images
    content = re.sub(r'<img\s+[^>]+>', process_img, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def process_css_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for font-display: swap; in @font-face
    def add_font_display(m):
        block = m.group(1)
        if 'font-display' not in block:
            block = block.rstrip()
            if not block.endswith(';'):
                block += ';'
            block += ' font-display: swap;'
        return f'@font-face {{{block}}}'

    content = re.sub(r'@font-face\s*\{([^}]+)\}', add_font_display, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    for root, dirs, files in os.walk('.'):
        if '.git' in root or 'node_modules' in root or '.netlify' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                process_html_file(os.path.join(root, file))
            elif file.endswith('.css'):
                process_css_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
