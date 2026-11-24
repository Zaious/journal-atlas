/**
 * What each page is called, in each language: the <title>, the description,
 * the label in the navigation. Everything else about a page (path, which source
 * files it is built from, whether it is indexable) is language-neutral and
 * lives in site.ts.
 *
 * The Chinese text is a translation of the English; where they differ, the
 * English is the original. It carries the same claims and no stronger ones.
 */
import type { Lang } from "../i18n";

export type PageId = "home" | "about" | "ai" | "privacy" | "status" | "notfound";

export interface PageText {
  title: string;
  description: string;
  navLabel?: string;
}

export const PAGE_TEXT: Record<Lang, Record<PageId, PageText>> = {
  en: {
    home: {
      title: "Journal Atlas: journal fit with the evidence shown",
      description:
        "Describe your paper and get journal and conference candidates scored against an open knowledge base. Every result shows how well each entry is evidenced.",
    },
    about: {
      title: "About Journal Atlas",
      description:
        "What Journal Atlas is, who maintains it, why it exists, and where to report a wrong entry.",
      navLabel: "About",
    },
    ai: {
      title: "How Journal Atlas is made, and what is AI",
      description:
        "Which parts of Journal Atlas are written by AI, which models run the demo, what no entry yet records, and what the project will not claim.",
      navLabel: "How it's made",
    },
    privacy: {
      title: "Privacy: what happens to the text you paste",
      description:
        "The text you paste is sent to a model provider to be read. This page says what is kept, what is not, and which third parties are involved.",
      navLabel: "Privacy",
    },
    status: {
      title: "Status",
      description: "Live status of the Journal Atlas demo: API reachability, models, daily limits and corpus version.",
      navLabel: "Status",
    },
    notfound: {
      title: "Page not found",
      description: "This address does not exist on Journal Atlas. Try the home page, the About page, or report a broken link.",
    },
  },
  "zh-Hant": {
    home: {
      title: "Journal Atlas：附上證據程度的期刊適配建議",
      description:
        "描述你的論文，即可取得依開放知識庫評分的期刊與研討會候選；每筆結果都標示該條目的證據程度。",
    },
    about: {
      title: "關於 Journal Atlas",
      description: "Journal Atlas 是什麼、誰在維護、為什麼存在，以及發現資料有誤時該往哪裡回報。",
      navLabel: "關於",
    },
    ai: {
      title: "Journal Atlas 如何製作，哪些部分是 AI",
      description:
        "Journal Atlas 的哪些部分由 AI 撰寫、示範由哪些模型運行、目前還沒有哪些條目記錄第一手報告，以及本專案不會宣稱什麼。",
      navLabel: "如何製作",
    },
    privacy: {
      title: "隱私：你貼上的文字會怎麼處理",
      description: "你貼上的文字會送到模型供應商閱讀。本頁說明哪些會被保留、哪些不會，以及涉及哪些第三方。",
      navLabel: "隱私",
    },
    status: {
      title: "狀態",
      description: "Journal Atlas 示範的即時狀態：API 是否可連線、模型、每日上限與語料版本。",
      navLabel: "狀態",
    },
    notfound: {
      title: "找不到頁面",
      description: "Journal Atlas 上沒有這個網址。請試試首頁、關於頁，或回報壞掉的連結。",
    },
  },
};

/** Alt text of the social-share image; the image itself is language-neutral. */
export const OG_IMAGE_ALT: Record<Lang, string> = {
  en: "Journal Atlas: journal fit with the evidence shown",
  "zh-Hant": "Journal Atlas：附上證據程度的期刊適配建議",
};
