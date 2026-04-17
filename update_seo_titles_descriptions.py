import re
import os

updates = {
    "index.html": {
        "title": "Trauma Therapy & EMDR | North Dakota & Minnesota",
        "description": "Specialized online trauma therapy and EMDR for high-functioning professionals. Heal from anxiety, PTSD, and people-pleasing with Deirdre Kuvaas, LPCC. Free consult."
    },
    "about/index.html": {
        "title": "Deirdre Kuvaas, LPCC | Trauma & EMDR Therapist",
        "description": "Meet Deirdre Kuvaas, LPCC — trauma therapist specializing in EMDR and CPT for high-functioning adults in ND, MN & UT. NPI: 1881112399. Book a consult."
    },
    "emdr/index.html": {
        "title": "EMDR Therapy North Dakota & Minnesota | Online EMDR",
        "description": "Online EMDR therapy for adults in ND & MN. Process trauma, anxiety, and perfectionism via secure telehealth with Deirdre Kuvaas, LPCC. Free 15-min consult."
    },
    "counseling-for-trauma/index.html": {
        "title": "Trauma Therapy North Dakota & Minnesota | EMDR & CPT",
        "description": "Evidence-based trauma therapy for high-functioning adults in ND & MN. Heal the root of burnout and anxiety with specialized EMDR & CPT. Start your journey."
    },
    "ptsd/index.html": {
        "title": "PTSD Treatment Adults | EMDR & CPT Online",
        "description": None
    },
    "individual-therapy/index.html": {
        "title": "Individual Therapy | High-Functioning Adults ND MN",
        "description": "Individual therapy for high-functioning adults in ND, MN & UT. Address burnout, anxiety, and perfectionism with Deirdre Kuvaas, LPCC. Book a consult."
    },
    "north-dakota-telehealth-therapy/index.html": {
        "title": "Online Therapy North Dakota | EMDR & Trauma Therapy",
        "description": "Licensed online trauma therapy for adults throughout North Dakota. Serving Fargo, Bismarck, and Grand Forks via secure telehealth. Free 15-minute consultation."
    },
    "minnesota-telehealth-therapy/index.html": {
        "title": "Online Trauma Therapy Minnesota | EMDR & CPT Telehealth",
        "description": "Online trauma therapy for Minnesota adults. EMDR and CPT via telehealth — serving Minneapolis, St. Paul, Duluth, Rochester and beyond. Free consultation."
    },
    "people-pleasing/index.html": {
        "title": "Fawn Response & People Pleasing Therapy | ND & MN",
        "description": "Stop over-functioning and start living for yourself. Specialized therapy for the fawn response and boundaries in ND and MN. Free consultation with Deirdre Kuvaas."
    },
    "mental-health-links/index.html": {
        "title": None,
        "description": "Curated mental health resources covering anxiety, PTSD, addiction, and more. Compiled by Deirdre Kuvaas, LPCC for clients in ND, MN and UT."
    }
}

blog_posts = [
    "your-people-pleasing-side-hustle-is-actually-traumas-full-time-job/index.html",
    "the-big-myth-do-i-have-to-talk-about-trauma-to-heal-it/index.html",
    "im-an-empath-and-other-lies-we-tell-ourselves-to-avoid-boundaries/index.html"
]

def update_file(filepath, title_new, desc_new, is_blog=False):
    fullpath = os.path.join("/opt/build/repo", filepath)
    if not os.path.exists(fullpath):
        print(f"File not found: {fullpath}")
        return

    with open(fullpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    if is_blog:
        # Just remove " - Inner World Counseling Services" from the <title>
        # Only in the main title tag, not og:title or twitter:title
        content = re.sub(r'(<title>.*?)( - Inner World Counseling Services)(.*?</title>)', r'\1\3', content, count=1, flags=re.IGNORECASE|re.DOTALL)
    else:
        if title_new is not None:
            content = re.sub(r'<title>.*?</title>', f'<title>{title_new}</title>', content, count=1, flags=re.IGNORECASE|re.DOTALL)
        if desc_new is not None:
            # We must be careful not to match og:description or twitter:description.
            # We look for <meta ... name="description" ...> or <meta name="description" ...>
            # A safe way is to replace the content attribute inside the tag that has name="description".
            
            def replace_meta_desc(match):
                tag = match.group(0)
                # replace the content="old" with content="new"
                # using a regex to find content="..." inside this specific tag
                new_tag = re.sub(r'content="[^"]*"', f'content="{desc_new}"', tag)
                return new_tag

            content = re.sub(r'<meta[^>]+name="description"[^>]*>', replace_meta_desc, content, count=1, flags=re.IGNORECASE)
            # handle case where name and content are swapped: <meta content="..." name="description" />
            
    if content != original_content:
        with open(fullpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes made to: {filepath} (Maybe already updated?)")

for filepath, data in updates.items():
    update_file(filepath, data['title'], data['description'])

for filepath in blog_posts:
    update_file(filepath, None, None, is_blog=True)

