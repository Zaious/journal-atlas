/**
 * Post-deploy check, against any base URL. The list is the one the sibling
 * product sites keep in their release gate (docs/status/SITE_SPEC.md, O2):
 * the pages, robots.txt, sitemap.xml, llms.txt, an unknown URL that must be a
 * 404, and the response headers. It reads only; it sends no body and no cookie.
 *
 *   npm run smoke                                       local preview (npm run preview)
 *   node scripts/smoke.mjs https://journal-atlas.chroniclecore.com
 *   node scripts/smoke.mjs http://localhost:4600 --api http://localhost:8000
 *
 * Exit 1 if anything fails. On the live site before this branch is deployed it
 * is expected to fail, which is the point: the failures are the gap list.
 */
const args = process.argv.slice(2);
const apiFlag = args.indexOf("--api");
const api = apiFlag >= 0 ? args.splice(apiFlag, 2)[1] : "https://api.journal-atlas.chroniclecore.com";
const base = (args[0] ?? "http://localhost:4600").replace(/\/$/, "");

// The zone answers some default User-Agents with 403, so identify as a browser-like client.
// Ask like a browser does. Cloudflare injects some scripts (Web Analytics) only
// into responses for requests that accept HTML, so a bare request sees a page no
// visitor gets; found on the first deploy, 2026-11-24.
const headers = {
  "user-agent": "Mozilla/5.0 (compatible; journal-atlas-smoke)",
  accept: "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
};
const results = [];
const check = (name, ok, detail = "") => results.push({ name, ok, detail });
// A known, accepted result: reported as EXPECTED, not hidden and not a failure.
// Each one says why it is accepted, and is only accepted under the condition
// written next to it; outside that condition it is an ordinary failure.
const expected = (name, detail) => results.push({ name, ok: true, expected: true, detail });

async function get(url) {
  try {
    const r = await fetch(url, { headers, redirect: "manual" });
    return { r, text: await r.text() };
  } catch (e) {
    return { r: null, text: "", error: String(e) };
  }
}

// Every page in both languages. The Chinese ones live under /zh-hant/ and must
// say so in <html lang> and point back at their English counterpart.
const PAGES = ["/", "/about/", "/ai/", "/privacy/", "/status/"];
for (const lang of ["en", "zh-Hant"]) {
  for (const page of PAGES) {
    const path = lang === "en" ? page : `/zh-hant${page}`;
    const { r, text } = await get(base + path);
    check(`${path} is a 200 HTML page`, r?.status === 200 && (r.headers.get("content-type") ?? "").includes("text/html"), r ? `${r.status} ${r.headers.get("content-type")}` : "no response");
    check(`${path} has its own <title> and one <h1>`, /<title>[^<]+<\/title>/.test(text) && (text.match(/<h1[\s>]/g) ?? []).length === 1);
    check(`${path} is <html lang="${lang}">`, text.includes(`<html lang="${lang}"`));
    check(`${path} canonical points at itself`, page === "/status/" || text.includes(`<link rel="canonical" href="https://journal-atlas.chroniclecore.com${path}"`));
    if (page !== "/status/") {
      check(`${path} names its other-language version (hreflang)`, text.includes('hreflang="zh-Hant"') && text.includes('hreflang="en"') && text.includes('hreflang="x-default"'));
    }
  }
}
const zhMissing = await get(base + "/zh-hant/no-such-page-smoke-test");
check("an unknown /zh-hant/ URL is a real 404 with the Chinese page", zhMissing.r?.status === 404 && zhMissing.text.includes("找不到頁面"), zhMissing.r ? String(zhMissing.r.status) : "no response");

