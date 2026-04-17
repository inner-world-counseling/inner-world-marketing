import re
import os

files = [
    "index.html",
    "about/index.html",
    "emdr/index.html",
    "counseling-for-trauma/index.html",
    "ptsd/index.html",
    "individual-therapy/index.html",
    "north-dakota-telehealth-therapy/index.html",
    "minnesota-telehealth-therapy/index.html",
    "people-pleasing/index.html",
    "mental-health-links/index.html",
    "your-people-pleasing-side-hustle-is-actually-traumas-full-time-job/index.html",
    "the-big-myth-do-i-have-to-talk-about-trauma-to-heal-it/index.html",
    "im-an-empath-and-other-lies-we-tell-ourselves-to-avoid-boundaries/index.html"
]

for f in files:
    path = os.path.join("/opt/build/repo", f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            c = file.read()
            title = re.search(r'<title>.*?</title>', c, re.IGNORECASE|re.DOTALL)
            desc = re.search(r'<meta[^>]+name="description"[^>]*>', c, re.IGNORECASE)
            print(f"--- {f} ---")
            print("Title:", title.group(0).strip() if title else "None")
            print("Desc:", desc.group(0).strip() if desc else "None")

