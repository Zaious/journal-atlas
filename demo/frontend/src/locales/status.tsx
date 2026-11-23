import type { ReactNode } from "react";
import type { Limits } from "../api";
import type { Lang } from "../i18n";
import { ISSUES_URL } from "../site";

/** The words on the Status page. English is the original. */
export interface StatusText {
  title: string;
  lede: string;
  rightNow: string;
  api: string;
  checking: string;
  reachable: string;
  unreachable: string;
  modelAccess: string;
  modelReady: (provider: string | null) => string;
  modelNotReady: string;
  modelUnknown: string;
  readsLabel: string;
  writesLabel: string;
  searchesToday: string;
  searchesTodayValue: (l: Limits) => string;
  entriesServed: string;
  recentUse: string;
  /** Replaces the API's own English note on the Chinese page. */
  recentNote: string;
  recentIntro: (note: string) => ReactNode;
  tableCaption: string;
  cols: { day: string; searches: string; finished: string; none: string; failed: string; refused: string };
  ifDownHeading: string;
  ifDown: ReactNode;
}

export const STATUS: Record<Lang, StatusText> = {
  en: {
    title: "Status",
    lede: "This page asks the API when you open it. If it cannot get an answer it says so; it never assumes the demo is fine.",
    rightNow: "Right now",
    api: "API",
    checking: "Checking…",
    reachable: "Reachable",
    unreachable: "Not reachable from your browser. The demo is down, or something between you and it is.",
    modelAccess: "Model access",
    modelReady: (provider) => `Ready (${provider})`,
    modelNotReady: "Not ready: the demo cannot call a model right now",
    modelUnknown: "Unknown: the API did not answer",
    readsLabel: "Reads your description",
    writesLabel: "Writes the recommendation",
    searchesToday: "Searches today",
    searchesTodayValue: (l) =>
      `${l.global_used_today} of ${l.global_daily_limit} (shared by everyone; each visitor gets ${l.per_client_hourly_limit} an hour)`,
    entriesServed: "Entries served",
    recentUse: "Recent use",
    recentNote: "",
    recentIntro: (note) => (
      <>
        Days are UTC. {note} The most useful column is &ldquo;found nothing&rdquo;: that is where someone asked and the
        knowledge base had no entry that fit.
      </>
    ),
    tableCaption: "Searches per day and how they ended",
    cols: {
      day: "Day",
      searches: "Searches",
      finished: "Finished",
      none: "Found nothing",
      failed: "Failed",
      refused: "Turned away",
    },
    ifDownHeading: "If it is down",
    ifDown: (
      <>
        There is no uptime promise: this is a research demo on one person&apos;s key and one small server. The
        knowledge base is plain files in the repository and the skill runs without this site, so a dead demo does not
        take the data with it. If you see a fault that is not listed here,{" "}
        <a href={ISSUES_URL} target="_blank" rel="noreferrer">
          open an issue
        </a>
        .
      </>
    ),
  },
  "zh-Hant": {
    title: "狀態",
    lede: "本頁在你開啟時向 API 詢問。如果得不到回應，它會直接說明；它絕不會預設示範一切正常。",
    rightNow: "目前",
    api: "API",
    checking: "檢查中…",
    reachable: "可連線",
    unreachable: "你的瀏覽器連不上。示範已停擺，或是你與它之間有什麼出了問題。",
    modelAccess: "模型存取",
    modelReady: (provider) => `就緒（${provider}）`,
    modelNotReady: "尚未就緒：示範目前無法呼叫模型",
    modelUnknown: "未知：API 沒有回應",
    readsLabel: "讀取你的描述",
    writesLabel: "撰寫推薦",
    searchesToday: "今日搜尋次數",
    searchesTodayValue: (l) =>
      `${l.global_used_today} / ${l.global_daily_limit}（所有人共用；每位訪客每小時 ${l.per_client_hourly_limit} 次）`,
    entriesServed: "提供的條目數",
    recentUse: "近期使用",
    recentNote: "匿名彙總，只存在記憶體中：不含位址、不含文字、不含識別碼。伺服器重新啟動時會從零開始，所以某一天的數字可能不完整。",
    recentIntro: (note) => (
      <>
        日期以 UTC 計。{note}最有用的是「沒找到」那一欄：那是有人問了、而知識庫裡沒有合適條目的地方。
      </>
    ),
    tableCaption: "每日搜尋次數及其結果",
    cols: {
      day: "日期",
      searches: "搜尋",
      finished: "完成",
      none: "沒找到",
      failed: "失敗",
      refused: "被拒絕",
    },
    ifDownHeading: "如果它掛了",
    ifDown: (
      <>
        我們不承諾上線時間：這是跑在一個人的金鑰和一台小伺服器上的研究示範。知識庫是儲存庫裡的純文字檔，skill 也不依賴本站運作，所以示範掛掉不會把資料帶走。如果你看到這裡沒有列出的故障，請{" "}
        <a href={ISSUES_URL} target="_blank" rel="noreferrer">
          開一則 issue
        </a>
        。
      </>
    ),
  },
};
