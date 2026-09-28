import { StrictMode } from 'react'
import { renderToString } from 'react-dom/server'
import App from './App.tsx'

/** The app's first render as HTML, for prerender.js to write into dist/index.html. */
export function render(): string {
  return renderToString(
    <StrictMode>
      <App />
    </StrictMode>,
  )
}
