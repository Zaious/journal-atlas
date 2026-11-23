/**
 * The Pages worker: send *.pages.dev to the canonical domain, and put the
 * security and caching headers on everything else.
 *
 * It intercepts every request, so it stays small and does three things only.
 * Anything else it did would be a way for the whole site to break.
 *
 * 1. Redirect every *.pages.dev hostname to the canonical domain.
 *
 *    Cloudflare Pages always exposes the project at `<project>.pages.dev`, plus
 *    a unique subdomain per deployment. Those URLs serve the app perfectly but
 *    cannot reach the API: the backend's CORS allowlist names exactly one
 *    origin, so the page loads and then every request fails with "Failed to
 *    fetch". A public URL that renders correctly and does nothing is worse than
 *    one that does not exist — it reads as the demo being broken.
 *
 *    Redirecting rather than widening the allowlist keeps one canonical origin,
 *    and means a shared pages.dev link still lands the visitor somewhere that
 *    works. 302, not 301: browsers cache a permanent redirect aggressively and
 *    this is a deployment detail that may want reversing. Path and query are
 *    preserved.
 *
 * 2. Security headers, the set the sibling product sites send
 *    (docs/status/SITE_SPEC.md, P3). The CSP is as strict as the app allows:
 *    its own origin, plus fetches to the API. The pages contain no inline
 *    script (the JSON-LD blocks are data, not executed) and no inline style.
 *    scripts/check-site.mjs fails the build if either appears, or if the API
 *    origin the bundle was built for is not the one allowed here.
 *    If a CSP error ever shows in the console after a deploy, rename the header
 *    to Content-Security-Policy-Report-Only below while you look.
 *
 * 3. Caching. Fingerprinted assets under /assets/ never change, so they are
 *    `immutable`. HTML is revalidated on every load, because a deploy replaces
 *    the hashed files and stale HTML would point at ones that no longer exist.
 *    Never add stale-while-revalidate to HTML for that reason
 *    (SITE_SPEC.md, P2).
 *
 * A request for a URL with no file gets 404.html with a 404 status from the
 * Pages asset layer; this worker passes that status through untouched.
 *
 * This file lives in `public/` so Vite copies it verbatim to `dist/`, where
 * Pages picks it up.
 */

const CANONICAL_HOST = "journal-atlas.chroniclecore.com";
const API_ORIGIN = "https://api.journal-atlas.chroniclecore.com";

function contentSecurityPolicy(env) {
  // `CSP_CONNECT_EXTRA` is for scripts/preview.mjs, which points the built
  // bundle at a local API. It is not set on Cloudflare.
  const connect = ["'self'", API_ORIGIN, env && env.CSP_CONNECT_EXTRA].filter(Boolean).join(" ");
  return [
    "default-src 'self'",
    "script-src 'self'",
    "style-src 'self'",
    "img-src 'self' data:",
    "font-src 'self'",
    `connect-src ${connect}`,
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'none'",
    "frame-ancestors 'none'",
    "upgrade-insecure-requests",
  ].join("; ");
}

const SECURITY_HEADERS = {
  "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
  "X-Content-Type-Options": "nosniff",
  "X-Frame-Options": "DENY",
  "Referrer-Policy": "strict-origin-when-cross-origin",
  "Permissions-Policy": "camera=(), microphone=(), geolocation=(), payment=(), usb=()",
};

function cacheControl(url, response) {
  const type = response.headers.get("content-type") || "";
  if (response.status >= 400) return "no-cache";
  if (url.pathname.startsWith("/assets/")) return "public, max-age=31536000, immutable";
  if (type.includes("text/html")) return "public, max-age=0, must-revalidate";
  return "public, max-age=3600";
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname.endsWith(".pages.dev")) {
      url.hostname = CANONICAL_HOST;
      url.protocol = "https:";
      url.port = "";
      return Response.redirect(url.toString(), 302);
    }

    const upstream = await env.ASSETS.fetch(request);
    const response = new Response(upstream.body, upstream);
    for (const [name, value] of Object.entries(SECURITY_HEADERS)) response.headers.set(name, value);
    response.headers.set("Content-Security-Policy", contentSecurityPolicy(env));
    if (response.status < 300 || response.status >= 400) {
      response.headers.set("Cache-Control", cacheControl(url, response));
    }
    return response;
  },
};
