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
- [x] Schema: duplicate Service / MedicalTherapy nodes — **CLOSED WON'T-FIX 2026-07-29. Do not re-open without reading the reasoning below.** 17 Service nodes across 13 pages, 2 MedicalTherapy nodes (both on `/`). Only two pages carry more than one such node. `/counseling-for-trauma/` has 3, but two are `hasPart` children of the first — correct composition, not duplication. `/` has 5: three `Service` (EMDR Therapy, CPT, Anxiety Counseling) and two `MedicalTherapy` (`#emdr-therapy`, `#cpt-therapy`). The EMDR and CPT pairs are the same modality expressed under two types, and the CPT pair shares an identical `name` string, which is likely what prompted this item. They are complementary rather than redundant, and each is reachable through a different property path:
  - `Service` carries `provider` (→ `#organization`) and `areaServed` (the four states). It answers "what does this practice offer, and where".
  - `MedicalTherapy` carries `alternateName` and `relevantSpecialty`, and answers "what is this treatment clinically".
  - **The decisive point: `#emdr-therapy` and `#cpt-therapy` are the targets of live `MedicalCondition.possibleTreatment` references on the same page** — `Post-Traumatic Stress Disorder (PTSD)` → both, and `Anxiety Disorder` → `#cpt-therapy`. Deleting the `MedicalTherapy` nodes to remove the apparent duplication would leave three dangling references and strip the condition→treatment links entirely. Deleting the `Service` nodes instead would drop `provider` and `areaServed`, which nothing else on the page supplies.
  Neither side is removable. **Zero true duplicates exist** — no page defines the same `@id` twice, and no two nodes on any page are identical JSON. Schema.org permits an entity described under multiple types, neither type drives a rich result for a therapy practice, and the site is 29 hand-maintained copies with no template — so editing working structured data for an aesthetic concern is pure downside risk. The only real wart is that the `Service` and `MedicalTherapy` CPT nodes share the byte-identical `name` string `"Cognitive Processing Therapy (CPT)"`, which is what makes this look like a duplicate at a glance. It is not one.
