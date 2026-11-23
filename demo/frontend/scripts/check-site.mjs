/**
 * The gate for the built site. Runs at the end of `npm run build` and fails the
 * build (exit 1) on anything below. It exists because the rules in
 * docs/status/SITE_SPEC.md are the ones that get skipped when they live in
 * someone's head, and the maintainer's standing rule is that a failure which
 * happens twice becomes an exit code.
 *
 *   node scripts/check-site.mjs        after `npm run build`
 *
 * What it checks, by spec id:
 *   S1, S2, S4-S6, S9, S10  every page: title, description, canonical, og/twitter,
 *                           JSON-LD, one h1, robots meta; sitemap, robots.txt,
 *                           llms.txt, 404 page, share image size
 *   A1, A3, A4              skip link and <main>; colour-token contrast, WCAG AA,
 *                           both themes; no text under 12 px
 *   D1                      no hex literal outside the tokens in index.css
 *   P1, P3, P4, M1, M2      size budget; the worker's headers and cache rules,
 *                           run against dist/ through scripts/pages-emulator.mjs;
 *                           no inline script or style (the CSP forbids them), no
 *                           third-party resource, no analytics or ad code, no
 *                           cookie or storage API; the API origin the bundle
 *                           calls is the one the CSP allows
 *   T3, T6                  no email address in the pages unless site.ts sets
 *                           one; no wording that claims human verification
 *   O4                      internal links and #fragments resolve
 */
import { readFile, readdir } from "node:fs/promises";
import { dirname, extname, join, relative } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { gzipSync } from "node:zlib";
import { makeAssets } from "./pages-emulator.mjs";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const DIST = join(ROOT, "dist");
const SRC = join(ROOT, "src");

// Size budget, gzip. Not taken from the siblings (they publish none; see
// SITE_SPEC.md P1): this is a ratchet set about 20% above the first measured
// build of this design (JS 103 KB, CSS 3 KB), so growth is a decision rather
// than an accident. Raise it deliberately, with the reason in the commit.
const BUDGET = { jsGz: 125 * 1024, cssGz: 12 * 1024, ogBytes: 200 * 1024 };

const failures = [];
const fail = (where, msg) => failures.push(`${where}: ${msg}`);
const read = (p) => readFile(p, "utf8");

async function walk(dir) {
  const out = [];
  for (const e of await readdir(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) out.push(...(await walk(p)));
    else out.push(p);
  }
  return out;
}

// ---------- contrast ----------

function hexToRgb(hex) {
  const h = hex.replace("#", "");
  return [0, 2, 4].map((i) => parseInt(h.slice(i, i + 2), 16) / 255);
}
function luminance(hex) {
  const [r, g, b] = hexToRgb(hex).map((c) => (c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4));
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}
function ratio(a, b) {
  const [hi, lo] = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return (hi + 0.05) / (lo + 0.05);
}

