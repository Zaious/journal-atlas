import { Component, type ReactNode } from "react";
import { localePath, type Lang } from "../i18n";
import { ISSUES_URL } from "../site";

/**
 * Without a boundary a render error unmounts the whole tree and the visitor
 * sees a blank page with no way to tell what happened or what to do. Every
 * sibling product site has one (docs/status/SITE_SPEC.md, D4).
 */
export class ErrorBoundary extends Component<{ children: ReactNode; lang: Lang }, { failed: boolean }> {
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
    const zh = this.props.lang === "zh-Hant";
    return (
      <div className="shell">
        <main id="main" className="page prose" role="alert">
          <h1>{zh ? "這個頁面出錯了" : "Something broke on this page"}</h1>
          <p>
            {zh ? "請重新載入頁面。若持續發生，請" : "Reload the page. If it keeps happening, "}
            <a href={ISSUES_URL} target="_blank" rel="noreferrer">
              {zh ? "開一則 issue" : "open an issue"}
            </a>
            {zh
              ? "並說明你當時在做什麼；不需要附上你貼上的內容。"
              : " and say what you were doing; what you pasted is not needed."}
          </p>
          <p>
            <a href={localePath(this.props.lang, "/")}>{zh ? "回到起點" : "Back to the start"}</a>
          </p>
        </main>
      </div>
    );
  }
}
