import { localePath, useLang } from "../i18n";
import { ISSUES_URL } from "../site";

/**
 * Served as /404.html (and /zh-hant/404.html) with a real 404 status by the
 * Pages worker, so a mistyped URL is not a "page" a search engine can index (a
 * soft 404).
 */
export default function NotFound() {
  const lang = useLang();
  const zh = lang === "zh-Hant";
  return (
    <article className="prose">
      <h1>{zh ? "找不到頁面" : "Page not found"}</h1>
      <p className="lede">{zh ? "這個網址上什麼都沒有。" : "There is nothing at this address."}</p>
      <ul>
        <li>
          <a href={localePath(lang, "/")}>{zh ? "為你的論文找期刊" : "Find a journal for your paper"}</a>
        </li>
        <li>
          <a href={localePath(lang, "/about/")}>{zh ? "關於 Journal Atlas" : "About Journal Atlas"}</a>
        </li>
        <li>
          <a href={localePath(lang, "/ai/")}>{zh ? "如何製作，哪些部分是 AI" : "How it's made, and what is AI"}</a>
        </li>
        <li>
          <a href={ISSUES_URL} target="_blank" rel="noreferrer">
            {zh ? "告訴我們有壞掉的連結" : "Tell us about a broken link"}
          </a>
        </li>
      </ul>
    </article>
  );
}