- [x] Schema: thin Person node — **mischaracterised; it was a normalization problem, resolved 2026-07-29**. The issue was not thinness but divergence: all 28 pages shared `@id` `https://deirdrekuvaas.com/#person` while carrying **6 different node shapes**, so any consumer merging by `@id` got conflicting data. `/ohio-telehealth-therapy/` was the worst — no `identifier` at all (therefore no NPI) and no `memberOf`. Normalized to one canonical node, assembled only from facts already published in the repo: `honorificSuffix` `LPCC`; all five `identifier` entries (NPI plus ND/MN/OH/UT licence numbers); `hasCredential` for LPCC, LCMHC and EMDR Trained Professional; `alumniOf` University of Mary and East Stroudsburg University of Pennsylvania (institution names only, no degrees or dates); plus the pre-existing `memberOf`, `knowsAbout`, `sameAs`, `worksFor`. Two facts were promoted from visible text into JSON-LD where they had not previously been structured: Ohio licence `E.2404393` (visible on `/ohio-telehealth-therapy/` only) and the two institutions (visible on `/about/` only). This is relocation of already-published data, not invention. `EMDR Trained Professional` was **moved** from `MedicalBusiness.hasCredential` to `Person.hasCredential` — a person holds training, a business does not — and removed from the Organization node in the same commit; it now appears on 28 Person nodes and 0 MedicalBusiness nodes. Result is **2 shapes, not 1**, solely because of the LADC hold below; the 25 non-LADC pages are byte-identical to each other and the 3 LADC pages differ by exactly one `hasCredential` entry. Corroboration for the four-state `description` adopted in the `#organization` normalization: the abandoned branch `agent-regulation-page-cbcd` independently carried the four-state string `"…for adults in ND, MN, OH, and UT."` in a commit dated **2026-05-04**, predating the creation of `/ohio-telehealth-therapy/`. Two separate authors arrived at the four-state form, which supports it being the intended text rather than a one-off on the Ohio page.
- [x] **Credential: LADC — RESOLVED 2026-07-30, confirmed active.** Held on 2026-07-29 because the LADC was claimed on `/about/`, `/privacy/` and `/terms/` with no licence number anywhere in the repo, while all four other licences had theirs. Human verification confirmed it is **active in Minnesota, licence 305177**. Added to the canonical Person node on all 28 pages: `Licensed Alcohol and Drug Counselor (LADC)` as the second `hasCredential` entry (after LPCC, matching the order the 3 pages already used), and `Minnesota LADC License` / `305177` as the fourth `identifier` entry, placed directly after `Minnesota LPCC License` so identifiers stay grouped by state. **No expiration date was recorded** — a hardcoded expiry would go stale exactly the way `dateModified` does. This resolves the deliberate 2-shape split: **all 28 Person nodes are now byte-identical, 1 shape.** The licence number lives in JSON-LD only and does not appear in visible text on any page.
- [x] **`sameAs` LinkedIn URL — RESOLVED 2026-07-30, corrected.** The URL asserted in `Person.sameAs` on all 28 pages was `…/in/deirdre-kuvaas`, which is **not** her profile. Automated verification on 2026-07-29 could not settle it: LinkedIn returns **HTTP 999** (its blanket anti-automation response) to every request shape, and 999 is not a 404, so it carries no information either way. It was left in place rather than removed on no evidence. Human verification in a browser produced the correct URL, and all 28 pages now carry `https://www.linkedin.com/in/deirdre-kuvaas-57bb64396`. Zero occurrences of the old string remain repo-wide. **Lesson worth keeping: HTTP 999 from LinkedIn means "unknown", not "absent" — do not treat it as evidence in either direction.**
- [x] **LinkedIn footer link — CLOSED WON'T-FIX 2026-07-30. Do not re-open without reading the reasoning below.** The decision: `sameAs` is the entity-resolution signal for structured data, and it is now correct on all 28 Person nodes. A footer link adds nothing beyond visual consistency — it does not improve entity resolution, and search engines read `sameAs` from JSON-LD regardless of whether the URL is also anchored in the page. Against that, the change would mean introducing a new inline SVG asset into the footer of **29 hand-maintained copies with known drift** (see the header/footer item above), which is real risk for no functional gain. **The originating premise was also never true** — "every other `sameAs` target is a real footer link" is false, and was false before this item was written: the NPI registry has never been linked from any footer either, so linking LinkedIn would not have achieved the consistency the item was created to deliver. Closing rather than leaving it open as a permanent low-value backlog entry. The technical findings that led here are retained below.
  Attempted 2026-07-30, **stopped before editing** because the prerequisite does not exist. The footer social row (`div.footer__social`) contains five links — email, Facebook, Instagram, X, YouTube — and **every icon is inline SVG path data embedded in the anchor itself. There is no icon file system**: no icon assets in `/images/`, no sprite sheet, no icon font, and no LinkedIn SVG path anywhere in the repo. The only occurrence of the string "linkedin" in any page is the `sameAs` URL inside JSON-LD. Adding the link therefore requires authoring or sourcing a LinkedIn SVG path, which is asset creation rather than a structural fix, so it was not improvised. **A LinkedIn icon must be supplied before this can be applied.**
  Correction to the premise recorded earlier: it is **not** true that every other `sameAs` target is a real footer link. Of the five `Person.sameAs` targets, three are footer links on all 29 pages (Psychology Today, EMDRIA, GoodTherapy) and **two are not — LinkedIn and the NPI registry** (`https://npiregistry.cms.hhs.gov/provider-view/1881112399`, which appears in zero footers). Adding LinkedIn alone would still leave the NPI registry asserted in structured data only.
  Note also that the footer's other outbound profile links (Zocdoc, Psychology Today) sit in their own `div`s **above** the social row as text links, not as icons — so a text-link treatment for LinkedIn would have been a viable alternative needing no icon at all. Recorded in case the decision is ever revisited: if it is, the text-link form is the cheaper route, and the NPI registry should be considered at the same time rather than separately.
- [x] **Schema: dangling `#website` reference — RESOLVED 2026-07-30 by option (b).** `WebPage.isPartOf` pointed at `https://deirdrekuvaas.com/#website` on the four state pages, while the `WebSite` node carrying that `@id` was defined only on `/`, so on those four the reference resolved to nothing. **The `isPartOf` property was dropped from all four `WebPage` nodes; `WebSite` was deliberately NOT defined on them.** Reasoning for choosing (b) over (a): option (a) would add four more copies of a node to keep in sync, in a repo whose central problem is unsynchronised duplication across hand-maintained files. Nothing else on the site asserts a page→site relationship — `/` defines `WebSite` but its own `WebPage` node carries no `isPartOf` — so (b) removes the dangling reference without losing a relationship the site otherwise uses anywhere. Smaller blast radius, nothing left dangling. Those four `WebPage` nodes now carry `@type`, `@id`, `url`, `name`, `author`. **Zero dangling `@id` references remain repo-wide.** The `WebSite` node on `/` is unchanged. Original analysis retained below:
  - **(a) Define the `WebSite` node on those four pages.** Makes the reference resolve and matches how `#organization` and `#person` are already handled (defined in full on every page that references them). Costs four more copies of a node to keep in sync, in a repo whose central problem is unsynchronised duplication.
  - **(b) Drop the `isPartOf` property from those four `WebPage` nodes.** Removes the dangling reference with no new duplication. Loses the page→site relationship, which no other page on the site asserts anyway.
  Two details that bear on the choice: `/` is the only page defining `WebSite`, yet its own `WebPage` node (`#webpage`) carries **no** `isPartOf` — so the one page where the reference would resolve is the one page that does not make it. And all five `#webpage` `@id`s in the repo are referenced by nothing, here or anywhere.
