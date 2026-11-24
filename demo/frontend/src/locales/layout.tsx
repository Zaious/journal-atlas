import type { ReactNode } from "react";
import { SITE } from "../site";
import { localePath, type Lang } from "../i18n";

/**
 * The words in the frame every page shares: skip link, header tag, footer
 * declarations. The English is the original; the Chinese carries the same
 * claims. Both are checked by scripts/check-site.mjs: the same links in the same
 * order in both languages, and no wording that claims human verification.
 */
interface LayoutText {
  skip: string;
  navAria: string;
  brandTag: string;
  source: string;
  sourceHint: string;
  switchLabel: string;
  support: string;
  supportAside: string;
  footerAria: string;
  footerLinks: { about: string; ai: string; privacy: string; status: string; source: string; report: string };
  declarations: (lang: Lang) => ReactNode;
}

export const LAYOUT: Record<Lang, LayoutText> = {
  en: {
    skip: "Skip to main content",
    navAria: "Site",
    brandTag: "Research prototype · AI-assisted",
    source: "Source",
    sourceHint: " (opens GitHub)",
    switchLabel: "Switch to English",
    support: SITE.supportLabel,
    supportAside: "(unlocks nothing; every feature is the same for everyone)",
    footerAria: "Site information",
    footerLinks: {
      about: "About",
      ai: "How it's made",
      privacy: "Privacy",
      status: "Status",
      source: "Source and knowledge base",
      report: "Report something wrong",
    },
    declarations: (lang) => (
      <>
        <p>
          Journal Atlas is a research project by{" "}
          <a href={SITE.author.url} target="_blank" rel="noreferrer">
            {SITE.author.handle}
          </a>
          , a{" "}
          <a href={SITE.studio.url} target="_blank" rel="noreferrer">
            {SITE.studio.name}
          </a>{" "}
          ({SITE.studio.nameZh}) production. Much of it is written by AI;{" "}
          <a href={localePath(lang, "/ai/")}>this page says which parts</a>.
        </p>
        <p>
          Not affiliated with, endorsed by, or sponsored by any journal,
          conference, publisher or index it names. Those names belong to their
          owners, and an entry is a description of a venue from public sources,
          not a statement by the venue.
        </p>
        <p>
          Knowledge base:{" "}
          <a href={SITE.license.contentUrl} target="_blank" rel="noreferrer">
            {SITE.license.content}
          </a>
          . Code:{" "}
          <a href={SITE.license.codeUrl} target="_blank" rel="noreferrer">
            {SITE.license.code}
          </a>
          . The site sets no cookies and loads no ads, analytics or third-party
          scripts.
        </p>
      </>
    ),
  },
  "zh-Hant": {
    skip: "跳到主要內容",
    navAria: "網站",
    brandTag: "研究原型 · AI 輔助",
    source: "原始碼",
    sourceHint: "（在 GitHub 開啟）",
    switchLabel: "切換為繁體中文",
    support: "請我喝杯咖啡",
    supportAside: "（不解鎖任何功能；每個人用到的功能都一樣）",
    footerAria: "網站資訊",
    footerLinks: {
      about: "關於",
      ai: "如何製作",
      privacy: "隱私",
      status: "狀態",
      source: "原始碼與知識庫",
      report: "回報錯誤",
    },
    declarations: (lang) => (
      <>
        <p>
          Journal Atlas 是{" "}
          <a href={SITE.author.url} target="_blank" rel="noreferrer">
            {SITE.author.handle}
          </a>{" "}
          的研究專案，由{" "}
          <a href={SITE.studio.url} target="_blank" rel="noreferrer">
            {SITE.studio.name}
          </a>
          （{SITE.studio.nameZh}）出品。其中大部分由 AI 撰寫；<a href={localePath(lang, "/ai/")}>本頁說明是哪些部分</a>。
        </p>
        <p>
          與本站提及的任何期刊、研討會、出版社或索引服務皆無隸屬、背書或贊助關係。這些名稱屬於其所有者；條目是依公開來源對該刊的描述，並非該刊本身的聲明。
        </p>
        <p>
          知識庫：
          <a href={SITE.license.contentUrl} target="_blank" rel="noreferrer">
            {SITE.license.content}
          </a>
          。程式碼：
          <a href={SITE.license.codeUrl} target="_blank" rel="noreferrer">
            {SITE.license.code}
          </a>
          。本站不設 cookie，也不載入廣告、分析或第三方腳本。
        </p>
        <p className="translation-note">中文為英文原文的翻譯，兩者有出入時以英文為準。</p>
      </>
    ),
  },
};

