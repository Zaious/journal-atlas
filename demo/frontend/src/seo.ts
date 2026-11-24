/**
 * The strings prerender.js writes outside the React tree: each page's <head>,
 * sitemap.xml, robots.txt and llms.txt. They are built from site.ts so the
 * title a visitor sees, the title a crawler reads and the line in llms.txt are
 * one value, not three (docs/status/SITE_SPEC.md, T3 and S1-S6).
 *
 * Nothing here knows a corpus count or a model name. A crawler gets the same
 * thing a reader does before the API answers: a description of what the site
 * is, and a pointer to where the live figures are.
 */
import { DEFAULT_LANG, LANGS, LANG_TAG, OG_LOCALE, localePath } from "./i18n";
import { OG_IMAGE_ALT } from "./locales/meta";
import { PAGES, SITE, absoluteUrl, pageInLang, type PageMeta } from "./site";

const esc = (s: string) =>
  s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

/** JSON for a <script type="application/ld+json">: `<` escaped so "</script>" cannot appear. */
const jsonForScript = (o: unknown) => JSON.stringify(o, null, 2).replace(/</g, "\\u003c");

const authorNode = {
  "@type": "Person",
  "@id": `${SITE.url}/#author`,
  name: SITE.author.name,
  alternateName: SITE.author.handle,
  url: SITE.author.url,
};

const studioNode = {
  "@type": "Organization",
  "@id": `${SITE.studio.url}/#organization`,
  name: SITE.studio.name,
  alternateName: SITE.studio.nameZh,
  url: SITE.studio.url,
};

/**
 * The paper that describes the system. The @id is its DOI URL, which resolves
 * (checked 2026-11-24); the Zenodo snapshot is the archived state it describes.
 * No date beyond the year, because the exact publication date was not checked.
 */
const paperNode = {
  "@type": "ScholarlyArticle",
  "@id": SITE.paper.doiUrl,
  headline: SITE.paper.title,
  name: SITE.paper.title,
  url: SITE.paper.doiUrl,
  sameAs: [SITE.paper.snapshotUrl],
  datePublished: SITE.paper.year,
  author: { "@id": authorNode["@id"] },
  isPartOf: { "@type": "PublicationEvent", name: SITE.paper.venueFull },
};

/**
 * Structured data that says only what the page shows. No ratings, no
 * `SearchAction` (there is no public search endpoint), no FAQPage (Google
 * retired the rich result 2026-05-07), no `offers` beyond "free", which is
 * true. `sameAs` lists URLs fetched anonymously and found to return 200.
 */
export function jsonLd(page: PageMeta): object[] {
  const url = absoluteUrl(page.path);
  // Each language is its own site root for structured data, so the English and
  // Chinese home pages describe themselves rather than each other.
  const home = absoluteUrl(localePath(page.lang, "/"));
  if (page.id === "home") {
    return [
      {
        "@context": "https://schema.org",
        "@graph": [
          {
            "@type": "WebSite",
            "@id": `${home}#website`,
            name: SITE.name,
            url: home,
            inLanguage: LANG_TAG[page.lang],
            publisher: { "@id": studioNode["@id"] },
          },
          {
            "@type": "WebApplication",
            "@id": `${home}#app`,
            name: SITE.name,
            url: home,
            inLanguage: LANG_TAG[page.lang],
            description: page.description,
            applicationCategory: "ReferenceApplication",
            browserRequirements: "Requires JavaScript",
            isAccessibleForFree: true,
            offers: { "@type": "Offer", price: "0", priceCurrency: "USD" },
            license: SITE.license.contentUrl,
            author: { "@id": authorNode["@id"] },
            publisher: { "@id": studioNode["@id"] },
            isBasedOn: SITE.repoUrl,
            subjectOf: { "@id": SITE.paper.doiUrl },
          },
          paperNode,
          { ...authorNode, sameAs: [SITE.author.url, "https://github.com/Zaious"] },
          studioNode,
        ],
      },
    ];
  }
  if (page.id === "about") {
    return [
      {
        "@context": "https://schema.org",
        "@type": "AboutPage",
        name: page.title,
        url,
        inLanguage: LANG_TAG[page.lang],
        isPartOf: { "@id": `${home}#website` },
        about: { "@id": `${home}#app` },
        author: { ...authorNode, sameAs: [SITE.author.url, "https://github.com/Zaious"] },
        citation: paperNode,
      },
    ];
  }
  return [];
}

