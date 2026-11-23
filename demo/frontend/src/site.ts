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
  /** Matches `--bg` in index.css, light theme. */
  themeColor: "#ffffff",
  ogImage: "/og.png",
  ogImageAlt: "Journal Atlas: journal fit with the evidence shown",
} as const;

export const ISSUES_URL = `${SITE.repoUrl}/issues`;

export type PageId = "home" | "about" | "ai" | "privacy" | "status" | "notfound";

export interface PageMeta {
  id: PageId;
  /** Canonical path, with a trailing slash except for the root. */
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

export const PAGES: PageMeta[] = [
  {
    id: "home",
    path: "/",
    title: "Journal Atlas: journal fit with the evidence shown",
    description:
      "Describe your paper and get journal and conference candidates scored against an open knowledge base. Every result shows how well each entry is evidenced.",
    sources: ["src/pages/Home.tsx", "src/App.tsx"],
  },
  {
    id: "about",
    path: "/about/",
    title: "About Journal Atlas",
    description:
      "What Journal Atlas is, who maintains it, why it exists, and where to report a wrong entry.",
    navLabel: "About",
    sources: ["src/pages/About.tsx"],
  },
  {
    id: "ai",
    path: "/ai/",
    title: "How Journal Atlas is made, and what is AI",
    description:
      "Which parts of Journal Atlas are written by AI, which models run the demo, what no entry yet records, and what the project will not claim.",
    navLabel: "How it's made",
    sources: ["src/pages/Ai.tsx"],
  },
  {
    id: "privacy",
    path: "/privacy/",
    title: "Privacy: what happens to the text you paste",
    description:
      "The text you paste is sent to a model provider to be read. This page says what is kept, what is not, and which third parties are involved.",
    navLabel: "Privacy",
    sources: ["src/pages/Privacy.tsx"],
  },
  {
    id: "status",
    path: "/status/",
    title: "Status",
    description: "Live status of the Journal Atlas demo: API reachability, models, daily limits and corpus version.",
    navLabel: "Status",
    noindex: true,
    sources: ["src/pages/Status.tsx"],
  },
  {
    id: "notfound",
    path: "/404.html",
    title: "Page not found",
    description: "This address does not exist on Journal Atlas. Try the home page, the About page, or report a broken link.",
    noindex: true,
    sources: ["src/pages/NotFound.tsx"],
  },
];

export function pageForPath(pathname: string): PageMeta | undefined {
  const clean = pathname.replace(/index\.html$/, "");
  const withSlash = clean.endsWith("/") ? clean : `${clean}/`;
  return PAGES.find((p) => p.path === withSlash && p.id !== "notfound");
}

/** The page for a URL path; anything unknown is the 404 page. */
export function resolvePage(pathname: string): PageMeta {
  return pageForPath(pathname) ?? PAGES.find((p) => p.id === "notfound")!;
}

export const absoluteUrl = (path: string) => `${SITE.url}${path}`;
