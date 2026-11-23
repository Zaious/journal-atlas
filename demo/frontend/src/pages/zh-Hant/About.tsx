import { useCoverage } from "../../api";
import { ISSUES_URL, SITE } from "../../site";

/**
 * 繁體中文版 of pages/About.tsx, written section for section against it. The
 * English is the original; this carries the same claims and the same links.
 * scripts/check-site.mjs fails the build if the two differ in sections, list
 * items or links.
 */
export default function About() {
  const coverage = useCoverage().data;

  return (
    <article className="prose">
      <h1>關於 Journal Atlas</h1>
      <p className="lede">
        Journal Atlas 是一個關於學術論文適合投往何處的開放知識庫，加上一個搜尋它的示範。知識庫才是產品；本站只是通往它的一扇窗。
      </p>

      <section>
        <h2>它是什麼，以及它不是什麼</h2>
        <p>
          每一本期刊或研討會就是 Git 儲存庫裡的一個 Markdown 檔。條目記載你查得到的事實（出版社、費用、審查模式、政策），以及你通常查不到的軟性中介資料（soft metadata）：審稿人群體期待什麼、該刊如何界定自己的範圍、容忍哪些主題。每個條目都標明它是怎麼寫成的、有多少內容有證據，而在沒有任何已知資訊之處，什麼都不會填。
        </p>
        <p>
          它不是排名，不是影響係數查詢，也不保證某本期刊會接受你的論文。在它說出一本看似合理、但其實所知甚少的期刊之前，它會先說「這個領域我沒有資料」。
        </p>
      </section>

      <section id="who">
        <h2>誰做的，為什麼</h2>
        <p>
          我是{" "}
          <a href={SITE.author.url} target="_blank" rel="noreferrer">
            {SITE.author.name} ({SITE.author.handle})
          </a>{" "}
          ——獨立 HCI 研究者與 AI agent 架構師。這個專案起於我自己的需求：我得決定把研究投到哪裡，而我希望這個決定建立在寫下來、可檢查的資訊上，而不是靠猜。
        </p>
        <p>
          當我接觸到 Open Journal Matcher（見下）時，我想把它的理念傳承下去，而不是從零開始：開放、免費使用，並且讓知識在任何一個人之後仍然留存。這個專案就是這次嘗試，以 AI agent 讀得懂的形式。
        </p>
        <p>
          這是{" "}
          <a href={SITE.studio.url} target="_blank" rel="noreferrer">
            {SITE.studio.name}
          </a>
          （{SITE.studio.nameZh}）的專案。AI 寫了多少、是哪些部分，在<a href="/zh-hant/ai/">它自己的頁面</a>。
        </p>
      </section>

      <section>
        <h2>接續 Open Journal Matcher 未竟之處</h2>
        <p>
          期刊推薦工具有二十年的脈絡，而其中多數已經關閉。本專案最受惠的一個是{" "}
          <a href="https://github.com/MarkEEaton/open-journal-matcher" target="_blank" rel="noreferrer">
            Mark E. Eaton 的 Open Journal Matcher
          </a>{" "}
          （CUNY，2020–2022）——免費、開放，把摘要與 DOAJ 比對。他在 2022 年 7 月把它下線，並寫道：
        </p>
        <blockquote>
          &quot;My hope is that someone will pick up where I left off.&quot;
          <cite>
            —{" "}
            <a
              href="https://kingsboroughlibtech.commons.gc.cuny.edu/2022/07/29/the-last-days-of-the-open-journal-matcher/"
              target="_blank"
              rel="noreferrer"
            >
              The last days of the Open Journal Matcher
            </a>
            , 2022
          </cite>
        </blockquote>
        <p>
          本專案是對這份邀請的一種回應。Eaton 也主張{" "}
          <a href="https://academicworks.cuny.edu/kb_pubs/261" target="_blank" rel="noreferrer">
            <em>pervious technology</em>
          </a>{" "}
          （可滲透的技術）——使用者能伸手進去調整、而不只是消費的工具。OJM 在程式碼層是可滲透的；本專案在<strong>資料</strong>
          層是可滲透的，而這個轉移就是全部的傳承：知識本身才是產品，而不是一個可以被關掉的服務。
          {coverage ? ` ${coverage.total} 個 Markdown 檔` : " Markdown 檔"}放在採用相同方式分享授權的 Git 儲存庫裡，不會因為某位維護者倦怠就被從你手中拿走——這正是 OJM 結束的方式。
        </p>
        <p>
          這也是為什麼我們要的是共同維護者，而不是使用者。一份比作者活得更久的語料，是唯一能夠呼應 Eaton 所指之事的版本；檔案留存是必要的、但並不充分。必須有人讓它們保持真實。
        </p>
      </section>

      <section id="contact">
        <h2>聯絡、更正與貢獻</h2>
        <p>
          更正與貢獻都透過 GitHub issue、公開進行，這樣一次更正也能幫到下一位讀者。
          {SITE.contact.email && "若你不使用 GitHub，請寫信到下方的專案信箱。"}
        </p>
        <ul>
          <li>
            <a href={ISSUES_URL} target="_blank" rel="noreferrer">
              回報錯誤的條目或 bug
            </a>{" "}
            ——請寫明期刊與領域。有爭議的主張依儲存庫治理文件中的流程處理，而不是靠在討論串裡爭辯。
          </li>
          <li>
            <a href={SITE.repoUrl} target="_blank" rel="noreferrer">
              貢獻一個條目或整個領域
            </a>{" "}
            ——見儲存庫中的貢獻指南。
          </li>
          <li>
            <a href={ISSUES_URL} target="_blank" rel="noreferrer">
              提議共同維護
            </a>{" "}
            ——本專案最需要的是願意審閱自己領域條目的人。
          </li>
        </ul>
        {SITE.contact.email && (
          <p>
            專案信箱：<a href={`mailto:${SITE.contact.email}`}>{SITE.contact.email}</a>
            。由維護者閱讀；不保證回覆，而且寄到那裡的訊息是私人的，不像 issue 是公開的。
          </p>
        )}
        <p>
          如果你想支持營運成本，有一個
          {SITE.supportUrl ? (
            <a href={SITE.supportUrl} target="_blank" rel="noreferrer">
              請我喝杯咖啡的連結
            </a>
          ) : (
            "支持連結"
          )}
          。它不解鎖任何東西：每個人用到的功能都一樣，示範的上限是預算，不是付費牆。
        </p>
      </section>

      <section>
        <h2>授權</h2>
        <p>
          知識庫採用{" "}
          <a href={SITE.license.contentUrl} target="_blank" rel="noreferrer">
            {SITE.license.content}
          </a>
          ；程式碼採用{" "}
          <a href={SITE.license.codeUrl} target="_blank" rel="noreferrer">
            {SITE.license.code}
          </a>
          。引用方式請依儲存庫的 <code>CITATION.cff</code>。
        </p>
      </section>
    </article>
  );
}
