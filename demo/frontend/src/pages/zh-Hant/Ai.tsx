import { providerLabel, useCoverage, useHealth } from "../../api";
import { HumanEvidence } from "../../components/HumanEvidence";
import { VersionLine } from "../../components/VersionLine";
import { SITE } from "../../site";

/**
 * 繁體中文版 of pages/Ai.tsx, written section for section against it. The
 * English is the original; this carries the same claims and no stronger ones.
 * scripts/check-site.mjs fails the build if the two differ in sections, table
 * rows, list items or links, or if this page claims human verification.
 */
export default function Ai() {
  const coverage = useCoverage().data;
  const health = useHealth().data;
  const provider = providerLabel(health?.provider);

  return (
    <article className="prose">
      <h1>Journal Atlas 如何製作，哪些部分是 AI</h1>
      <p className="lede">
        這個專案有很大一部分由 AI 撰寫。本頁說明是哪些部分、示範目前由哪些模型運行、目前還沒有哪些條目記錄第一手報告，以及本專案不會宣稱什麼。
      </p>

      <section>
        <h2>目前還沒有條目記錄的事</h2>
        <p className="callout">
          {coverage
            ? coverage.human_evidence
              ? <HumanEvidence coverage={coverage} />
              : "本頁連線的 API 目前還沒有提供這項紀錄。在它提供之前，請理解為：沒有任何條目記錄了本站能顯示給你的第一手報告。"
            : "正在從 API 載入目前的紀錄。"}
        </p>
        <p>
          條目的 tier 說的是<em>它是怎麼寫成的</em>
          。它不是「某位熟悉該期刊的人已經檢查過」的判定，本站任何地方都不應被如此解讀。若有人投稿過或審查過某個場地，那就是缺少的那一層，補上的方式是貢獻（見
          <a href="/zh-hant/about/#contact">關於</a>）。
        </p>
      </section>

      <section>
        <h2>什麼是由什麼寫的</h2>
        <table className="plain-table">
          <caption className="sr-only">專案的各個部分、其依據，以及各自如何標示</caption>
          <thead>
            <tr>
              <th scope="col">部分</th>
              <th scope="col">依據</th>
              <th scope="col">標示方式</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">網站程式碼與版面</th>
              <td>由 Claude 模型在維護者的指示下撰寫。</td>
              <td>
                提交紀錄是公開的。每個 commit 都附有 <code>Co-Authored-By</code> trailer，標明確切的模型。
              </td>
            </tr>
            <tr>
              <th scope="row">
                AI 研究條目
                {coverage ? `（${coverage.tiers.ai}）` : ""}
              </th>
              <td>
                AI 模型針對公開來源（出版社政策頁、近期出版品、審稿時間彙整站）逐一研究每本期刊。沒有公開來源的欄位就留白。
              </td>
              <td>
                一則註記橫幅、每個欄位 0 到 5 的 <code>signal_quality</code> 分數，以及查證了哪些來源的清單。未記錄任何人工複核。
              </td>
            </tr>
            <tr>
              <th scope="row">
                估計值（Estimated）條目
                {coverage ? `（${coverage.tiers.tier2}）` : ""}
              </th>
              <td>家族層級的估計：把同一個主張調整後套用到一群相似的期刊。不是逐刊的證據。</td>
              <td>Soft Metadata 區段上的警告橫幅。</td>
            </tr>
            <tr>
              <th scope="row">
                有附來源（Sourced）條目
                {coverage ? `（${coverage.tiers.tier1}）` : ""}
              </th>
              <td>每項主張都引用來源：具體文章篇數、來源網址與日期。由 AI 研究，沒有人核對過。</td>
              <td>沒有橫幅。每項主張都附上它的證據。</td>
            </tr>
            <tr>
              <th scope="row">分數</th>
              <td>
                由一支腳本（<code>fit_score.py</code>）計算。不涉及任何模型。
              </td>
              <td>附上證據涵蓋率百分比；候選並列時另附說明。</td>
            </tr>
            <tr>
              <th scope="row">撰寫出來的推薦</th>
              <td>由語言模型在每次請求時，根據前幾名候選條目的摘錄重新撰寫。</td>
              <td>它顯示在它所依據的候選卡片之下，讓你可以對照檢查。</td>
            </tr>
          </tbody>
        </table>
        <p className="footnote">
          各 tier 的條目來源記錄在儲存庫的 <code>SEED_DATA_QUALITY.md</code>
          。除了該檔案所說的之外，本頁不對單一 Sourced 或 Estimated 條目是誰打字的做任何主張。
        </p>
      </section>

      <section>
        <h2>一次推薦是怎麼產生的</h2>
        <ol>
          <li>
            <strong>讀取你的描述。</strong>{" "}
            {health?.extraction_model ? (
              <>
                目前由 {provider} 的模型（<code>{health.extraction_model}</code>）把它轉成結構化屬性：主題、方法、字數、費用預算，以及你已說明和未說明的限制條件。
              </>
            ) : (
              <>語言模型把它轉成結構化屬性：主題、方法、字數、費用預算，以及你已說明和未說明的限制條件。</>
            )}{" "}
            你沒有說明的限制條件會列回給你，而不是被猜測。
          </li>
          <li>
            <strong>篩選。</strong>{" "}
            一支確定性的腳本依六個加權維度為每個條目評分。它不看條目的 tier 標章；它看六個維度中有幾個有資料支撐，把未知的維度排除而不是捏造中間值，在所知甚少時把分數拉向中性的 50，並把這個涵蓋率顯示在分數旁。
          </li>
          <li>
            <strong>撰寫。</strong>{" "}
            {health?.synthesis_model ? (
              <>
                目前由 {provider} 的模型（<code>{health.synthesis_model}</code>）讀取前幾名候選的條目並撰寫推薦。
              </>
            ) : (
              <>語言模型讀取前幾名候選的條目並撰寫推薦。</>
            )}{" "}
            它會拿到專案的使用契約（consumption contract），要求它在條目不是 Sourced 時註明該條目的 tier、在條目沒有說明時寫「條目未載明」而不是猜測，並且只引用它看過的條目。
          </li>
        </ol>
        <p className="footnote">模型可能在程式碼不變的情況下更換；上面的名稱是在你開啟本頁時從 API 讀取的。</p>
      </section>

      <section>
        <h2>本專案不會做的事</h2>
        <ul>
          <li>把 AI 研究或 Estimated 條目呈現為已驗證，或讓 tier 標章取代「有人檢查過」。</li>
          <li>用看似合理的值填補未知欄位。空白就維持空白，並顯示為空白。</li>
          <li>編造沒有任何來源提供的接受率、審稿時間或審稿人行為。</li>
          <li>隱藏爭議。被人正式提出異議的主張，無論在哪個 tier，都會帶有 Disputed 標記。</li>
          <li>假裝撰寫出來的推薦是模型輸出以外的東西。它是最難檢查的部分，這就是為什麼它所依據的卡片放在它的上方。</li>
        </ul>
      </section>

      <section>
        <h2>研究它</h2>
        <p>
          知識庫、評分腳本與各 tier 涵蓋率的量測，依 {SITE.license.content} 與 {SITE.license.code}{" "}
          公開，因此本頁的每一項陳述都能對照儲存庫檢查。
        </p>
        <VersionLine version={coverage?.version} />
      </section>
    </article>
  );
}
