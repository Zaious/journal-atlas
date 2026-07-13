# Existing-Entry Merge — Flagged Conflicts (Human Review Needed)

> Generated 2026-07-13 from the 112-file careful comparison merge (see GAPS_AND_NOTES.md).
> These are cases where the existing curated entry already had real content in an
> in-scope field, and the WO2 research draft found something different or additional.
> Per the "不粗填不覆蓋" instruction, none of these were auto-resolved — each needs a
> maintainer to read both sides and decide.

**Total: 193 conflicts across 98 journals.**

## ACM Interactions
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\acm-interactions.md`

- **Preprint Policy > Version of Record / Open Access > Model**
  - Existing: Version of Record: "Restricted unless ACM Open paid"; Open Access Model: "Hybrid (Subscription + ACM Open OA option)"
  - WO2 finding: WO2 positioning/preprint finding states: 'as of January 1, 2026 ACM converted its magazines (including Interactions) to open access, reducing the practical relevance of preprinting for this title.'
  - Why flagged: 這是與現有『VoR 需付費 ACM Open 才開放』及『Hybrid』模式直接矛盾的重大時效性發現（若屬實，2026年起 Interactions 已全面轉為 OA 雜誌）。Open Access 與 Metrics 之外的欄位屬 out-of-scope（Open Access 明列不可動），且此為過帳資訊而非嚴格 in-scope 的 Preprint 列本身內容矛盾，故不逕自覆寫，留待人工查證 ACM 官方公告後再決定是否更新 Preprint > Version of Record 與 Open Access 區塊。

---

## ACM Transactions on Computer-Human Interaction (TOCHI)
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\acm-transactions-on-computer-human-interaction.md`

- **Policies > Preprint Policy > Under review**
  - Existing: No updates (per ACM default)
  - WO2 finding: Authors are 'encouraged' (not required) to refrain from uploading during the TOCHI review period itself, but do not need to remove an existing arXiv version before submitting, and no preferential treatment is given either way (per ACM Policy on Authorship).
  - Why flagged: 既有表述聽起來像是審稿期間「不得更新」的硬性規定,但WO2引用的ACM政策原文顯示這只是「鼓勵」而非強制要求,對作者的實際指引有實質差異(硬性禁止 vs. 軟性建議),不是單純補充細節,故列為衝突交由人工判斷,不逕行覆蓋。

---

## ACM Transactions on Interactive Intelligent Systems (TiiS)
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\acm-transactions-on-interactive-intelligent-systems.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per ACM default — varies by journal)
  - WO2 finding: Double-anonymous peer review, effective starting July 1, 2025 (journal-specific policy change — TiiS moved from single- to double-anonymous review; author identity hidden from reviewers, though the handling associate editor knows it). Submissions must comply with anonymity requirements and authors are 'encouraged to refrain from' posting to arXiv/preprint servers during review.
  - Why flagged: 既有欄位已有具體內容（非空白佔位），且將雙盲審查定性為「ACM 預設值、因刊物而異」；WO2 則找到一則更具體、帶日期的期刊專屬變更（2025-07-01 起由單盲改為雙盲），性質上是矛盾/不同描述而非單純補充細節，且 WO2 來源本身標註為搜尋引擎快取片段（dl.acm.org 直接抓取被 403 擋下），可信度有限，故不直接覆蓋，留待人工核實。

- **Policies > Preprint Policy > Under review**
  - Existing: No updates (per ACM default)
  - WO2 finding: TiiS-specific guidance (tied to its double-anonymous review policy effective 2025-07-01) 'encourages authors to refrain from' posting submitted-version preprints to arXiv or other public forums during the active review period, to preserve reviewer anonymity/blinding.
  - Why flagged: 既有欄位已有內容，屬「ACM 預設」的概括描述；WO2 找到一則具體、有理由（維持雙盲）的期刊專屬指引，內容實質不同於既有的泛用描述，屬矛盾而非細節補充，且來源同樣依賴搜尋引擎快取（tiis.acm.org 直接抓取 403），建議人工核實後再決定是否更新。

- **Soft Metadata > Framing Requirements / Methodological Preferences (positioning finding)**
  - Existing: 既有 Framing Requirements 與 Methodological Preferences 章節內容（Tier 2 社群估計）
  - WO2 finding: WO2 positioning.accepts_now / framing_required / methods_welcome：強調論文須同時滿足 TiiS 官方定義的『Intelligence』與『Interaction』兩要件，並列出目前活躍的徵稿主題（如 healthcare conversational agents 特刊、knowledge-systematizing 特刊等）。
  - Why flagged: 此為主觀/定位類發現，依規則不得直接編輯 Soft Metadata 的主觀子章節；註記此為補充性研究發現供人工參考。附註：此份 WO2 內容其實已於 2026-07-13 由另一支自動化流程（scripts/spine/patch_existing_entries.py）以『AI-Research Notes (WO2 supplement)』區塊完整附加於檔案中，此處僅重申其存在，不代表需要對 Framing Requirements 本身做編輯。

---

## Archives of Clinical Neuropsychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\cognitive-science\archives-of-clinical-neuropsychology.md`

- **Policies > AI Policy > Explicit permission gate? / Leniency (1-5)**
  - Existing: Explicit permission gate?: No — disclosure-based; Leniency (1-5): 4
  - WO2 finding: gate: "conditional"（近乎事前許可門檻）; leniency_1_5: 2
  - Why flagged: 此欄位並非空白待填（已有完整、具體的政策描述），依規則不可覆蓋。但WO2對同一份OUP出版社層級AI政策的解讀與既有條目有實質分歧：既有版本判定為『僅揭露即可、無需事前許可、寬容度4』，WO2則判定為『近乎需要事前許可的條件式門檻、寬容度僅2』。兩者引用的來源網址相同（academic.oup.com AI政策頁），差異在於解讀角度，需人工覆核决定何者更準確，不應自動二選一覆蓋。

- **Soft Metadata > Framing Requirements（範圍外之主觀章節）**
  - Existing: Mandatory framing? Yes (strong) — Manuscripts must demonstrate clinical neuropsychology practice contribution（NAN-affiliated clinical, forensic, assessment-practice focus）
  - WO2 finding: positioning.framing_required: 近期一篇文章（ACN 38(7):1352, AI-Driven Diagnostics for Child Neuropsychology）顯示期刊願意刊登評估生成式AI於神經心理診斷角色之研究，但基調為『promising but insufficient』——歡迎AI輔助診斷/評估類投稿，但需採審慎、驗證式框架，而非鼓吹AI取代臨床判斷
  - Why flagged: Framing Requirements屬於本次任務明確排除、不可直接編輯的主觀章節。此為WO2針對『AI輔助診斷類投稿框架要求』的補充性定位發現，與既有『臨床實務貢獻框架』並不矛盾但屬不同細節層次，建議留給人工判斷是否要在Framing Requirements中補充『AI輔助診斷需審慎驗證框架』的細節。註：此發現內容已於檔案內 Soft Metadata > AI-Research Notes（WO2 supplement, 2026-07-13）區塊完整記錄，此處僅重複標記以提醒審閱者，不建議另行編輯正文章節。

---

## AI & Society
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\ai-and-society.md`

- **Policies > AI Policy > Leniency (1-5) 與 Explicit permission gate**
  - Existing: Leniency: 4；Explicit permission gate?: No — disclosure-based
  - WO2 finding: leniency_1_5: 3；gate: "conditional"
  - Why flagged: 現有 AI Policy 欄位已有具體實質內容（非佔位符），故依規則不可直接覆蓋編輯；但 WO2 對同一政策給出的寬容度數值（3）與 gate 描述（conditional）與現有值（4／disclosure-based=No）存在實質落差，非僅補充細節，建議人工複核何者較準確。註：此 WO2 原始文字其實已於檔案內 Soft Metadata > AI-Research Notes（WO2 supplement, 2026-07-13）區塊逐字引用為補充註記，此處僅是把該數值落差明確標記出來供覆核，而非新增內容。

---

## ACM Transactions on Accessible Computing (TACCESS)
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\acm-transactions-on-accessible-computing.md`

- **Policies > AI Policy (Explicit permission gate? / Summary)**
  - Existing: Explicit permission gate?: No — disclosure-based / Summary: "AI-assisted writing typically requires acknowledgment; AI listed as author prohibited; verify current policy at the journal's author guidelines."
  - WO2 finding: gate: conditional / summary: 使用 AI 撰寫文稿現已「不再要求揭露」;但若 AI 被用於研究執行本身(方法設計、資料生成、程式碼、分析、模擬等),則必須在方法章節詳述用途。AI 不得列為作者。source: https://www.acm.org/publications/policies/frequently-asked-questions
  - Why flagged: 此欄位已有具體內容(非佔位符),不可粗暴覆蓋,但兩者對「AI 撰寫文稿是否需揭露」方向相反:既有條目稱『通常需要揭露』,WO2 稱『現已不再要求揭露』(僅方法論使用需揭露)。可能既有條目referencing 較舊版政策(new-acm-policy-on-authorship 頁面)而 WO2 引用較新的 FAQ 頁面,需人工比對兩份 ACM 官方頁面何者為現行版本後決定是否更新。

