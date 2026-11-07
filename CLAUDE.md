# deirdrekuvaas.com — Inner World Counseling

Hand-authored static HTML. Netlify + GitHub, no build step.
Repo: inner-world-counseling/inner-world-marketing

## Read first
`docs/repo-audit.md` — file inventory, page map, routing, open items.
Reconcile its KNOWN OPEN ITEMS list as the final step of any change.

## Hard constraints
- Publish dir is the repo root. Anything committed is served publicly at
  https://deirdrekuvaas.com/<path>. Never commit scripts, notes, tooling,
  or credentials to root. Sole exception: `scripts/indexnow.py` (see
  IndexNow below); it holds no secrets.
- Never alter license numbers, NPI, credentials, practitioner name, or any
  factual qualification claim. Stop and flag instead.
- Never invent or enrich factual data. Correct structure only.
- No one-off mutation scripts. 52 were deleted for causing header/footer
  drift. Tooling goes in a temp dir, never committed.
- Trailing slashes on all internal links, canonicals, and sitemap entries.
- No catch-all splat in netlify.toml. Netlify Pretty URLs handles trailing
  slashes natively; a splat rule cannot add or remove them and will loop.
- Header/footer are duplicated across ~29 pages, not templated, and have
  known drift. Changing one means verifying all.
- Parse HTML, do not grep. A grep for `FAQPage` hits microdata `itemtype`
  attributes and will be mistaken for JSON-LD coverage.
- Any PR that changes a page's content (visible text, title, metas or
  JSON-LD) also updates that page's `<lastmod>` in sitemap.xml to the
  change date (YYYY-MM-DD, America/Chicago). That edit to the protected
  sitemap.xml is pre-authorized; shared CSS/JS, `?v=` strings and
  sitewide header/footer markup do not count as content. Exception: a
  metadata-only correction that aligns a page's JSON-LD `dateModified`
  with its existing `<lastmod>` does not bump `<lastmod>` (bumping it
  would recreate the mismatch the correction removes).

## IndexNow
After any merged content change is live, run
`python scripts/indexnow.py <url> ...` (or `-f <file>`) with the changed
URLs: the same list as that PR's sitemap `<lastmod>` bumps, as full
https://deirdrekuvaas.com URLs with trailing slashes. Pre-authorized; no
owner approval needed. HTTP 200 or 202 means accepted. The key file
`/8a3604932ad6138ccbebee3818d3475f.txt` at the repo root must stay served as plain text
containing only the key; do not move, rename or redirect it.

## Verification bar
Any change touching HTML or JSON-LD must confirm before completion:
- All JSON-LD blocks parse; zero duplicate keys
- License/NPI/credential strings byte-identical to a pre-change snapshot
- Rendered text diff shows zero differences unless a copy change was requested
- Protected files unchanged: sitemap.xml, llms.txt, robots.txt, _headers,
  netlify.toml, _redirects, 404.html

## Workflow
Branch, PR, review diff, merge. Never push to main directly.
