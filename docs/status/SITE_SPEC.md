# Site spec: what "the maintainer's other product subsites" share

Status: derived 2026-11-23. Scope: `demo/frontend` (journal-atlas.chroniclecore.com)
and `demo/backend` (api.journal-atlas.chroniclecore.com, FastAPI on Outpost).

The maintainer asked for "the spec of our other product subsites" without
listing it, so this file **derives** the spec from the siblings instead of
guessing. Part 1 is the common spec, each item with the sibling file, live URL
or skill it came from. Part 2 compares the current Journal Atlas (JA) site with
it. Part 3 lists what needs the maintainer. Anything the siblings do not do is
marked **not found in siblings**; nothing here is invented to fill a gap.

## 0. What was read

Live hosts (public pages and headers fetched 2026-11-23):
`riftbound`, `summonlibrary`, `basesmall`, `smallol` under `chroniclecore.com`.
`techstackmap.chroniclecore.com` did not resolve on that date, so
TechnologyStackMap is source-only evidence here.

Sources under `P:\MyOpenSource\`: `TechnologyStackMap` (README, `data/`, `i18n/`,
`src/`, `dist/`), `SmalLoL-deploy` (`wrangler.toml`, `deploy.sh`, `worker.js`),
`riftatlas-companion` and `JIZURA-Zh` (browser extension and desktop tool, not
sites; checked, nothing site-level to add), `jev-capability-atlas` (docs repo, no
site), `SmalLoL-promo` (post drafts, nothing).

Sources outside `P:\MyOpenSource\` that the live sites turned out to be built
from (read only): `P:\Project\RiftBoundC` (`AGENTS.md`,
`docs/operations/PRODUCTION_RELEASE_GATE.md`,
`docs/operations/SEO_AND_DEPLOYMENT_CLEANUP.md`) and `P:\Project\MyLibra`
(`GEO-AUDIT-REPORT.md`, `MARKETING_WEB_AUDIT.md`).

Skills: `ccweb-footer`, `ccweb-ads`, `adsense-optimizer` (and its
`references/subdomain-checklist.md`), `search-visibility-audit` (references
`02`, `05`, `06`), `search-visibility-delivery`, `techstack` (index only; the
`accessibility`, `i18n`, `cloudflare` books were not opened, see "Not read"),
`outpost-deploy`, `ui-ux-pro-max` (rule table only), `taste-skill` (not applied:
it is a landing-page art-direction skill, and JA is a tool page with a fixed
visual identity).

Not read: the `techstack` reference books, the full `taste-skill`, the sibling
Next.js component sources. Items that depend on them are marked.

## 1. The common spec

Each sibling has its own visual identity; what they share is the checklist
below. ID prefixes: T trust, D design, A accessibility, S search, P performance
and delivery, M measurement and money, O operations.

### 1.1 Identity and trust

| ID | Spec | Source |
|---|---|---|
| T1 | Studio attribution on every page: "ChronicleCore Studio (編年史記工作室) 出品", author Zaious, studio URL `https://studio.chroniclecore.com`. | riftbound footer; summonlibrary footer; smallol footer + JSON-LD `publisher`; basesmall footer; TechnologyStackMap `i18n/zh-Hant/ui.json` `footer_studio`/`footer_author`, `data/meta.json` `studioUrl` |
| T2 | A non-affiliation / non-endorsement line in the footer, worded for the specific relationship (Riot, MLB, "technology names belong to their owners"). Where a visitor could mistake the site for official, also a visible badge beside the brand mark in the nav, not only a footnote. Re-derive the weight per site, do not copy a badge. | riftbound footer + nav "非官方" badge; smallol/basesmall footers; TechnologyStackMap `footer_legal`; skill `ccweb-footer` Problem 1 and "Applying across multiple sites" |
| T3 | Declaration text is defined once and referenced everywhere; grep every claim (counts, vendor names) when something changes; removing a vendor means updating every sentence naming it in the same change. | skill `ccweb-footer` Problem 2 and audit steps; MyLibra `GEO-AUDIT-REPORT.md` section 2 (`lib/marketing-facts.ts`); TechnologyStackMap README ("`{contact}`, `{repo}` from `meta.json`; a hard-coded address is blocked by `check`") |
| T4 | A licence line in the footer (code and content licences, link to terms). | TechnologyStackMap `footer_license` (CC BY-SA content, MIT code); smallol/basesmall footers (Apache-2.0) |
| T5 | A support link that states it unlocks nothing. | basesmall and smallol footers; riftbound `/partners` "支持作者" section; TechnologyStackMap `footer_support` |
| T6 | Contact: a project mailbox `<site>@chroniclecore.com` shown on a contact page or in the footer (riftbound, summonlibrary, TechnologyStackMap), or GitHub only (basesmall, smallol). The mailbox is never typed into prose; it comes from one config value. | riftbound `/contact`; summonlibrary footer and privacy section 11; TechnologyStackMap `meta.json` `site.contact`; basesmall/smallol footers |
| T7 | An AI-disclosure page or section: who made the site, which content is AI-produced, how that is labelled next to the content, what the site will never do (no fabricated rates or rankings, no fake author), what data it holds that others may study. | riftbound `/ai` "AI 方法論"; TechnologyStackMap `data/about.json` sections `ai`, `verify`; MyLibra not found |
| T8 | An About page with a named, first-person author entity, why it was built, and `Person` structured data. | riftbound `/about`; summonlibrary `/about`; MyLibra `GEO-AUDIT-REPORT.md` section 5 item 3 ("single biggest lever") |
| T9 | A privacy statement that matches the real data flows, including every third party that receives visitor data (fonts, AI vendors, payment), and is updated in the same change as the flow. | riftbound `/privacy`; summonlibrary `/privacy` (11 sections, AI vendors named, section 7 cookies and analytics); TechnologyStackMap `about.json` `privacy` (names Google Fonts) |
| T10 | A terms page only where there are accounts or payment. Free tools without accounts have none. | summonlibrary `/terms` exists (accounts, pricing); riftbound `/terms` is a 404; basesmall, smallol have none |
| T11 | A status page that does not lie when the backend fails (degraded, not "all systems normal") and is linked from the nav, not an orphan. | summonlibrary `/status`; MyLibra `GEO-AUDIT-REPORT.md` section 1 (`c034c0a`), `MARKETING_WEB_AUDIT.md` M1, M2 |
| T12 | Which build/data version the page shows, and when. | summonlibrary changelog (`/changelog`); riftbound `/updates`; JA already has `VersionLine` |

