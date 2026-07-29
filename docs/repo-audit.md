# Repository Audit & Context Record

## 1. PURPOSE

This file is the standing context for future agent runs and should be read first in every prompt to ensure complete architectural alignment, preserve site routing conventions, and maintain accurate knowledge of open technical debt.

## 2. FILE INVENTORY

### Root Directory Files
- `.gitignore`: Specifies files and patterns ignored by Git version control. (Flag: repository configuration; not part of the rendered site).
- `404.html`: Custom 404 error page served by Netlify for unmapped URL requests. (Flag: error response handler; not part of the standard rendered site).
- `README.md`: Repository overview and instructions. (Flag: project documentation; not part of the rendered site).
- `_headers`: Netlify HTTP response headers configuration file defining caching and security rules. (Flag: platform configuration; not part of the rendered site).
- `_redirects`: Netlify URL redirection rules for path aliases and legacy URLs. (Flag: platform configuration; not part of the rendered site).
- `favicon.ico`: Standard favicon image asset in ICO format.
- `favicon.png`: High-resolution favicon image asset in PNG format.
- `index.html`: Main website homepage.
- `llms.txt`: Machine-readable repository reference file for AI and LLM tooling. (Flag: meta documentation; not part of the rendered site).
- `netlify.toml`: Netlify configuration file for build options and feature flags. (Flag: platform configuration; not part of the rendered site).
- `robots.txt`: Search engine web crawler instructions file. (Flag: crawler directive; not rendered HTML content).
- `sitemap.xml`: Search engine XML sitemap containing canonical URLs. (Flag: XML metadata; not rendered HTML content).

### Grouped Subdirectory Files
- `about/`
  - `index.html`: Bio and qualifications page for Deirdre Kuvaas, LPCC.
- `appointment-request/`
  - `index.html`: Appointment request and intake page.
- `assets/`
  - `privacy-practices-2.pdf`: PDF document containing Notice of Privacy Practices.
- `blog/`
  - `index.html`: Main blog listing page.
  - `posts.json`: Structured JSON file containing blog post listings and metadata.
- `client-forms/`
  - `index.html`: Legacy redirect stub page for client forms.
- `cognitive-processing-therapy/`
  - `index.html`: Specialty page for Cognitive Processing Therapy (CPT).
- `contact/`
  - `index.html`: Contact information and inquiry page.
- `counseling-for-anxiety/`
  - `index.html`: Specialty page for anxiety counseling.
- `counseling-for-trauma/`
  - `index.html`: Specialty page for trauma counseling.
- `css/`
  - `style.css`: Primary global CSS stylesheet.
- `emdr/`
  - `index.html`: Specialty page for EMDR therapy.
- `faqs/`
  - `index.html`: Frequently asked questions page.
- `fonts/`
  - `satisfy-regular.woff2`: WOFF2 web font asset for accent script typography.
  - `work-sans-300.woff2`: WOFF2 web font asset (Light).
  - `work-sans-400.woff2`: WOFF2 web font asset (Regular).
  - `work-sans-500.woff2`: WOFF2 web font asset (Medium).
  - `work-sans-600.woff2`: WOFF2 web font asset (Semi-Bold).
  - `work-sans-latin-ext.woff2`: WOFF2 web font asset subset.
  - `work-sans-latin.woff2`: WOFF2 web font asset subset.
  - `work-sans-vietnamese.woff2`: WOFF2 web font asset subset.
- `im-an-empath-and-other-lies-we-tell-ourselves-to-avoid-boundaries/`
  - `index.html`: Blog article post on boundaries and empath identification.
- `images/`
  - `android-chrome-512x512.png`: Web application icon asset.
  - `deirdre-kuvaas-headshot.webp`: Headshot photograph of Deirdre Kuvaas.
  - `deirdre-kuvaas-trauma-specialist-mn-oh-ut.webp`: Hero and bio section image asset.
  - `deirdre-kuvaas.jpg`: Legacy headshot photo asset.
  - `hero-banner-leaves.webp`: Decorative background banner graphic.
  - `inner-world-counseling-logo-secondary.png`: Secondary practice logo image.
  - `inner-world-counseling-logo.png`: Primary practice logo image.
  - `meditation-practice.webp`: Content topic graphic asset.
  - `online-therapy-north-dakota-deirdre-kuvaas.webp`: Regional content photo asset.
  - `roots-of-healing.webp`: Content topic graphic asset.
  - `tranquil-trees-nature.webp`: Decorative background graphic asset.
