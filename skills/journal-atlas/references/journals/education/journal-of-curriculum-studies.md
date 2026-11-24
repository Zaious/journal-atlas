<!-- schema: v1.3 -->
<!-- AI-researched entry — Journal Atlas v2 coverage pipeline. See docs/ATLAS_V2_DESIGN.md for methodology. -->
<!-- Scaffold values from the OpenAlex Sources API (scripts/import_openalex.py dry-run, 2026-11-23), then filled by an AI deep research pass (maintainer-directed) on 2026-11-23. -->

# Journal of Curriculum Studies

> **Last verified**: 2026-11-24
> **Maintainer**: @Zaious
> **Venue type**: Journal
> **Evidence basis**: Sourced under the written rule (SEED_DATA_QUALITY.md): deeper per-journal research by an AI model, directed by the maintainer, 2026-11-23; overall signal_quality **3/5**. Claims cite source URLs or counts; blanks are recorded with reasons. Independent spot-check on 2026-11-23: 7 of 7 sampled pairs supported. No first-hand human reports; not human-verified.

---

## Identity

| Field | Value |
|-------|-------|
| **Abbreviation** | JCS (no source read for an official abbreviation; the string is the usual initialism, not a sourced fact) |
| **Venue type** | Journal |
| **Publisher** | Taylor & Francis. Source: https://api.crossref.org/journals/0022-0272 (publisher string "Informa UK (Taylor & Francis)"; title "Journal of Curriculum Studies"; print ISSN 0022-0272 and electronic ISSN 1366-5839 both returned), retrieved 2026-11-23 |
| **ISSN (Print)** | 0022-0272 |
| **ISSN (Online)** | 1366-5839 |
| **Founded** | Not stated on any page read. The earliest year with Crossref-registered items is 1968 (https://api.crossref.org/journals/0022-0272, `dois-by-issued-year`; retrieved 2026-11-23); that is the earliest registered year, not a confirmed founding date |
| **URL** | https://www.tandfonline.com/toc/tcus20/current |
| **Author Guidelines** | https://www.tandfonline.com/action/authorSubmission?journalCode=tcus20&page=instructions, read in full in a real browser on 2026-11-24 (it returned HTTP 403 to curl on 2026-11-23; the page prints no date). Aims, peer-review line, metrics block and board: https://www.tandfonline.com/journals/tcus20/about-this-journal (read the same day, undated). The Wayback copy of 2022-02-18 (https://web.archive.org/web/20220218183941id_/https://www.tandfonline.com/action/authorSubmission?journalCode=tcus20&show=instructions&) is older and differs on two points: the live abstract is unstructured (the 2022 copy asked for a structured one) and the live instructions say single anonymous review (the 2022 copy said double blind). Notes: chrome2/jcs-pages.txt in the researcher's scratch folder |
| **Society / Association** | None found in the pages read |
| **Editorial Board Location** | OpenAlex source country code: GB (https://openalex.org/S198786835). The live board on the journal's about page (https://www.tandfonline.com/journals/tcus20/about-this-journal, read in a real browser 2026-11-24, no date printed) lists 25 people (see Editorial-board geography), with the General Editor, Zongyi Deng, at UCL Institute of Education, University College London, UK, two executive editors at the University of Sussex (UK) and Western University (Canada), and a managing editor at the University of Duisburg-Essen (Germany). This confirms what a search-engine summary had shown on 2026-11-23 |
| **OpenAlex ID** | https://openalex.org/S198786835 |

---

## Metrics

> Source: OpenAlex (CC0), retrieved 2026-11-23 (scaffold values from the Sources API). JCR impact factor and quartile are paywalled and deliberately not stated. The 2-year mean citedness below is an OpenAlex proxy, not a JCR figure. The local spine (an OpenAlex snapshot dated 2026-07-13, `scripts/query_spine.py`) gives works_count 2775 and h-index 113 for the same ISSN; the live scaffold values below are newer.

| Metric | Value | Date |
|--------|-------|------|
| **Impact Factor** | Not stated (JCR is paywalled) | |
| **5-Year IF** | Not stated (JCR is paywalled) | |
| **h-index** | 137 (OpenAlex) | 2026-11-23 |
| **CiteScore** | 4.8, labelled "(2025) CiteScore (Scopus)" on the publisher's about-this-journal page (https://www.tandfonline.com/journals/tcus20/about-this-journal, read in a real browser 2026-11-24); Scopus itself was not opened. The same page prints Clarivate impact-factor and quartile figures, which are deliberately not recorded here | 2025 (label on page) |
| **Acceptance Rate** | 10% acceptance rate on the live publisher metrics block (https://www.tandfonline.com/journals/tcus20/about-this-journal, read in a real browser 2026-11-24); the block prints no period next to its speed and acceptance figures. This confirms the figure a search-engine summary had shown on 2026-11-23. LetPub's journal page displays a "competitiveness" of 7% with no stated provenance (https://www.letpub.com/journal-selector/journal/12317); it is secondary, unverified, and not used | 2026-11-24 (no period on live block) |
| **Desk Rejection Rate** | Blank. No source found: SciRev lists no reviews (https://scirev.org/journal/journal-of-curriculum-studies/) and LetPub lists 0 reviews (https://www.letpub.com/journal-selector/journal/12317) | 2026-11-23 |
| **Quartile (by field)** | Not stated (SJR not read). The local spine records JUFO level 3 for this ISSN (Finnish publication forum, spine snapshot 2026-07-13) | |
| **2-yr Mean Citedness (OpenAlex IF proxy)** | 5.51 (OpenAlex proxy, not JCR) | 2026-11-23 |
| **i10-index** | 1389 (OpenAlex) | 2026-11-23 |
| **Total Works** | 2764 (OpenAlex, all years and work types) | 2026-11-23 |

### Review Cycle Time

| Stage | Typical Time | Notes |
|-------|-------------|-------|
| **Time to first decision** | Publisher-reported, live block (https://www.tandfonline.com/journals/tcus20/about-this-journal, read 2026-11-24, no period printed): 8 days average from submission to first decision and 93 days average from submission to first post-review decision. SciRev has no reviews for this journal (https://scirev.org/journal/journal-of-curriculum-studies/) | Publisher averages, period not stated |
| **Time to first review** | Blank. No separate figure found | |
| **Time to acceptance (total)** | Blank. SciRev has no reviews (https://scirev.org/journal/journal-of-curriculum-studies/); LetPub has 0 reviews, and its displayed "average peer review 24 weeks" has no stated provenance (https://www.letpub.com/journal-selector/journal/12317), so it is not used | |
| **Time to publication (after acceptance)** | 30 days average from acceptance to online publication, publisher-reported on the live metrics block (https://www.tandfonline.com/journals/tcus20/about-this-journal, read 2026-11-24, no period printed) | Period not stated |

### Publication Frequency

| Aspect | Detail |
|--------|--------|
| **Schedule** | Six issues per year: the journal-information page, Wayback copy dated 2023-04-01 (https://web.archive.org/web/20230401175612id_/https://www.tandfonline.com/action/journalInformation?journalCode=tcus20), says 6 issues per year |
| **Articles per year (approx.)** | Crossref journal-article records by published year (https://api.crossref.org/journals/0022-0272/works?filter=from-pub-date:2021-01,until-pub-date:2026-12, 327 records, all of type journal-article): 2021 = 55, 2022 = 22, 2023 = 54, 2024 = 65, 2025 = 75, 2026 = 56 (partial year, latest record dated 2026-11-13). The 2022 dip is in the Crossref data; its cause was not investigated. Retrieved 2026-11-23 |
| **Special issues?** | Yes, themed issues and sections appear: the journal home copy of 2025-05-12 lists the issue "Social realism, knowledge and curriculum: furthering the conversation" (volume 57 issue 1, 2025; https://web.archive.org/web/20250512214347id_/https://www.tandfonline.com/journals/tcus20). Crossref records introductions to themed collections, for example https://doi.org/10.1080/00220272.2022.2070716, https://doi.org/10.1080/00220272.2023.2172361 and https://doi.org/10.1080/00220272.2023.2298461 |

---

## Policies

### Peer Review

| Aspect | Detail |
|--------|--------|
| **Type** | Single anonymous on the instructions page: the live instructions say that once the editor has assessed suitability the paper is "single anonymous peer reviewed by two independent, anonymous expert" referees, and warn that anonymity cannot be guaranteed for a manuscript shared on a preprint server (https://www.tandfonline.com/action/authorSubmission?journalCode=tcus20&page=instructions, read 2026-11-24). The live about page says: "All research articles in this journal have undergone rigorous peer review, based on initial editor screening and external refereeing by at least two anonymous referees" and does not say who is anonymous to whom (https://www.tandfonline.com/journals/tcus20/about-this-journal). Older, kept as older: the 2022-02-18 instructions copy said "double blind" (https://web.archive.org/web/20220218183941id_/https://www.tandfonline.com/action/authorSubmission?journalCode=tcus20&show=instructions&). Retrieved 2026-11-24 |
| **Transferable / Cascade?** | Blank. No source read |
| **Reviewer reports published?** | Blank. No statement found in the pages read |
| **Typical R+R rounds** | Blank. No source found |
| **Reviewer recommendations** | Blank. No source found |

### AI Policy

| Aspect | Detail |
|--------|--------|
| **Has journal-specific AI policy?** | Partly. The live instructions page (read in a real browser 2026-11-24) asks every submission to include a "Declaration of generative AI use": a statement disclosing whether and how generative AI was used in the research and manuscript preparation (https://www.tandfonline.com/action/authorSubmission?journalCode=tcus20&page=instructions). The 2022-02-18 copy predates this. The publisher-wide Taylor & Francis policy applies; that policy itself warns that some journals may restrict AI use beyond language improvement and tells authors to check the journal's instructions |
| **Explicit permission gate?** | No gate found. Use is allowed with a mandatory disclosure statement |
| **Leniency (1-5)** | 3 (allowed with mandatory disclosure; same rubric as the Mind entry) |
| **Summary** | Publisher policy: AI tools cannot be listed as authors. Authors must acknowledge any generative AI use in a specific statement giving the tool name and version, how it was used and why. Text or code generation without rigorous revision, synthetic data standing in for missing data, and AI creation or manipulation of research outputs or images are not permitted. Retrieved 2026-11-23 |
| **Source URL** | https://taylorandfrancis.com/our-policies/ai-policy/ |

### Preprint Policy

> Publisher-level policy, not journal-specific. Source: https://authorservices.taylorandfrancis.com/research-impact/sharing-versions-of-journal-articles/ (retrieved 2026-11-23). The journal-specific embargo period was not looked up.

| Stage | Allowed? | Notes |
|-------|----------|-------|
| Pre-submission | Yes | The page says the original manuscript may be shared as much as the author likes, including on non-commercial preprint servers such as SocArXiv, and that doing so is not duplicate publication. The journal's own instructions (Wayback copy 2022-02-18, https://web.archive.org/web/20220218183941id_/https://www.tandfonline.com/action/authorSubmission?journalCode=tcus20&show=instructions&) add that anonymity cannot be guaranteed once a version is on a preprint server |
| Under review | Blank | The page speaks of the pre-submission version; it does not separately address the under-review stage |
| Post-acceptance (AAM) | Yes, with embargo | The accepted manuscript may go on the author's own website after publication; repositories and scholarly networks after an embargo that the page gives as typically 18 months for the social sciences and humanities portfolio, counted from publication of the Version of Record. Embargo: 18 months is the publisher's typical figure, not confirmed for this journal |
| Version of Record | Open access articles may be shared freely | Per the same page; non-open-access articles via publisher eprint links |

### Open Access

| Aspect | Detail |
|--------|--------|
| **Model** | Hybrid (Taylor & Francis Open Select). Evidence: the instructions (copy 2022-02-18) describe the Open Select route; five of the six most recent articles listed on the journal home copy of 2025-05-12 carry an "Open Access" label (recounted from the archived page on 2026-11-23: the articles dated 30 Apr, 28 Apr twice, 26 Apr and 24 Apr 2025 carry it; the one dated 8 May 2025 does not) (https://web.archive.org/web/20250512214347id_/https://www.tandfonline.com/journals/tcus20); Open Select described at https://authorservices.taylorandfrancis.com/publishing-open-access/open-select/ |
| **APC (if OA chosen)** | Blank. The live instructions refer to the publisher's APC finder without printing an amount (read 2026-11-24); the finder was not read. Non-OA route: the live instructions state there are no submission fees, publication fees or page charges for this journal; print colour figures are charged (GBP 300 per figure in the 2022-02-18 copy; not re-read) |
| **Gold OA offered?** | Yes, per the instructions and the article labels above |
| **Read & Publish agreements** | Blank. No list read |

---

## Format

> Source for the general rules: the journal's live instructions for authors (https://www.tandfonline.com/action/authorSubmission?journalCode=tcus20&page=instructions), read in a real browser on 2026-11-24; the page prints no date. Retrieved 2026-11-24. The Wayback copy of 2022-02-18 is older; rows that rest only on it say so.

| Aspect | Detail |
|--------|--------|
| **Article types accepted** | Papers reporting research studies, critical essays, case studies and essay reviews; manuscripts in English only (archived instructions, 2022-02-18). Crossref lists all 327 records since 2021 as journal articles; no type split is available there |
| **Word limit** | "A typical paper for this journal should be no more than 10000 words, inclusive of" tables, references, figure or table captions, footnotes and endnotes (live instructions, read 2026-11-24; same figure in the 2022-02-18 copy). Crossref page ranges give a median article length of 19 pages (quartiles 16 and 22) over 319 of 327 records, 2021-2026 |
| **Word limit negotiability** | Blank. The live instructions word the limit as typical ("a typical paper"); no statement on exceptions found |
| **Abstract limit** | Unstructured abstract of 200 words; no more than 5 keywords (live instructions, read 2026-11-24). Older, kept as older: the 2022-02-18 copy asked for a structured abstract of 200 words covering objective, design, methods, results and conclusions |
| **Reference limit** | No separate cap found; references count inside the 10000 words (live instructions, read 2026-11-24) |
| **Supplementary material** | Supplemental material (video, dataset, files) is published via Figshare (archived instructions, 2022-02-18) |
| **Figure/Table limits** | No count limit found. Resolution and editable-table requirements are in the archived instructions; extra colour is charged only for print |
| **Style / submission format** | British (-ize) spelling used consistently; single quotation marks; authors are told to follow the quick style guidelines rather than published articles (live instructions, read 2026-11-24). Word or LaTeX, the publisher's reference guide (style not named in the text read), ScholarOne submission, Crossref similarity screening and full name and affiliation on the cover page are from the 2022-02-18 copy and were not re-checked |

---

## Subject Density

> Top Topics come from the OpenAlex works API, retrieved 2026-11-25 (request URL under the table); the Orientation counts below come from Crossref records, with abstracts from Semantic Scholar where stated there, retrieved 2026-11-23.

### Top Topics (last 5 years)

> Source: OpenAlex works API, source S198786835, works of type article dated 2021-11-23 to 2026-11-23 (261 works), grouped by topic: https://api.openalex.org/works?filter=primary_location.source.id:S198786835,type:article,from_publication_date:2021-11-23,to_publication_date:2026-11-23&group_by=topics.id . Retrieved 2026-11-25. 156 topics were returned; the top 10 are shown. These are OpenAlex topic-assignment counts, not article counts: a work can carry several topics, so the counts do not sum to 261.

| Topic | Article Count |
|-------|--------------|
| Educational Theory and Curriculum Studies | 142 |
| Educator Training and Historical Pedagogy | 60 |
| Education Pedagogy and Practices | 52 |
| Teacher Education and Leadership Studies | 50 |
| Mathematics Education and Teaching Techniques | 31 |
| Global Educational Policies and Reforms | 26 |
| Education, Philosophy, and Society | 20 |
| Critical Race Theory in Education | 16 |
| Historical Education Studies Worldwide | 15 |
| Citizenship Education and Democracy | 14 |

### Orientation

> Counts come from 327 Crossref journal-article records published 2021-01 to 2026-11 (https://api.crossref.org/journals/0022-0272/works?filter=from-pub-date:2021-01,until-pub-date:2026-12). Crossref holds no abstracts for this journal, so abstracts for 256 of the 327 records (78.3%) were taken from the Semantic Scholar API (https://api.semanticscholar.org/graph/v1/paper/batch, by DOI). Hits are counted over title plus abstract as a share of the 256; they are lower bounds. Regexes are listed in AI-Research Notes. Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Empirical vs. Theoretical** | Theoretical wording predominates: "theor-" 100 (39.1%) and "conceptual" 47 (18.4%) against "interview" 38 (14.8%), "survey/questionnaire" 20 (7.8%) and "regression/longitudinal/cohort" 9 (3.5%) of 256 records with abstracts |
| **Quantitative vs. Qualitative** | Qualitative wording is more frequent: "qualitative" 30 (11.7%), "quantitative" 11 (4.3%), "mixed methods" 7 (2.7%) of 256 |
| **Cross-disciplinary openness** | The aims text asks for a broad cross-disciplinary discourse in curriculum studies and welcomes empirical, philosophical, sociological and policy-related investigations (journal home copy dated 2025-05-12, https://web.archive.org/web/20250512214347id_/https://www.tandfonline.com/journals/tcus20). Curriculum 160 (62.5%), teacher 128 (50.0%), policy 51 (19.9%) and assessment 37 (14.5%) of 256 |

---

## Soft Metadata

### Epistemological & Political Leanings

> Evidence layers: Crossref records (327; abstracts for 256 via Semantic Scholar) and Crossref author affiliations; the journal's aims text (Wayback copy 2025-05-12). OpenAlex keyword counts were not obtained (rate limit). Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Cross-cultural friendliness** | Author countries taken from Crossref affiliation strings (766 of 818 authors, 94%, name a recognised country; counts are articles with at least one author in the country, of 327 articles): United States 61, United Kingdom 49, Sweden 41, Norway 29, Germany 27, Australia 21, Finland 21, China 18, Netherlands 14, South Africa 11, Ireland 10, Turkey 10, Israel 10, Belgium 8 (https://api.crossref.org/journals/0022-0272/works; the pattern lists country names and abbreviations such as UK and USA, and an affiliation naming Northern Ireland counts for both the United Kingdom and Ireland). The aims text asks authors what "a reader in Osaka, Pretoria, Berlin, or Toronto" would take from the paper (journal home copy 2025-05-12) |
| **Editorial-board geography** | Live about page (https://www.tandfonline.com/journals/tcus20/about-this-journal, read in a real browser 2026-11-24, no date printed): 25 people by first-listed affiliation: United States 5, Austria 4, Germany 3, United Kingdom 2, Canada 2, Australia 2, and one each in South Africa, Brazil, New Zealand, Norway, Singapore, Sweden and China (5 + 4 + 3 + 2 + 2 + 2 + 7 = 25). Roles: 1 General Editor, 2 Executive Editors, 1 Managing Editor, 18 Associate Editors, 1 Advisory Editor and 2 General Editor Emeriti (1 + 2 + 1 + 18 + 1 + 2 = 25). One emeritus entry lists two countries (Austria and Norway) and is counted under the first |
| **Non-Western epistemology openness** | Keyword count, title plus abstract of 256 records: "decolonial/Indigenous/Maori/Aboriginal" 12 (4.7%). The aims text describes a journal "accessible to all the national, cultural, and discipline-defined communities" among its readership (journal home copy 2025-05-12, short quote) and states that it does not subscribe to any particular methodology or theory |
| **Diversity topic receptiveness** | Counts of 256 records with abstracts: race/racism/ethnic 27 (10.5%), gender/feminism/women/girls 7 (2.7%), social class/inequality/disadvantage 13 (5.1%), disability/special needs/inclusion 22 (8.6%), queer/LGBT/transgender/sexuality 0. The journal states no editorial position on these topics in the pages read; one of the most cited 2021-2026 items is a critical analysis of race in a scripted reading curriculum (https://doi.org/10.1080/00220272.2022.2030803) |
| **Dominant theoretical tradition** | No single tradition stated: the aims text says the journal does not subscribe to any particular methodology or theory. Named theorists (Bourdieu, Foucault, Marx, Freire, Dewey, Deleuze, Arendt, Habermas) appear in 13 of 256 records (5.1%). The most cited 2021-2026 items in Crossref (citation counts at retrieval) include a Bernsteinian analysis of micro-credentials (146; https://doi.org/10.1080/00220272.2021.1887358), "Powerful knowledge, educational potential and knowledge-rich curriculum" (99; https://doi.org/10.1080/00220272.2022.2089538), "Trajectories of powerful knowledge and epistemic quality" (46; https://doi.org/10.1080/00220272.2023.2182164) and "Constructing 'powerful' curriculum theory" (37; https://doi.org/10.1080/00220272.2021.1887361), and the 2025 issue theme is social realism and curriculum (journal home copy 2025-05-12). The journal states no political position on any page that could be read |

### Framing Requirements

- **Mandatory framing?** Yes, stated by the journal itself: authors must connect their papers explicitly to the current discourse in curriculum studies and show why the contribution matters to the broader community, and are encouraged to relate their findings to longstanding strands of conversation in the journal (aims text, journal home copy dated 2025-05-12, https://web.archive.org/web/20250512214347id_/https://www.tandfonline.com/journals/tcus20; retrieved 2026-11-23).
- **What kind of engagement?** An international and cross-disciplinary one: the aims ask what a reader in another national context would take from the paper, and what the significance is for the issues examined, the approach employed and the resolutions reached (same aims text). The journal states that it does not subscribe to any particular methodology or theory.
- **Article type and length**: papers reporting research studies, critical essays, case studies and essay reviews; a typical paper up to 10000 words including references; structured abstract of 200 words; up to five keywords (instructions copy dated 2022-02-18, https://web.archive.org/web/20220218183941id_/https://www.tandfonline.com/action/authorSubmission?journalCode=tcus20&show=instructions&).
- **Special-issue framing seen**: the 2025 issue theme "Social realism, knowledge and curriculum: furthering the conversation" (journal home copy 2025-05-12); introductions to themed collections on teacher professional learning, teaching as pedagogical responsibility and differentiation through curriculum (https://doi.org/10.1080/00220272.2022.2070716, https://doi.org/10.1080/00220272.2023.2172361, https://doi.org/10.1080/00220272.2023.2298461).
- **Consequences of ignoring it**: Blank. No source states what happens to out-of-scope submissions, and no desk-rejection data exists (SciRev has no reviews: https://scirev.org/journal/journal-of-curriculum-studies/).

### Methodological Preferences

> Counts are Crossref records (327) published 2021-01 to 2026-11 whose title or abstract matches the regex (abstracts for 256 records, 78.3%, from Semantic Scholar by DOI); shares use 256 as the denominator. Scoring convention of this research pass (its own, not an external standard): share 0 = 0; under 1% = 1; 1-5% = 2; over 5% = 3; 4-5 only with a cited editorial statement. The journal's statement that it does not subscribe to any particular methodology or theory (aims text, journal home copy 2025-05-12) argues against rating one method above another, so no score above 3 is given. Scores measure how often a method appears, not how a reviewer would judge it. Regexes are in AI-Research Notes.

| Method | Receptiveness (0-5) | Evidence |
|--------|---------------------|----------|
| Quantitative experimental | 1 | "randomised/randomization/RCT/experiment" 2 of 256 (0.8%); "quantitative" 11 (4.3%) |
| Survey and regression / longitudinal | 3 | "survey/questionnaire" 20 (7.8%); "regression/longitudinal/panel data/cohort" 9 (3.5%, which alone scores 2) |
| Qualitative interviews | 3 | "interview" 38 (14.8%); "qualitative" 30 (11.7%) of 256 |
| Case study | 3 | "case study" 19 (7.4%) of 256; case studies are a listed article type (instructions copy 2022-02-18) |
| Ethnography | 1 | "ethnograph" 1 (0.4%) of 256; "autoethnography" was not counted separately |
| Discourse analysis | 3 | "discourse" 39 (15.2%) of 256 |
| Theoretical / Conceptual | 3 | "theor-" 100 (39.1%); "conceptual" 47 (18.4%); "philosoph-" 18 (7.0%); critical essays are a listed article type |
| Mixed methods | 2 | "mixed method" 7 (2.7%) of 256 |
| Systematic / literature review | 2 | "systematic review, meta-analysis, scoping review, literature review" 4 (1.6%) of 256 |

### Voice & Style

| Aspect | Detail |
|--------|--------|
| **First-person voice acceptance (0-5)** | Not scored. Sample: of the 100 most recently dated articles with an abstract (Crossref plus Semantic Scholar, dated up to 2026-11-13), 29 abstracts contain I, my, we or our and 7 contain I or my; across all 256 abstracts, 106 contain one of those words (plural "we" may be generic rather than authorial). Records containing I or my include https://doi.org/10.1080/00220272.2026.2680403 and https://doi.org/10.1080/00220272.2025.2531369. The archived instructions give no rule on first person. Retrieved 2026-11-23 |
| **Expected density** | Crossref page ranges give a median article length of 19 pages across 319 of 327 records (quartiles 16 and 22; 2021-2026; https://api.crossref.org/journals/0022-0272/works?filter=from-pub-date:2021-01,until-pub-date:2026-12). Length ceiling: about 10000 words including references (live instructions, read 2026-11-24) |
| **Abstract and keywords** | Unstructured abstract of 200 words and no more than 5 keywords (live instructions, read 2026-11-24, https://www.tandfonline.com/action/authorSubmission?journalCode=tcus20&page=instructions); the 2022-02-18 copy asked for a structured abstract |
| **Writing style notes** | Archived instructions (2022-02-18): British (-ize) spelling used consistently; single quotation marks; long quotations indented without marks; English only; authors told to follow the quick style guidelines rather than copy published articles. The same page gives a generic empirical section order (introduction, materials and methods, results, discussion), which is publisher template text; the aims text instead stresses explicit connection to the discourse of curriculum studies |
| **Authorship pattern** | Of 314 Crossref records with author lists (2021-01 to 2026-11): 110 single-author, 93 two authors, 57 three, 54 four or more (retrieved 2026-11-23); 39 of the 100 most recent records with an abstract are single-author |

### Reviewer Pool Characteristics

Reviewer behaviour itself is not observable from public pages; what follows is what public pages do show.

| Aspect | Detail | Evidence |
|--------|--------|----------|
| **Dominant tradition** | The live board lists 25 people with institutions but no disciplines, so no discipline split is given. The aims text says the journal is the prime international source for curriculum research and addresses readers in several national contexts | https://www.tandfonline.com/journals/tcus20/about-this-journal (live board, counted 2026-11-24); https://web.archive.org/web/20250512214347id_/https://www.tandfonline.com/journals/tcus20 (2025-05-12 copy); retrieved 2026-11-24 |
| **Review model** | Single anonymous per the live instructions; initial editor screening, then at least two anonymous external referees per the about page | Live instructions and about page (URLs in Peer Review), read 2026-11-24 |
| **Reviewer competence variance** | Blank. No first-hand report exists: SciRev has no reviews and LetPub 0 reviews | https://scirev.org/journal/journal-of-curriculum-studies/ ; https://www.letpub.com/journal-selector/journal/12317 |
| **Quantitative mindset bias on qualitative work?** | Blank. No source. Qualitative and survey work both appear (qualitative 11.7%, survey 7.8% of 256 records), but theoretical wording is far more frequent (theor- 39.1%), which cannot tell how reviewers treat any of them | Counts in Methodological Preferences |
| **Discourse community signals (author side)** | Author community as a proxy, not a reviewer list: United States 61, United Kingdom 49, Sweden 41, Norway 29, Germany 27 articles with at least one author affiliated there (Crossref affiliation strings, 327 articles, 2021-01 to 2026-11) | https://api.crossref.org/journals/0022-0272/works ; retrieved 2026-11-23 |

### Sensitive Topics

> Counts are Crossref records (327) with abstracts for 256, title plus abstract, as shares of 256 (Semantic Scholar abstracts by DOI; lower bounds). "Receptiveness" cells give frequency only; no editorial statement was found on these topics, so no row is rated High.

| Topic Category | Receptiveness | Evidence |
|----------------|---------------|----------|
| Decolonial / Indigenous | Present, small | 12 of 256 (4.7%) |
| Gender and feminism | Present, small | 7 of 256 (2.7%) |
| Race and ethnicity | Present | 27 of 256 (10.5%); https://doi.org/10.1080/00220272.2022.2030803 |
| Sexual and gender minorities | Rare | 0 of 256 for queer, LGBT, transgender or sexuality |
| Religion | Present, small | 9 of 256 (3.5%) |
| Political conflict, migration | Present | "war, conflict, refugee, migra-" 19 of 256 (7.4%); a 2026 article on war in Israeli history curricula and textbooks (https://doi.org/10.1080/00220272.2026.2744571) |
| AI and technology | Rare | "artificial intelligence, AI, ChatGPT, generative, machine learning, algorithm" 3 of 256 (1.2%) |
| Climate | Present, small | "climate, sustainab-, Anthropocene, ecolog-" 12 of 256 (4.7%) |
| Inequality, disability | Present | social class/inequality 13 (5.1%); disability/special needs/inclusion 22 (8.6%) of 256 |

### Practical Concerns

| Concern | Detail |
|---------|--------|
| **IRB requirement strictness** | Blank for any journal-specific ethics-approval rule: the archived instructions (2022-02-18) point to the publisher's publishing-ethics guidance and contain no journal-specific ethics text in the part read (https://web.archive.org/web/20220218183941id_/https://www.tandfonline.com/action/authorSubmission?journalCode=tcus20&show=instructions&) |
| **Single-author acceptance** | Single-author papers are common: 110 of 314 Crossref records with author lists (35.0%) published 2021-01 to 2026-11 (https://api.crossref.org/journals/0022-0272/works?filter=from-pub-date:2021-01,until-pub-date:2026-12; retrieved 2026-11-23) |
| **Independent scholar friendliness** | The archived instructions define the affiliation as where the research was conducted and state no independent-scholar rule (https://web.archive.org/web/20220218183941id_/https://www.tandfonline.com/action/authorSubmission?journalCode=tcus20&show=instructions&). No affiliation breakdown for independent scholars was obtained |
| **Data transparency requirement** | The journal applies the Taylor & Francis Basic Data Sharing Policy: data sharing is encouraged, not required; authors are asked at submission whether a data set exists and for its identifier; data sets are not peer reviewed (archived instructions, 2022-02-18) |
| **OPSEC compatibility** | The live instructions say single anonymous review (reviewers anonymous) and warn that a preprint removes any anonymity guarantee (https://www.tandfonline.com/action/authorSubmission?journalCode=tcus20&page=instructions, read 2026-11-24); the 2022-02-18 copy called the review double blind and asked for name and affiliation on the cover page. Pre-submission preprints are allowed by the publisher (https://authorservices.taylorandfrancis.com/research-impact/sharing-versions-of-journal-articles/) |
| **AI use** | Disclosure statement required; AI cannot be an author (https://taylorandfrancis.com/our-policies/ai-policy/), retrieved 2026-11-23 |
| **Open access and cost** | Hybrid; no submission or page charges on the non-OA route (archived instructions, 2022-02-18); APC for open access not read (https://authorservices.taylorandfrancis.com/publishing-open-access/open-select/) |
| **Originality screening** | All submissions are screened for unoriginal material with Crossref similarity checking (archived instructions, 2022-02-18) |

### AI-Research Notes (sources, blanks, and cross-language checks)

**signal_quality (0-5)**: overall 3. Per layer: Crossref plus Semantic Scholar keyword counts 3 (256 of 327 abstracts, lower bounds); Crossref affiliation-based author countries 3; OpenAlex 1 (scaffold values only; no keyword or country counts were obtained because the shared rate limit was reached; the topic table was added on 2026-11-25 from one OpenAlex request); publisher-wide policies 4; journal-specific policies and guidelines 4 (live instructions and about pages read in a real browser 2026-11-24, undated; the 2022 and 2025 Wayback copies are kept as labelled older figures); experiential layer 0.

**Method note**: keyword counts use Crossref records (journal-article type, published 2021-01-01 to 2026-11-23, `select` fields DOI, title, abstract, author, page) with abstracts from the Semantic Scholar batch API by DOI (256 of 327 returned; the other 71 are counted by title only, which lowers every share). Matching is case-insensitive over title plus abstract with these regexes (Python `re`, `\b` word boundary at the start): qualitative `\bqualitative`; quantitative `\bquantitative`; interview `\binterview`; survey `\bsurvey|\bquestionnaire`; randomised/experiment `\brandomi[sz]ed|\brandomi[sz]ation|\bRCT\b|\bexperiment`; mixed methods `\bmixed[- ]method`; reviews `\bsystematic review|\bmeta-analys|\bscoping review|\bliterature review`; ethnography `\bethnograph`; case study `\bcase stud`; theory `\btheor(y|ies|etical|ising|izing|ise|ize)\b`; conceptual `\bconceptual`; philosophy `\bphilosoph`; regression/longitudinal `\bregression|\blongitudinal|\bpanel data|\bcohort`; discourse `\bdiscourse`; decolonial/Indigenous `\bdecolon|\bindigenous|\bfirst nations|\bm[aā]ori|\baboriginal`; gender `\bgender|\bfeminis|\bwomen\b|\bgirls\b`; race `\brac(e|ism|ist|ial|ialised|ialized)\b|\bwhiteness|\bblack\b|\bethnic`; class/inequality `\bsocial class|\bworking[- ]class|\binequalit|\bsocio-?economic|\bdisadvantage`; AI `\bartificial intelligence|\bAI\b|\bChatGPT|\bgenerative|\bmachine learning|\balgorithm`; queer `\bqueer|\blgbt|\btransgender|\bsexualit`; religion `\breligio|\bislam|\bmuslim|\bchristian|\bspiritual`; named theorists `\bbourdieu|\bfoucault|\bmarx|\bfreire|\bdewey|\bdeleuze|\barendt|\bhabermas`; climate `\bclimate|\bsustainab|\banthropocene|\becolog`; conflict `\bwar\b|\bconflict|\brefugee|\bmigra`; disability `\bdisabilit|\bspecial (educational )?needs|\bautis|\bdyslexi|\bSEND?\b|\binclusi`; first person `\b(I|my|we|our)\b` on abstracts. Country counts match country names and abbreviations (for example `\bUK\b`, `\bUSA\b`, `\bUS\b`) in Crossref affiliation name and place strings; affiliations without a country name (for example a bare university name) are unmatched. Some patterns are broad ("black", "conflict", "experiment", "inclusi") and may over-count.

**Sources cited across this entry:**
- https://web.archive.org/web/20220218183941id_/https://www.tandfonline.com/action/authorSubmission?journalCode=tcus20&show=instructions& (instructions, Wayback copy 2022-02-18)
- https://web.archive.org/web/20250512214347id_/https://www.tandfonline.com/journals/tcus20 (journal home with aims text, Wayback copy 2025-05-12)
- https://web.archive.org/web/20230401175612id_/https://www.tandfonline.com/action/journalInformation?journalCode=tcus20 (journal information, Wayback copy 2023-04-01)
- https://api.crossref.org/journals/0022-0272 and https://api.crossref.org/journals/0022-0272/works (327 journal-article records 2021-01 to 2026-11)
- https://api.semanticscholar.org/graph/v1/paper/batch (abstracts by DOI)
- https://taylorandfrancis.com/our-policies/ai-policy/
- https://authorservices.taylorandfrancis.com/research-impact/sharing-versions-of-journal-articles/
- https://authorservices.taylorandfrancis.com/publishing-open-access/open-select/
- https://scirev.org/journal/journal-of-curriculum-studies/
- https://www.letpub.com/journal-selector/journal/12317

**Unreadable pages (never filled from memory):**
- None among the journal's own main pages as of 2026-11-24: the instructions page (https://www.tandfonline.com/action/authorSubmission?journalCode=tcus20&page=instructions) and the about page with metrics and board (https://www.tandfonline.com/journals/tcus20/about-this-journal), both HTTP 403 to curl on 2026-11-23, were read in a real browser; nothing was clicked. The live metrics block shows 8 days, 93 days and 10%, which matches the search-engine summary of 2026-11-23, so the earlier suspicion that the summary mixed this journal with another is not supported. The aims text still comes from the 2025-05-12 home copy. The about page prints Clarivate impact-factor and quartile figures, which are deliberately not recorded. Notes: chrome2/jcs-pages.txt in the researcher's scratch folder.

**Fields deliberately left blank, and why:**
- Acceptance rate, desk rejection rate, review times, reviewer culture, reviewer competence variance, quantitative bias: no first-hand source exists; SciRev has no reviews and LetPub 0 reviews (LetPub's displayed 24 weeks and 7% have no stated provenance).
- APC, ethics-approval rule: the cost finder was not read, and the live instructions state no ethics rule in the passages read.
- Impact factor, quartile: paywalled, not stated by policy. OpenAlex topic table: added on 2026-11-25 from one works-API request (see Subject Density).

**Cross-language and forum checks performed (all returned zero journal-specific first-hand reports):**
- SciRev (English): journal page exists, no reviews (https://scirev.org/journal/journal-of-curriculum-studies/).
- LetPub: journal page exists, 0 reviews (https://www.letpub.com/journal-selector/journal/12317).
- 小木虫 (muchong) and 知乎 (zhihu): web search "Journal of Curriculum Studies 投稿 审稿周期 经验 小木虫 知乎" returned no muchong or zhihu thread; one Chinese journal-listing site (iikx.com) came back.
- fabiaoji: not reached by the web search; not checked directly.
- Reddit: web search for the journal name with "submission experience review time desk reject reddit OR letpub" returned no Reddit thread. A BERA blog post quoting a 63 per cent desk-rejection rate (https://www.bera.ac.uk/?p=42570) is about a different journal and is not used.

---

## Strategic Notes

> Each statement below follows from a fact recorded above and names it. Where the evidence does not support a statement, the field says so.

### Hard Blockers

- **Scope**: the aims text requires authors to connect papers explicitly to the current discourse in curriculum studies and to show relevance for the broader community (Framing Requirements; journal home copy 2025-05-12). A paper with no engagement with curriculum studies is outside the stated scope.
- **Length**: a typical paper should not exceed 10000 words, references and notes included (Format; live instructions read 2026-11-24). A longer manuscript departs from the stated norm; whether exceptions are granted is not stated.
- **AI use**: undisclosed generative AI use, unrevised AI-generated text, or AI-manipulated research outputs breach the publisher policy (AI Policy, https://taylorandfrancis.com/our-policies/ai-policy/).
- **Language**: manuscripts in English only (2022-02-18 instructions copy; this sentence was not located in the live page text read on 2026-11-24).
- No other hard blocker is supported by a fact read; ethics-approval rules are not stated in the passages of the live instructions read (Practical Concerns).

### Soft Tax

- **Time**: no verified turnaround figure exists (Review Cycle Time); plan on an unknown first-decision time.
- **Abstract format**: the live instructions ask for an unstructured 200-word abstract (Format); the 2022-02-18 copy asked for a structured one, so older advice on the abstract format no longer applies.
- **Open access cost**: green deposit of the accepted manuscript is subject to a typical 18-month embargo for social-science and humanities journals on the publisher page (Preprint Policy; not confirmed for this journal); gold open access carries an APC whose amount was not found (Open Access).
- **Anonymisation**: the live instructions say single anonymous review and warn that a preprint removes any anonymity guarantee (Peer Review, Practical Concerns; read 2026-11-24).

### Best Suited For

- Curriculum-focused work: "curriculum" appears in 160 of 256 records with abstracts (62.5%) and "teacher" in 128 (50.0%) (Orientation).
- Theoretical, conceptual and critical-essay papers: theor- 39.1%, conceptual 18.4%, philosoph- 7.0% (Methodological Preferences), and critical essays are a listed article type (Format).
- Empirical work with a stated link to curriculum debates: the aims text says it welcomes empirical, philosophical, sociological and policy investigations and takes no methodological or theoretical stance (Framing Requirements).
- Authors with an international or comparative angle: author countries span the United States, Sweden, Norway, Germany, Australia and Finland among the top seven (Epistemological & Political Leanings), and the aims text asks for relevance for readers in other contexts.

### Not Recommended For

- Experimental or RCT-style work as the main design: "randomised/experiment" appears in 2 of 256 records (0.8%) (Methodological Preferences); this shows the form is rare here, not that it is rejected.
- Work on sexual and gender minorities as a main topic: 0 of 256 records match (Sensitive Topics); this shows absence from the sample, not rejection.
- Authors needing a verified turnaround or acceptance figure before choosing: none exists in readable sources (Metrics, Review Cycle Time).

### Rejection Fallback Chain

> No source states where rejected authors usually go. The rows below are topical neighbours that exist in this corpus, listed only because they share the subject area (curriculum and education research); they are not a claim about acceptance odds.

| Rank | Journal | Why this fallback works |
|------|---------|------------------------|
| 1 | [Curriculum Inquiry](curriculum-inquiry.md) | Same subject area (curriculum studies); an entry exists in this corpus. No fit evidence collected here |
| 2 | [Oxford Review of Education](oxford-review-of-education.md) | Broader education research; an entry exists in this corpus. No fit evidence collected here |
| 3 | | |

---

## Changelog

| Date | Change | By |
|------|--------|----|
| 2026-11-23 | AI deep research pass; no first-hand human reports | AI-assisted (maintainer-directed) |
| 2026-11-23 | Correction after independent check: open-access label count on the 2025-05-12 journal home copy is five of the six latest articles, not four | AI-assisted (maintainer-directed) |
| 2026-11-23 | Promoted to Tier 1 under the written rule: tier1_gate passes; independent spot-check 7 of 7 sampled pairs supported; banner removed; no first-hand human reports | AI-assisted (maintainer-authorised, not human-verified) |
| 2026-11-24 | Live T&F pages read in a real browser: instructions (10000-word typical ceiling, unstructured 200-word abstract (the 2022 copy said structured), up to 5 keywords, single anonymous review (the 2022 copy said double blind), generative-AI declaration, no submission or page charges) and about page (acceptance 10%, first decision 8 days, 93 days to first post-review decision, CiteScore 4.8 as labelled), which confirm the figures a search summary had shown; board now read from the page (25 = 1 + 2 + 1 + 18 + 1 + 2); 'unreadable' and 'not verified' statements replaced; Clarivate figures on the page not recorded | AI-assisted (maintainer-directed) |
| 2026-11-25 | Added the OpenAlex Top Topics table (dimension was missing) | @Zaious |