### 1.2 Design system

| ID | Spec | Source |
|---|---|---|
| D1 | Design tokens as CSS custom properties on `:root`; light and dark both defined; dark follows `prefers-color-scheme` unless `data-theme` forces it; `body` has an explicit background; `<meta name="theme-color">` matches the page background. | TechnologyStackMap `src/style.css` (`:root`, `@media (prefers-color-scheme: dark) :root:not([data-theme="light"])`, `:root[data-theme="dark"]`); riftbound `theme-color #0d0808`; summonlibrary `#F6F4EE`; basesmall/smallol `#15171C` |
| D2 | Typography: a CJK-aware stack with system fallbacks, a mono face for numbers and labels, headings that wrap (`text-wrap: balance`). Web fonts are a privacy and weight cost: TechnologyStackMap discloses Google Fonts in its privacy text; MyLibra's audit measured 632 KB of serif font for headings only (B15) and 'fonts take nearly half the home page bytes'. No shared typeface across siblings. | TechnologyStackMap `page.template.html`, `style.css`; MyLibra `MARKETING_WEB_AUDIT.md` B15, `GEO-AUDIT-REPORT.md` section 3 |
| D3 | One visual identity per site. Not a shared theme: riftbound is dark red, summonlibrary cream and serif, TechnologyStackMap drafting paper, basesmall/smallol dark. **No shared theme across siblings: not found in siblings.** | live pages; `taste-skill` read as anti-template guidance |
| D4 | Error boundary and error pages exist. | riftbound bundle chunks `app/global-error` and `app/(zh)/error`; see S9 for 404 |

### 1.3 Accessibility

| ID | Spec | Source |
|---|---|---|
| A1 | A "skip to main content" link first in the tab order, `<main id>` target. | TechnologyStackMap `page.template.html` `.skip`; MyLibra `MARKETING_WEB_AUDIT.md` M3 |
| A2 | Visible `:focus-visible` ring, never removed; focus not hidden behind sticky headers (WCAG 2.2 SC 2.4.11). | TechnologyStackMap `style.css`; MyLibra M4; `ui-ux-pro-max` priority 1 |
| A3 | Text contrast at least 4.5:1, non-text borders at least 3:1, checked for both light and dark. | MyLibra B2, B16, M19; `ui-ux-pro-max` priority 1; TechnologyStackMap README ("`--line2` below 3:1 on any of three backgrounds is blocked by `check`") |
| A4 | No text under 12 px (blocked by the build check). | TechnologyStackMap README `check` list |
| A5 | Touch targets at least 44 px with 8 px spacing. | MyLibra M5; `ui-ux-pro-max` priority 2 |
| A6 | `prefers-reduced-motion` honoured, including decorative animation. | MyLibra B4 |
| A7 | Errors and progress are announced (live region), focus is placed after an error, state is not colour-only. | MyLibra M11; TechnologyStackMap README (focus management, Esc, `aria-current` on navigation) |
| A8 | Tables carry real semantics (header cells, scope). | MyLibra B7 |
| A9 | `lang` on `<html>`, `viewport-fit=cover` with safe-area padding, layouts checked at 768-1023 px. | TechnologyStackMap `page.template.html`, `style.css`; MyLibra B6 |
| A10 | A gate, not a memory: contrast and minimum-size rules are enforced by a script with an exit code. | TechnologyStackMap `scripts/check.mjs`; `~/.claude/CLAUDE.md` "discipline retirement rule" |