- `individual-therapy/`
  - `index.html`: Specialty page for individual adult therapy.
- `js/`
  - `main.js`: Main client-side script for mobile navigation, header scroll styles, footer copyright year, and FAQ toggles.
- `mental-health-links/`
  - `index.html`: Crisis resources and mental health directory page.
- `minnesota-telehealth-therapy/`
  - `index.html`: Minnesota state telehealth landing page.
- `nervous-system-regulation-for-high-achievers/`
  - `index.html`: Blog article post on nervous system regulation.
- `north-dakota-telehealth-therapy/`
  - `index.html`: North Dakota state telehealth landing page.
- `ohio-telehealth-therapy/`
  - `index.html`: Ohio state telehealth landing page.
- `people-pleasing/`
  - `index.html`: Specialty page for fawn response and people-pleasing counseling.
- `personal-addiction-counseling/`
  - `index.html`: Specialty page for addiction counseling and LADC support.
- `privacy/`
  - `index.html`: Privacy policy page.
- `ptsd/`
  - `index.html`: Specialty page for PTSD treatment.
- `rates-insurance/`
  - `index.html`: Rates, fees, and insurance information page.
- `services/`
  - `index.html`: Comprehensive therapy services directory page.
- `staff/staff-1/`
  - `index.html`: Legacy redirect stub page for staff bio.
- `telehealth/`
  - `index.html`: Telehealth information page.
- `terms/`
  - `index.html`: Terms of service page.
- `the-big-myth-do-i-have-to-talk-about-trauma-to-heal-it/`
  - `index.html`: Blog article post on trauma healing.
- `utah-telehealth-therapy/`
  - `index.html`: Utah state telehealth landing page.
- `your-people-pleasing-side-hustle-is-actually-traumas-full-time-job/`
  - `index.html`: Blog article post on trauma and people-pleasing.

## 3. PAGE MAP

### HTML Pages (`index.html`)