- [x] **Schema: `#organization` carried 4 distinct shapes across 28 pages — normalized 2026-07-29, now 1 shape.** Original divergence and its resolution recorded below. Every page defines `MedicalBusiness` with `@id` `https://deirdrekuvaas.com/#organization`, but the node differs between pages, so a consumer merging by `@id` gets conflicting data. Measured 2026-07-29 **after** the Person normalization removed `hasCredential` from this node (that axis is already gone). Three axes remain:
  - `availableChannel` — present on the 4 state pages, absent on the other 24.
  - `legalName` — present on `/` only, absent on the other 27.
  - `description` — `/ohio-telehealth-therapy/` says `"…for adults in ND, MN, OH, and UT."`; all 27 other pages say `"…for adults in ND, MN, and UT."` **This is the substantive one**: it is a factual claim about states served, it omits Ohio on 27 of 28 pages, and it contradicts `areaServed` on those same nodes, which lists `["ND","MN","OH","UT"]` everywhere. Resolving it means deciding which description string is correct — not a mechanical merge.
  Shape counts were 23 pages / 3 state pages / `/` / `/ohio-telehealth-therapy/`, plus a fourth non-semantic axis: `telephone` sat before `address` on 24 pages and after it on 4.
  **Resolution 2026-07-29.** All 28 nodes replaced with one canonical form, every value lifted verbatim from an existing shape — nothing authored. `description` uses the four-state string; `availableChannel` and `legalName` are included on all 28. Reasoning per axis:
  - `description` — four-state form adopted. The three-state form contradicted `areaServed` on the same node, the footer link, and the licensure sentence. Ohio is an active licensure state. The string lives **only** in JSON-LD — it appears in no `<meta>` tag and no visible text — so the change was invisible to readers and the rendered-text diff was zero on all 31 pages.
  - `availableChannel` — included on all 28. The value was byte-identical on the 4 pages that had it, and telehealth delivery is a site-wide fact, not a state-page one: the homepage calls the practice a "telehealth therapy practice" offering "100% virtual therapy", three state pages repeat it, and all 29 footers say "via telehealth". There is no in-person channel anywhere in the repo, and `address` is a business location in Horace, ND rather than a clinic — so this property is the only thing distinguishing a telehealth practice from a walk-in office.
  - `legalName` — included on all 28 despite being byte-identical to `name` and therefore adding no information. Decided deliberately: the goal of the pass is that all 28 nodes end up identical, and carving out an exception for tidiness is the same reasoning that produced the drift in the first place.
  Post-change state: **1 distinct shape across 28 pages**, byte-identical modulo required indentation (27 pages at child-indent 6, `/nervous-system-regulation-for-high-achievers/` at 8 because its `@graph` nests one level deeper). Verified `areaServed` and the states named in `description` now agree on every page. No top-level non-`MedicalBusiness` node changed anywhere; the only new nested type is the `ServiceChannel` inside `availableChannel`.
