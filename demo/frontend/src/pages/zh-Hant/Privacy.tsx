import { providerLabel, useHealth } from "../../api";
import { ISSUES_URL, SITE } from "../../site";

/** Bump with any change to what the site or API collects or who receives it. Same date as the English page. */
const EFFECTIVE = "2026-11-23";

/**
 * 繁體中文版 of pages/Privacy.tsx, written section for section against it. The
 * English is the original; this says the same things about what is kept and who
 * receives what, and no more reassuringly. scripts/check-site.mjs fails the
 * build if the two differ in sections, table rows, list items or links.
 */
export default function Privacy() {
  const health = useHealth().data;
  const provider = providerLabel(health?.provider);
  const limits = health?.limits;

  return (
    <article className="prose">
      <h1>隱私：你貼上的文字會怎麼處理</h1>
      <p className="lede">
        Journal Atlas 沒有帳號。它處理的唯一東西，是你輸入或貼上的論文描述，而這份描述會離開本站：它會被送到語言模型供應商供其閱讀。
      </p>
      <p className="footnote">生效日 {EFFECTIVE}。儲存庫的歷史紀錄就是本頁的變更紀錄。</p>

      <section>
        <h2>你貼上的文字</h2>
        <ul>
          <li>
            它從你的瀏覽器送到示範的 API，再由 API 送到語言模型供應商
            {provider ? `（目前為 ${provider}，依 API 回報）` : ""}
            。供應商閱讀它以擷取你論文的屬性；而為了撰寫推薦與任何追問，會再連同知識庫的摘錄收到一次。
          </li>
          <li>API 沒有資料庫，也不會把你的文字寫到任何地方。它只在請求進行的期間存在於記憶體中。</li>
          <li>
            供應商保留什麼、保留多久，由供應商自己的條款決定，不由本專案決定。在貼上任何你不會直接送給該供應商的內容之前，請先閱讀這些條款。
          </li>
          <li>
            請貼摘要或概述，不要貼審查中或受協議約束的稿件，也不要貼關於研究參與者的資料。示範基於成本會限制長度，而這個上限也是一種提醒。
          </li>
        </ul>
        <p>
          如果你希望沒有任何東西離開你自己的機器，skill 跑在你自己的 AI 工作階段裡、用你自己的金鑰，直接讀你的檔案；見
          <a href="/zh-hant/">首頁</a>的安裝說明。
        </p>
      </section>

      <section>
        <h2>API 保存什麼</h2>
        <ul>
          <li>
            為了執行上限，它會依訪客位址計算請求次數
            {limits
              ? `（每人每小時 ${limits.per_client_hourly_limit} 次、每天 ${limits.per_client_daily_limit} 次，所有人合計每天 ${limits.global_daily_limit} 次）`
              : ""}
            。位址只存在行程的記憶體中，行程重新啟動就消失。狀態頁只顯示總數，絕不顯示位址。
          </li>
          <li>
            它也保存匿名的每日彙總，讓維護者知道示範有沒有人用：跑了幾次搜尋、各次如何結束（完成、停下來問問題、沒找到、失敗、被拒絕、被放棄）、最佳符合期刊所在的領域，以及追問了幾次。這些彙總不含位址、不含你文字的任何部分、也不含識別碼；它們存在記憶體中，隨伺服器重新啟動歸零，並公開在
            <a href="/zh-hant/status/">狀態頁</a>。
          </li>
          <li>
            如果呼叫模型供應商失敗，錯誤會寫進伺服器日誌，讓維護者能修復。那是供應商的錯誤訊息，不是你的文字，但供應商可能回傳的每一種錯誤格式並未逐一稽核。
          </li>
          <li>
            站前面的網頁伺服器與 API 以網頁伺服器通常的方式處理請求，可能在自己的日誌中記錄位址、網址、時間與瀏覽器的 user-agent 字串。本專案沒有在這之上加任何分析腳本或追蹤；上述匿名彙總是它唯一做的計數。
          </li>
        </ul>
      </section>

      <section>
        <h2>在你的瀏覽器中</h2>
        <p>
          本站不設 cookie、不使用 local 或 session storage，也不載入分析、廣告或第三方的腳本、字型與圖片；若這一點不再成立，建置就會失敗。通往 GitHub 與其他地方的連結在你點擊之前不會做任何事，點擊之後則適用該網站自己的政策。
        </p>
      </section>

      <section>
        <h2>還有誰涉入</h2>
        <table className="plain-table">
          <caption className="sr-only">第三方及其處理的內容</caption>
          <thead>
            <tr>
              <th scope="col">對象</th>
              <th scope="col">處理的內容</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">Cloudflare</th>
              <td>提供本站的頁面，並看到對這些頁面的一般網頁請求。你貼上的文字直接送到 API 主機；API 的位址目前沒有經過 Cloudflare。</td>
            </tr>
            <tr>
              <th scope="row">API 主機</th>
              <td>由維護者營運的一台租用虛擬伺服器。它接收你貼上的文字，並轉交給下面的供應商。</td>
            </tr>
            {SITE.contact.email && (
              <tr>
                <th scope="row">專案信箱</th>
                <td>僅在你寫信給它時。這個位址會轉寄到維護者自己的信箱，所以你的位址與訊息會在那裡保存，直到維護者不再保留為止。本站本身不收集電子郵件位址。</td>
              </tr>
            )}
            <tr>
              <th scope="row">{provider ?? "模型供應商"}</th>
              <td>接收你貼上的文字，以及隨附的知識庫摘錄，以產生每一次回答。</td>
            </tr>
          </tbody>
        </table>
        <p className="footnote">這個表格會與供應商或主機的任何更動在同一次變更中一起修改。上面的供應商名稱是從 API 讀取的。</p>
      </section>

      <section>
        <h2>問題與請求</h2>
        <p>
          由於專案沒有儲存任何能識別你的東西，這一側沒有什麼可以查詢或刪除。其他事情請在 GitHub{" "}
          <a href={ISSUES_URL} target="_blank" rel="noreferrer">
            開一則 issue
          </a>
          ；請勿在其中放入私人資訊，因為 issue 是公開的。
          {SITE.contact.email && (
            <>
              若是私人的事，或你不用 GitHub，請寫信到 <a href={`mailto:${SITE.contact.email}`}>{SITE.contact.email}</a>。
            </>
          )}
        </p>
      </section>
    </article>
  );
}
