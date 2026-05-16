# Journal Atlas

> 🌐 **Languages**: [English](README.md) | 繁體中文

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Content-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE-CODE)
[![Schema](https://img.shields.io/badge/Schema-v1.2-green.svg)](skills/journal-atlas/TEMPLATE.md)
[![Status](https://img.shields.io/badge/Status-Pre--release%20(seeding)-orange.svg)](#%E7%89%88%E6%9C%AC%E8%88%87%E5%93%81%E8%B3%AA%E5%88%86%E5%B1%A4-tier-system)

**一個由社群維護、為 AI 而生的學術期刊適配性知識庫。**

Journal Atlas 補上了 Impact Factor 與 Scimago 這類書目計量工具無法觸及的東西：學術期刊的**軟性元資料（soft metadata）**——審稿人文化、framing 期待、敏感主題接受度、AI 政策細節、方法論偏好、拒稿後備策略。所有內容封裝為一個 Claude Agent Skill，可跨 Claude Code、Claude Desktop、ChatGPT 安裝。

> **狀態（2026-05）：Pre-release。** 114 個種子 entries，跨 8 個領域目錄。
> 品質分層：**11 Tier 1**（有實證後盾）· **28 Tier 2**（社群推估）· **75 Skeleton**（自動骨架，Soft Metadata 待填）。
> 見 [版本與品質分層](#%E7%89%88%E6%9C%AC%E8%88%87%E5%93%81%E8%B3%AA%E5%88%86%E5%B1%A4-tier-system) 與 [SEED_DATA_QUALITY.md](SEED_DATA_QUALITY.md)。

---

## 目錄

- [快速開始](#%E5%BF%AB%E9%80%9F%E9%96%8B%E5%A7%8B)
- [安裝方式](#%E5%AE%89%E8%A3%9D%E6%96%B9%E5%BC%8F)
- [Skills 總覽](#skills-%E7%B8%BD%E8%A6%BD)
- [Slash Commands](#slash-commands)
- [工作流範例](#%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%AF%84%E4%BE%8B)
- [版本與品質分層 Tier System](#%E7%89%88%E6%9C%AC%E8%88%87%E5%93%81%E8%B3%AA%E5%88%86%E5%B1%A4-tier-system)
- [自動化 Scripts](#%E8%87%AA%E5%8B%95%E5%8C%96-scripts)
- [貢獻](#%E8%B2%A2%E7%8D%BB)
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

**Entry-count-aware 設計**：從現在 114 entries 規劃到 200+：
- ≤20 entries：直接全讀
- 21–50：`scripts/fit_score.py` 預排
- 50+：強制預排，AI 只讀 top 10–15
- 200+：先用 `scripts/query_journals.py` 領域篩選

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
< 114 家中有 6 家符合：
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

當前分佈：**11 Tier 1 · 28 Tier 2 · 75 Skeleton = 共 114**。

完整方法論與升級路徑見 [SEED_DATA_QUALITY.md](SEED_DATA_QUALITY.md)。

---

## 自動化 Scripts

`skills/journal-atlas/scripts/` 下 9 個 Python 3.10+ scripts，MIT 授權。從 skill root 執行：`cd skills/journal-atlas && python scripts/<name>.py`。

| Script | 用途 | 典型用法 |
|--------|------|---------|
| `query_journals.py` | 結構化布林過濾（publisher / OA model / h-index / quartile / AI policy / embargo / methodology） | `--field psychology --quartile Q1 --no-ai-permission-gate` |
| `fit_score.py` | 加權軟性適配評分 + 硬性條件淘汰 | `--topics "embodied cognition" --methodology theoretical --word-count 12000` |
| `similar_journals.py` | 8 維度加權相似度 | `--target phenomenology-and-the-cognitive-sciences --top-n 5` |
| `related_papers.py` | OpenAlex Works API 在指定期刊內搜尋 | `--journal pcs --keywords "embodied cognition,self-state"` |
| `import_openalex.py` | 從 OpenAlex 生成符合 v1.2 schema 的 entry | `--issn 1568-7759 --field psychology --dry-run` |
| `validate_structure.py` | Schema 驗證；CI 每個 PR 都會跑 | （不帶參數即驗證全部） |
| `bundle_for_upload.py` | 合併 journal 檔案上傳 ChatGPT GPT（20 檔上限） | `--out-dir dist/` |
| `update_metrics.py` | 從 OpenAlex 刷新既有 entries metrics；提出 diff | `--field psychology --apply` |
| `topic_trend_scan.py` | 掃描期刊近期 topic 分佈；keyword 存在檢查 | `--issn 0959-3543 --keywords "BDSM,autoethnography"` |

完整設定與範例見 [scripts/README.md](skills/journal-atlas/scripts/README.md)。

---

## 貢獻

最低門檻的貢獻路徑是 **`/ja-validate <journal>`** —— 對話式分享你的投稿經驗，skill 自動生成 PR-ready 的 Markdown patch 到 `dist/`。

其他路徑：

- **`/ja-contribute`** —— 從零提出新期刊 entry
- **[Submission Experience report](.github/ISSUE_TEMPLATE/submission-experience.md)** —— 結構化的 GitHub Issue 投稿經驗回報（作為社群 pattern library）
- **傳統 PR 流程** —— 複製 [`skills/journal-atlas/TEMPLATE.md`](skills/journal-atlas/TEMPLATE.md)，填你知道的，開 PR

品質標準、命名規範與審查指引見 [CONTRIBUTING.md](CONTRIBUTING.md)。

**最缺的是 Soft Metadata** —— 那些不成文的規則：reviewer culture、framing requirement、敏感主題接受度。如果你在某期刊發表過、或審過稿，那份知識是演算法挖不到的證據。

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

三個設計選擇把 Journal Atlas 跟前人區分：

1. **以期刊為單位的知識庫，不是 query-time app。** 持久、可被引用、隨社群貢獻單調改進的 profile。Soft metadata 演算法挖不到，需要人類社群知識，也需要超越任何單一 maintainer 承諾的耐久性。
2. **Markdown + Git，不是服務基礎設施。** 零代管成本，零單點失效。誰都能 fork。
3. **為 agent 時代設計。** 包裝為 Claude Agent Skill —— 一行安裝、任何懂 skill 規範的工具都能消費、跨越未來介面變動仍可流通。

我們跟 B!SON 互補，不競爭。用 B!SON 發現候選 OA 期刊，再讀 Journal Atlas 該期刊頁面，了解投稿*實際上*會碰到什麼。完整資料來源與參考資料見 [INSPIRATION.md](INSPIRATION.md)。

---

## 授權

Journal Atlas 採**雙授權**模式：

- **內容**（Markdown 檔、期刊條目、文件、模板）—— [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/)（CC BY-NC-SA 4.0）
- **程式碼**（`skills/journal-atlas/scripts/` 下所有檔案）—— [MIT License](LICENSE-CODE)

**所有使用（商業或非商業）都必須保留 attribution。** 偏好引用格式見 [CITATION.cff](CITATION.cff)，完整作者清單見 [AUTHORS.md](AUTHORS.md)。

**商業使用** —— 非商業使用依 CC BY-NC-SA 4.0 免費。若你要做商業整合（整合進付費產品、商業服務重新分發、付費 research-as-a-service 等），請聯絡 **Meng-Han Lee：zaious.design@gmail.com** 討論條款。

完整授權細節：[LICENSE](LICENSE) | [LICENSE-CODE](LICENSE-CODE)

---

## 致謝

**創始作者**：Meng-Han Lee（[Zaious](https://zaious.dev/)），獨立 HCI 研究者、AI Agent Architect。[Agentic Social Affordance Framework (ASAF)](https://doi.org/10.5281/zenodo.19652278) 的提出者。

**AI Agent Team**：ChronicleCore —— 在 Zaious 主導下協作的多 agent 系統。架構師：Cardinal（樞機師 / Yui）。其他成員會隨貢獻陸續列名。完整團隊與貢獻者名冊見 [AUTHORS.md](AUTHORS.md)。

由研究者打造、為研究者打造、由社群維護。

影響本專案設計的工具、論文、概念完整列表見 [INSPIRATION.md](INSPIRATION.md) —— 包括 ScienceClaw venue-templates 語料庫，為若干 entries 貢獻了 Format 與家族層 Soft Metadata 內容。
