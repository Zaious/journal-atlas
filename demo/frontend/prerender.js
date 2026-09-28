/**
 * Write the page's first render into dist/index.html.
 *
 * Without this the served HTML is an empty <div id="root">, and everything on
 * the page — what the tool is, where the source lives, who made it — exists
 * only for clients that run the bundle. Crawlers that render JavaScript see it;
 * link checkers, `curl`, and many crawlers do not. Prerendering costs one build
 * step and nothing at runtime: main.tsx hydrates this markup rather than
 * replacing it.
 *
 * Only the initial state is rendered. Everything that comes from the API
 * (coverage counts, rate limits) is fetched in effects, which do not run on the
 * server, so this markup is exactly the client's first render and hydration has
 * nothing to reconcile.
 *
 * Runs as the last step of `npm run build`, after the SSR build of
 * src/entry-server.tsx into dist-ssr/.
 */
import { readFile, writeFile } from "node:fs/promises";

const TEMPLATE = new URL("./dist/index.html", import.meta.url);
const EMPTY_ROOT = '<div id="root"></div>';

const { render } = await import("./dist-ssr/entry-server.js");
const template = await readFile(TEMPLATE, "utf8");

// A second run would find the root already filled; fail rather than guess.
if (!template.includes(EMPTY_ROOT)) {
  console.error(`prerender: no empty ${EMPTY_ROOT} in dist/index.html to fill`);
  process.exit(1);
}

// No whitespace around the markup: hydration walks the DOM node by node, and a
// newline inside #root is a text node the server sent and the client did not.
await writeFile(TEMPLATE, template.replace(EMPTY_ROOT, `<div id="root">${render()}</div>`));
console.log("prerender: wrote the first render into dist/index.html");
