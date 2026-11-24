/**
 * Enough of Cloudflare Pages to run public/_worker.js against dist/ locally.
 *
 * `vite preview` serves the files but not the three behaviours the live site
 * depends on: the worker's headers, a real 404 for an unknown URL, and the
 * `/about` to `/about/` redirect. This provides an `ASSETS` binding with those
 * behaviours so the worker can be tested and previewed without wrangler and
 * without touching Cloudflare.
 *
 * It follows what Pages documents and what the sibling static sites show
 * (a 404.html is served with a 404 status for anything that is not a file);
 * it has not been compared byte for byte against Cloudflare, so the post-deploy
 * smoke test (scripts/smoke.mjs against the live URL) stays the final word.
 */
import { readFile, stat } from "node:fs/promises";
import { createServer } from "node:http";
import { extname, join, normalize, sep } from "node:path";
import { pathToFileURL } from "node:url";

const TYPES = {
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".txt": "text/plain; charset=utf-8",
  ".xml": "application/xml",
  ".json": "application/json",
};

async function isFile(path) {
  try {
    return (await stat(path)).isFile();
  } catch {
    return false;
  }
}

async function isDir(path) {
  try {
    return (await stat(path)).isDirectory();
  } catch {
    return false;
  }
}

function respond(body, status, file) {
  return new Response(body, {
    status,
    headers: { "content-type": TYPES[extname(file)] ?? "application/octet-stream" },
  });
}

/** An `ASSETS` binding over a built `dist/` directory. */
export function makeAssets(dist) {
  return {
    async fetch(request) {
      const url = new URL(request.url);
      const rel = normalize(decodeURIComponent(url.pathname)).replace(/^[/\\]+/, "");
      // Refuse to leave dist/: normalize() resolves "..", this makes it a 404.
      const path = join(dist, rel);
      if (path !== dist && !path.startsWith(dist + sep)) return notFound(dist);

      if (url.pathname.endsWith("/")) {
        const index = join(path, "index.html");
        if (await isFile(index)) return respond(await readFile(index), 200, index);
        return notFound(dist);
      }
      if (await isFile(path)) return respond(await readFile(path), 200, path);
      if (await isDir(path) && (await isFile(join(path, "index.html")))) {
        const to = new URL(request.url);
        to.pathname += "/";
        return Response.redirect(to.toString(), 308);
      }
      return notFound(dist);
    },
  };
}

async function notFound(dist) {
  const page = join(dist, "404.html");
  if (await isFile(page)) return respond(await readFile(page), 404, page);
  return new Response("Not found", { status: 404 });
}

/** A local HTTP server running the built worker over the built files. */
export async function startServer({ dist, port, env = {} }) {
  const worker = (await import(pathToFileURL(join(dist, "_worker.js")).href)).default;
  const bindings = { ASSETS: makeAssets(dist), ...env };
  const server = createServer(async (req, res) => {
    const origin = `http://${req.headers.host}`;
    const request = new Request(origin + req.url, { method: req.method, headers: req.headers });
    const response = await worker.fetch(request, bindings);
    res.writeHead(response.status, Object.fromEntries(response.headers));
    res.end(Buffer.from(await response.arrayBuffer()));
  });
  await new Promise((resolve) => server.listen(port, "127.0.0.1", resolve));
  return server;
}