### 1.4 Search, structured data, machine-readable files

| ID | Spec | Source |
|---|---|---|
| S1 | Per page: unique `<title>`, `description`, canonical, `og:title/description/url/site_name/locale/image` (1200x630) with `image:alt`, `twitter:card summary_large_image`. A sub-page must not inherit the home page's og values. | all four live siblings; MyLibra B8; og image sizes: summonlibrary JPEG 99 KB (down from 729 KB PNG), smallol/basesmall `media/og.png` |
| S2 | JSON-LD matching what is visible and true: no `offers` the page contradicts, no `SearchAction` without a public search endpoint, `Organization` is the studio not the product, `sameAs` only URLs verified anonymously with curl, `softwareVersion` equals the changelog. | MyLibra `GEO-AUDIT-REPORT.md` sections 1 and 2; smallol/basesmall `SoftwareApplication` + `Organization` publisher + `Person` author |
| S3 | FAQPage markup is optional: the Google rich result was retired 2026-05-07. | `search-visibility-audit` reference `05` (read 2026-10-08); basesmall/smallol still carry it |
| S4 | `robots.txt` with a `Sitemap:` line; disallow only private or app routes. Do not add named AI-crawler groups: under RFC 9309 a named group replaces `*`, silently dropping every disallow unless copied. | riftbound, summonlibrary, basesmall, smallol robots.txt; MyLibra `GEO-AUDIT-REPORT.md` section 2 item 1 |
| S5 | `sitemap.xml` with `lastmod` on every URL, `xhtml:link` hreflang pairs where there are languages, only indexable pages. A page set to `noindex` is also dropped from the sitemap. | summonlibrary (15 URLs, all with lastmod); smallol/basesmall (hreflang); `ccweb-ads` section 1 |
| S6 | `llms.txt`: H1, blockquote summary, an "authoritative scope" / "not provided" section, key page list, attribution note. Generated from or checked against the same facts as the pages, because an out-of-date llms.txt answers "no" to features that exist. Google does not use it; it is for other systems. | all four live siblings; MyLibra M13; `search-visibility-audit` reference `06` |
| S7 | `ads.txt` only when ads are on or being kept for re-application. | riftbound (dormant, commented); TechnologyStackMap `dist/ads.txt` (env-gated); absent on summonlibrary, basesmall, smallol |
| S8 | Icons: favicon, apple-touch-icon; a web manifest only for installable apps. | riftbound and summonlibrary manifests; none on basesmall, smallol |
| S9 | Unknown URLs return a real 404 with a branded body, never the SPA shell with 200 (soft 404). | summonlibrary 404 (22.9 KB HTML), basesmall/smallol 404 (small HTML), riftbound 404; `SmalLoL-deploy/wrangler.toml` `not_found_handling = "404-page"`; `search-visibility-audit` reference `02` section C (soft 404); riftbound `PRODUCTION_RELEASE_GATE.md` ("unknown share code returns HTTP 404") |
| S10 | The primary content is in the raw HTML (prerender or SSR), one `<h1>` per page, heading levels not inverted. | summonlibrary audit ("SSR prerender, one h1 per page", M17); `search-visibility-audit` reference `02` section D |
| S11 | After meaningful changes, notify IndexNow for changed URLs only. Outward-facing. | riftbound `PRODUCTION_RELEASE_GATE.md`; `search-visibility-audit` reference `02` section K |
| S12 | Language: hreflang pairs with `x-default`; riftbound zh-Hant + `/ko`; basesmall en + `/zh/`; smallol zh-Hant + `/en/`; TechnologyStackMap has the infrastructure for many languages and ships one; summonlibrary zh-Hant only. | live heads; TechnologyStackMap README "新增一種語言" |

