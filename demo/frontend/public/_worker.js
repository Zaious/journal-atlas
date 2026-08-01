/**
 * Send every *.pages.dev hostname to the canonical domain.
 *
 * Cloudflare Pages always exposes the project at `<project>.pages.dev`, plus a
 * unique subdomain per deployment. Those URLs serve the app perfectly but
 * cannot reach the API: the backend's CORS allowlist names exactly one origin,
 * so the page loads and then every request fails with "Failed to fetch". A
 * public URL that renders correctly and does nothing is worse than one that
 * does not exist — it reads as the demo being broken.
 *
 * Redirecting rather than widening the allowlist keeps one canonical origin,
 * and means a shared pages.dev link still lands the visitor somewhere that
 * works.
 *
 * 302, not 301: browsers cache a permanent redirect aggressively and this is a
 * deployment detail that may want reversing. The path and query are preserved.
 *
 * This file lives in `public/` so Vite copies it verbatim to `dist/`, where
 * Pages picks it up. It intercepts every request, so it stays this small —
 * anything else it did would be a way for the whole site to break.
 */

const CANONICAL_HOST = "journal-atlas.chroniclecore.com";

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname.endsWith(".pages.dev")) {
      url.hostname = CANONICAL_HOST;
      url.protocol = "https:";
      url.port = "";
      return Response.redirect(url.toString(), 302);
    }
    return env.ASSETS.fetch(request);
  },
};
