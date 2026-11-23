import { ISSUES_URL } from "../site";

/**
 * Served as /404.html with a real 404 status by the Pages worker, so a
 * mistyped URL is not a "page" a search engine can index (a soft 404).
 */
export default function NotFound() {
  return (
    <article className="prose">
      <h1>Page not found</h1>
      <p className="lede">There is nothing at this address.</p>
      <ul>
        <li>
          <a href="/">Find a journal for your paper</a>
        </li>
        <li>
          <a href="/about/">About Journal Atlas</a>
        </li>
        <li>
          <a href="/ai/">How it&apos;s made, and what is AI</a>
        </li>
        <li>
          <a href={ISSUES_URL} target="_blank" rel="noreferrer">
            Tell us about a broken link
          </a>
        </li>
      </ul>
    </article>
  );
}
