/**
 * Everything the site says about itself, defined once.
 *
 * The footer, the About page, the JSON-LD, llms.txt and the sitemap all read
 * from here, so a changed URL or a new page is one edit and not a grep. This
 * is the same rule the sibling sites follow (see docs/status/SITE_SPEC.md,
 * item T3): a declaration that is typed in five places drifts in four of them.
 *
 * No corpus numbers and no model names belong in this file. Those are live,
 * from /api/coverage and /api/health, and a test fails the build if one is
 * typed into the front end.
 */

import { DEFAULT_LANG, LANGS, langOfPath, localePath, stripLang, type Lang } from "./i18n";
import { PAGE_TEXT, type PageId } from "./locales/meta";

export const SITE = {
  name: "Journal Atlas",
  url: "https://journal-atlas.chroniclecore.com",
  /** The API origin the CSP in public/_worker.js allows. Keep the two equal;
   *  scripts/check-site.mjs compares them. */
  apiUrl: "https://api.journal-atlas.chroniclecore.com",
  repoUrl: "https://github.com/Zaious/journal-atlas",
  studio: {
    name: "ChronicleCore Studio",
    nameZh: "編年史記工作室",
    url: "https://studio.chroniclecore.com",
  },
  author: {
    name: "Meng-Han Lee",
    handle: "Zaious",
    url: "https://zaious.dev/",
  },
  /**
   * Corrections and contributions go through GitHub issues, in public. The
   * project mailbox is for people who do not use GitHub. It is the only e-mail
   * address the site may show, and scripts/check-site.mjs fails the build if
   * another one appears or if this one is not on chroniclecore.com (so a
   * personal address cannot be put here by mistake). Decided 2026-11-23
   * (docs/status/SITE_SPEC.md, decision 1).
   *
   * The alias must exist and forward to the maintainer BEFORE the site that
   * shows it is deployed; until then mail to it bounces. Set to undefined to
   * hide it again.
   */
  contact: { email: "journal-atlas@chroniclecore.com" as string | undefined },
  /**
   * Buy Me a Coffee rather than GitHub Sponsors: sponsoring on GitHub needs the
   * *sponsor* to hold a GitHub account, and this audience (psychology and
   * philosophy researchers) mostly does not. Defaulted rather than required, so
   * a deployment that forgets the env var still shows the link; an empty string
   * turns it off.
   */
  supportUrl: (import.meta.env.VITE_SUPPORT_URL as string | undefined) ?? "https://buymeacoffee.com/zaious",
  supportLabel: (import.meta.env.VITE_SUPPORT_LABEL as string | undefined) ?? "Buy me a coffee",
  license: {
    content: "CC BY-SA 4.0",
    contentUrl: "https://creativecommons.org/licenses/by-sa/4.0/",
    code: "MIT",
    codeUrl: "https://github.com/Zaious/journal-atlas/blob/main/LICENSE-CODE",
  },
  /**
   * The paper that describes the system, as README.md cites it. All three links
   * were fetched anonymously on 2026-11-24 and resolve (doi.org 302 to ACM DL and
   * Zenodo; the tag page 200). The snapshot DOI is the version DOI of the
   * `jcdl2026` release, not the concept DOI, so it does not drift with the corpus.
   */
  paper: {
    title: "Journal Atlas: Venue Fit Scoring Under Incomplete Evidence, and the Corpus Method It Requires",
    author: "Meng-Han Lee",
    year: "2026",
    venue: "JCDL 2026",
    venueFull: "ACM/IEEE Joint Conference on Digital Libraries (JCDL 2026)",
    track: "Demonstrations",
    doiUrl: "https://doi.org/10.1145/3805696.3846515",
    snapshotUrl: "https://doi.org/10.5281/zenodo.22272331",
    tagUrl: "https://github.com/Zaious/journal-atlas/releases/tag/jcdl2026",
  },
  /** Matches `--bg` in index.css, light theme. */
  themeColor: "#ffffff",
  ogImage: "/og.png",
} as const;