/** The token block that follows `selector {` in index.css, as a name -> value map. */
function tokensOf(css, selectorRe) {
  const m = css.match(selectorRe);
  if (!m) return null;
  const start = m.index + m[0].length;
  const end = css.indexOf("}", start);
  const map = {};
  for (const [, name, value] of css.slice(start, end).matchAll(/--([\w-]+):\s*(#[0-9a-fA-F]{6})\s*;/g)) {
    map[name] = value.toLowerCase();
  }
  return map;
}

// Text pairs need 4.5:1 (WCAG 1.4.3); the non-text pairs mark a control's
// boundary or focus and need 3:1 (1.4.11). Each is a pairing the CSS really makes.
const TEXT_PAIRS = [
  ["fg", "bg"], ["fg", "surface"], ["fg", "surface-2"], ["fg", "raised"],
  ["fg-strong", "bg"], ["muted", "bg"], ["muted", "surface"], ["muted", "surface-2"],
  ["muted", "raised"], ["faint", "bg"], ["faint", "surface"],
  ["accent-text", "bg"], ["accent-text", "surface"], ["accent-text", "surface-2"],
  ["accent-text", "surface-hover"], ["accent-text", "raised"], ["accent-text", "info-bg"],
  ["on-accent", "accent"], ["on-accent", "accent-hover"],
  ["warn-fg", "warn-bg"], ["danger-fg", "danger-bg"],
  ["tier1-fg", "tier1-bg"], ["tier2-fg", "tier2-bg"], ["tierai-fg", "tierai-bg"],
];
const NONTEXT_PAIRS = [
  ["control", "bg"], ["control", "surface"], ["control", "info-bg"], ["control", "raised"],
  ["focus", "bg"], ["focus", "surface"], ["focus", "raised"],
];

async function checkTokens() {
  const css = await read(join(SRC, "index.css"));
  const light = tokensOf(css, /:root\s*\{/);
  const darkAuto = tokensOf(css, /:root:not\(\[data-theme="light"\]\)\s*\{/);
  const darkForced = tokensOf(css, /:root\[data-theme="dark"\]\s*\{/);
  if (!light || !darkAuto || !darkForced) return fail("index.css", "missing a :root token block (light, auto-dark or forced-dark)");
  // The dark set is written twice (system preference and the data-theme hook);
  // a token changed in one and not the other is a bug nobody would see.
  for (const k of new Set([...Object.keys(darkAuto), ...Object.keys(darkForced)])) {
    if (darkAuto[k] !== darkForced[k]) fail("index.css", `dark token --${k} differs between the media query and data-theme blocks`);
  }
  for (const [theme, tokens] of [["light", light], ["dark", { ...light, ...darkAuto }]]) {
    for (const [pairs, min] of [[TEXT_PAIRS, 4.5], [NONTEXT_PAIRS, 3]]) {
      for (const [a, b] of pairs) {
        if (!tokens[a] || !tokens[b]) { fail("index.css", `${theme}: token --${a} or --${b} is not defined`); continue; }
        const r = ratio(tokens[a], tokens[b]);
        if (r < min) fail("index.css", `${theme}: --${a} on --${b} is ${r.toFixed(2)}:1, needs ${min}:1`);
      }
    }
  }
}

// ---------- pages ----------

const meta = (html, attr, name) => {
  const m = html.match(new RegExp(`<meta ${attr}="${name}" content="([^"]*)"`));
  return m ? m[1] : null;
};
const textOf = (html) =>
  html.replace(/<script[\s\S]*?<\/script>/g, " ").replace(/<[^>]+>/g, " ").replace(/&[a-z#0-9]+;/g, " ").replace(/\s+/g, " ");
const decode = (s) => s.replace(/&quot;/g, '"').replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">");

const FORBIDDEN_CLAIMS = /human[- ]verified|expert[- ]reviewed|peer[- ]reviewed by|verified by (a |an )?(human|expert|editor|scholar)/i;
const THIRD_PARTY_CODE = /adsbygoogle|googlesyndication|doubleclick|posthog|gtag\(|google-analytics|googletagmanager|cloudflareinsights|plausible\.io|hotjar|mixpanel/i;
const EMAIL = /[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}/;

function pageFile(page) {
  if (page.path === "/") return join(DIST, "index.html");
  if (page.path.endsWith(".html")) return join(DIST, page.path.slice(1));
  return join(DIST, page.path, "index.html");
}

async function checkPages({ PAGES, SITE, absoluteUrl }) {
  const titles = new Map();
  const pageHtml = new Map();
  for (const page of PAGES) pageHtml.set(page.path, await read(pageFile(page)));

  for (const page of PAGES) {
    const where = page.path;
    const html = pageHtml.get(page.path);
    const need = (cond, msg) => cond || fail(where, msg);

    need(/<html lang="en"/.test(html), 'missing <html lang="en">');
    need(!html.includes("<!--seo-->"), "the <!--seo--> marker was not replaced");
    need((html.match(/<h1[\s>]/g) ?? []).length === 1, "needs exactly one <h1>");
    need(/<main id="main"/.test(html), 'missing <main id="main">');
    need(/class="skip" href="#main"/.test(html), "missing the skip link");
    need(/name="viewport"[^>]*viewport-fit=cover/.test(html), "viewport meta lacks viewport-fit=cover");

    const title = decode(html.match(/<title>([^<]*)<\/title>/)?.[1] ?? "");
    need(title === page.title, `title is "${title}", expected "${page.title}"`);
    need(title.length > 0 && title.length <= 70, `title length ${title.length} (1-70)`);
    if (titles.has(title)) fail(where, `title duplicates ${titles.get(title)}`);
    titles.set(title, where);

    const description = decode(meta(html, "name", "description") ?? "");
    need(description.length >= 50 && description.length <= 200, `description length ${description.length} (50-200)`);

    const canonical = html.match(/<link rel="canonical" href="([^"]*)"/)?.[1];
    if (page.id === "notfound") need(!canonical, "a 404 page must not declare a canonical URL");
    else need(canonical === absoluteUrl(page.path), `canonical is ${canonical}, expected ${absoluteUrl(page.path)}`);

    const robots = meta(html, "name", "robots") ?? "";
    need(/noindex/.test(robots) === Boolean(page.noindex), `robots meta "${robots}" disagrees with noindex=${Boolean(page.noindex)}`);

    for (const p of ["og:title", "og:description", "og:image", "og:image:alt", "og:url", "og:site_name"]) need(meta(html, "property", p), `missing ${p}`);
    need(meta(html, "property", "og:image:width") === "1200" && meta(html, "property", "og:image:height") === "630", "og:image size must be 1200x630");
    need(meta(html, "name", "twitter:card") === "summary_large_image", "missing twitter:card summary_large_image");
    need(meta(html, "name", "theme-color") === SITE.themeColor, "theme-color is not the --bg token value in site.ts");

    // Structured data must parse and must not carry template placeholders.
    for (const [, body] of html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)) {
      try {
        const data = JSON.parse(body);
        need(data["@context"] === "https://schema.org", "JSON-LD @context is not schema.org");
        need(!/YOURDOMAIN|REPLACE|PLACEHOLDER|[A-Z]+_[A-Z_]{3,}/.test(body), "JSON-LD has a template placeholder");
      } catch (e) {
        fail(where, `JSON-LD does not parse: ${e.message}`);
      }
    }

    // CSP in public/_worker.js allows no inline script and no inline style.
    need(!/<script(?![^>]*type="application\/ld\+json")(?![^>]*\ssrc=)[^>]*>/.test(html), "inline <script> (the CSP blocks it)");
    need(!/<style[\s>]/.test(html) && !/\sstyle="/.test(html), "inline style (the CSP blocks it)");
    // No third-party resource: every script, stylesheet, image or icon is same-origin.
    for (const [tag] of html.matchAll(/<(?:script|img|iframe|source|link)\b[^>]*>/g)) {
      const rel = tag.match(/rel="([^"]*)"/)?.[1] ?? "";
      if (tag.startsWith("<link") && /canonical|alternate/.test(rel)) continue;
      const ref = tag.match(/\b(?:src|href)="(https?:)?\/\/[^"]*"/);
      if (ref) fail(where, `third-party resource: ${tag.slice(0, 120)}`);
    }

    const text = textOf(html);
    need(!THIRD_PARTY_CODE.test(html), "analytics or ad code found (a decision for the maintainer, see SITE_SPEC.md part 3)");
    need(!FORBIDDEN_CLAIMS.test(text), `wording claims human verification: "${text.match(FORBIDDEN_CLAIMS)?.[0]}"`);
    const email = text.match(EMAIL)?.[0];
    if (email && email !== SITE.contact.email) fail(where, `an email address is visible: ${email} (set SITE.contact.email in site.ts to allow one)`);

    // Links and fragments that point inside the site must land somewhere.
    for (const [, href] of html.matchAll(/<a [^>]*href="(\/[^"]*)"/g)) {
      const [path, frag] = decode(href).split("#");
      const target = PAGES.find((p) => p.path === path);
      if (!target) {
        if (path !== "/" && !(await exists(join(DIST, path)))) fail(where, `link to ${href} does not resolve`);
        continue;
      }
      if (frag && !pageHtml.get(target.path).includes(`id="${frag}"`)) fail(where, `link ${href}: no id="${frag}" on that page`);
    }
    for (const [, frag] of html.matchAll(/<a [^>]*href="#([^"]+)"/g)) {
      if (!html.includes(`id="${frag}"`)) fail(where, `link #${frag}: no such id on the page`);
    }
  }
  return pageHtml;
}

async function exists(p) {
  try {
    await readFile(p);
    return true;
  } catch {
    return false;
  }
}

// ---------- crawler files ----------

async function checkCrawlerFiles({ PAGES, SITE, absoluteUrl }) {
  const sitemap = await read(join(DIST, "sitemap.xml"));
  const locs = [...sitemap.matchAll(/<loc>([^<]*)<\/loc>/g)].map((m) => m[1]);
  const want = PAGES.filter((p) => !p.noindex).map((p) => absoluteUrl(p.path));
  if (JSON.stringify([...locs].sort()) !== JSON.stringify([...want].sort())) {
    fail("sitemap.xml", `lists ${locs.join(", ")}; the indexable pages are ${want.join(", ")}`);
  }
  for (const [, d] of sitemap.matchAll(/<lastmod>([^<]*)<\/lastmod>/g)) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(d)) fail("sitemap.xml", `lastmod "${d}" is not an ISO date`);
  }

  const robots = await read(join(DIST, "robots.txt"));
  if (!robots.includes(`Sitemap: ${SITE.url}/sitemap.xml`)) fail("robots.txt", "no Sitemap line for the canonical sitemap");
  if (/Disallow:\s*\/?\s*$/m.test(robots) || /Disallow:\s*\/(assets|\s)/.test(robots)) fail("robots.txt", "disallows the site or its assets");
  if ([...robots.matchAll(/^User-agent:\s*(\S+)/gim)].some((m) => m[1] !== "*")) fail("robots.txt", "a named user-agent group replaces `*` entirely under RFC 9309; copy every rule into it or remove it");

  const llms = await read(join(DIST, "llms.txt"));
  if (!llms.startsWith("# ")) fail("llms.txt", "must start with an H1");
  for (const [, url] of llms.matchAll(/\]\((https:\/\/[^)]+)\)/g)) {
    if (url.startsWith(SITE.url) && !PAGES.some((p) => absoluteUrl(p.path) === url)) fail("llms.txt", `${url} is not a page of this site`);
  }

  const og = await readFile(join(DIST, "og.png"));
  const [w, h] = [og.readUInt32BE(16), og.readUInt32BE(20)];
  if (w !== 1200 || h !== 630) fail("og.png", `is ${w}x${h}, needs 1200x630`);
  if (og.length > BUDGET.ogBytes) fail("og.png", `${og.length} bytes exceeds ${BUDGET.ogBytes}`);
  for (const f of ["favicon.svg", "favicon-32.png", "apple-touch-icon.png", "_worker.js", "404.html"]) {
    if (!(await exists(join(DIST, f)))) fail(f, "missing from dist/");
  }
}