| URL Path | `<title>` | Canonical URL | JSON-LD? |
| :--- | :--- | :--- | :---: |
| `/` | Trauma Therapy & EMDR \| North Dakota & Minnesota | `https://deirdrekuvaas.com/` | Yes |
| `/about/` | Deirdre Kuvaas, LPCC \| Trauma & EMDR Therapist | `https://deirdrekuvaas.com/about/` | Yes |
| `/appointment-request/` | Appointment Request \| Inner World Counseling | `https://deirdrekuvaas.com/appointment-request/` | Yes |
| `/blog/` | Therapy & Mental Health Blog \| ND, MN, UT | `https://deirdrekuvaas.com/blog/` | Yes |
| `/client-forms/` | Redirecting... | `https://deirdrekuvaas.com/` | No |
| `/cognitive-processing-therapy/` | CPT for Trauma &amp; Stuck Points \| ND, MN, UT | `https://deirdrekuvaas.com/cognitive-processing-therapy/` | Yes |
| `/contact/` | Contact Inner World Counseling \| ND, MN, UT | `https://deirdrekuvaas.com/contact/` | Yes |
| `/counseling-for-anxiety/` | High-Functioning Anxiety Therapy Online \| Professionals | `https://deirdrekuvaas.com/counseling-for-anxiety/` | Yes |
| `/counseling-for-trauma/` | Trauma Therapy North Dakota & Minnesota \| EMDR & CPT | `https://deirdrekuvaas.com/counseling-for-trauma/` | Yes |
| `/emdr/` | EMDR Therapy North Dakota & Minnesota \| Online EMDR | `https://deirdrekuvaas.com/emdr/` | Yes |
| `/faqs/` | Therapy FAQs \| Insurance &amp; Virtual Sessions \| ND, MN, UT | `https://deirdrekuvaas.com/faqs/` | Yes |
| `/im-an-empath-and-other-lies-we-tell-ourselves-to-avoid-boundaries/` | “I’m an Empath” (and Other Lies We Tell Ourselves to Avoid Boundaries) | `https://deirdrekuvaas.com/im-an-empath-and-other-lies-we-tell-ourselves-to-avoid-boundaries/` | Yes |
| `/individual-therapy/` | Individual Therapy \| High-Functioning Adults ND MN | `https://deirdrekuvaas.com/individual-therapy/` | Yes |
| `/mental-health-links/` | Mental Health Links \| Inner World Counseling | `https://deirdrekuvaas.com/mental-health-links/` | Yes |
| `/minnesota-telehealth-therapy/` | Online EMDR Therapist Minnesota \| Virtual Trauma Therapy | `https://deirdrekuvaas.com/minnesota-telehealth-therapy/` | Yes |
| `/nervous-system-regulation-for-high-achievers/` | Nervous System Regulation for High Achievers: Your Window of Tolerance \| Inner World Counseling | `https://deirdrekuvaas.com/nervous-system-regulation-for-high-achievers/` | Yes |
| `/north-dakota-telehealth-therapy/` | Online Therapy North Dakota \| EMDR & Trauma Therapy | `https://deirdrekuvaas.com/north-dakota-telehealth-therapy/` | Yes |
| `/ohio-telehealth-therapy/` | Online Therapy in Ohio \| Inner World Counseling Services | `https://deirdrekuvaas.com/ohio-telehealth-therapy/` | Yes |
| `/people-pleasing/` | Fawn Response & People Pleasing Therapy \| ND & MN | `https://deirdrekuvaas.com/people-pleasing/` | Yes |
| `/personal-addiction-counseling/` | High-Functioning Addiction Counseling &amp; LADC Support | `https://deirdrekuvaas.com/personal-addiction-counseling/` | Yes |
| `/privacy/` | Privacy Policy \| Inner World Counseling | `https://deirdrekuvaas.com/privacy/` | Yes |
| `/ptsd/` | PTSD Treatment Adults \| EMDR & CPT Online | `https://deirdrekuvaas.com/ptsd/` | Yes |
| `/rates-insurance/` | Rates & Insurance \| Therapy in ND, MN, OH, UT | `https://deirdrekuvaas.com/rates-insurance/` | Yes |
| `/services/` | Services \| North Dakota, Minnesota, Ohio &amp; Utah Therapy | `https://deirdrekuvaas.com/services/` | Yes |
| `/staff/staff-1/` | Redirecting... | `https://deirdrekuvaas.com/` | No |
| `/telehealth/` | Telehealth Therapy \| Virtual Counseling \| ND, MN, UT | `https://deirdrekuvaas.com/telehealth/` | Yes |
| `/terms/` | Terms of Service \| Inner World Counseling | `https://deirdrekuvaas.com/terms/` | Yes |
| `/the-big-myth-do-i-have-to-talk-about-trauma-to-heal-it/` | The Big Myth: Do I Have to Talk About Trauma to Heal It? | `https://deirdrekuvaas.com/the-big-myth-do-i-have-to-talk-about-trauma-to-heal-it/` | Yes |
| `/utah-telehealth-therapy/` | Online Therapy in Utah \| Inner World Counseling Services | `https://deirdrekuvaas.com/utah-telehealth-therapy/` | Yes |
| `/your-people-pleasing-side-hustle-is-actually-traumas-full-time-job/` | Your People-Pleasing Side Hustle is Actually Trauma’s Full-Time Job | `https://deirdrekuvaas.com/your-people-pleasing-side-hustle-is-actually-traumas-full-time-job/` | Yes |

### Custom Error Page (`404.html`)

- **URL Path**: `/404.html`
- **Title**: `Page Not Found | Inner World Counseling Services`
- **Canonical URL**: None (no canonical tag present)
- **JSON-LD**: No
- **Indexing Directives**: Carries `<meta name="robots" content="noindex">` tag and `X-Robots-Tag: noindex` in `_headers`
- **Sitemap Inclusion**: Excluded from `sitemap.xml` by design

## 4. ROUTING

### Redirection Rules (`_redirects`)

