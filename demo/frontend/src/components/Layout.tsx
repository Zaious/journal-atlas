import type { ReactNode } from "react";
import { DEFAULT_LANG, LANGS, LANG_NAME, LANG_TAG, localePath, stripLang } from "../i18n";
import { LAYOUT } from "../locales/layout";
import { ISSUES_URL, PAGES, SITE, type PageMeta } from "../site";

/** GitHub mark, inlined rather than fetched: no external asset for one icon. */
export function GitHubMark() {
  return (
    <svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true" fill="currentColor">
      <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z" />
    </svg>
  );
}

/**
 * The brand, a short honest label for what kind of thing this is, a link to
 * the same page in the other language, and the page set. The label sits next to
 * the brand rather than in a footnote for the reason skill `ccweb-footer`
 * gives: a disclosure that only a reader of the About page ever sees is not
 * doing its job.
 */
function SiteHeader({ page }: { page: PageMeta }) {
  const text = LAYOUT[page.lang];
  const navPages = PAGES.filter((p) => p.lang === page.lang && p.navLabel);
  return (
    <header className="site-header">
      <div className="brand-row">
        <a className="brand" href={localePath(page.lang, "/")}>
          <img src="/favicon.svg" alt="" width="28" height="28" />
          <span>{SITE.name}</span>
        </a>
        <span className="brand-tag">{text.brandTag}</span>
        {LANGS.filter((l) => l !== page.lang).map((l) => (
          <a
            key={l}
            className="lang-switch"
            // A 404 has no counterpart page, so it points at the other home page.
            href={page.id === "notfound" ? localePath(l, "/") : localePath(l, stripLang(page.path))}
            hrefLang={LANG_TAG[l]}
            lang={LANG_TAG[l]}
            title={LAYOUT[l].switchLabel}
          >
            {LANG_NAME[l]}
          </a>
        ))}
      </div>
      <nav aria-label={text.navAria}>
        <ul className="nav-list">
          {navPages.map((p) => (
            <li key={p.id}>
              <a href={p.path} aria-current={p.id === page.id ? "page" : undefined}>
                {p.navLabel}
              </a>
            </li>
          ))}
          <li>
            <a href={SITE.repoUrl} target="_blank" rel="noreferrer">
              {text.source}
              <span className="sr-only">{text.sourceHint}</span>
            </a>
          </li>
        </ul>
      </nav>
    </header>
  );
}

/**
 * The declarations every page carries, defined here once per language
 * (locales/layout.tsx).
 *
 * What it asserts is limited to what the build can check: no ads, no cookies,
 * no analytics (scripts/check-site.mjs fails on a third-party script or on
 * storage APIs in src/), the licences from LICENSE and LICENSE-CODE, and a
 * non-endorsement line for the venues and data providers the site names.
 */
function SiteFooter({ page }: { page: PageMeta }) {
  const lang = page.lang;
  const text = LAYOUT[lang];
  const nav = PAGES.filter((p) => p.lang === lang && p.navLabel);
  const label = (id: string) => nav.find((p) => p.id === id)!;
  return (
    <footer className="site-footer" aria-label={text.footerAria}>
      {text.declarations(lang)}
      <ul className="footer-links">
        <li>
          <a href={label("about").path}>{text.footerLinks.about}</a>
        </li>
        <li>
          <a href={label("ai").path}>{text.footerLinks.ai}</a>
        </li>
        <li>
          <a href={label("privacy").path}>{text.footerLinks.privacy}</a>
        </li>
        <li>
          <a href={label("status").path}>{text.footerLinks.status}</a>
        </li>
        <li>
          <a href={SITE.repoUrl} target="_blank" rel="noreferrer">
            {text.footerLinks.source}
          </a>
        </li>
        <li>
          <a href={ISSUES_URL} target="_blank" rel="noreferrer">
            {text.footerLinks.report}
          </a>
        </li>
        {SITE.supportUrl && (
          <li>
            <a href={SITE.supportUrl} target="_blank" rel="noreferrer">
              {lang === DEFAULT_LANG ? SITE.supportLabel : text.support}
            </a>{" "}
            <span className="footer-aside">{text.supportAside}</span>
          </li>
        )}
        {SITE.contact.email && (
          <li>
            <a href={`mailto:${SITE.contact.email}`}>{SITE.contact.email}</a>
          </li>
        )}
      </ul>
    </footer>
  );
}

/**
 * The frame every page shares: skip link, header, one <main>, footer.
 * `<main>` takes focus on skip (tabIndex -1) so the next Tab starts inside it.
 */
export function Layout({ page, children }: { page: PageMeta; children: ReactNode }) {
  return (
    <>
      <a className="skip" href="#main">
        {LAYOUT[page.lang].skip}
      </a>
      <div className="shell">
        <SiteHeader page={page} />
        <main id="main" tabIndex={-1} className="page">
          {children}
        </main>
        <SiteFooter page={page} />
      </div>
    </>
  );
}