### 1.5 Performance and delivery

| ID | Spec | Source |
|---|---|---|
| P1 | Core Web Vitals "good": LCP <= 2.5 s, INP <= 200 ms, CLS <= 0.1 at p75. **A numeric byte budget: not found in siblings.** Practices instead: hero image 52 KB (down 67%), og image 99 KB, no 3.3 MB all-adapter bundles, fonts subset, reserve layout space for late content. | `search-visibility-audit` reference `02` section H (web.dev, read 2026-10-08); MyLibra `GEO-AUDIT-REPORT.md` section 1; `ccweb-ads` section 4; `adsense-optimizer` Step 3 |
| P2 | Caching: content-hashed assets `immutable`; HTML revalidates (`max-age=0, s-maxage=60, must-revalidate` on riftbound). Never `stale-while-revalidate` on HTML, because a deploy 404s the previous build's hashed chunks. | riftbound `PRODUCTION_RELEASE_GATE.md` "Caching / stale HTML"; MyLibra `GEO-AUDIT-REPORT.md` section 3 (zero asset cache = HIGH) |
| P3 | Security headers: HSTS (riftbound adds `preload`), CSP, `nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy`, `X-Frame-Options` or `frame-ancestors`. HTTP redirects to HTTPS. basesmall and smallol set none (Cloudflare defaults only). | riftbound and summonlibrary live headers; MyLibra `GEO-AUDIT-REPORT.md` section 3 BLOCKER |
| P4 | Third-party scripts: summonlibrary, basesmall, smallol load none; riftbound loads PostHog only after consent. | live HTML and CSP; riftbound `PRODUCTION_RELEASE_GATE.md` ("only if consented analytics is desired") |

### 1.6 Measurement and money

| ID | Spec | Source |
|---|---|---|
| M1 | Analytics: riftbound consented PostHog; summonlibrary first-party de-identified events and Web Vitals (privacy section 7), with its own audit complaining that the conversion funnel had zero instrumentation (B13); basesmall/smallol none ("no account, no server, no analytics"; smallol counts distinct app connections per hour without IP). **No common mechanism: not found in siblings.** | riftbound CSP; summonlibrary `/privacy` section 7; MyLibra B13; basesmall/smallol `llms.txt` and FAQ |
| M2 | Ads policy: never on pages where the reader is doing a task or where credibility is the product; placement decided by one route allowlist; ads need original content (thin generated pages get `noindex` and leave the sitemap); public repos hold no ad IDs (build env vars); ads are labelled "廣告"; basesmall/smallol state "no ads". | `ccweb-ads` sections 1 and 5; `adsense-optimizer` SKILL and `references/subdomain-checklist.md`; TechnologyStackMap README "部署 / 廣告"; riftbound `/partners` "不賣的位置" |
| M3 | Funding statements: "unlocks nothing; every feature is the same for everyone". | basesmall, smallol, riftbound |

### 1.7 Operations

| ID | Spec | Source |
|---|---|---|
| O1 | Deploy paths: static or Worker-with-assets on Cloudflare (basesmall, smallol via `SmalLoL-deploy`; riftbound via OpenNext on Workers; summonlibrary similar); backends on Outpost through `outpost-deploy` (non-root user, systemd, Caddy, `/healthz` mandatory, secrets only in `/etc/outpost/`). JA already follows this (`demo/DEPLOY.md`, `demo/DEPLOY_OUTPOST.md`). | `SmalLoL-deploy/wrangler.toml`, `deploy.sh`; skill `outpost-deploy` |
| O2 | A pre-deploy gate list (lint, typecheck, tests, build, `npm audit --omit=dev --audit-level=high`) and a post-deploy check of `/`, `/robots.txt`, `/sitemap.xml`, `/llms.txt`, an unknown URL (must be 404) and the response headers. | riftbound `PRODUCTION_RELEASE_GATE.md`; `SmalLoL-deploy/deploy.sh` ("what goes live must be what is committed", layout gate `pagebalance.mjs`) |
| O3 | Dependency advisories reviewed monthly. | riftbound `PRODUCTION_RELEASE_GATE.md` |
| O4 | Numbers on pages come from data, not prose; where prose must state one, a test ties it to the data. | riftbound `AGENTS.md` (counts block "regenerate before trusting"); JA `test_api_limits.py`; MyLibra M13 |
| O5 | Error monitoring tool and uptime monitor: **not found in siblings** (summonlibrary privacy mentions "錯誤監控" without naming a tool; riftbound gate says "check Cloudflare Worker errors and Supabase logs for the first 30 minutes"). | riftbound gate; summonlibrary `/privacy` section 10 |