export const ISSUES_URL = `${SITE.repoUrl}/issues`;

export type { PageId };

export interface PageMeta {
  id: PageId;
  lang: Lang;
  /** Canonical path, with a trailing slash except for the root and the 404 file. */
  path: string;
  title: string;
  description: string;
  /** Linked from the header and footer. */
  navLabel?: string;
  /** Kept out of search results and out of the sitemap. */
  noindex?: boolean;
  /** Source files whose last commit date is the page's `lastmod`. */
  sources: string[];
}

/** What is the same for a page in every language. */
interface PageBase {
  id: PageId;
  /** Language-neutral path; the language prefix is added by `localePath`. */
  path: string;
  noindex?: boolean;
  sources: Record<Lang, string[]>;
}

const BASE: PageBase[] = [
  {
    id: "home",
    path: "/",
    sources: {
      en: ["src/pages/Home.tsx", "src/App.tsx", "src/locales/home.tsx"],
      "zh-Hant": ["src/pages/Home.tsx", "src/App.tsx", "src/locales/home.tsx"],
    },
  },
  {
    id: "about",
    path: "/about/",
    sources: { en: ["src/pages/About.tsx"], "zh-Hant": ["src/pages/zh-Hant/About.tsx"] },
  },
  {
    id: "ai",
    path: "/ai/",
    sources: { en: ["src/pages/Ai.tsx"], "zh-Hant": ["src/pages/zh-Hant/Ai.tsx"] },
  },
  {
    id: "privacy",
    path: "/privacy/",
    sources: { en: ["src/pages/Privacy.tsx"], "zh-Hant": ["src/pages/zh-Hant/Privacy.tsx"] },
  },
  {
    id: "status",
    path: "/status/",
    noindex: true,
    sources: { en: ["src/pages/Status.tsx"], "zh-Hant": ["src/pages/Status.tsx", "src/locales/status.tsx"] },
  },
  {
    id: "notfound",
    path: "/404.html",
    noindex: true,
    sources: { en: ["src/pages/NotFound.tsx"], "zh-Hant": ["src/pages/NotFound.tsx"] },
  },
];

/** Every page in every language, English first. */
export const PAGES: PageMeta[] = LANGS.flatMap((lang) =>
  BASE.map((b) => ({
    id: b.id,
    lang,
    // The English 404 is /404.html, which Cloudflare Pages serves for any unknown
    // URL. Pages rewrites `x.html` to `x`, so the worker cannot rely on that name
    // for another language; the Chinese one is a directory page it fetches itself.
    path: b.id === "notfound" && lang !== DEFAULT_LANG ? localePath(lang, "/404/") : localePath(lang, b.path),
    ...PAGE_TEXT[lang][b.id],
    noindex: b.noindex,
    sources: b.sources[lang],
  })),
);

export function pageForPath(pathname: string): PageMeta | undefined {
  const lang = langOfPath(pathname);
  const clean = stripLang(pathname).replace(/index\.html$/, "");
  const withSlash = clean.endsWith("/") ? clean : `${clean}/`;
  return PAGES.find((p) => p.lang === lang && p.id !== "notfound" && stripLang(p.path) === withSlash);
}

/** The page for a URL path; anything unknown is the 404 page in that path's language. */
export function resolvePage(pathname: string): PageMeta {
  const found = pageForPath(pathname);
  if (found) return found;
  const lang = langOfPath(pathname);
  return PAGES.find((p) => p.lang === lang && p.id === "notfound")!;
}

/** The same page in another language. */
export function pageInLang(page: PageMeta, lang: Lang): PageMeta {
  return PAGES.find((p) => p.lang === lang && p.id === page.id)!;
}

export { DEFAULT_LANG };

export const absoluteUrl = (path: string) => `${SITE.url}${path}`;
