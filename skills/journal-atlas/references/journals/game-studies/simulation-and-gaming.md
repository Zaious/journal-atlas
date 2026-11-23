<!-- schema: v1.3 -->
<!-- AI-researched entry — Journal Atlas v2 coverage pipeline. See docs/ATLAS_V2_DESIGN.md for methodology. -->
<!-- Written without import_openalex.py (no OpenAlex request in this pass); Identity and Metrics come from the local spine and Crossref, then filled by an AI deep research pass (maintainer-directed) on 2026-11-23. -->

# Simulation & Gaming

> **Last verified**: 2026-11-23
> **Maintainer**: @Zaious
> **Venue type**: Journal
> **Evidence basis**: AI-researched, overall signal_quality **2/5** — per-fact source URLs with recorded blanks. The publisher (SAGE) answered curl with HTTP 403, so the journal home was read as a Wayback copy; the author instructions, editorial board and SAGE's AI and archiving policies were then read live in a real browser on 2026-11-23. Counts are Crossref-based and OpenAlex was not used. See [SEED_DATA_QUALITY.md](../../../../../SEED_DATA_QUALITY.md).

---

## Identity

| Field | Value |
|-------|-------|
| **Abbreviation** | S&G, as the journal's own pages abbreviate it (instructions copy 2025-08-12, https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG ) |
| **Venue type** | Journal |
| **Publisher** | SAGE Publications (Crossref publisher string, https://api.crossref.org/journals/1046-8781, retrieved 2026-11-23) |
| **ISSN (Print)** | 1046-8781 |
| **ISSN (Online)** | 1552-826X (Crossref lists both ISSNs for "Simulation & Gaming", https://api.crossref.org/journals/1046-8781, retrieved 2026-11-23) |
| **Founded** | Not stated as a year. The home page copy says the journal has served the field "for more than five decades" (https://web.archive.org/web/20261016143441id_/https://journals.sagepub.com/home/sag ); the earliest Crossref DOI year is 1990 with 66 DOIs, which is the start of DOI deposit, not of the journal |
| **URL** | https://journals.sagepub.com/home/sag |
| **Author Guidelines** | https://journals.sagepub.com/author-instructions/SAG (read live in a real browser 2026-11-23; curl got HTTP 403 on 3 tries; the live page matched the Wayback copy of 2025-08-12 on word limits, abstract length, anonymisation, preprints, colour charges and AI authorship, https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG ) |
| **Society / Association** | The journal header on the home page copy 2026-10-16 links to two simulation-gaming association sites, https://isaga.com/ and http://nasaga.org/ ; the page text read does not say what the relationship is (https://web.archive.org/web/20261016143441id_/https://journals.sagepub.com/home/sag ) |
| **Editorial Board Location** | Live board page, read in a real browser 2026-11-23 (https://journals.sagepub.com/editorial-board/SAG ): 43 entries (2 co-editors + 41 associate editors); per-country recount in Reviewer Pool Characteristics. The 43 and the country figures are "read in a real browser 2026-11-23; not independently re-checked" (curl gets HTTP 403). The newest curl-readable copy, Wayback 2022-02-15 (https://web.archive.org/web/20220215075712id_/https://journals.sagepub.com/editorial-board/SAG), had 51 entries (2 co-editors + 1 history entry + 34 associate editors + 14 advisory board = 51) |
| **OpenAlex ID** | Blank. The spine row has no OpenAlex ID and no OpenAlex request was made in this pass |
| **Other lists** | JUFO (Finland) record 67121 gives level 1; Norwegian register level 1 as copied in the same record (https://jufo-rest.csc.fi/v1.1/kanava/67121, retrieved 2026-11-23) |

---

## Metrics

> Source: local spine, an OpenAlex snapshot dated 2026-07-13 (`scripts/query_spine.py --issn 1046-8781`, run 2026-11-23). JCR impact factor and quartile are paywalled and deliberately not stated; the publisher pages print impact-factor figures and they are not recorded here by policy. The 2-year mean citedness below is an OpenAlex proxy, not a JCR figure.

| Metric | Value | Date |
|--------|-------|------|
| **Impact Factor** | Not stated (JCR is paywalled) | |
| **5-Year IF** | Not stated (JCR is paywalled) | |
| **h-index** | 99 (OpenAlex snapshot via spine, all years) | 2026-07-13 |
| **CiteScore** | Not stated (Scopus, not read) | |
| **Acceptance Rate** | Blank. No source: not on the pages read; SciRev's journal page has no editor-provided figure (https://scirev.org/journal/simulation-and-gaming/, retrieved 2026-11-23) | 2026-11-23 |
| **Desk Rejection Rate** | Blank. No journal figure. The instructions say manuscripts "may be desk rejected" if out of scope or unsuitable, without a rate (instructions copy 2025-08-12) | 2026-11-23 |
| **Quartile (by field)** | Not stated (SJR quartile not read) | |
| **2-yr Mean Citedness (OpenAlex IF proxy)** | 2.48 (OpenAlex snapshot via spine; proxy, not JCR) | 2026-07-13 |
| **i10-index** | Blank. The spine row has no i10 value | |
| **Total Works** | 1976 (OpenAlex snapshot via spine, all years and work types); 1938 DOIs in Crossref | 2026-07-13 |

### Review Cycle Time

| Stage | Typical Time | Notes |
|-------|-------------|-------|
| **Time to first decision** | Blank. The instructions copy gives no target: "reviewed as rapidly as possible" only (https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG ). SciRev lists the journal page with 0 reviews and every timing field n/a (https://scirev.org/journal/simulation-and-gaming/, retrieved 2026-11-23) | No time figure from any source read |
| **Time to first review** | Blank. No figure found | |
| **Time to acceptance (total)** | Blank. No figure found | |
| **Time to publication (after acceptance)** | Blank. No source read | |

### Publication Frequency

| Aspect | Detail |
|--------|--------|
| **Schedule** | "Published bi-monthly" per the journal home page copy of 2026-10-16 (https://web.archive.org/web/20261016143441id_/https://journals.sagepub.com/home/sag ) |
| **Articles per year (approx.)** | Crossref journal-article records by issued year, 2021-11-23 to 2026-11-23: 2021 = 4, 2022 = 42, 2023 = 43, 2024 = 53, 2025 = 41, 2026 = 37 (220 records in all; https://api.crossref.org/works?filter=issn:1046-8781,from-pub-date:2021-11-23); all are typed journal-article, so editorials are included, and 187 carry an abstract |
| **Special issues?** | Blank. No special-issue call was read; the home page copy lists an editorial dated Sep 2026 with the two journal editors as authors (https://web.archive.org/web/20261016143441id_/https://journals.sagepub.com/home/sag ) |

---

## Policies

### Peer Review

| Aspect | Detail |
|--------|--------|
| **Type** | Double-anonymised: identities of reviewer and author are concealed from each other; the manuscript must be fully anonymised with identifying information on a Title Page (instructions copy 2025-08-12, https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG ) |
| **Transferable / Cascade?** | Blank. No source read |
| **Reviewer reports published?** | Blank. The instructions copy says nothing about publishing reports |
| **Typical R+R rounds** | Blank. SciRev has no entries; the instructions say two independent reviews are required for a Revise or Accept decision (instructions copy) |
| **Reviewer recommendations** | Reviewers make comments to the author and recommendations to the Editor, who makes the final decision; authors cannot recommend reviewers; an initial evaluation comes first and out-of-scope manuscripts may be desk rejected (instructions copy 2025-08-12) |

### AI Policy

| Aspect | Detail |
|--------|--------|
| **Has journal-specific AI policy?** | No journal-specific text. The live instructions say chatbots such as ChatGPT should not be listed as authors and link to SAGE's publisher-wide AI policy (https://www.sagepub.com/journals/publication-ethics-policies/artificial-intelligence-policy), read in a real browser 2026-11-23 |
| **Explicit permission gate?** | No permission gate. SAGE sorts AI use into assistive (language, grammar or structure suggestions; no disclosure), generative (content that affects methods, analysis, results or conclusions; disclosure on submission) and prohibited. Disclosed use alone is not a ground for rejection; undisclosed inappropriate use lets the editor reject at any stage |
| **Leniency (1-5)** | 3 (author judgement from the SAGE page: assistive use is free, generative use needs disclosure, and listed prohibited uses include AI standing in for interview participants, AI theme analysis and fabricated references) |
| **Summary** | Publisher-wide SAGE rule applied here; disclosure goes in the methods or acknowledgements for generative uses such as literature compilation, translation, code, visualisation and reference compilation. Facts paraphrased, read in a real browser 2026-11-23 |
| **Source URL** | https://www.sagepub.com/journals/publication-ethics-policies/artificial-intelligence-policy |

### Preprint Policy

> Source: journal instructions, Wayback copy 2025-08-12 (https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG). Policies may have changed since.

| Stage | Allowed? | Notes |
|-------|----------|-------|
| Pre-submission | Yes | "Accepts preprints? Yes"; the preprint DOI goes into the submission form and the editorial office should be told |
| Under review | No for updated versions | The live instructions say not to post an updated version of the manuscript on a preprint server while it is being peer reviewed (read in a real browser 2026-11-23) |
| Post-acceptance (AAM) | Yes | SAGE's archiving guidelines (https://www.sagepub.com/author-archiving-and-re-use-msg, read in a real browser 2026-11-23; not independently re-checked) let authors share the original submission or accepted manuscript at any time after acceptance, on any website or repository or social channel; no embargo wording found on that page |
| Version of Record | Restricted | The same page says the final published PDF may not go on an unrestricted website or repository without SAGE's permission; it may be used for own teaching, individual sharing with colleagues, a thesis or an authored book |

### Open Access

| Aspect | Detail |
|--------|--------|
| **Model** | Subscription journal ("Access: Subscription") with optional open access via SAGE Choice and agreements (instructions copy 2025-08-12); the home page copy shows articles marked "Open Access" next to restricted ones |
| **APC (if OA chosen)** | Amount not on the pages read. "There are no fees payable to submit or publish in this journal"; open access is "for a fee". Colour in print: $800 for the first colour image and $200 for each additional one; online colour is free (instructions copy) |
| **Gold OA offered?** | Optional (see Model) |
| **Read & Publish agreements** | SAGE open access agreements exist and eligibility is decided by the corresponding author's affiliation at acceptance (instructions copy); the participating-institution list was not read |

---

## Format

> Source for the rules below: the author instructions, Wayback copy 2025-08-12 (https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG), called "instructions copy".

| Aspect | Detail |
|--------|--------|
| **Article types accepted** | Research articles (7000 words, excluding references); short research reports of pilot studies, at most two tables and two figures (3000 words, excluding references); theoretical articles (5000 words); "simulations ready to use" for classroom use, research-based and with the game guide in an appendix (5000 words); systematic reviews and meta-analyses are "encouraged over literature reviews"; case reports considered case by case (instructions copy) |
| **Word limit** | 7000 words for research articles, excluding references; limits "may only be exceeded by explicit permission" of the editors (instructions copy) |
| **Word limit negotiability** | Only with explicit editor permission (instructions copy) |
| **Abstract limit** | Structured abstract of 200 to 300 words; at least 3 keywords (instructions copy) |
| **Reference limit** | No cap found; references are outside the word counts. APA style |
| **Supplementary material** | The editors "may limit" supplementary material relative to article length and message (instructions copy); a guide for simulations goes in an appendix |
| **Figure/Table limits** | Two tables and two figures for short research reports; no count limit found for other types |
| **Style / submission format** | Word preferred, no template; body suggested as Background, Intervention, Methods, Results, Discussion with a research-objective statement at the start of Methods; cover letter explaining suitability; fully anonymised main file plus Title Page; submission through https://mc.manuscriptcentral.com/sg ; the IRB statement and EQUATOR-network checklist rules appear under Practical Concerns |

---

## Subject Density

> There is no OpenAlex scaffold for this entry. The table below counts keyword themes in Crossref title-plus-abstract text (regexes G17 to G21 in AI-Research Notes), not OpenAlex topics; one record can carry several themes.

### Top Topics (last 5 years)

| Topic | Article Count |
|-------|--------------|
| Learning, education, gamification, serious games, training (G17) | 143 |
| Simulation (G21) | 91 |
| Design, designers or mechanics (G20) | 85 |
| Players or player experience (G19) | 66 |
| Artificial intelligence or machine learning (G10) | 12 |
| Addiction, well-being, mental health (G18) | 12 |
| Gender, women, sexuality (G11) | 11 |

### Orientation

> Counts below are word-boundary regex matches (case-insensitive) over title plus abstract of Crossref journal-article records dated 2021-11-23 to 2026-11-23: 220 records, 187 with an abstract (85.0%), so counts are lower bounds. Denominator for shares: 187. Regexes are G1 to G22 in AI-Research Notes. Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Empirical vs. Theoretical** | Empirical predominates: quantitative, survey or statistical wording 79 of 187 (42.2%, G1); experiment or intervention wording 30 (16.0%, G2); theoretical or conceptual wording 27 (14.4%, G6). The instructions say the journal "encourages original research" (instructions copy 2025-08-12, https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG ) |
| **Quantitative vs. Qualitative** | Both are common, quantitative more so: G1 79 (42.2%) against interview or qualitative wording G3 50 (26.7%); mixed methods G7 10 (5.3%) |
| **Cross-disciplinary openness** | Education and training settings dominate: G17 143 (76.5%) and 89 record titles; simulation wording G21 91 (48.7%). The home page copy describes simulation and gaming methods "used in education, training, consultation, and research" (https://web.archive.org/web/20261016143441id_/https://journals.sagepub.com/home/sag ). SciRev lists the journal under Computer Science Applications (https://scirev.org/journal/simulation-and-gaming/) |

---

## Soft Metadata

> [!NOTE]
> **AI-Researched (2026-11-23)** — the fields below were researched per-journal from public sources (Crossref counts, Wayback copies of the publisher's pages, SciRev, and searches of Chinese-language and Reddit sources) rather than adapted from a family-level template. Every populated field cites its source or a stated count; fields with no public evidence were left blank with the reason recorded — see "AI-Research Notes" at the end of this section. This entry's overall `signal_quality` is **2/5**. This is a *different* evidence basis than "Sourced" (deeper per-journal research, every claim cites a source) or "Estimated" (family-level estimate) — see [SEED_DATA_QUALITY.md](../../../../../SEED_DATA_QUALITY.md).

### Epistemological & Political Leanings

> Evidence layers: Crossref records 2021-11-23 to 2026-11-23 (220 records, 187 with an abstract, regexes in AI-Research Notes); Crossref citation counts as of 2026-11-23; Wayback copies of the journal's pages. Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Cross-cultural friendliness** | Author countries were not counted: Crossref records carry no country field and OpenAlex was not used. The home page copy calls it "An International Journal of Theory, Practice and Research" (https://web.archive.org/web/20261016143441id_/https://journals.sagepub.com/home/sag ); board geography below |
| **Editorial-board geography** | Live board read in a real browser 2026-11-23 (https://journals.sagepub.com/editorial-board/SAG ): 43 entries (2 co-editors + 41 associate editors), all with a printed country, no advisory board listed; USA 8, Netherlands 5, Japan 4, Italy 3, Germany 3, Israel 3, Spain 2, UK 2, France 2, and one each in India, Switzerland, Hungary, Austria, Australia, Canada, Russia, New Zealand, Turkey, Poland and China (8+5+4+3+3+3+2+2+2+11 = 43; the printed spellings "United States" and "The Netherlands" are merged with USA and Netherlands; one co-editor lists two Japanese universities and counts once). The 43 entries and all counts here were read in a real browser 2026-11-23 and not independently re-checked. The newest curl-readable copy, Wayback 2022-02-15 (https://web.archive.org/web/20220215075712id_/https://journals.sagepub.com/editorial-board/SAG), had 51 entries (2+1+34+14) with USA 17, Netherlands 11 and Japan 3, recounted from that copy on 2026-11-24 |
| **Non-Western epistemology openness** | Indigenous, colonial or decolonial wording in 1 of 187 abstract-records (0.5%, G12); no editorial statement on the topic was found on the pages read (https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG ) |
| **Diversity topic receptiveness** | Gender, women, feminist or queer wording 11 of 187 (5.9%, G11); race or ethnicity wording 1 (0.5%, G12); SAGE's diversity and inclusion pledge is linked from the instructions copy |
| **Dominant theoretical tradition** | Applied, education-and-training oriented. Most-cited records of the window in Crossref (citation counts as of 2026-11-23): Therapeutic Use of Role-Playing Game (RPG) in Mental Health: A Scoping Review (61; https://doi.org/10.1177/10468781211073720), Modern Technologies and Gamification in Historical Education (50; https://doi.org/10.1177/10468781221075965), Effects of Gamification on Motivations of Elementary School Students (38; https://doi.org/10.1177/10468781241237389), Association between Clinical Simulation Design Features and Novice Healthcare Professionals' outcomes (37; https://doi.org/10.1177/10468781221120599), Integrating Biofeedback and Artificial Intelligence into eXtended Reality Training Scenarios (34; https://doi.org/10.1177/10468781241236688). The journal states no political position on the pages read |

### Framing Requirements

- **Mandatory framing?** Scope rule: the journal covers "simulation/gaming methodologies used in education, training, consultation, and research" (home page copy 2026-10-16, https://web.archive.org/web/20261016143441id_/https://journals.sagepub.com/home/sag). The instructions say a manuscript outside scope "will not be reviewed" (instructions copy 2025-08-12, https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG).
- **What kind of engagement?** Practice-facing: "simulations ready to use" must be research-based and "not simply descriptive or a sales pitch" for a commercial game, with a usage guide in an appendix (instructions copy); 143 of 187 abstract-records (76.5%) carry learning, education, gamification or training wording (G17).
- **Article type and length**: research articles 7000 words, short reports 3000, theoretical and ready-to-use articles 5000, all excluding references (see Format).
- **Special-issue framing seen**: none read; the home page copy lists no call (home page copy 2026-10-16).
- **Consequences of ignoring it**: manuscripts that do not follow the guidelines are returned for amendment before peer review, and out-of-scope manuscripts may be desk rejected (instructions copy 2025-08-12).

### Methodological Preferences

> Counts: regex matches over title plus abstract of Crossref records dated 2021-11-23 to 2026-11-23; 187 of 220 records have an abstract; shares use 187 as the denominator. Scoring convention of this research pass (its own, not an external standard): share 0 = 0; under 1% = 1; 1-5% = 2; over 5% = 3; 4-5 only with a cited editorial statement or a clearly dominant count. Scores measure how often a method appears in abstracts, not how a reviewer would judge it. Regexes are G1 to G9 in AI-Research Notes.

| Method | Receptiveness (0-5) | Evidence |
|--------|---------------------|----------|
| Quantitative experimental | 3 | Quantitative, survey or statistical wording 79 of 187 (42.2%, G1); experiment, intervention or user-study wording 30 (16.0%, G2); the count is large but the scale stops at 3 without an editorial statement |
| Qualitative interviews | 3 | Interview, focus-group, thematic, grounded-theory or "qualitative" wording 50 (26.7%, G3) |
| Autoethnography | 1 | 1 of 187 (0.5%, G5) |
| Theoretical / Conceptual | 3 | Theoretical, conceptual, philosophical or ontological wording 27 (14.4%, G6); "theoretical articles" are a listed article type of 5000 words (instructions copy) |
| Mixed methods | 3 | 10 of 187 (5.3%, G7) |
| Meta-analysis | 4 | Review, scoping or meta-analysis wording 14 (7.5%, G8); the instructions state that systematic reviews and meta-analyses are "encouraged over literature reviews" (instructions copy 2025-08-12, https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG) |
| Ethnography (added row) | 1 | 1 of 187 (0.5%, G4) |
| Textual, discourse and content analysis (added row) | 3 | G9 16 (8.6%) |

### Voice & Style

| Aspect | Detail |
|--------|--------|
| **First-person voice acceptance (0-5)** | Not scored. 84 of 187 abstracts (44.9%) contain I, we, our or my (regex FP, case-sensitive); among the 20 most recent abstracts (dated 2026-04-07 to 2026-11-21), 9 do (Crossref, retrieved 2026-11-23). The instructions say nothing on first person (instructions copy 2025-08-12) |
| **Expected density** | 7000 words for research articles excluding references; 3000 for short reports; 5000 for theoretical and ready-to-use articles (instructions copy, https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG) |
| **Abstract and keywords** | Structured abstract of 200 to 300 words and at least 3 keywords (same instructions copy) |
| **Writing style notes** | APA reference style; Word file, no template; the editors ask for succinct writing and graphics, tables and diagrams to support the text, and say longer articles are "set aside and not read" (paraphrase of the word-count note, instructions copy 2025-08-12) |
| **Authorship pattern** | Crossref author-list counts for the 219 records that have one (1 has none): 1 author 21, 2 authors 73, 3 authors 48, 4 or more 77 (retrieved 2026-11-23) |

### Reviewer Pool Characteristics

Reviewer behaviour itself is not observable from public pages; what follows is what public pages do show.

| Aspect | Detail | Evidence |
|--------|--------|----------|
| **Dominant tradition** | Live board, read in a real browser 2026-11-23: 43 entries = 2 co-editors + 41 associate editors (2+41 = 43); no advisory board listed (the 2022 copy had 14). The page prints institutions but no discipline labels, so a discipline count is not possible | https://journals.sagepub.com/editorial-board/SAG |
| **Reviewer list size** | Blank. No public reviewer list was found on the pages read | https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG |
| **Review model** | Double-anonymised; two independent reviews required for Revise or Accept (instructions copy 2025-08-12) | https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG |
| **Reviewer competence variance** | Blank. SciRev has 0 reviews for this journal | https://scirev.org/journal/simulation-and-gaming/ |
| **Quantitative mindset bias on qualitative work?** | Blank. No source on reviewer attitudes; qualitative wording appears in 50 of 187 abstract-records (G3), so qualitative work is common here, which cannot show how reviewers treat it | Crossref counts, see Methodological Preferences |
| **Discourse community signals (editorial board)** | Live board: USA 8, Netherlands 5 and Japan 4 of 43 entries; 20 countries in all (read in a real browser 2026-11-23; not independently re-checked). The 2022-02-15 Wayback copy of 51 entries had USA 17, Netherlands 11 and Japan 3 | https://journals.sagepub.com/editorial-board/SAG ; https://web.archive.org/web/20220215075712id_/https://journals.sagepub.com/editorial-board/SAG |

### Sensitive Topics

> Counts are regex matches (G-labels in AI-Research Notes) over title plus abstract of 187 Crossref records with an abstract, 2021-11-23 to 2026-11-23; lower bounds. "Receptiveness" gives frequency; High is used only where the journal states a position, runs a section or features the topic in a curated collection, which the pages read do not show for any row.

| Topic Category | Receptiveness | Evidence |
|----------------|---------------|----------|
| Mental health, therapy and well-being | Regularly published | G18 12 of 187 (6.4%); the most-cited window record is a scoping review of role-playing games in mental health (61 citations, https://doi.org/10.1177/10468781211073720) |
| AI and machine learning | Regularly published | G10 12 (6.4%); 8 record titles; https://doi.org/10.1177/10468781241236688 (biofeedback and AI in XR training, 34 citations) |
| Gender, women, sexuality | Present | G11 11 (5.9%) |
| Race, ethnicity, colonialism | Rare | G12 1 (0.5%) |
| Violence, toxicity, harassment | Rare | G13 3 (1.6%) |
| Politics, ideology, labour | Rare | G14 7 (3.7%) |
| Gambling and monetisation | Rare | G15 1 (0.5%) |

### Practical Concerns

| Concern | Detail |
|---------|--------|
| **IRB requirement strictness** | Research on human subjects needs an institutional review board approval statement (or, for some international researchers, a statement of national ethics rules); an ethical-considerations and consent section is also required on the Title Page; EQUATOR-network reporting checklists must be uploaded; clinical trials need registry details at the end of the abstract (instructions copy 2025-08-12, https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG) |
| **Single-author acceptance** | Single-author records are 21 of 219 with an author list (9.6%; Crossref, retrieved 2026-11-23); 77 records have 4 or more authors |
| **Independent scholar friendliness** | No independent-scholar rule found (instructions copy 2025-08-12, https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG) |
| **Data transparency requirement** | A data availability statement is part of the Title Page declarations; authors who cannot share data say why (instructions copy) |
| **OPSEC compatibility** | Double-anonymised: identifying information on the Title Page only; preprints accepted and the preprint DOI entered at submission (instructions copy 2025-08-12, https://web.archive.org/web/20250812102547id_/https://journals.sagepub.com/author-instructions/SAG) |
| **AI use** | Chatbots may not be listed as authors; under the SAGE AI policy (Wayback copy 2026-11-15, https://web.archive.org/web/20261115211059id_/https://www.sagepub.com/journals/publication-ethics-policies/artificial-intelligence-policy) assistive tools for language, grammar or structure need no disclosure, while generative uses that affect methods, analysis or results must be disclosed on submission, in the methods or acknowledgements (see AI Policy) |
| **Open access and cost** | No fees to submit or publish; optional open access for a fee, amount not read; colour in print $800 plus $200 per additional image (see Open Access) |
| **Funding and permissions** | A funding statement and a conflict-of-interest declaration are required; permissions for reproduced material must be supplied (instructions copy 2025-08-12) |
| **Prior and parallel publication** | The manuscript must be original work; SAGE's prior-publication guidance is linked from the preprint paragraph (instructions copy) |

### AI-Research Notes (sources, blanks, and cross-language checks)

**signal_quality (0-5)**: overall 2. Per layer: Crossref counts (methods, topics by wording, authors) 3 (abstract coverage 85.0%; no country data); journal-specific policies and guidelines 3 (live pages read in a real browser 2026-11-23); editorial board 3 (live page read 2026-11-23); experiential layer 0 (SciRev has a page but no reviews).

**Sources cited across this entry:**
- Wayback copies of journals.sagepub.com pages fetched with `curl --compressed` and the `id_` route: home (2026-10-16), author instructions (2025-08-12), editorial board (2022-02-15; the first try returned 429, a second try returned the page); each URL given where used. Live requests returned HTTP 403 (3 tries each, 2026-11-23).
- https://api.crossref.org/journals/1046-8781 ; Crossref works for the window (220 records, 187 with abstract); Crossref citation counts sorted for the window
- Local spine (OpenAlex snapshot 2026-07-13): works 1976, h-index 99, 2-year mean citedness 2.48, JUFO 1, Norwegian register 1
- https://jufo-rest.csc.fi/v1.1/kanava/67121 ; https://scirev.org/journal/simulation-and-gaming/

**Method notes:** Crossref abstracts were stripped of JATS markup and counted locally with the regexes below (Python re, IGNORECASE except FP). Share = hits / 187; hits count records, not occurrences. Broad patterns over-count: G17 matches "learning", "training" and "students"; G19 matches "player" in any sense; G20 matches "design" and "designers"; G21 matches any "simulat-" word, which is part of the journal's name; G10 matches the word "AI" in any case.

**Keyword regexes (exact):**
- G1 `\b(quantitative|statistical(ly)?|regression|ANOVA|surveys?|questionnaires?|structural equation|Likert)\b` ; G2 `\b(experiments?|experimental|quasi-experimental|randomi[sz]ed|control group|controlled trial|user study|user studies)\b`
- G3 `\b(interviews?|focus groups?|thematic analysis|grounded theory|qualitative|semi-structured)\b` ; G4 `\b(ethnograph\w*|netnograph\w*|participant observation|fieldwork)\b` ; G5 `\bautoethnograph\w*\b`
- G6 `\b(theoretical(ly)?|conceptual(ly)?|theori[sz](e|es|ed|ing)|philosoph\w*|ontolog\w*|phenomenolog\w*)\b` ; G7 `\bmixed[- ]methods?\b` ; G8 `\b(meta-analys[ei]s|systematic review|scoping review|literature review|systematic literature)\b`
- G9 `\b(close reading|close play|textual analysis|discourse analysis|content analysis|game analysis|critical analysis|rhetoric\w*|semiotic\w*)\b` ; G10 `\b(artificial intelligence|generative AI|ChatGPT|large language models?|LLMs?|AI|machine learning|reinforcement learning|neural|procedural content generation|deep learning)\b`
- G11 `\b(gender(ed)?|women|sexis\w*|feminis\w*|queer|LGBT\w*|transgender|non-?binary|sexuality|misogyn\w*)\b` ; G12 `\b(raci(al|alized|st|sm)|racio\w*|whiteness|antiracis\w*|ethnic(ity|ities)?|colonial\w*|decoloni\w*|indigenous)\b`
- G13 `\b(violen\w*|toxic\w*|harass\w*|extremis\w*|hate|abus\w*)\b` ; G14 `\b(politic\w*|ideolog\w*|fascis\w*|propaganda|censorship|labou?r|capitalis\w*)\b` ; G15 `\b(gambling|loot ?boxes?|monetization|monetisation|microtransactions?|gacha)\b`
- G17 `\b(learning|education\w*|gamification|serious games?|pedagog\w*|students?|training)\b` ; G18 `\b(addict\w*|gaming disorder|well-?being|mental health|depress\w*|anxiety|loneliness)\b` ; G19 `\b(players?|player experience|playe?rs?hip)\b`
- G20 `\b(game design|designers?|mechanics|level design|design)\b` ; G21 `\bsimulat\w*\b` ; FP (case-sensitive) `\b(I|[Ww]e|[Oo]ur|[Mm]y)\b`

**Unreadable pages (never filled from memory):**
- Read in a real browser 2026-11-23 (curl got 403): https://journals.sagepub.com/author-instructions/SAG , https://journals.sagepub.com/editorial-board/SAG , https://www.sagepub.com/journals/publication-ethics-policies/artificial-intelligence-policy , https://www.sagepub.com/author-archiving-and-re-use-msg
- Still not read: https://journals.sagepub.com/aims-scope/SAG , the linked manuscript-guidelines .docx (https://journals.sagepub.com/pb-assets/cmscontent/sag/SG%20Manuscript%20Submission%20Guidelines_2024-1738581514.docx), the open-access agreements list and the open-access fee amount
- The OpenAlex scaffold was not used (no OpenAlex request in this pass); OpenAlex ID, i10-index and OpenAlex topic counts are therefore not recorded.

**Fields deliberately left blank, and why:**
- Acceptance rate, desk rejection rate, review times, R+R rounds, transfer and cascade, reviewer reports published, reviewer list, special issues: no source on the pages read.
- APC amount: not on the pages read.
- Reviewer culture, competence variance, quantitative mindset bias: SciRev has no reviews.
- Author countries: Crossref has no country field.
- Impact factor and quartile: paywalled, not stated by policy.

**Cross-language and forum checks performed:**
- SciRev (English): journal page exists with popularity score and 0 reviews (https://scirev.org/journal/simulation-and-gaming/, read 2026-11-23).
- Web search (2026-11-23) "Simulation & Gaming journal SAGE 投稿 审稿 经验 OR reddit submission experience review time" returned official SAGE pages, an ABSEL paper from 2000 on the journal's review process (https://absel-ojs-ttu.tdl.org/absel/article/view/878; not read) and no Reddit, 小木虫 or 知乎 thread.
- LetPub and fabiaoji: not checked.

---

## Strategic Notes

> Each statement below follows from a fact recorded above and names it. Where the evidence does not support a statement, the field says so.

### Hard Blockers

- **Length by type**: 7000 words for research articles and 3000 for short reports, excluding references; more only with explicit editor permission (Format).
- **Anonymisation**: manuscripts must be fully anonymised with identifying information on a Title Page (Peer Review).
- **Ethics statement**: human-subjects work needs an IRB statement and an EQUATOR checklist (Practical Concerns).
- **Scope**: manuscripts out of scope may be desk rejected (Peer Review, Framing Requirements).

### Soft Tax

- **No timing information**: no publisher target and no SciRev entries exist, so planning a submission has no time anchor (Review Cycle Time).
- **Cost**: no submission or publication fee; optional open access carries a fee whose amount was not read; print colour costs $800 plus $200 per extra image (Open Access).
- **Structure**: the suggested Background, Intervention, Methods, Results, Discussion layout and the research-objective sentence add editing work for qualitative or theoretical papers (Format).

### Best Suited For

- Empirical studies of simulations, serious games and gamification in education and training, including health-professions education: G17 appears in 143 of 187 abstract-records and G21 in 91 (Orientation).
- Systematic reviews and meta-analyses, which the instructions encourage over literature reviews (Methodological Preferences).
- Classroom-ready games with evidence of effectiveness, a named article type (Format).

### Not Recommended For

- Cultural-critical or humanities game studies: race and colonial wording is 1 of 187 abstract-records (0.5%, G12) and politics wording 7 (3.7%, G14), so the evidence base here is thin (Sensitive Topics).
- Papers that need more than 7000 words before references (Format).
- Authors who need a decision-time estimate: none exists in the sources read (Review Cycle Time).

### Rejection Fallback Chain

> No source states where rejected authors usually go. The rows below are topical neighbours that exist in this corpus or in this directory, listed because they share subject area; they are not claims about acceptance odds.

| Rank | Journal | Why this fallback works |
|------|---------|------------------------|
| 1 | [Games and Culture](games-and-culture.md) | Social-science and humanities games journal; its G17 education wording is 38 of 319 abstract-records (11.9%) against 76.5% here (see that entry), so topical overlap is partial |
| 2 | [IEEE Transactions on Games](ieee-transactions-on-games.md) | Engineering-side games journal where titles with learning or serious-games wording are 107 of 424 (25.2%, see that entry) |
| 3 | [Entertainment Computing](../hci/entertainment-computing.md) | HCI-leaning neighbour already in the corpus; no fit evidence collected here |

---

## Changelog

| Date | Change | By |
|------|--------|----|
| 2026-11-23 | Initial entry (written from the local spine and Crossref; no import_openalex scaffold) | @your-handle |
| 2026-11-23 | AI deep research pass; no first-hand human reports | AI-assisted (maintainer-directed) |
| 2026-11-24 | Pages unreadable by curl re-read in a real browser (author instructions, editorial board, SAGE AI and archiving policies) | @Zaious |
| 2026-11-24 | Corrections after independent verification (AI-use row rewritten from the SAGE policy copy; real-browser board and archiving figures marked as not independently re-checked; 2022 board copy counts added) | @Zaious |
