import type { ReactNode } from "react";
import { corePercent, type Coverage, type CoverageField, type Limits } from "../api";
import { localePath, type Lang } from "../i18n";
import { ISSUES_URL, SITE } from "../site";

/**
 * Every word on the home page, in each language. The English is the original
 * and moved here verbatim from Home.tsx; the Chinese is a translation that
 * carries the same claims and no stronger ones.
 *
 * Nothing here may contain a corpus number or a model name: those come from the
 * API (a test fails the build if one is typed into the front end). Values the
 * API sends as English prose (field labels, the list of absent fields) are
 * translated by lookup below and fall back to the English the server sent, so a
 * value this file has not seen is shown rather than hidden.
 */

const FIELD_ZH: Record<string, string> = {
  psychology: "心理學",
  philosophy: "哲學",
  hci: "HCI（期刊）",
  "cognitive-science": "認知科學",
  biology: "生物學",
  "conferences/hci": "HCI 研討會",
  multidisciplinary: "跨領域",
  "conferences/ml": "ML 研討會",
  medical: "醫學",
  "qualitative-methods": "質性方法",
  "conferences/nlp": "NLP 研討會",
  physics: "物理學",
  "conferences/data-mining": "資料探勘研討會",
};

const ABSENT_ZH: Record<string, string> = {
  "Library and information science (including digital libraries)": "圖書資訊學（含數位圖書館）",
  Sociology: "社會學",
  Anthropology: "人類學",
  "Chemistry, mathematics, and the earth sciences": "化學、數學與地球科學",
};

const CORE_LABEL_ZH: Record<string, string> = {
  "psychology, philosophy, HCI and cognitive science": "心理學、哲學、HCI 與認知科學",
};

/** A field's name as the page's language shows it. */
export function fieldLabel(lang: Lang, f: CoverageField): string {
  return lang === "zh-Hant" ? (FIELD_ZH[f.field] ?? f.label) : f.label;
}

function coreLabel(lang: Lang, c: Coverage): string {
  return lang === "zh-Hant" ? (CORE_LABEL_ZH[c.core_label] ?? c.core_label) : c.core_label;
}

/** One absent field's name in the page's language (falls back to the server's English). */
export function absentLabel(lang: Lang, a: string): string {
  return lang === "zh-Hant" ? (ABSENT_ZH[a] ?? a) : a;
}

function absentList(lang: Lang, absent: string[], sep: string): string {
  return absent.map((a) => (lang === "zh-Hant" ? (ABSENT_ZH[a] ?? a) : a)).join(sep);
}

export type StageName = "parsing" | "screening" | "synthesis";
export type StageStatus = "pending" | "active" | "done";

interface SectionsContext {
  coverage: Coverage | null;
  limits: Limits | null;
  /** The copyable install command block. */
  install: ReactNode;
  /** The pictures beside the first two sections (components/HomeVisuals.tsx). */
  evidenceVisual: ReactNode;
  unknownVisual: ReactNode;
  /** The dated "no entry records a first-hand report" sentence. */
  humanEvidence: ReactNode;
}

export interface ShotFacts {
  shown: number;
  returned: number;
  corpus: string;
  date: string;
}

