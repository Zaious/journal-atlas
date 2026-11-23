<!-- schema: v1.3 -->
<!-- AI-researched entry — Journal Atlas v2 coverage pipeline. See docs/ATLAS_V2_DESIGN.md for methodology. -->
<!-- Written without import_openalex.py (no OpenAlex request in this pass); Identity and Metrics come from the local spine and Crossref, then filled by an AI deep research pass (maintainer-directed) on 2026-11-23. -->

# IEEE Transactions on Games

> **Last verified**: 2026-11-23
> **Maintainer**: @Zaious
> **Venue type**: Journal
> **Evidence basis**: AI-researched, overall signal_quality **2/5** — per-fact source URLs with recorded blanks. The journal runs its own site (https://transactions.games/), which answered curl with HTTP 200 and was read live on 2026-11-23; IEEE Xplore and IEEE Computational Intelligence Society pages are script-driven or absent and gave nothing usable. Crossref carries no abstracts for this journal, so counts are over titles only and are lower bounds. OpenAlex was not used. See [SEED_DATA_QUALITY.md](../../../../../SEED_DATA_QUALITY.md).

---

## Identity

| Field | Value |
|-------|-------|
| **Abbreviation** | ToG, as the journal's own pages abbreviate it (https://transactions.games/about/editorial, retrieved 2026-11-23); the DOI prefix uses "TG" (for example https://doi.org/10.1109/TG.2024.3461510) |
| **Venue type** | Journal |
| **Publisher** | Institute of Electrical and Electronics Engineers (Crossref publisher string, https://api.crossref.org/journals/2475-1502, retrieved 2026-11-23) |
| **ISSN (Print)** | 2475-1502 |
| **ISSN (Online)** | 2475-1510 (both listed for "IEEE Transactions on Games" at https://api.crossref.org/journals/2475-1502, retrieved 2026-11-23) |
| **Founded** | The JUFO record gives the start year 2018 for this title (https://jufo-rest.csc.fi/v1.1/kanava/88792, retrieved 2026-11-23); the journal pages read print no founding statement |
| **URL** | https://transactions.games/ |
| **Author Guidelines** | https://transactions.games/submit/submission-guidelines (HTTP 200, read live 2026-11-23) |
| **Society / Association** | IEEE. The journal site links to IEEE Computational Intelligence Society pages (https://cis.ieee.org/publications/t-games/associate-editor-spotlight); the text read does not state a sponsoring society |
| **Editorial Board Location** | https://www.transactions.games/about/editors (read live 2026-11-23): Editor-in-Chief at the University of California, Santa Cruz (USA); countries are printed for only some entries, so no country recount is given (see Reviewer Pool Characteristics) |
| **OpenAlex ID** | Blank. The spine row has no OpenAlex ID and no OpenAlex request was made in this pass |
| **Other lists** | JUFO (Finland) record 88792 gives level 1; Norwegian register level 1 as copied in the same record (https://jufo-rest.csc.fi/v1.1/kanava/88792, retrieved 2026-11-23) |

---

## Metrics

> Source: local spine, an OpenAlex snapshot dated 2026-07-13 (`scripts/query_spine.py --issn 2475-1502`, run 2026-11-23). JCR impact factor and quartile are paywalled and deliberately not stated; the journal home page prints impact-factor and CiteScore figures and they are not recorded here by policy. The 2-year mean citedness below is an OpenAlex proxy, not a JCR figure.

| Metric | Value | Date |
|--------|-------|------|
| **Impact Factor** | Not stated (JCR is paywalled) | |
| **5-Year IF** | Not stated (JCR is paywalled) | |
| **h-index** | 36 (OpenAlex snapshot via spine, all years) | 2026-07-13 |
| **CiteScore** | Not stated (Scopus, not read) | |
| **Acceptance Rate** | Blank. No source: not on the pages read; SciRev's journal page has no editor-provided figure (https://scirev.org/journal/ieee-transactions-on-games/, retrieved 2026-11-23) | 2026-11-23 |
| **Desk Rejection Rate** | Blank. No journal figure; the guidelines say the Editor-in-Chief vets papers before they go to associate editors, without a rate | 2026-11-23 |
| **Quartile (by field)** | Not stated (SJR quartile not read) | |
| **2-yr Mean Citedness (OpenAlex IF proxy)** | 1.93 (OpenAlex snapshot via spine; proxy, not JCR) | 2026-07-13 |
| **i10-index** | Blank. The spine row has no i10 value | |
| **Total Works** | 680 (OpenAlex snapshot via spine, all years and work types); 711 DOIs in Crossref | 2026-07-13 |

### Review Cycle Time

| Stage | Typical Time | Notes |
|-------|-------------|-------|
| **Time to first decision** | Stated goal only: "it is our goal that the whole review process does not take more than 3 months before the decision is sent to the authors" (https://transactions.games/submit/submission-guidelines, re-read 2026-11-24). No measured figure; the Editor-in-Chief's editorial (undated on the page) says the Editor-in-Chief wants to "shorten the time from submission to publication" (https://transactions.games/about/editorial). SciRev lists the journal page with 0 reviews and every timing field n/a (https://scirev.org/journal/ieee-transactions-on-games/, retrieved 2026-11-23) | A stated 3-month goal, not a measured time; no measured figure from any source read |
| **Time to first review** | Blank. No figure found | |
| **Time to acceptance (total)** | Blank. No figure found | |
| **Time to publication (after acceptance)** | Accepted final manuscripts are published electronically on IEEE Xplore with a DOI immediately and then queue for the print issue (https://transactions.games/submit/submission-guidelines, review-process section); no delay figure | Process statement only |

### Publication Frequency

| Aspect | Detail |
|--------|--------|
| **Schedule** | Blank as an issues-per-year statement. The home page spotlights a paper from "vol. 18, no. 3, pp. 432-447, Sept. 2026" (https://transactions.games/), which implies issues within a volume but no stated schedule |
| **Articles per year (approx.)** | Crossref journal-article records by issued year, 2021-11-23 to 2026-11-23: 2021 = 17, 2022 = 84, 2023 = 77, 2024 = 102, 2025 = 111, 2026 = 106 (497 records; https://api.crossref.org/works?filter=issn:2475-1502,from-pub-date:2021-11-23). 73 of the 497 carry no author list and are front matter such as "Table of Contents" and "Information for Authors", leaving 424 records with author lists |
| **Special issues?** | Yes: the home page lists five special-issue pages: Open Game Data for Games for Impact, Responsible and Human-Centered AI in Games, Multi-Modal Content Generation for Games, Human-Centred AI in Game Evaluation, and Large Language Models and Games (links from https://transactions.games/, read 2026-11-23); a proposal page exists at https://transactions.games/special-issue/propose-a-special-issue |

---

## Policies

### Peer Review

| Aspect | Detail |
|--------|--------|
| **Type** | Conflicting on the journal's own pages. The home page and guidelines say that from 2025-01-01 reviewing "will adopt a double-anonymous format" and papers submitted from that date must be fully anonymised, with papers submitted earlier treated as single-anonymous (https://transactions.games/submit/submission-guidelines, read 2026-11-23); the same page later says "The journal operates a double-blind review process"; the reviewer-resources page says each published article was reviewed by at least two reviewers under a single-blind process (https://transactions.games/submit/reviewer-resources). The IEEE Xplore about page, read in a real browser 2026-11-23 (https://ieeexplore.ieee.org/xpl/aboutJournal.jsp?punumber=7782673), says each article gets at least two independent reviewers under a "single and/or double anonymous" process and is screened for plagiarism before acceptance; it does not settle which applies now. Current model therefore still unverified; confirm on the submission site |
| **Transferable / Cascade?** | Blank. No source read |
| **Reviewer reports published?** | Blank. The pages read say nothing about publishing reports |
| **Typical R+R rounds** | Number of rounds blank. For a revise-and-resubmit, "If a revised version is sent within 6 months, it will most probably be handled by the same Action Editor" (https://transactions.games/submit/submission-guidelines, re-read 2026-11-24); for minor revisions "there will not be any additional round of review". The guidelines list the decisions Accept, Accept with minor revisions and further outcomes; the Associate Editor "will ordinarily make a recommendation after receiving three reviews (two for letters)" (guidelines, review-process section) |
| **Reviewer recommendations** | After vetting, the Editor-in-Chief sends the paper to Associate Editors, who manage review and invite reviewers matched by topic (guidelines and reviewer-resources pages, read 2026-11-23); the reviewer page lists seven questions reviewers should ask, including whether the study is well designed and whether the article suits the publication |

### AI Policy

| Aspect | Detail |
|--------|--------|
| **Has journal-specific AI policy?** | No journal-specific text on the journal pages (submission guidelines, reviewer resources, open access, editorial). The Xplore about page defers to IEEE's publisher-wide policy, and the become-a-reviewer page tells reviewers to read IEEE's rules on AI use (https://transactions.games/become-a-reviewer, read in a real browser 2026-11-23) |
| **Explicit permission gate?** | No permission gate; a disclosure rule. IEEE's Author Center says AI-generated content (text, figures, images, code) must be disclosed in the acknowledgements, naming the AI system and the sections concerned with a brief note on the level of use; AI for editing and grammar needs no disclosure but disclosure is recommended; reviewers must not put manuscript content through a public AI platform (https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/, read in a real browser 2026-11-23) |
| **Leniency (1-5)** | 3 (author judgement: generated content is allowed with disclosure; editing use is free) |
| **Summary** | Publisher-wide IEEE rule, facts paraphrased; the journal's own scope text welcomes papers on artificial intelligence for games, which is a subject, not a policy (https://transactions.games/) |
| **Source URL** | https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/ |

### Preprint Policy

> Source: the journal's open access page, read live 2026-11-23 (https://transactions.games/submit/open-access), which restates IEEE's sharing policy. Policies may change.

| Stage | Allowed? | Notes |
|-------|----------|-------|
| Pre-submission | Yes | Authors may post anywhere, including arXiv or TechRxiv, and posting on a preprint server does not count as prior publication |
| Under review | Yes | The submitted version may be posted on personal, employer, institutional or funder websites and on collaboration networks that follow STM sharing principles, with a notice on the first page; the double-anonymous rule for submissions does not discuss how a posted preprint interacts with anonymity |
| Post-acceptance (AAM) | Yes, with replacement | Previously posted versions must be replaced by the accepted version; funder repositories carry an embargo of 24 months, or less where the funder requires |
| Version of Record | Only under a CC BY licence | The final published article may be posted anywhere under CC BY; under the standard IEEE copyright form it may not be posted online |

### Open Access

| Aspect | Detail |
|--------|--------|
| **Model** | Hybrid in effect: the open access page describes a CC BY route and a standard IEEE copyright-form route (https://transactions.games/submit/open-access) |
| **APC (if OA chosen)** | Blank. The page read gives no amount. Separate page charges: an optional charge of $110 per printed page and a mandatory over-length charge of $200 per page above 10 pages (full papers), 15 (survey), 6 (short) and 4 (letters), imposed by IEEE only "If the voluntary page charge is not honoured" (https://transactions.games/submit/submission-guidelines) |
| **Gold OA offered?** | Yes through the CC BY route, amount not read |
| **Read & Publish agreements** | Blank. No source read |

---

## Format

> Source for the rules below: the submission guidelines, read live 2026-11-23 (https://transactions.games/submit/submission-guidelines), called "guidelines".

| Aspect | Detail |
|--------|--------|
| **Article types accepted** | Full papers (10 to 14 pages, fees apply over 10), letters (4 pages), survey papers (15 to 20 pages, fees over 15), short papers (6 to 8 pages, fees over 6) and immersive papers (6 to 14 pages plus an interactive part as a zip file); the guidelines also name dataset and benchmark papers, instrumentation and infrastructure papers, replication papers, and negative and null-result papers as welcome (guidelines) |
| **Word limit** | None in words: limits are in pages of the IEEE two-column format, including references and optional author biographies but excluding supplementary material (guidelines); the same page also says papers over 12 pages are considered only if the author justifies the length in the cover letter |
| **Word limit negotiability** | The 12-page justification rule above is the only exception found |
| **Abstract limit** | 150 to 200 words, one paragraph, self-contained; 2 to 5 keywords (guidelines) |
| **Reference limit** | No cap found; references count inside the page limits. IEEE style |
| **Supplementary material** | Excluded from page limits; software and data for review go through https://anonymous.4open.science/ ; authors are told to host dataset papers' data on Zenodo, GitHub or Figshare (guidelines) |
| **Figure/Table limits** | No count limit found; page limits apply |
| **Style / submission format** | IEEE Transactions template from the IEEE Author Center; a cover letter naming the submission type and whether it is for a special issue; "Comments to Editor-in-Chief" must say the work is not published or under review elsewhere; submission through https://mc.manuscriptcentral.com/tg-ieee ; fully anonymised manuscript with no author names, affiliations, biographies or funding acknowledgments (guidelines) |

---

## Subject Density

> There is no OpenAlex scaffold for this entry. The table below counts keyword themes in Crossref record titles (the 424 records with author lists; regexes G8, G10, G17 and G19 to G21 in AI-Research Notes), not OpenAlex topics; one title can carry several themes. Crossref carries no abstracts for this journal.

### Top Topics (last 5 years)

| Topic | Article Count |
|-------|--------------|
| Artificial intelligence, machine learning, procedural content generation (G10) | 113 |
| Learning, education, gamification, serious games, training (G17) | 107 |
| Players or player experience (G19) | 34 |
| Design, designers or mechanics (G20) | 19 |
| Review, survey or meta-analysis wording (G8) | 12 |
| Simulation (G21) | 9 |

### Orientation

> Counts below are word-boundary regex matches (case-insensitive) over the titles of Crossref journal-article records dated 2021-11-23 to 2026-11-23: 497 records, of which 424 have an author list (front matter excluded); 0 records carry an abstract, so counts are lower bounds. Denominator for shares: 424. Regexes are G1 to G22 in AI-Research Notes. Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Empirical vs. Theoretical** | Technical and applied by title wording: AI, machine-learning or procedural-generation wording 113 of 424 titles (26.7%, G10); theoretical or conceptual wording 1 (0.2%, G6). The scope text welcomes "all scientific, technical, and engineering aspects of games" (https://transactions.games/, read 2026-11-23) |
| **Quantitative vs. Qualitative** | Quantitative, survey or statistical wording 9 titles (2.1%, G1) and experiment or user-study wording 7 (1.7%, G2) against interview or qualitative wording 2 (0.5%, G3); titles seldom name a method, so these are very low lower bounds |
| **Cross-disciplinary openness** | The Editor-in-Chief's editorial (undated on the page) lists artificial intelligence, human-computer interaction, psychology, education and health as the disciplines games research spans (https://transactions.games/about/editorial); education and serious-games wording appears in 107 of 424 titles (25.2%, G17) |

---

## Soft Metadata

> [!NOTE]
> **AI-Researched (2026-11-23)** — the fields below were researched per-journal from public sources (Crossref counts, the journal's own site, SciRev, and searches of Chinese-language and Reddit sources) rather than adapted from a family-level template. Every populated field cites its source or a stated count; fields with no public evidence were left blank with the reason recorded — see "AI-Research Notes" at the end of this section. This entry's overall `signal_quality` is **2/5**. This is a *different* evidence basis than "Tier 1" (deep manual evidence-harvesting) or "Tier 2" (family-level community estimate) — see [SEED_DATA_QUALITY.md](../../../../../SEED_DATA_QUALITY.md).

### Epistemological & Political Leanings

> Evidence layers: Crossref titles 2021-11-23 to 2026-11-23 (424 records with author lists, no abstracts); Crossref citation counts as of 2026-11-23; the journal's own pages read live 2026-11-23. Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Cross-cultural friendliness** | Author countries were not counted: Crossref records carry no country field and OpenAlex was not used. Institutions named in the part of https://www.transactions.games/about/editors that was read include ones in Brazil, Denmark, Germany, Austria, Italy, Iceland, Spain, the Netherlands, Canada, Finland, Malta, India, Taiwan and China, and Ulster University (UK), alongside the USA; this shows spread but is not a count |
| **Editorial-board geography** | Not recounted by country: the board page prints a country for only some entries. Role counts from the page: 1 Editor-in-Chief, 6 Strategic Advisors, an Associate Editors section with 193 text lines in three-line entries (name, topics, institution) whose exact entry count was not taken because some entries lack a line, and 4 administrative roles (https://www.transactions.games/about/editors, read 2026-11-23) |
| **Non-Western epistemology openness** | Indigenous, colonial or decolonial wording in 0 of 424 titles (G12); no editorial statement on the topic was found on the pages read (https://transactions.games/about/editorial) |
| **Diversity topic receptiveness** | Gender, women or sexuality wording in 2 of 424 titles (0.5%, G11); race or ethnicity wording 0 (G12). The Editor-in-Chief's editorial (undated on the page) speaks of "a thriving and inclusive community" as a goal for authors and reviewers (https://transactions.games/about/editorial) |
| **Dominant theoretical tradition** | Engineering and computational. Most-cited records of the window in Crossref (citation counts as of 2026-11-23): Large Language Models and Games: A Survey and Roadmap (147; https://doi.org/10.1109/tg.2024.3461510), Win Prediction in Multiplayer Esports (80; https://doi.org/10.1109/tg.2019.2948469), Generating Role-Playing Game Quests With GPT Language Models (71; https://doi.org/10.1109/tg.2022.3228480), Real-Time Prediction of Simulator Sickness in Virtual Reality Games (59; https://doi.org/10.1109/tg.2022.3178539), Creating Pro-Level AI for a Real-Time Fighting Game Using Deep Reinforcement Learning (58; https://doi.org/10.1109/tg.2021.3049539). The journal states no political position on the pages read |

### Framing Requirements

- **Mandatory framing?** Scope rule: the journal welcomes work on "all scientific, technical, and engineering aspects of games" and its guidelines ask for "mature work that is original" (https://transactions.games/ and https://transactions.games/submit/submission-guidelines, read 2026-11-23).
- **What kind of engagement?** Technical contributions to game technologies, design and evaluation; the Editor-in-Chief's editorial (undated on the page) aims to make the journal "the central hub for this interdisciplinary field" (https://transactions.games/about/editorial). 113 of 424 titles (26.7%) carry AI, machine-learning or procedural-generation wording (G10).
- **Article type and length**: five types measured in pages: full 10 to 14, short 6 to 8, survey 15 to 20, letter 4, immersive 6 to 14 (see Format).
- **Special-issue framing seen**: five special-issue pages are linked from the home page (https://transactions.games/ ), including Large Language Models and Games and Open Game Data for Games for Impact.
- **Consequences of ignoring it**: over-length papers incur a $200 per page charge above the limit only if the voluntary page charge is not honoured; conference papers and book chapters already published are not acceptable unless significantly enhanced (guidelines, read 2026-11-23).

### Methodological Preferences

> Counts: regex matches over the titles of Crossref records dated 2021-11-23 to 2026-11-23; 424 records with author lists; shares use 424 as the denominator. Titles seldom name a method, so these are very low lower bounds, and Crossref has no abstracts for this journal. Scoring convention of this research pass (its own, not an external standard): share 0 = 0; under 1% = 1; 1-5% = 2; over 5% = 3; 4-5 only with a cited editorial statement or a clearly dominant count. Scores measure how often a method appears in titles, not how a reviewer would judge it. The schema's rows fit an engineering journal only partly; added rows say so. Regexes are G1 to G10 in AI-Research Notes.

| Method | Receptiveness (0-5) | Evidence |
|--------|---------------------|----------|
| Quantitative experimental | 2 | Quantitative, survey or statistical wording 9 of 424 titles (2.1%, G1); experiment, intervention or user-study wording 7 (1.7%, G2) |
| Qualitative interviews | 1 | Interview, focus-group or "qualitative" wording 2 of 424 (0.5%, G3) |
| Autoethnography | 0 | 0 of 424 (G5) |
| Theoretical / Conceptual | 1 | 1 of 424 (0.2%, G6) |
| Mixed methods | 1 | 1 of 424 (0.2%, G7) |
| Meta-analysis | 2 | Review, survey or meta-analysis wording 12 of 424 (2.8%, G8); "survey papers" are a listed article type of 15 to 20 pages (guidelines, https://transactions.games/submit/submission-guidelines) |
| Computational and machine-learning methods (added row) | 3 | AI, machine-learning, reinforcement-learning, neural or procedural-generation wording 113 of 424 titles (26.7%, G10); the Editor-in-Chief's editorial (undated on the page) names game AI, procedural generation and game analytics as current content (https://transactions.games/about/editorial) |
| Replication, datasets and null results (added row) | Not scored | The guidelines welcome dataset and benchmark, instrumentation, replication and negative-result papers (https://transactions.games/submit/submission-guidelines); titles were not searched for them |

### Voice & Style

| Aspect | Detail |
|--------|--------|
| **First-person voice acceptance (0-5)** | Not scored. Crossref holds 0 abstracts for this journal (0 of 497 records), so first-person use cannot be sampled from the abstracts, and article openings were not read. The guidelines do not mention first person (https://transactions.games/submit/submission-guidelines) |
| **Expected density** | Page limits, not words: 10 to 14 pages for full papers including references; letters 4 pages (guidelines) |
| **Abstract and keywords** | 150 to 200 words in one paragraph, 2 to 5 keywords; the page also says an abstract should include "three or four different keywords or phrases" (guidelines) |
| **Writing style notes** | IEEE Transactions format and IEEE reference style; abstracts without abbreviations, footnotes or references; detailed derivations may go in appendices (guidelines) |
| **Authorship pattern** | Crossref author-list counts for the 424 records that have one: 1 author 19, 2 authors 75, 3 authors 113, 4 or more 217 (retrieved 2026-11-23) |

### Reviewer Pool Characteristics

Reviewer behaviour itself is not observable from public pages; what follows is what public pages do show.

| Aspect | Detail | Evidence |
|--------|--------|----------|
| **Dominant tradition** | Board page: 1 Editor-in-Chief, 6 Strategic Advisors (one of them an industry associate editor), an Associate Editors section (entry count not taken), 4 administrative roles. Each associate editor lists research topics; entries seen in the part of that section read mention game AI, reinforcement learning, procedural content generation, game analytics, serious games, HCI and VR/AR/XR | https://www.transactions.games/about/editors |
| **Reviewer list size** | Blank. No public reviewer list found; the become-a-reviewer page (https://transactions.games/become-a-reviewer, read in a real browser 2026-11-23) says the journal is looking to expand its reviewer board and asks volunteers to fill in a form | https://transactions.games/submit/reviewer-resources |
| **Review model** | Conflicting statements: double-anonymous from 2025-01-01 (home page and guidelines), "double-blind" (guidelines), single-blind with at least two reviewers (reviewer-resources page), "single and/or double anonymous" (Xplore about page, read 2026-11-23); unverified | https://transactions.games/submit/submission-guidelines ; https://transactions.games/submit/reviewer-resources |
| **Reviewer competence variance** | Blank. SciRev has 0 reviews for this journal | https://scirev.org/journal/ieee-transactions-on-games/ |
| **Quantitative mindset bias on qualitative work?** | Blank. No source on reviewer attitudes; qualitative wording appears in 2 of 424 titles (G3), so qualitative work is rare here, which is a publication fact, not a reviewer fact | Crossref counts, see Methodological Preferences |
| **Discourse community signals (editorial board)** | The Editor-in-Chief's editorial (undated on the page) plans collaboration with the conferences IEEE CoG, CHI PLAY, AIIDE, Serious Play, the International Joint Conference on Serious Games and Foundations of Digital Games | https://transactions.games/about/editorial |

### Sensitive Topics

> Counts are regex matches (G-labels in AI-Research Notes) over the titles of 424 Crossref records with author lists, 2021-11-23 to 2026-11-23; lower bounds because titles are short. "Receptiveness" gives frequency; High is used only where the journal states a position, runs a section or features the topic in a curated collection.

| Topic Category | Receptiveness | Evidence |
|----------------|---------------|----------|
| AI and large language models | High | G10 113 of 424 titles (26.7%); a special-issue page on Large Language Models and Games and a special issue on Responsible and Human-Centered AI in Games (https://transactions.games/ ); the most cited window record is a survey on LLMs and games (147 citations, https://doi.org/10.1109/tg.2024.3461510) |
| Ethics in game AI | Mentioned | The Editor-in-Chief's editorial (undated on the page) names "Ethics in Game AI" among "current special issues" (https://transactions.games/about/editorial, re-read 2026-11-24). The page https://transactions.games/special-issue/special-issue-on-ethics-in-game-ai returned HTTP 404 on 2026-11-24, so no call or issue was read; this is a one-sentence editorial mention, not a scored receptiveness |
| Violence, toxicity, harassment | Rare | G13 3 of 424 titles (0.7%) |
| Gambling and monetisation | Rare | G15 3 (0.7%) |
| Gender, women, sexuality | Rare | G11 2 (0.5%) |
| Esports and streaming | Present | G16 4 (0.9%); https://doi.org/10.1109/tg.2019.2948469 (esports win prediction, 80 citations) |

### Practical Concerns

| Concern | Detail |
|---------|--------|
| **IRB requirement strictness** | Blank. No ethics-approval rule on the pages read (https://transactions.games/submit/submission-guidelines) |
| **Single-author acceptance** | Single-author records are 19 of 424 with an author list (4.5%; Crossref, retrieved 2026-11-23); 217 records have 4 or more authors |
| **Independent scholar friendliness** | No independent-scholar rule found; submissions must be anonymised, so affiliations are not shown to reviewers (https://transactions.games/submit/submission-guidelines) |
| **Data transparency requirement** | Dataset papers are welcomed and authors are told to host data on Zenodo, GitHub or Figshare; the submission system has a data-repository question (GitHub, Dryad or Other) (guidelines, read 2026-11-23); no mandatory data-sharing rule found |
| **OPSEC compatibility** | Double-anonymous for submissions from 2025-01-01: no author names, affiliations, biographies or funding acknowledgments in the manuscript; anonymised repositories through https://anonymous.4open.science/ (https://transactions.games/submit/submission-guidelines); preprints allowed (see Preprint Policy) |
| **AI use** | No journal-level AI-use text read (see AI Policy) |
| **Open access and cost** | CC BY route exists, amount not read; optional page charge $110 per page and an over-length charge of $200 per page imposed if the voluntary charge is not honoured (see Open Access) |
| **Funding and permissions** | Copyright transfer to IEEE with a signed form after acceptance, or the CC BY route (guidelines and open access page) |
| **Prior and parallel publication** | Previously published conference papers and book chapters are not acceptable unless significantly enhanced; the cover letter must state the work is not under review elsewhere (guidelines) |

### AI-Research Notes (sources, blanks, and cross-language checks)

**signal_quality (0-5)**: overall 2. Per layer: Crossref counts (titles only) 2 (0 abstracts; no country data); journal-specific policies and guidelines 3 (read live, but the review-model statements conflict); editorial board 2 (roles counted, entries not); experiential layer 0 (SciRev has a page but no reviews).

**Sources cited across this entry:**
- https://transactions.games/ , /submit/submission-guidelines , /submit/open-access , /submit/reviewer-resources , /about/editorial , https://www.transactions.games/about/editors (all HTTP 200, read live 2026-11-23)
- https://api.crossref.org/journals/2475-1502 ; Crossref works for the window (497 records, 0 with abstract, 424 with author lists); Crossref citation counts sorted for the window
- Local spine (OpenAlex snapshot 2026-07-13): works 680, h-index 36, 2-year mean citedness 1.93, JUFO 1, Norwegian register 1
- https://jufo-rest.csc.fi/v1.1/kanava/88792 ; https://scirev.org/journal/ieee-transactions-on-games/

**Method notes:** Crossref titles were counted locally with the regexes below (Python re, IGNORECASE). Share = hits / 424; hits count records, not occurrences. Broad patterns over-count: G10 matches the word "AI" in any case and "neural"; G17 matches "learning" in any sense (including machine learning), so it overlaps G10; G19 matches "player" in any sense; G20 matches "design"; G21 matches any "simulat-" word.

**Keyword regexes (exact):**
- G1 `\b(quantitative|statistical(ly)?|regression|ANOVA|surveys?|questionnaires?|structural equation|Likert)\b` ; G2 `\b(experiments?|experimental|quasi-experimental|randomi[sz]ed|control group|controlled trial|user study|user studies)\b`
- G3 `\b(interviews?|focus groups?|thematic analysis|grounded theory|qualitative|semi-structured)\b` ; G5 `\bautoethnograph\w*\b` ; G6 `\b(theoretical(ly)?|conceptual(ly)?|theori[sz](e|es|ed|ing)|philosoph\w*|ontolog\w*|phenomenolog\w*)\b`
- G7 `\bmixed[- ]methods?\b` ; G8 `\b(meta-analys[ei]s|systematic review|scoping review|literature review|systematic literature)\b` ; G10 `\b(artificial intelligence|generative AI|ChatGPT|large language models?|LLMs?|AI|machine learning|reinforcement learning|neural|procedural content generation|deep learning)\b`
- G11 `\b(gender(ed)?|women|sexis\w*|feminis\w*|queer|LGBT\w*|transgender|non-?binary|sexuality|misogyn\w*)\b` ; G12 `\b(raci(al|alized|st|sm)|racio\w*|whiteness|antiracis\w*|ethnic(ity|ities)?|colonial\w*|decoloni\w*|indigenous)\b`
- G13 `\b(violen\w*|toxic\w*|harass\w*|extremis\w*|hate|abus\w*)\b` ; G15 `\b(gambling|loot ?boxes?|monetization|monetisation|microtransactions?|gacha)\b` ; G16 `\b(esports?|e-sports?|streamers?|streaming|twitch)\b`
- G17 `\b(learning|education\w*|gamification|serious games?|pedagog\w*|students?|training)\b` ; G19 `\b(players?|player experience|playe?rs?hip)\b` ; G20 `\b(game design|designers?|mechanics|level design|design)\b` ; G21 `\bsimulat\w*\b`

**Unreadable pages (never filled from memory):**
- Recovered in a real browser 2026-11-23: the IEEE Xplore about-journal page (https://ieeexplore.ieee.org/xpl/aboutJournal.jsp?punumber=7782673; curl saw only page chrome), https://transactions.games/become-a-reviewer , and IEEE's submission and peer review policies (AI rule). https://cis.ieee.org/publications/ieee-transactions-on-games returned 404 earlier.
- Still not read: https://transactions.games/get-involved , the Associate Editors section of https://www.transactions.games/about/editors for an exact count (not retried in the browser), and the open-access fee amount
- The OpenAlex scaffold was not used (no OpenAlex request in this pass); OpenAlex ID, i10-index and OpenAlex topic counts are therefore not recorded.

**Fields deliberately left blank, and why:**
- Acceptance rate, desk rejection rate, review times, R+R rounds, transfer and cascade, reviewer reports published, reviewer list, issues per year: no source on the pages read.
- APC amount: the pages read give page charges but no open access amount.
- Review model: the journal's own pages conflict (see Peer Review).
- Reviewer culture, competence variance, quantitative mindset bias: SciRev has no reviews.
- Author countries and exact board counts by country: not printed.
- First-person voice: Crossref has no abstracts.
- Impact factor and quartile: paywalled, not stated by policy.

**Cross-language and forum checks performed:**
- SciRev (English): journal page exists with popularity score and 0 reviews (https://scirev.org/journal/ieee-transactions-on-games/, read 2026-11-23).
- Web search (2026-11-23) "IEEE Transactions on Games 投稿 经验 审稿周期 OR reddit review time desk reject" returned the journal's own pages, a Wikipedia page, peeref.com, an arXiv paper unrelated to this journal and no Reddit, 小木虫 or 知乎 thread about this journal.
- LetPub and fabiaoji: not checked.

---

## Strategic Notes

> Each statement below follows from a fact recorded above and names it. Where the evidence does not support a statement, the field says so.

### Hard Blockers

- **Length in pages**: full papers 10 pages in the IEEE two-column format including references; over-length pages carry a $200 each charge, described as mandatory but imposed only if the voluntary page charge is not honoured (Format, Open Access).
- **Anonymisation**: submissions from 2025-01-01 must be fully anonymised, including funding acknowledgments (Peer Review, Format).
- **Prior publication**: conference papers and book chapters must be significantly enhanced; the cover letter must say the work is not under review elsewhere (Practical Concerns).

### Soft Tax

- **Unclear review model**: the journal's own pages state double-anonymous, double-blind and single-blind in different places, so what reviewers see is unverified (Peer Review).
- **Timing**: the guidelines state only a goal of a decision within 3 months; no measured time and no SciRev entries exist (Review Cycle Time).
- **Cost**: page charges of $110 per page are requested after acceptance (optional) and over-length charges apply only if the voluntary charge is not honoured (Open Access).

### Best Suited For

- Technical game research: game AI, procedural content, analytics, player modelling and serious-games engineering, which carry 113 of 424 titles with AI wording and 107 with learning or serious-games wording (Orientation).
- Surveys, datasets, benchmarks, replications and null results, which the guidelines name as welcome (Format).
- Work on large language models in games, with a linked special issue and the most-cited window record (Sensitive Topics).

### Not Recommended For

- Cultural-critical, qualitative or theoretical game studies: qualitative wording is 2 of 424 titles (0.5%, G3) and theoretical wording 1 (0.2%, G6) (Methodological Preferences).
- Authors who need a stated review model, measured decision time, acceptance rate or AI policy: none of these could be read except the 3-month decision goal and the AI rule, which is a publisher-wide disclosure rule (Peer Review, Review Cycle Time, AI Policy).

### Rejection Fallback Chain

> No source states where rejected authors usually go. The rows below are topical neighbours that exist in this corpus or in this directory, listed because they share subject area; they are not claims about acceptance odds.

| Rank | Journal | Why this fallback works |
|------|---------|------------------------|
| 1 | [Entertainment Computing](../hci/entertainment-computing.md) | HCI-leaning games neighbour already in the corpus; no fit evidence collected here |
| 2 | [Simulation & Gaming](simulation-and-gaming.md) | Applied games journal with 12 AI-wording abstract-records of 187 (6.4%, see that entry) |
| 3 | [Games and Culture](games-and-culture.md) | Social-science side; AI wording is 6 of 319 abstract-records (1.9%, see that entry), so overlap is partial |

---

## Changelog

| Date | Change | By |
|------|--------|----|
| 2026-11-23 | Initial entry (written from the local spine and Crossref; no import_openalex scaffold) | @your-handle |
| 2026-11-23 | AI deep research pass; no first-hand human reports | AI-assisted (maintainer-directed) |
| 2026-11-24 | Pages unreadable by curl re-read in a real browser (Xplore about page review statement, IEEE AI disclosure rule, become-a-reviewer page) | @Zaious |
| 2026-11-24 | Corrections after independent verification (3-month decision goal and 6-month revision window filled; $200 charge condition stated; Ethics in game AI downgraded, dead URL dropped; topic table order) | @Zaious |