- [x] **Copy: homepage licensure claims — RESOLVED 2026-07-29.** Deirdre confirmed licensure in **ND, MN, OH and UT**. ND and MN are primary and long-term; OH and UT are secondary and may be dropped in future. The two-state phrasings in the five *licensure* statements were **stale, not deliberate**, and all five were rewritten to name all four states in a tiered form — ND/MN leading, OH/UT in a separable trailing clause or element so dropping a state later is a clean deletion rather than a rewrite. State order is OH before UT throughout, matching `areaServed`, the JSON-LD `description`, and every footer. Line 768's text is byte-mirrored in the homepage `FAQPage` `acceptedAnswer`; both were updated together so they remain identical. The five as they stood before the fix:
  1. **line 559** (hero paragraph) — *"Deirdre Kuvaas is a Licensed Professional Clinical Counselor specializing in online trauma therapy for high-functioning adults in **North Dakota and Minnesota**."* → 2 states
  2. **line 569** (hero credential strip) — *"EMDR Trained Therapist | CPT Specialist | **Licensed in ND, MN, & UT**"* → 3 states
  3. **line 599** (bio paragraph) — *"…She provides specialized online trauma therapy (EMDR & CPT) for high-functioning adults experiencing burnout and PTSD across **North Dakota, Minnesota, Ohio, and Utah**."* → 4 states
  4. **line 726** (body paragraph) — *"I am licensed to provide 100% virtual therapy for adults across **North Dakota and Minnesota**. Broadening access to evidence-based care: Now also accepting telehealth clients in Utah."* → 2 states, with Utah named separately as an addition and Ohio absent entirely
  5. **line 768** (FAQ answer) — *"I am licensed for telehealth in **North Dakota, Minnesota, Ohio, and Utah**."* → 4 states
  Current text after the fix: 559 *"…in North Dakota and Minnesota, and is also licensed in Ohio and Utah."* · 569 *"Licensed in ND & MN | Also OH & UT"* · 599 *"…across North Dakota and Minnesota, and is also licensed in Ohio and Utah."* · 726 *"…across North Dakota and Minnesota. Broadening access to evidence-based care: I am also licensed in Ohio and Utah."* · 768 *"I am licensed for telehealth in North Dakota and Minnesota, and also in Ohio and Utah."*
- [x] **Copy: remaining two-state phrasings are INTENTIONAL market targeting, not drift. Do not "fix" them.** Recorded 2026-07-29 so future passes stop flagging them. The ND/MN focus in the homepage's SEO-facing copy is deliberate: ND and MN are the primary long-term markets, and `/ohio-telehealth-therapy/` and `/utah-telehealth-therapy/` target those geographies on their own pages. These are **positioning copy, not licensure claims**, and are correct as they stand:
  - `index.html` **line 7** `<title>` — *"Trauma Therapy & EMDR | North Dakota & Minnesota"*
  - `index.html` **line 558** `<h1>` — *"Online Trauma Therapy & EMDR Counseling in North Dakota & Minnesota"*
  - `index.html` **line 601** — *"…All sessions are provided online, making specialized trauma therapy accessible to clients across North Dakota and Minnesota."*
  - `index.html` **line 603** `<h2>` — *"Online Trauma Therapy for High-Functioning Adults in North Dakota & Minnesota"*
  - `index.html` **line 747** — *"Evidence-based trauma therapy using EMDR and Cognitive Processing Therapy (CPT), available online across North Dakota and Minnesota."*
  - `index.html` **line 822** — *"Providing specialized telehealth services for high-functioning adults residing in North Dakota (Fargo, Bismarck, Grand Forks) and Minnesota (Minneapolis, St. Paul, Rochester, Duluth)."*
  - `index.html` **line 176** — `WebPage.name` in JSON-LD, which mirrors the `<title>` and is covered by the same rationale.
  - Two-state page `<title>`s: `/counseling-for-trauma/`, `/emdr/` (and its `<h1>`), `/individual-therapy/`, `/people-pleasing/`.
  - Three-state (`ND, MN, UT`) page `<title>`s: `/blog/`, `/cognitive-processing-therapy/`, `/contact/`, `/faqs/`, `/telehealth/`. `/rates-insurance/` already names all four.
  The distinction to apply in future passes: **a statement about where Deirdre is licensed or accepting clients must name all four states; a statement about who the page is aimed at need not.**
- [x] **Copy: three homepage statements named ND, MN and UT but omitted Ohio — RESOLVED 2026-07-29.** Ruled availability claims, not targeting copy: naming UT while omitting OH has no strategic rationale, so this was staleness. Ohio added to all three, in the site's OH-before-UT order. `index.html` now carries **zero** ND/MN/UT-without-OH statements. The `twitter:description` also had an unrelated lowercase sentence fragment (`"addiction. serving"`), fixed to `"addiction. Serving"` in the same pass. Final text: line 743 *"Now booking new clients in ND, MN, OH, & UT."* · `og:description` *"…serving adults in ND, MN, OH, & UT…"* · `twitter:description` *"…addiction. Serving ND, MN, OH & UT…"*. The three as they stood before the fix:
  - `index.html` **line 743** — *"Now booking new clients in ND, MN, & UT."* This is a **booking availability claim**, the closest of the three to a licensure statement, and the strongest candidate for correction.
  - `index.html` **line 13** `<meta property="og:description">` — *"Telehealth therapy for anxiety, trauma & addiction — serving adults in ND, MN, & UT. Deirdre Kuvaas, LPCC uses EMDR & CPT. Free 15-min consultation. Book now."*
  - `index.html` **line 23** `<meta name="twitter:description">` — *"Telehealth therapy for anxiety, trauma & addiction. serving ND, MN & UT. Book a free 15-min consultation with Deirdre Kuvaas, LPCC."*
  These were the last three on the homepage. The equivalent problem on the rest of the site is recorded in the next item.
