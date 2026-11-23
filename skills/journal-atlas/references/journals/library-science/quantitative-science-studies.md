<!-- schema: v1.3 -->
<!-- AI-researched entry — Journal Atlas v2 coverage pipeline. See docs/ATLAS_V2_DESIGN.md for methodology. -->
<!-- Written by an AI deep research pass (maintainer-directed) on 2026-11-23; scaffold built from the local spine snapshot and Crossref because the OpenAlex scaffold was not used. -->

# Quantitative Science Studies

> **Last verified**: 2026-11-23
> **Maintainer**: @Zaious
> **Venue type**: Journal
> **Evidence basis**: AI-researched, overall signal_quality **2/5** — per-fact source URLs with recorded blanks. MIT Press pages (direct.mit.edu) returned HTTP 403 to curl live; the publisher pages were read as Wayback copies: submission guidelines (2026-07-30), editorial information (2026-03-10), and the MIT open-access, release-schedule and authors pages (2026-11-15). The scope statement and the MIT Press generative-AI policy text were not read. Crossref abstract coverage is 96.2% for the window. Distinct from "Sourced" (deeper per-journal research, every claim cites a source) and "Estimated" (family-level estimate). See [SEED_DATA_QUALITY.md](../../../../../SEED_DATA_QUALITY.md).

---

## Identity