## 2. Gap analysis: Journal Atlas as found on 2026-11-23

Evidence for the "now" column: live fetches of `https://journal-atlas.chroniclecore.com/`
and `https://api.journal-atlas.chroniclecore.com/`, plus `demo/` at the branch
base. Priority: **P0** truthfulness or something that misleads people or
crawlers; **P1** the common spec's core; **P2** polish; **D** needs a decision
(Part 3). Status is as of the last commit on this branch.

| ID | JA now | Pri | Status |
|---|---|---|---|
| T-live | `App.tsx` hard-codes corpus numbers in 7 places (399, 236, 88%, 106, 40%, 100%); the corpus is growing (live API says 399, the maintainer's branch is further on), so each is already wrong or about to be | P0 | done |
| T-models | Provider and model names are not on the page; they change | P0 | done |
| T-human | No statement of how many entries carry first-hand human evidence; footer says "none human-verified" for philosophy only | P0 | done |
| T7 | No AI-disclosure page | P0 | done |
| T9 | No privacy statement. The page sends the pasted text to a third-party model provider (Anthropic at the time of writing, from `/api/health`) | P0 | done |
| S9 | Every unknown path, `robots.txt`, `sitemap.xml`, `llms.txt`, `manifest.webmanifest` returns the SPA shell with 200 (verified by curl: 8,255 bytes each) | P0 | done |
| S4, S5, S6 | No `robots.txt`, `sitemap.xml`, `llms.txt` (see S9) | P1 | done |
| S1, S2 | `<title>Journal Atlas</title>` only; no description, canonical, OG, twitter, JSON-LD, `theme-color`, apple-touch-icon | P1 | done |
| T8, T1 | One page. No About; no studio attribution | P1 | done |
| T2 | No non-endorsement line for the journals, publishers and data providers it names; no "research prototype / AI-assisted" mark near the brand | P1 | done |
| T4 | No licence line on the site | P1 | done |
| T6 | Contact is "Report something wrong" (GitHub issues) only, which is the instruction for this task | P1 | done |
| T11 | No status page; `/healthz` and `/api/health` exist but are not surfaced | P2 | done |
| T3 | Declarations live in three JSX blocks and the README; no single source | P1 | done |
| P3 | Live headers: only `nosniff` and `referrer-policy` (no CSP, HSTS, `X-Frame-Options`, `Permissions-Policy`) | P1 | done |
| P2 | Hashed assets get `max-age=14400, must-revalidate`, not `immutable` | P2 | done |
| A1, A2 | No skip link; no `<main>`; textarea focus ring is a 15% alpha shadow with `outline: none`; button has no visible ring | P1 | done |
| A3 | Several grey and lilac text colours below 4.5:1 on white (to be measured, not estimated) | P1 | done |
| A5 | Copy button and small controls under 44 px | P2 | done |
| A6 | Pulse and fade animations ignore `prefers-reduced-motion` | P2 | done |
| A7 | Errors and stage changes are not announced; stage state is colour-only | P1 | done |
| A8 | Coverage table has no `scope` on headers | P2 | done |
| D1 | Colours are 110 hex literals (80 distinct) in `App.css`; no tokens; dark mode by media query only | P2 | done |
| D4 | No error boundary: a render error blanks the page | P2 | done |
| S10 | Prerender covers the home page only; one `<h1>` there | P1 | done |
| S8 | Favicon SVG only | P2 | done |
| O2 | Gates exist in `demo/README`/`DEPLOY.md` prose, not as a script | P1 | done |
| O4 | `test_frontend_and_readme_report_the_same_concentration` ties README to the API; nothing stops a number being typed back into the front end | P1 | done |
| P1 | No size check; first-load JS is 328 KB (103 KB gzip), measured | P2 | done |
| S12 | English only; `README.zh-Hant.md` exists | D | done 2026-11-23, decision 11: Traditional Chinese under `/zh-hant/`, same five pages plus a 404, `hreflang` pairs and `x-default`, sitemap alternates, language-aware `<html lang>`/`og:locale`/JSON-LD. Prose pages are one component per language (`src/pages/zh-Hant/`), Home and Status read a language table (`src/locales/`). The gate fails on: a page missing in a language, different headings/sections/paragraphs/list items/table cells/ids/links from the English one, a link crossing languages, no hreflang pair, "verified by a human/expert" wording in either language. **The Chinese is a translation by the drafting model and has not been read by the maintainer; the footer says the English wins.** Backend messages (rate-limit refusals, errors) and the recommendation text are not translated |
| M1 | None. Nothing to configure | D | n/a by constraint |
| M2 | No ads. Policy not written down | D | open |
| S7 | No `ads.txt` (correct while there are no ads) | n/a | n/a |
| S11 | No IndexNow | D | decided 2026-11-23: not done |
| T10 | No terms page (siblings only have one where there are accounts or payment) | n/a | n/a |
| O3 | `npm audit` not run on a schedule | P2 | done: `.github/workflows/npm-audit.yml` (monthly, opens one issue). Workflow YAML parses; not run on GitHub (not pushed); `npm audit` run locally: 0 vulnerabilities |
| O5 | No uptime monitor or error monitor | D | done for uptime: `.github/workflows/site-health.yml` (daily smoke test of the live site, opens one issue; off until repository variable `SITE_HEALTH_ENABLED=true` after deploy). Not run on GitHub. No error-monitoring tool, by decision 10 (none of the siblings has one) |

**What "done" means here.** Implemented on this branch and checked by
`npm run build` (which runs `scripts/check-site.mjs`: pages, tokens, worker
headers over `dist/` through a Pages emulator, sitemap, bundle rules), by
`pytest demo/backend/tests`, and by loading every page in headless Chromium
through the real worker code, in light and dark and at 390 px, with no console
error, CSP violation or hydration warning (the 404 page logs the browser's own
"404" resource line). **Not verified:** behaviour on Cloudflare itself (the
emulator follows the documented Pages behaviour, it is not Cloudflare), the
new `/api/coverage` fields on the deployed API (it predates them; the pages
degrade to wording without the figures, checked against the live JSON), real
Core Web Vitals (no field data; the only measured number is bundle size:
JS 107.8 KB and CSS 3.7 KB gzip), and screen-reader behaviour (no screen
reader was run; the markup follows A1-A9). Run `node scripts/smoke.mjs <url>`
after deploying. Before this branch the same script, run against the live
site, failed 13 of 30 checks (no canonical, CSP, HSTS, robots/sitemap/llms
answered by the SPA shell with 200, unknown URL answered 200).

## 3. Decisions for the maintainer

Written up here, not decided or built.

1. **Contact mailbox.** DECIDED 2026-11-23: show a project mailbox,
   `journal-atlas@chroniclecore.com`, one value in `site.ts`; the build gate
   fails for any address not on chroniclecore.com. **The alias must exist and
   forward before deploy.** Original description follows. Four of five siblings expose a project mailbox
   (`<site>@chroniclecore.com`) and the siblings' `check` scripts forbid typing
   it into prose. This task said "no maintainer email, GitHub issues unless the
   siblings do otherwise". They do, partly. Built with GitHub issues only, and
   with one config value (`SITE.contact`) that renders a mailbox if you set it.
   Options: keep GitHub-only (zero spam surface, but researchers without GitHub
   accounts cannot reach you, and the footer already worries about exactly that
   for payments); or create `journal-atlas@chroniclecore.com` as an alias.
2. **Analytics.** DECIDED 2026-11-23: anonymous first-party totals on the API
   only (`demo/backend/usage.py`, public `GET /api/usage`, shown on the Status
   page, disclosed on the Privacy page). Per UTC day: searches, how each ended,
   field directory of the best match, follow-ups. No address, no text, no
   identifier; in memory, restarts from zero with the process. No third party,
   no cookie, no script. Needs a backend restart to take effect. Tests:
   `demo/backend/tests/test_usage.py`. Original description follows. Siblings split: none (basesmall, smallol), first-party
   de-identified (summonlibrary), consented PostHog (riftbound). Built: none.
   Options: stay at none and learn nothing about use; first-party counters on
   the API only (no third party, still visitor data, needs a privacy line); or
   a consented tool. Any of the last two needs your yes.
3. **Ads.** DECIDED 2026-11-23: stay with no ads and write no policy. Nothing
   changed; the footer line and the build gate stay. Original description
   follows. Siblings: riftbound dormant AdSense account, TechnologyStackMap
   env-gated. JA is a tool whose product is trust in a recommendation, which by
   `ccweb-ads` section 5 is a "trust page" where ads cost more than they earn.
   Built: "no ads" is stated on the site. Say if that should change.
4. **IndexNow, Search Console, Bing Webmaster.** DECIDED 2026-11-23: IndexNow not done. Search Console and Bing Webmaster were not raised and are not done. Outward-facing.
5. **A zh-Hant interface.** Three siblings ship a second language. JA's
   audience is international researchers, but `README.zh-Hant.md` exists.
   CORRECTION (2026-11-23): an earlier draft said the page text lives in one
   module so a translation is only a data change. That was wrong. Site-wide facts
   (names, URLs, licences) are in `site.ts`, but the prose of every page is JSX
   in `src/pages/*.tsx` (about 2,000 lines, with inline links and live figures).
   A second language needs that prose extracted into per-language dictionaries
   first, then translated and reviewed by the maintainer.
6. **Content licence wording.** DECIDED 2026-11-23: CC BY-SA 4.0 stands (the
   2026-05-18 change documented in `LICENSE`). `AGENTS.md` was the stale file;
   its two NC-SA lines were corrected (workspace file, not in git). No other
   file in the repo still names NC-SA as the current licence.
7. **The human-evidence statement.** DECIDED 2026-11-23: count it by code, not
   by hand. That needs a structured "First-hand reports" field in the entries,
   which is content/schema work for the content session (proposal handed over in
   the shared notes folder, `site-session-handover-first-hand-field.md`). Until the
   field exists the number stays 0 by hand, dated. A text-pattern gate was tried
   on paper and rejected: all 5 files that match "first-hand experience" in the
   current corpus match a negative statement, so it would count absence as
   presence. Original description follows. "0 of N entries carry a first-hand human
   report, no external contributors yet" is not derivable from the corpus. It is
   recorded by hand in `demo/backend/main.py` with a date, like `absent_checked`
   already is, and printed with that date. Someone has to change it when the
   first outside contribution lands. Also check the wording against
   `SEED_DATA_QUALITY.md`, which describes Tier 1 as built from "author
   submission research": that reads as first-hand experience of the maintainer,
   and the page says only what you told me, which is that no entry records a
   first-hand report.
8. **Strict CSP.** DECIDED 2026-11-23: keep enforcing; run `npm run smoke`
   right after deploy; fall back to `Report-Only` with the one-line switch below
   if it shows a console error. Original description follows. Built and enforced in the Pages worker (`public/_worker.js`).
   It was tested against the built pages and with a headless browser through the
   worker code, not on Cloudflare. If the first post-deploy smoke test shows a
   console CSP error, switch the header name to `Content-Security-Policy-Report-Only`
   in one line while you look.
9. **Header badge.** DECIDED 2026-11-23: keep as is. Original description
   follows. A short "research prototype, AI-assisted" tag sits next to the
   brand. Remove it if you think it undersells the project.
10. **What the AI page says about who wrote what.** DECIDED 2026-11-23: keep
    as is (basis of evidence, no claim about who typed an entry). Open for the
    content session: `SEED_DATA_QUALITY.md` describes Tier 1 as built from "author
    submission research", which reads as the maintainer's first-hand experience;
    the maintainer says in practice it was his direction plus multi-round AI
    research, with no first-hand human information. The site does not repeat that
    phrase. Original description follows. It states the basis of each
    part (code by Claude models, per the commit trailers; AI-Researched by a
    per-journal AI run; Tier 2 as family-level estimates; Tier 1 as evidenced)
    and says outright that it makes no claim about who typed an individual
    Tier 1 or Tier 2 entry. If you want it to say more (for example that the
    Tier 1 entries come from your own submission research), that is a sentence
    you add. It names no agent personas and describes no orchestration, per the
    red lines in `AGENTS.md`.
11. **About page, first person (found during review).** The first draft had the
    maintainer saying "I had manuscripts to place" and "I started writing down
    what that colleague would have said", neither approved, the second
    contradicting "0 first-hand reports". DECIDED 2026-11-23: keep only the facts,
    his own need ("I had to choose where to submit my research"), and that
    coming across the Open Journal Matcher made him want to carry its ideas
    forward. Rewritten accordingly. The clause "built so the knowledge outlives any
    one person" is the drafter's wording of that idea (it echoes the OJM section
    below it); say if it should go.