- [x] **Copy: the ND/MN/UT three-state form — RESOLVED 2026-07-30. All 47 occurrences across 15 pages fixed; zero remain site-wide.** Found by a site-wide scan while fixing the homepage. Every occurrence was a `<title>` or `<meta>` tag — none were body copy, and `<body>` was not touched on any page. The 47 were split into two buckets and treated differently:
  - **Bucket A — 28 availability or licensure claims → Ohio added**, in the site's OH-before-UT order, each preserving its own separator style (serial comma or not). These are `description` / `og:description` / `twitter:description` on `/about/`, `/appointment-request/`, `/counseling-for-anxiety/`, `/counseling-for-trauma/`, `/emdr/`, `/individual-therapy/`, `/mental-health-links/`, `/people-pleasing/`, `/ptsd/`, `/services/`, `/telehealth/`, plus `/services/` `twitter:title`.
  - **Bucket B — 19 title-family tags → state list dropped entirely** rather than expanded. A three-state list in a title is not coherent targeting, and the non-state part of each title already carries the positioning. Affects `<title>`, `og:title` and/or `twitter:title` on `/blog/`, `/cognitive-processing-therapy/`, `/contact/`, `/emdr/`, `/faqs/`, `/individual-therapy/`, `/people-pleasing/`, `/telehealth/`. Example: `"Telehealth Therapy | Virtual Counseling | ND, MN, UT"` → `"Telehealth Therapy | Virtual Counseling"`.
  This removed the split-answer problem where a page's title family and description family named different state sets — `/cognitive-processing-therapy/` and `/contact/` each had three-state titles against four-state descriptions, which was the clearest evidence the three-state form was staleness rather than intent. The lowercase sentence fragment on `/counseling-for-anxiety/` (`"root cause. serving"`) was fixed in the same pass, matching the identical homepage fix.
  **The four state pages were deliberately left alone** and are correct as they stand: `/north-dakota-`, `/minnesota-`, `/ohio-` and `/utah-telehealth-therapy/` each name only their own state in their own title and metas. None appeared in the 47. Do not normalize them to a four-state list — each targets its own geography by design.
  Two-state positioning copy remains untouched per the market-targeting decision recorded above; the rule that governs both items is: **a statement about where Deirdre is licensed or accepting clients must name all four states; a statement about who a page is aimed at need not.**
  Original finding, retained for context: found 2026-07-29 by a site-wide scan while fixing the homepage; only `index.html` was in scope at the time. These matter more than body copy because `<title>` and `<meta description>` are what search results and social cards display, so they reach people who never load the page. Most are phrased as **availability**, which by the rule recorded above means they should name all four states: *"Telehealth sessions … in ND, MN, & UT"*, *"serving ND, MN & UT"*, *"Telehealth in ND, MN, & UT"*, *"from anywhere in ND, MN, & UT"*, *"Serving adults across ND, MN, & UT"*, *"Online trauma therapy in ND, MN, and UT"*.
  Affected pages: `/about/`, `/appointment-request/`, `/blog/`, `/cognitive-processing-therapy/`, `/contact/`, `/counseling-for-anxiety/`, `/counseling-for-trauma/`, `/emdr/`, `/faqs/`, `/individual-therapy/`, `/mental-health-links/`, `/people-pleasing/`, `/ptsd/`, `/services/`, `/telehealth/`.
  **Two pages are internally inconsistent, which is the clearest evidence this is staleness rather than intent.** On `/cognitive-processing-therapy/` the `<title>`, `og:title` and `twitter:title` all say `ND, MN, UT` while the `description`, `og:description` and `twitter:description` on the same page all say `ND, MN, OH, UT`. `/contact/` has exactly the same split — titles say three states, descriptions say four (*"telehealth therapy in North Dakota, Minnesota, Ohio & Utah"*). A page cannot be deliberately targeting three states in its title and four in its description.
  Note `/counseling-for-anxiety/` carries the same lowercase-fragment typo the homepage had: *"…start healing the root cause. serving ND, MN & UT."* Worth fixing in the same pass. `/rates-insurance/` already names all four and needs nothing.
