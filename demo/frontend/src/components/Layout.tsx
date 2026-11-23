import type { ReactNode } from "react";
import { ISSUES_URL, PAGES, SITE, type PageId } from "../site";

/** GitHub mark, inlined rather than fetched: no external asset for one icon. */
export function GitHubMark() {
  return (
    <svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true" fill="currentColor">
      <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z" />
    </svg>
  );
}

const NAV_PAGES = PAGES.filter((p) => p.navLabel);

/**
 * The brand, a short honest label for what kind of thing this is, and the
 * page set. The label sits next to the brand rather than in a footnote for the
 * reason skill `ccweb-footer` gives: a disclosure that only a reader of the
 * About page ever sees is not doing its job.
 */
function SiteHeader({ current }: { current: PageId }) {
  return (
    <header className="site-header">
      <div className="brand-row">
        <a className="brand" href="/">
          <img src="/favicon.svg" alt="" width="28" height="28" />
          <span>{SITE.name}</span>
        </a>
        <span className="brand-tag">Research prototype · AI-assisted</span>
      </div>
      <nav aria-label="Site">
        <ul className="nav-list">
          {NAV_PAGES.map((p) => (
            <li key={p.id}>
              <a href={p.path} aria-current={p.id === current ? "page" : undefined}>
                {p.navLabel}
              </a>
            </li>
          ))}
          <li>
            <a href={SITE.repoUrl} target="_blank" rel="noreferrer">
              Source<span className="sr-only"> (opens GitHub)</span>
            </a>
          </li>
        </ul>
      </nav>
    </header>
  );
}

/**
 * The declarations every page carries, defined here once.
 *
 * What it asserts is limited to what the build can check: no ads, no cookies,
 * no analytics (scripts/check-site.mjs fails on a third-party script or on
 * storage APIs in src/), the licences from LICENSE and LICENSE-CODE, and a
 * non-endorsement line for the venues and data providers the site names.
 */
function SiteFooter() {
  return (
    <footer className="site-footer" aria-label="Site information">
      <p>
        Journal Atlas is a research project by{" "}
        <a href={SITE.author.url} target="_blank" rel="noreferrer">
          {SITE.author.handle}
        </a>
        , a{" "}
        <a href={SITE.studio.url} target="_blank" rel="noreferrer">
          {SITE.studio.name}
        </a>{" "}
        ({SITE.studio.nameZh}) production. Much of it is written by AI;{" "}
        <a href="/ai/">this page says which parts</a>.
      </p>
      <p>
        Not affiliated with, endorsed by, or sponsored by any journal,
        conference, publisher or index it names. Those names belong to their
        owners, and an entry is a description of a venue from public sources,
        not a statement by the venue.
      </p>
      <p>
        Knowledge base:{" "}
        <a href={SITE.license.contentUrl} target="_blank" rel="noreferrer">
          {SITE.license.content}
        </a>
        . Code:{" "}
        <a href={SITE.license.codeUrl} target="_blank" rel="noreferrer">
          {SITE.license.code}
        </a>
        . The site sets no cookies and loads no ads, analytics or third-party
        scripts.
      </p>
      <ul className="footer-links">
        <li>
          <a href="/about/">About</a>
        </li>
        <li>
          <a href="/ai/">How it&apos;s made</a>
        </li>
        <li>
          <a href="/privacy/">Privacy</a>
        </li>
        <li>
          <a href="/status/">Status</a>
        </li>
        <li>
          <a href={SITE.repoUrl} target="_blank" rel="noreferrer">
            Source and knowledge base
          </a>
        </li>
        <li>
          <a href={ISSUES_URL} target="_blank" rel="noreferrer">
            Report something wrong
          </a>
        </li>
        {SITE.supportUrl && (
          <li>
            <a href={SITE.supportUrl} target="_blank" rel="noreferrer">
              {SITE.supportLabel}
            </a>{" "}
            <span className="footer-aside">(unlocks nothing; every feature is the same for everyone)</span>
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
export function Layout({ current, children }: { current: PageId; children: ReactNode }) {
  return (
    <>
      <a className="skip" href="#main">
        Skip to main content
      </a>
      <div className="shell">
        <SiteHeader current={current} />
        <main id="main" tabIndex={-1} className="page">
          {children}
        </main>
        <SiteFooter />
      </div>
    </>
  );
}
