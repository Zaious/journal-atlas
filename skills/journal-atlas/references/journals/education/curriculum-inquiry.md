<!-- schema: v1.3 -->
<!-- AI-researched entry — Journal Atlas v2 coverage pipeline. See docs/ATLAS_V2_DESIGN.md for methodology. -->
<!-- Scaffold values from the OpenAlex Sources API (scripts/import_openalex.py dry-run, 2026-11-23), then filled by an AI deep research pass (maintainer-directed) on 2026-11-23. -->

# Curriculum Inquiry

> **Last verified**: 2026-11-23
> **Maintainer**: @Zaious
> **Venue type**: Journal
> **Evidence basis**: Sourced under the written rule (SEED_DATA_QUALITY.md): deeper per-journal research by an AI model, directed by the maintainer, 2026-11-23; overall signal_quality **3/5**. Claims cite source URLs or counts; blanks are recorded with reasons. Independent spot-check on 2026-11-23: 8 of 8 sampled pairs supported; one inflated count corrected. No first-hand human reports; not human-verified.

---

## Identity

| Field | Value |
|-------|-------|
| **Abbreviation** | CI (used by the journal's own aims text, https://curriculum-inquiry.squarespace.com/about; retrieved 2026-11-23). No ISO abbreviation source read |
| **Venue type** | Journal |
| **Publisher** | Taylor & Francis (Routledge), on behalf of the Ontario Institute for Studies in Education (OISE). Source: https://curriculum-inquiry.squarespace.com/about and https://api.crossref.org/journals/0362-6784 (publisher string "Informa UK (Taylor & Francis)"; title "Curriculum Inquiry"; print ISSN 0362-6784 and electronic ISSN 1467-873X both returned), retrieved 2026-11-23 |
| **ISSN (Print)** | 0362-6784 |
| **ISSN (Online)** | 1467-873X |
| **Founded** | The journal's own past-editors list gives a predecessor, Curriculum Theory Network, edited from 1968 (John Herbert, 1968-1971), and Curriculum Inquiry editors from 1977 (https://curriculum-inquiry.squarespace.com/editorial-boards; retrieved 2026-11-23). Earliest Crossref-registered year: 1976 (https://api.crossref.org/journals/0362-6784) |
| **URL** | https://www.tandfonline.com/toc/rcui20/current (journal's own site: https://curriculum-inquiry.squarespace.com/about) |
| **Author Guidelines** | The journal's own page, read live: https://curriculum-inquiry.squarespace.com/information-for-authors (submissions go through the Taylor & Francis submission portal). The publisher's instructions page (live copy returns HTTP 403) was read as a Wayback copy dated 2022-04-18: https://web.archive.org/web/20220418231644id_/https://www.tandfonline.com/action/authorSubmission?journalCode=rcui20&show=instructions& (current wording may differ) |
| **Society / Association** | Ontario Institute for Studies in Education, University of Toronto (publication is "on behalf of" OISE; contact address on the journal's site is at OISE) (https://curriculum-inquiry.squarespace.com/about; retrieved 2026-11-23) |
| **Editorial Board Location** | OpenAlex source country code: US (https://openalex.org/S64935255), while the journal's own site places the editorial office at OISE, Toronto, Canada. The journal's own board page lists an editor-in-chief, a faculty editor, a senior editor, two associate editors, an assistant editor and a journal coordinator, plus OISE and international boards (https://curriculum-inquiry.squarespace.com/editorial-boards; retrieved 2026-11-23); no personal addresses are repeated here |
| **OpenAlex ID** | https://openalex.org/S64935255 |

---

## Metrics

> Source: OpenAlex (CC0), retrieved 2026-11-23 (scaffold values from the Sources API). JCR impact factor and quartile are paywalled and deliberately not stated, and the impact-factor figures shown on the publisher's archived metrics page are not repeated here. The 2-year mean citedness below is an OpenAlex proxy, not a JCR figure. The local spine (an OpenAlex snapshot dated 2026-07-13, `scripts/query_spine.py`) gives works_count 2476 and h-index 92 for the same ISSN; the live scaffold values below are newer.

| Metric | Value | Date |
|--------|-------|------|
| **Impact Factor** | Not stated (JCR is paywalled) | |
| **5-Year IF** | Not stated (JCR is paywalled) | |
| **h-index** | 105 (OpenAlex) | 2026-11-23 |
| **CiteScore** | Not stated (Scopus not accessed) | |
| **Acceptance Rate** | 10%, as reported by the publisher's journal-metrics page for calendar year 2021 (Wayback copy 2022-09-04, https://web.archive.org/web/20220904173323id_/https://www.tandfonline.com/action/journalInformation?show=journalMetrics&journalCode=rcui20); the current figure was not obtained | 2022-09-04 copy (2021 data) |
| **Desk Rejection Rate** | Blank. No rate found. The journal's own page says every submission is first reviewed internally by the editorial team, which may reject it, ask for revision, or send it out (https://curriculum-inquiry.squarespace.com/editorial-review-process). SciRev lists no reviews (https://scirev.org/journal/curriculum-inquiry/) | 2026-11-23 |
| **Quartile (by field)** | Not stated (SJR not read). The local spine records JUFO level 1 for this ISSN (Finnish publication forum, spine snapshot 2026-07-13) | |
| **2-yr Mean Citedness (OpenAlex IF proxy)** | 1.09 (OpenAlex proxy, not JCR) | 2026-11-23 |
| **i10-index** | 748 (OpenAlex) | 2026-11-23 |
| **Total Works** | 2010 (OpenAlex, all years and work types) | 2026-11-23 |

### Review Cycle Time

| Stage | Typical Time | Notes |
|-------|-------------|-------|
| **Time to first decision** | Publisher-reported for calendar year 2021: 61 days average from submission to first decision, and 93 days average from submission to first post-review decision (Wayback copy 2022-09-04, https://web.archive.org/web/20220904173323id_/https://www.tandfonline.com/action/journalInformation?show=journalMetrics&journalCode=rcui20). The page defines both as median-style averages over the last full calendar year | Publisher figure is 2021 data; it may have changed |
| **Time to first review** | Blank. No separate figure found | |
| **Time to acceptance (total)** | Blank. SciRev has no reviews (https://scirev.org/journal/curriculum-inquiry/); a LetPub page for the title was not located by search | |
| **Time to publication (after acceptance)** | 56 days average from acceptance to online publication of the Version of Record, publisher-reported for calendar year 2021 (same metrics page, Wayback copy 2022-09-04) | 2021 data |

### Publication Frequency

| Aspect | Detail |
|--------|--------|
| **Schedule** | Five issues per year: the journal-information page, Wayback copy dated 2022-09-04 (https://web.archive.org/web/20220904173321id_/https://www.tandfonline.com/action/journalInformation?journalCode=rcui20), says 5 issues per year; the issue numbers in Crossref match (volume 54 has issues 1 to 5 in 2024; volume 55 has issues 1, 2, a combined 3-4 and 5 in 2025) (https://api.crossref.org/journals/0362-6784/works?filter=from-pub-date:2021-01,until-pub-date:2026-12) |
| **Articles per year (approx.)** | Crossref journal-article records by published year (https://api.crossref.org/journals/0362-6784/works?filter=from-pub-date:2021-01,until-pub-date:2026-12, 168 records, all of type journal-article): 2021 = 29, 2022 = 43, 2023 = 21, 2024 = 24, 2025 = 31, 2026 = 20 (partial year, latest record dated 2026-10-19). The records include five "Reviewers for Volume" lists and editorial essays (every issue carries an editorial essay per the aims text). Retrieved 2026-11-23 |
| **Special issues?** | Yes. The journal's own site lists open calls ("Racial Capitalism and Education", "Epistemologies of Ignorance", "New Scholars in Review") and a special-issue proposals page asking for an 800 to 1000 word prospectus (https://curriculum-inquiry.squarespace.com/special-issue-proposals; retrieved 2026-11-23) |

---

## Policies

### Peer Review

| Aspect | Detail |
|--------|--------|
| **Type** | Internal editorial screening first, then anonymous external peer review. The journal's own page says every submission is reviewed internally by the editorial team, which may send it for external review, ask for revisions first, or reject it, and that every published manuscript is anonymously peer reviewed by external experts; editors rely heavily on reviewers but are not bound by them (https://curriculum-inquiry.squarespace.com/editorial-review-process; retrieved 2026-11-23). The publisher's instructions (Wayback copy 2022-04-18, https://web.archive.org/web/20220418231644id_/https://www.tandfonline.com/action/authorSubmission?journalCode=rcui20&show=instructions&) call the review "double blind" by independent anonymous referees |
| **Transferable / Cascade?** | Blank. No source read |
| **Reviewer reports published?** | Blank. No statement found in the pages read |
| **Typical R+R rounds** | Blank. No source found. The journal's page lists "request that the author make revisions before being considered for peer review" as one possible editor outcome |
| **Reviewer recommendations** | Blank. No source found |

### AI Policy

| Aspect | Detail |
|--------|--------|
| **Has journal-specific AI policy?** | No journal-specific policy found in the journal's own pages read; the publisher's instructions page was unreadable (403) and the 2022-04-18 copy predates generative-AI wording. The publisher-wide Taylor & Francis policy applies; that policy itself warns that some journals may restrict AI use beyond language improvement and tells authors to check the journal's instructions |
| **Explicit permission gate?** | No gate found. Use is allowed with a mandatory disclosure statement |
| **Leniency (1-5)** | 3 (allowed with mandatory disclosure; same rubric as the Mind entry) |
| **Summary** | Publisher policy: AI tools cannot be listed as authors. Authors must acknowledge any generative AI use in a specific statement giving the tool name and version, how it was used and why. Text or code generation without rigorous revision, synthetic data standing in for missing data, and AI creation or manipulation of research outputs or images are not permitted. Retrieved 2026-11-23 |
| **Source URL** | https://taylorandfrancis.com/our-policies/ai-policy/ |

### Preprint Policy

> The journal's own page is stricter than the publisher's. Journal: https://curriculum-inquiry.squarespace.com/editorial-review-process (retrieved 2026-11-23). Publisher: https://authorservices.taylorandfrancis.com/research-impact/sharing-versions-of-journal-articles/ (retrieved 2026-11-23). The journal-specific embargo period was not looked up.

| Stage | Allowed? | Notes |
|-------|----------|-------|
| Pre-submission | Restricted by the journal | The journal's page says its policy is to publish work available for the first time through the journal, asks authors to confirm the manuscript has not been published before "including electronically", and says sharing the unpublished manuscript with a limited audience such as colleagues or students would not prejudice acceptance, but not posting it to a widely accessible website. The publisher's general page, by contrast, says preprints on non-commercial servers are not duplicate publication for its journals. The two statements differ; the journal's is the more restrictive and is the one that applies to this journal's editors |
| Under review | Blank | Not separately addressed in the pages read |
| Post-acceptance (AAM) | Yes, with embargo | The accepted manuscript may go on the author's own website after publication; repositories and scholarly networks after an embargo that the publisher page gives as typically 18 months for the social sciences and humanities portfolio. Embargo: 18 months is the publisher's typical figure, not confirmed for this journal |
| Version of Record | Open access articles may be shared freely | Per the publisher page; non-open-access articles via publisher eprint links |

### Open Access

| Aspect | Detail |
|--------|--------|
| **Model** | Hybrid (Taylor & Francis Open Select) with a free-access editorials page. Evidence: the instructions copy dated 2022-04-18 describes the Open Select route, and the aims copy of 2022-09-04 says authors can choose gold open access (https://web.archive.org/web/20220904173323id_/https://www.tandfonline.com/action/journalInformation?show=aimsScope&journalCode=rcui20); the journal's own site lists every issue's editorial essay as free access (https://curriculum-inquiry.squarespace.com/openaccess); Open Select described at https://authorservices.taylorandfrancis.com/publishing-open-access/open-select/ |
| **APC (if OA chosen)** | Blank. The instructions say to use the publisher's APC finder, which was not read. Non-OA route: the instructions (2022-04-18 copy) state no submission fees, publication fees or page charges, with print colour figures charged at GBP 300 per figure |
| **Gold OA offered?** | Yes, per the instructions and aims copies above |
| **Read & Publish agreements** | Blank. No list read |

---

## Format

> Source for the general rules: the journal's own guidelines page, read live on 2026-11-23 (https://curriculum-inquiry.squarespace.com/information-for-authors), with the publisher's instructions (Wayback copy dated 2022-04-18, https://web.archive.org/web/20220418231644id_/https://www.tandfonline.com/action/authorSubmission?journalCode=rcui20&show=instructions&) for items the journal's page does not cover. Where the two differ the journal's own page is used.

| Aspect | Detail |
|--------|--------|
| **Article types accepted** | The archived instructions leave the article-type list empty. The journal's pages describe research articles and an editorial essay in every issue (https://curriculum-inquiry.squarespace.com/about); the publisher's home copy of 2025-06-27 labels items Article, Case Report and Editorial (https://web.archive.org/web/20250627034041id_/https://www.tandfonline.com/journals/rcui20). The journal says it typically does not publish curriculum, policy or programme efficacy evaluations, scoping reviews, literature reviews or bibliometric analyses (https://curriculum-inquiry.squarespace.com/editorial-review-process) |
| **Word limit** | Manuscripts should not exceed 9,000 words when first submitted, and revised manuscripts may be up to 10,000; the count includes abstract, tables, captions, reference list and endnotes (journal's own page). The archived publisher instructions say a typical paper is no more than 10,000 words including tables, references, captions, footnotes and endnotes. Crossref page ranges give a median article length of 19.5 pages (quartiles 12 and 23) over 168 of 168 records, 2021-2026 (includes editorials) |
| **Word limit negotiability** | Partly stated: the limit rises from 9,000 at submission to 10,000 at revision (journal's own page). No statement on other exceptions found |
| **Abstract limit** | 200 to 250 words (journal's own page); the archived publisher instructions say an unstructured abstract of 250 words and 5 keywords |
| **Reference limit** | No separate cap found; references count inside the 9,000 and 10,000 words (journal's own page) |
| **Supplementary material** | Supplemental material (video, dataset, files) is published via Figshare (archived instructions, 2022-04-18) |
| **Figure/Table limits** | No count limit found. Figures: at least 1200 dpi for line art, 600 dpi for greyscale and 300 dpi for colour, as separate files in TIFF, JPEG, EPS or PNG (journal's own page); extra print colour is charged (archived instructions) |
| **Style / submission format** | APA 7th edition citations and references, with commentary endnotes allowed but citations not as endnotes; double-spaced, 12-point black font, 2.54 cm margins; Microsoft Word, not PDF; a cover letter is requested from all authors and is especially recommended for work that differs in topic, method or approach from what the journal usually publishes and for submissions from outside the United States and Canada; submission through the Taylor & Francis submission portal (journal's own page, read live 2026-11-23) |

---

## Subject Density

> Top Topics come from the OpenAlex works API, retrieved 2026-11-25 (request URL under the table); the Orientation counts below come from Crossref records, with abstracts from Semantic Scholar where stated there, retrieved 2026-11-23.

### Top Topics (last 5 years)

> Source: OpenAlex works API, source S64935255, works of type article dated 2021-11-23 to 2026-11-23 (110 works), grouped by topic: https://api.openalex.org/works?filter=primary_location.source.id:S64935255,type:article,from_publication_date:2021-11-23,to_publication_date:2026-11-23&group_by=topics.id . Retrieved 2026-11-25. 82 topics were returned; the top 10 are shown. The 10th and 11th topics are tied at 8; the order between tied topics is the API's. These are OpenAlex topic-assignment counts, not article counts: a work can carry several topics, so the counts do not sum to 110.

| Topic | Article Count |
|-------|--------------|
| Critical Race Theory in Education | 46 |
| Critical and Liberation Pedagogy | 34 |
| Educational Theory and Curriculum Studies | 22 |
| Educator Training and Historical Pedagogy | 16 |
| Indigenous and Place-Based Education | 14 |
| Gender, Sexuality, and Education | 13 |
| Teacher Education and Leadership Studies | 12 |
| Peace and Human Rights Education | 11 |
| Decolonial Thought and Epistemologies | 10 |
| Indigenous Health, Education, and Rights | 8 |

### Orientation

> Counts come from 168 Crossref journal-article records published 2021-01 to 2026-11 (https://api.crossref.org/journals/0362-6784/works?filter=from-pub-date:2021-01,until-pub-date:2026-12). Crossref holds no abstracts for this journal, so abstracts for 149 of the 168 records (88.7%) were taken from the Semantic Scholar API (https://api.semanticscholar.org/graph/v1/paper/batch, by DOI). Hits are counted over title plus abstract as a share of the 149; they are lower bounds. Regexes are listed in AI-Research Notes. Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Empirical vs. Theoretical** | Theoretical and critical wording predominates: "theor-" 51 (34.2%), "conceptual" 13 (8.7%), "discourse" 15 (10.1%) against "interview" 23 (15.4%), "survey/questionnaire" 1 (0.7%) and "regression/longitudinal/cohort" 0 of 149 records with abstracts. The journal asks that manuscripts articulate theories and concepts and integrate them into the analysis (https://curriculum-inquiry.squarespace.com/editorial-review-process) |
| **Quantitative vs. Qualitative** | Qualitative: "qualitative" 8 (5.4%), "ethnograph" 11 (7.4%), "case study" 9 (6.0%) against "quantitative" 0 and "mixed methods" 0 of 149 |
| **Cross-disciplinary openness** | The aims text describes scholars "from a variety of academic fields and disciplines" working on curriculum and pedagogy, with activist engagements and critical theoretical engagements named in the journal's own current aims (https://curriculum-inquiry.squarespace.com/about). Curriculum 82 (55.0%), teacher 38 (25.5%), higher education 20 (13.4%) of 149 |

---

## Soft Metadata

### Epistemological & Political Leanings

> Evidence layers: the journal's own website (aims, review criteria, rejection reasons, board, editorial list; read live); Crossref records (168; abstracts for 149 via Semantic Scholar) and Crossref author affiliations. OpenAlex keyword counts were not obtained (rate limit). Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Cross-cultural friendliness** | Author countries taken from Crossref affiliation strings (273 of 298 authors, 92%, name a recognised country; counts are articles with at least one author in the country, of 168 articles): United States 88, Canada 60, Australia 8, United Kingdom 7, Palestine 5, Colombia 3, Chile 2, South Korea 2 (https://api.crossref.org/journals/0362-6784/works; method in AI-Research Notes). The journal itself says its editorial team and reviewers tend to be more familiar with US and Canadian contexts than with other parts of the world, and asks authors from elsewhere to explain their context in a cover letter (https://curriculum-inquiry.squarespace.com/information-for-authors) |
| **Editorial-board geography** | The journal's own board page lists an international editorial board of 85 members: United States 53, Canada 21, United Kingdom 3, Australia 2, and one each in Brazil, Colombia, Ireland, Puerto Rico, Singapore and Taiwan (counted from the page, 85 entries sum to 85), plus an OISE advisory board of 29 and an editorial team of seven (editor-in-chief, faculty editor, senior editor, two associate editors, assistant editor, journal coordinator) (https://curriculum-inquiry.squarespace.com/editorial-boards; retrieved 2026-11-23) |
| **Non-Western epistemology openness** | Keyword counts, title plus abstract of 149 records: "decolonial/Indigenous/Maori/Aboriginal" 40 (26.8%); "Indigenous" alone 33 (22.1%). The journal's own editorial list includes essays titled "Black and Indigenous futures in education: Thinking with interdisciplinary rebellious methodologies" (volume 55 issue 2, 2025) and "Curricular battlegrounds: Education, scholasticide, and steadfastness in Palestine and beyond" (volume 55 issues 3-4, 2025) (https://curriculum-inquiry.squarespace.com/openaccess) |
| **Diversity topic receptiveness** | Counts of 149 records with abstracts: race/racism/ethnic 62 (41.6%), gender/feminism/women/girls 33 (22.1%), queer/LGBT/transgender/sexuality 16 (10.7%), disability/special needs/inclusion 15 (10.1%), social class/inequality/disadvantage 5 (3.4%). The journal's own editorials include "The messiness of putting queerness to work" (volume 53 issue 3, 2023) and "Abolition as method: Asking new questions" (volume 55 issue 1, 2025) (https://curriculum-inquiry.squarespace.com/openaccess) |
| **Dominant theoretical tradition** | Critical curriculum studies. The journal's own page says it is especially interested in work that pushes the journal toward more critical engagements in critical curriculum studies (https://curriculum-inquiry.squarespace.com/information-for-authors), and its aims describe critical theoretical engagements (https://curriculum-inquiry.squarespace.com/about). Counts of 149 records: "critical race, settler, anti-Black, BlackCrit, abolition" 44 (29.5%), "Black" 39 (26.2%), "posthuman/new materialism/more-than-human" 5 (3.4%), named theorists (Bourdieu, Foucault, Marx, Freire, Dewey, Deleuze, Arendt, Habermas) 5 (3.4%). The most cited 2021-2026 items in Crossref (citation counts at retrieval) include "Media education and the limits of 'literacy'" (60; https://doi.org/10.1080/03626784.2020.1865104), "Education and ecological precarity" (52; https://doi.org/10.1080/03626784.2022.2052634), "Toward a pedagogy of solidarity" (34; https://doi.org/10.1080/03626784.2022.2082733) and "Land acknowledgements in the academy: Refusing the settler myth" (25; https://doi.org/10.1080/03626784.2021.1889924) |

### Framing Requirements

- **Mandatory framing?** Yes, stated by the journal itself. The three most common reasons for rejection are that the manuscript does not critically engage with contemporary debates in curriculum studies, that it is a curriculum, policy or programme efficacy evaluation, scoping review, literature review or bibliometric analysis (which the journal says it typically does not publish), or that it does not meet the review criteria (https://curriculum-inquiry.squarespace.com/editorial-review-process; retrieved 2026-11-23).
- **What kind of engagement?** The review criteria list a clear central question in keeping with the aims, a justification of the contribution to curriculum studies scholarship, theories and concepts that define the problem and are integrated into the analysis, a justified choice of method, clarity about how author positionality shapes the question, and a clear summative argument (same page). The journal asks for cover letters for work unlike what it usually publishes (https://curriculum-inquiry.squarespace.com/information-for-authors).
- **Article type and length**: research articles up to 9,000 words at submission and 10,000 at revision, an abstract of 200 to 250 words, APA 7 references (https://curriculum-inquiry.squarespace.com/information-for-authors).
- **Special-issue framing seen**: current open calls "Racial Capitalism and Education", "Epistemologies of Ignorance" and "New Scholars in Review"; proposals are asked for "big questions" that challenge common understandings and present divergent or competing perspectives, in a prospectus of roughly 800 to 1000 words (https://curriculum-inquiry.squarespace.com/special-issue-proposals; retrieved 2026-11-23).
- **Consequences of ignoring it**: the journal says these are the most common reasons for rejection (editorial-review-process page above). No desk-rejection rate exists (SciRev has no reviews: https://scirev.org/journal/curriculum-inquiry/).

### Methodological Preferences

> Counts are Crossref records (168) published 2021-01 to 2026-11 whose title or abstract matches the regex (abstracts for 149 records, 88.7%, from Semantic Scholar by DOI); shares use 149 as the denominator. Scoring convention of this research pass (its own, not an external standard): share 0 = 0; under 1% = 1; 1-5% = 2; over 5% = 3; 4-5 only with a cited editorial statement. Two rows use the journal's own statements (editorial-review-process and information-for-authors pages, read live 2026-11-23) to go above or below the count score, and say so. Scores measure how often a method appears, not how a reviewer would judge it. Regexes are in AI-Research Notes.

| Method | Receptiveness (0-5) | Evidence |
|--------|---------------------|----------|
| Quantitative experimental | 1 | "randomised/randomization/RCT/experiment" 3 of 149 (2.0%, which alone scores 2; the matches include non-experimental uses such as an arts "experiment"); "quantitative" 0. The journal says it typically does not publish curriculum, policy or programme efficacy evaluations (https://curriculum-inquiry.squarespace.com/editorial-review-process), so the score is set at 1 |
| Survey and regression / longitudinal | 1 | "survey/questionnaire" 1 (0.7%); "regression/longitudinal/panel data/cohort" 0 of 149 |
| Qualitative interviews | 3 | "interview" 23 (15.4%); "qualitative" 8 (5.4%) of 149 |
| Case study | 3 | "case study" 9 (6.0%) of 149 |
| Ethnography | 3 | "ethnograph" 11 (7.4%) of 149; "autoethnography" 3 (2.0%) |
| Narrative and arts-based | 3 | "narrative, storytelling, counter-story" 25 (16.8%); "arts-based, artistic, poetry, poetic, performance" 11 (7.4%) of 149 |
| Theoretical / Conceptual | 4 | "theor-" 51 (34.2%); "conceptual" 13 (8.7%); "discourse" 15 (10.1%) of 149. The journal's review criteria require theories and concepts that define the problem and are integrated into the analysis, and it is especially interested in more critical engagements (https://curriculum-inquiry.squarespace.com/editorial-review-process; https://curriculum-inquiry.squarespace.com/information-for-authors), which supports a score above the count score of 3 |
| Mixed methods | 0 | "mixed method" 0 of 149 |
| Systematic / literature review | 0 | "systematic review, meta-analysis, scoping review, literature review" 0 of 149; the journal says it typically does not publish scoping reviews, literature reviews or bibliometric analyses (editorial-review-process page above) |

### Voice & Style

| Aspect | Detail |
|--------|--------|
| **First-person voice acceptance (0-5)** | Not scored. Sample: of the 100 most recently dated articles with an abstract (Crossref plus Semantic Scholar, dated up to 2026-10-19), 88 abstracts contain I, my, we or our and 40 contain I or my; across all 149 abstracts, 126 contain one of those words (plural "we" may be generic rather than authorial). Records containing I or my include https://doi.org/10.1080/03626784.2026.2657614 and https://doi.org/10.1080/03626784.2026.2664453. The journal's guidelines give no rule on first person but ask authors to explain how positionality shapes the question (review criteria page). Retrieved 2026-11-23 |
| **Expected density** | Crossref page ranges give a median article length of 19.5 pages across 168 of 168 records (quartiles 12 and 23; 2021-2026, includes editorials). Length ceiling: 9,000 words at submission and 10,000 at revision including references (the journal's guidelines page) |
| **Abstract and keywords** | The journal asks for a 200 to 250 word abstract that gives "a vivid sense of the issues, findings, and conclusions" (short quote, journal's guidelines page); the archived publisher instructions say an unstructured abstract of 250 words and 5 keywords (https://web.archive.org/web/20220418231644id_/https://www.tandfonline.com/action/authorSubmission?journalCode=rcui20&show=instructions&) |
| **Writing style notes** | Journal's guidelines: APA 7, double-spaced, 12-point black font, 1-inch margins, Word format; endnotes only for commentary. Archived publisher instructions (2022-04-18): any spelling style if consistent; double quotation marks; concise section headings; English only |
| **Authorship pattern** | Of 162 Crossref records with author lists (2021-01 to 2026-11): 81 single-author, 48 two authors, 18 three, 15 four or more (retrieved 2026-11-23); 44 of the 100 most recent records with an abstract are single-author |

### Reviewer Pool Characteristics

Reviewer behaviour itself is not observable from public pages; what follows is what public pages do show.

| Aspect | Detail | Evidence |
|--------|--------|----------|
| **Dominant tradition** | The journal's own page says the editorial team and reviewers tend to be more familiar with US and Canadian contexts than with other parts of the world. The international editorial board lists 74 of 85 members in the United States (53) and Canada (21) | https://curriculum-inquiry.squarespace.com/information-for-authors ; https://curriculum-inquiry.squarespace.com/editorial-boards ; retrieved 2026-11-23 |
| **Review model** | Editorial-team screening first, then anonymous external peer review; the publisher's instructions call it double blind | https://curriculum-inquiry.squarespace.com/editorial-review-process ; https://web.archive.org/web/20220418231644id_/https://www.tandfonline.com/action/authorSubmission?journalCode=rcui20&show=instructions& (2022-04-18 copy) |
| **Reviewer competence variance** | Blank. No first-hand report exists: SciRev has no reviews; a LetPub page for the title was not located | https://scirev.org/journal/curriculum-inquiry/ |
| **Quantitative mindset bias on qualitative work?** | Blank for reviewers. The journal's own page states editors typically do not publish efficacy evaluations, scoping or literature reviews and bibliometric work; this concerns editorial acceptance, not reviewer behaviour, and counts show survey and regression work almost absent (survey 0.7%, regression/longitudinal 0 of 149 records) | https://curriculum-inquiry.squarespace.com/editorial-review-process |
| **Discourse community signals (editorial board)** | Board composition as above; the board page also lists a 29-member OISE advisory board and an editorial team of seven. Two of the 85 international board members are listed as independent scholars | https://curriculum-inquiry.squarespace.com/editorial-boards ; retrieved 2026-11-23 |

### Sensitive Topics

> Counts are Crossref records (168) with abstracts for 149, title plus abstract, as shares of 149 (Semantic Scholar abstracts by DOI; lower bounds). A row is rated High only where the journal's own editorial list or calls (https://curriculum-inquiry.squarespace.com/openaccess, https://curriculum-inquiry.squarespace.com/about) name the topic.

| Topic Category | Receptiveness | Evidence |
|----------------|---------------|----------|
| Decolonial / Indigenous | High | 40 of 149 (26.8%); editorial "Black and Indigenous futures in education" (volume 55 issue 2, 2025) on the journal's editorial list |
| Gender and feminism | Present, frequent | 33 of 149 (22.1%) |
| Race and ethnicity | High | 62 of 149 (41.6%); "critical race, settler, anti-Black, BlackCrit, abolition" 44 (29.5%); a current open call on racial capitalism and education (https://curriculum-inquiry.squarespace.com/about) and the editorial "Abolition as method" (volume 55 issue 1, 2025) |
| Sexual and gender minorities | High | 16 of 149 (10.7%); editorial "The messiness of putting queerness to work" (volume 53 issue 3, 2023) |
| Religion | Present, small | 10 of 149 (6.7%); the publisher's home copy of 2025-06-27 lists a 2025 case report titled "Sending balms across geographies of grief: Transoceanic letters on Muslim aliveness" (https://web.archive.org/web/20250627034041id_/https://www.tandfonline.com/journals/rcui20) |
| Political conflict, Palestine | High | "Palestin-, Gaza" 17 of 149 (11.4%); editorial "Curricular battlegrounds: Education, scholasticide, and steadfastness in Palestine and beyond" (volume 55 issues 3-4, 2025) |
| AI and technology | Present, small | "artificial intelligence, AI, ChatGPT, generative, machine learning, algorithm" 6 of 149 (4.0%) |
| Climate | Present | "climate, sustainab-, Anthropocene, ecolog-" 25 of 149 (16.8%); https://doi.org/10.1080/03626784.2022.2052634 |
| Disability | Present | disability/special needs/inclusion 15 of 149 (10.1%) |

### Practical Concerns

| Concern | Detail |
|---------|--------|
| **IRB requirement strictness** | Blank for any journal-specific ethics-approval rule: neither the journal's guidelines page nor the archived publisher instructions (2022-04-18) contains ethics-approval text in the parts read (https://curriculum-inquiry.squarespace.com/information-for-authors) |
| **Single-author acceptance** | Single-author papers are common: 81 of 162 Crossref records with author lists (50.0%) published 2021-01 to 2026-11 (https://api.crossref.org/journals/0362-6784/works?filter=from-pub-date:2021-01,until-pub-date:2026-12; retrieved 2026-11-23) |
| **Independent scholar friendliness** | The archived instructions define the affiliation as where the research was conducted and state no independent-scholar rule (https://web.archive.org/web/20220418231644id_/https://www.tandfonline.com/action/authorSubmission?journalCode=rcui20&show=instructions&). Two of the 85 international editorial board members are listed as independent scholars (https://curriculum-inquiry.squarespace.com/editorial-boards) |
| **Data transparency requirement** | Blank. No data-sharing policy appears in the journal's guidelines page or in the 2022-04-18 instructions copy (its contents list has no data-sharing section) |
| **OPSEC compatibility** | Review is anonymous, but a cover letter is requested and the journal's page discourages posting the manuscript to a widely accessible website before publication (https://curriculum-inquiry.squarespace.com/editorial-review-process). Anonymisation instructions for the manuscript itself were not found in the pages read |
| **AI use** | Disclosure statement required; AI cannot be an author (https://taylorandfrancis.com/our-policies/ai-policy/), retrieved 2026-11-23 |
| **Open access and cost** | Hybrid; no submission or page charges on the non-OA route (archived instructions, 2022-04-18); APC for open access not read (https://authorservices.taylorandfrancis.com/publishing-open-access/open-select/) |
| **Originality screening** | All submissions are screened for unoriginal material with Crossref similarity checking (archived instructions, 2022-04-18) |

### AI-Research Notes (sources, blanks, and cross-language checks)

**signal_quality (0-5)**: overall 3. Per layer: Crossref plus Semantic Scholar keyword counts 3 (149 of 168 abstracts, lower bounds); Crossref affiliation-based author countries 3; the journal's own website 4 (read live, undated); OpenAlex 1 (scaffold values only; no keyword or country counts were obtained because the shared rate limit was reached; the topic table was added on 2026-11-25 from one OpenAlex request); publisher-wide policies 4; publisher journal pages 3 (Wayback copies of 2022; live pages unreadable); experiential layer 0.

**Method note**: keyword counts use Crossref records (journal-article type, published 2021-01-01 to 2026-11-23, `select` fields DOI, title, abstract, author, page) with abstracts from the Semantic Scholar batch API by DOI (149 of 168 returned; the other 19 are counted by title only, which lowers every share). Matching is case-insensitive over title plus abstract with these regexes (Python `re`, `\b` word boundary at the start): qualitative `\bqualitative`; quantitative `\bquantitative`; interview `\binterview`; survey `\bsurvey|\bquestionnaire`; randomised/experiment `\brandomi[sz]ed|\brandomi[sz]ation|\bRCT\b|\bexperiment`; mixed methods `\bmixed[- ]method`; reviews `\bsystematic review|\bmeta-analys|\bscoping review|\bliterature review`; ethnography `\bethnograph`; autoethnography `\bauto-?ethnograph`; case study `\bcase stud`; narrative `\bnarrative|\bstorytelling|\bcounter-?stor`; arts-based `\barts?-based|\bartistic|\bpoetry|\bpoetic|\bperformance`; theory `\btheor(y|ies|etical|ising|izing|ise|ize)\b`; conceptual `\bconceptual`; philosophy `\bphilosoph`; regression/longitudinal `\bregression|\blongitudinal|\bpanel data|\bcohort`; discourse `\bdiscourse`; decolonial/Indigenous `\bdecolon|\bindigenous|\bfirst nations|\bm[aā]ori|\baboriginal`; gender `\bgender|\bfeminis|\bwomen\b|\bgirls\b`; race `\brac(e|ism|ist|ial|ialised|ialized)\b|\bwhiteness|\bblack\b|\bethnic`; critical race `\bcritical race|\bsettler|\banti-?black|\bblackcrit|\babolition`; Black `\bblack\b|\bblackness`; class/inequality `\bsocial class|\bworking[- ]class|\binequalit|\bsocio-?economic|\bdisadvantage`; AI `\bartificial intelligence|\bAI\b|\bChatGPT|\bgenerative|\bmachine learning|\balgorithm`; queer `\bqueer|\blgbt|\btransgender|\bsexualit`; religion `\breligio|\bislam|\bmuslim|\bchristian|\bspiritual`; named theorists `\bbourdieu|\bfoucault|\bmarx|\bfreire|\bdewey|\bdeleuze|\barendt|\bhabermas`; posthuman `\bposthuman|\bnew materialis|\bmore-than-human`; Palestine `\bpalestin|\bgaza`; climate `\bclimate|\bsustainab|\banthropocene|\becolog`; disability `\bdisabilit|\bspecial (educational )?needs|\bautis|\bdyslexi|\binclusi` plus `(?-i:\bSEND?\b)`, matched case-sensitively as an acronym only (the first version matched `\bSEND?\b` case-insensitively and counted the verb in "to send letters as balms", https://doi.org/10.1080/03626784.2025.2477613; recomputed 2026-11-23 over the same 168 records and 149 abstracts: 16 became 15, 10.1%; the acronym form matches 0 records here); first person `\b(I|my|we|our)\b` on abstracts. Country counts match country names and abbreviations (for example `\bUK\b`, `\bUSA\b`, `\bUS\b`) in Crossref affiliation name and place strings; affiliations without a country name are unmatched, and a string naming Northern Ireland would count for both the United Kingdom and Ireland. Some patterns are broad ("black", "performance", "experiment", "inclusi") and may over-count. Board counts were made from the journal's own page text: the international board has 85 entries (two have no personal-site link and were counted separately by hand).

**Sources cited across this entry:**
- https://curriculum-inquiry.squarespace.com/about, /editorial-boards, /editorial-review-process, /information-for-authors, /openaccess and /special-issue-proposals (the journal's own site, read live 2026-11-23)
- https://web.archive.org/web/20220418231644id_/https://www.tandfonline.com/action/authorSubmission?journalCode=rcui20&show=instructions& (publisher instructions, Wayback copy 2022-04-18)
- https://web.archive.org/web/20220904173323id_/https://www.tandfonline.com/action/journalInformation?show=journalMetrics&journalCode=rcui20 (metrics, Wayback copy 2022-09-04)
- https://web.archive.org/web/20220904173323id_/https://www.tandfonline.com/action/journalInformation?show=aimsScope&journalCode=rcui20 (aims, Wayback copy 2022-09-04)
- https://web.archive.org/web/20220904173321id_/https://www.tandfonline.com/action/journalInformation?journalCode=rcui20 (journal information, Wayback copy 2022-09-04)
- https://web.archive.org/web/20250627034041id_/https://www.tandfonline.com/journals/rcui20 (publisher journal home, Wayback copy 2025-06-27)
- https://api.crossref.org/journals/0362-6784 and https://api.crossref.org/journals/0362-6784/works (168 journal-article records 2021-01 to 2026-11)
- https://api.semanticscholar.org/graph/v1/paper/batch (abstracts by DOI)
- https://taylorandfrancis.com/our-policies/ai-policy/
- https://authorservices.taylorandfrancis.com/research-impact/sharing-versions-of-journal-articles/
- https://authorservices.taylorandfrancis.com/publishing-open-access/open-select/
- https://scirev.org/journal/curriculum-inquiry/

**Unreadable pages (never filled from memory):**
- unreadable live: the publisher's pages at tandfonline.com for this journal (403); readable as Wayback copies listed above. The aims page at https://www.tandfonline.com/journals/rcui20/about-this-journal has no Wayback copy; the aims text comes from the journal's own site and the 2022-09-04 copy.
- unreadable: a LetPub page for this title was not located by search; no figure from LetPub is used.
- secondary, unverified: a search-engine summary said the publisher's current page lists a different editor-in-chief from the 2022 copy; the journal's own site (read live) confirms the current team, so the summary is not needed.

**Fields deliberately left blank, and why:**
- Desk rejection rate, time to acceptance, reviewer culture, reviewer competence variance: no first-hand source exists; SciRev has no reviews and no LetPub page was located.
- APC, ethics-approval rule, data-sharing rule, current publisher metrics: cost-finder and live publisher pages not readable or not stated.
- Impact factor, quartile: paywalled, not stated by policy. OpenAlex topic table: added on 2026-11-25 from one works-API request (see Subject Density).

**Cross-language and forum checks performed (all returned zero journal-specific first-hand reports):**
- SciRev (English): journal page exists, no reviews (https://scirev.org/journal/curriculum-inquiry/).
- LetPub: not located by search.
- 小木虫 (muchong) and 知乎 (zhihu): web search "Curriculum Inquiry journal 投稿 审稿 经验 小木虫 OR 知乎 OR reddit review time" returned no muchong or zhihu thread; an aggregator page of metrics came back and was not used.
- fabiaoji: not reached by the web search; not checked directly.
- Reddit: the same search returned no Reddit thread for this journal. A BERA blog post quoting a 63 per cent desk-rejection rate (https://www.bera.ac.uk/?p=42570) is about a different journal and is not used.

---

## Strategic Notes

> Each statement below follows from a fact recorded above and names it. Where the evidence does not support a statement, the field says so.

### Hard Blockers

- **Scope**: the journal says the most common rejection reasons are not critically engaging with contemporary debates in curriculum studies and being a curriculum, policy or programme efficacy evaluation, scoping review, literature review or bibliometric analysis (Framing Requirements; https://curriculum-inquiry.squarespace.com/editorial-review-process). Those paper types are outside what the journal typically publishes.
- **Length**: manuscripts should not exceed 9,000 words at submission, including abstract, references and notes, and 10,000 at revision (Format; journal's guidelines page).
- **Prior online posting**: the journal says it publishes work available for the first time through the journal and that posting the manuscript to a widely accessible website does not fall under the sharing it tolerates (Preprint Policy). A public preprint therefore risks conflict with that stated policy.
- **AI use**: undisclosed generative AI use, unrevised AI-generated text, or AI-manipulated research outputs breach the publisher policy (AI Policy, https://taylorandfrancis.com/our-policies/ai-policy/).
- No other hard blocker is supported by a fact read.

### Soft Tax

- **Time**: the publisher's 2021 figures were 61 days to first decision and 93 days to first post-review decision (Review Cycle Time); the current figures are not known.
- **Selectivity**: the publisher reported a 10% acceptance rate for calendar year 2021 (Metrics, 2022-09-04 copy); the current rate is unknown.
- **Context cost for non-North-American work**: the journal says its team and reviewers are more familiar with US and Canadian contexts and asks for an explanatory cover letter (Practical Concerns, Epistemological & Political Leanings).
- **Open access cost**: green deposit of the accepted manuscript is subject to a typical 18-month embargo for social-science and humanities journals on the publisher page (Preprint Policy; not confirmed for this journal); gold open access carries an APC whose amount was not found (Open Access).

### Best Suited For

- Theoretically driven, critical curriculum scholarship: "theor-" 34.2% and "critical race, settler, anti-Black, BlackCrit, abolition" 29.5% of 149 records, and the journal's stated interest in more critical engagements (Methodological Preferences, Epistemological & Political Leanings).
- Work on race, Indigeneity, gender and sexuality, disability, Palestine or ecology in education: 41.6%, 26.8%, 22.1%, 10.7%, 10.1%, 11.4% and 16.8% of 149 records, with matching editorial essays (Sensitive Topics).
- Qualitative, narrative, arts-based and ethnographic designs: interview 15.4%, narrative 16.8%, ethnograph 7.4% (Methodological Preferences).
- Sole authors: 81 of 162 records are single-author (Voice & Style).

### Not Recommended For

- Programme or policy efficacy evaluations, scoping or literature reviews and bibliometric studies: the journal says it typically does not publish them (Format, Hard Blockers).
- Survey, regression or experimental designs as the main contribution: "survey" 1 of 149, "regression/longitudinal" 0, "mixed methods" 0 (Methodological Preferences); this shows near absence in the sample, with the efficacy-evaluation statement as the cited editorial reason.
- Authors who want to post a public preprint before publication (Preprint Policy).

### Rejection Fallback Chain

> No source states where rejected authors usually go. The rows below are topical neighbours that exist in this corpus, listed only because they share the subject area (curriculum studies or critical education research); they are not a claim about acceptance odds.

| Rank | Journal | Why this fallback works |
|------|---------|------------------------|
| 1 | [Journal of Curriculum Studies](journal-of-curriculum-studies.md) | Same subject area (curriculum studies); an entry exists in this corpus. No fit evidence collected here |
| 2 | [Educational Philosophy and Theory](educational-philosophy-and-theory.md) | Theory-oriented education research; its aims list curriculum theory in the entry. No fit evidence collected here |
| 3 | | |

---

## Changelog

| Date | Change | By |
|------|--------|----|
| 2026-11-23 | AI deep research pass; no first-hand human reports | AI-assisted (maintainer-directed) |
| 2026-11-23 | Correction after independent check: disability/special needs/inclusion count 16 (10.7%) to 15 (10.1%) of 149; the case-insensitive \bSEND?\b pattern had matched the verb "send" (DOI 10.1080/03626784.2025.2477613); regex now matches the acronym case-sensitively | AI-assisted (maintainer-directed) |
| 2026-11-23 | Promoted to Tier 1 under the written rule: tier1_gate passes; independent spot-check 8 of 8 sampled pairs supported; one inflated count corrected; banner removed; no first-hand human reports | AI-assisted (maintainer-authorised, not human-verified) |
| 2026-11-25 | Added the OpenAlex Top Topics table (dimension was missing) | @Zaious |