- [x] **Decided, not drift: the Psychology Today `sameAs` slug is `deirdre-kuvaas-fargo-nd`, and that is correct.** Recorded 2026-07-29 so future passes stop re-flagging it. The practice is physically located in **Horace, ND** (as `address.addressLocality` correctly states) but uses **Fargo** for recognition, Horace being a small community in the Fargo metro. Psychology Today resolves profiles by the numeric ID `1073735`; the slug segment is cosmetic and does not affect resolution. The branch `agent-regulation-page-cbcd` carried `deirdre-kuvaas-horace-nd`, which is the **stale** form — that is one of several reasons that branch was superseded. `fargo-nd` is the form on all 28 pages and is the one to keep. Do not "correct" it to match `addressLocality`.
- [x] **Lighthouse: images missing explicit width/height — RESOLVED 2026-07-30.** All 38 `<img>` tags that lacked a dimension now carry `width` and `height` taken from the files themselves, never from CSS: `/images/hero-banner-leaves.webp` → **1000 × 1778** (read with PIL) on 9 pages, and the GoodTherapy seal `verified_seal2.svg` → **752 × 209** (read from the root `<svg>` element's own `width`/`height`, which match its `viewBox`) on 29 pages. All 100 `<img>` tags site-wide now carry both. No other attribute was altered on any image — `src`, `alt`, `loading`, `fetchpriority`, `style` and `title` are byte-identical. Rendered text unchanged on all 31 pages. Note both images are laid out by CSS (`width:100%;height:100%;object-fit:cover` for the hero, inline `width:100px;height:auto` for the seal), so the attributes act purely as aspect-ratio hints for CLS and change nothing visually. **Caveat: the seal is a third-party asset.** If GoodTherapy ever reissues it at a different aspect ratio the hardcoded 752 × 209 becomes wrong; it is a remote file the repo cannot validate on its own.
- [ ] **Lighthouse: 27 heading-level skips site-wide — REPORTED 2026-07-30, deliberately NOT fixed.** Every one would change appearance, so under the "purely semantic only" rule all were skipped. Two distinct classes:
  - **23 × footer `h2 → h4`** (and `h1 → h4` on `404.html`). The footer's three headings — Office Hours, Areas Served, Contact Information — are `<h4>` and are styled by the **element selector** `.footer__col h4{color:olive;font-size:.875rem;margin-bottom:1rem}` plus global `h4{font-family:var(--font-ui);font-size:1.125rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em}`. Retagging them `h3` would drop all of that and pick up `h3{font-size:1.5rem;color:taupe}` **and** the global override `h3{color:#2d3436!important}` — a large, visible change. Preserving appearance would mean adding a class to 87 headings across 29 hand-maintained files plus new `!important`-strength CSS in `css/style.css`.
  - **5 × body `h1 → h3`** on `/blog/`, `/emdr/`, `/individual-therapy/`, `/mental-health-links/`, `/rates-insurance/`. Each is a `page-banner__title` `h1` followed directly by a plain `h3`. Retagging to `h2` changes size 1.5rem → 2rem and colour, again requiring compensating CSS.
  Note `404.html` is not fully fixable by retagging alone: its last body heading is `h1`, so even `h4 → h3` leaves an `h1 → h3` skip. Also note 7 pages already end their body content on an `h3`, so a footer `h3` would be legal there — the fix is not uniform across pages.
- [ ] **Lighthouse: colour-contrast failures — REPORTED 2026-07-30, not changed. Brand colours are a business decision.** Computed WCAG ratios for the palette pairs actually in use. Failing AA for normal text (<4.5:1): `--color-link #96836E` on white **3.64:1** and on cream **3.13:1**; `--color-taupe #9A9085` on white **3.13:1** and on cream **2.70:1** (this one also fails AA-large); `--color-olive #646756` on `--color-light-sage #C9D8BD` **3.88:1**; `--color-sage #5F7C54` on cream **4.02:1**. Passing comfortably: olive on white 5.81:1, olive on cream 5.00:1, sage on white 4.67:1, body text 12.08:1 on white and 10.40:1 on cream, nav `#2d3436` on cream 10.92:1, white on olive 5.81:1, white on sage 4.67:1. The worst offender is **taupe on cream at 2.70:1**, which fails at every size and is used for breadcrumbs and card meta text. Fixing means darkening brand colours — not a structural change, and not to be done without the practice's sign-off.
- [x] **Console errors on page load — CHECKED 2026-07-30, none found.** Live load of `https://deirdrekuvaas.com/` in a real browser produced **zero console errors and zero failed network requests**; the only runtime request captured was the SimplePractice booking widget (`spwidget-deirdre-kuvaas.clientsecure.me`), HTTP 200. Static analysis agrees: every local asset referenced by `img`/`script`/`link`/`source` resolves on disk, and **nothing references a file deleted in the earlier cleanup or a script that no longer exists**. Two external scripts load site-wide — `member.psychologytoday.com/verified-seal.js` (27 pages) and `widget-cdn.simplepractice.com/assets/integration-1.0.js` (29 pages). One path looks missing to a static checker but is not: `/.netlify/images?url=…` is Netlify's Image CDN endpoint, resolved at request time by the platform, and correctly has no on-disk file.
- [x] **Bug: the hero preload `imagesrcset` descriptor overstated the image width — RESOLVED 2026-07-30.** On `/`, `/counseling-for-anxiety/` and `/emdr/` the preload declared `/images/hero-banner-leaves.webp 1600w`, but the file is **1000 px wide** (1000 × 1778). A `w` descriptor that lies about the real width can make the browser choose the wrong candidate and defeats the purpose of the responsive set. Corrected to `1000w` on all three; zero occurrences of `1600w` remain in any page. Found while reading intrinsic dimensions for the width/height fix — the descriptor and the file disagreed, which is only visible if you read the actual file rather than trusting the markup.
- [x] **Lighthouse: `llms.txt` failed the Agentic Browsing audit ("File does not appear to contain any links") — RESOLVED 2026-07-30.** The file already had a conforming `# ` H1 and a `>` description, and already listed six key pages — but as **bare URLs**, e.g. `- Trauma therapy: https://…`. A parser looking for Markdown link syntax finds none, hence "no links". Converted all seven URLs to `[label](url)` form. **Syntax only**: the H1 and description lines are byte-identical, every label is the exact text that preceded the colon, and the distinct URL set is unchanged — nothing added, nothing removed, same 40 lines. `llms.txt` is on the protected-files list; this edit was explicitly approved.
  **Superseded 2026-07-30 (same day):** the page list initially stayed North Dakota and Minnesota only, on the reasoning that it mirrored the homepage's primary/secondary targeting framing. That was reversed on the correct ground that **`llms.txt` is not competing for search queries** — it is a machine-readable directory, not SEO copy, so the targeting rationale does not transfer. The file already stated all four states served, which made linking only two read as an omission rather than a choice. `/ohio-telehealth-therapy/` and `/utah-telehealth-therapy/` were added after Minnesota; the list is now all four states. The distinction worth carrying forward: **the ND/MN targeting decision applies to `<title>` and `<meta>` copy, which competes for queries, and not to machine-readable inventories, which should be complete.**
  The provider credential line was also made state-explicit in the same pass: `LPCC (…) in North Dakota, Minnesota, and Ohio; LCMHC (…) in Utah; LADC (…) in Minnesota`. The credential-to-state mapping is taken from `/about/` (`LPCC (ND, MN, OH)`, `LCMHC (UT)`, `LADC (MN)`) and cross-checked against the five `Person.identifier` licence entries; all three sources agree. Note the wording is not byte-identical to `/about/`, which uses state abbreviations in parentheses — the full state names and the `in <state>` idiom were used to match `llms.txt`'s own existing style (`States served: North Dakota, Minnesota, Ohio, Utah`, and the pre-existing `LCMHC in Utah`). No factual claim was introduced or altered; only the credential expansions, which `/about/` supplies verbatim, were added.
- [ ] _redirects: /privacy and /terms rules are inert no-ops and would create an infinite redirect if a ! were added
- [ ] _headers: X-Robots-Tag: all on /* is a no-op; "all" is already the default
- [x] **No dedicated Fargo-Moorhead metro page existed — BUILT 2026-07-30 at `/fargo-moorhead-therapy/`. Awaiting human review on the deploy preview; not yet merged.** Targets city-level queries ("therapist fargo", "counselor moorhead") that nothing on the site addressed — the state pages target state-level terms and nobody searches "therapist north dakota". The differentiator is not four-state licensure but the narrower fact that Fargo-Moorhead is one metro with a state line through it, and dual ND/MN licensure means the river does not decide who she can work with.
  **Anti-cannibalization constraints applied and verified:** self-referencing canonical; no state names in the H1; links flow outward to the state and service pages; one inbound contextual link from homepage body copy, anchor `therapy in Fargo-Moorhead`.
  **Rules 4 and 6 of the build brief were REVERSED on 2026-08-01 — the page IS in the nav and footer, deliberately.** The brief said "do not add to the nav" and allowed only the single homepage body link, on the reasoning that a 25th header link would dilute link equity and make the page compete with the homepage for brand queries. **That rule was wrong.** In practice it left the page reachable from exactly one link on one page, orphaning it from the other 29 — and *Areas Served* is precisely where a user looking for local therapy would go. Link-equity dilution across ~30 pages is not a real concern at this scale; the cost of being unreachable is. `/fargo-moorhead-therapy/` is now **first** in the header *Areas Served* dropdown and **first** in the footer *Areas Served* block on all 30 pages, ahead of the four states — primary market, most specific geography. Do not re-orphan it on the strength of the original rule.
  Labels follow each variant's own convention rather than being uniform: the 25 short-label header copies say `Fargo-Moorhead`, the 5 long-label copies (`404.html`, `/about/`, `/`, `/privacy/`, `/terms/`) say `Therapy in Fargo-Moorhead`; footers likewise, 29 short and `/` long. **Four pages carry a long-label header against a short-label footer** — `404.html`, `/about/`, `/privacy/`, `/terms/` — which is pre-existing drift, not introduced here; each was matched to its own existing convention on each side rather than normalised.
  **Duplicate-copy check was measured, not eyeballed:** all 47 body sentences compared against the visible `<main>` text of every other page. **Zero exact duplicates.** One near match at 0.75 — *"Sessions run over a secure, HIPAA-compliant video platform."* against `/telehealth/`'s *"All sessions use a HIPAA-compliant, encrypted video platform."* — which is a paraphrase rather than a lift and is the brief's own wording. The CTA block is byte-identical to the four state pages **by design**, per the instruction to match the existing pattern rather than author a new one; it is shared chrome and was excluded from the body-copy comparison.
  **One approved wording change from the brief — do not "restore" the original.** The brief's opening read *"For most therapists here, that line is a wall."* The page instead says *"For a therapist licensed on one side of it, that line is a wall."* The original was an empirical claim about the local market — that most Fargo-Moorhead therapists hold single-state licensure — which the site cannot support, and comparative claims about other practitioners in a licensed profession can attract board scrutiny. The replacement is **definitional rather than a headcount**: it keeps the metaphor and the rhetorical work of turning geography into a problem, but makes the point about what single-state licensure means rather than about who else is in the market. Approved 2026-07-31.
  **Three deviations from the brief, all requested:** the regional-framing paragraph about local work culture was omitted as unreviewed inference and its position marked with an HTML comment; insurance copy was not written, replaced by a single link to `/rates-insurance/` so the panel list stays in one place; the city list was cut to the core metro — Fargo, West Fargo, Horace, Moorhead, Dilworth.
  **Schema follows the conventions set earlier in this session:** single `@graph` with `WebPage` / `Service` / `MedicalBusiness` / `Person` / `BreadcrumbList` / `FAQPage`; `@id`s `#webpage`, `#service-fargo-moorhead`, `#faq`; **no `isPartOf`** (removed site-wide in PR #67); Person and Organization nodes byte-identical to the other 28. The `Service` node's `areaServed` names the five metro communities as `City` objects rather than states, which is what distinguishes it from the state pages' `Service` nodes.
  Added to `sitemap.xml` (priority 0.8, matching the state pages) and to `llms.txt` under Key pages. Both are protected files; the additions were mandated by the brief.
- [ ] **Copy: `/minnesota-telehealth-therapy/` and `/fargo-moorhead-therapy/` both claim Moorhead.** The Minnesota page's FAQ lists *"Minneapolis, St. Paul, Rochester, Duluth, Mankato, **Moorhead**, Bloomington, Brooklyn Park, and all surrounding communities"*, and the new metro page is built around Moorhead. The intents differ — statewide coverage versus metro-level targeting — so this is not necessarily a conflict, but the two "communities served" lists overlap on the single term the new page is built around. Someone should decide deliberately which page owns "Moorhead" rather than leaving it to chance. Flagged 2026-07-30 during the metro page build; not changed.
