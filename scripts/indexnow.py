"""Submit changed deirdrekuvaas.com URLs to IndexNow (Bing, Yandex and others).

Usage:
  python scripts/indexnow.py https://deirdrekuvaas.com/ https://deirdrekuvaas.com/faqs/
  python scripts/indexnow.py -f urls.txt      (one URL per line; blank lines and # comments ignored)

Run after a content change is merged and live, with the same URLs whose
<lastmod> was bumped in sitemap.xml. Prints the HTTP status: 200 or 202 means
accepted. The key is public by design; it is served at KEY_LOCATION.
"""
import json
import sys
import urllib.error
import urllib.parse
import urllib.request

HOST = "deirdrekuvaas.com"
KEY = "8a3604932ad6138ccbebee3818d3475f"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"


def read_urls(argv):
    if argv[:1] == ["-f"]:
        if len(argv) != 2:
            sys.exit("usage: indexnow.py -f FILE")
        with open(argv[1], encoding="utf-8") as fh:
            lines = [ln.strip() for ln in fh]
        return [ln for ln in lines if ln and not ln.startswith("#")]
    return argv


def main(argv):
    urls = read_urls(argv)
    if not urls:
        sys.exit(__doc__)
    bad = [u for u in urls if urllib.parse.urlsplit(u).scheme != "https" or urllib.parse.urlsplit(u).hostname != HOST]
    if bad:
        sys.exit("not https://" + HOST + " URLs: " + ", ".join(bad))
    urls = list(dict.fromkeys(urls))
    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": KEY_LOCATION, "urlList": urls}).encode("utf-8")
    req = urllib.request.Request(ENDPOINT, data=body, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.status
    except urllib.error.HTTPError as err:
        status = err.code
    print(f"IndexNow: HTTP {status} for {len(urls)} URL(s)")
    return 0 if status in (200, 202) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