/** Everything that goes between <head> and </head> except the built asset tags. */
export function headTags(page: PageMeta): string {
  const url = absoluteUrl(page.id === "notfound" ? localePath(page.lang, "/") : page.path);
  const img = absoluteUrl(SITE.ogImage);
  // Language alternates only where the page is indexable: a noindex page or a
  // 404 has no use for them, and an alternate that points at a noindex page is
  // a broken pair.
  const alternates = page.noindex
    ? []
    : [
        ...LANGS.map(
          (l) => `<link rel="alternate" hreflang="${LANG_TAG[l]}" href="${esc(absoluteUrl(pageInLang(page, l).path))}" />`,
        ),
        `<link rel="alternate" hreflang="x-default" href="${esc(absoluteUrl(pageInLang(page, DEFAULT_LANG).path))}" />`,
      ];
  const otherLocales = page.noindex
    ? []
    : LANGS.filter((l) => l !== page.lang).map(
        (l) => `<meta property="og:locale:alternate" content="${OG_LOCALE[l]}" />`,
      );
  const lines = [
    `<title>${esc(page.title)}</title>`,
    `<meta name="description" content="${esc(page.description)}" />`,
    page.noindex
      ? `<meta name="robots" content="noindex, follow" />`
      : `<meta name="robots" content="index, follow, max-image-preview:large" />`,
    // A 404 page is served at whatever URL was mistyped, so it must not claim one.
    ...(page.id === "notfound" ? [] : [`<link rel="canonical" href="${esc(url)}" />`]),
    ...alternates,
    `<meta name="theme-color" content="${SITE.themeColor}" />`,
    `<link rel="icon" type="image/svg+xml" href="/favicon.svg" />`,
    `<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png" />`,
    `<link rel="apple-touch-icon" href="/apple-touch-icon.png" />`,
    `<meta property="og:type" content="website" />`,
    `<meta property="og:site_name" content="${esc(SITE.name)}" />`,
    `<meta property="og:locale" content="${OG_LOCALE[page.lang]}" />`,
    ...otherLocales,
    `<meta property="og:title" content="${esc(page.title)}" />`,
    `<meta property="og:description" content="${esc(page.description)}" />`,
    `<meta property="og:url" content="${esc(url)}" />`,
    `<meta property="og:image" content="${esc(img)}" />`,
    `<meta property="og:image:width" content="1200" />`,
    `<meta property="og:image:height" content="630" />`,
    `<meta property="og:image:alt" content="${esc(OG_IMAGE_ALT[page.lang])}" />`,
    `<meta name="twitter:card" content="summary_large_image" />`,
    `<meta name="twitter:title" content="${esc(page.title)}" />`,
    `<meta name="twitter:description" content="${esc(page.description)}" />`,
    `<meta name="twitter:image" content="${esc(img)}" />`,
    ...jsonLd(page).map((o) => `<script type="application/ld+json">\n${jsonForScript(o)}\n</script>`),
  ];
  return lines.join("\n    ");
}

const indexable = () => PAGES.filter((p) => !p.noindex);

export function sitemapXml(lastmod: (page: PageMeta) => string | null): string {
  const urls = indexable()
    .map((p) => {
      const lm = lastmod(p);
      // Every URL lists the full set of its language versions, itself included,
      // as hreflang requires, plus x-default.
      const alternates = [
        ...LANGS.map((l) => ({ hreflang: LANG_TAG[l], href: absoluteUrl(pageInLang(p, l).path) })),
        { hreflang: "x-default", href: absoluteUrl(pageInLang(p, DEFAULT_LANG).path) },
      ]
        .map((a) => `\n    <xhtml:link rel="alternate" hreflang="${a.hreflang}" href="${esc(a.href)}" />`)
        .join("");
      return `  <url>\n    <loc>${esc(absoluteUrl(p.path))}</loc>${lm ? `\n    <lastmod>${lm}</lastmod>` : ""}${alternates}\n  </url>`;
    })
    .join("\n");
  return `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n${urls}\n</urlset>\n`;
}

