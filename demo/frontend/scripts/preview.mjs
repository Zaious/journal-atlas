/**
 * Preview the built site the way Cloudflare will serve it: the real
 * public/_worker.js (headers, pages.dev redirect) over dist/, with a 404 page
 * for unknown URLs. `npm run build` first.
 *
 *   npm run preview                 http://localhost:4600
 *   node scripts/preview.mjs 8080   another port
 *
 * The page talks to whatever API it was built for. To try the CSP against a
 * local backend, build with VITE_API_BASE=http://localhost:8000 and the preview
 * adds that origin to connect-src for you (this server only; Cloudflare's
 * worker never does).
 */
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { startServer } from "./pages-emulator.mjs";

const dist = join(dirname(fileURLToPath(import.meta.url)), "..", "dist");
const port = Number(process.argv[2] ?? 4600);
const api = process.env.PREVIEW_API ?? "http://localhost:8000";

await startServer({ dist, port, env: { CSP_CONNECT_EXTRA: api } });
console.log(`preview: http://localhost:${port}/  (worker headers and 404 page active; API allowed: ${api})`);