```
# Every target below is a FINAL URL (trailing slash included) so each request
# resolves in a single hop. Trailing slashes are supplied by Netlify's Pretty
# URLs feature, not by a redirect rule — see netlify.toml.

/privacy.html  /privacy/  301
/terms.html    /terms/    301
/privacy  /privacy/  301
/terms    /terms/    301
/who-i-help  /services/  301

# State landing page aliases (old slugs -> new slugs)
/north-dakota-therapy  /north-dakota-telehealth-therapy/  301
/minnesota-therapy  /minnesota-telehealth-therapy/  301
/ohio-therapy  /ohio-telehealth-therapy/  301
/utah-therapy  /utah-telehealth-therapy/  301
/nd-therapy  /north-dakota-telehealth-therapy/  301
/mn-therapy  /minnesota-telehealth-therapy/  301
/oh-therapy  /ohio-telehealth-therapy/  301
/ut-therapy  /utah-telehealth-therapy/  301
/cognitive-behavioral-therapy /cognitive-processing-therapy/ 301
```

### Netlify Configuration (`netlify.toml`)

```toml
# No catch-all trailing-slash redirect here — on purpose.
#
# A `from = "/*"` -> `to = "/:splat/"` rule cannot work on Netlify and loops:
# the CDN normalizes trailing slashes BEFORE redirect rules are evaluated, so
# "/about" and "/about/" match the same rule, and the rule's own output
# re-matches it forever. Netlify's docs state this directly: "You cannot use a
# redirect rule to add or remove a trailing slash."
#
# Trailing slashes are added by Netlify's Pretty URLs feature, which is enabled
# by default and forwards "/about" to "/about/" without any rule.
#
# Project configuration > Build & deploy > Post processing > Pretty URLs
```

The catch-all trailing-slash redirect rule was deliberately removed because Netlify's Pretty URLs handles trailing slashes natively and a splat rule cannot add or remove them.

## 5. CONVENTIONS

- **Trailing Slashes**: Enforced on all internal links, canonical URLs, and `sitemap.xml` entries.
- **Header and Footer Duplication**: Shared `<header>` and `<footer>` markup is duplicated across 29 page files directly instead of using a component template engine.

## 6. KNOWN OPEN ITEMS

