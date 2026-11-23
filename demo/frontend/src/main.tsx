import { StrictMode } from 'react'
import { createRoot, hydrateRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

const container = document.getElementById('root')!
const app = (
  <StrictMode>
    <App pathname={window.location.pathname} />
  </StrictMode>
)

// A production build arrives with the first render already in the HTML (see
// prerender.js); the dev server sends an empty root.
if (container.hasChildNodes()) hydrateRoot(container, app)
else createRoot(container).render(app)