// ---------- source and bundle rules ----------

async function checkSourceAndBundle() {
  const files = await walk(SRC);
  for (const f of files) {
    const rel = relative(ROOT, f).replace(/\\/g, "/");
    const text = await read(f);
    if (/\.(css|tsx?)$/.test(f) && !rel.endsWith("src/index.css") && !rel.endsWith("src/site.ts")) {
      // Comments may quote a hex value; code and CSS may not use one.
      const code = text.replace(/\/\*[\s\S]*?\*\//g, "").replace(/^\s*\/\/.*$/gm, "");
      const hex = code.match(/#[0-9a-fA-F]{3,8}\b(?![\w-])/);
      if (hex && /\.css$/.test(f)) fail(rel, `hex colour ${hex[0]}: use a token from index.css`);
    }
    if (/\.tsx?$/.test(f) && /\b(localStorage|sessionStorage|indexedDB)\b|document\.cookie/.test(text.replace(/\/\*[\s\S]*?\*\//g, "").replace(/^\s*\/\/.*$/gm, ""))) {
      fail(rel, "uses a browser storage or cookie API; the footer and privacy page say the site uses none");
    }
    if (/\.css$/.test(f) && /@import|url\(\s*["']?https?:/.test(text)) fail(rel, "pulls CSS or an asset from another origin");
  }

  const assets = (await walk(join(DIST, "assets"))).filter((f) => !f.endsWith(".map"));
  const js = assets.filter((f) => extname(f) === ".js");
  const css = assets.filter((f) => extname(f) === ".css");
  const gz = async (list) => (await Promise.all(list.map(async (f) => gzipSync(await readFile(f)).length))).reduce((a, b) => a + b, 0);
  const jsGz = await gz(js);
  const cssGz = await gz(css);
  if (jsGz > BUDGET.jsGz) fail("bundle", `JS is ${(jsGz / 1024).toFixed(1)} KB gzip, budget ${BUDGET.jsGz / 1024} KB`);
  if (cssGz > BUDGET.cssGz) fail("bundle", `CSS is ${(cssGz / 1024).toFixed(1)} KB gzip, budget ${BUDGET.cssGz / 1024} KB`);

  for (const f of css) {
    const body = await read(f);
    for (const [, n, unit] of body.matchAll(/font-size:\s*([\d.]+)(rem|px)/g)) {
      const px = unit === "rem" ? Number(n) * 16 : Number(n);
      if (px < 12) fail(relative(ROOT, f).replace(/\\/g, "/"), `font-size ${n}${unit} is under 12 px`);
    }
  }

  return { js, jsGz, cssGz };
}

async function checkApiOrigin({ SITE }, js) {
  const bundle = (await Promise.all(js.map(read))).join("\n");
  const apis = new Set([...bundle.matchAll(/https?:\/\/(?:api\.)[a-z0-9.-]+/g)].map((m) => m[0]));
  for (const a of apis) if (a !== SITE.apiUrl) fail("bundle", `calls ${a}, but site.ts and the worker's CSP allow ${SITE.apiUrl}`);
  if (/localhost:8000/.test(bundle) && !process.env.ALLOW_LOCAL_API) {
    fail("bundle", "was built for http://localhost:8000: VITE_API_BASE is not set, so the live site would call a local API (set ALLOW_LOCAL_API=1 for a local preview build)");
  }
  const worker = await read(join(DIST, "_worker.js"));
  if (!worker.includes(`const API_ORIGIN = "${SITE.apiUrl}"`)) fail("_worker.js", "API_ORIGIN differs from SITE.apiUrl in site.ts");
}

// ---------- the worker, run over dist/ ----------

async function checkWorker({ SITE }, js) {
  const worker = (await import(pathToFileURL(join(DIST, "_worker.js")).href)).default;
  const env = { ASSETS: makeAssets(DIST) };
  const get = (path, host = "journal-atlas.chroniclecore.com") => worker.fetch(new Request(`https://${host}${path}`), env);
  const need = (where, cond, msg) => cond || fail(`worker ${where}`, msg);

  const home = await get("/");
  const csp = home.headers.get("content-security-policy") ?? "";
  need("/", home.status === 200, `status ${home.status}`);
  need("/", /default-src 'self'/.test(csp) && /script-src 'self'(;|$)/.test(csp) && !/unsafe-/.test(csp), "CSP is missing or allows unsafe-inline/eval");
  need("/", csp.includes(`connect-src 'self' ${SITE.apiUrl}`), "CSP connect-src does not name the API origin");
  need("/", /frame-ancestors 'none'/.test(csp) && /object-src 'none'/.test(csp), "CSP lacks frame-ancestors/object-src 'none'");
  need("/", /max-age=31536000/.test(home.headers.get("strict-transport-security") ?? ""), "no HSTS");
  need("/", home.headers.get("x-content-type-options") === "nosniff", "no nosniff");
  need("/", home.headers.get("x-frame-options") === "DENY", "no X-Frame-Options");
  need("/", home.headers.get("referrer-policy") === "strict-origin-when-cross-origin", "no Referrer-Policy");
  need("/", /camera=\(\)/.test(home.headers.get("permissions-policy") ?? ""), "no Permissions-Policy");
  need("/", /must-revalidate/.test(home.headers.get("cache-control") ?? "") && !/stale-while-revalidate/.test(home.headers.get("cache-control") ?? ""), "HTML must revalidate and never stale-while-revalidate");

  const about = await get("/about");
  need("/about", about.status === 308 && about.headers.get("location")?.endsWith("/about/"), `expected a redirect to /about/, got ${about.status}`);
  const aboutSlash = await get("/about/");
  need("/about/", aboutSlash.status === 200, `status ${aboutSlash.status}`);

  const asset = "/assets/" + js[0].split(/[\\/]/).pop();
  const a = await get(asset);
  need(asset, /immutable/.test(a.headers.get("cache-control") ?? ""), "hashed asset is not immutable");

  const missing = await get("/no-such-page-xyz");
  need("unknown URL", missing.status === 404, `status ${missing.status}: a soft 404 (200 on a missing page) is what this prevents`);
  need("unknown URL", (await missing.text()).includes("Page not found"), "the 404 body is not the 404 page");
  need("unknown URL", /noindex/.test(await (await get("/404.html")).text()), "404.html is indexable");

  for (const f of ["/robots.txt", "/sitemap.xml", "/llms.txt"]) {
    const r = await get(f);
    need(f, r.status === 200 && !(r.headers.get("content-type") ?? "").includes("text/html"), `status ${r.status}, ${r.headers.get("content-type")} (the SPA shell must not answer for it)`);
  }

  const pagesDev = await get("/about/", "journal-atlas.pages.dev");
  need("pages.dev", pagesDev.status === 302 && pagesDev.headers.get("location") === "https://journal-atlas.chroniclecore.com/about/", "pages.dev host is not redirected to the canonical domain");
}

// ---------- run ----------

const ssr = await import(pathToFileURL(join(ROOT, "dist-ssr", "entry-server.js")).href);
await checkTokens();
await checkPages(ssr);
await checkCrawlerFiles(ssr);
const { js, jsGz, cssGz } = await checkSourceAndBundle();
await checkApiOrigin(ssr, js);
await checkWorker(ssr, js);

if (failures.length) {
  console.error(`check-site: ${failures.length} problem(s)\n` + failures.map((f) => `  - ${f}`).join("\n"));
  process.exit(1);
}
console.log(
  `check-site: ok (${ssr.PAGES.length} pages, JS ${(jsGz / 1024).toFixed(1)} KB gzip, CSS ${(cssGz / 1024).toFixed(1)} KB gzip)`
);