- [ ] Publish directory is the repo root; every committed file is public. Partially mitigated: `_redirects` now returns a forced 404 for `/CLAUDE.md`, `/README.md`, and `/docs/*`. Any future non-content file added to the root will be public unless a rule is added for it.
- [ ] Header/footer duplicated across 29 pages, with known drift between copies — **assessed 2026-07-28**, drift characterised by parsing all 29 copies (2 further files, `client-forms/` and `staff/staff-1/`, are 387-byte redirect stubs with no header/footer and were excluded). Headers: 3 distinct link-sets across 10 markup variants; footers: 2 link-sets across 3 markup variants. **Link graph verified even**: all 24 distinct header hrefs and all 18 distinct footer hrefs are now present on 29/29 pages. Nothing links to `/who-i-help`; all 29 use `/services/`, so that `_redirects` rule is legacy-only. **One missing link found and fixed**: `index.html`'s footer omitted `/ohio-telehealth-therapy/` while its own header and licensure sentence both still referenced Ohio; restored using the long-form label `Telehealth in Ohio` already used by that page's header. Also fixed: `404.html` carried `main-nav__link--active` on `/about/`, inherited from `about/index.html`; removed, so no nav item is active on the 404. Remaining differences are **classified cosmetic and deliberately deprioritised** — per-page `main-nav__link--active` placement (correct by design on the other 28), inline `style` vs `extracted-style-NN` classes in `index.html`'s footer, and `fetchpriority`/`loading` on the homepage logo. Remaining **substantive but low-value** differences, left alone by decision: state-page anchor text long-form on 5 pages (`404`, `about`, `index`, `privacy`, `terms`) vs short-form on 24; `faqs` and `services` carry two extra `/services/` dropdown entries ("Treatment Approaches" plus a duplicate "Who I Help", so `/services/` appears 3x) and order Resources before Areas Served; those same two pages use straight quotes in `"The Roots" (Trauma)` where 27 use curly; logo `alt` text has a long and short form on the same 5-page cohort as the state labels; `nervous-system-regulation-for-high-achievers` drops the Psychology Today `aria-label` and the "GoodTherapy Verified Seal" / "EMDRIA Member Link" strings. The underlying duplication is unchanged — there is still no template, so every future header/footer edit must be applied to all 29 copies.
- [x] Schema: "telecom" used instead of "telephone" — resolved. Renamed across 24 pages; the 4 state landing pages carried a redundant `telecom` block alongside an already-correct `telephone` string and had that block deleted outright. Zero occurrences remain repo-wide.
- [x] Schema: `telephone` held a `ContactPoint` object where schema.org expects Text — resolved. Flattened to a bare string on all 28 `MedicalBusiness` nodes; the `ContactPoint` wrapper and `contactType` were dropped as they add nothing for a solo practitioner.
- [x] Schema: orphan FAQ microdata with no parent FAQPage scope — **fully resolved**. Earlier pass fixed `/`, `/people-pleasing/`, and `/telehealth/`, where a valid FAQPage block already existed in JSON-LD and the dead microdata attributes were stripped so JSON-LD is the single source. Resolved 2026-07-28 on `/ohio-telehealth-therapy/` and `/utah-telehealth-therapy/`, which had orphan Question/Answer microdata **and** no FAQPage in JSON-LD: FAQPage JSON-LD was authored first, verified byte-identical to the existing visible text while the microdata was still in place, and only then were the microdata attributes stripped — so the FAQ content was never absent from structured data. Each page gained a FAQPage node appended as the 6th member of its existing single `@graph` (2 questions each), carrying `@id` `https://deirdrekuvaas.com/<page>/#faq`. Note this follows the `/individual-therapy/` convention; the other 10 FAQPage nodes site-wide omit `@id` entirely, so `@id` usage remains inconsistent — see the FAQPage conventions item below. Zero orphan Question/Answer microdata now remains repo-wide (parsed, not grepped).
- [ ] Schema: `/minnesota-telehealth-therapy/` and `/north-dakota-telehealth-therapy/` express their FAQs as correctly scoped FAQPage **microdata only**, with no JSON-LD equivalent. This is valid as-is and was deliberately left alone, but it is inconsistent with every other page on the site, which uses JSON-LD. Decide whether to convert these two for consistency. Note that a plain grep for `FAQPage` hits these files via `itemtype` attributes and can be mistaken for JSON-LD coverage — parse, do not grep. As of 2026-07-28 these two are the **only** remaining FAQ microdata in the repo; every other FAQ on the site is JSON-LD. Their microdata is correctly scoped and emits fine, so this is a consistency question, not a bug.
- [ ] Schema: FAQPage conventions are not uniform. 12 FAQPage nodes exist across 12 pages. Placement: 11 sit inside the page's `@graph`, 2 are standalone `<script>` blocks with their own `@context` (`/emdr/`, `/telehealth/`). `@id`: 9 omit it, 3 carry `https://deirdrekuvaas.com/<page>/#faq` (`/individual-therapy/`, `/ohio-telehealth-therapy/`, `/utah-telehealth-therapy/`). Node shape itself is uniform everywhere — `@type`/`name`/`acceptedAnswer` → `@type`/`text`, with no `mainEntityOfPage`, `isPartOf`, `url`, or `name`. Pick one `@id` convention and one placement convention and normalize; both current forms are valid, so this is cleanup rather than a correctness fix.
- [ ] Schema: `dateModified` values are current as of 2026-07-29 but remain hardcoded per page with no build-time automation, so they will drift stale again. Only `/` and `/nervous-system-regulation-for-high-achievers/` carry the property at all; it was deliberately not added elsewhere, since inventing a modification date is data fabrication rather than a structural fix.
- [ ] Schema: duplicate Service / MedicalTherapy nodes — **characterised 2026-07-29, recommend won't-fix.** 17 Service nodes across 13 pages, 2 MedicalTherapy nodes (both on `/`). Only two pages carry more than one such node. `/counseling-for-trauma/` has 3, but two are `hasPart` children of the first — correct composition, not duplication. `/` has 5: three `Service` (EMDR Therapy, CPT, Anxiety Counseling) and two `MedicalTherapy` (`#emdr-therapy`, `#cpt-therapy`). The EMDR and CPT pairs are the same modality expressed under two types, and the CPT pair shares an identical `name` string, which is likely what prompted this item. They are complementary rather than redundant: `Service` carries `provider` and `areaServed`; `MedicalTherapy` carries `relevantSpecialty` and is the target of two live `MedicalCondition.possibleTreatment` references on the same page. Deleting either side breaks something. **Zero true duplicates exist** — no page defines the same `@id` twice.
- [x] Schema: thin Person node — **mischaracterised; it was a normalization problem, resolved 2026-07-29**. The issue was not thinness but divergence: all 28 pages shared `@id` `https://deirdrekuvaas.com/#person` while carrying **6 different node shapes**, so any consumer merging by `@id` got conflicting data. `/ohio-telehealth-therapy/` was the worst — no `identifier` at all (therefore no NPI) and no `memberOf`. Normalized to one canonical node, assembled only from facts already published in the repo: `honorificSuffix` `LPCC`; all five `identifier` entries (NPI plus ND/MN/OH/UT licence numbers); `hasCredential` for LPCC, LCMHC and EMDR Trained Professional; `alumniOf` University of Mary and East Stroudsburg University of Pennsylvania (institution names only, no degrees or dates); plus the pre-existing `memberOf`, `knowsAbout`, `sameAs`, `worksFor`. Two facts were promoted from visible text into JSON-LD where they had not previously been structured: Ohio licence `E.2404393` (visible on `/ohio-telehealth-therapy/` only) and the two institutions (visible on `/about/` only). This is relocation of already-published data, not invention. `EMDR Trained Professional` was **moved** from `MedicalBusiness.hasCredential` to `Person.hasCredential` — a person holds training, a business does not — and removed from the Organization node in the same commit; it now appears on 28 Person nodes and 0 MedicalBusiness nodes. Result is **2 shapes, not 1**, solely because of the LADC hold below; the 25 non-LADC pages are byte-identical to each other and the 3 LADC pages differ by exactly one `hasCredential` entry.
- [ ] **Credential: LADC status needs human verification before it propagates.** `/about/`, `/privacy/` and `/terms/` claim `Licensed Alcohol and Drug Counselor (LADC)` in `Person.hasCredential`, and `/about/` and `/personal-addiction-counseling/` claim it in visible text. **No LADC licence number exists anywhere in the repo**, while all four other licences (ND LPCC, MN LPCC, OH LPCC, UT LCMHC) have theirs. `/about/` states it is a Minnesota credential. Deliberately excluded from the canonical Person node on 2026-07-29 and deliberately **not** removed from the 3 pages that already carry it — held pending confirmation of current status. Once confirmed, either add it to the canonical node with its licence number or remove it from those 3 pages; do not leave it in this split state indefinitely.
- [ ] **`sameAs` contains one unverifiable URL.** `https://www.linkedin.com/in/deirdre-kuvaas` is asserted in `Person.sameAs` on all 28 pages but is linked from no markup anywhere on the site — every other `sameAs` target is also a real footer link. Attempted verification 2026-07-29 returned **HTTP 999** (LinkedIn's blanket anti-automation response) for both plain and browser-User-Agent requests; 999 is not a 404 and carries no information about whether the profile exists. Left in place because removing it on no evidence would delete an existing claim. Needs a human to open it in a browser. If it resolves, it should also be linked from the footer for consistency with the other four `sameAs` targets; if it does not, drop it from `sameAs` on all 28 pages.
- [ ] Schema: `#website` is referenced but not defined on four pages — `WebPage.isPartOf` points at `https://deirdrekuvaas.com/#website` on `/minnesota-`, `/north-dakota-`, `/ohio-` and `/utah-telehealth-therapy/`, but the `WebSite` node carrying that `@id` is defined only on `/`. Each page is an independent graph, so on those four the reference resolves to nothing. Fix by defining the `WebSite` node on those pages or dropping the `isPartOf`.
- [ ] _redirects: /privacy and /terms rules are inert no-ops and would create an infinite redirect if a ! were added
- [ ] _headers: X-Robots-Tag: all on /* is a no-op; "all" is already the default
- [ ] No dedicated Fargo-Moorhead metro page exists