export interface HomeText {
  // ---- hero ----
  kicker: string;
  heroTitle: string;
  heroSub: string;
  installCta: string;
  paperLink: ReactNode;
  shotAria: string;
  shotQueryLabel: string;
  shotCaption: (f: ShotFacts) => ReactNode;
  // ---- coverage notice ----
  coverageSummary: (c: Coverage) => ReactNode;
  coverageCaption: string;
  colField: string;
  colEntries: string;
  tierTitles: { t1: string; t2: string; ai: string };
  coverageAbsent: (c: Coverage) => ReactNode;
  coverageNotForYou: string;
  coverageThin: (c: Coverage, philosophy: CoverageField | null) => ReactNode;
  coverageSee: (humanEvidence: ReactNode) => ReactNode;
  // ---- errors ----
  tooLong: (limit: string) => string;
  serverError: (status: number) => string;
  // ---- copy button ----
  copy: { idle: string; copied: string; select: string; copiedSr: string; selectSr: string };
  // ---- the product page under the hero ----
  legendTitle: string;
  legend: { t1: string; t2: string; ai: string };
  legendScoreLabel: string;
  unknownTitle: string;
  unknownLoading: string;
  unknownNone: string;
  unstatedTitle: string;
  unstatedCaption: string;
  sections: (ctx: SectionsContext) => ReactNode;
  // ---- the tool ----
  stageLabels: (total: number | null) => Record<StageName, string>;
  stageState: Record<StageStatus, string>;
  repoLink: string;
  eyebrow: ReactNode;
  tagline: string;
  paperLabel: string;
  paperPlaceholder: string;
  paperNote: (provider: string | null) => ReactNode;
  working: string;
  findJournal: string;
  noscript: string;
  recommendationReady: string;
  readHeading: string;
  topics: string;
  methodology: string;
  sensitive: string;
  clarifyHeading: string;
  clarifyAnswersLabel: string;
  clarifyPlaceholder: string;
  clarifyAnswer: string;
  clarifySkip: string;
  candidatesHeading: (n: number) => string;
  disputedTag: string;
  evidencePct: (pct: number) => string;
  evidencePctTitle: string;
  tiedWith: (n: number) => string;
  tiedTitle: (n: number) => string;
  disputedClaim: string;
  articles: (n: number) => string;
  noTopicData: string;
  recommendationHeading: string;
  followupHeading: (left: number) => string;
  followupLabel: string;
  followupPlaceholder: string;
  ask: string;
  thinking: string;
  followupLimit: string;
}

