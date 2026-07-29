# deirdrekuvaas.com — Inner World Counseling

Hand-authored static HTML. Netlify + GitHub, no build step.
Repo: inner-world-counseling/inner-world-marketing

## Read first
`docs/repo-audit.md` — file inventory, page map, routing, open items.
Reconcile its KNOWN OPEN ITEMS list as the final step of any change.

## Hard constraints
- Publish dir is the repo root. Anything committed is served publicly at
  https://deirdrekuvaas.com/<path>. Never commit scripts, notes, tooling,
  or credentials to root.
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

## Verification bar
Any change touching HTML or JSON-LD must confirm before completion:
- All JSON-LD blocks parse; zero duplicate keys
- License/NPI/credential strings byte-identical to a pre-change snapshot
- Rendered text diff shows zero differences unless a copy change was requested
- Protected files unchanged: sitemap.xml, llms.txt, robots.txt, _headers,
  netlify.toml, _redirects, 404.html

## Workflow
Branch, PR, review diff, merge. Never push to main directly.
