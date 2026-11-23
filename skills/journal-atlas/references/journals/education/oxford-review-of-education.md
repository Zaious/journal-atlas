<!-- schema: v1.3 -->
<!-- AI-researched entry — Journal Atlas v2 coverage pipeline. See docs/ATLAS_V2_DESIGN.md for methodology. -->
<!-- Scaffold values from the OpenAlex Sources API (scripts/import_openalex.py dry-run, 2026-11-23), then filled by an AI deep research pass (maintainer-directed) on 2026-11-23. -->

# Oxford Review of Education

> **Last verified**: 2026-11-24
> **Maintainer**: @Zaious
> **Venue type**: Journal
> **Evidence basis**: Sourced under the written rule (SEED_DATA_QUALITY.md): deeper per-journal research by an AI model, directed by the maintainer, 2026-11-23; overall signal_quality **3/5**. Claims cite source URLs or counts; blanks are recorded with reasons. Independent spot-check on 2026-11-23: 6 supported and 1 partial of 7 sampled pairs; mislabelled data year corrected. No first-hand human reports; not human-verified.

---

## Identity

| Field | Value |
|-------|-------|
| **Abbreviation** | ORE (the journal's own Twitter handle is @OxfordRevEd, https://www.education.ox.ac.uk/our-research/oxford-review-of-education/; retrieved 2026-11-23). No ISO abbreviation source read |
| **Venue type** | Journal |
| **Publisher** | Taylor & Francis. Source: https://api.crossref.org/journals/0305-4985 (publisher string "Informa UK (Taylor & Francis)"; title "Oxford Review of Education"; print ISSN 0305-4985 and electronic ISSN 1465-3915 both returned), retrieved 2026-11-23 |
| **ISSN (Print)** | 0305-4985 |
| **ISSN (Online)** | 1465-3915 |
| **Founded** | 1974; the journal's aims text refers to "its foundation in 1974" (Wayback copy 2022-06-21, https://web.archive.org/web/20220621124018id_/https://www.tandfonline.com/action/journalInformation?show=aimsScope&journalCode=core20), and the host department's page says it was founded in 1974 in the Department of Education with the first issue in 1975 (https://www.education.ox.ac.uk/our-research/oxford-review-of-education/; retrieved 2026-11-23) |
| **URL** | https://www.tandfonline.com/toc/core20/current |
| **Author Guidelines** | https://www.tandfonline.com/action/authorSubmission?journalCode=core20&page=instructions, read in full in a real browser on 2026-11-24 (it returned HTTP 403 to curl on 2026-11-23; the page prints no date). Aims, peer-review line, metrics block and board: https://www.tandfonline.com/journals/core20/about-this-journal (read the same day, undated). The Wayback copy of 2022-08-09 (https://web.archive.org/web/20220809103843id_/https://www.tandfonline.com/action/authorSubmission?journalCode=core20&show=instructions&) is older; the 6,000 to 8,000-word range, 100-200-word abstract and double blind review are unchanged on the live page. Notes: chrome2/oxrev-pages.txt in the researcher's scratch folder |
| **Society / Association** | None found. The journal is edited from the University of Oxford Department of Education (https://www.education.ox.ac.uk/our-research/oxford-review-of-education/; retrieved 2026-11-23) |
| **Editorial Board Location** | OpenAlex source country code: GB (https://openalex.org/S55586218). The department page lists the current academic editors as Jo-Anne Baird, Velda Elliott and Steve Strand and an editorial office at the department (https://www.education.ox.ac.uk/our-research/oxford-review-of-education/; retrieved 2026-11-23). The live board on the journal's about page (https://www.tandfonline.com/journals/core20/about-this-journal, read in a real browser 2026-11-24, no date printed) lists 30 people: 3 general editors, 1 chair, 1 managing editor, 9 editorial board members, 6 emeritus board members and 10 international advisory board members (3 + 1 + 1 + 9 + 6 + 10 = 30); 20 are at the University of Oxford or Oxford Brookes University (the page prints no country for them) and the rest are listed in Australia 4, Germany 1, Greece 1, Chile 1, Hong Kong 1 and Switzerland 1, with one entry (a company) giving no country. Older, kept as older: the board page copy dated 2022-08-02 (https://web.archive.org/web/20220802233828id_/https://www.tandfonline.com/action/journalInformation?show=editorialBoard&journalCode=core20) listed 23 people (2 general editors, a chair, eight editorial board members, five emeritus board members and seven international advisory board members) |
| **OpenAlex ID** | https://openalex.org/S55586218 |

---

## Metrics

> Source: OpenAlex (CC0), retrieved 2026-11-23 (scaffold values from the Sources API). JCR impact factor and quartile are paywalled and deliberately not stated. The 2-year mean citedness below is an OpenAlex proxy, not a JCR figure. The local spine (an OpenAlex snapshot dated 2026-07-13, `scripts/query_spine.py`) gives works_count 2100 and h-index 111 for the same ISSN; the live scaffold values below are newer.

| Metric | Value | Date |
|--------|-------|------|
| **Impact Factor** | Not stated (JCR is paywalled) | |
| **5-Year IF** | Not stated (JCR is paywalled) | |
| **h-index** | 137 (OpenAlex) | 2026-11-23 |
| **CiteScore** | 5.9, labelled "(2025) CiteScore (Scopus)" on the publisher's about-this-journal page (https://www.tandfonline.com/journals/core20/about-this-journal, read in a real browser 2026-11-24); Scopus itself was not opened. The same page prints Clarivate impact-factor and quartile figures, which are deliberately not recorded here | 2025 (label on page) |
| **Acceptance Rate** | 18% acceptance rate on the live publisher metrics block (https://www.tandfonline.com/journals/core20/about-this-journal, read in a real browser 2026-11-24); the block prints no period next to its speed and acceptance figures. This confirms the value a search-engine summary had shown on 2026-11-23. Older, kept as older: 12%, from the publisher's journal-metrics page, Wayback copy 2022-06-21 (https://web.archive.org/web/20220621124023id_/https://www.tandfonline.com/action/journalInformation?show=journalMetrics&journalCode=core20), which said its figures were for the last full calendar year before the capture without naming the year | 2026-11-24 (no period on live block); 2022-06-21 copy |
| **Desk Rejection Rate** | Blank. No source found: SciRev lists 1 review with an outcome of rejection after a full review round and gives no desk-rejection rate (https://scirev.org/journal/oxford-review-of-education/), LetPub lists 0 reviews (https://www.letpub.com/journal-selector/journal/12180) | 2026-11-23 |
| **Quartile (by field)** | Not stated (SJR not read). The local spine records JUFO level 2 for this ISSN (Finnish publication forum, spine snapshot 2026-07-13) | |
| **2-yr Mean Citedness (OpenAlex IF proxy)** | 4.36 (OpenAlex proxy, not JCR) | 2026-11-23 |
| **i10-index** | 1241 (OpenAlex) | 2026-11-23 |
| **Total Works** | 2088 (OpenAlex, all years and work types) | 2026-11-23 |

### Review Cycle Time

| Stage | Typical Time | Notes |
|-------|-------------|-------|
| **Time to first decision** | Publisher-reported, live block (https://www.tandfonline.com/journals/core20/about-this-journal, read 2026-11-24, no period printed): 41 days average from submission to first decision and 90 days average from submission to first post-review decision. Older, kept as older: 14 days and 154 days in the Wayback copy 2022-06-21 of the metrics page. SciRev, n=1 review: first review round 19.5 weeks, outcome rejection (https://scirev.org/journal/oxford-review-of-education/; retrieved 2026-11-23) | Publisher averages, period not stated |
| **Time to first review** | Blank. No separate figure found | |
| **Time to acceptance (total)** | Blank. The SciRev page (retrieved 2026-11-23) shows "Tot. handling time acc. manuscripts 4.5 months", but it has n=1 review, whose outcome is Rejected (first review round 19.5 weeks), so no accepted manuscript was reported; the 4.5 months equals the first-round duration shown on the same page and is not recorded as an acceptance time (https://scirev.org/journal/oxford-review-of-education/); LetPub has 0 reviews (https://www.letpub.com/journal-selector/journal/12180) | |
| **Time to publication (after acceptance)** | 38 days average from acceptance to online publication, publisher-reported on the live metrics block (https://www.tandfonline.com/journals/core20/about-this-journal, read 2026-11-24, no period printed). Older, kept as older: 42 days (Wayback copy 2022-06-21) | Period not stated |

### Publication Frequency

| Aspect | Detail |
|--------|--------|
| **Schedule** | Six issues per year: the journal-information page (Wayback copy 2021-04-26, https://web.archive.org/web/20210426171711id_/https://www.tandfonline.com/action/journalInformation?journalCode=core20) and the host department's page (https://www.education.ox.ac.uk/our-research/oxford-review-of-education/, retrieved 2026-11-23) both say six issues a year |
| **Articles per year (approx.)** | Crossref journal-article records by published year (https://api.crossref.org/journals/0305-4985/works?filter=from-pub-date:2021-01,until-pub-date:2026-11, 314 records, all of type journal-article): 2021 = 64, 2022 = 44, 2023 = 58, 2024 = 49, 2025 = 61, 2026 = 38 (partial year, latest record dated 2026-11-16). OpenAlex, 2021-11-23 to 2026-11-23 (all work types, 261 records): article 250, editorial 6, review 5; by publication year 2022 = 44, 2023 = 58, 2024 = 49, 2025 = 59, 2026 = 38, 2021 = 13 (partial window). Retrieved 2026-11-23 |
| **Special issues?** | Yes, normally two each year; guest editors are often invited (aims text, Wayback copy 2022-06-21, https://web.archive.org/web/20220621124018id_/https://www.tandfonline.com/action/journalInformation?show=aimsScope&journalCode=core20). The department page lists recent special and thematic issues (2024 socio-economic inequality and education; 2023 pedagogy and Indigenous knowing and learning; 2023 early years intervention research; 2022 higher education internationalisation) and invites special-issue proposals via the editorial office (https://www.education.ox.ac.uk/our-research/oxford-review-of-education/; retrieved 2026-11-23) |

---

## Policies

### Peer Review

| Aspect | Detail |
|--------|--------|
| **Type** | Anonymised. The live instructions say that once the editor has assessed suitability the paper is "double blind peer reviewed by independent, anonymous expert referees", and warn that a preprint removes any anonymity guarantee (https://www.tandfonline.com/action/authorSubmission?journalCode=core20&page=instructions, read 2026-11-24). The live about page says: "All research articles in this journal have undergone rigorous peer review, based on initial editor screening and anonymised refereeing by at least two anonymous referees" (https://www.tandfonline.com/journals/core20/about-this-journal). The same instructions also ask for full name and affiliation on the cover page (2022-08-09 copy; not re-checked on the live page). Retrieved 2026-11-24 |
| **Transferable / Cascade?** | Blank. No source read |
| **Reviewer reports published?** | Blank. No statement found in the pages read |
| **Typical R+R rounds** | Blank. No source found; SciRev's single review reports 1.0 review round and 1.0 review report (https://scirev.org/journal/oxford-review-of-education/), which is n=1 |
| **Reviewer recommendations** | Blank. No source found |

### AI Policy

| Aspect | Detail |
|--------|--------|
| **Has journal-specific AI policy?** | Partly. The live instructions page (read in a real browser 2026-11-24) asks every submission to include a "Declaration of generative AI use": a statement disclosing whether and how generative AI was used in the research and manuscript preparation (https://www.tandfonline.com/action/authorSubmission?journalCode=core20&page=instructions). The 2022-08-09 copy predates this. The publisher-wide Taylor & Francis policy applies; that policy itself warns that some journals may restrict AI use beyond language improvement and tells authors to check the journal's instructions |
| **Explicit permission gate?** | No gate found. Use is allowed with a mandatory disclosure statement |
| **Leniency (1-5)** | 3 (allowed with mandatory disclosure; same rubric as the Mind entry) |
| **Summary** | Publisher policy: AI tools cannot be listed as authors. Authors must acknowledge any generative AI use in a specific statement giving the tool name and version, how it was used and why. Text or code generation without rigorous revision, synthetic data standing in for missing data, and AI creation or manipulation of research outputs or images are not permitted. Retrieved 2026-11-23 |
| **Source URL** | https://taylorandfrancis.com/our-policies/ai-policy/ |

### Preprint Policy

> Publisher-level policy, not journal-specific. Source: https://authorservices.taylorandfrancis.com/research-impact/sharing-versions-of-journal-articles/ (retrieved 2026-11-23). The journal-specific embargo period was not looked up.

| Stage | Allowed? | Notes |
|-------|----------|-------|
| Pre-submission | Yes | The page says the original manuscript may be shared as much as the author likes, including on non-commercial preprint servers such as SocArXiv, and that doing so is not duplicate publication. The journal's own instructions (Wayback copy 2022-08-09, https://web.archive.org/web/20220809103843id_/https://www.tandfonline.com/action/authorSubmission?journalCode=core20&show=instructions&) add that anonymity cannot be guaranteed once a version is on a preprint server |
| Under review | Blank | The page speaks of the pre-submission version; it does not separately address the under-review stage |
| Post-acceptance (AAM) | Yes, with embargo | The accepted manuscript may go on the author's own website after publication; repositories and scholarly networks after an embargo that the page gives as typically 18 months for the social sciences and humanities portfolio, counted from publication of the Version of Record. Embargo: 18 months is the publisher's typical figure, not confirmed for this journal |
| Version of Record | Open access articles may be shared freely | Per the same page; non-open-access articles via publisher eprint links |

### Open Access

| Aspect | Detail |
|--------|--------|
| **Model** | Hybrid (Taylor & Francis Open Select). Evidence: the journal home copy dated 2025-12-13 carries the "Open Select: choose to publish open access" label (https://web.archive.org/web/20251213031310id_/https://www.tandfonline.com/journals/core20); OpenAlex open-access status of the 261 records dated 2021-11-23 to 2026-11-23: hybrid 155, closed 86, green 14, bronze 6 (retrieved 2026-11-23); Open Select described at https://authorservices.taylorandfrancis.com/publishing-open-access/open-select/ |
| **APC (if OA chosen)** | Blank. The live instructions refer to the publisher's APC finder without printing an amount (read 2026-11-24); the finder was not read, and the Open Select page says the choice is made on acceptance. Non-OA route: the live instructions state there are no submission fees, publication fees or page charges, and colour figures are free online (a print charge applies; the 2022-08-09 copy gave GBP 300 per figure) |
| **Gold OA offered?** | Yes: the aims copy dated 2022-06-21 says authors can choose gold open access, and the instructions describe the Open Select route |
| **Read & Publish agreements** | Blank. No list read |

---

## Format

> Source for the general rules: the journal's live instructions for authors (https://www.tandfonline.com/action/authorSubmission?journalCode=core20&page=instructions), read in a real browser on 2026-11-24; the page prints no date. Retrieved 2026-11-24. The Wayback copy of 2022-08-09 is older; rows that rest only on it say so.

| Aspect | Detail |
|--------|--------|
| **Article types accepted** | The archived instructions list one type: original articles; manuscripts in English only. OpenAlex type counts for 2021-11-23 to 2026-11-23: article 250, editorial 6, review 5 (retrieved 2026-11-23) |
| **Word limit** | "A typical paper for this journal should be between 6,000 and 8,000 words, inclusive of tables, references, figure captions, endnotes" (live instructions, read 2026-11-24; same range in the 2022-08-09 copy). Crossref page ranges give a median article length of 18 pages (quartiles 17 and 20) over 314 of 314 records, 2021-2026 |
| **Word limit negotiability** | Blank. The live instructions word the range as typical ("a typical paper"); no statement on exceptions found |
| **Abstract limit** | Unstructured abstract of 100-200 words that should summarise the paper including methods; between 4 and 6 keywords (live instructions, read 2026-11-24) |
| **Reference limit** | No separate cap found; references count inside the 6,000 to 8,000 words (live instructions, read 2026-11-24) |
| **Supplementary material** | Supplemental material (video, dataset, files) is published via Figshare (archived instructions, 2022-08-09) |
| **Figure/Table limits** | No count limit found. Resolution and editable-table requirements are in the archived instructions; extra colour is charged only for print |
| **Style / submission format** | British (-ise) spelling used consistently; single quotation marks; long quotations indented without quotation marks; authors are told to follow the quick style guidelines rather than published articles (live instructions, read 2026-11-24). Word format with a template, the publisher's reference guide (style not named in the text read), the Taylor & Francis submission portal, Crossref similarity screening and full name and affiliation on the cover page are from the 2022-08-09 copy and were not re-checked |

---

## Subject Density

> Based on OpenAlex topic analysis (scaffold, retrieved 2026-11-23).

### Top Topics (last 5 years)

> These are OpenAlex topic-assignment counts, not article counts: a work can carry several topics, so the first row (352) exceeds the 261 records the journal has in the 2021-11-23 to 2026-11-23 window.

| Topic | Article Count |
|-------|--------------|
| Global Educational Policies and Reforms | 352 |
| School Choice and Performance | 336 |
| Historical Education Studies Worldwide | 276 |
| Education, Philosophy, and Society | 230 |
| Educational Theory and Curriculum Studies | 200 |
| Higher Education Governance and Development | 186 |
| Teacher Education and Leadership Studies | 168 |
| Education Pedagogy and Practices | 148 |
| Educational Assessment and Improvement | 131 |
| Intergenerational and Educational Inequality Studies | 103 |

### Orientation

> Counts come from 314 Crossref journal-article records published 2021-01 to 2026-11 (https://api.crossref.org/journals/0305-4985/works?filter=from-pub-date:2021-01,until-pub-date:2026-11). Crossref holds no abstracts for this journal, so abstracts for 271 of the 314 records (86.3%) were taken from the Semantic Scholar API (https://api.semanticscholar.org/graph/v1/paper/batch, by DOI). Hits are counted over title plus abstract, as a share of the 271 records with abstracts; they are lower bounds. Regexes are listed in AI-Research Notes. Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Empirical vs. Theoretical** | Mixed. "interview" 46 (17.0%), "survey/questionnaire" 37 (13.7%), "regression/longitudinal/cohort" 26 (9.6%) alongside "theor-" 44 (16.2%) and "conceptual" 23 (8.5%) of 271 records with abstracts |
| **Quantitative vs. Qualitative** | Both present: "qualitative" 24 (8.9%), "quantitative" 8 (3.0%), "mixed methods" 4 (1.5%) of 271 records with abstracts |
| **Cross-disciplinary openness** | The journal's aims text says it cultivates educational scholarship across a wide range of academic disciplines (journal home copy dated 2025-12-13, https://web.archive.org/web/20251213031310id_/https://www.tandfonline.com/journals/core20). The host department's page says editors welcome analytic or reflective pieces that draw on the full range of disciplines relevant to education (https://www.education.ox.ac.uk/our-research/oxford-review-of-education/). Policy 68 (25.1%), assessment/exam 49 (18.1%), higher education 31 (11.4%) and teacher 94 (34.7%) of 271 |

---

## Soft Metadata

### Epistemological & Political Leanings

> Evidence layers: OpenAlex counts over 261 records (2021-11-23 to 2026-11-23, retrieved before the shared rate limit was hit, so only totals, types, years, open-access status and author countries were obtained); Crossref records (314) with Semantic Scholar abstracts (271); the Wayback-archived board page (copy 2022-08-02); the department page. Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Cross-cultural friendliness** | Author countries on the 261 OpenAlex records dated 2021-11-23 to 2026-11-23 (records with at least one author in the country): United Kingdom 136, Australia 19, United States 19, China 17, Hong Kong 9, Spain 8, Ireland 8, Israel 7, Netherlands 6, Chile 5, South Korea 5, Belgium 4 (OpenAlex works API grouped by authorship country, retrieved 2026-11-23) |
| **Editorial-board geography** | Live board (about page, https://www.tandfonline.com/journals/core20/about-this-journal, read 2026-11-24, no date printed): 30 people. General editors 3, chair 1, managing editor 1 and emeritus board members 6 are all at the University of Oxford; of the 9 editorial board members, 8 are at Oxford and 1 at Oxford Brookes University (the page prints no country, so UK is inferred from the institutions: 3 + 1 + 1 + 9 + 6 = 20). The 10 international advisory board members are in Australia 4, Germany 1, Greece 1, Chile 1, Hong Kong 1 and Switzerland 1, with one entry at a company (Duolingo and EdAstra Tech) that gives no country (4 + 1 + 1 + 1 + 1 + 1 + 1 = 10; 20 + 10 = 30). Older, kept as older: the 2022-08-02 copy listed 23 entries: 11 editors, chair and board members all at UK institutions (University of Oxford 9, Oxford Brookes University 1, UCL 1), 7 international advisers (Germany 1, Tanzania 1, United States 1, South Africa 1, Singapore 1, Hong Kong 1, Australia 1) and 5 emeritus members |
| **Non-Western epistemology openness** | Keyword counts, title plus abstract of 271 records: "decolonial/Indigenous/Maori/Aboriginal" 13 (4.8%). The department page lists a 2023 special issue titled "Pedagogy and Indigenous knowing and learning" (https://www.education.ox.ac.uk/our-research/oxford-review-of-education/) |
| **Diversity topic receptiveness** | Counts of 271 records with abstracts: gender/feminism/women/girls 23 (8.5%), race/racism/ethnic 17 (6.3%), social class/inequality/disadvantage 44 (16.2%), disability/special needs/inclusion 23 (8.5%), queer/LGBT/transgender/sexuality 0. The journal states no editorial position on these topics in the pages read |
| **Dominant theoretical tradition** | No single tradition. Named theorists (Bourdieu, Foucault, Marx, Freire, Dewey, Deleuze, Arendt, Habermas) appear in 8 of 271 records (3.0%); "theor-" appears in 44 (16.2%). The most cited 2021-2026 items in Crossref (citation counts at retrieval) include "What is global higher education?" (123; https://doi.org/10.1080/03054985.2022.2061438), "Rethinking teacher education: The trouble with accountability" (115; https://doi.org/10.1080/03054985.2020.1842181), "Factors influencing academic performance and dropout rates in higher education" (94; https://doi.org/10.1080/03054985.2024.2316616) and "The core content framework and the 'new science' of educational research" (73; https://doi.org/10.1080/03054985.2023.2182768). The journal states no political position on any page that could be read |

### Framing Requirements

- **Mandatory framing?** One scope condition is stated by the journal itself: it aims to publish important new work on educational topics of general interest, in a form accessible to a broad educational readership, with wide educational relevance. Sources: the journal home copy dated 2025-12-13 (https://web.archive.org/web/20251213031310id_/https://www.tandfonline.com/journals/core20) and the host department's page (https://www.education.ox.ac.uk/our-research/oxford-review-of-education/). Retrieved 2026-11-23.
- **What kind of engagement?** Both significant new research and conceptual or theoretical contributions are welcome, per the aims text (journal home copy dated 2025-12-13). The department page adds analytic or reflective pieces that draw on the range of disciplines relevant to education.
- **Article type and length**: original articles in the archived instructions, a typical paper of 6,000 to 8,000 words including references, an unstructured 100-200 word abstract and 4-6 keywords (instructions copy dated 2022-08-09, https://web.archive.org/web/20220809103843id_/https://www.tandfonline.com/action/authorSubmission?journalCode=core20&show=instructions&).
- **Special-issue framing seen**: special issues are normally two a year and proposals are invited through the editorial office; recent themes include "Competence, competition, content and control: Sociological perspectives on educational assessment" (vol. 51 no. 2, April 2025) and "The political economies of school exclusion across the UK" (vol. 50 no. 6, December 2024) (https://www.education.ox.ac.uk/our-research/oxford-review-of-education/; retrieved 2026-11-23).
- **Consequences of ignoring it**: Blank. No source states what happens to out-of-scope submissions, and no desk-rejection data exists for this journal (SciRev has one review that is a rejection after a review round: https://scirev.org/journal/oxford-review-of-education/).

### Methodological Preferences

> Counts are Crossref records (314) published 2021-01 to 2026-11 whose title or abstract matches the regex (abstracts for 271 records, 86.3%, from Semantic Scholar by DOI); shares use 271 as the denominator. Scoring convention of this research pass (its own, not an external standard): share 0 = 0; under 1% = 1; 1-5% = 2; over 5% = 3; 4-5 only with a cited editorial statement, and none was found. Scores measure how often a method appears, not how a reviewer would judge it. Regexes are in AI-Research Notes.

| Method | Receptiveness (0-5) | Evidence |
|--------|---------------------|----------|
| Quantitative experimental | 2 | "randomised/randomization/RCT/experiment" 8 of 271 (3.0%); "quantitative" 8 (3.0%) |
| Survey and regression / longitudinal | 3 | "survey/questionnaire" 37 (13.7%); "regression/longitudinal/panel data/cohort" 26 (9.6%) |
| Qualitative interviews | 3 | "interview" 46 (17.0%); "qualitative" 24 (8.9%) of 271 |
| Case study | 3 | "case study" 19 (7.0%) of 271 |
| Ethnography | 2 | "ethnograph" 3 (1.1%) of 271; "autoethnography" was not counted separately |
| Theoretical / Conceptual | 3 | "theor-" 44 (16.2%); "conceptual" 23 (8.5%); "philosoph-" 9 (3.3%) |
| Mixed methods | 2 | "mixed method" 4 (1.5%) of 271 |
| Systematic / literature review | 2 | "systematic review, meta-analysis, scoping review, literature review" 11 (4.1%) of 271; the tenth most cited item of the window is a systematic review of student voice (https://doi.org/10.1080/03054985.2023.2257132, 50 citations in Crossref) |

### Voice & Style

| Aspect | Detail |
|--------|--------|
| **First-person voice acceptance (0-5)** | Not scored. Sample: of the 100 most recently dated articles that have an abstract (Crossref plus Semantic Scholar), 43 abstracts contain I, my, we or our and 8 contain I or my; across all 271 abstracts, 112 contain one of those words (plural "we" may be generic rather than authorial). Records containing I or my include https://doi.org/10.1080/03054985.2025.2603288 and https://doi.org/10.1080/03054985.2025.2500943 and https://doi.org/10.1080/03054985.2024.2439289. The archived instructions give no rule on first person. Retrieved 2026-11-23 |
| **Expected density** | Crossref page ranges give a median article length of 18 pages across 314 of 314 records (quartiles 17 and 20; 2021-2026; https://api.crossref.org/journals/0305-4985/works?filter=from-pub-date:2021-01,until-pub-date:2026-11). Length range: 6,000 to 8,000 words including references (live instructions, read 2026-11-24) |
| **Abstract and keywords** | Unstructured abstract of 100 to 200 words, 4 to 6 keywords, optional graphical abstract (live instructions, read 2026-11-24, https://www.tandfonline.com/action/authorSubmission?journalCode=core20&page=instructions) |
| **Writing style notes** | Archived instructions (2022-08-09): British (-ise) spelling used consistently; single quotation marks; long quotations indented without marks; English only; authors told to follow the quick style guidelines rather than copy published articles. The manuscript structure is given as title page, abstract, keywords, then introduction/methods/results/discussion "or an alternative structure that is more appropriate to a high-quality non-empirical article" |
| **Authorship pattern** | Of 314 Crossref records with author lists (2021-01 to 2026-11): 105 single-author, 91 two authors, 51 three, 67 four or more (retrieved 2026-11-23); 31 of the 100 most recent records with an abstract are single-author |

### Reviewer Pool Characteristics

Reviewer behaviour itself is not observable from public pages; what follows is what public pages do show.

| Aspect | Detail | Evidence |
|--------|--------|----------|
| **Dominant tradition** | The live board lists 3 general editors, 1 chair, 1 managing editor, 9 editorial board members, 6 emeritus board members and 10 international advisory board members (30). The page gives professional titles but no disciplines list; titles seen include education, assessment, sociology and social policy, geography, psychology and education, philosophy of education and research policy. The department page says the board is drawn from the Department of Education and other relevant Oxford departments and fields | https://www.tandfonline.com/journals/core20/about-this-journal (live, counted 2026-11-24); https://www.education.ox.ac.uk/our-research/oxford-review-of-education/ ; retrieved 2026-11-23 |
| **Review model** | Anonymised refereeing by at least two anonymous referees after editor screening; the instructions call it double blind | Live instructions and about page (URLs in Peer Review), read 2026-11-24 |
| **Reviewer competence variance** | Blank. One first-hand report exists (SciRev, n=1: first round 19.5 weeks, only one of two reviewers commented, overall rating 3.0 of 5, rejected); it is one data point and says nothing about variance | https://scirev.org/journal/oxford-review-of-education/ ; LetPub 0 reviews: https://www.letpub.com/journal-selector/journal/12180 |
| **Quantitative mindset bias on qualitative work?** | Blank. No source. Both interview-based and survey or regression work appear (interview 17.0%, survey 13.7%, regression/longitudinal 9.6% of 271 records), which cannot tell how reviewers treat either | Counts in Methodological Preferences |
| **Discourse community signals (author side)** | Author community as a proxy, not a reviewer list: United Kingdom 136, Australia 19, United States 19, China 17, Hong Kong 9 records with at least one author there (OpenAlex, 261 records, 2021-11-23 to 2026-11-23) | OpenAlex works API grouped by authorship country, retrieved 2026-11-23 |

### Sensitive Topics

> Counts are Crossref records (314) with abstracts for 271, title plus abstract, as shares of 271 (Semantic Scholar abstracts by DOI; lower bounds). "Receptiveness" cells give frequency only; no editorial statement was found, so no row is rated High.

| Topic Category | Receptiveness | Evidence |
|----------------|---------------|----------|
| Decolonial / Indigenous | Present, small | 13 of 271 (4.8%); a 2023 special issue on Indigenous knowing and learning (https://www.education.ox.ac.uk/our-research/oxford-review-of-education/) |
| Gender and feminism | Present | 23 of 271 (8.5%) |
| Race and ethnicity | Present | 17 of 271 (6.3%) |
| Sexual and gender minorities | Rare | 0 of 271 for queer, LGBT, transgender or sexuality |
| Religion | Present, small | 10 of 271 (3.7%); a 2025 article on Arab teacher leaders and faith visibility appears among recent records (https://doi.org/10.1080/03054985.2026.2745837) |
| Political conflict, migration | Present, small | "war, conflict, refugee, migra-" 12 of 271 (4.4%) |
| AI and technology | Present, small | "artificial intelligence, AI, ChatGPT, generative, machine learning, algorithm" 9 of 271 (3.3%) |
| Climate | Present | "climate, sustainab-, Anthropocene, ecolog-" 28 of 271 (10.3%) |
| Inequality and disability | Frequently published | social class/inequality 44 (16.2%); disability/special needs/inclusion 23 (8.5%); a 2024 special issue on socio-economic inequality and education (department page above) |

### Practical Concerns

| Concern | Detail |
|---------|--------|
| **IRB requirement strictness** | Blank for any journal-specific ethics-approval rule: the archived instructions (2022-08-09) point to the publisher's publishing-ethics guidance and contain no journal-specific ethics text in the part read (https://web.archive.org/web/20220809103843id_/https://www.tandfonline.com/action/authorSubmission?journalCode=core20&show=instructions&) |
| **Single-author acceptance** | Single-author papers are common: 105 of 314 Crossref records (33.4%) published 2021-01 to 2026-11 (https://api.crossref.org/journals/0305-4985/works?filter=from-pub-date:2021-01,until-pub-date:2026-11; retrieved 2026-11-23) |
| **Independent scholar friendliness** | The archived instructions define the affiliation as where the research was conducted and state no independent-scholar rule (https://web.archive.org/web/20220809103843id_/https://www.tandfonline.com/action/authorSubmission?journalCode=core20&show=instructions&). No reviewer or author-affiliation breakdown for independent scholars was obtained |
| **Data transparency requirement** | The journal applies the Taylor & Francis Basic Data Sharing Policy: data sharing is encouraged, not required; authors are asked at submission whether a data set exists and for its identifier; data sets are not peer reviewed (archived instructions, 2022-08-09) |
| **OPSEC compatibility** | Review is described as double blind, but authors also give name and affiliation on the cover page and a preprint removes any anonymity guarantee (archived instructions, https://web.archive.org/web/20220809103843id_/https://www.tandfonline.com/action/authorSubmission?journalCode=core20&show=instructions&). Pre-submission preprints are allowed by the publisher (https://authorservices.taylorandfrancis.com/research-impact/sharing-versions-of-journal-articles/) |
| **AI use** | Disclosure statement required; AI cannot be an author (https://taylorandfrancis.com/our-policies/ai-policy/), retrieved 2026-11-23 |
| **Open access and cost** | Hybrid; no submission or page charges on the non-OA route (archived instructions, 2022-08-09); APC for open access not read (https://authorservices.taylorandfrancis.com/publishing-open-access/open-select/). 155 of 261 recent records are hybrid OA in OpenAlex |
| **Originality screening** | All submissions are screened for unoriginal material with Crossref similarity checking (archived instructions, 2022-08-09) |

### AI-Research Notes (sources, blanks, and cross-language checks)

**signal_quality (0-5)**: overall 3. Per layer: OpenAlex counts 2 (only totals, types, years, OA and countries were obtained before a rate limit; keyword counts were not); Crossref plus Semantic Scholar keyword counts 3 (271 of 314 abstracts, lower bounds); publisher-wide policies 4; journal-specific policies and guidelines 4 (live instructions and about pages read in a real browser 2026-11-24, undated; the 2022 Wayback copies are kept as labelled older figures); experiential layer 1 (one SciRev review).

**Method note**: the OpenAlex works API was queried with 5 grouped or total counts and then returned HTTP 429, after which no further OpenAlex request was made (per the brief). A first keyword query ("qualitative" = 0) was discarded because the filter value was double-percent-encoded in the script, so no OpenAlex keyword count is used. Keyword counts use Crossref records (journal-article type, published 2021-01-01 to 2026-11-23, `select` fields DOI, title, abstract, author, page) with abstracts from the Semantic Scholar batch API by DOI (271 of 314 returned; the other 43 are counted by title only, which lowers every share). Matching is case-insensitive over title plus abstract with these regexes (Python `re`, `\b` word boundary at the start): qualitative `\bqualitative`; quantitative `\bquantitative`; interview `\binterview`; survey `\bsurvey|\bquestionnaire`; randomised/experiment `\brandomi[sz]ed|\brandomi[sz]ation|\bRCT\b|\bexperiment`; mixed methods `\bmixed[- ]method`; reviews `\bsystematic review|\bmeta-analys|\bscoping review|\bliterature review`; ethnography `\bethnograph`; case study `\bcase stud`; theory `\btheor(y|ies|etical|ising|izing|ise|ize)\b`; conceptual `\bconceptual`; philosophy `\bphilosoph`; regression/longitudinal `\bregression|\blongitudinal|\bpanel data|\bcohort`; decolonial/Indigenous `\bdecolon|\bindigenous|\bfirst nations|\bm[aā]ori|\baboriginal`; gender `\bgender|\bfeminis|\bwomen\b|\bgirls\b`; race `\brac(e|ism|ist|ial|ialised|ialized)\b|\bwhiteness|\bblack\b|\bethnic`; class/inequality `\bsocial class|\bworking[- ]class|\binequalit|\bsocio-?economic|\bdisadvantage`; AI `\bartificial intelligence|\bAI\b|\bChatGPT|\bgenerative|\bmachine learning|\balgorithm`; queer `\bqueer|\blgbt|\btransgender|\bsexualit`; religion `\breligio|\bislam|\bmuslim|\bchristian|\bspiritual`; named theorists `\bbourdieu|\bfoucault|\bmarx|\bfreire|\bdewey|\bdeleuze|\barendt|\bhabermas`; climate `\bclimate|\bsustainab|\banthropocene|\becolog`; conflict `\bwar\b|\bconflict|\brefugee|\bmigra`; disability `\bdisabilit|\bspecial (educational )?needs|\bautis|\bdyslexi|\bSEND?\b|\binclusi`. Some patterns are broad ("black", "conflict", "experiment") and may over-count; others may miss synonyms. First-person regex: `\b(I|my|we|our)\b` on abstracts. Correction 2026-11-23 (recomputed over the same 314 records and 271 abstracts, case-insensitive, title plus abstract): policy `\bpolicy\b|\bpolicies\b` 68 (25.1%, reproduces the earlier figure); teacher `\bteachers?\b` 94 (34.7%, reproduces); assessment/exam `\bassessments?\b|\bexams?\b|\bexaminations?\b` 49 (18.1%); higher education `\bhigher education\b` 31 (11.4%). The earlier figures "assessment/exam 60" and "higher education 49" came from regexes that were not recorded and could not be reproduced, so they were replaced.

**Sources cited across this entry:**
- https://web.archive.org/web/20220809103843id_/https://www.tandfonline.com/action/authorSubmission?journalCode=core20&show=instructions& (instructions, Wayback copy 2022-08-09)
- https://web.archive.org/web/20220621124023id_/https://www.tandfonline.com/action/journalInformation?show=journalMetrics&journalCode=core20 (metrics, Wayback copy 2022-06-21)
- https://web.archive.org/web/20220621124018id_/https://www.tandfonline.com/action/journalInformation?show=aimsScope&journalCode=core20 (aims, Wayback copy 2022-06-21)
- https://web.archive.org/web/20251213031310id_/https://www.tandfonline.com/journals/core20 (journal home, Wayback copy 2025-12-13)
- https://web.archive.org/web/20220802233828id_/https://www.tandfonline.com/action/journalInformation?show=editorialBoard&journalCode=core20 (editorial board, Wayback copy 2022-08-02)
- https://web.archive.org/web/20210426171711id_/https://www.tandfonline.com/action/journalInformation?journalCode=core20 (journal information, Wayback copy 2021-04-26)
- https://www.education.ox.ac.uk/our-research/oxford-review-of-education/ (host department page, read live)
- https://api.crossref.org/journals/0305-4985 and https://api.crossref.org/journals/0305-4985/works (314 journal-article records 2021-01 to 2026-11)
- https://api.semanticscholar.org/graph/v1/paper/batch (abstracts by DOI)
- https://api.openalex.org/works (grouped counts for source S55586218, 2021-11-23 to 2026-11-23)
- https://taylorandfrancis.com/our-policies/ai-policy/
- https://authorservices.taylorandfrancis.com/research-impact/sharing-versions-of-journal-articles/
- https://authorservices.taylorandfrancis.com/publishing-open-access/open-select/
- https://scirev.org/journal/oxford-review-of-education/
- https://www.letpub.com/journal-selector/journal/12180

**Unreadable pages (never filled from memory):**
- None among the journal's own main pages as of 2026-11-24: the instructions page (https://www.tandfonline.com/action/authorSubmission?journalCode=core20&page=instructions) and the about page with metrics and board (https://www.tandfonline.com/journals/core20/about-this-journal), both HTTP 403 to curl on 2026-11-23, were read in a real browser; nothing was clicked. The live metrics block confirms the 18%, 41-day and 90-day figures that a search summary had shown on 2026-11-23. The about page prints Clarivate impact-factor and quartile figures, which are deliberately not recorded. Notes: chrome2/oxrev-pages.txt in the researcher's scratch folder.

**Fields deliberately left blank, and why:**
- Desk rejection rate, time to acceptance, reviewer culture, reviewer competence variance, quantitative bias: no first-hand source beyond one SciRev review (rejected after 19.5 weeks); LetPub shows 0 reviews.
- APC, ethics-approval rule: the cost finder was not read, and the live instructions state no ethics rule in the passages read.
- Impact factor, quartile: paywalled, not stated by policy.

**Cross-language and forum checks performed (all returned zero journal-specific first-hand reports):**
- SciRev (English): journal page exists with 1 review (https://scirev.org/journal/oxford-review-of-education/).
- LetPub: journal page exists, 0 reviews (https://www.letpub.com/journal-selector/journal/12180).
- 小木虫 (muchong) and 知乎 (zhihu): web search "Oxford Review of Education 投稿 审稿周期 经验 小木虫 OR 知乎" returned no muchong or zhihu thread; one Chinese journal-listing site (iikx.com) returned with empty review-speed fields.
- fabiaoji: not reached by the web search; not checked directly.
- Reddit: web search for the journal name with "submission experience desk reject reddit" returned no Reddit thread; a Duotrope result was a paywalled submission log and was not read.

---

## Strategic Notes

> Each statement below follows from a fact recorded above and names it. Where the evidence does not support a statement, the field says so.

### Hard Blockers

- **Scope**: the journal's own aims text asks for work of general interest to a broad educational readership and wide educational relevance (Framing Requirements; journal home copy 2025-12-13). A paper of narrow specialist interest only is outside that stated aim.
- **Length**: a typical paper is 6,000 to 8,000 words including references and notes (Format; live instructions read 2026-11-24). A much longer manuscript departs from the stated norm; whether exceptions are granted is not stated.
- **AI use**: undisclosed generative AI use, unrevised AI-generated text, or AI-manipulated research outputs breach the publisher policy (AI Policy, https://taylorandfrancis.com/our-policies/ai-policy/).
- **Language**: manuscripts in English only (2022-08-09 instructions copy; this sentence was not located in the live page text read on 2026-11-24).
- No other hard blocker is supported by a fact read; ethics-approval rules are not stated in the passages of the live instructions read (Practical Concerns).

### Soft Tax

- **Time**: SciRev's single review reports 19.5 weeks for the first round (Review Cycle Time, n=1); the publisher's live block gives 90 days to a first post-review decision (no period printed; the archived 2022-06-21 copy gave 154 days) (Review Cycle Time), so the sources differ. Total time to acceptance is unknown.
- **Selectivity**: the publisher's live metrics block reports an 18% acceptance rate (no period printed; read 2026-11-24); the archived 2022-06-21 copy reported 12% (Metrics).
- **Open access cost**: green deposit of the accepted manuscript is subject to a typical 18-month embargo for social-science and humanities journals on the publisher page (Preprint Policy; not confirmed for this journal); gold open access carries an APC whose amount was not found (Open Access).
- **Anonymisation**: review is described as double blind but the same instructions ask for author name and affiliation on the cover page, and a preprint removes any anonymity guarantee (Peer Review, Practical Concerns).

### Best Suited For

- Education research of broad interest across policy, teachers and higher education: policy 25.1%, teacher 34.7%, assessment/exam 18.1% and higher education 11.4% of 271 records with abstracts (Orientation).
- Both empirical and conceptual work: interview 17.0%, survey 13.7%, theor- 16.2% and conceptual 8.5% (Methodological Preferences), consistent with the aims text welcoming new research and conceptual or theoretical pieces (Framing Requirements).
- Papers on inequality, gender, race, or disability in education: 16.2%, 8.5%, 6.3% and 8.5% of 271 records (Sensitive Topics).
- Single-authored work: 105 of 314 records are single-author (Voice & Style).

### Not Recommended For

- Work on sexual and gender minorities as a main topic: 0 of 271 records with abstracts match (Sensitive Topics); this shows absence from the sample, not rejection.
- Papers that need a dated turnaround or acceptance figure: the live publisher figures print no period (Metrics, Review Cycle Time).
- Very short or very long submissions: the stated typical range is 6,000 to 8,000 words (Format).

### Rejection Fallback Chain

> No source states where rejected authors usually go. The rows below are topical neighbours that exist in this corpus, listed only because they share the subject area (general education research); they are not a claim about acceptance odds.

| Rank | Journal | Why this fallback works |
|------|---------|------------------------|
| 1 | [British Journal of Educational Studies](british-journal-of-educational-studies.md) | Same subject area (general UK-based education research); an entry exists in this corpus. No fit evidence collected here |
| 2 | [Educational Researcher](educational-researcher.md) | Same subject area; an entry exists in this corpus. No fit evidence collected here |
| 3 | | |

---

## Changelog

| Date | Change | By |
|------|--------|----|
| 2026-11-23 | AI deep research pass; no first-hand human reports | AI-assisted (maintainer-directed) |
| 2026-11-23 | Correction after independent check: speed/acceptance block no longer labelled "calendar year 2020" (page says only "last full calendar year", data year not stated; only citation metrics carry "(2020)"); SciRev "Tot. handling time acc. manuscripts 4.5 months" described exactly (n=1, outcome rejection); assessment/exam and higher-education counts recomputed with stated word-boundary regexes (49 and 31 of 271) | AI-assisted (maintainer-directed) |
| 2026-11-23 | Promoted to Tier 1 under the written rule: tier1_gate passes; independent spot-check 6 supported and 1 partial of 7 sampled pairs; mislabelled data year corrected; banner removed; no first-hand human reports | AI-assisted (maintainer-authorised, not human-verified) |
| 2026-11-24 | Live T&F pages read in a real browser: instructions (6,000 to 8,000-word typical range, 100-200-word abstract, 4 to 6 keywords, double blind, generative-AI declaration, no submission or page charges) and about page (acceptance 18%, first decision 41 days, 90 days to first post-review decision, CiteScore 5.9 as labelled); the figures that had only a search summary are now read on the page and the older 12%, 14-day and 154-day figures kept as older; board recounted to 30 (3 + 1 + 1 + 9 + 6 + 10, was 23); 'unreadable' statements replaced; Clarivate figures on the page not recorded | AI-assisted (maintainer-directed) |
