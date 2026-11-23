import type { ComponentType } from "react";
import "./App.css";
import { ErrorBoundary } from "./components/ErrorBoundary";
import { Layout } from "./components/Layout";
import About from "./pages/About";
import Ai from "./pages/Ai";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import Privacy from "./pages/Privacy";
import Status from "./pages/Status";
import { resolvePage, type PageId } from "./site";

const BODIES: Record<PageId, ComponentType> = {
  home: Home,
  about: About,
  ai: Ai,
  privacy: Privacy,
  status: Status,
  notfound: NotFound,
};

/**
 * One component per URL, chosen by path.
 *
 * There is no client-side router on purpose: each page is its own prerendered
 * HTML file (see prerender.js), links are ordinary links, and the sibling
 * static sites work the same way. The tool on the home page keeps its state
 * for as long as that page is open, which is all it ever did.
 */
function App({ pathname }: { pathname: string }) {
  const page = resolvePage(pathname);
  const Body = BODIES[page.id];
  return (
    <ErrorBoundary>
      <Layout current={page.id}>
        <Body />
      </Layout>
    </ErrorBoundary>
  );
}

export default App;