| Field | Value |
|-------|-------|
| **Abbreviation** | QSS, used inside the submission guidelines text only as the full name; no short title read in Crossref (https://api.crossref.org/journals/2641-3337; retrieved 2026-11-23). Left blank. DOIs use the prefix 10.1162 with "qss_a" |
| **Venue type** | Journal |
| **Publisher** | MIT Press (Crossref publisher string "MIT Press", https://api.crossref.org/journals/2641-3337, retrieved 2026-11-23; page title of the guidelines copy reads "MIT Press") |
| **ISSN (Print)** | Blank. Crossref lists only the electronic ISSN |
| **ISSN (Online)** | 2641-3337 (Crossref; footer of the guidelines copy) |
| **Founded** | Blank as a journal statement. Crossref's earliest DOI year is 2020, with 93 DOIs (https://api.crossref.org/journals/2641-3337, retrieved 2026-11-23) |
| **URL** | https://direct.mit.edu/qss (403 to curl on 2026-11-23) |
| **Author Guidelines** | https://direct.mit.edu/qss/pages/submission-guidelines, read only as a Wayback copy dated 2026-07-30 (https://web.archive.org/web/20260730174826id_/https://direct.mit.edu/qss/pages/submission-guidelines); the live page returned 403. Needs real-browser read: https://direct.mit.edu/qss/pages/submission-guidelines |
| **Society / Association** | International Society for Scientometrics and Informetrics (ISSI): the journal "serves as the official journal of the International Society for Scientometrics and Informetrics (ISSI)" and the ISSI Board appoints the Editor-in-Chief (editorial information page, Wayback copy 2026-03-10, https://web.archive.org/web/20260310170354id_/https://direct.mit.edu/qss/pages/editorial-info) |
| **Editorial Board Location** | Editor-in-Chief at Université de Montréal, Canada; 3 Associate Editors (Leiden, Netherlands; Bristol, no country printed; Fudan, China); 2 Editorial Assistants (names only); 38 board members, counted by country under Reviewer Pool Characteristics (editorial information page, Wayback copy 2026-03-10, https://web.archive.org/web/20260310170354id_/https://direct.mit.edu/qss/pages/editorial-info). Spine country code for the journal: US |
| **OpenAlex ID** | Not looked up (OpenAlex not called in this pass) |

---

## Metrics

> Source: local spine, an OpenAlex snapshot dated 2026-07-13 (`query_spine.py --issn 2641-3337`, 2026-11-23). JCR impact factor and quartile are paywalled and not stated. The 2-year mean citedness is an OpenAlex proxy, not a JCR figure.

| Metric | Value | Date |
|--------|-------|------|
| **Impact Factor** | Not stated (JCR is paywalled) | |
| **5-Year IF** | Not stated (JCR is paywalled) | |
| **h-index** | 43 (OpenAlex snapshot via spine, all years) | 2026-07-13 |
| **CiteScore** | Blank. Not read | |
| **Acceptance Rate** | Blank. SciRev has the editor-supplied fields empty ("n/a", https://scirev.org/journal/quantitative-science-studies/, retrieved 2026-11-23) | 2026-11-23 |
| **Desk Rejection Rate** | Blank. The guidelines say contributions deemed unsuitable by the Editor-in-Chief or an Associate Editor "can be rejected without further review", with no rate (Wayback copy 2026-07-30) | 2026-11-23 |
| **Quartile (by field)** | Not stated. Spine fields (snapshot 2026-07-13): Norwegian level 1, JUFO level 2 | 2026-07-13 |
| **2-yr Mean Citedness (OpenAlex IF proxy)** | 5.45 (OpenAlex proxy via spine, not JCR) | 2026-07-13 |
| **Total Works** | 460 (OpenAlex snapshot via spine, all years); cited-by count 11631 | 2026-07-13 |

### Review Cycle Time

| Stage | Typical Time | Notes |
|-------|-------------|-------|
| **Time to first decision** | The journal "will attempt to review each manuscript within five weeks of submission, but delays may be expected" (guidelines copy 2026-07-30, https://web.archive.org/web/20260730174826id_/https://direct.mit.edu/qss/pages/submission-guidelines) | Journal statement of intent, not a measured figure. SciRev has no review data (popularity score 77.4; https://scirev.org/journal/quantitative-science-studies/) |
| **Time to first review** | Blank. No separate figure | |
| **Time to acceptance (total)** | Blank. No source | |
| **Time to publication (after acceptance)** | Blank. No source | |

### Publication Frequency

| Aspect | Detail |
|--------|--------|
| **Schedule** | Continuous publication: the MIT Press release schedule lists Quantitative Science Studies as "open access 2026", "continuous publication", volume 7, in progress (Wayback copy 2026-11-15, https://web.archive.org/web/20261115102008id_/https://direct.mit.edu/journals/pages/release-schedule) |
| **Articles per year (approx.)** | Crossref DOI counts by issued year: 2020 = 93, 2021 = 76, 2022 = 58, 2023 = 52, 2024 = 55, 2025 = 62, 2026 = 69 to 2026-11-23 (https://api.crossref.org/journals/2641-3337). Crossref returns 312 journal-article records for 2021-11-23 to 2026-11-23, 300 with an abstract |
| **Special issues?** | Blank. None seen on the pages read |

---

## Policies

### Peer Review

| Aspect | Detail |
|--------|--------|
| **Type** | Single-anonymised: authors' names are disclosed to reviewers, reviewers stay anonymous unless they choose to disclose; the guidelines print the STM peer-review taxonomy as "Single anonymized". The Editor-in-Chief or an Associate Editor first judges suitability; in-scope articles and reviews go to external reviewers, "typically two or three", chosen by the editors, with author suggestions encouraged (guidelines copy 2026-07-30). The spine lists "Anonymous peer review" |
| **Transferable / Cascade?** | Blank. No source read |
| **Reviewer reports published?** | Yes after acceptance: the reviewer reports, author responses and editor decision letters "will be made openly available in Web of Science (formerly Publons)"; reviewers remain anonymous unless they choose otherwise. Reviewers of preprinted manuscripts are encouraged to post their reviews publicly, without revealing the submission to the journal (guidelines copy) |
| **Typical R+R rounds** | Blank. No source (SciRev empty) |
| **Reviewer recommendations** | Letters may go to external review at editorial discretion; reviewers are expected to keep the process confidential (guidelines copy) |

### AI Policy

| Aspect | Detail |
|--------|--------|
| **Has journal-specific AI policy?** | A publisher policy exists; its text was not read. The MIT Press authors page says "Information on MIT Press policies on the use of generative AI in scholarly publishing" is at https://direct.mit.edu/journals/pages/ai_guidelines (authors page, Wayback copy 2026-11-15, https://web.archive.org/web/20261115113327id_/https://direct.mit.edu/journals/pages/authors); that page has no archived copy and the live page returns 403. The journal's guidelines copy (2026-07-30) carries no AI policy text of its own, only a site-wide notice that content may not be used to train AI systems without MIT Press permission |
| **Explicit permission gate?** | Blank |
| **Leniency (1-5)** | Not scored (no journal rule read) |
| **Summary** | None read. Needs real-browser read: https://direct.mit.edu/journals/pages/ai_guidelines |
| **Source URL** | https://web.archive.org/web/20261115113327id_/https://direct.mit.edu/journals/pages/authors (pointer to the publisher policy) |

### Preprint Policy

> Source: guidelines copy 2026-07-30 (https://web.archive.org/web/20260730174826id_/https://direct.mit.edu/qss/pages/submission-guidelines). Policies may have changed since.

| Stage | Allowed? | Notes |
|-------|----------|-------|
| Pre-submission | Yes, encouraged | The journal "strongly encourages" publishing the submitted manuscript on a preprint server such as arXiv, bioRxiv, MetaArXiv or SocArXiv |
| Under review | Yes, encouraged | The recommendation is to preprint each version, including revised versions submitted to the journal |
| Post-acceptance (AAM) | Yes, encouraged | The accepted version should also be preprinted |
| Version of Record | Yes | Articles are published under CC BY (see Open Access) |

### Open Access

| Aspect | Detail |
|--------|--------|
| **Model** | Fully open access; all authors must agree to a Creative Commons Attribution (CC BY) licence (guidelines copy 2026-07-30) |
| **APC (if OA chosen)** | No submission fee; an article processing charge applies only to accepted articles (guidelines copy). The MIT Press open-access page says APCs for articles and reviews are "$750 for members of the International Society for Scientometrics and Informetrics (ISSI) and $1200 for non-members"; a waiver programme funded by the Eugene Garfield Foundation exists (open-access page, Wayback copy 2026-11-15, https://web.archive.org/web/20261115144725id_/https://direct.mit.edu/journals/pages/open-access). The local spine, an OpenAlex snapshot, lists 800 USD, which matches neither figure and is treated as a stale spine value |
| **Gold OA offered?** | Yes, the only route |
| **Read & Publish agreements** | Blank. Not read |

---

## Format

> Source for the rules below: the journal's submission guidelines, Wayback copy dated 2026-07-30 (https://web.archive.org/web/20260730174826id_/https://direct.mit.edu/qss/pages/submission-guidelines). Rules may have changed since; the live page returns 403 to curl.

| Aspect | Detail |
|--------|--------|
| **Article types accepted** | Articles (original theoretical, empirical or methodological research, typically 5,000 to 8,000 words); Reviews (novel synthesis of a research area, typically 5,000 to 10,000 words); Letters (responses to published research or events, up to about 1,000 words, at editorial discretion); Book reviews (typically 1,000 to 2,000 words) |
| **Word limit** | "Typically" ranges as above, not hard limits; the page does not say whether references count |
| **Word limit negotiability** | Blank. The ranges are labelled "typically"; no statement on exceptions |
| **Abstract limit** | 200 words at first submission; up to six keywords |
| **Reference limit** | No cap found. First submission: any consistent author-year style, no numbered references; at revision, APA style |
| **Supplementary material** | Any suitable file type, up to 100 MB; data essential to the key findings must be in a public repository with a persistent identifier such as a DOI ("data available on request is not acceptable"), with a data availability statement; exceptions for legal or ethical limits, such as proprietary scientometric databases |
| **Figure/Table limits** | No count limit found. At revision: figures as EPS, JPG or TIFF files, each at most 10 MB, 300 dpi desirable, at most 7 by 10 inches; tables inline, no colour |
| **Style / submission format** | Submission through the journal's "submission site" (linked as https://mc.manuscriptcentral.com/qss on the guidelines copy); single Word or PDF file at first submission, page and section numbering, line numbers suggested; cover letter preferably under 300 words on significance and scope fit; CRediT author contributions required for research and review articles; ORCIDs strongly encouraged; revision in Word or LaTeX, APA style, methods early in the manuscript, American or British English used consistently |

---

## Subject Density

> Based on Crossref records (not OpenAlex), 2021-11-23 to 2026-11-23.

### Top Topics (last 5 years)

> Not tabulated: no OpenAlex topic data was fetched.

| Topic | Article Count |
|-------|--------------|
| Not tabulated (OpenAlex not called) | — |

### Orientation

> Counts are word-boundary regex matches (case-insensitive) over the abstract of Crossref journal-article records dated 2021-11-23 to 2026-11-23: 312 records, 300 with an abstract (96.2%), so counts are lower bounds. Denominator for shares: 300. Regexes are listed as Q1 to Q18 in AI-Research Notes. Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Empirical vs. Theoretical** | Empirical and data-driven: statistical, regression or survey wording 83 (27.7%, Q1); bibliometric or citation wording 162 (54.0%, Q9; the regex includes the generic word "citation"); "theoretical, conceptual, theorize" 19 (6.3%, Q5). The guidelines name original "theoretical, empirical, or methodological research" as articles (guidelines copy 2026-07-30) |
| **Quantitative vs. Qualitative** | Quantitative wording 83 (27.7%) against qualitative 14 (4.7%, Q3); computational wording 26 (8.7%, Q8); experiments 21 (7.0%, Q2); mixed methods 2 (0.7%, Q7) |
| **Cross-disciplinary openness** | Scholarly communication, publishing and open-science wording is frequent: open science, reproducibility, replication, preprint or open access 48 (16.0%, Q17); gender wording 35 (11.7%, Q13); inequality wording 20 (6.7%, Q16). The guidelines say data from proprietary scientometric databases are typical (guidelines copy) |

---

## Soft Metadata

> [!NOTE]
> **AI-Researched (2026-11-23)** — the fields below were researched per-journal from public sources (Crossref counts, a Wayback copy of the publisher's guidelines, SciRev) rather than adapted from a family-level template. Every populated field cites its source or a stated count; fields with no public evidence were left blank with the reason recorded — see "AI-Research Notes" at the end of this section. This entry's overall `signal_quality` is **2/5**. This is a *different* evidence basis than "Sourced" (deeper per-journal research, every claim cites a source) or "Estimated" (family-level estimate) — see [SEED_DATA_QUALITY.md](../../../../../SEED_DATA_QUALITY.md).

### Epistemological & Political Leanings

> Evidence layers: Crossref records 2021-11-23 to 2026-11-23 (312 records, 300 with an abstract, regexes in AI-Research Notes); the Wayback copy of the guidelines. Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Cross-cultural friendliness** | Author countries were not counted (no country field in Crossref; OpenAlex not called). A most-cited record addresses geographic and language coverage of scholarly publishing (https://doi.org/10.1162/qss_a_00228) |
| **Editorial-board geography** | 38 board members in 13 countries: USA 10, Netherlands 5, Belgium 4, Canada 4, Italy 3, Denmark 3, Germany 2, China 2, and one each in Sweden, Taiwan, Brazil, the UK and the Republic of Korea (sums to 38; Ismael Rafols prints two affiliations, Leiden and Sussex, and is counted once under the Netherlands). Editor-in-Chief in Canada and Associate Editors in the Netherlands, China and Bristol (editorial information page, Wayback copy 2026-03-10, https://web.archive.org/web/20260310170354id_/https://direct.mit.edu/qss/pages/editorial-info) |
| **Non-Western epistemology openness** | Indigenous, decolonial or colonial wording in 1 of 300 abstracts (0.3%, Q12); a 88-citation record is titled around "a vast decolonization process" in scholarly publishing (https://doi.org/10.1162/qss_a_00228). No editorial statement read |
| **Diversity topic receptiveness** | Gender wording 35 (11.7%, Q13); race wording 1 (0.3%, Q11); migration wording 1 (0.3%, Q14). No editorial statement on these topics read |
| **Dominant theoretical tradition** | Quantitative science-of-science and bibliometrics. Most-cited 2021-2026 Crossref records (citations as of 2026-11-23): "The strain on scientific publishing" (324; https://doi.org/10.1162/qss_a_00327), "Scopus 1900-2020: Growth in articles, abstracts, countries, fields, and journals" (208; https://doi.org/10.1162/qss_a_00177), "The oligopoly's shift to open access: How the big five academic publishers profit from article processing charges" (129; https://doi.org/10.1162/qss_a_00272), "Overton: A bibliometric database of policy document citations" (103; https://doi.org/10.1162/qss_a_00204). The journal states no political position on any page read |

### Framing Requirements

- **Mandatory framing?** Yes, as a scope check: the first submission needs a cover letter, preferably under 300 words, commenting on significance and fit with the journal's scope; the Editor-in-Chief or an Associate Editor first judges suitability and may reject without review (https://web.archive.org/web/20260730174826id_/https://direct.mit.edu/qss/pages/submission-guidelines, copy 2026-07-30). The scope statement itself was not readable.
- **What kind of engagement?** Original theoretical, empirical or methodological research (Articles), novel syntheses (Reviews), short responses (Letters) and book reviews (guidelines copy). Public datasets must be cited with persistent identifiers where possible.
- **Article type and length**: Articles typically 5,000 to 8,000 words (see Format).
- **Special-issue framing seen**: none seen on the pages read.
- **Consequences of ignoring it**: contributions "deemed unsuitable" can be rejected without review (guidelines copy). No rejection-reason data (SciRev empty, https://scirev.org/journal/quantitative-science-studies/).

### Methodological Preferences

> Counts: regex matches over the abstract of Crossref records dated 2021-11-23 to 2026-11-23; 300 of 312 records have an abstract; shares use 300. Scoring convention of this research pass (its own, not an external standard): share 0 = 0; under 1% = 1; 1-5% = 2; over 5% = 3; 4-5 only with a cited editorial statement or a clearly dominant count. Scores measure how often a method appears in abstracts, not how a reviewer would judge it. Regexes Q1 to Q9 are in AI-Research Notes.

| Method | Receptiveness (0-5) | Evidence |
|--------|---------------------|----------|
| Quantitative experimental | 3 | Statistical, regression or survey wording 83 (27.7%, Q1); experiment wording 21 (7.0%, Q2) |
| Qualitative interviews | 2 | Interview, focus-group or "qualitative" wording 14 (4.7%, Q3) |
| Autoethnography | 0 | 0 of 300 (Q4). The row does not fit the field |
| Theoretical / Conceptual | 3 | 19 (6.3%, Q5); the guidelines list theoretical research as an article type (guidelines copy) |
| Mixed methods | 1 | 2 of 300 (0.7%, Q7) |
| Meta-analysis | 2 | Meta-analysis, systematic or literature review wording 8 (2.7%, Q6); Reviews of 5,000 to 10,000 words are a named article type (guidelines copy) |
| Bibliometric and citation analysis (added row) | 3 | 162 (54.0%, Q9), clearly dominant; the regex includes the generic word "citation", so it over-counts; 55 record titles carry a matching word (17.6% of 312 records) |
| Computational methods (added row) | 3 | 26 (8.7%, Q8) |

### Voice & Style

| Aspect | Detail |
|--------|--------|
| **First-person voice acceptance (0-5)** | Not scored. Abstract-only: 242 of 300 abstracts (80.7%) contain I, we, our or my (case-sensitive regex Q18); title plus abstract also 242. Among the 20 most recent abstracts (dated up to 2026-11-20) 18 do (Crossref, retrieved 2026-11-23). No guideline statement on first person was in the copy read |
| **Expected density** | Articles typically 5,000 to 8,000 words; Reviews 5,000 to 10,000 (guidelines copy 2026-07-30) |
| **Abstract and keywords** | Abstract limited to 200 words, up to six keywords (guidelines copy) |
| **Writing style notes** | First submission: consistent author-year references, no numbered references, numbered sections and line numbers suggested; at revision: APA style, methods discussed early, acknowledgments, author contributions, competing interests, funding, data availability statements and appendices at the end (guidelines copy) |
| **Authorship pattern** | Crossref author counts of 312 records: 1 author 55, 2 authors 86, 3 authors 68, 4 or more 102, no author list 1 (55+86+68+102+1 = 312; https://api.crossref.org/works?filter=issn:2641-3337, retrieved 2026-11-23) |

### Reviewer Pool Characteristics

Reviewer behaviour itself is not observable from public pages; what follows is what public pages do show.

| Aspect | Detail | Evidence |
|--------|--------|----------|
| **Dominant tradition** | Scientometrics and informetrics: the journal is the ISSI's official journal; the most repeated board affiliations are Indiana University Bloomington (3 entries), Leiden University (4 entries, one shared with Sussex), KU Leuven (2) and Georgia Institute of Technology (2) | https://web.archive.org/web/20260310170354id_/https://direct.mit.edu/qss/pages/editorial-info |
| **Reviewer list size** | Two or three external reviewers per reviewed Article or Review, chosen by the editors; no public list | https://web.archive.org/web/20260730174826id_/https://direct.mit.edu/qss/pages/submission-guidelines |
| **Review model** | Single-anonymised (STM taxonomy label printed in the guidelines); reviewer identities disclosed only if the reviewer opts in; reports published after acceptance | https://web.archive.org/web/20260730174826id_/https://direct.mit.edu/qss/pages/submission-guidelines |
| **Reviewer competence variance** | Blank. SciRev has no entries (all fields "n/a") | https://scirev.org/journal/quantitative-science-studies/ |
| **Quantitative mindset bias on qualitative work?** | Blank. No source on reviewer attitudes; qualitative wording appears in 14 of 300 abstracts (Q3) and bibliometric wording in 162 (Q9), so quantitative work is the norm here, which cannot tell how reviewers treat qualitative work | Crossref counts, see Methodological Preferences |
| **Discourse community signals (editorial board)** | Editor-in-Chief appointed by the ISSI Board, normally for three years; Associate Editors and the board are convened at the Editor-in-Chief's discretion with the ISSI Board's consultation (editorial information page copy). Board country mix is under Editorial-board geography | https://web.archive.org/web/20260310170354id_/https://direct.mit.edu/qss/pages/editorial-info |

### Sensitive Topics

> Counts are regex matches (labels in AI-Research Notes) over the abstract of 300 Crossref records, 2021-11-23 to 2026-11-23; lower bounds. "Receptiveness" gives frequency; "High" is used only where the journal states a position or runs a section, and none did.

| Topic Category | Receptiveness | Evidence |
|----------------|---------------|----------|
| Open science, reproducibility and open access | Regularly published | 48 of 300 (16.0%, Q17); preprinting is "strongly" encouraged and shared data are required (guidelines copy) |
| Gender and sexuality | Regularly published | 35 (11.7%, Q13) |
| AI and large language models | Regularly published | 21 (7.0%, Q10) and 14 record titles |
| Inequality and class | Present | 20 (6.7%, Q16) |
| Climate and environment | Rare | 4 (1.3%, Q15) |
| Politics and democracy | Rare | 4 (1.3%, Q19) |
| War, violence and conflict | Rare | 2 (0.7%, Q20) |
| Race, indigenous and migration topics | Rare | race 1, indigenous or decolonial 1, migration 1 (each 0.3%; Q11, Q12, Q14) |

### Practical Concerns

| Concern | Detail |
|---------|--------|
| **IRB requirement strictness** | No ethics-approval wording in the copy read, which mentions legal or ethical limits only for data sharing (guidelines copy 2026-07-30, https://web.archive.org/web/20260730174826id_/https://direct.mit.edu/qss/pages/submission-guidelines) |
| **Single-author acceptance** | Single-author records are 55 of 312 (17.6%) (Crossref, https://api.crossref.org/works?filter=issn:2641-3337, retrieved 2026-11-23) |
| **Independent scholar friendliness** | Blank. No rule found; authors give names, affiliations and funding information at submission (guidelines copy) |
| **Data transparency requirement** | Required: all data essential to the key findings in a public repository with a persistent identifier; a data availability statement; code strongly recommended (guidelines copy) |
| **OPSEC compatibility** | Not blind to reviewers: author names are disclosed to reviewers and the first page carries names and affiliations; preprints are encouraged (guidelines copy) |
| **AI use** | A publisher policy exists; its text was unread (see AI Policy) |
| **Open access and cost** | No submission fee; an APC for accepted articles, $750 for ISSI members and $1200 for non-members, with a waiver programme (open-access page copy 2026-11-15, https://web.archive.org/web/20261115144725id_/https://direct.mit.edu/journals/pages/open-access); CC BY required (guidelines copy) |
| **Funding and permissions** | Competing interests declared for all authors; funding information collected; all authors approve the manuscript; reprinted figures or text must be compatible with CC BY (guidelines copy) |
| **Prior and parallel publication** | Original work with no significant overlap with manuscripts under consideration or in press elsewhere; related submissions must be reported to the editor (guidelines copy) |

### AI-Research Notes (sources, blanks, and cross-language checks)

**signal_quality (0-5)**: overall 2. Per layer: Crossref counts 4 (96.2% abstract coverage; no country data); journal policies and guidelines 3 (one page, one dated Wayback copy; no AI section in it); editorial board 3 (editorial-information page read via a 2026-03-10 Wayback copy; may be out of date); open access and fees 3 (MIT open-access page, 2026-11-15 copy); experiential layer 0 (SciRev empty).

**Sources cited across this entry:**
- Wayback copies (curl, `id_` route): https://direct.mit.edu/qss/pages/submission-guidelines (2026-07-30); https://web.archive.org/web/20260310170354id_/https://direct.mit.edu/qss/pages/editorial-info (2026-03-10); https://web.archive.org/web/20261115144725id_/https://direct.mit.edu/journals/pages/open-access (2026-11-15); https://web.archive.org/web/20261115102008id_/https://direct.mit.edu/journals/pages/release-schedule (2026-11-15); https://web.archive.org/web/20261115113327id_/https://direct.mit.edu/journals/pages/authors (2026-11-15)
- https://api.crossref.org/journals/2641-3337 and Crossref works for the window (312 records, 300 with an abstract)
- Local spine (OpenAlex snapshot 2026-07-13) via `query_spine.py`; https://scirev.org/journal/quantitative-science-studies/

**Method notes:** Python `re` IGNORECASE except Q18, over the abstract (title only where stated); regex hits count records. Broad patterns over-count: Q9 matches "citation(s)", Q10 matches "AI" in any case, Q16 matches "class".

**Keyword regexes (exact):**
- Q1 `\b(regression|statistical(ly)?|quantitative|surveys?|questionnaires?|panel data|econometric\w*|multilevel|propensity)\b` ; Q2 `\b(experiments?|experimental|randomi[sz]ed|quasi-experimental)\b` ; Q3 `\b(interviews?|focus groups?|thematic analysis|grounded theory|qualitative)\b` ; Q4 `\bautoethnograph\w*\b`
- Q5 `\b(theoretical(ly)?|conceptual(ly)?|theori[sz]\w*)\b` ; Q6 `\b(meta-analys[ei]s|systematic review|literature review|scoping review|research synthesis)\b` ; Q7 `\bmixed[- ]methods?\b` ; Q8 `\b(machine learning|computational|topic model\w*|network analysis|natural language processing|deep learning|text mining)\b` ; Q9 `\b(bibliometric\w*|scientometric\w*|citation analysis|citations?|altmetric\w*|h-index|co-citation)\b`
- Q10 `\b(artificial intelligence|generative AI|ChatGPT|large language models?|LLMs?|AI)\b` ; Q11 `\b(raci(al|alized|alised|ist|sm)|racio\w*|whiteness|anti-?racis\w*)\b` ; Q12 `\b(indigenous|decoloni\w*|postcolonial|colonial\w*)\b` ; Q13 `\b(gender(ed)?|queer|LGBT\w*|transgender|non-?binary|sexuality|feminis\w*)\b` ; Q14 `\b(migrants?|refugees?|immigrants?|immigration|asylum|migration)\b`
- Q15 `\b(climate|environmental|ecolog\w*)\b` ; Q16 `\b(inequalit\w*|social justice|precarity|racism|class)\b` ; Q17 `\b(open science|reproducib\w*|replicat\w*|preprints?|open access)\b` ; Q18 (case-sensitive) `\b(I|[Ww]e|[Oo]ur|[Mm]y)\b` ; Q19 `\b(populis\w*|authoritarian\w*|polari[sz]ation|election\w*|democra\w*)\b` ; Q20 `\b(war|genocide|Gaza|Ukraine|Palestin\w*|violence)\b`

**Unreadable pages (never filled from memory):**
- Needs real-browser read: https://direct.mit.edu/journals/pages/ai_guidelines (the MIT Press generative-AI policy named on the authors page; live 403, no archived copy)
- Needs real-browser read: the journal's scope statement on https://direct.mit.edu/qss (not read)
- The live direct.mit.edu pages return 403 to curl; the Wayback copies cited above can be out of date. Wayback fetches returned HTTP 429 now and then; retries succeeded.

**Fields deliberately left blank, and why:** abbreviation, print ISSN, OpenAlex ID, acceptance and desk rejection rates, time to acceptance and publication, transfer policy, journal-level AI policy text (publisher policy unread), reviewer list. The spine's 800 USD APC is not used (stale).

**Cross-language and forum checks performed:**
- SciRev: journal page exists, no review data (all fields "n/a").
- One English web search naming this journal with "reddit", "review time" and "desk reject" returned no thread about it (2026-11-23). Chinese-language sources and LetPub were not searched for this journal in this pass (time box); that is not a "0 results" finding.

---

## Strategic Notes

> Each statement follows from a fact recorded above and names it. Where evidence is missing the field says so.

### Hard Blockers

- **Open data**: data essential to the key findings must sit in a public repository with a persistent identifier unless legal or ethical limits apply (Format; Practical Concerns).
- **CC BY licence**: all authors must agree to it, including for reprinted material (Open Access; Practical Concerns).
- **Scope check**: papers unsuitable for the journal can be rejected without review (Framing Requirements).
- **APC for accepted articles**: $750 for ISSI members, $1200 for non-members (Open Access).

### Soft Tax

- **Not blind to reviewers**: author names are disclosed to reviewers (Peer Review).
- **Reports become public** after acceptance via Web of Science (Peer Review).
- **Revision formatting**: APA style, CRediT contributions, and Word or LaTeX files are required at the revision stage (Format).
- **Time**: a five-week review target with delays expected; no measured data (Review Cycle Time).

### Best Suited For

- Quantitative studies of science, publishing and scholarly communication that share data: bibliometric wording in 162 of 300 abstracts, statistical wording in 83 (Orientation; Methodological Preferences).
- Authors who want to preprint every version, which the journal strongly encourages (Preprint Policy).

### Not Recommended For

- Qualitative or ethnographic work: qualitative wording in 14 of 300 abstracts, autoethnography 0 (Methodological Preferences).
- Authors who need blind review or whose data cannot be shared at all (Peer Review; Practical Concerns).
- Authors who need the text of the publisher's AI policy before choosing: it was not read (AI Policy).

### Rejection Fallback Chain

> No source states where rejected authors usually go. The rows below are topical neighbours that already exist in this corpus, listed only because they share subject area; they are not claims about acceptance odds.

| Rank | Journal | Why this fallback works |
|------|---------|------------------------|
| 1 | [Journal of the Association for Information Science and Technology](journal-of-the-association-for-information-science-and-technology.md) | Topical neighbour in information science and scientometrics; no fit evidence collected here |
| 2 | [Journal of Documentation](journal-of-documentation.md) | Topical neighbour in LIS; no fit evidence collected here |
| 3 | | |

---

## Changelog

| Date | Change | By |
|------|--------|----|
| 2026-11-23 | Initial entry (spine and Crossref scaffold) | AI-assisted (maintainer-directed) |
| 2026-11-23 | AI deep research pass; no first-hand human reports | AI-assisted (maintainer-directed) |
| 2026-11-24 | Corrections after independent verification (society, editorial board and country counts, APC amounts, schedule, AI-policy pointer, submission-site wording) | @Zaious |
