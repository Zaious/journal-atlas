// oxlint-disable react/only-export-components -- a build entry, not a component module
import { StrictMode } from 'react'
import { renderToString } from 'react-dom/server'
import App from './App.tsx'

/** One page's first render as HTML, for prerender.js to write into its file. */
export function render(pathname: string): string {
  return renderToString(
    <StrictMode>
      <App pathname={pathname} />
    </StrictMode>,
  )
}

// What prerender.js and scripts/check-site.mjs need from the same modules the
// browser bundle uses, so the build and the gate read one definition of the site.
export { PAGES, SITE, absoluteUrl } from './site.ts'
export { headTags, sitemapXml, robotsTxt, llmsTxt } from './seo.ts'
