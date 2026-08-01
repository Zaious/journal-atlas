# Journal Atlas

> 🌐 **Languages**: [English](README.md) | 繁體中文

[![License: CC BY-SA 4.0](https://img.shields.io/badge/Content-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE-CODE)
[![Schema](https://img.shields.io/badge/Schema-v1.3-green.svg)](skills/journal-atlas/TEMPLATE.md)
[![Status](https://img.shields.io/badge/Status-Pre--release%20(seeding)-orange.svg)](#%E7%89%88%E6%9C%AC%E8%88%87%E5%93%81%E8%B3%AA%E5%88%86%E5%B1%A4-tier-system)

### ▶ [立刻試用 — journal-atlas.chroniclecore.com](https://journal-atlas.chroniclecore.com)

貼上摘要，拿到帶引註的推薦。不用註冊、不用安裝。跑的是跟下面那個 skill
完全相同的知識庫與評分程式碼。

**一個由社群維護、為 AI 而生的學術期刊適配性知識庫。**

Journal Atlas 補上了 Impact Factor 與 Scimago 這類書目計量工具無法觸及的東西：學術期刊的**軟性元資料（soft metadata）**——審稿人文化、framing 期待、敏感主題接受度、AI 政策細節、方法論偏好、拒稿後備策略。所有內容封裝為一個 Claude Agent Skill，可跨 Claude Code、Claude Desktop、ChatGPT 安裝。

> **狀態（2026-07）：Pre-release。** 399 個種子 entries：379 篇期刊跨 9 個領域
> （新增 `philosophy/`）+ 20 個會議跨 4 個子領域（HCI / ML / NLP / Data Mining）。
> 品質分層：**11 Tier 1**（有實證後盾）· **152 Tier 2**（社群推估）·
> **236 AI-Researched**（v2 覆蓋優先轉向、逐刊 AI 研究並附 signal_quality）· **0 Skeleton**。
> Schema **v1.3** — 新增 `Venue type` 欄位 + `Conference Specifics` 區塊。
> 另外 8 個 Society Registry entries（`references/societies/`，schema `society-v1`）
> 涵蓋 ACM SIGCHI / SIGACCESS / ACL / APS / APA / Cell Press / Nature Portfolio / PLOS。
> 見 [版本與品質分層](#%E7%89%88%E6%9C%AC%E8%88%87%E5%93%81%E8%B3%AA%E5%88%86%E5%B1%A4-tier-system) 與 [SEED_DATA_QUALITY.md](SEED_DATA_QUALITY.md)。

---

## 目錄

- [快速開始](#%E5%BF%AB%E9%80%9F%E9%96%8B%E5%A7%8B)
- [安裝方式](#%E5%AE%89%E8%A3%9D%E6%96%B9%E5%BC%8F)
- [Skills 總覽](#skills-%E7%B8%BD%E8%A6%BD)
- [Slash Commands](#slash-commands)
- [工作流範例](#%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%AF%84%E4%BE%8B)
- [涵蓋範圍與收錄現況](#%e6%b6%b5%e8%93%8b%e7%af%84%e5%9c%8d%e8%88%87%e6%94%b6%e9%8c%84%e7%8f%be%e6%b3%81)
- [版本與品質分層 Tier System](#%E7%89%88%E6%9C%AC%E8%88%87%E5%93%81%E8%B3%AA%E5%88%86%E5%B1%A4-tier-system)
- [這一路是怎麼走到這裡的](#%e9%80%99%e4%b8%80%e8%b7%af%e6%98%af%e6%80%8e%e9%ba%bc%e8%b5%b0%e5%88%b0%e9%80%99%e8%a3%a1%e7%9a%84)
- [自動化 Scripts](#%E8%87%AA%E5%8B%95%E5%8C%96-scripts)
- [不用安裝就能試](#%E4%B8%8D%E7%94%A8%E5%AE%89%E8%A3%9D%E5%B0%B1%E8%83%BD%E8%A9%A6)
- [**貢獻：真正有用的兩件事**](#%e8%b2%a2%e7%8d%bb%e7%9c%9f%e6%ad%a3%e6%9c%89%e7%94%a8%e7%9a%84%e5%85%a9%e4%bb%b6%e4%ba%8b)
- [使用案例](#%E4%BD%BF%E7%94%A8%E6%A1%88%E4%BE%8B)
- [這個 repo 不做的事](#%E9%80%99%E5%80%8B-repo-%E4%B8%8D%E5%81%9A%E7%9A%84%E4%BA%8B)
- [鄰近工具](#%E9%84%B0%E8%BF%91%E5%B7%A5%E5%85%B7)
- [譜系 Lineage](#%E8%AD%9C%E7%B3%BB-lineage)
- [授權](#%E6%8E%88%E6%AC%8A)
- [致謝](#%E8%87%B4%E8%AC%9D)

---

## 快速開始

```bash
# 1. 安裝（Claude Code 主 session）
/plugin marketplace add Zaious/journal-atlas
/plugin install journal-atlas@journal-atlas
# 重啟 Claude Code

# 2. 自然提問
/ja-recommend
> 「我有一篇 12,000 字、研究 embodied cognition 的理論論文。
>   沒有 IRB，沒有 APC 預算。請推薦適合的期刊。」
```

你會得到帶有資料庫證據引用的排序推薦、硬性條件淘汰結果、拒稿後備鏈條與戰略註記。

---

## 安裝方式

### Option 1：Claude Code via plugin marketplace（推薦）

在 Claude Code **主 session**（不是 worktree 子 session——那種環境不開放 `/plugin`）：

```
/plugin marketplace add Zaious/journal-atlas
/plugin install journal-atlas@journal-atlas
```

重啟 Claude Code。兩個 skill（`journal-atlas` + `journal-atlas-contribute`）與所有 8 個 slash command 隨即可用。

### Option 1b：Claude Code via 手動 `git clone`（fallback）

如果你在 worktree session 或環境沒有 `/plugin`：

```bash
# Windows PowerShell
git clone https://github.com/Zaious/journal-atlas.git $HOME\.claude\plugins\journal-atlas

# macOS / Linux
git clone https://github.com/Zaious/journal-atlas.git ~/.claude/plugins/journal-atlas
```

重啟 Claude Code。Plugin（skills + commands）就會可用。

### Option 2：Claude Desktop

1. Clone 本 repo：`git clone https://github.com/Zaious/journal-atlas.git`
2. 在 Claude Desktop 新建一個 Project
3. 把 `skills/journal-atlas/references/journals/` 下的 `.md` 檔上傳作為 Project Knowledge
4. 把 `skills/journal-atlas/SKILL.md` 內容貼進 Project Instructions
5. （可選）同樣方式加入 `skills/journal-atlas-contribute/SKILL.md`，啟用貢獻工作流

### Option 3：ChatGPT（GPT Builder）

1. Clone 本 repo
2. 從 repo root 跑 `cd skills/journal-atlas && python scripts/bundle_for_upload.py` —— 把 journal 檔案合併成符合 ChatGPT 20 檔上限的 bundles
3. 把 `dist/` 下的 bundles 上傳到 GPT 的 Knowledge 區
4. 把 `skills/journal-atlas/SKILL.md` 內容貼進 GPT Instructions

### Option 4：純瀏覽知識庫

在 GitHub 上瀏覽 [`skills/journal-atlas/references/journals/`](skills/journal-atlas/references/journals/)。每個期刊就是一份可讀的 Markdown 頁。不需要 AI。

---

## Skills 總覽

Plugin 包含**兩個 skill**，各自處理不同工作流：

### `journal-atlas` —— 顧問（Advisor）

當你**有一篇論文、需要決策**時使用：推薦、比較、拒稿應對、結構化查詢、橫向探索。

**能力**：
- 讀取期刊知識庫
- 套用硬性條件（字數、APC 預算、AI 政策、IRB、OA 需求）
- 依 6 個維度的軟性適配性排序候選
- 走拒稿後備鏈條（Rejection Fallback Chain）
- 推薦時附證據引用 + Tier 可信度標記

**Entry-count-aware 設計**：從現在 399 entries 繼續擴張：
- ≤20 entries：直接全讀
- 21–50：`scripts/fit_score.py` 預排
- 50+：強制預排，AI 只讀 top 10–15
- 200+：先用 `scripts/query_journals.py` 領域篩選（399 已是預設路徑）

### `journal-atlas-contribute` —— 貢獻者（Contributor）

當你**有經驗想分享**時使用：驗證既有 entry、貢獻新期刊、生成可提交 PR 的 patch。

**兩種模式**：

| 模式 | 何時用 | 流程 |
|------|--------|-----|
| **Mode B —— Validate & Augment**（預設）| 既有 entry 已存在 | AI 讀既有 entry，把宣稱逐條 quote 給你，捕捉你的確認 / 修正 / 補充，生成帶有 evidence-source 升級的 Markdown patch（例如 `(community estimate)` → `(personal experience 2024)`）。最有效率把 Tier 2 升 Tier 1。 |
| **Mode A —— Cold Contribute** | 沒有既有 entry | AI 用 OpenAlex 自動生成結構骨架，然後走 7 段結構化訪談填 Soft Metadata + Strategic Notes。 |

**輸出強制持久化** —— patch 會寫到 `dist/contributed_<slug>.md` 或 `dist/patch_<slug>_<date>.md`，方便你後續開 PR。

---

## Slash Commands

所有命令都用 `ja-` 前綴避免 namespace 衝突。`$ARGUMENTS` passthrough 讓你能一行帶細節直接觸發。

### Advisor commands（路由到 `journal-atlas` skill）

#### `/ja-recommend`

完整 6 步推薦工作流。若你沒提供論文屬性，AI 會主動問。

**範例**：
```
/ja-recommend
> 「12,000 字理論論文，主題是 embodied cognition。沒有 IRB。
>   APC 預算 $0。用 AI 輔助寫作（會揭露）。不要求 immediate OA。」
```

**你會拿到**：top 3 排序推薦，每家附「為什麼適合」evidence quotes、「要留意的風險」、「Key stats」、「Cost」（subscription / OA 兩條路徑）、「If rejected, try next」拒稿後備鏈，以及「考慮過但淘汰」的透明度表格。

#### `/ja-compare`

兩家以上指定期刊的 head-to-head 比較。

**範例**：
```
/ja-compare
> 「PCS vs RGP vs T&P —— 12K 理論論文，AI 揭露，要求 immediate OA，
>   $0 預算」
```

**你會拿到**：跨維度比較表（Topic / Methodology / AI 政策 / 字數 / APC / Embargo / Reviewer culture / Sensitive topics），每家有明確 verdict。

#### `/ja-fallback`

拒稿應對 —— 走特定期刊的 Rejection Fallback Chain。

**範例**：
```
/ja-fallback
> 「我被 PCS 拒稿了。reviewer 說 framing 不夠 phenomenological。
>   下一步該投哪？」
```

**你會拿到**：該期刊的官方 Fallback Chain，依你提供的拒稿理由 filter，再加一段針對下一個目標的「pivot strategy」（如何改寫論文）。

#### `/ja-query`

結構化布林過濾 —— 跑 `scripts/query_journals.py` 並呈現表格。

**範例查詢**：
```
/ja-query → 「列出所有 Q1 心理學期刊，且沒有 AI 預許可制」
/ja-query → 「列出 Sage 旗下零禁售期（zero embargo）的期刊」
/ja-query → 「自我民族誌接受度 3/5 以上的期刊」
/ja-query → 「依 h-index 排序，列前 10 名 HCI 期刊」
```

**你會拿到**：符合條件的篩選表格，列出對應資料點。不走 AI 推理，純 deterministic filter，可擴展到上千 entries。

#### `/ja-similar`

依演算法找跟目標最相似的期刊 —— 比人工策劃的 Rejection Fallback Chain 更廣。

**範例**：
```
/ja-similar → 「跟 PCS 最像的期刊有哪些？」
/ja-similar → 「列出跟 Qualitative Inquiry 最相近的 10 家」
```

**你會拿到**：依演算法排序的相似期刊，附**每維度貢獻分解**（topic Jaccard、methodology cosine、publisher match、OA model、h-index proximity、word-limit proximity、AI policy、embargo）。經常會浮現出人工 fallback chain 漏掉的橫向候選。

#### `/ja-related`

找出特定期刊近期跟你關鍵字最相關的論文 —— 適合寫 cover letter 時引用（「we engage with their recent X, Y, Z」）。

**範例**：
```
/ja-related → 「PCS 近 5 年 embodied cognition 相關論文」
/ja-related → 「QRP 近期 self-state autoethnography 論文，top 3」
```

**你會拿到**：排序好的論文清單（title、作者、年份、citation 數、DOI），依 keyword match + recency + citation 評分。Markdown 格式，可直接貼進 cover letter。

### Contributor commands（路由到 `journal-atlas-contribute` skill）

#### `/ja-contribute`

Cold Contribute 模式 —— 從零提出一個新期刊條目。

**範例**：
```
/ja-contribute
> 「我想加入 Behavioral and Brain Sciences 的條目。我有在那發表過。」
```

**流程**：AI 用 OpenAlex 自動生成骨架 → 走 7 個 Soft Metadata 子段的結構化訪談（Epistemological Leanings / Framing / Methodological Preferences / Voice & Style / Reviewer Pool / Sensitive Topics / Practical Concerns）+ Strategic Notes → 生成符合 TEMPLATE 規範的完整 entry → 寫入 `dist/contributed_<slug>.md` → 引導你開 PR。

#### `/ja-validate`

Validate & Augment 模式 —— 用你的經驗升級既有 entry。

**範例**：
```
/ja-validate
> 「我去年投過 PCS。我們 entry 對 Reviewer Pool 的描述準確嗎？」
```

**流程**：AI 讀 PCS entry → quote Reviewer Pool 的宣稱 → 請你確認 / 修正 / 補充 → 繼續走其他你有經驗的 Soft Metadata 段 → 生成 Markdown patch → 寫入 `dist/patch_pcs_2026-05-16.md` → 引導你開 PR。

**這是推薦的貢獻路徑** —— 把 Tier 2 entry 升 Tier 1 最有效率的方式。

---

## 工作流範例

端到端範例。每個範例展示對話、skill 內部行為、與典型輸出。

### Workflow 1：找一家適合你論文的期刊

**情境**：你有論文，需要一個投稿目標。

```
> /ja-recommend
< 你的論文是什麼主題？請分享：主題、方法、字數、APC 預算、
< AI 使用、IRB 狀態、敏感內容、OA 需求、時程偏好。

> 12,000 字理論論文，主題是 embodied cognition。
> 沒有 IRB（純理論）。APC 預算 $0。AI 輔助寫作（會揭露）。
> 不要求 immediate OA。敏感內容：ritualized altered states。

< [AI 讀 psychology/、cognitive-science/、hci/ 條目；硬條件過濾；
<  剩下的依 6 維度軟適配排序；走 fallback chain]

< 🥇 Phenomenology and the Cognitive Sciences
<   Why it fits: 2020-2025 有 205 篇 embodied/self-state 文獻……
<   Cost: $0 訂閱路徑 / $3,190 OA 路徑
<   If rejected, try next: Theory & Psychology → Review of General Psychology
<                         → New Ideas in Psychology
< 🥈 ……
```

### Workflow 2：比較指定期刊

**情境**：在 2–3 家期刊間抉擇。

```
> /ja-compare PCS vs RGP vs T&P，12K 理論論文，AI 揭露，
> $0 APC，要求 immediate OA

< [生成跨維度表格；每格 quote TEMPLATE 對應段資料]
< 裁決：RGP —— 全硬性條件下唯一倖存者（Sage zero embargo 達成 $0
< immediate OA；15K 字上限容下 12K；AI 揭露制即可；T&P 被 AI 預許可制
< + 10K 字上限雙殺；PCS 被 Springer 12-month embargo 殺掉 immediate-OA）
```

### Workflow 3：拒稿應對

**情境**：reviewer 把你拒了，下一步該怎麼辦？

```
> /ja-fallback PCS 拒稿 —— reviewer 2 說 framing 不夠 phenomenological

< [AI 讀 PCS 的 Rejection Fallback Chain；依拒稿理由 filter]
< 被硬條件殺掉的官方 fallback：
<   Theory & Psychology：被 AI gate + 10K 字上限雙殺
<   New Ideas in Psychology：被 7.5K 字上限 + 24-month embargo 雙殺
<
< 🏆 唯一倖存者：Review of General Psychology
<   為什麼適合：Sage zero embargo 達成 $0 immediate OA；15K 字寬鬆；
<   不要求 phenomenology。Pivot 戰略：拿掉歐陸哲學詞彙，把改變意識狀態
<   的自我民族誌重新包裝為「揭示普通心理學中 self-state 機制的極端
<   理論案例」。
```

### Workflow 4：結構化查詢（條件過濾）

**情境**：你要的是過濾清單，不是推薦。

```
> /ja-query 列出所有 Q1 心理學期刊，零禁售期，沒有 AI 預許可

< [跑 scripts/query_journals.py，flags：--field psychology --quartile Q1
<  --zero-embargo --no-ai-permission-gate]
<
< 163 個 entries 中有 6 個符合：
< | Journal | h-index | OA model | Word limit |
< |---------|---------|----------|------------|
< | Review of General Psychology | 158 | hybrid | 15,000 |
< | Culture & Psychology | 75 | hybrid | 12,000 |
< | ……
```

### Workflow 5：找相似期刊（橫向探索）

**情境**：你在探索，人工 fallback chain 不夠用。

```
> /ja-similar 跟 PCS 最像的有哪些？

< 最相似（演算法 8 維度加權）：
< 1. AI & Society（0.508）—— Springer 出版社 + 認知科學跨領域重疊；
<    h-index 接近度 90%。**沒有**列在 PCS 人工 fallback chain，
<    但演算法找到的橫向候選。
< 2. Culture & Psychology（0.441）—— methodology cosine 0.97……
< ……
```

### Workflow 6：cover letter 準備

**情境**：你選好期刊了，要找該期刊近期相關論文來引用。

```
> /ja-related PCS embodied cognition self-state 4E，近 5 年

< [查 OpenAlex Works API，filter by PCS source，依 keyword + recency
<  + citations 評分]
< Top 3：
< 1. 「The exceptionality of enactivism within 4E cognition」（2026）
<    DOI: 10.1007/s11097-025-10131-1
< 2. 「What is 4E cognitive science?」（2025）—— 6 citations
< 3. ……

# 直接把 markdown 貼進 cover letter 草稿。
```

### Workflow 7：貢獻你的投稿經驗

**情境**：你在某期刊發表過（或被拒）。你的經驗就是 evidence。

```
> /ja-validate 我去年投過 PCS。想分享經驗。

< 讀取 PCS entry…… 我們 entry 說「reviewer pool 主要來自 phenomenology
< 與 4E-cognition 社群；期待對 Husserl, Merleau-Ponty, Gallagher, Zahavi
< 有深度熟悉度」。你的觀察符合嗎？

> Reviewer 2 明顯偏 Husserl；reviewer 1 偏 predictive processing 傳統；
> reviewer 3 是 methodologist，要求更清楚的 phenomenological-method 證成。

< 記錄為：「2024 觀察到的 reviewer 組合：phenomenology 傳統焦點
< （Husserl + predictive processing + phenomenological method）」。
< 這是 first-hand 經驗證據 —— entry 升級從 community-estimate 到
< personal-experience。要繼續下一個宣稱嗎？

[…… 繼續走過其他 Soft Metadata 宣稱 ……]

< Patch 寫入 dist/patch_phenomenology-and-the-cognitive-sciences_2026-05-16.md
< 打開這個檔案，複製內容，到 https://github.com/Zaious/journal-atlas 開
< PR。需要我引導你過 PR 流程嗎？
```

---

## 涵蓋範圍與收錄現況

**Journal Atlas 不是一個通用期刊資料庫。** 它是文獻版圖裡某一塊區域的深掘地圖：
質性與詮釋取向的人文社會科學，加上計算領域裡研究「人」的那部分。先看這張表，
再看任何一則推薦。

### 語料庫裡實際有什麼

399 篇 curated entries，截至 2026-07-30：

| 領域 | 篇數 | Tier 1 | Tier 2 | AI-Researched |
|---|---:|---:|---:|---:|
| 心理學 | 160 | 8 | 52 | 100 |
| 哲學 | 106 | 0 | 0 | **106** |
| HCI（期刊） | 60 | 0 | 30 | 30 |
| 認知科學 | 17 | 0 | 17 | 0 |
| 生物學 | 15 | 0 | 15 | 0 |
| HCI（會議） | 10 | 0 | 10 | 0 |
| 綜合型（*Nature*、*Science*、PNAS、PLOS ONE…） | 8 | 0 | 8 | 0 |
| ML 會議（NeurIPS、ICML、ICLR、AAAI、CVPR） | 5 | 0 | 5 | 0 |
| 醫學（*NEJM*、*Lancet*、*JAMA*、*BMJ*、*Annals*） | 5 | 0 | 5 | 0 |
| 質性方法 | 5 | 3 | 2 | 0 |
| NLP 會議（ACL、EMNLP、NAACL） | 3 | 0 | 3 | 0 |
| 物理 | 3 | 0 | 3 | 0 |
| 資料探勘會議（KDD、WWW） | 2 | 0 | 2 | 0 |

四個彼此相鄰的領域 —— 心理學、哲學、HCI、認知科學 —— 佔了**語料庫的 88%
（399 篇中的 353 篇）**。其餘全部是刻意挑選的稀疏樣本：五本綜合型頂刊、五本綜合
醫學期刊、主要的 ML/NLP 會議。它們是地標，不是覆蓋。

### 明確查證為零的領域

2026-07-30 探測語料庫，以下回傳 **0 篇**：

- **圖書資訊學（含數位圖書館）** —— 是的：這個工具無法評估一篇投往本專案自己
  瞄準的那個場域的論文。與其讓使用者自己撞上，不如寫在這裡。
- **社會學** · **人類學** · **化學、數學與地球科學**

接近零、而且容易誤導的：經濟／商管（2）、法律（1）、政治學（1）—— 這四篇全部是
談該主題的**哲學**期刊（*Business Ethics Quarterly*、*Erasmus Journal for
Philosophy and Economics*），不是該學科自己的期刊。教育（9）與語言學（3）只以
「面向心理學的那一邊」存在。沒有行銷、沒有消費者研究、沒有護理科學，工程領域
除了三本機器人期刊之外一片空白。

**如果你的領域在上面這份清單裡，這個工具目前給不了你東西，而且它會直接這樣說。**
它被設計成回答「我沒有這方面的資料」，而不是把手上最接近的幾本期刊排出一個看起來
很像樣的名次 —— 一則錯的推薦，代價是作者好幾個月。用 `/ja-contribute` 指向一本你
熟悉的期刊，它就會成為新領域的第一篇。

### 為什麼分佈長這樣

這不是一套有原則的抽樣框架。它反映的是這個專案的起點 —— 一個研究者自己在質性
心理學與心靈哲學的投稿問題 —— 然後沿著對貢獻者重要的路徑向外長。這個語料庫誠實
承認自己是便利樣本。上面那些空白領域是最值得長進去的地方 —— 兩條真正有用的路徑
見[貢獻](#%e8%b2%a2%e7%8d%bb%e7%9c%9f%e6%ad%a3%e6%9c%89%e7%94%a8%e7%9a%84%e5%85%a9%e4%bb%b6%e4%ba%8b)。

### 單篇 entry 有多完整

跟「有哪些期刊」無關的另一層問題：每篇 entry 被填寫的程度不同。所有評分維度在
缺乏證據時回傳「未知」而非中位數，因此每則推薦都會在分數旁附上**證據覆蓋率**：

- **163 篇（Tier 1 + Tier 2）：85–100% 覆蓋。** 幾乎每個維度都評得出來。
- **236 篇（AI-Researched）：約 40% 覆蓋。** 它們缺的是同樣四項 —— 方法論契合度、
  審稿人結構、書寫聲音相容性、策略註記 —— 因為 AI-research pipeline 從設計上就
  不允許在沒有來源的情況下推測這些。它們需要真實的投稿或審稿經驗才填得起來。
  見 [SEED_DATA_QUALITY.md](SEED_DATA_QUALITY.md)。

所以 `62.5/100 · 45% evidence` 和 `73.0/100 · 75% evidence` 是兩種不同的主張，
介面會讓你看見你拿到的是哪一種。薄證據上的高分在計算上本來就已經被收縮 —— 分數
會依「已知的少」按比例往中性的 50 拉 —— 但它仍然比同樣數字但證據更厚的那個值錢
更少。

**哲學是最尖銳的案例：106 篇，零篇經人工查證。** 它是語料庫裡第二大的領域，也是
最缺乏佐證的。那些推薦請當成「待查的線索」，不是結論。

---

## 版本與品質分層 Tier System

每個 entry 有兩個正交維度：

**Evidence Quality**（`Tier 1` ↔ `Tier 2`）—— Soft Metadata 宣稱的可信度。

**Completeness**（`Skeleton` ↔ filled）—— Soft Metadata 是否已被書寫。

生命週期：

```
Skeleton ──[社群書寫 Soft Metadata]──► Tier 2
（尚無 Tier 標記，> [!NOTE] banner）   （> [!WARNING] banner）
                                              │
                              [證據累積：文章計數、
                               來源 URL、第一手經驗]
                                              ▼
                                           Tier 1
                                        （無 banner）
```

當前分佈：**11 Tier 1 · 152 Tier 2 · 236 AI-Researched · 0 Skeleton = 共 399**（379 期刊 + 20 會議）。

與 tier 無關的另一層標記：14 篇帶有**出版狀態橫幅**——12 篇經查證已停刊或更名（每篇都寫明後繼刊，讓被拒的稿子有地方去），2 篇標為休眠（十餘年查無出刊，但也查不到停刊公告）。推薦一個根本無法收稿的刊物，浪費的是作者要不回來的時間，所以這些寧可標記也不默默排進名次。AI-Researched 是 v2 覆蓋優先轉向引入的第三種證據基礎，見 [SEED_DATA_QUALITY.md](SEED_DATA_QUALITY.md#a-third-evidence-basis-ai-researched-2026-07)。

完整方法論與升級路徑見 [SEED_DATA_QUALITY.md](SEED_DATA_QUALITY.md)。

---

## 這一路是怎麼走到這裡的

以下每個日期都是 commit 日期，`git log --reverse` 可以核。歷史的**形狀**本身就是
論證，所以照實給，不作摘要。

### 沒有人在解的那個問題

問任何一個夠強的模型「我這篇該投哪裡」，你會拿到該領域最有名的幾本刊。這個答案
與其說是錯的，不如說是沒用：那是你自己也猜得到的答案，它忽略了所有真正決定結果的
限制 —— 費用預算、字數上限、倫理審查、你的方法能不能活過那個審稿人群 —— 而且不管
模型是真的知道這本刊，還是從刊名的形狀重建出來的，語氣一樣篤定。

有不少工具把鄰近的問題答得很好：B!SON 拿摘要配 OA 期刊、Cabells 標掠奪性刊物、
Scimago 排名。但沒有一個握有作者私下真正在互相打聽的那部分 —— 這個審稿人群怎麼
對待質性研究、那個「無嚴格字數限制」是不是真的、在那裡被 desk reject 代表什麼。
這些知識存在，分散在投過稿、審過稿的人身上，而且沒有一份是機器讀得到的。

所以這個專案出發的問題很窄：**那些軟知識，能不能寫成 AI agent 讀得懂的形式，
而且不去編造沒有人知道的那部分？**

### 2026-05-12 → 05-18：dogfood，22 → 163 篇

為了解決一個研究者自己的投稿問題而做，就在他自己的領域。第一天的第二個 commit
就已經把範圍從那些領域放寬到所有學科 —— 窄是當場就看得出來的。

真正決定後面一切的判斷發生在 **05-14，全庫只有 22 篇的時候**：Tier 2 警告橫幅與
[SEED_DATA_QUALITY.md](SEED_DATA_QUALITY.md)，寫在還沒有任何值得辯護的語料庫之前。
在你幾乎什麼都沒有的時候把自己的資料標成低可信度，很便宜；等到那個數字變成你寧可
拿來引用的東西之後，就很貴了。在 22 篇的時候做，是 tier 系統今天承重而不是裝飾的
原因。

**05-17** 語料庫透過吸收一個相鄰的 venue-template 專案、加上手寫會議 entry 來到
163 篇。**05-18** 內容授權從 CC BY-NC-SA 改成 **CC BY-SA** —— 拿掉 NonCommercial，
因為一個商業工具不准讀的知識庫，是在跟自己的目的吵架。

然後**八週什麼都沒有**。05-18 到 07-13，零 commit。

### 2026-07-13：轉向 —— 要有廣度，深度才能被評價

163 篇手寫 entry 是一個 demo。問題在於**沒有人有辦法判斷一個 demo 對不對**。問它
一本它收了的期刊，它看起來很厲害；問它你真正在意的那本，它什麼都沒有，而你分不出
「這是一台謹慎的儀器，只是語料窄」跟「這東西很薄」。

所以 v2 走覆蓋優先，在一天之內：

- 一個 **166,821 列的 ISSN spine**，接起 OpenAlex、DOAJ、JUFO、CAS、Norwegian
  Register 與 Retraction Watch —— 足以對幾乎任何 ISSN 回答*這本刊存在嗎、有被索引
  嗎、還活著嗎*，而不假裝有軟性元資料。
- 一條 **AI 研究 pipeline**（[WO2](docs/workorders/WO2_SOFT_METADATA_BATCH.md)），
  同一天把語料庫從 163 帶到 **399**。

這條 pipeline 的規則才是重點，也正是上面那張覆蓋表長這樣的原因：**有來源 URL 的
事實，或是一個記下了理由的空白。** 不是一個聽起來合理的句子。`review_time：
SciRev 回傳 0 篇評論` 是一個正確的輸出。中文來源（小木虫、知乎）是**強制**而非
選配 —— 對很多期刊來說，那是唯一存在的第一手訊號。

這條規則正是 236 篇 AI-Researched entry 停在約 40% 證據覆蓋而不是 100% 的原因。
它們缺的四個維度 —— 方法論契合、審稿人結構、書寫聲音、策略註記 —— 剛好都需要
真的投過稿的人。一條會去填滿它們的 pipeline，會產出一個好看得多、而且更差的
語料庫。

### 2026-07-20 → 07-30：找出它到底哪裡錯了

**十天的 commit，零篇新增。** 這個專案的最後三分之一，都花在拆自己的作品：

| 發現了什麼 | 為什麼要命 |
|---|---|
| AI 使用許可閘門比對到 TEMPLATE 自己的欄位標籤 | **399 篇全中**——任何揭露 AI 使用的論文被全庫淘汰，而且無聲 |
| 頁數與年份被讀成字數上限 | 有一本刊因此拒絕任何超過「30 字」的稿 |
| 未提及的 IRB 與費用預算被讀成*沒有* IRB、預算*為零* | 一篇理論論文被無聲淘汰掉 33 本期刊 |
| 字數區間取下界 | 「最多可到 10,000 字」被算成 5,000——被 evals 抓到，而且此前已有一個測試斷言了錯的行為 |
| 六個評分維度裡有兩個從來沒被實作 | 讓全庫每一篇的證據覆蓋率都封頂在 70% |
| 61 個沒有任何引註的高分 | 補上真實 OpenAlex 計數；其中 1 個被證據推翻而降級 |
| 停刊偵測 | 實測約 30% 誤判率，於是 `--write` 被關進人工查證後面，而不是就這樣出貨 |

每一條的共同模式：一個把候選淘汰掉的硬性限制，**對使用者是不可見的**。錯的推薦
還能吵。一本從來就沒出現過的期刊，沒得吵。所以現在模稜兩可一律往寬處解，未知
一路傳遞成未知，而不是變成一個中位數。

同一段時間還做了：附帶明確回應時限的[爭議機制](docs/GOVERNANCE.md)、`Disputed`
標記、內容 linter、CI、12 本經查證停刊的期刊（每篇都寫明後繼刊），以及第一次真的
接上活模型跑完整條 pipeline —— 當場又炸出四個缺陷。

### 2026-07-31：公開

不是因為做完了。是因為「它收了什麼、沒收什麼、以及它錯過哪些」現在都寫下來、
可以查了 —— 而對一個陌生人來說，這份聲明比再多兩百篇 entry 有用。

它做得到的：拿真實限制去排真實刊物、給出每個主題的實際文章計數、告訴你每個分數
背後有多少證據、以及說「我沒有這方面的資料」。它做不到的：涵蓋學界的大部分、對
399 篇裡的 236 篇講出任何可信的審稿文化、或取代一位真的在那裡發表過的同行。數字
見[涵蓋範圍與收錄現況](#%e6%b6%b5%e8%93%8b%e7%af%84%e5%9c%8d%e8%88%87%e6%94%b6%e9%8c%84%e7%8f%be%e6%b3%81)，
「做完」長什麼樣見 [PROJECT_COMPLETION.md](docs/PROJECT_COMPLETION.md)。

### 覺得關於某期刊的描述有誤？

Soft Metadata 會對真實、具名的期刊做主觀描述——審稿文化、框架期待、政治
傾向等。如果某項描述不準確，有正式的更正管道：開一則
[Dispute a Claim](.github/ISSUE_TEMPLATE/dispute-claim.md) issue。任何人都可以
提出，編輯或讀者一視同仁，判斷依據是提出的證據而非提出者的身分。爭議處理
期間，該條目會掛上 `Disputed` 標記並指明爭議欄位，確保該項聲稱不會被呈現得
跟無爭議的一樣有把握。

完整政策（適用範圍、處理結果、回應時效承諾）見
[docs/GOVERNANCE.md](docs/GOVERNANCE.md)。

---

## 自動化 Scripts

`skills/journal-atlas/scripts/` 下 9 個 Python 3.10+ scripts，MIT 授權。從 skill root 執行：`cd skills/journal-atlas && python scripts/<name>.py`。

| Script | 用途 | 典型用法 |
|--------|------|---------|
| `query_journals.py` | 結構化布林過濾（publisher / OA model / h-index / quartile / AI policy / embargo / methodology） | `--field psychology --quartile Q1 --no-ai-permission-gate` |
| `fit_score.py` | 加權軟性適配評分 + 硬性條件淘汰 | `--topics "embodied cognition" --methodology theoretical --word-count 12000` |
| `similar_journals.py` | 8 維度加權相似度 | `--target phenomenology-and-the-cognitive-sciences --top-n 5` |
| `related_papers.py` | OpenAlex Works API 在指定期刊內搜尋 | `--journal pcs --keywords "embodied cognition,self-state"` |
| `import_openalex.py` | 從 OpenAlex 生成符合 v1.3 schema 的 entry | `--issn 1568-7759 --field psychology --dry-run` |
| `validate_structure.py` | Schema 驗證；CI 每個 PR 都會跑 | （不帶參數即驗證全部） |
| `bundle_for_upload.py` | 合併 journal 檔案上傳 ChatGPT GPT（20 檔上限） | `--out-dir dist/` |
| `update_metrics.py` | 從 OpenAlex 刷新既有 entries metrics；提出 diff | `--field psychology --apply` |
| `topic_trend_scan.py` | 掃描期刊近期 topic 分佈；keyword 存在檢查 | `--issn 0959-3543 --keywords "BDSM,autoethnography"` |

完整設定與範例見 [scripts/README.md](skills/journal-atlas/scripts/README.md)。

---

## 不用安裝就能試

[`demo/`](demo/) 是一個小型網頁 app，跑的是 skill 使用的同一條管線：自由描述 →
`fit_score.py` 掃過全部 399 篇 → 串流輸出推薦。三個階段、無資料庫、請求之間不留存任何東西。

它直接重用未經修改的 `fit_score.py`，而不是把評分邏輯重寫一遍；後端可跑 Gemini 或
Claude（`.env` 裡的 `LLM_PROVIDER` 決定）。每個候選以可展開的卡片呈現，帶著它的證據
tier 與真實的引註文章數——這是「推薦來自可查核的紀錄、而非模型記憶」的可見證明。

安裝與啟動說明見 [demo/README.md](demo/README.md)。

---

## 貢獻：真正有用的兩件事

上面那張覆蓋表已經把兩個洞講精確了，而它們需要兩種不同的協助。其他都是次要的。

> **洞一 —— 學界的大部分不在裡面。** 九個領域目錄，其中 88% 集中在四個相鄰領域。
> 圖資學、社會學、人類學、物理科學：零篇。
>
> **洞二 —— 399 篇裡有 236 篇背後沒有人。** 它們帶著有來源的政策與主題事實，
> 但關於「實際投起來如何」什麼都沒有。

### 路徑一 —— 把你整個領域帶進來，用我們用過的方法

**這是槓桿最大的貢獻，而且它不是一本一本填的苦工。** 2026-07-13 那次 236 篇的
擴張是**一次** AI 研究執行跑過一份目標清單，而那套程序是公開的，你可以把它指向
你自己的領域：[**WO2_SOFT_METADATA_BATCH.md**](docs/workorders/WO2_SOFT_METADATA_BATCH.md)。

大致是：

1. **建一份目標清單。** 選你的領域，用 OpenAlex 引用數排，或用你領域的人真的會投
   的刊排。20 本就是實質貢獻；100 本會讓你的領域變成一等公民。
2. **每本刊跑三層** —— 政策層（AI 使用、審查制度、preprint、OA/APC）取自出版商
   頁面；定位層取自 OpenAlex topics；經驗層（審稿時間、desk reject 率、審稿文化）
   取自 SciRev、Reddit，以及**中文論壇小木虫／知乎——這是強制的，不是選配**：
   對相當多的期刊而言，那是全世界唯一存在的第一手記述。
3. **開一個帶著草稿的 PR。** 它們會以 AI-Researched tier 落地，橫幅照掛，並成為
   你領域的實務工作者後續回填的骨架。

有兩條規則決定這是幫忙還是傷害：

- **有來源 URL 的事實，或是一個記下了理由的空白。** `review_time：SciRev 回傳
  0 篇評論` 是一個正確而且有價值的輸出。一個沒有來源、聽起來合理的句子，比空白
  更糟 —— 因為空白是誠實的，而且會有人來填。
- **絕不存逐字原文**（論壇貼文、政策條文、摘要），一律正規化成「事實 + 連結」。
  這是語料庫能維持 CC BY-SA 相容的原因。

如果你的領域今天是零篇，那第一個 PR 就是最重要的那個。在 issue 裡說一聲，目標
清單可以跟你一起建。

### 路徑二 —— 回填只有你知道的那部分

**如果你投過或審過某本期刊，你手上握有這個專案用任何其他方式都拿不到的資料。**
再多 AI 研究都碰不到它。那正好就是 236 篇 AI-Researched entry 缺的那四個維度：

- 那個審稿人群會不會拿量化標準審質性研究？
- 標示的字數上限是真的，還是實務上可以談？
- 一篇稿子要用什麼 framing 才活得下來？
- 哪些主題實際上比 scope 說明承認的更難過？
- 在那裡被 desk reject 到底代表什麼，接下來該去哪？

```bash
/ja-validate <journal name>
```

它會用對話訪談你，然後把 PR-ready 的 patch 寫進 `dist/`。花十分鐘講一本你真的
熟的期刊，價值大於一百篇政策爬取的 entry —— 而且如果它跟現有 entry 的說法牴觸，
請直接說：牴觸會走[爭議機制](docs/GOVERNANCE.md)，不會被默默丟掉。

**一本期刊就是實質貢獻。** 路徑二的價值多半就是一篇一篇累積起來的。

### 其他路徑

- **`/ja-contribute`** —— 從零冷啟一篇新 entry
- **[Submission Experience report](.github/ISSUE_TEMPLATE/submission-experience.md)** —— 結構化的投稿後回顧 issue
- **傳統 PR** —— 複製 [`TEMPLATE.md`](skills/journal-atlas/TEMPLATE.md)，填你知道的，其餘留白
- **指出某篇寫錯了** —— 見[覺得關於某期刊的描述有誤？](#%e8%a6%ba%e5%be%97%e9%97%9c%e6%96%bc%e6%9f%90%e6%9c%9f%e5%88%8a%e7%9a%84%e6%8f%8f%e8%bf%b0%e6%9c%89%e8%aa%a4)

品質標準、命名規範與審查指引見 [CONTRIBUTING.md](CONTRIBUTING.md)。唯一不可談判
的那條：**空白勝過猜測。**

---

## 使用案例

完整多輪對話 transcript，端到端展示 skill 能做什麼：

- **[Self-State Dynamics in Altered-State Autoethnography](use-cases/self-state-altered-states-autoethnography.md)**（EN）/ **[自我狀態動力學 vs 改變意識狀態自我民族誌](use-cases/zh-Hant/self-state-altered-states-autoethnography.md)**（繁中）—— 8 輪對話涵蓋推薦、條件變更、拒稿應對、比較裁決、超出 coverage 誠實處理

[`use-cases/`](use-cases/) 內含貢獻 case study 的 template 與投稿指引。

---

## 這個 repo 不做的事

- **不是期刊排名工具。** 我們提供 metadata，你決定優先序。
- **不是 predatory journal 黑名單。** 用 [Cabells](https://www2.cabells.com/)。
- **不是 Scimago / JCR 的替代品。** 我們把它們的量化指標當輔助；我們的價值是那些沒有的軟性元資料。
- **不是論文發現工具。** 跨網路找跟你研究相關的論文，請用 [Connected Papers](https://www.connectedpapers.com/)、[Research Rabbit](https://www.researchrabbit.ai/)、[Litmaps](https://www.litmaps.com/) 或 [Semantic Scholar](https://www.semanticscholar.org/)。我們的 `/ja-related` 只在**指定期刊內**找相關論文 —— 適合 cover letter 準備。

---

## 鄰近工具

Journal Atlas 跟以下工具搭配良好 —— 每個工具回答不同問題：

| 工具 | 回答什麼問題 |
|------|------------|
| **Journal Atlas**（本 repo）| 「哪個期刊適合我這篇論文，投過去會碰到什麼？」 |
| [B!SON](https://service.tib.eu/bison/) | 「給定 abstract，哪些 OA 期刊演算法上 match？」 |
| [Cabells](https://www2.cabells.com/) | 「這家期刊是 predatory 嗎？」 |
| [Scimago](https://www.scimagojr.com/) / [JCR](https://jcr.clarivate.com/) | 「這家期刊的書目計量排名？」 |
| [Connected Papers](https://www.connectedpapers.com/) | 「跟我的關鍵論文叢聚的有哪些？」 |
| [Research Rabbit](https://www.researchrabbit.ai/) | 「我這篇的智識鄰域長什麼樣？」 |
| [Semantic Scholar](https://www.semanticscholar.org/) | 「這個主題的全網文獻有哪些？」 |

典型工作流會混用幾個：

1. 用 B!SON 發現候選期刊
2. 讀 Journal Atlas 條目，了解該期刊軟性條件
3. 用 Cabells 交叉確認非 predatory
4. 用 `/ja-related` 在選定期刊內找要引用的論文

---

## 譜系 Lineage

Journal Atlas 立基於 20 年期刊推薦器的傳統。我們承認前人工作，將自己定位在這個譜系**之內**，而非之外。

| 年份 | 系統 | 方法 | 狀態 |
|------|------|------|------|
| 2007 | [JANE](https://jane.biosemantics.org/)（Schuemie & Kors, *Bioinformatics*）| PubMed 文本相似度 | 運作中，僅限生醫 |
| 2007 | [eTBLAST](https://pubmed.ncbi.nlm.nih.gov/17452348/)（Errami et al., *Nucleic Acids Research*）| 三合一：reviewer + journal + duplicate detection | Server 已關 |
| 2015 | [Elsevier Journal Finder](https://journalfinder.elsevier.com/)（Kang et al., *RecSys*）| NLP + Okapi BM25，限 Elsevier 自家 catalog | 運作中，vendor lock-in |
| 2018 | [Maglet](https://ieeexplore.ieee.org/document/8660987/)（Mohtaj & Tavakkoli, *IST*）| 波斯語區域推薦器 | 學術出版 |
| 2022 | [Open Journal Matcher](https://github.com/MarkEEaton/open-journal-matcher)（Eaton, CUNY）| spaCy word vectors over DOAJ；提出「[pervious technology](https://academicworks.cuny.edu/kb_pubs/261)」概念 | 2022/07 下線 |
| 2021– | [B!SON](https://service.tib.eu/bison/)（TIB + SLUB Dresden，BMBF-funded）| Elasticsearch + BM25 + OpenCitations + ML semantic | **當前 OA 推薦的 state of the art** |

### 向 Open Journal Matcher（OJM）致敬

本專案特別感謝 **Mark E. Eaton 的 Open Journal Matcher**（2020-2022）。2022 年 7 月，Eaton 把 OJM 下線，寫道：

> *「我希望有人能接手我未完成的工作，做出類似的東西，或基於 OJM 的程式碼擴充。學術期刊推薦這塊不該完全留給大型出版商。」*
> —— Eaton (2022), [The last days of the Open Journal Matcher](https://kingsboroughlibtech.commons.gc.cuny.edu/2022/07/29/the-last-days-of-the-open-journal-matcher/)

**Journal Atlas 是對這份邀請的一個回應。**

Eaton 的對應論文 [*On the ethics of working with library technology*](https://academicworks.cuny.edu/kb_pubs/261) 提出了「**pervious technology**」概念 —— 使用者可深入、修改、調整的工具。Journal Atlas 把這個想法擴展：OJM 在「程式碼層」是 pervious 的，Journal Atlas 在「資料層」是 pervious 的。**知識本身就是產品**，不是依賴某個 maintainer 撐著的服務。

### Journal Atlas 加進譜系的三件事

語料庫是看得見的那部分，但它不是貢獻本身。這三件裡有兩件是**方法**，而方法可以
移轉到這個專案永遠不會涵蓋的領域。

**1. 一套判斷適配性的方法** —— [`fit_score.py`](skills/journal-atlas/scripts/fit_score.py)
加上 [CONSUMPTION_CONTRACT.md](skills/journal-atlas/CONSUMPTION_CONTRACT.md)。硬性
條件負責淘汰，六個加權維度負責排序活下來的。真正讓它能用的紀律在於它怎麼處理無知：
沒有證據的維度回傳**未知**而不是中位數，剩下的權重重新正規化，然後結果依「已知的
有多少」按比例往中性收縮。所以分數出來時帶著證據覆蓋率，而 `62.5/100 · 45%
evidence` 讀起來就是一個比 `73.0/100 · 75% evidence` 更弱的主張。這一整套跟期刊
沒有任何關係，換個領域照樣成立。

**2. 一套用 AI 建語料庫而不編造的方法** ——
[WO2_SOFT_METADATA_BATCH.md](docs/workorders/WO2_SOFT_METADATA_BATCH.md)。每個場域
跑三層（政策、定位、經驗），跨語言來源是強制不是選配，而決定一切的只有一條規則：
**有來源 URL 的事實，或是一個記下了理由的空白。** `review_time：SciRev 回傳 0 篇
評論` 是一個正確的輸出。這條 pipeline 就是一天之內把語料庫從 163 帶到 399 的東西，
也是貢獻者可以指向自己領域的東西。

**3. 標準是可以 fork 的，不必吵。** 兩種歧見走兩種機制。如果某個**宣稱**錯了，
[爭議流程](docs/GOVERNANCE.md)就地更正。如果你覺得**標準**錯了 —— Tier 2 太寬鬆、
AI-Researched 根本不該出貨、權重校準有問題 —— 你 fork、改規則、跑你自己的版本。
這件事在這裡特別便宜，正是因為沒有服務需要複製：clone 一個 repo、改 Markdown，
完成。兩個標準不同的語料庫可以對不同的讀者都是對的，而那是一個只有單一託管答案的
工具做不到的事。

我們跟 B!SON 互補，不競爭。用 B!SON 發現候選 OA 期刊，再讀 Journal Atlas 該期刊頁面，了解投稿*實際上*會碰到什麼。完整資料來源與參考資料見 [INSPIRATION.md](INSPIRATION.md)。

---

## 授權

Journal Atlas 採**雙 libre/open 授權**模式：

- **內容**（Markdown 檔、期刊條目、文件、模板）—— [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)（CC BY-SA 4.0）—— 與 Wikipedia 採用相同的 copyleft 授權。
- **程式碼**（`skills/journal-atlas/scripts/` 下所有檔案）—— [MIT License](LICENSE-CODE)

**所有使用都必須保留 attribution。** 偏好引用格式見 [CITATION.cff](CITATION.cff)，完整作者清單見 [AUTHORS.md](AUTHORS.md)。

**ShareAlike（copyleft）保護知識共享。** 你可以為任何目的（包括商業用途）分享與修改 Journal Atlas 的內容，但衍生作品必須以同樣的 CC BY-SA 4.0 授權釋出。這阻止了專屬軟體的吸收，確保知識庫真正自由。

此雙授權模式與 Free Software Foundation 的 Four Freedoms、Open Source Initiative 的 Open Source Definition、以及 Creative Commons 的 Definition of Free Cultural Works 對齊。

**合作與整合** —— 若你需要超越授權範圍的深度合作（客製化資料集、長期整合等），請聯絡 **Meng-Han Lee：zaious.design@gmail.com**。

完整授權細節：[LICENSE](LICENSE) | [LICENSE-CODE](LICENSE-CODE)

---

## 致謝

**創始作者**：Meng-Han Lee（[Zaious](https://zaious.dev/)），獨立 HCI 研究者、AI Agent Architect。[Agentic Social Affordance Framework (ASAF)](https://doi.org/10.5281/zenodo.19652278) 的提出者。

**AI Agent Team**：ChronicleCore —— 在 Zaious 主導下協作的多 agent 系統。架構師：Cardinal（樞機師 / Yui）。其他成員會隨貢獻陸續列名。完整團隊與貢獻者名冊見 [AUTHORS.md](AUTHORS.md)。

由研究者打造、為研究者打造、由社群維護。

影響本專案設計的工具、論文、概念完整列表見 [INSPIRATION.md](INSPIRATION.md) —— 包括 ScienceClaw venue-templates 語料庫，為若干 entries 貢獻了 Format 與家族層 Soft Metadata 內容。