export const HOME: Record<Lang, HomeText> = {
  en: {
    kicker: "Open-source agent skill · Free",
    heroTitle: "Where your paper fits, and how sure we are.",
    heroSub:
      "Describe your paper. Journal Atlas ranks journals and conferences from an open knowledge base and shows, for each one, how much of what it says is evidenced. No account, no install.",
    installCta: "Install the skill",
    paperLink: (
      <>
        Paper at{" "}
        <a href={SITE.paper.doiUrl} target="_blank" rel="noreferrer">
          {SITE.paper.venue}
        </a>{" "}
        ({SITE.paper.track}) · <a href="/about/#paper">How to cite</a>
      </>
    ),
    shotAria: "A real screening result: three candidate journals, each with an evidence tier, a score and how much of the score had data behind it.",
    shotQueryLabel: "Example paper",
    shotCaption: (f) => (
      <>
        A real screening run, not a mock-up: the top {f.shown} of the {f.returned} candidates the scoring script
        returned for this example, from corpus <code>{f.corpus}</code> on {f.date}. The paper&apos;s attributes were
        entered by hand; the ranking, tiers, coverage and article counts are the script&apos;s output. Tier 2 is a
        family-level estimate, not a checked fact.
      </>
    ),
    coverageSummary: (c) => (
      <>
        Covers <strong>{coreLabel("en", c)}</strong> in depth — {corePercent(c)}% of {c.total} entries. Many fields are
        not covered at all. <span className="coverage-more">What&apos;s in here?</span>
      </>
    ),
    coverageCaption: "Entries per field, by how each entry was written",
    colField: "Field",
    colEntries: "Entries",
    tierTitles: {
      t1: "Evidence-backed: specific article counts, source URLs, dates",
      t2: "Community estimate: family-level, no per-claim evidence yet",
      ai: "AI-researched: per-journal sources, honest blanks, no human review recorded",
    },
    coverageAbsent: (c) => (
      <>
        <strong>Verifiably absent</strong> (probed {c.absent_checked}): {absentList("en", c.absent, " · ")}. Economics,
        law and political science exist only as philosophy journals <em>about</em> those subjects. There is no
        marketing, no nursing science, and no engineering beyond three robotics venues.
      </>
    ),
    coverageNotForYou:
      "If your field is on that list, this tool has nothing for you yet — and it will tell you that rather than ranking the nearest journals it happens to hold.",
    coverageThin: (c, philosophy) => (
      <>
        Entries also differ in <strong>how much of each one is filled in</strong>. Unscorable dimensions return
        &quot;unknown&quot; instead of a midpoint, so every candidate carries an evidence-coverage figure. The{" "}
        {c.tiers.ai} AI-researched entries are missing the parts that need lived submission experience, so they
        usually show far less coverage than the others.{" "}
        {philosophy && (
          <strong>
            Philosophy is the sharpest case: all {philosophy.total} of its entries are AI-researched.
          </strong>
        )}{" "}
        Scores on thin evidence are already pulled toward a neutral 50, but treat them as leads to check.
      </>
    ),
    coverageSee: (humanEvidence) => (
      <>
        {humanEvidence} See <a href="/ai/">how the entries were made</a>.
      </>
    ),
    tooLong: (limit) =>
      `That description is too long for the demo — paste an abstract or a summary rather than the full manuscript. (Limit: ${limit} characters.)`,
    serverError: (status) => `Server error (${status})`,
    copy: {
      idle: "Copy",
      copied: "Copied",
      select: "Ctrl+C",
      copiedSr: "Copied to clipboard",
      selectSr: "Text selected; press Ctrl+C",
    },
    legendTitle: "What the badge means",
    legend: {
      t1: "Specific sources, article counts and dates behind each claim.",
      t2: "A family-level estimate: one claim adapted across similar journals.",
      ai: "Researched per journal by an AI model from public sources; blanks where nothing was found.",
    },
    legendScoreLabel: "From the screening run above",
    unknownTitle: "Not covered yet",
    unknownLoading: "Loading the list of fields with no entries from the API…",
    unknownNone: "0 entries",
    unstatedTitle: "Not stated, so not applied",
    unstatedCaption: "The tool's own words for the example paper above.",
    sections: ({ coverage, limits, install, evidenceVisual, unknownVisual, humanEvidence }) => (
      <>
        <section className="feature" aria-labelledby="f-evidence">
          <div className="feature-copy">
            <h2 id="f-evidence">Every answer shows its evidence.</h2>
            <p>
              Each entry carries a tier that says how it was written, and every score carries how much of it had data
              behind it. A score built on little is pulled toward a neutral 50 instead of looking confident.
            </p>
            <p>
              <a href="/ai/">How the entries are made</a>
            </p>
          </div>
          <div className="feature-visual">{evidenceVisual}</div>
        </section>

        <section className="feature flip" aria-labelledby="f-unknown">
          <div className="feature-copy">
            <h2 id="f-unknown">When it doesn&apos;t know, it says so.</h2>
            <p>
              Many fields are not covered at all, and the tool tells you that instead of ranking the nearest journals it
              happens to hold. Constraints you did not state are listed back to you, not guessed.
            </p>
          </div>
          <div className="feature-visual">{unknownVisual}</div>
        </section>

        <section className="feature" id="install" aria-labelledby="f-install">
          <div className="feature-copy">
            <h2 id="f-install">Run it in your own AI, with no cap.</h2>
            <p>
              The demo runs on one person&apos;s key, so it is capped. The skill runs inside your own Claude session, on
              your own key, over the same knowledge base, and can read your actual manuscript instead of a pasted
              summary. In a Claude Code <strong>main session</strong>:
            </p>
          </div>
          <div className="feature-visual">
            {install}
            <p className="footnote">
              Then restart Claude Code. Claude Desktop, ChatGPT and plain-git setups are in the{" "}
              <a href={`${SITE.repoUrl}#installation`} target="_blank" rel="noreferrer">
                installation guide
              </a>
              .
            </p>
          </div>
        </section>

        <section className="cta-band" aria-labelledby="f-maintain">
          <h2 id="f-maintain">It needs more than one maintainer.</h2>
          <p>
            Scholarly tools die when the one person behind them moves on. The licences ({SITE.license.content} for the
            knowledge base, {SITE.license.code} for the code) mean nobody can be locked out of a fork. What it needs most
            is people who will correct entries about journals they know.
          </p>
          <div className="cta-actions">
            <a className="button-link primary" href={ISSUES_URL} target="_blank" rel="noreferrer">
              Report a wrong entry
            </a>
            <a className="button-link secondary" href={`${SITE.repoUrl}/blob/main/CONTRIBUTING.md`} target="_blank" rel="noreferrer">
              Contribute an entry
            </a>
          </div>
        </section>

        <section className="faq" aria-labelledby="f-faq">
          <div className="faq-head">
            <h2 id="f-faq">Questions</h2>
            <p>
              Something else? Ask in a{" "}
              <a href={ISSUES_URL} target="_blank" rel="noreferrer">
                GitHub issue
              </a>
              .
            </p>
          </div>
          <div className="faq-list">
          <details>
            <summary>Is it free? Why is there a limit?</summary>
            <p>
              Yes. The demo&apos;s model calls are billed to the maintainer personally, which is the only reason it is
              capped
              {limits
                ? ` at ${limits.per_client_hourly_limit} searches an hour per person and ${limits.global_daily_limit} a day across everyone`
                : ""}
              . There is no paid tier. The skill runs with no cap on your own key.
            </p>
          </details>
          <details>
            <summary>Where does the data come from?</summary>
            <p>
              {coverage
                ? `The knowledge base holds ${coverage.total} entries: ${coverage.tiers.tier1} Tier 1, ${coverage.tiers.tier2} Tier 2 and ${coverage.tiers.ai} AI-researched. `
                : ""}
              Tier 1 entries cite specific sources, Tier 2 entries are family-level estimates, and AI-researched
              entries were researched journal by journal from public sources. {humanEvidence}{" "}
              <a href="/ai/">How it&apos;s made</a>.
            </p>
          </details>
          <details>
            <summary>How much of this is written by AI?</summary>
            <p>
              Much of it: the site&apos;s code, the AI-researched entries, and every written recommendation. Scores come
              from a script, not a model. <a href="/ai/">The How it&apos;s made page</a> lists each part.
            </p>
          </details>
          <details>
            <summary>What happens to the text I paste?</summary>
            <p>
              It is sent to a language-model provider to be read, and this site does not save it. Paste an abstract,
              not a manuscript under review. <a href="/privacy/">Privacy</a>.
            </p>
          </details>
          <details>
            <summary>My field isn&apos;t covered. What can I do?</summary>
            <p>
              Bring it in: the AI-research run that added the AI-researched entries is{" "}
              <a
                href={`${SITE.repoUrl}/blob/main/docs/workorders/WO2_SOFT_METADATA_BATCH.md`}
                target="_blank"
                rel="noreferrer"
              >
                published
              </a>
              , so you can point it at your field. Or, if you have submitted to or reviewed for a journal, add what no
              amount of research reaches. No entry records that yet.
            </p>
          </details>
          </div>
        </section>

        <section className="trust" aria-labelledby="f-trust">
          <h2 id="f-trust">Nothing to sign up for.</h2>
          <p>
            No account, no cookies, no ads. What you paste goes to a language-model provider to be read and is not saved
            by this site; the API keeps only anonymous daily totals, with no address and no text.{" "}
            <a href="/privacy/">Privacy</a>
          </p>
        </section>
      </>
    ),
    stageLabels: (total) => ({
      parsing: "Reading your paper",
      screening: total ? `Screening ${total} entries` : "Screening the knowledge base",
      synthesis: "Writing your recommendation",
    }),
    stageState: { pending: "waiting", active: "in progress", done: "done" },
    repoLink: "Source on GitHub",
    eyebrow: (
      <>
        A live demo of an open-source <strong>agent skill</strong> — the thing answering you here installs into your
        own AI session in one command, and runs there without this page or its limits.
      </>
    ),
    tagline:
      "Paste your abstract or describe your paper. No account, no install — this reads the same open knowledge base the real skill uses, and shows for every entry how it was written and how much of it is evidenced.",
    paperLabel: "Your paper",
    paperPlaceholder:
      "e.g. A survey of how graduate students choose and use reference managers, with follow-up interviews. About 7,000 words, no budget for open-access fees, discloses AI-assisted copyediting…",
    paperNote: (provider) => (
      <>
        What you paste is sent to a language-model provider
        {provider ? ` (currently ${provider})` : ""} to be read, and this site does not save it. Paste an abstract,
        not a manuscript that is under review. <a href="/privacy/">What happens to it</a>.
      </>
    ),
    working: "Working…",
    findJournal: "Find my journal",
    noscript:
      "The recommender needs JavaScript. The knowledge base itself is plain Markdown in the repository.",
    recommendationReady: "Recommendation ready",
    readHeading: "What I read from your description",
    topics: "Topics:",
    methodology: "Methodology:",
    sensitive: "Flagged sensitive content:",
    clarifyHeading: "A couple of questions first",
    clarifyAnswersLabel: "Your answers",
    clarifyPlaceholder: "e.g. no budget at all; about 8,000 words; conferences are fine too",
    clarifyAnswer: "Answer and search",
    clarifySkip: "Skip — search anyway",
    candidatesHeading: (n) => `Top ${n} candidates after screening`,
    disputedTag: "Disputed",
    evidencePct: (pct) => `${pct}% evidence`,
    evidencePctTitle: "Share of the scoring dimensions that had actual data behind them",
    tiedWith: (n) => `tied with ${n}`,
    tiedTitle: (n) =>
      `Scores identically to ${n} other candidate${n > 1 ? "s" : ""} on all six dimensions. The order between them is arbitrary.`,
    disputedClaim: "Disputed claim:",
    articles: (n) => `${n} articles`,
    noTopicData: "No topic-count data on file for this entry yet.",
    recommendationHeading: "Recommendation",
    followupHeading: (left) => `Follow-up ${left > 0 ? `(${left} left)` : "(none left)"}`,
    followupLabel: "Your follow-up question",
    followupPlaceholder: "e.g. why not CHI? / what would I need to change for the second choice?",
    ask: "Ask",
    thinking: "Thinking…",
    followupLimit:
      "Two follow-ups is the limit for this demo. Edit your description above and search again to explore a different angle.",
  },

  "zh-Hant": {
    kicker: "開源 agent skill · 免費",
    heroTitle: "你的論文該投哪裡，以及我們有多確定。",
    heroSub:
      "描述你的論文。Journal Atlas 從一份開放知識庫排出期刊與研討會，並為每一個標示它所說的內容有多少有證據。免註冊、免安裝。",
    installCta: "安裝 skill",
    paperLink: (
      <>
        論文發表於{" "}
        <a href={SITE.paper.doiUrl} target="_blank" rel="noreferrer">
          {SITE.paper.venue}
        </a>
        （展示論文）· <a href="/zh-hant/about/#paper">引用方式</a>
      </>
    ),
    shotAria: "一次真實的篩選結果：三本候選期刊，每本都附上證據層級、分數，以及分數中有多少有資料支撐。",
    shotQueryLabel: "範例論文",
    shotCaption: (f) => (
      <>
        這是一次真實的篩選，不是示意圖：評分腳本為這個範例回傳的 {f.returned} 個候選中的前 {f.shown} 名，語料版本 <code>{f.corpus}</code>，{f.date}
        。論文屬性是手動輸入的；排名、tier、涵蓋率與文章篇數都是腳本的輸出。Tier 2 是家族層級的估計，不是查證過的事實。
      </>
    ),
    coverageSummary: (c) => (
      <>
        深入涵蓋<strong>{coreLabel("zh-Hant", c)}</strong>——占 {c.total} 筆條目的 {corePercent(c)}%。許多領域完全沒有涵蓋。
        <span className="coverage-more">這裡面有什麼？</span>
      </>
    ),
    coverageCaption: "各領域的條目數，依條目的撰寫方式分列",
    colField: "領域",
    colEntries: "條目",
    tierTitles: {
      t1: "有證據支持：具體文章篇數、來源網址與日期",
      t2: "社群估計：家族層級，尚無逐項主張的證據",
      ai: "AI 研究：逐刊來源、誠實留白，未記錄任何人工複核",
    },
    coverageAbsent: (c) => (
      <>
        <strong>可確認缺少</strong>（{c.absent_checked} 查證）：{absentList("zh-Hant", c.absent, "、")}。經濟學、法學與政治學只以「談論這些主題的哲學期刊」的形式存在。沒有行銷學、沒有護理學，工程領域除了三個機器人場地之外也沒有。
      </>
    ),
    coverageNotForYou:
      "如果你的領域在這份清單上，這個工具目前沒有東西可以給你——它會直接告訴你，而不是把手上最接近的期刊排給你。",
    coverageThin: (c, philosophy) => (
      <>
        條目還有一個差異：<strong>每一筆填了多少</strong>。無法評分的維度會回傳「未知」而不是中間值，所以每個候選都附有證據涵蓋率。{c.tiers.ai} 筆 AI 研究條目缺少需要實際投稿經驗才有的部分，因此涵蓋率通常遠低於其他條目。{" "}
        {philosophy && <strong>哲學是最極端的例子：它的 {philosophy.total} 筆條目全部是 AI 研究。</strong>}{" "}
        證據薄弱的分數已被拉向中性的 50，但仍請把它們當作待查證的線索。
      </>
    ),
    coverageSee: (humanEvidence) => (
      <>
        {humanEvidence} 請見<a href={localePath("zh-Hant", "/ai/")}>條目是怎麼製作的</a>。
      </>
    ),
    tooLong: (limit) => `這段描述對示範來說太長——請貼摘要或概述，而不是整份稿件。（上限：${limit} 字元。）`,
    serverError: (status) => `伺服器錯誤（${status}）`,
    copy: {
      idle: "複製",
      copied: "已複製",
      select: "Ctrl+C",
      copiedSr: "已複製到剪貼簿",
      selectSr: "文字已選取；請按 Ctrl+C",
    },
    legendTitle: "標章代表什麼",
    legend: {
      t1: "每項主張背後都有具體來源、文章篇數與日期。",
      t2: "家族層級的估計：同一個主張調整後套用到相似的期刊。",
      ai: "由 AI 模型依公開來源逐刊研究；找不到的就留白。",
    },
    legendScoreLabel: "取自上方那次篩選",
    unknownTitle: "尚未涵蓋",
    unknownLoading: "正在從 API 載入沒有任何條目的領域清單…",
    unknownNone: "0 筆",
    unstatedTitle: "沒有說明，所以沒有套用",
    unstatedCaption: "工具對上方範例論文的原文輸出（英文）。",
    sections: ({ coverage, limits, install, evidenceVisual, unknownVisual, humanEvidence }) => (
      <>
        <section className="feature" aria-labelledby="f-evidence">
          <div className="feature-copy">
            <h2 id="f-evidence">每個答案都標出證據。</h2>
            <p>
              每個條目都帶有一個 tier，說明它是怎麼寫成的；每個分數都附上其中有多少有資料支撐。所知甚少的分數會被拉向中性的 50，而不是看起來很有把握。
            </p>
            <p>
              <a href="/zh-hant/ai/">條目是怎麼製作的</a>
            </p>
          </div>
          <div className="feature-visual">{evidenceVisual}</div>
        </section>

        <section className="feature flip" aria-labelledby="f-unknown">
          <div className="feature-copy">
            <h2 id="f-unknown">不知道，就說不知道。</h2>
            <p>
              許多領域完全沒有涵蓋，工具會直接告訴你，而不是把手上最接近的期刊排給你。你沒有說明的限制條件會列回給你，而不是被猜測。
            </p>
          </div>
          <div className="feature-visual">{unknownVisual}</div>
        </section>

        <section className="feature" id="install" aria-labelledby="f-install">
          <div className="feature-copy">
            <h2 id="f-install">裝進你自己的 AI，沒有上限。</h2>
            <p>
              示範跑在一個人的金鑰上，所以設有上限。skill 跑在你自己的 Claude 工作階段裡、用你自己的金鑰、讀同一份知識庫，還能讀你真正的稿件，而不只是貼上的摘要。在 Claude Code 的<strong>主工作階段</strong>中：
            </p>
          </div>
          <div className="feature-visual">
            {install}
            <p className="footnote">
              然後重新啟動 Claude Code。Claude Desktop、ChatGPT 與純 git 的設定方式見
              <a href={`${SITE.repoUrl}#installation`} target="_blank" rel="noreferrer">
                安裝指南
              </a>
              。
            </p>
          </div>
        </section>

        <section className="cta-band" aria-labelledby="f-maintain">
          <h2 id="f-maintain">它需要不只一位維護者。</h2>
          <p>
            學術工具常在背後那一個人離開時跟著死去。授權（知識庫 {SITE.license.content}、程式碼 {SITE.license.code}
            ）確保沒有人會被擋在 fork 之外。它最需要的，是願意更正自己熟悉期刊條目的人。
          </p>
          <div className="cta-actions">
            <a className="button-link primary" href={ISSUES_URL} target="_blank" rel="noreferrer">
              回報錯誤的條目
            </a>
            <a className="button-link secondary" href={`${SITE.repoUrl}/blob/main/CONTRIBUTING.md`} target="_blank" rel="noreferrer">
              貢獻一個條目
            </a>
          </div>
        </section>

        <section className="faq" aria-labelledby="f-faq">
          <div className="faq-head">
            <h2 id="f-faq">常見問題</h2>
            <p>
              還有別的問題？請在{" "}
              <a href={ISSUES_URL} target="_blank" rel="noreferrer">
                GitHub issue
              </a>{" "}
              提出。
            </p>
          </div>
          <div className="faq-list">
          <details>
            <summary>免費嗎？為什麼有上限？</summary>
            <p>
              免費。示範的模型呼叫由維護者個人付費，這是它設有上限的唯一原因
              {limits ? `：每人每小時 ${limits.per_client_hourly_limit} 次搜尋，所有人合計每天 ${limits.global_daily_limit} 次` : ""}
              。沒有付費方案。skill 用你自己的金鑰跑，沒有上限。
            </p>
          </details>
          <details>
            <summary>資料從哪裡來？</summary>
            <p>
              {coverage
                ? `知識庫共有 ${coverage.total} 筆條目：Tier 1 ${coverage.tiers.tier1} 筆、Tier 2 ${coverage.tiers.tier2} 筆、AI 研究 ${coverage.tiers.ai} 筆。`
                : ""}
              Tier 1 條目引用具體來源，Tier 2 條目是家族層級的估計，AI 研究條目則依公開來源逐刊研究。{humanEvidence}
              <a href="/zh-hant/ai/">如何製作</a>。
            </p>
          </details>
          <details>
            <summary>這裡有多少是 AI 寫的？</summary>
            <p>
              很大一部分：網站程式碼、AI 研究條目，以及每一份撰寫出來的推薦。分數來自腳本，不是模型。
              <a href="/zh-hant/ai/">「如何製作」頁</a>逐項列出。
            </p>
          </details>
          <details>
            <summary>我貼上的文字會怎麼處理？</summary>
            <p>
              它會送到語言模型供應商閱讀，本站不會儲存。請貼摘要，不要貼審查中的稿件。<a href="/zh-hant/privacy/">隱私</a>。
            </p>
          </details>
          <details>
            <summary>我的領域不在裡面，可以怎麼做？</summary>
            <p>
              把它帶進來：新增 AI 研究條目的那次 AI 研究流程
              <a
                href={`${SITE.repoUrl}/blob/main/docs/workorders/WO2_SOFT_METADATA_BATCH.md`}
                target="_blank"
                rel="noreferrer"
              >
                已經公開
              </a>
              ，你可以把它指向你的領域。或者，如果你投稿過或審查過某本期刊，請補上再多研究也摸不到的部分。目前沒有任何條目記錄這些。
            </p>
          </details>
          </div>
        </section>

        <section className="trust" aria-labelledby="f-trust">
          <h2 id="f-trust">什麼都不用註冊。</h2>
          <p>
            沒有帳號、不設 cookie、沒有廣告。你貼上的內容會送到語言模型供應商閱讀，本站不會儲存；API 只保存匿名的每日彙總，不含位址、也不含文字。
            <a href="/zh-hant/privacy/">隱私</a>
          </p>
        </section>
      </>
    ),
    stageLabels: (total) => ({
      parsing: "讀取你的論文",
      screening: total ? `篩選 ${total} 筆條目` : "篩選知識庫",
      synthesis: "撰寫你的推薦",
    }),
    stageState: { pending: "等待中", active: "進行中", done: "完成" },
    repoLink: "GitHub 原始碼",
    eyebrow: (
      <>
        這是一個開源 <strong>agent skill</strong> 的即時示範——在這裡回答你的東西，一行指令就能裝進你自己的 AI 工作階段，離開本頁及其限制也能照常運作。
      </>
    ),
    tagline:
      "貼上摘要或描述你的論文。免註冊、免安裝——它讀的是真正的 skill 所用的同一份開放知識庫，並為每個條目標示它是怎麼寫成的、有多少內容有證據。",
    paperLabel: "你的論文",
    paperPlaceholder:
      "例如：一項關於研究生如何選擇與使用書目管理工具的問卷研究，並附追蹤訪談。約 7,000 字，沒有開放近用費用的預算，並揭露使用 AI 輔助文字編修…",
    paperNote: (provider) => (
      <>
        你貼上的內容會送到語言模型供應商{provider ? `（目前為 ${provider}）` : ""}閱讀，本站不會儲存。請貼摘要，不要貼審查中的稿件。{" "}
        <a href={localePath("zh-Hant", "/privacy/")}>它會被怎麼處理</a>。
      </>
    ),
    working: "處理中…",
    findJournal: "找我的期刊",
    noscript: "推薦功能需要 JavaScript。知識庫本身是儲存庫裡的純 Markdown。",
    recommendationReady: "推薦已就緒",
    readHeading: "我從你的描述讀到的內容",
    topics: "主題：",
    methodology: "方法：",
    sensitive: "標記的敏感內容：",
    clarifyHeading: "先問幾個問題",
    clarifyAnswersLabel: "你的回答",
    clarifyPlaceholder: "例如：完全沒有預算；約 8,000 字；研討會也可以",
    clarifyAnswer: "回答並搜尋",
    clarifySkip: "略過——直接搜尋",
    candidatesHeading: (n) => `篩選後的前 ${n} 名候選`,
    disputedTag: "有爭議（Disputed）",
    evidencePct: (pct) => `證據 ${pct}%`,
    evidencePctTitle: "評分維度中有實際資料支撐的比例",
    tiedWith: (n) => `與 ${n} 個並列`,
    tiedTitle: (n) => `六個維度的分數與另外 ${n} 個候選完全相同，彼此的順序是任意的。`,
    disputedClaim: "有爭議的主張：",
    articles: (n) => `${n} 篇文章`,
    noTopicData: "這個條目目前沒有主題篇數資料。",
    recommendationHeading: "推薦",
    followupHeading: (left) => `追問${left > 0 ? `（剩 ${left} 次）` : "（已無剩餘）"}`,
    followupLabel: "你的追問",
    followupPlaceholder: "例如：為什麼不投 CHI？／第二志願需要改什麼？",
    ask: "送出",
    thinking: "思考中…",
    followupLimit: "這個示範最多追問兩次。請修改上方的描述並重新搜尋，以探索不同的角度。",
  },
};
