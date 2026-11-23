import type { ComponentType } from "react";
import "./App.css";
import { ErrorBoundary } from "./components/ErrorBoundary";
import { Layout } from "./components/Layout";
import { LangContext, type Lang } from "./i18n";
import About from "./pages/About";
import Ai from "./pages/Ai";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import Privacy from "./pages/Privacy";
import Status from "./pages/Status";
import AboutZh from "./pages/zh-Hant/About";
import AiZh from "./pages/zh-Hant/Ai";
import PrivacyZh from "./pages/zh-Hant/Privacy";
import { resolvePage, type PageId } from "./site";

/**
 * Prose pages are one component per language, written side by side so a
 * paragraph, a link or a caveat in one has a visible counterpart in the other;
 * scripts/check-site.mjs fails the build if the two drift apart. Pages that are
 * mostly behaviour (Home, Status, NotFound) are one component that reads its
 * words from the language's message table.
 */
const BODIES: Record<Lang, Record<PageId, ComponentType>> = {
  en: { home: Home, about: About, ai: Ai, privacy: Privacy, status: Status, notfound: NotFound },
  "zh-Hant": { home: Home, about: AboutZh, ai: AiZh, privacy: PrivacyZh, status: Status, notfound: NotFound },
};

/**
 * One component per URL, chosen by path.
 *
 * There is no client-side router on purpose: each page is its own prerendered
 * HTML file (see prerender.js), links are ordinary links, and the sibling
 * static sites work the same way. The tool on the home page keeps its state
 * for as long as that page is open, which is all it ever did. The language is
 * part of the URL, so it is known at render time and never stored.
 */
function App({ pathname }: { pathname: string }) {
  const page = resolvePage(pathname);
  const Body = BODIES[page.lang][page.id];
  return (
    <LangContext.Provider value={page.lang}>
      <ErrorBoundary lang={page.lang}>
        <Layout page={page}>
          <Body />
        </Layout>
      </ErrorBoundary>
    </LangContext.Provider>
  );
}

export default App;