/**
 * Everything is crawlable. There are no private routes to disallow: the API is
 * on another host, and the status page is kept out of results with `noindex`
 * rather than by robots.txt, because a disallowed URL cannot be crawled to read
 * its noindex. No per-bot groups: under RFC 9309 a named group replaces `*`
 * entirely, so adding one later means copying every rule into it.
 */
export function robotsTxt(): string {
  return `User-agent: *\nAllow: /\n\nSitemap: ${SITE.url}/sitemap.xml\n`;
}

/**
 * For systems that read llms.txt. Google does not use it; it costs nothing and
 * is kept short and free of figures that would go stale. Structure follows the
 * sibling sites' files: summary, authoritative scope, what is not provided,
 * key pages, attribution.
 */
export function llmsTxt(): string {
  const pageLine = (p: PageMeta) => `- [${p.title}](${absoluteUrl(p.path)}): ${p.description}`;
  return `# ${SITE.name}

> Journal Atlas is an open, community-maintainable knowledge base about where academic papers fit (journals and conferences), plus a demo that scores a pasted paper description against it and shows, for every candidate, how well that entry is evidenced. It is a research project by ${SITE.author.handle}, a ${SITE.studio.name} production, and much of it is written by AI.

## Authoritative scope

- Every entry carries a tier that says how it was written: Sourced (each claim cites a source), Estimated (family-level estimate, not sourced per journal), AI-Researched (per-journal AI research with sources and blanks). A tier is not a statement that anyone who knows the venue has checked the entry.
- How many entries record a first-hand report from someone who submitted to or reviewed for a venue is stated, with its date, in the live API at ${SITE.apiUrl}/api/coverage (field \`human_evidence\`). Do not describe an entry as verified, expert-reviewed or human-checked unless the entry itself says so.
- Corpus size, per-field and per-tier counts, the corpus version, and the models that run the demo are served live at ${SITE.apiUrl}/api/coverage and ${SITE.apiUrl}/api/health. This file states none of them because they change.
- Many fields are not covered at all; the live coverage record lists which. The demo says so instead of ranking the nearest journals it happens to hold.
- Journal and conference names belong to their owners. Entries describe venues from public sources and are not statements by the venues. No venue endorses this project.

## Pages

${PAGES.filter((p) => p.lang === DEFAULT_LANG && p.id !== "notfound").map(pageLine).join("\n")}

## Paper

${SITE.paper.author}. ${SITE.paper.year}. ${SITE.paper.title}. ${SITE.paper.venueFull}, ${SITE.paper.track} track.

- [Paper (ACM Digital Library)](${SITE.paper.doiUrl})
- [Archived state the paper describes (Zenodo)](${SITE.paper.snapshotUrl}); also the tag \`jcdl2026\` in the repository
- The corpus has grown since; the live API reports which version it serves.

## Translations

The same pages exist in Traditional Chinese under ${SITE.url}/zh-hant/ ; the English pages are the original and win where the two differ. The translations carry the same claims and no stronger ones. The recommendation text the demo writes is produced by a model from English-language entries; this site does not translate it.

## Source

- [Repository and knowledge base](${SITE.repoUrl}): one Markdown file per venue, scoring script, licences
- [Issues](${SITE.repoUrl}/issues): corrections, contributions, co-maintainers${SITE.contact.email ? `\n- Project mailbox: ${SITE.contact.email} (for people who do not use GitHub)` : ""}

## Attribution

Knowledge base: ${SITE.license.content}. Code: ${SITE.license.code}. Link back to the page you cite, name the project, and do not present entries as official statements of a journal.
`;
}
