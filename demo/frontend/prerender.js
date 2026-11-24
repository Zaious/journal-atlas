/**
 * Write every page's first render into its own HTML file, plus the files a
 * crawler asks for: sitemap.xml, robots.txt, llms.txt.
 *
 * Without this the served HTML is an empty <div id="root">, and everything on
 * the page — what the tool is, where the source lives, who made it — exists
 * only for clients that run the bundle. Crawlers that render JavaScript see it;
 * link checkers, `curl`, and many crawlers do not. Prerendering costs one build
 * step and nothing at runtime: main.tsx hydrates this markup rather than
 * replacing it.
 *
 * Only the initial state is rendered. Everything that comes from the API
 * (coverage counts, model names, rate limits) is fetched in effects, which do
 * not run on the server, so this markup is exactly the client's first render
 * and hydration has nothing to reconcile.
 *
 * Output, from the page list in src/site.ts:
 *   dist/index.html            /
 *   dist/<page>/index.html     /about/, /ai/, /privacy/, /status/
 *   dist/zh-hant/...           the same set in Traditional Chinese
 *   dist/404.html              served with a 404 status for any unknown URL
 *   dist/zh-hant/404.html      the same for unknown URLs under /zh-hant/ (the
 *                              Pages worker picks it, see public/_worker.js)
 *   dist/sitemap.xml, robots.txt, llms.txt
 *
 * Runs as the last build step, after the SSR build of src/entry-server.tsx
 * into dist-ssr/. scripts/check-site.mjs then inspects what was written.
 */
import { execFileSync } from "node:child_process";
import { mkdir, readFile, writeFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = dirname(fileURLToPath(import.meta.url));
const DIST = join(ROOT, "dist");
const EMPTY_ROOT = '<div id="root"></div>';
const SEO_MARKER = "<!--seo-->";

const { render, PAGES, LANG_TAG, headTags, sitemapXml, robotsTxt, llmsTxt } = await import(
  "./dist-ssr/entry-server.js"
);
const template = await readFile(join(DIST, "index.html"), "utf8");

// A second run would find the root already filled; fail rather than guess.
if (!template.includes(EMPTY_ROOT) || !template.includes(SEO_MARKER)) {
  console.error(`prerender: dist/index.html needs an empty ${EMPTY_ROOT} and a ${SEO_MARKER} marker`);
  process.exit(1);
}

function outFile(page) {
  if (page.path === "/") return join(DIST, "index.html");
  if (page.path.endsWith(".html")) return join(DIST, page.path.slice(1));
  return join(DIST, page.path, "index.html");
}

for (const page of PAGES) {
  // The path a 404 page is rendered for is irrelevant, but it must resolve to
  // the not-found body, so hand it one nothing else uses.
  // It must resolve to the not-found page of the page's own language.
  const unknown = page.lang === "en" ? "/__not-found__/" : "/zh-hant/__not-found__/";
  const pathname = page.id === "notfound" ? unknown : page.path;
  // No whitespace around the markup: hydration walks the DOM node by node, and
  // a newline inside #root is a text node the server sent and the client did not.
  const html = template
    .replace('<html lang="en">', `<html lang="${LANG_TAG[page.lang]}">`)
    .replace(SEO_MARKER, headTags(page))
    .replace(EMPTY_ROOT, `<div id="root">${render(pathname)}</div>`);
  const file = outFile(page);
  await mkdir(dirname(file), { recursive: true });
  await writeFile(file, html);
}

/**
 * The last commit that touched the files a page is built from, as the page's
 * `lastmod`. Null when git or history is unavailable (a shallow CI checkout,
 * an exported tarball): the sitemap then omits `lastmod` rather than stamping
 * every page with the build date, which would say "changed today" for pages
 * that did not.
 */
function lastmod(page) {
  try {
    const out = execFileSync("git", ["log", "-1", "--format=%cs", "--", ...page.sources], {
      cwd: ROOT,
      encoding: "utf8",
      stdio: ["ignore", "pipe", "ignore"],
    }).trim();
    return /^\d{4}-\d{2}-\d{2}$/.test(out) ? out : null;
  } catch {
    return null;
  }
}

await writeFile(join(DIST, "sitemap.xml"), sitemapXml(lastmod));
await writeFile(join(DIST, "robots.txt"), robotsTxt());
await writeFile(join(DIST, "llms.txt"), llmsTxt());
console.log(`prerender: wrote ${PAGES.length} pages, sitemap.xml, robots.txt, llms.txt`);