const home = await get(base + "/");
const h = (name) => home.r?.headers.get(name) ?? "";
check("headers: Content-Security-Policy", /default-src 'self'/.test(h("content-security-policy")), h("content-security-policy") || "absent");
check("headers: Strict-Transport-Security", /max-age=\d{7,}/.test(h("strict-transport-security")), h("strict-transport-security") || "absent");
check("headers: X-Content-Type-Options nosniff", h("x-content-type-options") === "nosniff");
check("headers: Referrer-Policy", h("referrer-policy") === "strict-origin-when-cross-origin", h("referrer-policy") || "absent");
check("headers: X-Frame-Options or frame-ancestors", h("x-frame-options") === "DENY" || /frame-ancestors/.test(h("content-security-policy")));
check("headers: no cookie is set", !home.r?.headers.get("set-cookie"), home.r?.headers.get("set-cookie") ?? "");
// The build gate checks dist/; this checks what is actually served, which the
// CDN can change. The site says it loads no analytics or third-party scripts.
const thirdParty = [...home.text.matchAll(/<script\b[^>]*\bsrc="(https?:)?\/\/[^"]*"/g)].map((m) => m[0]);
const analytics = /cloudflareinsights|googletagmanager|google-analytics|gtag\(|posthog|plausible\.io|adsbygoogle|googlesyndication/i;
// Cloudflare Web Analytics is switched on for the Pages project, and Cloudflare
// injects its beacon into browser requests. The maintainer decided on 2026-11-24
// to leave that setting on (docs/status/SITE_SPEC.md, "Deployment state"). The
// CSP allows scripts from 'self' only, so the browser refuses the beacon and
// nothing is loaded or sent; the footer's "loads no analytics" stays true. So
// the beacon, and only the beacon, is EXPECTED while the CSP still blocks it.
const beaconOnly = thirdParty.length > 0 && thirdParty.every((t) => /static\.cloudflareinsights\.com\/beacon/.test(t));
const otherAnalytics = analytics.test(home.text.replace(/<script\b[^>]*static\.cloudflareinsights\.com[^>]*>(<\/script>)?/g, ""));
const cspBlocksIt = /script-src 'self'(;|$)/.test(h("content-security-policy")) && !/cloudflareinsights/.test(h("content-security-policy"));
if (beaconOnly && !otherAnalytics && cspBlocksIt) {
  expected(
    "served HTML has no third-party or analytics script",
    "Cloudflare Web Analytics beacon injected by Cloudflare; left on by decision, blocked by the CSP (script-src 'self'), so nothing loads",
  );
} else {
  check("served HTML has no third-party or analytics script", thirdParty.length === 0 && !analytics.test(home.text), thirdParty.join(" ").slice(0, 160));
}

const robots = await get(base + "/robots.txt");
check("/robots.txt is plain text with a Sitemap line", robots.r?.status === 200 && !(robots.r.headers.get("content-type") ?? "").includes("html") && /^Sitemap: /m.test(robots.text), robots.r ? `${robots.r.status} ${robots.r.headers.get("content-type")}` : "no response");
const sitemap = await get(base + "/sitemap.xml");
check("/sitemap.xml is XML and lists the indexable pages", sitemap.r?.status === 200 && /<urlset/.test(sitemap.text) && ["/about/", "/ai/", "/privacy/", "/zh-hant/about/", "/zh-hant/privacy/"].every((p) => sitemap.text.includes(p)), sitemap.r ? `${sitemap.r.status} ${sitemap.r.headers.get("content-type")}` : "no response");
check("/sitemap.xml leaves out the noindex status page", !/\/status\//.test(sitemap.text));
const llms = await get(base + "/llms.txt");
check("/llms.txt is plain text starting with an H1", llms.r?.status === 200 && /^# /.test(llms.text), llms.r ? `${llms.r.status} ${llms.r.headers.get("content-type")}` : "no response");
const missing = await get(base + "/no-such-page-smoke-test");
check("an unknown URL is a real 404", missing.r?.status === 404, missing.r ? String(missing.r.status) : "no response");
const ads = await get(base + "/ads.txt");
check("/ads.txt is absent (no ads on this site)", ads.r?.status === 404, ads.r ? String(ads.r.status) : "no response");

const healthz = await get(api + "/healthz");
check("API /healthz answers ok", healthz.r?.status === 200 && /"ok"/.test(healthz.text), healthz.r ? String(healthz.r.status) : "no response");
let coverage = null;
try {
  coverage = JSON.parse((await get(api + "/api/coverage")).text);
} catch {
  /* reported below */
}
check("API /api/coverage reports tier totals and a dated human-evidence record", Boolean(coverage?.tiers && coverage?.human_evidence?.recorded), coverage ? "fields missing: this backend predates the change" : "no JSON");
let health = null;
try {
  health = JSON.parse((await get(api + "/api/health")).text);
} catch {
  /* reported below */
}
check("API /api/health names the provider and both models", Boolean(health?.provider && health?.extraction_model && health?.synthesis_model), health ? JSON.stringify({ provider: health.provider }) : "no JSON");

const failed = results.filter((x) => !x.ok);
for (const x of results) {
  const tag = x.expected ? "EXPECTED" : x.ok ? "PASS" : "FAIL";
  console.log(`${tag}  ${x.name}${(x.ok && !x.expected) || !x.detail ? "" : `  [${x.detail}]`}`);
}
const nExpected = results.filter((x) => x.expected).length;
console.log(
  `\nsmoke: ${results.length - failed.length}/${results.length} passed against ${base} (API ${api})` +
    (nExpected ? `, of which ${nExpected} expected (see EXPECTED lines)` : ""),
);
process.exit(failed.length ? 1 : 0);
