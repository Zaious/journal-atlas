import { Component, type ReactNode } from "react";
import { ISSUES_URL } from "../site";

/**
 * Without a boundary a render error unmounts the whole tree and the visitor
 * sees a blank page with no way to tell what happened or what to do. Every
 * sibling product site has one (docs/status/SITE_SPEC.md, D4).
 */
export class ErrorBoundary extends Component<{ children: ReactNode }, { failed: boolean }> {
  state = { failed: false };

  static getDerivedStateFromError() {
    return { failed: true };
  }

  componentDidCatch(error: unknown) {
    // No reporting endpoint exists on purpose (no analytics); the console is
    // where someone who files an issue can copy it from.
    console.error("Journal Atlas render error:", error);
  }

  render() {
    if (!this.state.failed) return this.props.children;
    return (
      <div className="shell">
        <main id="main" className="page prose" role="alert">
          <h1>Something broke on this page</h1>
          <p>
            Reload the page. If it keeps happening,{" "}
            <a href={ISSUES_URL} target="_blank" rel="noreferrer">
              open an issue
            </a>{" "}
            and say what you were doing; what you pasted is not needed.
          </p>
          <p>
            <a href="/">Back to the start</a>
          </p>
        </main>
      </div>
    );
  }
}