12. **Nothing was deployed, pushed or enabled.** No wrangler, no VPS change, no
    third-party analytics, no ads, no accounts or keys. Two things need a deploy to take
    effect: the Pages build (frontend) and a backend restart (the
    `/api/coverage` additions and `/api/usage`).

### Deployment state (2026-11-25)

- **Merged.** PR #2 (this site) into `main` as a merge commit; `main` also holds
  the content PR #3 (493 entries; tiers named Sourced, Estimated,
  AI-Researched).
- **Backend: live from a clean copy of `main`.** Deployed with the Outpost
  deploy script unchanged except for `SOURCE`, which pointed at a detached
  checkout of `main` instead of the shared main checkout (that one is a content
  session's working copy). The live API reports 493 entries, the tier totals,
  the dated human-evidence record (0 first-hand reports, 0 outside
  contributors, recorded 2026-11-23) and `/api/usage`.
- **Frontend: live, built from the same `main`.** Both went out together so the
  pages and the API use the same tier names.
- **Cloudflare Web Analytics stays on** (maintainer, 2026-11-24). Cloudflare
  injects its beacon into browser requests; the CSP (`script-src 'self'`)
  blocks it, so nothing loads and the footer's "loads no analytics" stays true.
  `scripts/smoke.mjs` reports that one line as **EXPECTED**, not as a pass and
  not hidden, and only while the beacon is the sole third-party script and the
  CSP still blocks it; anything else is a failure.
- **Topic vocabulary gate.** The committed `topic_vocabulary.json` was 155
  topics short of the corpus (second time; the first was 2026-09-03), which also
  made the deploy record a "-dirty" version. It was regenerated, and
  `demo/backend/tests/test_topic_vocabulary.py` now fails CI when it drifts.
- **Open: the home page's product shot.** It still shows the recorded run on
  the 399-entry corpus (captioned with that version and date, so it is true as
  a record). Re-recorded on the 493-entry corpus, the same example ranks two
  unrelated Sourced journals at 30 % evidence second and third. Which run the
  home page shows is the maintainer's call (it is honest either way, and the
  newer one shows the scorer's current weakness on the first screen).

### Before deploying (maintainer's actions)

1. DONE 2026-11-23: the Email Routing rule `journal-atlas@chroniclecore.com`
   exists and is active, forwarding to the same verified address as the six
   sibling aliases (created in the Cloudflare dashboard at the maintainer's
   request). Not yet tested end to end: send one message to it and check it
   arrives.
2. Read the Chinese pages (`src/pages/zh-Hant/`, `src/locales/`); they have
   not been read by a human. Anything that says more, or less, than the English
   is a bug.
3. Build with `VITE_API_BASE` unset only if the API is the production one
   (`npm run build` refuses a build that points at localhost unless
   `ALLOW_LOCAL_API=1`).
4. After the deploy: `npm run smoke -- https://journal-atlas.chroniclecore.com`
   (64 checks, both languages). Then set the repository variable
   `SITE_HEALTH_ENABLED=true` to switch the daily live-site check on.
5. Restart the backend so `/api/coverage` (`tiers`, `human_evidence`) and
   `/api/usage` exist; the pages degrade to wording without the figures until
   then.
6. The CSP is enforced. If the smoke test or the console shows a CSP error,
   rename the header in `public/_worker.js` to
   `Content-Security-Policy-Report-Only` and redeploy while you look.

7. The home page's product shot and the "not stated" lines are a recorded
   screening run (`demo/frontend/src/sample/screening-sample.json`), captioned
   with its corpus version and date. After the corpus changes (for example when
   the content branches are merged), re-run
   `python demo/backend/make_hero_sample.py` and rebuild, so the picture
   matches the corpus the site serves.

### Home page as a product page (decision 13, 2026-11-23)

The maintainer judged the first version a wall of text with no visual, no hook
and no call to action, and asked whether the sibling product pages had really
been used. They had been read only as a compliance checklist, not as product
pages; that was the gap. The home page now follows the basesmall / SmalLoL
product-page structure, with one change he asked for: the tool stays in the
first screen.

- Hero: kicker, a one-line hook, one sentence, the paste box with a solid
  primary button ("Find my journal") and a secondary one ("Install the skill"),
  and on the right a real screening result in a browser frame with a caption
  naming the corpus and date. On a phone the tool comes first.
- Three feature rows, each a short claim and a picture of real output
  (tier legend and score from the recorded run; fields with no entries, live
  from `/api/coverage`; the backend's own "not stated" lines; the install
  command).
- One contribution band with two buttons, five folded questions that hold what
  used to be four long paragraphs, and a one-line close.
- The example paper is neutral (older adults and voice assistants), not
  related to any manuscript of the maintainer; the old placeholder
  (autoethnography, embodied cognition) was replaced for the same reason.
- The recorded run's top three are all Tier 2 at 65 % evidence coverage. That is
  what the scorer returns today and is shown as is; the example was not chosen
  to make the picture look better.

### Decided not to do

- **IndexNow** (decision 12, 2026-11-23): not done. Crawlers will find the
  sitemap on their own.
- **Ads, third-party analytics, an error-monitoring tool**: not done (decisions
  3, 4, 10).
