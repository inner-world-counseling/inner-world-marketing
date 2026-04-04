import os, glob, re

banner_unsplash = "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?w=1600&q=80"
new_banner = "/images/hero-banner-leaves.webp"
banner_aria = 'role="img" aria-label="Lush green leaves macro shot representing growth and mental wellness." loading="eager" fetchpriority="high"'

for filepath in glob.glob('**/*.html', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Replace the hero/banner background image
    if banner_unsplash in content:
        # We need to inject the role, aria-label, loading, and fetchpriority into the tag.
        # Find the tag containing the background-image style.
        # It's usually <section class="page-banner" style="..."> or <div class="page-banner" style="..."> or <section class="hero" style="...">
        
        # Simple replacement for the URL first
        content = content.replace(banner_unsplash, new_banner)
        
        # Then we find style="background-image: url('/images/hero-banner-leaves.webp');" and add attributes after it
        style_str = 'style="background-image: url(\'/images/hero-banner-leaves.webp\');"'
        if style_str in content:
            new_style_str = style_str + ' ' + banner_aria
            content = content.replace(style_str, new_style_str)
            
        style_str_2 = 'style="background-image:url(\'/images/hero-banner-leaves.webp\');"' # no space
        if style_str_2 in content:
            new_style_str_2 = style_str_2 + ' ' + banner_aria
            content = content.replace(style_str_2, new_style_str_2)

    # 4. About Page
    if 'about/index.html' in filepath:
        # main profile image
        content = content.replace('/images/deirdre-kuvaas.jpg', '/images/deirdre-kuvaas-headshot.webp')
        # update alt text
        content = content.replace('alt="Deirdre Kuvaas, LPCC, LADC, LCMHC — Telehealth Therapist"', 'alt="Deirdre Kuvaas, LPCC, LADC, LCMHC - Telehealth Trauma Specialist."')
        
    # Meta tag images (all pages)
    content = content.replace('https://deirdrekuvaas.com/images/deirdre-kuvaas.jpg', 'https://deirdrekuvaas.com/images/deirdre-kuvaas-headshot.webp')
    
    # Deirdre image src everywhere else (like index.html)
    content = content.replace('/images/deirdre-kuvaas.jpg', '/images/deirdre-kuvaas-headshot.webp')

    # index.html specifics
    if filepath == 'index.html':
        content = content.replace('alt="Deirdre Kuvaas, LPCC - Trauma and Anxiety Therapist providing EMDR or CPT telehealth in ND, MN, OH, and UT."', 'alt="Deirdre Kuvaas, LPCC, LADC, LCMHC - Telehealth Trauma Specialist."')
        
        # Replace Meditation and Mindfulness sections.
        # Wait, earlier we couldn't find "Mindfulness" or "Meditation" in index.html.
        # Let's check the images:
        # L361: <img src="https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&q=80"
        # L369: <div class="split-section__image" style="background-image: url('https://d2xsxph8kpxj0f.cloudfront.net/310519663414304285/KN4599JhbwugePYZSyhEUq/survival-habits-therapeutic_65a5371c.jpg');"

    if original != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

