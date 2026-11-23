<!-- schema: v1.3 -->
<!-- AI-researched entry — Journal Atlas v2 coverage pipeline. See docs/ATLAS_V2_DESIGN.md for methodology. -->
<!-- Scaffolded from the local OpenAlex spine snapshot (2026-07-13) and Crossref, then filled by an AI deep research pass (maintainer-directed) on 2026-11-23. -->

# Teaching in Higher Education

> **Last verified**: 2026-11-23
> **Maintainer**: @Zaious
> **Venue type**: Journal
> **Evidence basis**: Tier 1 under the written rule (SEED_DATA_QUALITY.md): deeper per-journal research by an AI model, directed by the maintainer, 2026-11-23; overall signal_quality **3/5**. Claims cite source URLs or counts; blanks are recorded with reasons. Independent spot-check on 2026-11-23: 8 of 8 sampled pairs supported; board counts recounted. No first-hand human reports; not human-verified.

---

## Identity

| Field | Value |
|-------|-------|
| **Abbreviation** | Blank. The publisher's journal code is CTHE (cthe20 in its URLs); no ISO abbreviation source read |
| **Venue type** | Journal |
| **Publisher** | Taylor & Francis. Source: https://api.crossref.org/journals/1470-1294 (publisher string "Informa UK (Taylor & Francis)"), retrieved 2026-11-23 |
| **ISSN (Print)** | 1356-2517 |
| **ISSN (Online)** | 1470-1294 |
| **Founded** | 1996, derived: the journal's own blog says it added the subtitle Critical Perspectives in 2017, "twenty-one years after its first publication" (https://teachinginhighereducation.wordpress.com/exploring-what-it-means-for-teaching-in-higher-education-to-have-critical-perspectives/), retrieved 2026-11-23 |
| **URL** | https://www.tandfonline.com/journals/cthe20 (live page returns HTTP 403 to the research tool; Wayback copy 2025-12-15: https://web.archive.org/web/20251215180644/https://www.tandfonline.com/journals/cthe20) |
| **Author Guidelines** | Live page https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=cthe20 returns HTTP 403. Wayback copies read: https://web.archive.org/web/20221006133515/https://www.tandfonline.com/action/authorSubmission?journalCode=cthe20&show=instructions& (page states "Updated 16th August 2022") and https://web.archive.org/web/20220618120116/https://www.tandfonline.com/action/authorSubmission?journalCode=cthe20&page=instructions& . Author guidance from the editors: https://teachinginhighereducation.wordpress.com/2020/02/01/seven-questions-for-potential-authors-how-to-get-published-in-teaching-in-higher-education/ |
| **Society / Association** | None found on the pages read |
| **Editorial Board Location** | UK-led: the editor is listed at the University of Manchester, UK, and six executive editors at institutions in the UK (4), South Africa (1) and Japan (1) (journal information page, Wayback copy 2025-11-19, https://web.archive.org/web/20251119053632/https://www.tandfonline.com/action/journalInformation?journalCode=cthe20). OpenAlex spine country code: GB |
| **OpenAlex ID** | Not recorded in the local spine snapshot; ISSN lookup via `scripts/query_spine.py --issn 1356-2517` (snapshot 2026-07-13) |

---

## Metrics

> Source for the OpenAlex figures: the local spine, an OpenAlex snapshot dated 2026-07-13 (`scripts/query_spine.py --issn 1356-2517`; OpenAlex's live API was unavailable for this pass). Speed and acceptance figures are the publisher's own, from the journal information page (Wayback copy 2025-11-19, https://web.archive.org/web/20251119053632/https://www.tandfonline.com/action/journalInformation?journalCode=cthe20). JCR impact factor and quartile appear on that page but are paywalled data and deliberately not restated; SJR, SNIP and CiteScore are likewise not restated. The 2-year mean citedness below is an OpenAlex proxy, not a JCR figure.

| Metric | Value | Date |
|--------|-------|------|
| **Impact Factor** | Not stated (JCR is paywalled) | |
| **5-Year IF** | Not stated (JCR is paywalled) | |
| **h-index** | 128 (OpenAlex snapshot via spine) | 2026-07-13 |
| **CiteScore** | Not stated (Scopus not accessed) | |
| **Acceptance Rate** | 8%, publisher-reported: "articles accepted in the previous calendar year as percentage of all papers receiving a final decision", updated annually in February (journal information page, Wayback copy 2025-11-19, so the year is 2024) | 2025-11-19 |
| **Desk Rejection Rate** | Blank. No separate rate. An editor's blog post says the journal receives over 500 submissions a year and publishes around 50 plus special issues, and that "the vast majority of the remainder are rejected before the peer review process" (https://teachinginhighereducation.wordpress.com/2020/02/01/seven-questions-for-potential-authors-how-to-get-published-in-teaching-in-higher-education/, post dated 2020-02-01) | 2020-02-01 |
| **Quartile (by field)** | Not stated (SJR not read). SciRev shows a popularity-score quartile (Q2 in its Education category), which is a SciRev measure, not a citation quartile (https://scirev.org/journal/teaching-in-higher-education/) | 2026-11-23 |
| **2-yr Mean Citedness (OpenAlex IF proxy)** | 2.64 (OpenAlex snapshot via spine; proxy, not JCR) | 2026-07-13 |
| **i10-index** | Not in the spine snapshot | |
| **Total Works** | 2147 (OpenAlex snapshot via spine, all years and work types) | 2026-07-13 |

### Review Cycle Time

> Publisher-reported medians from the journal information page (Wayback copy 2025-11-19). Speed figures are based on the six months before the page was captured; the page says some manuscripts will take longer than the average shown. The first-decision figure includes desk rejections.

| Stage | Typical Time | Notes |
|-------|-------------|-------|
| **Time to first decision** | 32 days (median, includes manuscripts not sent for peer review) | Publisher-reported |
| **Time to first review** | 98 days from submission to first post-review decision (median, for manuscripts sent out for review) | Publisher-reported |
| **Time to acceptance (total)** | Blank. SciRev has 0 reviews (https://scirev.org/reviews/teaching-in-higher-education/) and LetPub shows 0 reviews (https://www.letpub.com/journal-selector/journal/11909); retrieved 2026-11-23 | |
| **Time to publication (after acceptance)** | 29 days from acceptance to online publication of the Version of Record (median over the six months before 2025-11-19) | Publisher-reported |

### Publication Frequency

| Aspect | Detail |
|--------|--------|
| **Schedule** | 8 issues per year (journal information page, Wayback copy 2025-11-19). The home-page copy of 2025-12-15 shows volume 30 issue 8 (2025) as the current issue |
| **Articles per year (approx.)** | Crossref journal-article records by published year, window 2021-11-23 to 2026-11-23 (https://api.crossref.org/works?filter=issn:1470-1294,from-pub-date:2021-11-23; 440 records, all typed journal-article, so comments and Points of Departure pieces are included): 2021 = 12 (December only), 2022 = 81, 2023 = 63, 2024 = 68, 2025 = 104, 2026 = 112 (partial year). The 2020 editor blog post says "around 50" published per year plus special issues. Retrieved 2026-11-23 |
| **Special issues?** | Yes. The journal states it runs special issues and "virtual" special issues of past articles (journal information page, Wayback copy 2025-11-19). Calls listed on that copy: Plural Values in Humanities Education, https://think.taylorandfrancis.com/special_issues/plural-values-in-humanities-education/ ; and Teaching and Marginalised Communities: Participatory Approaches, Pedagogies and Power, https://think.taylorandfrancis.com/special_issues/teaching-and-marginalised-communities-participatory-approaches-pedagogies-and-power/ (call pages themselves not read; whether they are still open is not known) |

---

## Policies

### Peer Review

| Aspect | Detail |
|--------|--------|
| **Type** | Anonymised refereeing after editor screening. The instructions copy (updated 2022-08-16) says that once a paper has been assessed for suitability by the editor it is "double blind peer reviewed" by independent anonymous expert referees (https://web.archive.org/web/20221006133515/https://www.tandfonline.com/action/authorSubmission?journalCode=cthe20&show=instructions&). The aims text on the information page (copy 2025-11-19) says at least two anonymous referees "from the journal's international Editorial Board" (https://web.archive.org/web/20251119053632/https://www.tandfonline.com/action/journalInformation?journalCode=cthe20). Retrieved 2026-11-23 |
| **Transferable / Cascade?** | Blank. No source read |
| **Reviewer reports published?** | Not as described on any page read |
| **Typical R+R rounds** | Blank. No source found |
| **Reviewer recommendations** | Blank. No source found |

### AI Policy

| Aspect | Detail |
|--------|--------|
| **Has journal-specific AI policy?** | No journal-specific policy found; the instructions copies read predate the publisher policy and the live page returns HTTP 403. The publisher-wide policy applies and says some journals may allow AI use only for language improvement, so authors should check the instructions page |
| **Explicit permission gate?** | No gate found. Use is allowed with a mandatory disclosure statement |
| **Leniency (1-5)** | 3 (allowed with mandatory disclosure; same rubric as the Mind entry) |
| **Summary** | AI tools cannot be listed as authors. Authors must acknowledge any generative AI use with the tool name and version, how it was used and why, in a specific disclosure statement. Permitted: idea generation, copyediting and language improvement, translation, literature classification, coding assistance. Not accepted: text or code generation without rigorous revision, synthetic data to replace missing data, inaccurate generated content including abstracts. Creating or manipulating research outputs or images is prohibited. Editors and reviewers may not upload unpublished manuscripts into AI tools. Retrieved 2026-11-23 |
| **Source URL** | https://taylorandfrancis.com/our-policies/ai-policy/ |

### Preprint Policy

> Publisher-level policy, not journal-specific. Source: https://authorservices.taylorandfrancis.com/research-impact/sharing-versions-of-journal-articles/ (retrieved 2026-11-23). The journal-specific embargo period was not looked up (the page says it is on the publisher's Open Access Cost Finder).

| Stage | Allowed? | Notes |
|-------|----------|-------|
| Pre-submission | Yes | Posting on a non-commercial preprint server such as arXiv or SocArXiv is not considered duplicate publication. The journal's own instructions copy adds that anonymity cannot be guaranteed for a manuscript already on a preprint server (https://web.archive.org/web/20221006133515/https://www.tandfonline.com/action/authorSubmission?journalCode=cthe20&show=instructions&) |
| Under review | Blank | The page speaks of the pre-submission version and does not separately address the under-review stage |
| Post-acceptance (AAM) | Yes, with embargo for repositories | Accepted Manuscript may go on a personal website at any time after publication; repositories and scholarly networks after an embargo, typically 18 months for social sciences and humanities counted from first online publication of the Version of Record. Embargo: 18 months is the publisher's typical figure, not confirmed for this journal |
| Version of Record | Open access articles may be shared freely | Per the same page |

### Open Access

| Aspect | Detail |
|--------|--------|
| **Model** | Hybrid: "part of the Taylor & Francis Open Select publishing program" (journal information page, Wayback copy 2025-11-19) |
| **APC (if OA chosen)** | Blank. The amount sits behind the publisher's APC finder and was not read. The page says no APC applies if the author does not choose open access, and the instructions copy (2022) lists no submission fees, publication fees or page charges, with print colour figures charged (GBP 300 for one figure at that date) |
| **Read & Publish agreements** | Blank. The page says institutional agreements may reduce or waive the APC; no list read |

---

## Format

> Source: instructions-for-authors Wayback copies (2022-06-18 and 2022-10-06, page updated 2022-08-16), https://web.archive.org/web/20221006133515/https://www.tandfonline.com/action/authorSubmission?journalCode=cthe20&show=instructions& ; the live page returns HTTP 403, so current wording may differ. Retrieved 2026-11-23.

| Aspect | Detail |
|--------|--------|
| **Article types accepted** | The instructions copy lists one type, original articles; manuscripts in English only. The aims text also describes a "Points of Departure" format for critical and reflective pieces, speculative fiction, responses and polemics, reviewed in the regular process (journal information page, copy 2025-11-19). Recent items on the home-page copy of 2025-12-15 carry the labels Article and Comment |
| **Word limit** | A typical paper should be no more than 7000 words, inclusive of the abstract, tables and figure or table captions (instructions copy 2022). Points of Departure pieces: around 3,000 words, not including references (information page copy 2025-11-19). Crossref page ranges give a median article length of 17 pages over 438 of 440 records with parseable ranges, 2021-2026 |
| **Word limit negotiability** | Blank. The limit is worded as a typical-paper ceiling; no statement on exceptions found |
| **Abstract limit** | Unstructured abstract of 150 words; 5 to 6 keywords (instructions copy 2022) |
| **Reference limit** | Blank. The archived list of what the 7000 words include does not name references |
| **Supplementary material** | Supplemental material (video, dataset, files) is published via Figshare (instructions copy 2022) |
| **Figure/Table limits** | No count limit found. Figure resolution requirements and an editable-table requirement are given in the instructions copy; extra colour figures are charged only for print |
| **Style / submission format** | Any spelling style if consistent; single quotation marks; long quotations indented; title page with full author names and affiliations; Word or LaTeX (LaTeX also as PDF plus source); Routledge submission portal; Crossref similarity screening of all submissions; an ethics statement (committee name and reference number) is required where human participants were involved (instructions copy 2022) |

---

## Subject Density

> Source: Crossref journal-article records of ISSN 1470-1294 published 2021-11-23 to 2026-11-23 (440 records; 0 carry an abstract, so all counts below use titles only and are lower bounds), retrieved 2026-11-23. OpenAlex topic counts were not obtained because OpenAlex returned its first rate-limit response during this batch and was not used again, as instructed.

### Top Topics (last 5 years)

| Topic | Article Count |
|-------|--------------|
| Titles with "student" or "students" | 92 of 440 |
| Titles with assessment or feedback | 54 of 440 |
| Titles with "critical" or "critique" | 47 of 440 |
| Titles with "academic" | 44 of 440 |
| Titles with AI, ChatGPT or generative | 25 of 440 |
| Titles with decolonial or colonial terms | 22 of 440 |
| Titles with doctoral, PhD or supervision | 22 of 440 |
| Titles with climate or sustainab- | 16 of 440 |

### Orientation

> Counts are Crossref titles matching a word-boundary regular expression (for example `\btheor\w*`), over 440 records; shares use 440 as denominator. Title-only counts understate how often a method or theme appears in the body or abstract.

| Dimension | Assessment |
|-----------|------------|
| **Empirical vs. Theoretical** | The journal states a theorised, critical orientation (aims text, journal home copy 2025-12-15 and information page copy 2025-11-19). Title counts: theor- 15 (3.4%), concept- or philosoph- 10 (2.3%), "critical" or "critique" 47 (10.7%); empirical terms in titles are rarer (survey 0, quantitative or statistic or experiment 1) |
| **Quantitative vs. Qualitative** | Both rare in titles: interview or qualitative 5 (1.1%), quantitative terms 1 (0.2%). An editor's blog post says quantitative submissions are welcome if critical, accessible and rigorous, and that large-scale descriptive surveys are generally not published (https://teachinginhighereducation.wordpress.com/2020/02/01/seven-questions-for-potential-authors-how-to-get-published-in-teaching-in-higher-education/) |
| **Cross-disciplinary openness** | The aims text says the journal seeks "a discourse of teaching and learning which transcends disciplinary boundaries and specialisms". The editors say it is not a general higher-education journal and that papers without clear engagement with teaching are rejected (blog post above) |

---

## Soft Metadata

### Epistemological & Political Leanings

> Evidence layers: the journal's aims text (Wayback copy 2025-11-19 of the information page); two posts on the journal's own blog (retrieved 2026-11-23); Crossref titles and affiliation strings of 440 journal-article records, 2021-11-23 to 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Cross-cultural friendliness** | Literal country-name counts over Crossref author-affiliation strings (articles with at least one affiliation string that contains the name; 435 of 440 records carry an affiliation string, and 226 of those 435 contain none of the 44 country names searched (including England, Scotland, Wales and Northern Ireland), because Crossref affiliation strings often give only an institution, so every count below is a lower bound and says nothing about the 226): United Kingdom 51 (case-sensitive regex `\bUnited Kingdom\b|\bUK\b|\bU\.K\.`; England 7, Wales 3 and Scotland 2 are literal names counted separately and not added), Australia 38, United States 28 (`\bUnited States\b|\bUSA\b|\bU\.S\.A\.?|\bUS\b`), Hong Kong 23, China 18, South Africa 18, New Zealand 9, Canada 9, Spain 5, South Korea 4, Netherlands 4, Denmark 3, Sweden 3 (other countries use `\b<name>\b`; recomputed 2026-11-23 from the 440 Crossref records, https://api.crossref.org/journals/1470-1294/works). The earlier figures (UK 133, Australia 83 and so on) came from an unpublished keyword list over institution and place names and were removed. The aims text asks for engagement with "a variety of cultural and disciplinary contexts represented in higher education internationally" |
| **Editorial-board geography** | The journal's information page (Wayback copy 2025-11-19, fetched in its raw id_ form, https://web.archive.org/web/20251119053632id_/https://www.tandfonline.com/action/journalInformation?journalCode=cthe20) lists 137 names: 1 editor, 1 social media editor, 6 executive editors, 2 founding editors and 127 board members (1+1+6+2+127 = 137). Country as printed at the end of each affiliation, one label per name (the entry with two affiliations, Belfast and South Africa, is counted once under South Africa, its last label): UK 45, Australia 15, South Africa 15, USA 9, New Zealand 6 (printed as "NZ" 3 or "New Zealand" 3), Canada 5, China 4, Italy 3, Sweden 3, Portugal 2, Ireland 2 (one of the two is a Belfast institution labelled Ireland), India 2, Hong Kong 2, Denmark 2, Netherlands 2, and one each labelled England, Northern Ireland, Japan, Spain, South Korea, Qatar, Israel, Finland, Estonia, Egypt, Colombia, Malaysia, Cyprus, Switzerland and "Brussels"; 5 names print no country label (an Edinburgh university, a Newcastle university whose country is not printed, an institution whose name ends in "Sri Lanka", one whose name ends in "China", and one truncated "Chin"). Tallies sum to 137 (45+15+15+9+6+5+4+3+3+2+2+2+2+2+2 = 117, plus 15 single labels = 132, plus 5 without a label). Counted by script from the page text on 2026-11-23 |
| **Non-Western epistemology openness** | The aims text names "social and epistemic justice, and equity" among the values the journal welcomes work on. The editors' criticality post lists feminism, critical race theory, post-colonial and decolonial theory and critical discourse analysis as ways a critical perspective is enacted, and notes power imbalances between the Global North and South and the dominance of English (https://teachinginhighereducation.wordpress.com/exploring-what-it-means-for-teaching-in-higher-education-to-have-critical-perspectives/). Crossref titles: decolonial or colonial terms 22 of 440 (5.0%), "Indigenous" or Māori 3 (0.7%) |
| **Diversity topic receptiveness** | See the Sensitive Topics table. Crossref titles: gender, feminist or women 9 (2.0%); racial, racism, Black or whiteness 9 (2.0%; regex in Method notes); queer, LGBT or trans 1 (0.2%); disability or neurodiversity 5 (1.1%) |
| **Dominant theoretical tradition** | Stated, not counted: "critical and theorised research" is the journal's tagline on its home copy (https://web.archive.org/web/20251215180644/https://www.tandfonline.com/journals/cthe20), and the criticality post names the Frankfurt School, critical pedagogy, ecopedagogy, participatory and emancipatory approaches. Crossref titles naming Bourdieu, Foucault, Freire, Bernstein or Legitimation Code: 6 of 440 (1.4%). The most cited records of the window in Crossref (citation counts at retrieval) are an inclusive-assessment paper (136; https://doi.org/10.1080/13562517.2021.2021395), a 2024 paper on generative AI and trust in teacher-student relationships (92; https://doi.org/10.1080/13562517.2024.2341005), a 2023 paper on colonial futurities in climate education (71; https://doi.org/10.1080/13562517.2023.2193667) and a 2022 systematic review of formal learning spaces (57; https://doi.org/10.1080/13562517.2022.2066469) |
| **Stated position** | The aims text says submissions that do not offer a critical perspective on teaching in higher education "are not considered appropriate for the journal's peer review process", and lists what is not published (below) |

### Framing Requirements

- **Mandatory framing?** The aims text states that submissions without a critical perspective on teaching in higher education are not sent to peer review, and that authors are strongly encouraged to engage with and build on previous contributions in the journal (information page, Wayback copy 2025-11-19, https://web.archive.org/web/20251119053632/https://www.tandfonline.com/action/journalInformation?journalCode=cthe20).
- **What is not published** (same page): descriptions or evaluations of policy or practice; localised case studies not contextualised and theorised; large-scale surveys not theoretically and critically analysed; studies replicating earlier work without originality.
- **What kind of engagement?** The editors' blog post gives seven screening questions: fit with the aims page; a critical perspective, with the note that the journal tends to accept papers engaging with problems rather than offering solutions; real engagement with teaching (the journal is "not a general higher education journal"); broad appeal beyond a single context; use of earlier articles in the journal; for quantitative work, critical, accessible and rigorous treatment; and not being too closely focused on practice, since the journal does not generally publish descriptions of new teaching approaches or small-scale evaluations (https://teachinginhighereducation.wordpress.com/2020/02/01/seven-questions-for-potential-authors-how-to-get-published-in-teaching-in-higher-education/, post dated 2020-02-01).
- **Article type and length**: original articles of up to about 7000 words including the abstract, tables and captions, with a 150-word abstract; Points of Departure pieces of around 3,000 words (instructions copy 2022-10-06; information page copy 2025-11-19).
- **Consequences of ignoring it**: the editors state that the vast majority of the roughly 500 submissions a year not published are rejected before peer review, either for falling outside scope or for insufficient rigour, and that papers without clear engagement with teaching are rejected (blog post above).

### Methodological Preferences

> Counts: Crossref titles of 440 journal-article records published 2021-11-23 to 2026-11-23 (0 with abstract; lower bounds). Scoring convention of this research pass (its own, not an external standard): share 0 = 0; under 1% = 1; 1-5% = 2; over 5% = 3; 4-5 only with a cited editorial statement. Because only titles were searchable, the count-based scores understate real method frequency; the editorial statements carry more weight than the counts here. Regexes are word-boundary patterns, for example `\binterview\w*|\bqualitative\b`.

| Method | Receptiveness (0-5) | Evidence |
|--------|---------------------|----------|
| Quantitative experimental | 1 | Titles with quantitative, statistic, regression or experiment terms: 1 of 440 (0.2%); "survey" in titles 0. Editors: quantitative work is welcome if critical, accessible and rigorous, and large-scale descriptive surveys are generally not published (blog post, https://teachinginhighereducation.wordpress.com/2020/02/01/seven-questions-for-potential-authors-how-to-get-published-in-teaching-in-higher-education/) |
| Qualitative interviews | 2 | Titles with interview or qualitative: 5 of 440 (1.1%); the journal's criticality post cites interview-based, critical discourse analysis and participatory action research papers as examples of critical approaches (https://teachinginhighereducation.wordpress.com/exploring-what-it-means-for-teaching-in-higher-education-to-have-critical-perspectives/) |
| Autoethnography | 2 | Titles with autoethnography or narrative: 5 of 440 (1.1%); the Points of Departure format invites reflective and experimental pieces (information page copy 2025-11-19) |
| Theoretical / Conceptual | 4 | Editorial statement: the journal "introduces theoretical perspectives and insights" and excludes localised case studies "not contextualized and theorised" (aims text, information page copy 2025-11-19, https://web.archive.org/web/20251119053632/https://www.tandfonline.com/action/journalInformation?journalCode=cthe20). Titles with theor-: 15 of 440 (3.4%); with "critical" or "critique": 47 (10.7%) |
| Mixed methods | 1 | Not counted separately; titles with participatory, action research, co-creation or co-design: 3 of 440 (0.7%) |
| Meta-analysis / systematic review | 2 | Titles with systematic review, scoping review or meta-analysis: 6 of 440 (1.4%); one is among the most cited of the window (https://doi.org/10.1080/13562517.2022.2066469, 57 Crossref citations) |
| Case study | 1 | Titles with "case study": 2 of 440 (0.5%); the aims text excludes localised case studies that are not contextualised and theorised |

### Voice & Style

| Aspect | Detail |
|--------|--------|
| **First-person voice acceptance (0-5)** | Not scored. No abstracts are available (Crossref 0 of 440; the publisher's article pages return HTTP 403), so first-person use in article openings could not be sampled. The journal invites "critical accounts of lived experiences of higher education pedagogies" (aims text, copy 2025-11-19) and reflective Points of Departure pieces |
| **Expected density** | Up to about 7000 words including abstract, tables and captions (instructions copy 2022). Crossref page ranges give a median length of 17 pages across 438 of 440 records, 2021-2026 (https://api.crossref.org/works?filter=issn:1470-1294,from-pub-date:2021-11-23) |
| **Abstract and keywords** | Unstructured abstract of 150 words; 5 to 6 keywords; authors may add a translated abstract on acceptance (instructions copy 2022-10-06) |
| **Writing style notes** | Any spelling style if consistent; single quotation marks; long quotations indented; the editors ask for papers that explain their national and institutional context for an international readership and avoid unexplained jargon (blog post, https://teachinginhighereducation.wordpress.com/2020/02/01/seven-questions-for-potential-authors-how-to-get-published-in-teaching-in-higher-education/) |
| **Authorship pattern** | Crossref author counts for the 440 records: 139 single-author, 134 two authors, 77 three, 44 four, 19 five, 23 six or more, and 4 with no listed author (retrieved 2026-11-23) |

### Reviewer Pool Characteristics

Reviewer behaviour itself is not observable from public pages; what follows is what public pages do show.

| Aspect | Detail | Evidence |
|--------|--------|----------|
| **Dominant tradition** | The aims text says refereeing is by anonymous referees "from the journal's international Editorial Board". The board page copy lists 137 names: an editor, a social media editor, 6 executive editors, 2 founding editors and 127 board members; the country spread is given under Epistemological & Political Leanings. Disciplines are not stated on the page | https://web.archive.org/web/20251119053632/https://www.tandfonline.com/action/journalInformation?journalCode=cthe20 ; retrieved 2026-11-23; board composition may have changed since |
| **Reviewer list size** | 137 named editors and board members (127 of them board members); the board is the stated referee source, so this is an upper bound on the named pool, not a count of reviewers used | Same page |
| **Review model** | Editor screening, then anonymised review by at least two referees; "double blind" in the 2022 instructions copy | https://web.archive.org/web/20221006133515/https://www.tandfonline.com/action/authorSubmission?journalCode=cthe20&show=instructions& |
| **Reviewer competence variance** | Blank. No first-hand report exists: SciRev 0 reviews, LetPub 0 reviews | https://scirev.org/reviews/teaching-in-higher-education/ ; https://www.letpub.com/journal-selector/journal/11909 |
| **Quantitative mindset bias on qualitative work?** | Blank. No source. The editors' statements on quantitative work are recorded under Methodological Preferences; they describe editorial screening, not reviewer behaviour | Editors' blog post |
| **Discourse community signals (author side)** | Author affiliations as a proxy, literal country names only: United Kingdom 51, Australia 38, United States 28, Hong Kong 23, China 18, South Africa 18 of 440 Crossref records with at least one affiliation string containing the name (lower bounds; 226 of 435 records with an affiliation name none of the searched countries; regexes under Cross-cultural friendliness) | Crossref records, retrieved 2026-11-23 |

### Sensitive Topics

> Counts are Crossref titles (440 records, no abstracts, lower bounds) published 2021-11-23 to 2026-11-23 matching word-boundary patterns. A rating of High is used only where an editorial statement is cited.

| Topic Category | Receptiveness | Evidence |
|----------------|---------------|----------|
| Decolonial / postcolonial | High | Editorial statement: the criticality post names post-colonial and decolonial theory among the journal's critical approaches (https://teachinginhighereducation.wordpress.com/exploring-what-it-means-for-teaching-in-higher-education-to-have-critical-perspectives/); a Points of Departure example in the aims text concerns decolonising in a South African classroom. Titles with decolonial or colonial terms: 22 of 440 (5.0%) |
| Race and racism | High | The same post names critical race theory; the aims text names social and epistemic justice and equity (https://web.archive.org/web/20251119053632/https://www.tandfonline.com/action/journalInformation?journalCode=cthe20). Titles with racial, racism, Black or whiteness: 9 of 440 (2.0%; the earlier 10 included "Opening the black box of degree classification algorithms", which is not about race, so the regex now excludes "black box") |
| Gender and feminism | High | The criticality post names feminism. Titles with gender, feminist or women: 9 of 440 (2.0%) |
| Sexual and gender minorities | Rare | Titles with queer, LGBT or trans terms: 1 of 440 (0.2%) |
| Disability | Present | Titles with disability or neurodiversity terms: 5 of 440 (1.1%) |
| Indigenous knowledge | Rare | Titles with Indigenous or Māori: 3 of 440 (0.7%) |
| AI and technology | Frequently published | Titles with AI, ChatGPT or generative terms: 25 of 440 (5.7%); one of the most cited of the window concerns generative AI (https://doi.org/10.1080/13562517.2024.2341005) |
| Climate and sustainability | Present | Titles with climate or sustainab-: 16 of 440 (3.6%); https://doi.org/10.1080/13562517.2023.2193667 |
| Political and institutional critique | Present | Titles naming neoliberal terms: 1 of 440; the aims text welcomes work on the impact of policy, funding, institutional change and marketisation. The editors' blog lists "exploring the impact of marketisation" among critical topics |

### Practical Concerns

| Concern | Detail |
|---------|--------|
| **IRB requirement strictness** | An ethics statement is required where human participants were involved: the ethics committee's name and a reference number where available (instructions copy 2022-10-06, https://web.archive.org/web/20221006133515/https://www.tandfonline.com/action/authorSubmission?journalCode=cthe20&show=instructions&) |
| **Single-author acceptance** | Single-author papers are common: 139 of 440 Crossref records (31.6%), 2021-11-23 to 2026-11-23 |
| **Independent scholar friendliness** | Affiliation rule: full name and affiliation on the cover page, defined as where the research was conducted; no independent-scholar rule stated (instructions copy 2022). No data on acceptance of such authors |
| **Data transparency requirement** | The journal applies the publisher's Basic Data Sharing Policy: sharing is encouraged, not required, and a data availability statement is encouraged (instructions copy 2022) |
| **OPSEC compatibility** | Anonymised review, but the title page carries full author names and affiliations and a manuscript on a preprint server loses any anonymity guarantee (instructions copy 2022). Pre-submission preprints are allowed by the publisher (https://authorservices.taylorandfrancis.com/research-impact/sharing-versions-of-journal-articles/) |
| **AI use** | Disclosure statement required; AI cannot be an author (https://taylorandfrancis.com/our-policies/ai-policy/), retrieved 2026-11-23 |
| **Open access and cost** | Hybrid Open Select; no submission or page charges on the non-OA route in the 2022 instructions copy; APC amount not read (https://authorservices.taylorandfrancis.com/publishing-open-access/open-select/) |
| **Originality screening** | Crossref similarity screening of all submissions (instructions copy 2022) |
| **Submission volume** | More than 500 submissions a year according to an editor's 2020 blog post, against about 8% acceptance reported for 2024 (journal information page copy 2025-11-19): the two figures are from different years |

### AI-Research Notes (sources, blanks, and cross-language checks)

**signal_quality (0-5)**: overall 3. Per layer: journal-own policy and aims facts 3 (Wayback copies of the instructions are from 2022, the information page from 2025-11-19; the live pages return HTTP 403); editors' blog posts 4 (read live, dates stated); Crossref counts 2 (440 records, 0 with abstract, so titles only); OpenAlex 1 (spine snapshot figures only); publisher-wide policies 4; experiential layer 0.

**Sources cited across this entry:**
- https://web.archive.org/web/20251119053632/https://www.tandfonline.com/action/journalInformation?journalCode=cthe20 (information page, aims, metrics, board, Wayback copy 2025-11-19)
- https://web.archive.org/web/20251215180644/https://www.tandfonline.com/journals/cthe20 (home page, Wayback copy 2025-12-15)
- https://web.archive.org/web/20221006133515/https://www.tandfonline.com/action/authorSubmission?journalCode=cthe20&show=instructions& and https://web.archive.org/web/20220618120116/https://www.tandfonline.com/action/authorSubmission?journalCode=cthe20&page=instructions& (instructions, copies of 2022)
- https://teachinginhighereducation.wordpress.com/2020/02/01/seven-questions-for-potential-authors-how-to-get-published-in-teaching-in-higher-education/
- https://teachinginhighereducation.wordpress.com/exploring-what-it-means-for-teaching-in-higher-education-to-have-critical-perspectives/
- https://api.crossref.org/journals/1470-1294 and https://api.crossref.org/works?filter=issn:1470-1294,from-pub-date:2021-11-23 (440 records)
- local spine, `scripts/query_spine.py --issn 1356-2517` (OpenAlex snapshot 2026-07-13)
- https://taylorandfrancis.com/our-policies/ai-policy/
- https://authorservices.taylorandfrancis.com/research-impact/sharing-versions-of-journal-articles/
- https://authorservices.taylorandfrancis.com/publishing-open-access/open-select/
- https://scirev.org/journal/teaching-in-higher-education/ and https://scirev.org/reviews/teaching-in-higher-education/
- https://www.letpub.com/journal-selector/journal/11909

**Unreadable pages (never filled from memory):**
- unreadable live: https://www.tandfonline.com/journals/cthe20 , /action/journalInformation?journalCode=cthe20 , /action/authorSubmission?show=instructions&journalCode=cthe20 (all HTTP 403 to the research tool and to the fetch tool). Facts from them come from the Wayback copies named above and carry those dates.
- The newest instructions copy found is from 2022, so any change since (word limit, AI wording, ethics, data rules) is not captured.
- The Wayback CDX index was offline during this pass, so no search for further copies was possible beyond the availability API.
- https://think.taylorandfrancis.com/special_issues/ call pages: not read.

**Fields deliberately left blank, and why:**
- Desk rejection rate (as a rate), total time to acceptance, reviewer culture, reviewer competence, quantitative bias: no first-hand source (SciRev 0 reviews, LetPub 0 reviews).
- Abbreviation, transferability, R+R rounds, whether references count in the word limit, APC amount: not found on any page read.
- First-person voice in article openings: no abstract source (Crossref 0 of 440; publisher article pages 403).
- Impact factor, quartile, CiteScore, SJR: paywalled or licensed; the publisher's page displays them but they are not restated.

**Cross-language and forum checks performed (all returned zero journal-specific first-hand reports):**
- SciRev (English): journal page exists, 0 reviews, popularity score only.
- LetPub: journal page exists, 0 reviews.
- 小木虫 (muchong), 知乎 (zhihu), fabiaoji, sciencenet: a web search restricted to these domains returned only experiences for other journals (Teaching and Teacher Education, Higher Education, Studies in Higher Education) and none for this one.
- Reddit: the search tool refuses reddit.com-restricted searches; one general web search returned no thread, so Reddit was not directly searched.

**Method notes:** Crossref records were fetched with cursor paging, no key, and counted locally with word-boundary regular expressions over lower-cased titles. Author countries are literal country-name matches (word-boundary regexes, listed under Cross-cultural friendliness) over Crossref affiliation strings, article level, lower bounds. Race regex (case-insensitive, titles): `\bracial|\bracis|\bwhiteness|\bblack\b(?! box)`, 9 of 440. Gender regex `\bgender|\bfeminis|\bwomen\b` gives 9 of 440 (reproduces). The editorial-board country counts were made from the archived page text and are as printed. OpenAlex live counts were not used: OpenAlex hit its rate limit earlier in this batch (for another journal) and was not used again.

---

## Strategic Notes

> Each statement below follows from a fact recorded above and names it.

### Hard Blockers

- **Scope**: manuscripts that do not offer a critical perspective on teaching in higher education are not sent to peer review (Framing Requirements; aims text, information page copy 2025-11-19).
- **Excluded forms**: descriptions or evaluations of policy or practice, localised case studies not contextualised and theorised, large-scale surveys not theoretically and critically analysed, and replication studies without originality are stated as not published (Framing Requirements).
- **Teaching focus**: papers without a clear engagement with teaching are rejected (editors' blog post, Framing Requirements).
- **Language**: English only (Format; instructions copy 2022).
- **AI use**: undisclosed generative AI use or AI-produced text, data or images breach the publisher policy (AI Policy).
- No other hard blocker is supported by a fact read.

### Soft Tax

- **Desk rejection**: the editors state most non-published submissions are rejected before peer review, and the journal reports an 8% acceptance rate for 2024 (Metrics; Practical Concerns). The 32-day median to first decision includes those desk rejections (Review Cycle Time).
- **Time**: for manuscripts sent to review, the median to first post-review decision is 98 days (Review Cycle Time; publisher-reported).
- **Positioning**: the editors expect engagement with earlier articles in the journal and a theorised, problem-oriented stance rather than solutions (Framing Requirements).
- **Anonymisation**: review is anonymised but a title page with author names is part of the submission; a preprint removes any anonymity guarantee (Practical Concerns).
- **Open access cost**: green deposit of the accepted manuscript is subject to a typical 18-month embargo for social-science and humanities journals on the publisher page (Preprint Policy; not confirmed for this journal); gold open access carries an APC whose amount was not found (Open Access).

### Best Suited For

- Theorised, critical analyses of teaching, curriculum, assessment or doctoral supervision in higher education, with a wider-than-local argument: the journal's tagline and aims text (Epistemological & Political Leanings; Framing Requirements), and titles with "critical" in 47 of 440 records (Subject Density).
- Decolonial, feminist, critical-race and social-justice framings of teaching: named in the editors' criticality post (Sensitive Topics).
- Work that engages earlier articles of the journal: the editors state this as an expectation (Framing Requirements).
- Short provocations or reflective pieces of about 3,000 words through Points of Departure (Format).
- Quantitative work that is explicitly critical and well explained for non-specialists (Methodological Preferences; editors' statement).

### Not Recommended For

- Reports of a new teaching method or a small-scale evaluation without a wider argument, or descriptive large-scale surveys: stated as generally not published (Framing Requirements).
- School-teacher-training or language-teaching papers without relevance to wider debates: the editors say they tend not to accept these (blog post, Framing Requirements).
- Work focused on employment outcomes, university management or student profiling rather than teaching: the editors report receiving many such submissions and rejecting those without clear connection to teaching (blog post).
- Authors who need a verified total time to acceptance: only stage medians are published (Review Cycle Time).

### Rejection Fallback Chain

> No source states where rejected authors usually go. The rows below are topical neighbours; only entries that exist in this corpus are linked. They are not a claim about acceptance odds.

| Rank | Journal | Why this fallback works |
|------|---------|------------------------|
| 1 | [British Journal of Educational Studies](british-journal-of-educational-studies.md) | Entry exists in this corpus; general education studies venue. No fit evidence collected here |
| 2 | [Learning, Media and Technology](learning-media-and-technology.md) | Entry exists in this corpus; critical orientation on technology in education, relevant to the journal's frequent AI and digital titles (Subject Density). No fit evidence collected here |
| 3 | Studies in Higher Education | Same subject area (higher education); no entry in this corpus and no fit evidence collected here |

---

## Changelog

| Date | Change | By |
|------|--------|----|
| 2026-11-23 | Initial entry (scaffold from the local OpenAlex spine snapshot and Crossref; structural fields only) | @your-handle |
| 2026-11-23 | AI deep research pass; no first-hand human reports | AI-assisted (maintainer-directed) |
| 2026-11-23 | Correction after independent check: board recounted from the 2025-11-19 copy (137 names = 1 editor + 1 social media editor + 6 executive + 2 founding + 127 board members, not 115) with country tallies summing to 137; race-title count 10 to 9 (2.0%) after removing the false hit "Opening the black box of degree classification algorithms"; author-affiliation counts replaced by literal country-name counts with stated regexes (UK 51, not 133) because the earlier keyword list was unpublished | AI-assisted (maintainer-directed) |
| 2026-11-23 | Promoted to Tier 1 under the written rule: tier1_gate passes; independent spot-check 8 of 8 sampled pairs supported; board counts recounted; banner removed; no first-hand human reports | AI-assisted (maintainer-authorised, not human-verified) |