- **Open Access > Model / APC (out of scope, flagged for awareness only)**
  - Existing: Model: Hybrid OA / APC (if OA chosen): ~$700-2,500 (ACM Open)
  - WO2 finding: WO2 preprint 欄位附帶提及:「ACM 自 2026-01-01 起全面轉為 Open Access 出版社」(source: https://www.acm.org/publications/policies/roles-and-responsibilities)
  - Why flagged: Open Access 屬本次任務明確排除的欄位,不提議直接編輯,但此為與既有 Hybrid OA 描述可能牴觸的重大新事實(若屬實,ACM 已全面轉全 OA,Hybrid OA 描述可能已過時),留供人工判斷是否需要另行更新 Open Access 區塊。

---

## Annual Review of Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\annual-review-of-psychology.md`

- **Policies > AI Policy (Leniency / Explicit permission gate)**
  - Existing: Leniency (1-5): 3; Explicit permission gate?: No — disclosure-based; Has journal-specific AI policy?: No (follows Annual Reviews publisher default)
  - WO2 finding: leniency_1_5: 2; gate: "conditional"; summary describes the same Annual Reviews publisher-wide policy (AI should not replace authors in first-draft generation but can be used to check completeness/readability; authors must check with their Production Editor) — WO2 itself notes this is publisher-level, not confirmed journal-specific
  - Why flagged: 既有表格已有具體內容（非佔位符），不可覆蓋；但 WO2 給出的 leniency 分數（2 vs 既有 3）與 gate 描述（'conditional' vs 'disclosure-based'）與既有評分不完全一致，屬於數值/描述上的實質分歧，需人工覆核何者更準確。註：此差異的敘事版本已於既有檔案 Soft Metadata > AI-Research Notes（WO2 supplement, 2026-07-13）段落中以補充說明方式呈現，但表格本身的 Leniency/Gate 數值尚未對齊，故仍列為衝突供覆核。

---

## ACM Transactions on Human-Robot Interaction (THRI)
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\acm-transactions-on-human-robot-interaction.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (typical journal default; check publisher policy)
  - WO2 finding: Double-anonymous (double-blind) peer review, standard 3 reviewers spanning disciplines; exception is conference-extension papers which are not double-anonymous (sourced from THRI's own author-guidelines page: https://dl.acm.org/journal/thri/author-guidelines)
  - Why flagged: 既有值是家族通則式推測(single-blind、且自行加註『check publisher policy』表示未經期刊本身驗證);WO2 則引用 THRI 自己的 author-guidelines 頁面,得出恰恰相反的結論(double-anonymous/雙盲,且有審稿人數與例外規則的具體細節)。這是實質矛盾而非單純補充細節,且該欄位已有具體內容,不符合 placeholder 條件,故不逕行覆蓋,留待人工以 THRI 官方 author-guidelines 頁面覆核。

- **Policies > Preprint Policy > Post-acceptance (AAM) row ("Embargo varies by publisher (0-12 months)")**
  - Existing: Post-acceptance (AAM) | Yes | Embargo varies by publisher (0-12 months)
  - WO2 finding: Allowed under ACM's general Publication Rights & Licensing Policy: authors retain unrestricted right to post pre-submission, submitted, and accepted versions to arXiv or other non-commercial repositories at any stage; no embargo; ACM asks authors to also post the DOI of the Version of Record alongside the preprint (source: https://www.acm.org/publications/policies/publication-rights-and-licensing-policy)
  - Why flagged: 既有表格已有具體內容(embargo 0-12 個月的範圍描述),非 placeholder。WO2 引用 ACM 官方 Publication Rights & Licensing Policy,明確指出『no embargo』,與既有『embargo 依出版商而異、最長 12 個月』的描述存在實質差異,可能是既有條目過時或引用了錯誤的通用政策版本,建議人工核對 ACM 現行政策文字後再決定是否修正。

- **Metrics > Review Cycle Time (all four rows, currently community-estimate placeholders)**
  - Existing: *(community estimate)* across all four Review Cycle Time rows
  - WO2 finding: experiential.review_time_months 為 null(WO2 明確找不到任何 SciRev/Reddit/中文論壇的第一手審稿週期數據);但 WO2 acceptance_note 提到 THRI author guidelines 載明:minor revision 須於 2 個月內回覆、major revision 須於 3 個月內回覆,且有 EIC 初審退件(desk-reject)機制存在(但無量化比例)。
  - Why flagged: 雖然 Review Cycle Time 四列目前確實是空白 placeholder,理論上可填,但 WO2 本身對這四個確切欄位(time to first decision / first review / acceptance total / publication)並無實質數據(review_time_months 為 null,desk_reject_pct 為 null),僅有『修訂稿回覆期限』這類流程政策敘述,語意上不等同於『首次決定時間』等既定欄位定義,若直接套入恐產生誤導。故不提出逕行填寫,僅作為補充線索留供人工判斷是否要在 Notes 中補一句流程說明。

- **Soft Metadata > Framing Requirements / Methodological Preferences (WO2 positioning finding)**
  - Existing: 既有內容為 Tier 2 家族通則推測(ACM HCI Transactions family conventions),尚未有 THRI 專屬的 accepts_now / methods_welcome 實證資料
  - WO2 finding: WO2 positioning.accepts_now 與 methods_welcome 皆未能完成系統性掃描(僅零星搜尋片段提及 trust assessment 系統性回顧、social norms、human-robot teaming survey、robotic vision for HRI collaboration 等主題,但 WO2 自陳信心不足,不足以做為 accepts_now 推論依據),methods_welcome 為空陣列。
  - Why flagged: 此為 Soft Metadata 主觀子章節範疇(超出本次可編輯欄位),且 WO2 自身信心與完整度都低(signal_quality 2/5,且明確聲明未完成系統性文獻掃描),不構成可直接採用的定位發現,僅供人工日後若要做 Tier 1 升級驗證時參考的線索,不建議自動套用。

---

## Alzheimer's & Dementia: The Journal of the Alzheimer's Association
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\alzheimers-and-dementia.md`

- **Soft Metadata > Framing Requirements / Best Suited For (positioning, out-of-scope subjective sections)**
  - Existing: Best Suited For 僅列出 AD/dementia 臨床研究、生物標記驗證、臨床試驗報告(CONSORT)、多學科AD研究(臨床+神經影像+生物標記);Framing Requirements 僅泛稱需符合該學會專科領域
  - WO2 finding: WO2 研究發現本刊為阿茲海默症協會官方旗艦刊,涵蓋 bench-to-bedside 全光譜:基礎科學/分子機轉、遺傳體學、影像/生物標記、臨床試驗、AI/數位健康應用於失智症研究(2023年起有一系列 AI in dementia 專題文章)、流行病學/預防、社會行為照護面向、系統性綜述;並強制要求每篇文章附150字以內'Research in Context'摘要段落作為框架要求
  - Why flagged: 此為 WO2 針對期刊定位/接受範圍的補充研究發現,觸及 Soft Metadata 之 Best Suited For 與 Framing Requirements 等主觀章節,依規則不得直接編輯,列為補充發現供人工複核是否需擴充『AI/數位健康應用』為新的 Best Suited For 條目,以及是否需在 Framing Requirements 加入'Research in Context'摘要格式要求。

---

## Cognitive Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\cognitive-science\cognitive-psychology.md`

- **Policies > AI Policy > Explicit permission gate? / Leniency**
  - Existing: Explicit permission gate: "No — disclosure-based for text; image generation prohibited"; Leniency (1-5): 3
  - WO2 finding: gate: "conditional"; leniency_1_5: 4
  - Why flagged: 既有內容已描述真實政策(揭露制、非強制許可關卡),非留白格,依規則不可覆蓋;但 WO2 判定為 gate="conditional"、寬鬆度 4,與既有的「No / 寬鬆度 3」在程度描述上有出入,屬於同一 in-scope 欄位的不同判讀,留供人工複核是否要調整寬鬆度評分或 gate 描述用語。

---

## Assessment
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\assessment.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (typical journal default; check publisher)
  - WO2 finding: double-anonymized (double-blind) — source: https://journals.sagepub.com/author-instructions/asm
  - Why flagged: 現有欄位已有具體內容(非佔位符,是家族通用推測值),但與 WO2 找到的審稿型態直接矛盾(單盲 vs 雙盲匿名),屬於實質分歧而非單純補充細節,需人工查證官方 author-instructions 頁面後再決定是否更正,不宜逕行覆蓋或自動判定何者為真。

- **Policies > Preprint Policy (Under review / Post-acceptance (AAM) 兩列)**
  - Existing: Under review: Yes - Most journals permit; Post-acceptance (AAM): Yes - Embargo varies by publisher (0-12 months)
  - WO2 finding: Allowed with conditions — 稿件可先掛在預印本伺服器,但一旦正式接受,作者需在該預印本頁面附上最終出版版本連結;投稿正文中應避免引用預印本(若引用之後有正式出版版本,需更新引用為正式版)。source: https://journals.sagepub.com/author-instructions/asm
  - Why flagged: 現有欄位內容為家族通用推測值,非嚴格定義的佔位符,故未逕行覆蓋;但 WO2 提供了直接來自期刊自身 author-instructions 頁面的具體條件(需回連正式出版版本、投稿正文應避免引用預印本),明顯比現有籠統敘述更精確且來源更直接,建議人工比對後決定是否據此升級為 Tier 1 並改寫此欄位。

---

## Cognition
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\cognitive-science\cognition.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (per Elsevier default — varies by journal; some are double-blind)
  - WO2 finding: Double-anonymized (double-blind) peer review; editors screen for suitability first, then typically send to a minimum of two independent expert reviewers (source: https://www.sciencedirect.com/journal/cognition/publish/guide-for-authors)
  - Why flagged: 既有值是根據 Elsevier 通用預設推測的（single-blind），WO2 則引用該刊自己的 guide-for-authors 頁面明確指出是 double-anonymized/double-blind——兩者是實質矛盾而非只是細節補充，需要人工查證 guide-for-authors 原文後才能定案，不應自動覆蓋。

- **Policies > Preprint Policy (supplementary detail, not contradictory)**
  - Existing: Pre-submission | Yes (Elsevier article sharing policy permits preprints)
  - WO2 finding: Cognition additionally offers a free preprint-posting service via SSRN: during submission authors can opt to have their manuscript posted publicly on SSRN as soon as it passes initial editorial screening (source: https://www.elsevier.com/about/policies-and-standards/sharing).
  - Why flagged: 此為補充性質的具體服務細節（SSRN 自動預印本張貼服務），與既有值不衝突，但既有儲存格已有實質內容（非 placeholder），依規則不應直接覆蓋填入；留給人工評估是否值得補述在 Notes 欄。

---

## Clinical Psychology Review
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\clinical-psychology-review.md`

- **Policies > AI Policy > Explicit permission gate?**
  - Existing: No — disclosure-based for text; image generation prohibited
  - WO2 finding: gate: "conditional" (WO2 structured field, same underlying source: Elsevier generative-AI writing policy page)
  - Why flagged: 既有欄位已有實質內容（非佔位符），依規則不可覆蓋；但 WO2 將 gate 分類標記為「conditional」而非「No」，與既有的「No」分類存在字面上的不一致（雖然兩者描述的底層政策內容——需揭露、圖像生成禁止——本身並不矛盾）。是否要統一分類用語，建議人工複核後再決定是否調整措辭。

---

## Behaviour & Information Technology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\behaviour-and-information-technology.md`

- **Policies > AI Policy > Explicit permission gate?**
  - Existing: No — disclosure-based
  - WO2 finding: conditional (gate: "conditional")
  - Why flagged: 既有欄位已有具體內容（非佔位符），依規則不可覆蓋；但 WO2 將 gate 標記為 conditional，與既有的「No — disclosure-based」用詞不同分類方式，可能只是同一政策的不同標籤法，也可能反映不同判讀，建議人工確認是否需調整措辭。

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 4 (disclosure-based; AI cannot be listed as author)
  - WO2 finding: 3
  - Why flagged: 兩者皆基於同一份 Taylor & Francis 集團 AI 政策（來源相同 URL），但既有評分為 4、WO2 評分為 3，屬於對同一政策寬嚴程度的不同主觀判斷，非單純補充細節，故列為衝突交人工複核，不逕行覆蓋。

- **Review Cycle Time > Time to first review / Time to acceptance (total)**
  - Existing: *(pending)* / *(pending)*
  - WO2 finding: muchong.com(小木虫) 單一投稿案例：初審約2個月，經reject & resubmit後總計約11個月獲接受(n=1)；fabiaoji.com 另兩則個案顯示拒稿約1-2個月
  - Why flagged: 資料僅來自單一或極少數匿名論壇個案(n=1~2)，WO2 自身亦註記「不足以代表整體」，未達到可直接視為『typical time』填入表格的可信度門檻，故不逕行填入，僅供人工參考是否要以個案/範圍形式謹慎補充。

---

## Computers and Composition
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\computers-and-compositioncomputers-and-composition.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (per Elsevier default — varies by journal; some are double-blind)
  - WO2 finding: Double-blind（投稿須為盲審，作者須自行移除稿件正文中所有可識別身分的資訊）— 來源：https://www.elsevier.com/journals/computers-and-composition/8755-4615/guide-for-authors
  - Why flagged: 現有欄位已有具體內容（非佔位符），但WO2從該刊自己的Guide for Authors頁面找到的資訊與現有內容直接矛盾——現有寫『單盲（Elsevier預設，因刊而異）』，WO2寫『雙盲，且明確要求作者自行移除稿件正文中可識別身分資訊』。這不是補充細節而是實質衝突，且WO2來源是期刊專屬頁面（比泛用的Elsevier預設更具體），故不逕行覆蓋，留待人工核實。

- **Policies > AI Policy > Leniency (1-5) 與 Explicit permission gate?**
  - Existing: Leniency: 3；Explicit permission gate?: No — disclosure-based for text; image generation prohibited
  - WO2 finding: Leniency: 2；gate: conditional（作者端條件式允許僅潤飾+需揭露，圖像生成與審稿端AI使用皆封閉）
  - Why flagged: AI Policy欄位已有完整、非佔位符的具體政策描述，依規則不得逕行編輯覆蓋。但WO2對同一份Elsevier政策給出不同的寬容度評分（2 vs 現有3）與略有差異的gate措辭（conditional vs No—disclosure-based），屬於對同一政策的不同評估角度，留供人工比對後決定是否調整評分。

---

## Computational Linguistics
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\cognitive-science\computational-linguistics.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per ACL default)
  - WO2 finding: Single-blind (NOT double-blind) — authors' names/affiliations are on the manuscript and known to editors and reviewers; reviewers' identities are not disclosed to authors. (source: https://cljournal.org/submissions.html)
  - Why flagged: 現有條目與 WO2 對審稿匿名制度的描述直接矛盾（雙盲 vs 單盲），且 WO2 引用的是期刊自己的投稿頁面，證據強度不低，需要人工查證 cljournal.org/submissions.html 後再決定是否修正，不宜自動覆蓋既有內容。

---

## Cognitive Science
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\cognitive-science\cognitive-science.md`

- **Review Cycle Time > Time to first decision**
  - Existing: *(fill manually)*
  - WO2 finding: 「總處理時間(至有決議稿件)約 4.7 個月」(SciRev 樣本, n=5)
  - Why flagged: WO2 只給了兩個時間點:「首輪審查約3.0個月」(已對應填入 Time to first review)與「總處理時間(至有決議稿件)約4.7個月」。後者的語意可能指「Time to first decision」(拿到任何決議的時間,含修訂輪次前的第一次決議)或「Time to acceptance (total)」(直到最終被接受為止的總時間,平均審查輪數1.7輪意味著可能歷經修訂),兩者定義不同且無法從原文明確判斷究竟對應哪一列,為避免誤植到錯誤欄位,留給人工判斷後再決定填入哪一列(或兩列都不填)。

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per Wiley default — varies by journal)
  - WO2 finding: double-anonymized (雙盲) peer review — 作者需自行匿名化稿件並另附 title page 檔案(來源:期刊本身 forauthors.html,非僅 Wiley 通用預設頁)
  - Why flagged: 此欄位並非佔位符(已有具體內容「Double-anonymized」),依規則不可覆蓋。但WO2找到的來源是本刊自己的 forauthors.html 頁面(而非泛用 Wiley 預設頁),等於把既有推測「per Wiley default — varies by journal」升級為期刊專屬確認證據,且補充了「作者需自行匿名化並另附 title page」這個實務細節。建議人工評估是否要把來源等級從 Tier 2 估計升級為 Tier 1(已驗證),但本次不直接編輯此欄位。

---

## Cognitive Therapy and Research
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\cognitive-therapy-and-research.md`

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 4
  - WO2 finding: 3
  - Why flagged: 既有內容並非佔位符（已有具體評分與完整 Summary），依規則不可覆蓋；但 WO2 獨立研究給出不同的寬容度評分（3 分而非 4 分），數值有實質差異，留待人工複核判斷哪個評分較準確。

- **Policies > AI Policy > Explicit permission gate?**
  - Existing: No — disclosure-based
  - WO2 finding: conditional
  - Why flagged: 既有內容描述為「無需許可,僅揭露」(No)，WO2 則歸類為「conditional（視情況而定）」——兩者可能只是同一政策的不同分類框架（文字潤色免揭露、其餘須揭露，可解讀為條件式），但分類標籤不同，既有欄位非佔位符，故不逕行覆蓋，建議人工確認何者較貼切。

- **Soft Metadata > Methodological Preferences / Framing Requirements (out of scope)**
  - Existing: 現有 Methodological Preferences 表未提及機器學習、複雜網路分析、迷幻藥治療機轉等新興方法；Framing Requirements 僅描述傳統 CBT 貢獻框架。
  - WO2 finding: positioning.accepts_now 提到近期編輯方向鼓勵複雜網路分析、機器學習、轉譯研究、迷幻藥治療機轉研究，並重視 dissemination 與跨文化面向。
  - Why flagged: 此為 WO2 定位性發現，觸及 Soft Metadata 主觀子章節（超出本次授權範圍），且該內容已以原文形式收錄於檔案既有的「AI-Research Notes (WO2 supplement)」區塊中，僅在此重申供人工評估是否要據此更新 Methodological Preferences / Framing Requirements 等主觀章節。

---

## College Composition and Communication
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\qualitative-methods\college-composition-and-communication.md`

- **Policies > AI Policy (Has journal-specific policy? / Summary / Source URL)**
  - Existing: Yes (publisher default + may have journal overlay); disclosure-based, no explicit permission gate; leniency 3-4; summary is generic family-norm language ("AI-assisted writing typically requires acknowledgment...verify current policy"); source URL points to a general CCCC position statement (postpandemicwriting).
  - WO2 finding: WO2 found a specific, named, dated policy: "CCC Generative AI Policy"(2025年10月採行),明訂作者可用GenAI「支援」而非「取代」學術勞動,須附不超過200字揭露聲明(工具、任務、人類作者比例),審稿人被明確禁止將手稿內容輸入GenAI平台。Source: https://cccc.ncte.org/cccc/ccc-generative-ai-policy/
  - Why flagged: 既有欄位已有實質內容(非裸佔位符),依規則不得直接覆蓋改寫,但WO2找到的是具體、有日期、有正式名稱的期刊專屬政策,遠比現有的通用/含糊措辭("may have journal overlay"、"verify current policy")精確,且來源網址也不同(現有連到postpandemicwriting立場聲明,WO2連到專屬AI政策頁)。非直接矛盾(結論方向一致:揭露制、非全面禁止),但建議人工核實後手動升級至Tier 1,並更新Source URL。

- **Review Cycle Time > Time to publication (after acceptance)**
  - Existing: *(typical: 2-6 weeks)*
  - WO2 finding: 目前無稿件積壓(no backlog),獲接受的稿件通常在接下來兩期內刊出。 (acceptance_note, signal_quality 3/5, source: https://cccc.ncte.org/cccc/ccc/write)
  - Why flagged: 既有值為家族通用估計(2-6週),WO2的說法是「接下來兩期內刊出」——若CCC為季刊或更低頻率,兩期的實際時間跨度可能遠超過2-6週,兩者在量級上可能實質矛盾,需人工查證期刊實際出刊頻率後再判斷是否更新。

---

## Counselling Psychology Quarterly
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\counselling-psychology-quarterly.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (typical journal default; check publisher)
  - WO2 finding: Double-anonymized (double-blind) peer review; initial editor appraisal, then review by independent anonymous expert referees, via ScholarOne Manuscripts. Source: https://www.tandfonline.com/journals/ccpq20/about-this-journal
  - Why flagged: 既有值為 family-norm 推測(single-blind),WO2 從期刊官方 about-this-journal 頁面查得的是 double-anonymized(double-blind)。兩者直接矛盾,需人工核實後決定是否更新,不應由本次 patch 直接覆蓋。

- **Review Cycle Time > Time to publication (after acceptance)**
  - Existing: *(typical: 2-6 weeks)*
  - WO2 finding: ~8 days (T&F official: avg. acceptance-to-online-publication, per https://www.tandfonline.com/journals/ccpq20/about-this-journal)
  - Why flagged: 既有欄位已有具體內容(非空白/佔位符),而 WO2 提供的官方數字(8天)與既有的『2-6週』估計有實質落差,屬矛盾而非單純補充細節,依規則應留待人工判斷,不逕行覆蓋。

- **Soft Metadata > Framing Requirements / Epistemological & Political Leanings (超出範圍,僅供人工參考)**
  - Existing: 既有 Tier 2 內容偏向泛用 family-norm 描述(如 cross-cultural friendliness: Medium,無特別提及去殖民化/批判取向)
  - WO2 finding: WO2 positioning finding(signal_quality 4/5)指出近期(2025下半-2026)CPQ 明顯歡迎去殖民化(decolonizing)、文化回應督導、社會正義/多元文化批判框架之投稿,Vol 39 Issue 1(2026)甚至為『Decolonizing Counselling Psychology』專題特輯
  - Why flagged: 此為 Soft Metadata 主觀分節(Epistemological & Political Leanings / Framing Requirements),依規則屬 out-of-scope,不可直接編輯,僅記錄供人工日後評估是否應調整 Tier 2 假設或升級為 Tier 1。

---

## Cultural Studies Critical Methodologies
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\qualitative-methods\cultural-studies-critical-methodologies.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per Sage default)
  - WO2 finding: Open peer review(依多方搜尋結果一致指出為 open-peer reviewed research articles,但未直接抓取官方頁面逐字確認,信度中等)
  - Why flagged: 既有欄位已有具體內容(雙盲匿名),非空白/佔位符,不應覆蓋;但 WO2 的獨立研究結論(開放式同行評審)與現有記載直接矛盾(雙盲 vs 開放),屬於實質分歧而非僅補充細節,需人工查證 Sage/CSC 官方頁面以確認何者正確,不可自動擇一採用。

- **Subject Density / Soft Metadata(近期收稿主題傾向)**
  - Existing: 現有 Subject Density > Top Topics 與 Soft Metadata > Epistemological & Political Leanings、Methodological Preferences 已描述後人類倫理、批判種族理論、去殖民/原住民知識論、自我民族誌等傾向(2022-2025 OpenAlex 主題分析)
  - WO2 finding: WO2 positioning.accepts_now 指出 2023-2025 實際刊出主題進一步集中於:黑人研究方法論與民族誌、黑人女性主義與嘻哈方法論、黑人男性氣質與運動員心理健康、去殖民化知識分享與正義路徑、兒童期批判質性探究、非人類感官/氛圍研究;並具體指出 2025 年兩期為 Special Issue(Vol 25 Iss 1『Childhoods, Cultures, and Critical Qualitative Inquiry』、Vol 25 Iss 3『Paths to Justice』)
  - Why flagged: 此為 Soft Metadata / Subject Density 範疇的定位性發現,依規則屬 out-of-scope 主觀子節,不應直接編輯;但內容具體且來源明確(signal_quality 4/5),值得人工評估是否納入 Top Topics 或 Epistemological Leanings 更新,故列為補充發現供複核而非直接改稿。

- **Soft Metadata > Reviewer Pool / Strategic Notes(投稿者第一手經驗)**
  - Existing: 現有 Reviewer Pool Characteristics 描述審稿人偏好與知識傳統(未含具體案例軼事);Metrics 的審稿週期/桌拒率欄位仍為 (pending)
  - WO2 finding: WO2 experiential 僅查得萬維學術(wanweixueshu.com)2-3 則零星留言:一則『一天內桌拒』案例、一則提及該刊使用腳注引註格式(非常見期刊格式)、一則回報獲得接受;signal_quality 僅 1/5,WO2 本身明確表示樣本數過少無法換算平均審稿時間或桌拒率,review_time_months 與 desk_reject_pct 均為 null
  - Why flagged: 此為 Practical Concerns / Strategic Notes 範疇的軼事型補充發現,樣本數極低(僅 2-3 則留言)且 WO2 已自陳不足以支撐任何量化欄位填補,不建議直接引用為結論;僅供人工參考,是否值得在 Practical Concerns 加註一句「已知有投稿者回報極快桌拒案例」由人工決定。

---

## Contemporary Educational Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\contemporary-educational-psychology.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (per Elsevier default — varies by journal; some are double-blind)
  - WO2 finding: double-anonymized (double-blind), per third-party aggregator (LetPub/scispace-derived search summary); journal's own guide-for-authors page returned HTTP 403, not independently confirmed
  - Why flagged: 現有值與 WO2 對本期刊實際審稿型態的判斷方向相反（單盲 vs 雙盲），且雙方都非一手來源確認（現有為 Elsevier 預設推論、WO2 為第三方聚合網頁摘要且原始頁面 403），屬於實質分歧而非單純補充細節，需人工查證後再定奪，不應直接覆蓋。

- **Soft Metadata > Framing Requirements（超出本次授權範圍的主觀子章節）**
  - Existing: Mandatory framing? Yes (soft) — Manuscripts must demonstrate contemporary educational psychology contribution
  - WO2 finding: positioning.framing_required: 期刊明確偏好嚴謹的質性/量化/混合方法實證研究，樣本需具代表性、置於真實教學情境中；純理論或非實證投稿不受鼓勵
  - Why flagged: WO2 提供了更具體的『偏好實證研究、不鼓勵純理論投稿』定位資訊，可能對 Framing Requirements 或 Methodological Preferences 這類主觀章節有參考價值，但這些章節在本次任務範圍之外，故僅列為衝突／補充發現供人工評估是否納入，不做直接編輯。

---

## Consciousness and Cognition
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\cognitive-science\consciousness-and-cognition.md`

- **Metrics > Review Cycle Time (四列：Time to first decision / Time to first review / Time to acceptance total / Time to publication)**
  - Existing: 全數為 *(fill manually)* 佔位符
  - WO2 finding: experiential.review_time_months: "SciRev aggregate (based on only 3 submitted reviews total, small sample): average total handling time ~1.7-1.9 months; average review time (first round) ~1.7-1.9 months (the two SciRev-derived pulls in this session gave slightly inconsistent 1.7/1.9 labeling for handling vs review time, both from the same page — treat as approximate, not precise); average first review round ~10.9 weeks per one query; average 1.7 review rounds; average ~2.0 reports per round." Sources: https://scirev.org/journal/consciousness-and-cognition/ , https://scirev.org/reviews/consciousness-and-cognition/
  - Why flagged: 雖然四列目前確實是空白佔位符（技術上符合可填補標準），但 WO2 自己承認這組數據存在內部矛盾：「首輪審稿時間」在同一頁面上出現兩個不同數字（1.7-1.9 個月 vs 10.9 週 ≈ 2.5 個月，落差約 30-45%），且樣本數僅 n=3（SciRev 極小樣本），WO2 亦自陳「treat as approximate, not precise」。若逕行選定其中一個數字填入特定列（例如武斷地把 1.7-1.9 個月填進「Time to acceptance total」、或把兩個互相矛盾的數字挑一個填進「Time to first review」），將構成對不確定/矛盾原始數據的粗暴精確化，與「不粗填」原則牴觸。故不提出直接編輯，改列為衝突，留待人工判斷是否要以極低信心度標註方式收錄、或等待更可靠來源。

---

## Computers in Human Behavior
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\computers-in-human-behavior.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (per Elsevier default — verify)
  - WO2 finding: Double-anonymized（雙盲）review — 編輯初審適合度，通過後送至少兩位獨立審稿人；編輯做最終決定。(source: elsevier.com/journals/computers-in-human-behavior guide-for-authors)
  - Why flagged: 既有值本身標註「per Elsevier default — verify」，即未經查證的預設猜測；WO2 引用該刊 guide-for-authors 頁面得出雙盲結論，兩者審稿類型直接矛盾（單盲 vs 雙盲），屬實質衝突而非細節補充，需人工查證何者正確，不逕行覆蓋。

- **Metrics > Review Cycle Time > Time to acceptance (total)**
  - Existing: *(pending — Elsevier typical 4-6 months)*
  - WO2 finding: SciRev（n=6，極小樣本）：整體處理時間（含接受案）平均 7.3 個月
  - Why flagged: 既有欄位雖標 pending 但已附帶具體猜測值（4-6個月），依規則不算裸 placeholder，故不可逕行填補；WO2 另有該刊專屬但樣本極小（n=6）的實測值 7.3 個月，與既有猜測範圍有實質落差，列為衝突待人工判斷。

---

## Collabra: Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\collabra-psychology.md`

- **Metrics > Review Cycle Time (全四列:first decision / first review / acceptance total / publication)**
  - Existing: 四列皆為 *(pending)*(publication 列的 Notes 已有 'OA — typically rapid post-acceptance')
  - WO2 finding: SciRev 自報(n=1,2016):首輪審查 ~2.3 週、總處理 ~4.3 週。中文期刊聚合站(非第一手)轉述期刊自報『平均約 16 週(約4個月)出版』。
  - Why flagged: WO2 自己在 blanks 欄位中已將 'experiential.review_time_months(第一手)' 列為未能可靠回答的項目(樣本僅 1 筆且非第一手),不宜逕行當作正式數值填入 Review Cycle Time 表格;是否要以高度加註警語的方式納入,建議由人工判斷。

- **Soft Metadata > Framing Requirements(對照 WO2 positioning.framing_required)**
  - Existing: Manuscripts must align with open-science values — preregistration, data/code sharing, replicability claims, or methodological transparency. The "Methodology and Research Practice" section is the entry point for non-traditional methods.
  - WO2 finding: 以「方法嚴謹性(soundness/rigor)」而非新穎性或影響力為評審核心;強調透明、開放資料與程式碼(期望分享 data 與 code)。稿件宜凸顯方法透明度與可重現性,不需主張突破性創新即可送審。
  - Why flagged: WO2 補充了『審稿核心是方法嚴謹性而非新穎性/影響力,不需主張突破性創新』這個可操作的定位細節,與現有描述不衝突但更具體;此欄屬 Soft Metadata 主觀性子區塊,依規則僅記錄供人工參考,不逕行編輯正文。

---

## Culture & Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\culture-and-psychology.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per Sage default)
  - WO2 finding: 公開審查(open review)——編輯部尋求至少兩位審稿人評估科學內容與呈現方式；作者與審稿人皆可要求維持匿名(非強制單盲或雙盲)
  - Why flagged: 現有條目寫「雙盲(default)」，WO2 查到的來源(author-instructions/cap)卻描述為「開放式審查、非強制單盲/雙盲」，屬實質矛盾而非補充細節，需人工回查 SAGE 該刊投稿須知頁面確認何者為準確版本，不應由本次比對逕自覆蓋。

- **Policies > AI Policy > Leniency / Explicit permission gate**
  - Existing: Leniency 4 (disclosure-based, no editor pre-approval gate); Explicit permission gate: No — disclosure-based
  - WO2 finding: leniency_1_5: 3; gate: conditional
  - Why flagged: 兩者皆引用同一 SAGE 平台層級 AI 政策來源，但對「寬容度評分」與「是否為條件式閘門」的判讀不同(4 分/無閘門 vs 3 分/conditional)，屬評分判斷差異而非新事實，且既有內容已非空白佔位，故不逕自修改，留供人工複核何者評分較貼近原始政策文字。

- **Soft Metadata > Framing Requirements / Methodological Preferences (超出範圍，僅供參考)**
  - Existing: Mandatory framing? Yes — cultural framing mandatory; Methodological Preferences 表列量化實驗接受度 2/5
  - WO2 finding: positioning.framing_required: 官方 Aims & Scope 明文要求，若納入實證證據須服務理論推進，且因心理現象本質為質性，實證證據被期待採用質性方法——純量化實證研究若缺乏理論建構貢獻則不符定位
  - Why flagged: 此為 WO2 針對主觀/定位類欄位(Framing Requirements、Methodological Preferences)的補充發現，依規則此類欄位不在本次可編輯範圍內，僅作為人工複核的補充參考，不建議直接編輯既有文字。

---

## Design Issues
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\design-issues.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per MIT Press default — varies by journal)
  - WO2 finding: Public submission guidelines only describe an editor/board-mediated confidential three-stage process (new submission → reviewer feedback → revised manuscript, monthly Editorial Board meetings); do NOT explicitly state single-blind vs double-blind vs open identity disclosure. WO2 explicitly lists 'peer_review.type (blind status)' as unconfirmed.
  - Why flagged: 現有欄位已有具體內容(非佔位符),按規則不可覆蓋,但 WO2 獨立研究找不到任何公開來源證實「雙盲」這個具體說法,建議人工重新查證 Design Issues 是否真的採雙盲審稿,或現有斷言的來源為何。

- **Policies > AI Policy (Explicit permission gate / Leniency)**
  - Existing: Explicit permission gate? No — disclosure-based; Leniency (1-5): 4
  - WO2 finding: gate: "conditional"; leniency_1_5: 3 — 依 MIT Press 出版社層級通用政策(揭露即可,非全面禁止),同一來源 direct.mit.edu/desi/pages/submission-guidelines 與 direct.mit.edu/journals/pages/publication-ethics
  - Why flagged: 既有欄位已有具體內容,定性描述(disclosure-based ≈ conditional)大致一致,但寬鬆度評分不同(4 vs 3),屬於同一政策的細微評分差異而非硬性矛盾,留給人工判斷是否需微調;另注意此 WO2 內容已於 2026-07-13 以「AI-Research Notes (WO2 supplement)」補充說明的形式併入本檔案 Soft Metadata 區塊(未覆蓋既有 Tier 評估),故本次審閱視為既有補充的重複確認,非新發現。

---

## Developmental Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\developmental-psychology.md`

- **Metrics > Acceptance Rate**
  - Existing: *(fill manually if known)*（空白佔位）
  - WO2 finding: WO2 acceptance_note：三個互相矛盾的歷史數字（2013年拒絕率~80%／2019年APA官方年度統計拒絕率~72%〔711投稿195接受〕／網路來源聲稱32%接受率但無官方出處），且WO2自身明言「不採信單一數字」，未找到2024-2026年官方營運報告可核實
  - Why flagged: 雖然此欄位目前是空白佔位符，理論上符合可填條件，但WO2提供的三筆數字互相矛盾且WO2本身已聲明不採信任一數字，若強行選一個填入會構成武斷覆蓋且可能誤導使用者；建議留給人工查證APA最新年度Summary Report of Journal Operations後再填，暫不提出變更

- **Review Cycle Time > Time to first review**
  - Existing: *(fill manually)*（空白佔位）
  - WO2 finding: WO2 experiential.review_time_months：SciRev僅1筆使用者回報首輪審稿21.7週（約5.0個月），WO2自身將此欄位列在"blanks"（無法找到可信證據）清單中，明言樣本量過小不足以代表期刊平均
  - Why flagged: 此欄位為空白佔位符，但WO2的唯一數據來源是n=1的單一審稿人回報，且WO2自己的signal_quality評為2/5並主動將此列為未解決的空白項；填入單一觀察值會呈現過度確定的假象，不符合保守合併原則，建議暫不填入，留待更多一手資料

---

## Design Studies
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\design-studies.md`

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 3
  - WO2 finding: 4 (signal_quality 2/5, explicitly noted as inherited publisher-default, not journal-verified)
  - Why flagged: 既有 AI Policy 欄位已有具體實質內容（非佔位符），非可直接覆蓋對象；但寬容度數值本身與 WO2 不同（3 vs 4），屬於實質分歧而非單純補充細節，需人工比對 Elsevier 政策原文後判斷是否調整。

- **Policies > AI Policy > Explicit permission gate?**
  - Existing: No — disclosure-based for text; image generation prohibited
  - WO2 finding: conditional
  - Why flagged: 對 gate 類型的定性描述不同（既有版本明確區分文字揭露制 vs 圖像禁止；WO2 僅籠統標為 conditional），且既有欄位已有實質內容，依規則不可覆寫，僅記錄供人工核對。

- **Metrics > Review Cycle Time（全部四列，目前均為 *(fill manually)* 佔位符）**
  - Existing: *(fill manually)* (all four rows)
  - WO2 finding: SciRev(n=3): first review ~4.6 months, total handling ~5.9 months, immediate-rejection ~40 days, ~2.0 rounds；LetPub: first review ~5.7 weeks, overall ~7.3 weeks, online pub ~9.5 weeks
  - Why flagged: 雖然這些列目前是空白/佔位符（技術上符合可填條件），但 WO2 自身兩個來源數字互相矛盾且差距近 4 倍（月 vs 週），WO2 標註 signal_quality 僅 2/5、樣本量小（SciRev n=3）、方法論不明，且 WO2 報告文字本身承認『materially disagree』。強行選一個數字填入會構成粗暴填入而非可信資料，故不填，留待人工查證後決定採用何值或是否標註為多來源分歧估計。

- **Metrics > Acceptance Rate**
  - Existing: *(fill manually if known)*
  - WO2 finding: LetPub 定性描述『较易』(relatively easy)，無具體百分比，且 LetPub 為代寫/編輯服務商業網站，WO2 自評為低可信度
  - Why flagged: WO2 對此欄位並未提供實際比率數字，只有一句未量化、來源可信度存疑的定性描述，不構成『real, sourced answer』門檻，且此發現已完整呈現於既有檔案的 AI-Research Notes 補充區塊中，故不重複填入 Metrics 表格，留待人工判斷是否有更可靠來源。

---

## Computer Supported Cooperative Work (CSCW)
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\computer-supported-cooperative-work-cscw.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per Springer default — varies by journal)
  - WO2 finding: Single-blind. Search-engine synthesis of the journal's submission guidelines states manuscripts are reviewed by 3 referees plus 1 Associate Editor; no article accepted without 3 complete reviews. (Direct page fetch blocked by Springer login wall — medium confidence.)
  - Why flagged: 既有內容基於「Springer 預設、依期刊而異」的假設性推測；WO2 則找到具體的單盲＋3位審稿人＋1位副編輯的審稿結構描述，兩者對「雙盲 vs 單盲」的定性直接矛盾。但 WO2 自身也承認此資訊僅來自搜尋引擎快取／摘要，未能直接讀取 Springer 官方頁面（登入牆阻擋），信心中等，需人工查證期刊官方 submission guidelines 頁面後才能定案，不宜逕行覆蓋。

- **Policies > AI Policy (Explicit permission gate? / Leniency)**
  - Existing: Explicit permission gate? No — disclosure-based; Leniency (1-5): 4
  - WO2 finding: gate: "conditional"; leniency_1_5: 3
  - Why flagged: 既有 AI Policy 區塊已有實質內容（非佔位符），依規則不可直接編輯；但 WO2 對同一份 Springer Nature 政策給出略為不同的分類（「條件式」 vs 「無明確許可關卡、僅需揭露」）與較低的寬容度評分（3 vs 4），屬於同一來源資訊的詮釋落差，非新事實，僅供人工校準參考，不建議自動覆蓋。

- **Soft Metadata > Framing Requirements (out of scope, supplementary)**
  - Existing: Manuscripts must demonstrate CSCW contribution — cooperative / collaborative work / technology mediating group interaction. CSCW tradition very accommodating of ethnographic / qualitative methods.
  - WO2 finding: Aims & scope explicitly favors work grounded in real cooperative-work practice: (1) ethnographic/in-depth fieldwork of work practices with technological implications; (2) empirical evaluations of existing or novel technical solutions under real-world conditions; (3) technical or conceptual frameworks for practice-oriented computing research built on prior fieldwork/evaluations. Purely abstract/algorithmic CSCW-adjacent papers without practice/fieldwork grounding appear to be a scope mismatch. (signal quality 2/5, source reached only via search-engine cache, login wall blocked direct verification)
  - Why flagged: 此為 Soft Metadata 主觀章節（Framing Requirements），依規則超出本次可編輯範圍；WO2 的發現提供了更具體的「田野調查／實務落地」框架要求細節，可作為未來人工升級 Tier 2→Tier 1 時的補充參考，故僅記錄於此供人工複核，不提出直接編輯。

---

## Dementia and Geriatric Cognitive Disorders
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\dementia-and-geriatric-cognitive-disorders.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind or double-blind (per Karger default — varies)
  - WO2 finding: single-anonymous（單盲）：審稿人知道作者姓名，作者不知道審稿人身份。除社論及部分通訊外，所有文章皆送外部審查，通常至少2位該領域專家審查。本刊為 Neuroscience Peer Review Consortium (NPRC) 會員，可依作者要求快速轉送審稿意見至其他NPRC會員期刊。(source: https://karger.com/dem/pages/guidelines)
  - Why flagged: 既有欄位已有具體內容（非空白佔位符），依規則不可直接覆寫；但WO2提供了更明確且有來源頁面佐證的說法（明確為single-anonymous單盲，而非「varies」的模糊表述），並補充NPRC會員快速轉審機制這項既有內容完全沒有的細節。是否要用更具體的說法取代目前的「varies」措辭，建議留給人工判斷，而非自動覆蓋。

- **Metrics > Acceptance Rate / Desk Rejection Rate; Review Cycle Time（四列）**
  - Existing: *(fill manually if known)* / *(fill manually)*（皆為空白佔位符）
  - WO2 finding: 無官方量化數據。僅有中文鏡像站（iikx.com/klxksci.com）標註的「網友分享經驗」：錄取率約50%、平均審稿時間約2個月；medsci.cn論壇有單一2020年個案（5天內未覓得審稿人、2/24遭拒）。WO2 signal_quality僅2/5，且WO2自身研究筆記已明確聲明「不作為可信量化事實填入」「未強行換算成統計數字」。
  - Why flagged: 這些欄位目前確實是空白佔位符（技術上可填），但WO2找到的唯一數據是未經官方或多方交叉驗證的網友估計值，WO2自己的分析也主動排除將其當作可信量化事實。基於「不粗填」原則，選擇不將此類低信度、單一來源的網友傳言直接填入正式Metrics/Review Cycle Time表格，僅在此標記供人工評估是否有價值以其他方式（如加註來源與信度警語）呈現。

---

## Environment and Behavior
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\environment-and-behavior.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (typical journal default; check publisher)
  - WO2 finding: double-anonymized (雙向匿名審查)，來源：https://journals.sagepub.com/author-instructions/eab
  - Why flagged: 現有值為心理學家族範本套用的通用猜測（非該刊專屬確認），WO2 則引用該刊官方 author-instructions 頁面得出具體且相反的結論（雙向匿名 vs. 現有猜測的單盲）。因現有欄位並非嚴格定義下的《空白/佔位符》（有實質內容，即使是猜測性質），且兩者為實質矛盾而非單純補充細節，故不直接覆蓋，列為衝突交由人工核實 EAB 官方投稿頁面後裁定。

---

## Educational Psychology Review
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\educational-psychology-review.md`

- **Policies > AI Policy > Explicit permission gate? / Leniency (1-5)**
  - Existing: Explicit permission gate? No — disclosure-based ; Leniency (1-5): 4
  - WO2 finding: gate: "conditional"（有條件揭露）; leniency_1_5: 3
  - Why flagged: WO2 將此政策標記為 conditional,而現有檔案標記為「No — disclosure-based」;雖然 WO2 自身文字說明其底層機制與現有描述相同(無需事前許可、屬事後揭露制),但標籤詞彙(conditional vs No)與寬容度評分(3 vs 4)不一致,屬於同一維度的具體數值/標籤分歧,建議人工核實後統一,而非自動判定何者正確。

- **Policies > Preprint Policy > Post-acceptance (AAM) embargo**
  - Existing: Yes | Embargo: 12 months
  - WO2 finding: 可在正式出版後至少 6 個月上傳作者接受版(accepted version)——依 Springer Nature 通用政策外推,非該刊逐字聲明,信心中等 (source: https://communities.springernature.com/posts/citing-a-preprint-a-guide-researchers)
  - Why flagged: AAM 禁運期月數具體衝突(現有 12 個月 vs WO2 至少 6 個月),且 WO2 來源為出版社通用政策頁面的外推,並非該刊逐字聲明,兩者信心層級與數字皆不同,建議人工核實該刊實際 embargo 規定,不宜自動覆蓋既有較具體的數字。

---

## Human-Computer Interaction
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\human-computer-interaction.md`

- **Policies > AI Policy > Leniency (1-5) / Explicit permission gate?**
  - Existing: Leniency 4（disclosure-based; AI cannot be listed as author）；Explicit permission gate = No — disclosure-based
  - WO2 finding: leniency_1_5: 3；gate: "conditional"（WO2 signal_quality 僅 2/5，且承認未能直接讀到 hhci20 專屬頁面，403 fetch 失敗，是用 T&F 集團通用政策反推）
  - Why flagged: 既有欄位已有具體內容（非佔位符），WO2 給出的寬容度評分與 gate 類型與既有評分不同、屬於實質分歧而非單純補充細節，故不逕自覆蓋，留待人工判斷孰優（尤其 WO2 自身信心不高，403 多次未能讀到期刊專屬頁）。

---

## Human Factors
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\human-factors.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per Sage default)
  - WO2 finding: single-anonymized (single-blind) as default; double-anonymized available on author request via cover letter + separate title page — sourced directly from journal's own author-instructions page (https://journals.sagepub.com/author-instructions/hfs)
  - Why flagged: 既有欄位已有具體內容(非佔位符),但 WO2 的發現與其實質矛盾(預設審稿制度不同:雙盲 vs 單盲預設+可申請雙盲),且 WO2 來源是該刊自己的 Author Guidelines 頁面而非泛用 Sage 政策頁,證據力可能更高,需人工核實既有條目是否已過時或有誤,不由本次流程逕自覆蓋。

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 4
  - WO2 finding: 3 (gate: "conditional")
  - Why flagged: 既有 AI Policy 整段(含 Summary/Source URL)已是實質內容而非佔位符,依規則不應覆蓋;但 WO2 對同一份 Sage 政策給出的寬容度評分(3)與既有評分(4)不同、且 gate 描述用詞也有差異("disclosure-based" vs "conditional"),屬於對同一政策的量化評估分歧,列為衝突供人工複核,而非自動改寫既有數值。

---

## European Journal of Personality
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\european-journal-of-personality.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per SAGE default)
  - WO2 finding: single/double-anonymized peer review(具體匿名方式未逐字確認,不同 WebSearch 摘要用詞不一,有稱 anonymized 有稱 traditional);另設有 Registered Reports 軌道(自2018年起)及 streamlined review(可攜帶前一期刊審查意見重新投稿)
  - Why flagged: 既有檔案斷定為 double-anonymized,但 WO2 無法用逐字頁面確認匿名層級,信心不足;此外 WO2 發現期刊另設 Registered Reports 及 streamlined review 兩種審查通道,屬既有檔案未記載的新資訊,建議人工以期刊原始 Author Guidelines 頁面逐字核對後再決定是否更新 Type 欄位或於 Notes 補充審查通道類型。

- **Policies > AI Policy > Leniency / Gate**
  - Existing: Leniency 4;Explicit permission gate? No — disclosure-based
  - WO2 finding: Leniency 3;gate=conditional(需揭露,非全開放,亦非全禁)
  - Why flagged: 兩者對同一份 SAGE 通用 AI 政策的嚴格度評分不同(4 vs 3),且 gate 描述用詞不同(既有檔案稱『No — disclosure-based』,WO2 稱『conditional』,語意接近但嚴格度判讀有落差)。WO2 signal_quality 僅 2/5(期刊專屬 AI 政策子頁 404,屬 publisher-level 推論),既有檔案內容為既有維護者判斷,兩者孰優需人工複核,不逕自覆蓋。

- **Soft Metadata > Methodological Preferences (out of scope, supplementary only)**
  - Existing: 現有方法學偏好表未列出 Registered Reports、network psychometrics/Taxonomic Graph Analysis、streamlined review 等項目
  - WO2 finding: positioning.methods_welcome 列出 empirical/meta-analyses/theoretical/methodological/systematic reviews/registered reports/network psychometrics 等,並指出近年(2023-2025)刊出網絡心理計量、Taxonomic Graph Analysis 等新興計算方法論文
  - Why flagged: 此為主觀分類章節(Methodological Preferences),依規則不可直接編輯,但 WO2 提供了具體、可能有價值的補充發現(Registered Reports 軌道、network psychometrics 方法學歡迎度),建議維護者評估是否手動納入該章節,而非由此次自動比對逕行修改。

---

## Frontiers in Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\frontiers-in-psychology.md`

- **Metrics > Acceptance Rate**
  - Existing: High (~50%+) — reflects Frontiers editorial model
  - WO2 finding: 知乎資料：2024 年接受率約 37%，近年拒稿率上升、審查趨嚴，非「易發」期刊
  - Why flagged: 現有數字（~50%+，泛指 Frontiers 編審模式）與 WO2 引用的知乎社群估計（2024 年約 37%，且指出近年趨嚴）存在實質矛盾而非僅是精細化，且 WO2 來源為單一中文社群估計、信度中等，需要人工核實後才能決定是否更新，故不逕行覆蓋。

---

## Health Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\health-psychology.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per APA default)
  - WO2 finding: Single-masked (reviewers are anonymous to authors; author identity is known to reviewers — authors must NOT mask their own identifying information).
  - Why flagged: 現有內容是套用「APA 一般預設」的假設值，並非針對本期刊查證；WO2 則是直接引用本刊官方投稿頁面（apa.org/pubs/journals/hea/submit）得出「單盲」而非「雙盲」的結論，兩者屬於實質矛盾（盲審方向完全相反），且現有欄位並非佔位符，故不逕自覆蓋，需人工對照期刊官方 Submission Guidelines 後裁定。

---

## European Journal of Social Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\european-journal-of-social-psychology.md`

- **Policies > Preprint Policy > Post-acceptance (AAM) embargo length**
  - Existing: Yes | Embargo: 12 months
  - WO2 finding: accepted (peer-reviewed) version 可於 24 個月禁運期後自我典藏(standard Wiley SSH — Social Sciences & Humanities — embargo)
  - Why flagged: 既有條目寫 12 個月禁運期,但 WO2 引用 Wiley self-archiving 官方頁面指出社會/人文科學(SSH)類期刊標準禁運期為 24 個月,與現有值實質矛盾(可能既有值誤用了 STM 領域的通用預設,而非 SSH 領域專屬規則),需人工覆核 Wiley 官方頁面確認 EJSP 實際適用哪一個禁運期

- **Metrics > Review Cycle Time > Time to first decision**
  - Existing: *(fill manually)*
  - WO2 finding: SciRev 顯示「立即拒稿」(immediately rejected)決定時間為 23 天,但此數字僅適用於桌拒(desk-reject)子集,並非涵蓋所有決定結果的一般性「首次決定時間」
  - Why flagged: WO2 找到的唯一時間數字只針對桌拒個案(且僅 n=5 極小樣本中的最近一筆),不能代表期刊整體的首次決定時間,若直接填入該格恐誤導使用者,故不予直接套用,留待人工判斷是否有更完整數據

---

## IEEE Pervasive Computing
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\ieee-pervasive-computing.md`

- **Policies > AI Policy > Explicit permission gate**
  - Existing: No — disclosure-based
  - WO2 finding: JSON 結構化欄位 gate="yes",但其 summary 敘述內容其實描述的是「acknowledgments 揭露 AI 使用範圍」的揭露制,並非要求作者事先取得允許的「permission gate」;且此 WO2 來源(IEEE 出版倫理總則頁)非 IEEE Pervasive Computing 期刊專屬頁面。
  - Why flagged: 既有欄位已有具體內容(非 placeholder),依規則不得覆蓋;但 WO2 的結構化 gate 值與其自身文字描述、以及與既有檔案內容三者之間有實質不一致,需要人工複核到底 gate 該標 Yes 或 No,不宜由此次 patch 自動判定。

- **Policies > Preprint Policy > Pre-submission row**
  - Existing: Yes | arXiv / bioRxiv / similar permitted by most publishers
  - WO2 finding: Yes, but IEEE 政策明確僅認可 arXiv 與 TechRxiv 為第三方預印本儲存庫(未將 bioRxiv 列入認可名單);屬 IEEE 全出版線通則,非期刊專屬。
  - Why flagged: 既有欄位已有具體內容(非 placeholder),依規則不覆蓋;但 WO2 指出 IEEE 官方認可名單不含 bioRxiv,與既有欄位把 bioRxiv 一併列為「多數出版社允許」的寫法存在實質出入,可能誤導作者,建議人工核實後決定是否修正措辭。

- **Metrics > Review Cycle Time (Time to first decision / Time to first review / Time to acceptance total 三列)**
  - Existing: *(community estimate)* (三列皆為空白 placeholder)
  - WO2 finding: ~3 個月(12 週)——但此數字僅來自 LetPub/小木虫聚合頁/学术之家等中文期刊聚合站的統計摘要,WO2 自身將其 signal_quality 標為 1/5,並在「Fields WO2 could not find evidence for」清單中明列此欄位為缺乏可追溯第一手證據、未達到工作單要求的查證門檻。
  - Why flagged: 雖然這三列在既有檔案中確實是空白可填格,但 WO2 對應數據本身被其自身研究流程判定為證據不足、不可追溯到具體個案,不符合「有真實、可查證答案」的填入門檻,故未直接套用,留供人工判斷是否仍要以低信度社群估計形式收錄。

---

## Frontiers in Computer Science
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\frontiers-in-computer-science.md`

- **Policies > Peer Review > Type**
  - Existing: Frontiers collaborative peer review model (reviewer-author interactive)
  - WO2 finding: Single anonymized peer review（審稿人身份對作者匿名，作者身份對審稿人公開；文章發表時公開編輯與審稿人姓名及單位）
  - Why flagged: 此欄位已有具體內容，非空白佔位符，故不直接覆蓋。但兩者描述角度明顯不同：現有內容強調 Frontiers 標榜的「協作式、互動式」審稿流程風格，WO2 則給出正式的盲審分類（單向匿名），且明確指出審稿人姓名僅於文章接受後才公開。兩者未必互斥（可能是同一機制的不同敘述層次），但用詞差異足以造成讀者認知落差，建議人工核實後決定是否合併或並列兩種描述。

- **Review Cycle Time > Time to first decision / Time to first review**
  - Existing: *(pending)* / *(pending)*（兩列皆為空白佔位符）
  - WO2 finding: 約 13 週（約 3 個月）—— 來源為 Frontiers 官方頁面自陳數值，並經 LetPub（52 位評分者的中國作者投稿資料彙整站）交叉印證同為「13 Weeks」；SciRev 上本刊 0 筆評論，無法做獨立第一手驗證。
  - Why flagged: WO2 的 experiential.review_time_months 是一個有來源、有交叉驗證的具體數字，理論上可用來填補「Time to first decision」或「Time to first review」其中一列的空白，但來源描述僅稱其為籠統的『審稿週期』，未明確指出究竟對應四列中的哪一列（首次決定？首次收到審稿意見？還是與現有已填的「Time to acceptance (total): 3–4 months」重疊、只是同一統計的不同引用來源？）。基於逐一比對、不粗填的原則，這裡選擇不強行指定欄位，留給人工判斷此數字最適合放入哪一列，或是否僅作為對現有『3–4 個月』總接受時程的交叉佐證附註。

---

## International Journal of Child-Computer Interaction
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\international-journal-of-child-computer-interaction.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (per Elsevier default — varies by journal; some are double-blind)
  - WO2 finding: Double-blind, minimum 2 referees (來源: https://www.editage.com/research-solutions/journal/international-journal-of-child-computer-interaction/28946)
  - Why flagged: 既有條目標注為single-blind，但僅是基於Elsevier集團預設值的推測（並已自行註明『varies by journal』）；WO2從Editage的該刊專屬頁面找到具體資訊，明確指出此刊為double-blind且至少2位審稿人。兩者為single-blind vs double-blind的實質矛盾，且WO2來源看似指向該刊專屬條目而非集團泛用預設，建議人工核對官方Guide for Authors頁面（sciencedirect頁面曾回傳403無法直接驗證）以確認何者正確，故不代為覆蓋。

---

## IEEE Transactions on Affective Computing
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\ieee-transactions-on-affective-computing.md`

- **Policies > AI Policy (Explicit permission gate? / Leniency)**
  - Existing: Explicit permission gate? No — disclosure-based；Leniency (1-5): 4
  - WO2 finding: gate: "conditional"；leniency_1_5: 3
  - Why flagged: 既有內容並非佔位符（已具體描述 IEEE 通用 AI 政策），依規則不可直接覆蓋。但 WO2 對同一份 IEEE 通用政策的定性不同：既有檔案判定「無明確許可關卡、僅需揭露」且寬容度4；WO2 判定為「conditional gate」且寬容度僅3。兩者對同一政策的嚴格程度評分不一致，建議人工重新核對 IEEE Author Center 原文後決定是否調整寬容度分數或 gate 分類。

- **Metrics > Acceptance Rate / Desk Rejection Rate**
  - Existing: *(fill manually if known)* （兩者皆為佔位符）
  - WO2 finding: acceptance_note: 一則經WebSearch聚合之知乎/CSDN文章聲稱拒稿率約70%，但原文(zhuanlan.zhihu.com/p/674046111)遭403拒絕僅能以搜尋引擎摘要間接佐證；desk_reject_pct 明確留白(null)
  - Why flagged: WO2 自身已將此70%拒稿率數字標註為「可信度中等，未列為高信度數字」，且來源網頁無法直接存取（僅搜尋摘要）。依規則只在 WO2「有真實、有來源根據的答案」時才可填入，此數字不符合門檻，故不逕行套用，留待人工判斷是否值得以高度但書方式記錄或直接捨棄。

- **Review Cycle Time (全部四列)**
  - Existing: *(fill manually)* （四列皆為佔位符：first decision / first review / acceptance total / publication）
  - WO2 finding: review_time_months: 「分歧極大，區間約2–12個月」，綜合 SciRev(n=2,一審17週/總3.5月平均)、小木虫(n=1,三輪審查約8個月)、LetPub網友彙整(初審約45天但大修後總週期7–9個月，亦有案例一審等11個月)、CSDN(宣傳性文章聲稱2個月但自承2–12個月區間)
  - Why flagged: WO2 資料雖有引用來源，但樣本數極小(n=1-2)、彼此矛盾、且未清楚區分「首次決定/首次審稿意見/總計錄用時間/接受後出版時間」四個不同階段，若強行拆分填入四個欄位將等同虛構精確度。建議留給人工判斷是否要以區間+但書方式填入其中一列（例如 acceptance total 大致 2-12 個月，樣本極小），而非由本次自動比對逕行分配。

- **Soft Metadata（範圍外：Framing Requirements / Best Suited For / Reviewer Pool Characteristics）**
  - Existing: Framing Requirements 已描述必須具情感運算貢獻；Best Suited For 列出臉部/語音/生理情緒辨識等；Reviewer Pool Characteristics 描述 ACII/IEEE 情感運算社群審稿人
  - WO2 finding: positioning.accepts_now: 近期(2025)徵稿聚焦「情感LLM與心理健康應用」「社交媒體情感/情緒推理分析」等新方向；reviewer_culture: SciRev唯一評論(2.5/5)指出審查「不必要地冗長」且疑似對錯稿件，另中國大陸作者占發文23.3%、中國科學院為主要投稿機構之一（惟均屬行銷性部落格文字，非嚴謹統計）
  - Why flagged: 此為 WO2 針對範圍外主觀章節（定位/審稿文化）的補充發現，依規則不可直接編輯這些章節，僅供人工後續參考是否要更新 Best Suited For（納入情感LLM/心理健康/社群媒體情感分析新方向）或 Reviewer Pool Characteristics（審稿冗長個案、中國大陸投稿比例高）等描述。

---

## IEEE Access
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\ieee-access.md`

- **Metrics > Acceptance Rate (not filled) vs. Soft Metadata > Reviewer Pool Characteristics existing acceptance-rate claim**
  - Existing: 現有 Soft Metadata > Reviewer Pool Characteristics 段落已寫:「~27% average acceptance rate (community evidence: manusights 2026-05)」;Metrics 表格的 Acceptance Rate / Desk Rejection Rate 儲存格本身仍是 *(fill manually if known)* 空白。
  - WO2 finding: WO2 experiential 發現:SciRev 未揭露確切錄取率(n/a);中文論壇(小木虫、知乎)提及近年錄取率由約 50% 降至約 30%,但此為二手轉述、非一手統計,WO2 自身也將其列入 blanks(desk_reject_pct 精確數字缺乏權威來源)。
  - Why flagged: WO2 沒有足夠一手/權威數字可直接填入 Metrics 表格的 Acceptance Rate / Desk Rejection Rate(故本次未提出變更),但其約 30%(近年下降趨勢)的方向性資訊與既有 Soft Metadata 中 ~27% 的社群估計大致吻合、可互相佐證,建議人工複核後決定是否要把「近年由 ~50% 降至 ~30%」的趨勢描述補充進 Metrics 表格備註或既有 Reviewer Pool Characteristics 段落(屬於主觀子區塊,依規則不由本次 patch 直接編輯)。

---

## International Journal of Human-Computer Interaction
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\international-journal-of-human-computer-interaction.md`

- **Metrics > Acceptance Rate**
  - Existing: *(not disclosed by publisher)*
  - WO2 finding: LetPub 聚合評價（97 筆，總分 6.7/10）將接受難度標為「容易」，但 WO2 自身註明這是群眾聚合的單一詞標籤而非第一手百分比；另一則小木虫論壇貼文提到一次因「非新穎數據/非高科學重要性」而遭拒的理由，但 WO2 亦坦承無法確認該討論串主題是否真的對應本刊（signal_quality: 2/5）
  - Why flagged: 雖然現有儲存格文字符合 placeholder 判定條件，但 WO2 提供的並非可直接套入表格的接受率數字，而是低信度、群眾聚合且主題比對不確定的質性標籤，貿然填入恐造成誤導性精確度，建議留給人工判斷是否採用或改寫為質性附註

- **Review Cycle Time > Time to first decision / Time to first review**
  - Existing: *(pending)*
  - WO2 finding: experiential.review_time_months: 「1.5-3 months (6-12 weeks) per LetPub aggregate...一則小木虫貼文描述約 3 個月做出初步編輯決定，但該討論串內容偏生醫資訊學調性，可能與本 HCI 期刊主題不符（低信度標記）；SciRev 顯示零筆送審評論」（signal_quality: 2/5）
  - Why flagged: WO2 提供的是一個籠統且彼此略有出入的區間（LetPub 六到十二週 vs 小木虫約三個月），且未能對應到表格四個具體階段（首次決定/首次審稿/總接受時間/出版）中的哪一項，也對主題相關性存疑，強行拆分填入特定欄位風險過高，建議人工核實後再決定要填入哪一列、以及是否加註信度說明

- **Strategic Notes / Framing Requirements（主觀章節，範圍外，僅供補充參考）**
  - Existing: 現有 Framing Requirements 已描述『需展現應用型 HCI 貢獻』等既有框架要求，未提及特定徵稿主題
  - WO2 finding: positioning.framing_required：目前開放中的特刊《The Age of AI Agents》（截稿 2026-03-15）明確歡迎批判/社會技術框架（偏見、歧視、監控、隱私、透明度、公平性、平台資本主義、AI 治理、東西方比較），但 WO2 也發現另一則搜尋結果顯示該刊『目前並未接受新特刊提案』，兩者矛盾且 WO2 未能以單一權威來源調解
  - Why flagged: 此為觸及 Strategic Notes/Framing Requirements 等主觀章節的定位性發現，依規則不可直接編輯該區塊，且 WO2 內部兩則來源本身互相矛盾（特刊開放中 vs 期刊不接受新特刊提案），需要人工查證特刊現況後再決定是否採用

---

## International Journal of Social Robotics
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\international-journal-of-social-robotics.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per Springer default — varies by journal)
  - WO2 finding: single-blind (sourced from https://link.springer.com/journal/12369/submission-guidelines)
  - Why flagged: 這是實質衝突而非補充細節——現有值是套用 Springer 通用預設的推測(檔案本身也註記「varies by journal」),WO2 則引用該刊官方投稿指引頁得出「single-blind」。兩者矛盾,需人工查證該刊官方頁面實際審稿制度後再決定採用哪一個值,不逕自覆蓋。

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 4
  - WO2 finding: 3
  - Why flagged: 現有內容已是完整實質政策描述(非佔位符),故不比對填補;但 WO2 對同一 Springer Nature 標準政策給出不同寬容度評分(4 vs 3),且 permission gate 描述用語也有差異(現有:「No — disclosure-based」;WO2:「conditional」),語意相近但評分不同,建議人工核實後決定是否調整既有評分。

---

## International Journal of Human-Computer Studies
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\international-journal-of-human-computer-studies.md`

- **Review Cycle Time > Time to first decision / Time to first review（目前皆為 *(pending)*）**
  - Existing: *(pending)*
  - WO2 finding: WO2 experiential.review_time_months 內部即有兩組互相矛盾的數字:SciRev(僅 3 筆評論)顯示總處理時間約 3.0 個月、決定時間約 73 天;LetPub 則引用「Elsevier 官方統計」平均 20.8 週(約 4.8 個月)投稿至首次決定。兩者差距近一倍。
  - Why flagged: WO2 自身已標註 overall signal_quality 僅 2/5,且 SciRev 樣本量極小(n=3)不足以代表整體,兩來源數字又互相矛盾,沒有單一「real, sourced answer」可直接採用,若挑一個填入即是變相的粗填/覆蓋風險,故不填表格,留給人工判斷要採用哪個數字、或以區間/雙來源並陳方式呈現。

---

## International Journal of Design
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\international-journal-of-design.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (typical journal default; check publisher)
  - WO2 finding: Double-blind (雙盲審) — 來源 http://www.ijdesign.org/index.php/IJDesign/about/submissions
  - Why flagged: 現有值是套用「期刊家族常規假設」且明白寫著「check publisher」尚未查證；WO2 實地查閱該刊官方投稿頁後得出具體結論「雙盲審」，兩者直接矛盾（單盲 vs 雙盲），非單純補充細節，故列為衝突待人工核實，不逕行覆蓋。

- **Policies > AI Policy（Has journal-specific AI policy? / Leniency / Summary 等列）**
  - Existing: Has journal-specific AI policy? Yes (publisher default + may have journal overlay); Explicit permission gate? No — disclosure-based; Leniency 3-4; Summary 描述一般揭露式政策
  - WO2 finding: WO2 逐字查閱投稿頁與作者須知全文，未見任何 AI/生成式AI 使用揭露或許可條款，亦查無期刊或出版單位（Chaoyang University of Technology / Taiwan Design Center）獨立發布的 AI 政策頁；gate 與 leniency 皆刻意留空(null)，該子項 signal_quality=0。
  - Why flagged: 現有表格假設此刊「有」AI政策並給出具體寬鬆度(3-4)，但 WO2 的實地查證結論是「查無此刊或其出版單位發布的任何AI政策證據」，屬實質矛盾而非僅是細節不足；此發現雖已於下方 Soft Metadata > AI-Research Notes 供人工複核，但上方 Policies > AI Policy 表格本身尚未依此調整，故仍列為衝突，不逕行覆蓋既有內容。

- **Metrics > Review Cycle Time（Time to first decision 列，階段對應含糊）**
  - Existing: Time to first decision | *(community estimate)* | （佔位符，符合可填條件）
  - WO2 finding: experiential.review_time_months = ">3個月 (>12週) 或屬邀稿(by invitation)"，來源為 LetPub 期刊頁彙總統計（非單一投稿人經驗分享），但未指明此數字對應「首次決定」「首次審稿」或「總計錄取時間」四列中的哪一項
  - Why flagged: WO2 提供的是複合且含糊的審稿週期敘述（">12週" 或 "屬邀稿" 二選一），未明確對應表格四個階段中的哪一列；且 WO2 對此段落整體 signal_quality 僅 2/5，原始資料中亦多次自陳「可信度中等偏低，僅供參考」「原頁403無法核實，僅搜尋引擎二手摘要」。為避免不精確地指派到某個特定 pending 欄位造成誤導性精確感，保守起見不逕行填入，留待人工判斷應歸類於哪一列或是否僅適合放在敘述性 Notes 中。

---

## Journal of Abnormal Child Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-abnormal-child-psychology.md`

- **Policies > AI Policy — Explicit permission gate? / Leniency**
  - Existing: Explicit permission gate? No — disclosure-based | Leniency (1-5): 4
  - WO2 finding: gate: "conditional" | leniency_1_5: 3
  - Why flagged: 現存欄位已有實質內容（非佔位符），依規則不可直接覆寫；但 WO2 對『gate』的分類（conditional）與寬容度評分（3）跟現存資料（No/disclosure-based, 4）略有出入，且 WO2 signal_quality 僅 2/5、其判斷是根據 Springer Nature 通用政策文字外推，並非該期刊獨有頁面（原頁面被 Springer 登入牆擋下），故列為衝突留待人工複核，不逕行覆蓋。

---

## Journal of Applied Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-applied-psychology.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per APA default)
  - WO2 finding: Masked (single-anonymized) peer review — author identity concealed from reviewers only (not mutual anonymity); manuscripts that pass desk screen go to 2-3 reviewers. Source: https://www.apa.org/pubs/journals/apl/submit
  - Why flagged: 現有欄位已有具體內容（雙盲），非佔位符，故不可直接覆蓋；但 WO2 直接引用 JAP 投稿頁面得出「單盲（作者對審稿人匿名，但審稿人身分不隱藏）」，與現有的「雙盲」屬實質矛盾而非僅補充細節，需要人工核對 JAP 官方投稿頁面以確認實際審稿制度類型。

- **Metrics > Acceptance Rate / Desk Rejection Rate**
  - Existing: *(fill manually if known)*
  - WO2 finding: null / 無法找到任何來源（SciRev 與 LetPub 頁面此欄位皆為空，僅一則質化軼事：fabiaoji.com 單一中國作者 2021 投稿被拒，原因為研究設計缺陷）
  - Why flagged: 雖然是可填空的佔位符，但 WO2 本身也明確表示查無具體數字，因此沒有可用於填入表格的實質數值，僅有質化印象（審稿人專業、被拒因研究設計硬傷），列為 conflicts 供人工留意而非直接編輯 Metrics 表格。

---

## Journal of Psychopathology and Clinical Science (formerly Journal of Abnormal Psychology)
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-psychopathology-and-clinical-science.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per APA default)
  - WO2 finding: Single-anonymous by default; masked (double-anonymous) review is optional and must be explicitly requested by the author in the cover letter — this is APA's standard practice referenced for this journal.
  - Why flagged: 現有欄位已有具體內容（非佔位符），但 WO2 的結論與現有內容直接矛盾：現有寫「預設雙盲」，WO2 寫「預設單盲，雙盲需作者主動於 cover letter 要求」。這是實質分歧而非細節補充，且 WO2 自己在 blanks 中承認未找到 JPCS 專屬（相對於 APA 通用慣例）的確認聲明，故不予覆蓋，交由人工核實。

- **Policies > Preprint Policy > Under review 列**
  - Existing: No updates
  - WO2 finding: Yes, permitted. APA (publisher-wide policy covering this journal) explicitly supports posting preprints before and during submission; no restriction found specific to JPCS.
  - Why flagged: 現有表格已有具體內容，WO2 的說法（『投稿前及投稿期間皆可張貼/更新』）與現有『審查中不可更新』存在潛在牴觸。且 WO2 引用來源是一篇 SAGE 期刊的 DOI（非 APA 官方頁面），來源與該期刊出版社不符，可信度存疑，故不採用，僅供人工複核。

- **Soft Metadata > Framing Requirements（範疇外，僅供參考）**
  - Existing: Mandatory framing: mechanism-focused clinical-science contribution; anti-stigma framing expected
  - WO2 finding: positioning.framing_required: 'Work should be framed as basic/etiological science relevant to psychopathology mechanisms rather than purely applied/clinical-intervention-outcome studies... Currently soliciting a special issue specifically on medical assistance in dying.'
  - Why flagged: 此為主觀/定位類欄位，依規則不可直接編輯，僅作為人工複核用的補充發現：WO2 進一步指出目前有一個關於『醫助死亡（medical assistance in dying）』的徵稿專刊，且強調『基礎/病因學研究』相對於『應用/臨床介入結果研究』的定位區分，可作為現有 Framing Requirements 段落未來人工更新時的參考素材。

---

## Journal of Applied Social Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-applied-social-psychology.md`

- **Policies > AI Policy > Leniency (1-5) / Explicit permission gate?**
  - Existing: Leniency = 3; Gate = "No — disclosure-based; image generation prohibited"
  - WO2 finding: Leniency = 2; Gate = "conditional"
  - Why flagged: 兩者描述的底層政策(Wiley 揭露制 AI 政策)實質相同,但既有條目已有具體內容(非佔位符),不可逕行覆蓋。WO2 給出的 leniency 分數(2)比既有條目(3)更保守,且 gate 標籤用詞不同("No" vs "conditional")——是否要因此下修既有評分,需人工判斷,不宜由此次 surgical patch 自動覆蓋。

- **Soft Metadata > Reviewer Pool Characteristics / Practical Concerns(補充性發現,非直接編輯)**
  - Existing: 既有 Tier 2 敘述:審稿人來自應用社會心理學/SPSSI 社群,審稿人常見要求聚焦『實務意涵』『生態效度』
  - WO2 finding: WO2 experiential finding(SciRev n=5,低代表性):審稿報告品質評分2.8/5(中下)、整體投稿體驗2.2/5(中等偏下)、審稿難度3.7/5(偏難);其中一則評論提及『編輯在作者大幅修改後直接拒稿、未再送審』,顯示編輯決策可能不完全遵循標準流程
  - Why flagged: 此為 Soft Metadata 主觀子章節範疇(Reviewer Pool Characteristics / Practical Concerns),依規則不可直接編輯,僅供人工日後評估是否要在 Tier 2 描述中補充『編輯可能繞過標準送審流程直接拒稿』此一經驗性觀察。樣本量極小(n=5),使用時應標註低可信度。

---

## Journal of Clinical and Experimental Neuropsychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\cognitive-science\journal-of-clinical-and-experimental-neuropsychology.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per T&F default)
  - WO2 finding: Single anonymized (single-blind) peer review, editor-mediated initial appraisal before referee assignment (source: https://www.tandfonline.com/journals/ncen20/about-this-journal)
  - Why flagged: 既有值是根據「T&F 預設值」的推測性假設,並非期刊專屬確認;WO2 則引用了期刊自己的 'about this journal' 頁面,明確指出是單盲(single-anonymized)而非雙盲。這是審稿類型上的實質矛盾(雙盲 vs 單盲),會直接影響投稿人對評審流程的預期,建議人工查核 tandfonline.com/journals/ncen20/about-this-journal 原始頁面後再決定是否修正,不應由此次比對逕自覆蓋。

---

## Journal of Counseling Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-counseling-psychology.md`

- **Policies > AI Policy > Leniency (1-5) / Explicit permission gate?**
  - Existing: Leniency: 4；Explicit permission gate?: No — disclosure-based
  - WO2 finding: leniency_1_5: 3；gate: "conditional"（同一段政策描述文字，但WO2將寬容度評為3/5、閘門定性為「有條件」，既有檔案評為4/5、閘門定性為「No」）
  - Why flagged: 兩邊引用的政策原文幾乎相同（APA統一政策：允許使用但強制揭露、AI不得列作者），但對同一政策的量化評分（4 vs 3）與閘門定性描述（No vs conditional）不一致，屬於評分口徑差異而非新事實，需要人工判斷該用哪個評分口徵，不宜自動覆蓋既有非空白欄位。

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per APA default)
  - WO2 finding: Masked (blind) review — APA整體約半數的47本期刊強制匿名審查、其餘多數可依要求採用，但WO2明確指出「JCP自己的頁面並未明文重申此點，故本刊層級的確切匿名審查狀態未經確認」
  - Why flagged: 既有欄位以肯定語氣寫「per APA default」，WO2研究則明確表示此刊層級的匿名審查狀態『未經確認』，屬於確定性程度上的分歧（既有較肯定、WO2較保留），建議人工核實JCP的Instructions for Authors是否明文規定，而非直接修改已有內容的欄位。

---

## Journal of Consulting and Clinical Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-consulting-and-clinical-psychology.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per APA default)
  - WO2 finding: Masked (anonymized) peer review, mandatory for all submissions (sourced directly from JCCP's own submission-guidelines page: https://www.apa.org/pubs/journals/ccp/submit)
  - Why flagged: 現有值是「假設 APA 預設為 double-anonymized」，屬推定；WO2 是直接引用期刊自己投稿頁的用詞「masked (anonymized)」，用語不同（masked 未必等同 double-anonymized，可能僅指單向匿名）。因現有欄位已有實質內容（非佔位符），依規則不可逕行覆蓋，僅供人工核實是否為同一制度的不同措辭或實質差異。

- **Policies > AI Policy > Leniency (1-5) / Explicit permission gate?**
  - Existing: Leniency: 4；Explicit permission gate?: No — disclosure-based
  - WO2 finding: leniency_1_5: 3；gate: "conditional"
  - Why flagged: 現有欄位已有具體內容（非佔位符），依規則不得直接覆蓋分數判斷。WO2 給出的寬容度評分（3）與現有評分（4）不同，且 gate 標籤用詞不同（conditional vs. disclosure-based），雖然兩者敘述的政策實質內容（APA 揭露即可、AI 不可掛名作者）看似一致，但量化評分有落差，留供人工複核。附註：本檔案 Soft Metadata 已有一份 2026-07-13 新增的「AI-Research Notes (WO2 supplement)」段落收錄了此 WO2 摘要作為補充研究筆記，此處僅是在資料表格層級再次標記此量化落差。

---

## Journal of Design History
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\journal-of-design-history.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (typical journal default; check publisher)
  - WO2 finding: double-anonymized (double-blind) peer review; at least two independent referees per manuscript (source: https://academic.oup.com/jdh/pages/general_instructions)
  - Why flagged: 現有欄位並非空白佔位符,已有具體內容(Single-blind),但屬於通用家族預設猜測而非期刊實查;WO2 直接引用該刊 General Instructions 頁面查得為 double-anonymized(double-blind)審查,兩者在審查類型這個核心事實上直接矛盾,非僅細節補充,需人工核實官方頁面後再決定是否更正,不宜自動覆蓋。

- **Policies > AI Policy > Explicit permission gate? / Leniency (1-5) / Source URL**
  - Existing: Explicit permission gate? No — disclosure-based | Leniency (1-5): 3-4 | Source URL: https://academic.oup.com/journals/pages/authors/preparing_your_manuscript/ai-policy
  - WO2 finding: gate: conditional (WO2 摘要指出 AI 生成內容需經 OUP 書面許可,必要時須以人工內容替換) | leniency_1_5: 2 | source_url: https://academic.oup.com/pages/for-authors/books/author-use-of-artificial-intelligence
  - Why flagged: 現有欄位已有具體內容而非佔位符,但 WO2 查證發現 JDH 專屬 AI 政策頁(academic.oup.com/jdh/pages/ai-policy)回傳 404,期刊本身並無獨立頁面,現有 Source URL 可能已失效或本來就非期刊專屬;且 WO2 引用的 OUP 出版社通用政策文字顯示對 AI 生成內容有『需書面許可』的門檻(偏向 conditional/permission-gated),與現有『No — disclosure-based』的定性存在實質分歧,寬容度評分也不同(2 vs 3-4)。這屬於對同一欄位的不同結論,而非單純補充細節,故列為衝突交由人工核實,不做覆蓋。

---

## Journal of Cognitive Neuroscience
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\cognitive-science\journal-of-cognitive-neuroscience.md`

- **Policies > AI Policy (Has journal-specific AI policy? / Leniency)**
  - Existing: Has journal-specific AI policy? = "No (follows MIT Press publisher default)"；Leniency (1-5) = 4
  - WO2 finding: gate = "conditional"（JoCN 有專屬 AI 政策，補充 MIT Press 出版倫理，屬 conditional gate）；leniency_1_5 = 3
  - Why flagged: 屬直接矛盾而非單純補充細節：現有條目認定「無專屬政策、僅遵循 MIT Press 預設」，WO2 調查則認定「JoCN 確有專屬 AI 政策」，且寬嚴度評分（4 vs 3）也不同。此矛盾此前已被同一 WO2 研究批次以獨立補充意見形式記錄在 Soft Metadata > AI-Research Notes 區塊（2026-07-13），但尚未反映到 Policies > AI Policy 表格本身，故仍需人工比對 direct.mit.edu 稿約頁面後裁決是否要覆蓋表格內容，不宜由本次流程自動代為判斷。

- **Review Cycle Time（全部四列）**
  - Existing: 四列皆為 *(fill manually)* 佔位符，尚無實質內容
  - WO2 finding: SciRev（僅2筆評論）顯示首輪審查約3.8個月、總處理時間約7.1個月（最新一筆23.4週）；LetPub 網友經驗匯總則稱『一般3-8週』
  - Why flagged: 雖然這些欄位目前是真正的佔位符（符合可填空條件），但 WO2 自身已在 experiential.review_time_months 中明確聲明『兩者差距大且樣本量都極小，故不宜取單一數字』——也就是說 WO2 並未提供一個『真實且有信心的單一答案』可直接套入表格，而是兩個互相矛盾、樣本量各僅個位數的來源。強行選一個數字填入會違反『不粗填』原則，故留待人工判斷是否要以區間/附注形式呈現，而非由本次流程直接寫入。

---

## Journal of Child Psychology and Psychiatry
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-child-psychology-and-psychiatry.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per Wiley default — varies by journal)
  - WO2 finding: single-blind (editor triage + external referees); double-blind not confirmed — inferred from a search-engine-synthesized snippet, not primary text (author guidelines page returned HTTP 402 on WO2's fetch attempts)
  - Why flagged: 既有內容為「雙盲」與 WO2 查到的「單盲」直接矛盾,且雙方證據都不算特別扎實(既有為 Wiley 預設推論,WO2 為二手搜尋摘要),需人工查證期刊自己的作者指南頁面以確認實際盲審類型,不應由 AI 逕自擇一覆蓋。

- **Review Cycle Time > Time to first decision**
  - Existing: *(fill manually)* — 空白,但檔案內 Soft Metadata > Reviewer Pool Characteristics 段落已寫「Decision in ~5 weeks (excluding desk rejects)」
  - WO2 finding: publisher 目標 60 天(~2 個月,送外審案件);SciRev 彙總(n=5)平均 2.1 個月投稿到首次決定;另外桌拒/triage 平均約 18 天
  - Why flagged: 雖然此表格欄位本身是空白,但檔案另一段落已寫明「~5 週」的具體數字,與 WO2 的「~2 個月 / 2.1 個月」量級不完全一致(5 週≈1.15 個月 vs 2~2.1 個月)。若直接依 WO2 填入本表,會與檔案內既有敘述產生內部不一致,建議人工核對後統一,而非逕自填入。

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 3
  - WO2 finding: 2(WO2 標記為推斷值,signal_quality 僅 2/5)
  - Why flagged: 兩者都是基於同一份 Wiley 出版社通用 AI 政策(均未找到 JCPP 期刊專屬頁面)做出的主觀寬鬆度評分,但數字不同。因 AI Policy 欄位已有實質內容(非空白佔位),依規則不應直接編輯,僅記錄此數值分歧供人工複核是否要調整既有評分。

- **Soft Metadata > Framing Requirements / Epistemological & Political Leanings (out of scope,僅供參考)**
  - Existing: 既有段落基於 2026-05 的 ACAMH 作者指南與 editage.com 聚合證據,強調「clinical/mechanism contribution」框架要求與 ~50% 首週桌拒
  - WO2 finding: WO2 提供更新的 2025-2026 具體範例(Lukito 2025 doi:10.1111/jcpp.70003 之 ADHD/autism 共創測量驗證論文;Charman 2026 doi:10.1111/jcpp.70048 之前瞻縱貫嬰兒手足研究),並將定位精煉為『clinically relevant / translational value to developmental psychopathology』,純基礎科學或非臨床族群研究為較弱的 fit
  - Why flagged: 此為 WO2 對『目前期刊實際接受什麼』的補充性定位發現,涉及 Soft Metadata 的主觀章節(Framing Requirements/Epistemological & Political Leanings),依規則屬 out of scope 不應直接編輯,僅供人工評估是否納入既有敘述作補充更新。

---

## Journal of Experimental Psychology: Learning, Memory, and Cognition
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\cognitive-science\journal-of-experimental-psychology-learning-memory-and-cognition.md`

- **Policies > AI Policy > Explicit permission gate? / Leniency (1-5)**
  - Existing: Explicit permission gate?: No — disclosure-based ; Leniency (1-5): 4
  - WO2 finding: gate: "conditional" ; leniency_1_5: 3
  - Why flagged: 兩邊都是根據同一份APA出版社通用生成式AI政策頁面得出結論，但既有條目判定為「否，僅屬揭露制」且寬容度給4分，WO2結構化欄位卻判定為「conditional（條件式）」且寬容度給3分——這是對同一份原始政策的不同解讀（是否等同於「需要許可」），非單純細節補充，建議人工複核以決定哪個描述更準確，故未逕行覆蓋既有內容。

---

## Journal of Environmental Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-environmental-psychology.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (per Elsevier default — varies by journal; some are double-blind)
  - WO2 finding: Double anonymized (double-blind); empirical manuscripts typically sent to 3 independent expert reviewers, other submission types to at least 2 (sourced directly from this journal's own Guide for Authors page: https://www.sciencedirect.com/journal/journal-of-environmental-psychology/publish/guide-for-authors)
  - Why flagged: 既有內容是套用 Elsevier 集團預設值的推測性描述（帶「varies by journal」的保留語），而 WO2 引用的是本刊自己的 Guide for Authors 頁面，明確指出是 double-blind 而非 single-blind。兩者在審稿盲審類型上直接矛盾，且 WO2 來源看似更具期刊專屬性，但因原始 Guide for Authors 頁面對 WebFetch 回傳 403（WO2 自陳未能逐字核對原文，只能靠 WebSearch 聚合摘要），建議人工直接開啟該頁面核實後再決定是否覆寫既有欄位。

---

## Journal of Educational Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-educational-psychology.md`

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 4
  - WO2 finding: 3
  - Why flagged: 兩者對政策性質的判斷方向一致（皆為揭露式/conditional，非事前許可制），但寬容度評分本身不同（現有 4 分 vs WO2 判定 3 分），屬量化評分的實質分歧而非單純補充細節，依規則不可逕行覆蓋，留待人工覆核決定是否調整。

---

## Journal of Personality Assessment
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-personality-assessment.md`

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 4
  - WO2 finding: 3
  - Why flagged: 兩者對同一份 T&F 集團通用 AI 政策(揭露義務強制、無需編輯逐案事前核准)描述內容一致,但對「寬容度」的主觀評分不同(現存 4 分 vs WO2 3 分)。這是判斷分數落差而非事實矛盾,留給人工覆核決定採用哪一個評分,不逕行覆蓋。

---

## Journal of Experimental Psychology: General
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\cognitive-science\journal-of-experimental-psychology-general.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per APA default)
  - WO2 finding: Masked (double-masked/blind) review is OPTIONAL — 作者可於投稿時選擇匿名審查文章類型；預設非強制雙盲。
  - Why flagged: 兩者對「雙盲審查是否為強制預設」的陳述直接矛盾（既有：APA 預設即為雙盲；WO2：作者可自選、非強制預設），需人工查證 APA/XGE 官方投稿頁以確認何者正確，故不逕行覆蓋，留待人工複核。

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 4
  - WO2 finding: 3 (gate: conditional)
  - Why flagged: 既有條目已有具體政策描述（非佔位符），依規則不應直接覆蓋；但兩份研究對寬容度評分不一致（4 vs 3），且 WO2 將 gate 定性為 conditional 而既有條目定性為「No — disclosure-based」，語意相近但量化評分有落差，列為衝突供人工複核，不逕行修改。

- **Soft Metadata > Framing Requirements (out-of-scope subjective section)**
  - Existing: Mandatory framing? Yes (strong) — 需展現 general experimental psychology contribution with broad interest；83% raw rejection rate 等既有描述
  - WO2 finding: 官方 Aims & Scope 明確要求投稿須論證『跨越至少兩個心理學次領域傳統的廣泛興趣』；Brief Reports（≤3000字）未經審查即拒稿比例較高，需展現高度結果穩健性。
  - Why flagged: WO2 對 positioning/framing 的官方 Aims & Scope 引述提供了比既有條目更明確的『跨≥2次領域』具體門檻描述，屬主觀章節（Framing Requirements）範圍，依規則不逕行編輯，僅供人工複核是否納入補充。

- **Soft Metadata > Reviewer Pool Characteristics (out-of-scope subjective section)**
  - Existing: Reviewers drawn primarily from the general experimental psychology community... Reviewer competence variance: Medium
  - WO2 finding: SciRev 量化評分：審稿報告品質 3.8/5.0；整體流程評價 3.6/5.0；其中一筆評論審稿難度評為 4.7/5.0（非常困難）；審稿人『非常專業並提供大量有用建議』（樣本僅 6 筆，需謹慎採信）。
  - Why flagged: WO2 提供了具體量化的 SciRev 評分數據，可作為既有質性描述的補充佐證，但樣本量極小（n=6）且屬主觀章節範圍，依規則不逕行編輯，列為供人工複核的補充發現。

---

## Journal of Occupational Health Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-occupational-health-psychology.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per APA default)
  - WO2 finding: masked review (author identity concealed from reviewers; standard APA masked review) — source: apa.org/pubs/journals/ocp/submit
  - Why flagged: 現有內容已明確填寫「雙向匿名(double-anonymized)」,屬有實質內容的欄位,依規則不可逕自覆蓋。但 WO2 的措辭「author identity concealed from reviewers」聽起來偏向單盲(僅隱匿作者身分,未提及審稿人身分是否對作者匿名),與現有「double-anonymized」的雙盲描述可能矛盾,建議人工查核 APA/JOHP 官方投稿頁面確認實際審稿類型是單盲或雙盲。

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 4
  - WO2 finding: 3
  - Why flagged: AI Policy 整欄(含 Summary 文字)已是具體內容而非佔位符,依規則不可覆蓋。兩份資料對政策內容的描述(揭露制、非作者列名、非事前核准)幾乎一致,但寬容度評分不同(現有評4分、WO2評3分),屬評分主觀判斷差異而非事實矛盾,建議人工複核何者評分較合理再決定是否調整。

- **Metrics > Review Cycle Time (四列)**
  - Existing: 全部為 *(fill manually)* 佔位符
  - WO2 finding: WO2 experiential.review_time_months: SciRev僅2筆評論 — 第一輪約1.5個月、總處理時間約3.1個月、最新一筆6.6週、另一筆立即拒稿(desk reject)決策31天;WO2 signal_quality=1 且自行註明「因樣本數僅2,不可視為穩定估計」
  - Why flagged: 雖然四列都是可填的佔位符,但 WO2 資料樣本數僅2筆、訊號品質自評1/5,且四個數字（第一輪/總處理/最新一筆/desk reject）無法明確、無爭議地對應到現有表格的四個欄位(first decision / first review / acceptance total / publication),強行拆分填入需要額外詮釋與臆測,不符「不粗填」原則。故不逕自套入表格,改列為衝突項供人工判斷是否採用及如何分類對應。

- **Soft Metadata > Framing Requirements（補充參考,非直接編輯）**
  - Existing: Manuscripts must demonstrate workplace + health/wellbeing intersection. SOHP affiliated.
  - WO2 finding: WO2 positioning finding: Aims & Scope 頁列出三大範疇 — 工作組織(organization of work)、個人心理特質(individual psychological attributes)、工作與非工作介面(work-nonwork interface),皆連結至員工健康/安全/福祉；投稿類型分標準手稿(上限40頁)與 Research Notes 短文(上限20頁,暱稱'Kevin's Corner')。positioning.signal_quality 僅1(未取得逐篇文章佐證,僅期刊層級 scope 敘述)。
  - Why flagged: Soft Metadata 之 Framing Requirements 屬主觀分析區塊,依規則不得直接編輯,僅能作為補充參考列入衝突項供人工評估是否要用此更細緻的三分類 Aims & Scope 描述、或新增 Research Notes/'Kevin's Corner' 短文類型的字數上限資訊(此點亦可能與 Format > Word limit 佔位符相關,但因未達 fillable 標準之直接證據，未列入 changes)。

---

## Journal of Personality
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-personality.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per Wiley default — varies by journal)
  - WO2 finding: single-blind（依 Wikipedia 條目與一般 Wiley 心理學期刊慣例描述；未能於期刊官方作者指南頁直接核實，因該頁 HTTP 402 無法讀取）
  - Why flagged: 現有條目與 WO2 對審稿類型給出直接矛盾的結論（雙盲匿名 vs. 單盲），且雙方都承認證據不夠扎實（現有為 Wiley 預設推定「varies by journal」；WO2 為 Wikipedia 條目推定、官方頁面因付費牆無法核實）。屬實質分歧而非細節補充，需人工查核期刊官方 Author Guidelines 頁以定案，不應由本次比對自動擇一覆蓋。

---

## Journal of Experimental Psychology: Human Perception and Performance
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-experimental-psychology-human-perception-and-performance.md`

- **Metrics > Review Cycle Time(四列:first decision / first review / acceptance total / publication)**
  - Existing: 四列皆為 *(fill manually)* 佔位符
  - WO2 finding: experiential.review_time_months: "1.8 個月(首輪審查/總處理時間中位數估計);立即拒稿(desk reject)平均決定時間約 1 天;平均審查輪數 1.0 輪"(來源 SciRev,樣本僅 3 筆評價)
  - Why flagged: WO2 自身用語已表明 1.8 個月這個數字究竟對應「首輪審查」還是「總處理時間」並不確定,無法可靠對應到表格四列中的哪一列;desk reject 的 1 天則是表格中沒有對應列的桌拒決定時間,不宜硬塞進任何一列。且來源樣本量僅 3 筆評價,信心度低。基於『不確定就不動』原則,不逕自填入,留待人工判斷是否採用及填入哪一列並加註樣本量警語。

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 4
  - WO2 finding: 3(WO2 ai_policy.leniency_1_5)
  - Why flagged: 現有條目與 WO2 對政策文字描述(事後揭露制、無需事前申請許可、AI 不得列為作者)高度一致,但寬容度評分不同(現有 4 分 vs WO2 3 分)。此為主觀評分差異而非單純遺漏或明顯錯誤,依規則不應逕自覆蓋既有評分,故列為衝突留待人工複核是否調整。

---

## Journal of Experimental Social Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-experimental-social-psychology.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (per Elsevier default — varies by journal; some are double-blind)
  - WO2 finding: Double-anonymized (double-blind) peer review; minimum 2 independent reviewers after editor suitability screen; one formal appeal allowed per submission (source: ScienceDirect guide-for-authors, 'Peer review' / 'Double anonymized peer review' section, browser-rendered 2026-07-13)
  - Why flagged: 現有欄位是套用 Elsevier 集團「預設值」的猜測性描述(註明「varies by journal」),而 WO2 直接引用該刊自己的 Guide for Authors,明確指出 JESP 採雙盲審稿並附帶審稿人數與申訴機制細節。這是實質矛盾(single-blind default vs. 確認為 double-blind),非單純補充細節,依規則應留待人工核實後決定是否覆蓋,不可逕行覆寫既有欄位。

- **Metrics > Review Cycle Time (Time to first decision / Time to acceptance total)**
  - Existing: *(fill manually)*
  - WO2 finding: experiential.review_time_months: SciRev 顯示首輪審稿(至第一次決定)約 2.1 個月,接受稿件總處理時間約 2.1 個月(僅單筆近期樣本);另有知乎文章聲稱平均 5-7 個月,兩來源差異大且知乎非一手審稿人證言,signal_quality 僅 2/5
  - Why flagged: 此欄位雖為空白(placeholder),但 WO2 自身在 blanks 與內文中明確表示『兩來源數字差異大,未能交叉驗證,故僅並陳不取單一數字』,訊號品質僅 2/5 且樣本數為 1。這不構成『有把握的、有來源根據的答案』,若逕行填入會把一組自承不可靠、互相矛盾的數字寫進期刊的正式指標表,有誤導風險,故不予直接編輯,建議人工進一步查證(如 Editorial Manager 公開統計或作者投稿經驗)後再決定是否填入。

- **Policies > AI Policy > Summary (reviewer/editor AI use scope)**
  - Existing: Reviewers/editors not permitted to use AI during peer review.
  - WO2 finding: 審稿人/編輯明確被禁止把未發表稿件上傳到生成式 AI 工具,僅能用 AI 輔助潤飾審稿意見文字或做背景文獻搜尋。(source: ScienceDirect guide-for-authors, 'Declaration of generative AI use' 與 elsevier.com generative-ai-policies-for-journals)
  - Why flagged: 現有摘要是「審稿全程禁用 AI」的一刀切描述,WO2 找到的是更細緻的規則:禁止上傳未發表稿件,但允許用 AI 潤飾審稿意見文字/做背景搜尋。這屬於範圍上的實質差異(禁止 vs. 有限度允許),不是單純補充細節,依規則此欄位本已有實質內容(非佔位符)不可逕行編輯,故列為衝突交由人工核實後決定是否修訂措辭。

---

## Journal of Social and Clinical Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-social-and-clinical-psychology.md`

- **Policies > AI Policy (Explicit permission gate? / Leniency / Summary)**
  - Existing: Explicit permission gate? No — disclosure-based; Leniency (1-5): 4; Summary: Follows Guilford Press publisher AI policy: disclosure required; AI cannot be listed as author.
  - WO2 finding: gate: "yes - discourages/restricts use to create article content"; leniency_1_5: 2; summary: Guilford journals currently do not allow AI to be used to create article content, including figures, tables, images, and other materials. (source: guilfordjournals.com/about)
  - Why flagged: 現有欄位已有具體、完整的內容（非佔位符），依規則不可覆蓋；但WO2對同一Guilford發行政策給出實質相反的結論——現有稱『無需明確許可、僅需揭露』且寬容度4，WO2稱『限制/不允許AI產出文章內容（含圖表）』且寬容度僅2。兩者對Guilford AI政策的解讀方向不同，需人工重新核實guilfordjournals.com/about原文以確認何者準確，不宜逕行編輯。

- **Policies > Peer Review > Type**
  - Existing: Double-blind (per Guilford default)
  - WO2 finding: Single-blind by default (author identity visible to reviewers); double-blind available on author request, in which case identifying info is confined to a separate cover page. [WO2自陳：僅透過搜尋引擎快取摘要取得guilfordjournals.com/journal/jscp/authors內容，直接抓取回傳403，未能對照原頁面文字獨立驗證]
  - Why flagged: 現有欄位已有具體內容，非空白/佔位符，依規則不可覆蓋。但WO2發現的審稿類型（預設單盲、雙盲需申請）與現有值（預設雙盲）方向相反，屬實質衝突而非僅補充細節。且WO2自身資料來源可信度存疑（僅快取摘要、非直接驗證），建議人工至期刊官網或作者須知頁面核實實際審稿制度後再決定是否更新，不應由AI逕行覆蓋。

---

## Journal of Research in Personality
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-research-in-personality.md`

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 3 — 現有詞條敘述:「Has journal-specific AI policy? No (follows Elsevier publisher default)」,並將寬容度評為 3。
  - WO2 finding: 2 — WO2 對同一份 Elsevier 通用生成式 AI 政策(作者需揭露 AI 使用、圖像生成禁止、AI 不得列為作者)評為「有條件許可 + 強制揭露」閘門,寬容度給 2。
  - Why flagged: 雙方描述的是同一份 Elsevier 出版社通用政策(非本刊特定),事實描述高度一致,但對同一事實給出的寬容度分數不同(3 vs 2),屬於主觀評分層級的實質分歧而非單純補充細節,故不逕自覆蓋,留待人工比較兩者評分依據後定奪。

---

## Journal of Personality and Social Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journal-of-personality-and-social-psychology.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per APA default)
  - WO2 finding: Masked (blind) review — manuscript is anonymized so reviewers do not see author identity; cover letter carries author names. Rejection by one section editor counts as rejection by all three sections.
  - Why flagged: 現有內容主張雙向匿名(double-anonymized),但 WO2 描述的是「稿件對審稿人匿名、但 cover letter 附作者姓名」的做法,較接近單向匿名(reviewer-blind,編輯知道作者身分),兩者對審查匿名程度的描述實質不同,需人工對照 APA/JPSP 投稿指南核實,不宜逕行覆蓋既有具體內容。

- **Policies > AI Policy > Leniency (1-5) / Explicit permission gate**
  - Existing: Leniency (1-5): 4; Explicit permission gate: No — disclosure-based
  - WO2 finding: Leniency (1-5): 3; gate: conditional
  - Why flagged: 雙方對同一份 APA 揭露式 AI 政策的寬鬆程度評分不同(4 vs 3),且對「是否有守門機制」的定性也不同(現有稱「無守門、僅需揭露」,WO2 稱「有條件式守門」)。底層事實(需揭露、AI 不得列為作者)一致,但評分與定性有實質分歧,屬人工判斷範疇,不逕行覆蓋既有已填寫內容。

---

## Memory & Cognition
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\memory-and-cognition.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (typical journal default; check publisher)
  - WO2 finding: Peer-reviewed; commonly described as double-blind in secondary sources (journal-comparison sites), but WO2 explicitly flags this as NOT confirmed against the journal's own submission-guidelines page (which was inaccessible behind an IdP login redirect).
  - Why flagged: 既有條目與 WO2 對「單盲 vs 雙盲」的說法直接矛盾，且 WO2 自身也承認未能對照官方投稿頁面驗證，屬低信度二手來源，需要人工查證後才能決定是否更正，不宜自動覆蓋。

- **Metrics > Acceptance Rate**
  - Existing: *(community estimate)*
  - WO2 finding: SciRev 將本刊評為審稿意見/接受難度 5.0/5.0「非常困難」，但整體稿件處理品質評為 3.0/5.0；樣本僅 3 筆送審紀錄，統計信心極低（未提供實際接受率百分比）。
  - Why flagged: 此為主觀難度評分而非具體接受率數字，不足以直接填入 Acceptance Rate 儲存格（樣本量過小、非百分比），但作為人工複核時的參考訊號值得記錄。

---

## Multimodal Technologies and Interaction
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\multimodal-technologies-and-interaction.md`

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 4
  - WO2 finding: 3
  - Why flagged: 兩者皆同意此為MDPI出版社統一的揭露式(disclosure-based)政策而非期刊專屬條款，但對寬鬆度評分不同（現有4分 vs WO2 3分），屬同一政策的不同主觀評級，非單純補充細節，建議人工複核後擇一或調和。

---

## Neuropsychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\cognitive-science\neuropsychology.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per APA default)
  - WO2 finding: masked (single-anonymous) review
  - Why flagged: 既有內容是依「APA 預設慣例」推論而來的假設值,並非針對本刊逐條查證;WO2 則引用本刊官方投稿頁(apa.org/pubs/journals/neu/submit)得出「單盲(masked)」的結論,兩者直接矛盾(雙盲 vs 單盲),需要人工去官方投稿頁核實,不宜自動覆蓋既有值。

- **Policies > AI Policy > Explicit permission gate? / Leniency**
  - Existing: Explicit permission gate?: No — disclosure-based; Leniency (1-5): 4
  - WO2 finding: gate: conditional; leniency_1_5: 3
  - Why flagged: 兩者依據同一份 APA generative-AI 政策頁面,但對「是否為許可關卡」與寬鬆程度的判讀不同(既有版本判定為純揭露制、寬鬆度4;WO2 判定為有條件關卡、寬鬆度3),屬於實質評分分歧,而非單純補充細節,建議人工複核後決定是否調整既有評分。WO2 的完整政策摘要文字已於本檔案 Soft Metadata > AI-Research Notes 段落收錄可供對照。

---

## New Ideas in Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\new-ideas-in-psychology.md`

- **Policies > Peer Review > Type**
  - Existing: *(per Elsevier default — pending verification; commonly single-blind in psychology, but recheck)*
  - WO2 finding: Double anonymized (double-blind); editor screens first, then min. one independent expert reviewer (source: https://www.sciencedirect.com/journal/new-ideas-in-psychology/publish/guide-for-authors)
  - Why flagged: 既有欄位雖標注 pending verification,但已附帶具體傾向性陳述(『commonly single-blind』),不符合逐字比對的『純占位符』定義,故不直接覆蓋。WO2 從同一份 Guide for Authors 獨立研究得出明確相反結論(double-blind),兩者直接矛盾,需人工回查原始 Guide for Authors 頁面以確認何者正確,再手動更新。

- **Policies > AI Policy > Has journal-specific AI policy?**
  - Existing: Yes — journal-specific image restriction beyond Elsevier default(完整 Summary 描述 AI 生成/輔助影像除非 AI 本身即研究方法,否則禁止使用)
  - WO2 finding: 採 Elsevier 出版社通用政策(非期刊特化)。WO2 blanks 備註:『查無期刊層級 AI 政策;僅能引用 Elsevier 出版社通用政策,故 policy 層 signal_quality 偏低』,signal_quality=2
  - Why flagged: 既有條目已有具體內容(非占位符),依規不直接覆蓋。但 WO2 本次獨立研究明確表示『查無期刊層級 AI 政策』,與既有條目主張『NIP 有超出 Elsevier 預設的期刊特化影像限制政策』直接矛盾。雖然 WO2 自評此欄 signal_quality 偏低(2/5),但屬直接對立主張,建議人工重新核對 Guide for Authors 頁面上是否確實存在該影像限制條款,而非以本次較低信度的 WO2 結果取代既有內容。

---

## NeuroImage
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\cognitive-science\neuroimage.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (typical journal default; check publisher)
  - WO2 finding: Double-anonymized (double-blind) peer review, minimum two independent reviewers (source: sciencedirect.com guide-for-authors search-cache extract; direct fetch 403, corroborated via sibling journal NeuroImage: Stroke guide-for-authors snippet)
  - Why flagged: 現有值為家族通則猜測(single-blind, 註明「check publisher」),WO2 則引用(間接、快取版)guide-for-authors 具體指出 double-anonymized。兩者屬實質矛盾（單盲 vs 雙盲），且 WO2 來源本身為快取/間接推論非直接 fetch 成功，可信度中等，故不逕行覆蓋，留供人工查證 sciencedirect.com/journal/neuroimage/publish/guide-for-authors 現行版本以確認。

- **Soft Metadata > Reviewer Pool Characteristics / Sensitive Topics (subjective, out of scope for direct edit)**
  - Existing: Reviewer competence variance: Low-Medium; 未載明國際/在地作者接受度差異之經驗性描述
  - WO2 finding: experiential.reviewer_culture: SciRev 一則回報稱其中一位審稿人「態度不佳、不熟悉技術細節」；另一則稱期刊維持「極高拒絕率」；小木虫使用者反映對非中國大陸機構之國際作者接受度較高、母語作者被拒率提及較少（單一站台個人化陳述，未交叉驗證）
  - Why flagged: 此為觸及主觀評估區塊(Reviewer Pool Characteristics/Sensitive Topics)的補充性經驗發現，非本輪可直接編輯範圍；且此內容已於 2026-07-13 由前一輪 WO2 patch 完整收錄於 Soft Metadata > AI-Research Notes（experiential finding 段落），故僅供人工複核是否需要進一步upgrade 至 Tier 1 主體評估區塊，不建議在本輪重複處理。

---

## Personality and Social Psychology Review
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\personality-and-social-psychology-review.md`

- **Policies > AI Policy > Leniency (1-5) 與 Explicit permission gate**
  - Existing: Explicit permission gate: 'No — disclosure-based'; Leniency: 4
  - WO2 finding: gate: 'conditional'; leniency_1_5: 3
  - Why flagged: 既有欄位已有具體內容（非佔位符），依規則不可直接覆蓋。但WO2對同一政策給出不同的寬嚴度評分（3 vs 現有的4）與稍不同的gate描述（conditional vs disclosure-based/No），屬於程度上的分歧，留供人工複核判斷是否需調整既有評分，而非逕自覆蓋。

---

## Personality and Individual Differences
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\personality-and-individual-differences.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (per Elsevier default — varies by journal; some are double-blind)
  - WO2 finding: double anonymized(雙盲),依據該刊官方 Guide for Authors: https://www.sciencedirect.com/journal/personality-and-individual-differences/publish/guide-for-authors
  - Why flagged: 現有值是 Elsevier 通用預設的模糊猜測(單盲,且註明因刊而異、也可能雙盲),WO2 則引用本刊官方 Guide for Authors 明確指出採雙盲審查制度,兩者實質矛盾。WO2 的 preprint 欄位論述(『採雙盲審查,最終決定前不應公開為 preprint』)也是建立在雙盲的前提上,與現有 Peer Review Type 欄位不一致,建議人工核對官方 Guide for Authors 頁面以確認正確審查類型,而非直接覆蓋。

- **Metrics > Acceptance Rate / Desk Rejection Rate**
  - Existing: *(fill manually if known)* (both rows)
  - WO2 finding: WO2 本身亦未取得官方公開數字:acceptance rate 於 SciRev/Editage 皆標示 n/a;desk-reject 僅有 fabiaoji 11 筆自述小樣本(4/11≈36%),WO2 report 明確將此列為 blanks、註明樣本過小不具代表性。
  - Why flagged: 雖然欄位目前是 placeholder,但 WO2 本身也承認沒有可靠的第一手公開數字,只有極小樣本的社群自述,故不建議直接填入具體百分比,列為 conflict 供人工判斷是否要以『小樣本估計,僅供參考』的方式加註,而非當作確定數字填入。

---

## Personality and Social Psychology Bulletin
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\personality-and-social-psychology-bulletin.md`

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 4
  - WO2 finding: 3(signal_quality 2/5,基於 Sage 集團通用政策文字判讀，非期刊專屬頁面)
  - Why flagged: 兩者對同一 1-5 寬鬆度評分給出不同數字(既有 4 分 vs WO2 3 分),屬於實質分歧而非單純補充細節,且雙方都是基於同一份 Sage 集團 AI 政策文字做出的主觀評分差異，需要人工判斷該用哪個分數或如何調和;WO2 的 gate 描述為「conditional」，與既有「No — disclosure-based」措辭雖大致同義但角度不同，一併附上供覆核。

---

## Nature Machine Intelligence
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\nature-machine-intelligence.md`

- **positioning.methods_welcome (touches Methodological Preferences / Best Suited For — out of scope subjective sections)**
  - Existing: Soft Metadata > Methodological Preferences table and Strategic Notes > Best Suited For list already describe ML/algorithm development, AI-in-science, foundation models, AI ethics/safety, RL as core strengths
  - WO2 finding: ["machine learning", "robotics", "AI 對其他科學領域/社會產業的影響(如科學發現、醫療診斷、永續城市與交通、農業)"]
  - Why flagged: WO2 對「目前實際接受什麼題材」的補充發現(來自 aims & scope 摘要),涉及範圍外的主觀章節(Methodological Preferences / Best Suited For),依規則不可直接編輯。內容大致與現有 Tier 2 敘述一致(尤其『AI in science』『跨領域應用』),但新增了『robotics』與較具體的產業別(醫療診斷、永續城市與交通、農業)未見於現有條目,建議人工核實後決定是否補充至 Best Suited For。

---

## Personal and Ubiquitous Computing
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\personal-and-ubiquitous-computing.md`

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 4
  - WO2 finding: 2 (WO2 ai_policy.leniency_1_5, signal_quality 2/5)
  - Why flagged: 同一個「寬鬆度」量表在既有條目與 WO2 給出明顯不同的數值(4 對 2),兩者描述的政策內容本身(揭露即可、非全面許可也非全面禁止)其實一致,只是主觀寬鬆度評分不同,屬於需要人工重新校準的實質分歧,不應由此次自動合併逕自二選一覆蓋。

- **Soft Metadata > Framing Requirements (out of scope,僅供人工參考)**
  - Existing: Mandatory framing? Yes (soft) — 需展現 personal/ubiquitous computing 貢獻(mobile、wearable、IoT、smart environments),純 HCI 或純 IoT 工程會被redirect。
  - WO2 finding: positioning.framing_required: 期刊官方 aims & scope 明文要求所有文章須具備強烈 human-centred、使用者或設計觀點,須透過設計研究/參與式設計/民族誌方法/負責任研究方法/田野使用者研究呈現;純技術/演算法論文若無使用者研究成分可能不符範疇。
  - Why flagged: WO2 的措辭把強制框架的重點放在「必須有使用者研究方法論」而非既有條目強調的「必須是行動/穿戴/IoT主題」,兩者角度不同、可能互補也可能需要調整既有描述,但屬於 Soft Metadata 主觀子區塊(範圍外),依規則僅記錄供人工判斷,不逕自編輯。

- **Soft Metadata > Methodological Preferences (out of scope,僅供人工參考)**
  - Existing: 現有方法接受度表未列出 LLM/生成式 AI 分析穿戴式或行動感測資料 這類方法。
  - WO2 finding: positioning.methods_welcome 列出 "LLM/生成式 AI 應用於穿戴式與行動感測資料分析" 為期刊近期(2024-2026)明顯接受的新興方法之一,並在 accepts_now 中舉了具體例子(LLM 驅動活動辨識、IoT 任務推理等)。
  - Why flagged: 屬於期刊近期投稿趨勢的補充觀察,可能值得未來人工把「LLM 輔助感測資料分析」新增進方法偏好表或 Best Suited For,但這屬於範圍外的主觀評估子區塊,故僅記錄不逕自編輯。

---

## Qualitative Inquiry
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\qualitative-methods\qualitative-inquiry.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per Sage default)
  - WO2 finding: open peer review（非雙盲/雙匿名）— sourced to https://journals.sagepub.com/home/QIX
  - Why flagged: 既有內容與 WO2 發現直接矛盾（雙盲 vs. 非雙盲的開放式同儕審查），非單純細節補充，屬實質分歧，不應由自動化流程逕自覆蓋，需人工查證該刊實際審稿制度（Sage 集團預設 vs. 該刊可能的例外）。

- **Policies > AI Policy > Explicit permission gate? / Leniency (1-5)**
  - Existing: Explicit permission gate?: No — disclosure-based; Leniency: 4
  - WO2 finding: gate: "conditional"; leniency_1_5: 3
  - Why flagged: 兩者對政策本質的描述有出入：既有版本主張『無事前許可門檻，僅需揭露』，WO2 標記為『conditional（有條件式門檻）』，寬容度評分也不同（4 vs 3）。雖然底層 summary 文字幾乎相同（Sage 集團通用政策），但 gate 有無的判斷與寬容度分數不一致，屬於評分/判斷層級的分歧而非事實補充，故列為衝突交人工判斷，不逕自修改既有表格。

---

## Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\acm-pacm-imwut.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (typical journal default; check publisher policy)
  - WO2 finding: AE-triage model: submissions may receive Desk Rejection by Editors (no reviewers assigned; scope/formatting issues), Early Rejection by Associate Editors (after AE's own initial read, no external reviewers), or proceed to full external review (SciRev data shows ~4 review reports per first round) with major/minor revision cycles. Source: https://dl.acm.org/journal/imwut/reviewers
  - Why flagged: 既有欄位斷言的是『盲審制度類型』（single-blind，且僅為家族慣例推測、未附來源），WO2 找到的則是有來源、具體描述『審稿流程/分級機制』（桌拒／AE 初審拒稿／外審），兩者談的是不同面向、無法直接判定孰是孰非，也不構成單純的『補充細節』可安全覆蓋既有內容——需人工判斷是否要重寫此欄或另闢一列收錄 AE 分級流程，故列為衝突待決，不逕行編輯。

- **Subject Density / Soft Metadata > Methodological Preferences（現況接受主題與方法）**
  - Existing: Soft Metadata 目前為 Tier 2 家族推測值（如 Quantitative/Qualitative/Mixed methods 各給 3-5 分），Subject Density 的 Top Topics 亦為 community estimate。
  - WO2 finding: positioning.methods_welcome 列出：mobile systems and infrastructure; wearable technologies and new sensing hardware; intelligent/smart environments and IoT; user experience studies and HCI evaluation; new methodologies/tools/theories/models for ubiquitous computing; societal impact studies of pervasive computing。（signal_quality 2/5，accepts_now 因 403 無法用實際近年篇名驗證，僅基於期刊自述 scope）
  - Why flagged: 此為 positioning／方法偏好類補充發現，觸及本次任務明列為 out-of-scope 的 Soft Metadata 主觀子章節（Methodological Preferences）與 Subject Density，依規則僅供人工參考，不逕行編輯既有主觀評分或主題密度表。

---

## Self and Identity
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\self-and-identity.md`

- **Policies > Peer Review > Type**
  - Existing: *(per T&F default — pending verification; commonly double-anonymized)*
  - WO2 finding: Single-anonymized (single-blind) peer review; initial Editor screening then refereeing by at least two independent expert referees; ScholarOne Manuscripts submission system. (source: https://www.tandfonline.com/journals/psai20/about-this-journal)
  - Why flagged: 此欄位雖以括號＋斜體呈現，但內含具體猜測「commonly double-anonymized」，並非精確比對表中允許的空白樣板字串，因此依規則不算 placeholder、不可逕行覆蓋。然而 WO2 提供的是相反且更具體、有來源佐證的結論（single-anonymized，附審稿流程與系統細節），與既有猜測直接矛盾，需人工查證後才能決定採用哪一版本，故列為衝突而非直接填入。

- **Policies > AI Policy (Leniency 1-5 與 Summary)**
  - Existing: Leniency 4 (disclosure-based; AI cannot be listed as author); Summary: 泛用 T&F 政策、揭露即可、建議聯繫編輯部確認最新版本
  - WO2 finding: Leniency 3 (gate: conditional); Summary 更詳細：允許構想發想/語言潤飾/文獻檢索分類/程式協助，但明確禁止用 AI 生成或操作研究資料、圖像或圖表，且需在方法或致謝中揭露工具名稱、版本、用途與使用方式
  - Why flagged: 既有 AI Policy 各列已有實質內容（非空白樣板），依規則不可逕改；但 WO2 的寬容度評分（3）與既有評分（4）不同，且 WO2 補充了既有摘要未明確提及的『禁止用於資料/圖像操作』限制，屬實質分歧而非單純補充細節，故列為衝突供人工複核。附註：檔案中『AI-Research Notes (WO2 supplement)』小節已將此 WO2 全文原樣附上作為補充研究紀錄，此衝突僅提醒不要據此逕自覆蓋主表格中的 Leniency/Summary 儲存格。

---

## Psychology and Aging
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\psychology-and-aging.md`

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 4
  - WO2 finding: 3
  - Why flagged: 既有值與 WO2 值為同一量表下的不同具體數字(4 vs 3),屬於實質分歧而非單純補充細節,依規則不可逕行覆蓋,交由人工判斷採信哪個評分較準確(兩者引用的都是同一份 APA publisher-wide AI 政策,只是評分者主觀寬鬆度判斷不同)。

---

## Qualitative Research in Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\qualitative-methods\qualitative-research-in-psychology.md`

- **Policies > Peer Review > Type**
  - Existing: *(per T&F default — pending verification; commonly double-anonymized)*
  - WO2 finding: Double-anonymized (double-blind) with initial editor screening — source: https://www.tandfonline.com/journals/uqrp20/about-this-journal
  - Why flagged: 現有欄位已有具體內容(non-placeholder,含 pending verification 註記),依規則不可自動覆蓋;但 WO2 提供期刊專屬頁面來源,確認 double-anonymized 並補充 initial editor screening 細節,可解除現有的『pending verification』懸念,建議人工核實後再決定是否更新措辭。

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 4 (disclosure-based; AI cannot be listed as author)
  - WO2 finding: 3 (conditional/disclosure-based; 另指出同儕審查者不得用生成式 AI 分析/摘要投稿稿件,亦不得將未發表稿件上傳至 AI 工具)
  - Why flagged: AI Policy 整節已有實質內容,非裸佔位符,依規則不列入可編輯範圍;但 WO2 給出的 leniency 數值(3)與現有(4)不同,且補充了現有 Summary 未提及的『審查者禁用 AI』限制,建議人工複核是否需調整評分或補述。

---

## Proceedings of the ACM on Human-Computer Interaction — CSCW (PACM CSCW)
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\hci\acm-pacm-cscw.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (typical journal default; check publisher policy)
  - WO2 finding: Double-blind, journal-style multi-round review (revise-and-resubmit); varies by track (CSCW/EICS/MobileHCI/ISS/CHI PLAY each have their own track and cycle). Source: https://cscw.acm.org/2026/blog/reviewprocess.html
  - Why flagged: 現有值為家族通則推測(single-blind),WO2 從 CSCW 官方審稿流程頁直接查得為 double-blind(且明確要求投稿完全匿名化,這點在現有檔案 AI Policy 摘要裡其實也提到『CSCW track 額外要求投稿完全匿名化(雙盲審)』,與此處 Type 欄位的 single-blind 描述互相矛盾)。這是實質性衝突而非單純補細節,需人工核實後再決定是否覆蓋。

- **Metrics > Acceptance Rate**
  - Existing: *(community estimate; varies by year)*
  - WO2 finding: CSCW 主軌歷年約 25-36%(2013-2019,openaccept.org 統計);MobileHCI 2025 軌道 27.2%;ISS/ETRA 等特刊約 30% 上下 —— WO2 自行註明『未涵蓋近年 rolling 制改版後數據』
  - Why flagged: 此欄位現有文字雖為模糊估計但已有『varies by year』的實質性措辭,不完全符合空白格判定;且 WO2 提供的具體數字本身明確標註是 2013-2019 的舊制數據、未涵蓋 CSCW 近年改為 rolling review 制後的現況,若直接填入恐誤導讀者以為是當前接受率。建議人工評估是否要以『歷史區間僅供參考』的方式呈現,而非由此次比對逕自覆蓋。

---

## Social Cognitive and Affective Neuroscience
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\social-cognitive-and-affective-neuroscience.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per Oxford UP default — varies by journal)
  - WO2 finding: single-anonymized (single-blind): 作者身分對編輯與審稿人公開,審稿人身分僅編輯知悉,對作者匿名。通常送2位審稿人。(source: https://academic.oup.com/scan/pages/author-guidelines)
  - Why flagged: 現存值是套用 Oxford UP 集團預設值的推測(且自註「varies by journal」),WO2 則引用該刊自己的 author-guidelines 頁面得出相反結論(single-anonymized)。兩者實質矛盾,且 WO2 來源較具期刊專屬性,但既有欄位已有具體內容,不應直接覆蓋,需人工核實。

- **Policies > AI Policy (整組:Has journal-specific AI policy? / Explicit permission gate? / Leniency / Summary / Source URL)**
  - Existing: Has journal-specific AI policy?: No (follows Oxford UP publisher default); gate: No — disclosure-based; leniency: 4; source: https://academic.oup.com/journals/pages/authors (集團泛用頁)
  - WO2 finding: gate: conditional; leniency: 3; summary 指出此為 SCAN 期刊專屬 author-guidelines 頁面上的具體落地政策(非泛用集團頁),要求於 cover letter 及 Methods/Acknowledgements 揭露生成式AI使用,AI 不得列為作者,期刊會篩查作者名單;source: https://academic.oup.com/scan/pages/author-guidelines
  - Why flagged: 現存條目主張『沒有期刊專屬 AI 政策,僅套用集團預設』,WO2 卻指出有一個 SCAN 專屬的 author-guidelines 頁面具體規範此政策,且來源 URL、leniency 分數(3 vs 4)、gate 描述(conditional vs disclosure-based/No)皆有出入。屬於既有欄位已有實質內容下的資訊衝突,非佔位符,故不直接覆蓋,留供人工比對兩份來源頁面後裁決。

---

## Qualitative Health Research
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\qualitative-methods\qualitative-health-research.md`

- **Policies > AI Policy > Has journal-specific AI policy?**
  - Existing: No (follows SAGE publisher default)
  - WO2 finding: QHR 投稿須知(author-instructions/qhr)在 SAGE 集團政策之外,具體要求:凡使用生成式AI協助構思、研究設計、資料生成、分析協助或呈現研究發現等『構成質性研究要素』的活動,須在正文標示並在 Acknowledgements 揭露技術名稱、存取時間與用途。
  - Why flagged: 現有欄位斷言『無期刊專屬 AI 政策、僅循 SAGE 預設』,但 WO2 從 QHR 官方投稿須知中找到期刊層級具體化的揭露規則(範圍涵蓋研究設計/分析協助等),這是『無 vs 有』的實質分歧而非僅補充細節,依規則不逕行覆蓋既有欄位,留待人工核實後決定是否升級此欄位陳述。

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 4
  - WO2 finding: 3
  - Why flagged: 兩份資料對寬容度評分不同(現有 4 分 vs WO2 3 分),屬於數值上的實質分歧;且 WO2 此欄位 signal_quality 僅 3/5,證據強度有限,故不逕行覆蓋,列為衝突供人工裁決。

---

## Social and Personality Psychology Compass
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\social-and-personality-psychology-compass.md`

- **Strategic Notes > Hard Blockers / Framing Requirements（範疇外，僅供人工參考）**
  - Existing: Hard Blockers 列「Original empirical work」為阻擋項；Framing Requirements 說明「Empirical work redirected to JPSP / PSPB / J Personality」
  - WO2 finding: positioning.accepts_now：依 2025-2026 搜尋結果，期刊近期已開放『簡潔實徵報告』(concise empirical reports ≤5000字)、資料驅動理論發展、重複驗證研究、期中發現等，並非純綜述期刊
  - Why flagged: 此為觸及 Strategic Notes/Framing Requirements（範疇外的主觀章節）的定位性發現，依規則不可直接編輯，僅供人工複核；註：此發現已由先前的自動化流程記錄於本檔案 Soft Metadata > 'AI-Research Notes (WO2 supplement)' 區塊作為補充說明，但尚未反映於 Hard Blockers / Framing Requirements 正文，建議維護者評估是否需要更新既有措辭以符合期刊近期實際收稿範圍。

---

## The American Journal of Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\american-journal-of-psychology.md`

- **Policies > AI Policy (Has journal-specific AI policy? / Explicit permission gate? / Leniency / Summary)**
  - Existing: Has journal-specific AI policy?: No (follows UIP publisher default); Explicit permission gate?: No — disclosure-based; Leniency (1-5): 4; Summary: "Follows University of Illinois Press publisher AI policy: disclosure required; AI cannot be listed as author."
  - WO2 finding: gate: null, leniency_1_5: null, signal_quality: 0. Summary: "查無此刊或其出版社(University of Illinois Press／Scholarly Publishing Collective／Scholastica投稿系統)公開發布的AI/生成式AI使用政策頁面。UI Press官方投稿頁與Scholastica「For Authors」頁均只列出APA第7版格式、雙盲審稿、題頁匿名化等要求,未提及AI/ChatGPT使用規範。"
  - Why flagged: 現有條目斷言存在一個具體的「UIP 出版社預設 AI 政策」(揭露即可、AI 不得列為作者)並給出寬容度 4 分；但 WO2 的獨立研究通盤查閱 UIP 官方投稿頁與 Scholastica 投稿系統「For Authors」頁後，明確表示查無任何期刊層級或出版社層級公開發布的 AI/生成式 AI 政策頁面，因此 WO2 將 gate 與 leniency 都留白(null)、signal_quality 標為 0。這不只是「更多細節」，而是對「該政策是否確實存在且可被驗證」的實質分歧，需要人工重新查證現有條目中「UIP 預設政策」說法的原始來源，而非由本次比對自動判定取捨。

---

## Social Psychology Quarterly
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\social-psychology-quarterly.md`

- **Policies > AI Policy (Explicit permission gate? / Leniency)**
  - Existing: Explicit permission gate?: "No — disclosure-based"; Leniency (1-5): 4
  - WO2 finding: WO2 raw JSON 結構化欄位: gate="conditional", leniency_1_5=3 —— 但 WO2 自己的敘述摘要文字寫的是「未強制事前許可審批 (no pre-approval gate)」,與其自身 gate=conditional 標記自相矛盾
  - Why flagged: 既有欄位已有具體真實內容(非 placeholder),依規則不應覆蓋;但 WO2 原始 JSON 的結構化分類(gate/leniency)與既有檔案內容不一致,且與 WO2 自己的敘述摘要內部矛盾,可能是 WO2 draft 資料品質問題(該 pass 標示 signal_quality=2/5),建議人工複核 AI Policy 的 gate/leniency 分類是否需要調整,不宜自動修改。

---

## The Clinical Neuropsychologist
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\cognitive-science\clinical-neuropsychologist.md`

- **Policies > AI Policy > Has journal-specific AI policy?**
  - Existing: Yes (publisher default + may have journal overlay)
  - WO2 finding: 未見期刊專屬 AI 政策頁,僅查得出版社(Taylor & Francis)集團層級政策;找不到 TCN 期刊本身的專屬 AI 政策頁或投稿須知中的 AI 段落(且原始政策頁 WebFetch 被 403 擋下,轉引自 WebSearch 摘要,非逐字核對)
  - Why flagged: 現有條目暗示可能有期刊層級加疊政策('may have journal overlay'),但 WO2 實際查證後明確表示找不到期刊專屬頁面,僅有集團通用政策 —— 屬於實質分歧而非單純補充細節,且 WO2 本身信度已打折(signal_quality 2/5,無法直接讀取原文),需人工判斷是否降級現有描述。

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 3-4
  - WO2 finding: 2 (conditional gate — 允許使用但須揭露,非全面禁止但也非開放)
  - Why flagged: 數值有明顯落差(3-4 vs 2),屬於實質分歧而非精細化描述;但 WO2 此分數是根據二手 WebSearch 摘要(非直接讀取 T&F 政策原文,404/403 擋下)推估,信度較低(signal_quality 2/5),故不逕行覆蓋現有數值,留待人工比對原始政策文字後裁定。

---

## The Journals of Gerontology: Series B
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\journals-of-gerontology-b-psychological-sciences.md`

- **Metrics > Review Cycle Time (Time to first decision / Time to first review / Time to acceptance (total))**
  - Existing: 三列皆為 *(community estimate)* 佔位符，尚未填入任何實質數字
  - WO2 finding: experiential.review_time_months: 「說法不一：SciRev(n=10 筆回報)第一輪平均 1.7 個月、整體處理至決定平均 3.7 個月；中文期刊聚合站(好期刊/學術之家/letpub)另稱『審稿較慢，約 6-12 週』。兩者量級相近但非同一批樣本，故取範圍呈現而非單一數字。」
  - Why flagged: 此為有來源(SciRev n=10)的實質數字，理論上可用來填補三個空白列，但 WO2 只給出「第一輪」與「整體處理至決定」兩個聚合數字，並未明確對應到本表定義的『first decision』『first review』『acceptance total』三個具體階段——若由我自行猜測對應關係並填入特定列，屬於過度詮釋原始資料（WO2 本身也註明『說法不一…故取範圍呈現而非單一數字』，顯示其對精確歸類沒有把握）。建議交由人工判斷這兩個數字應對應哪一列（或以範圍/附註形式呈現），而非由此次 patch 逕行分列填入。

---

## Transactions of the Association for Computational Linguistics
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\cognitive-science\transactions-of-acl.md`

- **Policies > Peer Review > Type**
  - Existing: Single-blind (typical journal default; check publisher policy)
  - WO2 finding: Double-anonymized (double-blind) journal-style review with Action Editor system; reviewers submit reviews to an Action Editor who makes 1 of 4 decisions (accept / conditional accept within 2 months / reject-with-R&R in 3-6 months / reject with 1-year moratorium). Source: https://direct.mit.edu/tacl/pages/submission-guidelines
  - Why flagged: 既有內容是 Tier 2 的家族類推猜測（標明「check publisher policy」代表未經查證），而 WO2 直接引用 TACL 官方投稿須知，得出完全相反的結論（single-blind vs double-blind）。屬於實質矛盾而非單純補充細節，需要人工查證官方頁面後再決定是否覆蓋，不可逕行覆蓋。

- **Policies > AI Policy (整節：Has journal-specific policy? / Explicit permission gate? / Source URL)**
  - Existing: Has journal-specific AI policy?: Yes (follows publisher default + may have journal-specific overlay); Explicit permission gate?: No — disclosure-based; Source URL: https://2025.aclweb.org/calls/main_conference_papers/
  - WO2 finding: WO2 查證 transacl.org 的 Submission Guidelines / Editorial Policies 全文後，未找到任何 TACL 期刊專屬的 AI 政策條文；目前適用的是 MIT Press 出版社層級通用政策（direct.mit.edu/journals/pages/publication-ethics）：AI 不得列為作者、使用 AI 產生內容須揭露並由作者負全責。另外，既有欄位的 Source URL 指向的是 2025.aclweb.org 的 ACL『會議』徵稿頁面，並非 TACL『期刊』的政策頁面，兩者範疇不同。
  - Why flagged: 既有 AI Policy 整節已有具體內容（非空白佔位符），依規則不可直接編輯；但 WO2 的查證結果與既有內容存在實質分歧（有無期刊專屬政策）且既有 Source URL 疑似指錯範疇（會議 CFP 頁而非期刊政策頁），建議人工核實並視情況修正 Source URL 與 Summary 措辞。

- **Policies > Preprint Policy > Pre-submission / Under review rows**
  - Existing: Pre-submission: Yes — arXiv / bioRxiv / similar preprint servers permitted by most publishers; Under review: Yes — Most journals permit preprint update; verify journal-specific policy
  - WO2 finding: WO2（引用 https://direct.mit.edu/tacl/pages/submission-guidelines）：preprint 有條件允許，但有嚴格的『匿名窗口』限制——投稿前一個月起到審稿結束為止，不得有非匿名的 preprint／workshop 版本存在；若 preprint 於投稿一個月前即已存在，作者須在 Comments to the Editor 欄位揭露該 preprint 的場地、標題、URL 與日期，且 TACL 投稿本身仍須維持匿名（不可自我引用該 preprint）。
  - Why flagged: 既有兩列都有具體內容（非空白佔位符），依規則不可直接編輯；但 WO2 找到的匿名窗口限制比既有『Yes，多數期刊允許』的簡化敘述嚴格許多，若作者依既有簡化敘述行事可能違反 TACL 實際規定，建議人工核實後決定是否改寫成更精確版本。

- **Soft Metadata > Reviewer Pool Characteristics / Practical Concerns（主觀性補充發現，不可直接編輯）**
  - Existing: Reviewer Pool Characteristics: 'ACL community reviewers... Reviewer competence variance: Medium'; Practical Concerns > Independent scholar friendliness: Medium-High
  - WO2 finding: Ehud Reiter(2023) 第一手經驗：TACL 審稿人皆由 Action Editor 從 Standing Reviewer Team 中手動指派、多為資深研究者（相當 Area Chair 等級），非會議式演算法配對，審稿更嚴謹但也更花時間；知乎社群多數正面評價審稿品質『靠谱/精确/建设性』（僅一則低可信度匿名酸評，未採用）；另有知乎社群指出 TACL 未被中國 CCF 推薦目錄收錄，對部分中國大陸學者的職涯採認度/吸引力較低。
  - Why flagged: 這些是 WO2 針對主觀性欄位（審稿人特質、獨立學者友善度等）的補充實證發現，依規則屬於 Out-of-scope 的 Soft Metadata 主觀性子項，不可直接編輯，僅供人工評估是否納入既有描述（尤其 CCF 未收錄一點對特定讀者群體的職涯考量可能有實質參考價值）。

---

## Universal Access in the Information Society
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\universal-access-in-the-information-society.md`

- **Policies > Peer Review > Type**
  - Existing: Double-anonymized (per Springer default — varies by journal)
  - WO2 finding: single-blind, two-referee (no article accepted without two complete reviews) — source: https://link.springer.com/journal/10209/submission-guidelines
  - Why flagged: 現有條目記載為雙盲(double-anonymized)審稿，WO2 從該刊投稿指南頁面找到的卻是單盲、雙審稿人制度（無兩份完整審稿意見不予接受），兩者對審稿類型的敘述直接矛盾而非僅細節差異，需人工核對投稿指南原文以確認何者為準（可能其中一份資料已過時）。

- **Policies > AI Policy > Explicit permission gate? / Leniency (1-5)**
  - Existing: Explicit permission gate? No — disclosure-based | Leniency (1-5): 4
  - WO2 finding: gate: conditional | leniency_1_5: 3 — 依據 https://www.springernature.com/gp/researchers/ai-policy（出版社通用政策，非本刊專屬頁）
  - Why flagged: 兩者引用同一份 Springer Nature 出版社通用 AI 政策，具體規則描述大致相符（生成內容須揭露、AI生成圖像禁止），但對「是否設有明確許可關卡」的分類結論不同（現有答「No，僅需揭露」；WO2 答「conditional 條件式允許」），寬容度評分也有一分落差(4 vs 3)，屬於對同一政策的不同歸類角度，建議人工比對政策原文統一用語與評分，故不逕自覆寫。

---

## Theory & Psychology
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\theory-and-psychology.md`

- **Metrics > Review Cycle Time > Time to first decision**
  - Existing: ~2-3 months — Per Sage average for the journal
  - WO2 finding: 首輪約 3.1 個月(SciRev,n=2 篇評論)
  - Why flagged: 此欄位已有具體數值(來自 Sage 官方平均),非空白佔位,不應覆蓋。WO2 為獨立來源(SciRev 極小樣本 n=2),數字略高於既有區間上限,屬於不同來源的實質差異,建議人工判斷是否需並列或註記,而非逕行取代。

- **Metrics > Review Cycle Time > Time to acceptance (total)**
  - Existing: *(pending)*
  - WO2 finding: 稿件在審/在編輯處總計約 3.4 個月;平均 2.0 輪審查後定案(SciRev n=2 篇評論)
  - Why flagged: 此欄位確為空白佔位,但 SciRev 的「總審查時間」指標定義是否精確對應本表「Time to acceptance (total)」(而非泛指所有稿件含拒絕之決定時間)並不明確,且樣本僅 n=2、WO2 自評 signal_quality 僅 2/5,信心不足以逕行歸入此特定列,故列為衝突供人工判斷是否採用及如何標注,而非直接填入。

- **Policies > AI Policy > Leniency (1-5)**
  - Existing: 2 (default ban; case-by-case exception)
  - WO2 finding: 3
  - Why flagged: 既有 AI 政策欄位（含 Summary）已有實質內容,並非空白佔位,依規則不可覆蓋。WO2 給出不同的寬容度評分(3 vs 既有 2),且政策描述框架略有出入:WO2 強調 SAGE 三層制(輔助型 AI 免揭露、生成型 AI 需揭露),既有描述側重「預設禁止、個案例外」,兩者並非單純補充細節而是評分/框架上的實質分歧,建議人工複核後決定是否調整評分或補充措辭。

- **Soft Metadata > Methodological Preferences / Framing Requirements（主觀定位類欄位）**
  - Existing: 既有欄位已有具體評分與描述(如 Theoretical/Conceptual 5、Framing Requirements 要求理論貢獻前景化)
  - WO2 finding: WO2 positioning 發現近期(2025-2026, Vol.36)實際刊登主題包含馬克思女性主義對生殖勞動/墮胎禁令之批判、延伸 Ian Hacking「looping effects」概念、Q 方法論哲學再探與評論、女性主義理論;方法偏好列表另含歷史/系譜學分析、批判理論(含女性主義/馬克思主義)等具體範例
  - Why flagged: 依規則,Soft Metadata 的主觀子區塊（含 Methodological Preferences、Framing Requirements）不在可編輯範圍內,即使 WO2 有相關定位發現也只能列為補充參考,交由人工決定是否用具體案例更新既有評分或描述,不宜由本次審閱直接編輯。

- **Policies > Peer Review > Typical R+R rounds（範圍外,但 WO2 恰有相關數據）**
  - Existing: *(pending)*
  - WO2 finding: 平均 2.0 輪審查後定案(SciRev n=2 篇評論)
  - Why flagged: 本次審閱範圍僅限 Peer Review 表格中的 Type 列,Typical R+R rounds 不在授權可編輯範圍內,即便仍為空白且 WO2 恰有對應資料,也不應在本次直接填入,故列為衝突供未來人工決定是否納入(樣本極小 n=2,信心有限)。

---

## Trends in Cognitive Sciences
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\cognitive-science\trends-in-cognitive-sciences.md`

- **Policies > AI Policy > Explicit permission gate?**
  - Existing: No — disclosure-based for text; image generation prohibited
  - WO2 finding: WO2 結構化欄位標記 gate = "conditional"(signal_quality 3/5),但其自然語言 summary 實質描述與既有內容一致(揭露制,非硬性許可關卡)
  - Why flagged: 這是分類欄位的語意粒度落差,不是實質政策內容矛盾——WO2 的敘述文字本身與既有『No』的說明相符,只是其結構化 schema 把『需揭露但不需事先批准』標成 conditional 而非 no。是否要把既有用語從『No』微調為『No / Conditional (disclosure-based, no prior approval required)』以更精確對齊分類語彙,留給人工判斷,不逕行覆蓋。

---

## Phenomenology and the Cognitive Sciences
`P:\MyOpenSource\JournalMatchEvaluator\journal-atlas\skills\journal-atlas\references\journals\psychology\phenomenology-and-the-cognitive-sciences.md`

- **Policies > Peer Review > Type**
  - Existing: *(per Springer default — pending verification; commonly double-anonymized for humanities/philosophy)*
  - WO2 finding: double-blind (single-anonymous is not used; author identity hidden from reviewers)
  - Why flagged: 現有內容含具體猜測文字(非裸占位符),依規則不可直接覆蓋;WO2 給出較確定的說法,建議人工核對 Springer 頁面原文。

- **Policies > AI Policy > Leniency (1-5) / Explicit permission gate**
  - Existing: Explicit permission gate? No — disclosure-based; Leniency (1-5): 4
  - WO2 finding: gate: conditional; leniency_1_5: 3
  - Why flagged: 表格已有完整填答內容,非占位符;WO2 量化評分與既有評分不完全一致,分歧可能只是主觀評分認定差異,建議人工複核。

---
