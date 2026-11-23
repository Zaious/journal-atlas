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

function absentList(lang: Lang, absent: string[], sep: string): string {
  return absent.map((a) => (lang === "zh-Hant" ? (ABSENT_ZH[a] ?? a) : a)).join(sep);
}

export type StageName = "parsing" | "screening" | "synthesis";
export type StageStatus = "pending" | "active" | "done";

interface NotesContext {
  coverage: Coverage | null;
  limits: Limits | null;
  /** The copyable install command block. */
  install: ReactNode;
}

export interface HomeText {
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
  // ---- notes under the tool ----
  notes: (ctx: NotesContext) => ReactNode;
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
    notes: ({ coverage, limits, install }) => {
      const absent = coverage?.absent ?? [];
      return (
        <>
          <section>
            <h2>This is an experiment, running on one person&apos;s API key</h2>
            <p>
              Journal Atlas is a research project, not a service. There is no company behind it and no uptime promise
              — the model calls this page makes are billed to the maintainer personally, which is the only reason it
              is capped
              {limits
                ? ` at ${limits.per_client_hourly_limit} searches an hour per person and ${limits.global_daily_limit} a day across everyone`
                : ""}
              . The cap is a budget, not a paywall: there is no tier that removes it, because there is nothing to
              sell.
            </p>
          </section>

          <section>
            <h2>Run it yourself, with no cap at all</h2>
            <p>
              The demo is a shop window. The real thing is a skill that runs inside your own Claude session, against
              your own key, over the same knowledge base — no limits, no queue, and it can read your actual
              manuscript instead of a pasted summary. In a Claude Code <strong>main session</strong>:
            </p>
            {install}
            <p className="footnote">
              Then restart Claude Code. Claude Desktop, ChatGPT and plain-git setups are covered in the{" "}
              <a href={`${SITE.repoUrl}#installation`} target="_blank" rel="noreferrer">
                installation guide
              </a>
              . The knowledge base is {SITE.license.content} — you can also just read it.
            </p>
          </section>

          <section>
            <h2>Your field is probably not in here</h2>
            <p>
              {coverage ? (
                <>
                  {corePercent(coverage)}% of the corpus is {coreLabel("en", coverage)}.
                  {absent.length > 0 && <> At zero: {absentList("en", absent, "; ")}.</>}
                </>
              ) : (
                <>
                  Most of the corpus sits in a few adjacent fields, and many fields have nothing at all. The
                  coverage note above lists which.
                </>
              )}{" "}
              Two things fix that, and neither requires touching code:
            </p>
            <ul>
              <li>
                <strong>Bring a whole field in.</strong> The AI-research expansion that added
                {coverage ? ` the ${coverage.tiers.ai}` : " the"} AI-researched entries was one run over a target
                list, and{" "}
                <a
                  href={`${SITE.repoUrl}/blob/main/docs/workorders/WO2_SOFT_METADATA_BATCH.md`}
                  target="_blank"
                  rel="noreferrer"
                >
                  the procedure is published
                </a>{" "}
                so you can point it at yours. Twenty journals is a real contribution.
              </li>
              <li>
                <strong>Tell us how it actually went.</strong> If you have submitted to or reviewed for a journal,
                you hold the part no amount of research reaches — whether the word limit is real, how the reviewer
                pool treats qualitative work, what a desk rejection there means. That is exactly what the
                AI-researched entries are missing, and no entry yet records it. Ten minutes on one journal you know
                well beats a hundred scraped ones.
              </li>
            </ul>
          </section>

          <section>
            <h2>And it needs more than one maintainer</h2>
            <p>
              Scholarly tools die a specific death: one person builds something genuinely useful, maintains it
              alone, and then their circumstances change — and the whole thing goes read-only, then stale, then
              wrong. Anyone who has watched a library or digital-humanities project go dark knows the pattern.
            </p>
            <p>
              The licence is a partial answer — {SITE.license.content} content and {SITE.license.code} code mean
              nobody can be locked out of a fork. But a fork nobody maintains is still dead. So if this turns out to
              be worth keeping, <strong>the thing it most needs is co-maintainers</strong>: people who will review
              contributions in their own field and correct entries about journals they know. Say so in an{" "}
              <a href={ISSUES_URL} target="_blank" rel="noreferrer">
                issue
              </a>{" "}
              and you will be taken up on it. <a href="/about/">Who made this, and why</a>.
            </p>
          </section>
        </>
      );
    },
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
      "e.g. A qualitative study using autoethnography to explore embodied cognition in collaborative design teams. ~9,000 words, no institutional funding for open access, discloses AI-assisted copyediting...",
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
    notes: ({ coverage, limits, install }) => {
      const absent = coverage?.absent ?? [];
      return (
        <>
          <section>
            <h2>這是一個實驗，跑在一個人的 API 金鑰上</h2>
            <p>
              Journal Atlas 是研究專案，不是服務。它背後沒有公司，也不承諾上線時間——本頁發出的模型呼叫都由維護者個人付費，這是它設有上限的唯一原因
              {limits ? `：每人每小時 ${limits.per_client_hourly_limit} 次搜尋，所有人合計每天 ${limits.global_daily_limit} 次` : ""}
              。上限是預算，不是付費牆：沒有任何方案能解除它，因為沒有任何東西在賣。
            </p>
          </section>

          <section>
            <h2>自己跑，完全沒有上限</h2>
            <p>
              示範只是櫥窗。真正的東西是一個 skill，跑在你自己的 Claude 工作階段裡、用你自己的金鑰、讀同一份知識庫——沒有限制、不用排隊，還能讀你真正的稿件，而不只是貼上的摘要。在 Claude Code 的<strong>主工作階段</strong>中：
            </p>
            {install}
            <p className="footnote">
              然後重新啟動 Claude Code。Claude Desktop、ChatGPT 與純 git 的設定方式見
              <a href={`${SITE.repoUrl}#installation`} target="_blank" rel="noreferrer">
                安裝指南
              </a>
              。知識庫採用 {SITE.license.content}——你也可以直接讀它。
            </p>
          </section>

          <section>
            <h2>你的領域很可能不在裡面</h2>
            <p>
              {coverage ? (
                <>
                  語料有 {corePercent(coverage)}% 是{coreLabel("zh-Hant", coverage)}。
                  {absent.length > 0 && <>數量為零：{absentList("zh-Hant", absent, "；")}。</>}
                </>
              ) : (
                <>語料大多集中在少數相鄰領域，許多領域完全沒有。上方的涵蓋說明列出是哪些。</>
              )}{" "}
              有兩件事可以改善這個狀況，而且都不必動程式碼：
            </p>
            <ul>
              <li>
                <strong>把整個領域帶進來。</strong>
                新增{coverage ? ` ${coverage.tiers.ai} 筆` : ""} AI 研究條目的那次 AI 研究擴充，是對一份目標清單跑一次完成的，而且
                <a
                  href={`${SITE.repoUrl}/blob/main/docs/workorders/WO2_SOFT_METADATA_BATCH.md`}
                  target="_blank"
                  rel="noreferrer"
                >
                  流程已經公開
                </a>
                ，你可以把它指向你的領域。二十本期刊就是實質的貢獻。
              </li>
              <li>
                <strong>告訴我們實際經過。</strong>
                如果你投稿過或審查過某本期刊，你握有再多研究也摸不到的部分——字數限制是不是真的、審稿人群體如何看待質性研究、在那裡被 desk reject 代表什麼。這正是 AI 研究條目所缺的，而且目前沒有任何條目記錄這些。在你熟悉的一本期刊上花十分鐘，勝過一百本爬來的。
              </li>
            </ul>
          </section>

          <section>
            <h2>而且它需要不只一位維護者</h2>
            <p>
              學術工具有一種特定的死法：一個人做出真正有用的東西，獨自維護，然後他的處境改變——整個東西先變成唯讀，再變過時，最後變錯。看過圖書館或數位人文專案走向沉寂的人都知道這個模式。
            </p>
            <p>
              授權是部分的答案——{SITE.license.content} 內容與 {SITE.license.code} 程式碼意味著沒有人會被擋在 fork 之外。但沒人維護的 fork 還是死的。所以如果這件事值得留下，
              <strong>它最需要的是共同維護者</strong>
              ：願意在自己的領域審閱貢獻、更正自己熟悉期刊條目的人。請在{" "}
              <a href={ISSUES_URL} target="_blank" rel="noreferrer">
                issue
              </a>{" "}
              中說一聲，你會被接納。<a href={localePath("zh-Hant", "/about/")}>誰做的，為什麼</a>。
            </p>
          </section>
        </>
      );
    },
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
      "例如：以自我民族誌探討協作設計團隊中具身認知的質性研究。約 9,000 字，沒有機構資助開放近用費用，並揭露使用 AI 輔助文字編修…",
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
