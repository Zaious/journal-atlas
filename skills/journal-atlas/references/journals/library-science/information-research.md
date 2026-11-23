<!-- schema: v1.3 -->
<!-- AI-researched entry — Journal Atlas v2 coverage pipeline. See docs/ATLAS_V2_DESIGN.md for methodology. -->
<!-- Written by an AI deep research pass (maintainer-directed) on 2026-11-23; scaffold built from the local spine snapshot and Crossref because the OpenAlex scaffold was not used. -->

# Information Research

> **Last verified**: 2026-11-23
> **Maintainer**: @Zaious
> **Venue type**: Journal
> **Evidence basis**: Sourced under the written rule (SEED_DATA_QUALITY.md): deeper per-journal research by an AI model, directed by the maintainer, 2026-11-23; overall signal_quality **2/5**. Claims cite source URLs or counts; blanks are recorded with reasons. Independent spot-check on 2026-11-23: 6 of 6 sampled pairs supported; pages wrongly recorded as unreadable were read from archive copies and used afterwards. No first-hand human reports; not human-verified.

---

## Identity

| Field | Value |
|-------|-------|
| **Abbreviation** | Blank. No short title read on the pages fetched or in Crossref (https://api.crossref.org/journals/1368-1613; retrieved 2026-11-23). DOIs use the prefix 10.47989 |
| **Venue type** | Journal |
| **Publisher** | University of Borås (Swedish School of Library and Information Science), hosted by the National Library of Sweden on the Publicera platform (about page, Wayback copy 2026-05-19, https://web.archive.org/web/20260519125033id_/https://publicera.kb.se/ir/about). Crossref's publisher string is the journal's own name (https://api.crossref.org/journals/1368-1613, retrieved 2026-11-23), so the Crossref string was not used |
| **ISSN (Print)** | Blank. Crossref lists only an electronic ISSN (https://api.crossref.org/journals/1368-1613, retrieved 2026-11-23) |
| **ISSN (Online)** | 1368-1613 (footer of the about page copy, URL above) |
| **Founded** | 1995, "established in 1995 by Professor T.D. Wilson" (about page copy, URL above) |
| **URL** | https://publicera.kb.se/ir/ (current site; the older site https://informationr.net/ir/ still answers HTTP 200 and says the journal "has moved its publication", retrieved 2026-11-23) |
| **Author Guidelines** | https://web.archive.org/web/20260519125033id_/https://publicera.kb.se/ir/instructions (Wayback copy 2026-05-19) and https://web.archive.org/web/20260523200558id_/https://publicera.kb.se/ir/about/submissions (Wayback copy 2026-05-23). The live pages return the Anubis challenge to curl (2026-11-23) |
| **Society / Association** | None found: owned by the university's school, not a society (about page copy, URL above) |
| **Editorial Board Location** | Journal run from Sweden (spine country code SE). The editorial team page (Wayback copy 2026-05-19, https://web.archive.org/web/20260519125033id_/https://publicera.kb.se/ir/about/editorialTeam) lists an Editor-in-Chief at University College Dublin, Ireland, 10 regional and area editors, and 49 "Editorial Board" entries; the board is counted by country under Reviewer Pool Characteristics |
| **OpenAlex ID** | Not looked up (OpenAlex not called in this pass) |

---

## Metrics

> Source: local spine, an OpenAlex snapshot dated 2026-07-13, read with `query_spine.py --issn 1368-1613` on 2026-11-23. JCR impact factor and quartile are paywalled and not stated. The 2-year mean citedness is an OpenAlex proxy, not a JCR figure.

| Metric | Value | Date |
|--------|-------|------|
| **Impact Factor** | Not stated (JCR is paywalled) | |
| **5-Year IF** | Not stated (JCR is paywalled) | |
| **h-index** | 13 (OpenAlex snapshot via spine, all years) | 2026-07-13 |
| **CiteScore** | Blank. Not read | |
| **Acceptance Rate** | Blank. SciRev's journal page has the editor-supplied field empty ("n/a", https://scirev.org/journal/information-research/, retrieved 2026-11-23); no figure on the pages read | 2026-11-23 |
| **Desk Rejection Rate** | Blank. The about page says every manuscript is first assessed by an editor who decides whether it goes to review, but gives no rate (Wayback copy 2026-05-19) | 2026-11-23 |
| **Quartile (by field)** | Not stated. Spine fields from the Norwegian register and the Finnish JUFO classification (snapshot 2026-07-13): Norwegian level 1, JUFO level 2 | 2026-07-13 |
| **2-yr Mean Citedness (OpenAlex IF proxy)** | 0.69 (OpenAlex proxy via spine, not JCR) | 2026-07-13 |
| **Total Works** | 764 (OpenAlex snapshot via spine, all years); cited-by count 1470 | 2026-07-13 |

### Review Cycle Time

| Stage | Typical Time | Notes |
|-------|-------------|-------|
| **Time to first decision** | The about page says the review process "is expected to take 6 to 8 weeks but may vary depending on reviewer availability" (Wayback copy 2026-05-19, https://web.archive.org/web/20260519125033id_/https://publicera.kb.se/ir/about) | Journal statement of expectation, not a measured figure. SciRev has no review data for the journal: duration fields "n/a", popularity score 14.3 (https://scirev.org/journal/information-research/, retrieved 2026-11-23) |
| **Time to first review** | Blank. No separate figure | |
| **Time to acceptance (total)** | Blank. No source | |
| **Time to publication (after acceptance)** | Blank. No source | |

### Publication Frequency

| Aspect | Detail |
|--------|--------|
| **Schedule** | The older site's issue list shows four numbers per volume for volumes 1 to 27 (2022), e.g. Vol. 26 (2021) No 1 to No 4, plus a special issue in vol. 27 (https://informationr.net/ir/, retrieved 2026-11-23). The author instructions say the journal "publishes three regular issues every year", alongside special issues and conference proceedings (https://web.archive.org/web/20260519125033id_/https://publicera.kb.se/ir/instructions) |
| **Articles per year (approx.)** | Crossref DOI counts by issued year: 2021 = 34, 2022 = 131, 2023 = 48, 2024 = 77, 2025 = 212, 2026 = 236 to 2026-11-23 (https://api.crossref.org/journals/1368-1613). The spikes in 2022, 2025 and 2026 probably include conference-proceedings supplements: the most-cited records carry DOI segments such as "iconf" and "colis" (e.g. https://doi.org/10.47989/ir30iconf47143, https://doi.org/10.47989/colis2206); this is an inference from DOI patterns, not a journal statement. Crossref returns 726 journal-article records for 2021-11-23 to 2026-11-23, 718 with an abstract |
| **Special issues?** | A special issue appears in vol. 27 (https://informationr.net/ir/, retrieved 2026-11-23). No current CFP read |

---

## Policies

### Peer Review

| Aspect | Detail |
|--------|--------|
| **Type** | Double-blind: "authors and reviewers are anonymous throughout the review process"; an editor first decides whether a manuscript goes to review, then two or more experts review it; the editor recommends accept, revise or reject. Original articles are externally reviewed; invited and other content is reviewed internally; book reviews are approved by the editors without external review (about page, Wayback copy 2026-05-19) |
| **Transferable / Cascade?** | Blank. No source read |
| **Reviewer reports published?** | Blank. Not stated on the pages read |
| **Typical R+R rounds** | Blank. No source (SciRev empty) |
| **Reviewer recommendations** | Policies page (Wayback copy 2026-04-09, https://web.archive.org/web/20260409105939id_/https://publicera.kb.se/ir/policies): reviewers should accept only manuscripts within their subject area, declare conflicts of interest, respond to invitations without delay, and give constructive feedback with concrete examples |

### AI Policy

| Aspect | Detail |
|--------|--------|
| **Has journal-specific AI policy?** | Yes: a section "Policy on the use of AI tools" (policies page, Wayback copy 2026-04-09, URL above) |
| **Explicit permission gate?** | No gate. Disclosure is required instead: authors "are required to disclose" generative-AI use in written content, images, or data collection and analysis, naming the tool(s) and version(s); AI used only to correct spelling or grammar need not be credited |
| **Leniency (1-5)** | 4 (this pass's judgement: use is allowed with disclosure; no ban and no pre-approval) |
| **Summary** | AI tools cannot be credited with authorship, citing the COPE position statement; authors are fully responsible for AI-assisted content and for crediting quoted material (same page copy) |
| **Source URL** | https://web.archive.org/web/20260409105939id_/https://publicera.kb.se/ir/policies |

### Preprint Policy

> Source: policies page, Wayback copy 2026-04-09 (https://web.archive.org/web/20260409105939id_/https://publicera.kb.se/ir/policies) and about page, Wayback copy 2026-05-19. Policies may have changed since.

| Stage | Allowed? | Notes |
|-------|----------|-------|
| Pre-submission | Yes | The journal accepts manuscripts previously posted as preliminary versions, on personal websites, or presented at conferences, provided authors hold the copyright (about page copy) |
| Under review | Yes, with a caveat | Editors "cannot guarantee full anonymity" when earlier versions are public (policies page copy) |
| Post-acceptance (AAM) | Yes | Authors may self-archive the submitted and the published version without embargo (policies page copy). Authors are expected to cross-link the versions with DOI links if the article is published |
| Version of Record | Yes | Same self-archiving statement; articles are open access (see below) |

### Open Access

| Aspect | Detail |
|--------|--------|
| **Model** | Fully open access with immediate access; authors keep copyright; CC BY-NC 4.0 from volume 30, CC BY-NC-ND for volumes 1 to 29 (open-access page, Wayback copy 2026-05-19, https://web.archive.org/web/20260519125033id_/https://publicera.kb.se/ir/openaccess) |
| **APC (if OA chosen)** | None: "does not charge author or publication fees" (same page copy) |
| **Gold OA offered?** | Yes, the only route |
| **Read & Publish agreements** | Not applicable (no charge) |

---

## Format

> Sources: about page (Wayback copy 2026-05-19), author instructions (https://web.archive.org/web/20260519125033id_/https://publicera.kb.se/ir/instructions, Wayback copy 2026-05-19) and submission page (https://web.archive.org/web/20260523200558id_/https://publicera.kb.se/ir/about/submissions, Wayback copy 2026-05-23). The live pages return the Anubis challenge to curl, so the copies may be out of date.

| Aspect | Detail |
|--------|--------|
| **Article types accepted** | Original articles (external review), invited and other content (internal review), book reviews (editor-approved) (about page copy). The submission form's list of article types is not in the copies read |
| **Word limit** | No hard limit found. The instructions give a recommended length of "approximately 7,000 to 8,000 words", excluding abstract, references and appendices (instructions copy) |
| **Word limit negotiability** | Blank. The length is a recommendation; no statement on exceptions |
| **Abstract limit** | No word limit found. A "full, informative, structured abstract" is required, formatted as the Word template describes (instructions copy); the template itself was not read |
| **Reference limit** | No numeric limit found. APA 7th edition; a DOI for each reference where one exists; archived links for web references; no footnotes (instructions copy) |
| **Supplementary material** | Blank. The policies page encourages linking open research data under a special heading, following the FAIR principles, when funders require open data (policies page copy 2026-04-09) |
| **Figure/Table limits** | Tables and figures go in the text per the Word template; figures are also submitted as separate .jpg or .png files, maximum width 750px (instructions copy) |
| **Style / submission format** | APA 7th edition for citations and references; British English spelling; the provided Word template is required; submission through the journal's OJS site after registration (instructions copy; submission page https://web.archive.org/web/20260523200558id_/https://publicera.kb.se/ir/about/submissions). When authors fail to comply with the house rules, the contribution "will be rejected without review"; breaking the style guide may bring a revision request (instructions copy) |

---

## Subject Density

> Based on Crossref records (not OpenAlex), 2021-11-23 to 2026-11-23. OpenAlex topic counts were not pulled in this pass.

### Top Topics (last 5 years)

> Not tabulated: no OpenAlex topic data was fetched. Scope as the journal states it is listed in Orientation and Framing Requirements.

| Topic | Article Count |
|-------|--------------|
| Not tabulated (OpenAlex not called) | — |

### Orientation

> Counts are word-boundary regex matches (case-insensitive) over the abstract of Crossref journal-article records dated 2021-11-23 to 2026-11-23: 726 records, 718 with an abstract (98.9%), so counts are lower bounds on the abstract text. Denominator for shares: 718. Regexes are listed in AI-Research Notes. These records include conference-proceedings material (see Publication Frequency). Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Empirical vs. Theoretical** | Empirical wording leads: interview or qualitative terms 269 (37.5%, M3); survey, regression or statistical terms 188 (26.2%, M1); "theoretical, conceptual, theorize" 161 (22.4%, M4). The about page asks for work "oriented towards the human information seeker and user" rather than algorithms (Wayback copy 2026-05-19) |
| **Quantitative vs. Qualitative** | Qualitative 269 (37.5%) against quantitative 188 (26.2%); experiments 29 (4.0%, M2); mixed methods 21 (2.9%, M6); content analysis 66 (9.2%, M12) |
| **Cross-disciplinary openness** | The scope list names about a dozen areas, from knowledge organisation and archives to HCI, data science, health informatics and public libraries (about page copy). Bibliometric or citation wording 38 (5.3%, M9) and machine-learning or computational wording 44 (6.1%, M8) |

---

## Soft Metadata

### Epistemological & Political Leanings

> Evidence layers: Crossref records 2021-11-23 to 2026-11-23 (726 records, 718 with an abstract, regexes in AI-Research Notes); Wayback copies of the about and policies pages. Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Cross-cultural friendliness** | Author countries were not counted (Crossref has no country field; OpenAlex was not called). The journal describes itself as "international" and is run from Sweden (about page, Wayback copy 2026-05-19, https://web.archive.org/web/20260519125033id_/https://publicera.kb.se/ir/about) |
| **Editorial-board geography** | 49 board entries across 27 countries; USA 7, Sweden 6, UK 4, Japan 3, the rest 2 or fewer (country list under Reviewer Pool Characteristics; team page, Wayback copy 2026-05-19, https://web.archive.org/web/20260519125033id_/https://publicera.kb.se/ir/about/editorialTeam) |
| **Non-Western epistemology openness** | Indigenous, decolonial or colonial wording in 13 of 718 abstracts (1.8%, M14). No editorial statement read |
| **Diversity topic receptiveness** | Gender, queer or feminist wording 35 (4.9%, M15); race wording 3 (0.4%, M13); migration wording 12 (1.7%, M16). No editorial statement on these topics was found |
| **Dominant theoretical tradition** | No single school. The scope is organised by information discipline and centred on the human information seeker (about page copy). Most-cited 2021-2026 Crossref records (citations as of 2026-11-23): "Deskilling and upskilling with AI systems" (38; https://doi.org/10.47989/ir30iconf47143), "Who is using ChatGPT and why? Extending the Unified Theory of Acceptance and Use of Technology" (32; https://doi.org/10.47989/ir291647), "Bibliographic coupling: a main path analysis from 1963 to 2020" (28; https://doi.org/10.47989/irpaper918), "Mapping science: tools for bibliometric and altmetric studies" (15; https://doi.org/10.47989/irpaper909), "Data Cultures: a scoping literature review" (13; https://doi.org/10.47989/irpaper950). Two further records rank above the last two: "Promoting AI literacy through U.S. academic libraries: an analysis of LibGuides from ARL and Oberlin" (18; https://doi.org/10.47989/ir30iconf47182) and "Interrogating paradata" (15, tied with "Mapping science"; https://doi.org/10.47989/colis2206). The list is a selection of the most-cited records. The journal states no political position on any page read |

### Framing Requirements

- **Mandatory framing?** Yes, as a scope rule: submissions should be oriented towards "the human information seeker and user"; the journal says it is "not interested in the algorithms used in information systems" but in their impact on users or in how users' requirements are explored in design (about page, Wayback copy 2026-05-19, https://web.archive.org/web/20260519125033id_/https://publicera.kb.se/ir/about).
- **What kind of engagement?** The scope list covers business intelligence, scholarly communication and bibliometrics, cultural heritage, data science, disciplinary applications, HCI, human information behaviour, information literacy, information systems (AI, retrieval), knowledge organisation, and society and information including public libraries (about page copy). Intended readers: scholars, researchers and practitioners in library and information science (same page).
- **Article type and length**: original articles, invited content, book reviews are named (about page copy); length guidance is in Format (recommended 7,000 to 8,000 words).
- **Special-issue framing seen**: a special issue in volume 27 (https://informationr.net/ir/, retrieved 2026-11-23); conference-linked material appears in volumes 30 onwards by DOI pattern (see Publication Frequency). No current CFP read.
- **Consequences of ignoring it**: the about page says algorithm-centred work is outside the journal's interest (same page copy). No desk-rejection statistic or reason list was found (SciRev empty, https://scirev.org/journal/information-research/).

### Methodological Preferences

> Counts: regex matches over the abstract of Crossref records dated 2021-11-23 to 2026-11-23; 718 of 726 records have an abstract; shares use 718. Scoring convention of this research pass (its own, not an external standard): share 0 = 0; under 1% = 1; 1-5% = 2; over 5% = 3; 4-5 only with a cited editorial statement. Scores measure how often a method appears in abstracts, not how a reviewer would judge it. Regexes M1 to M16 are in AI-Research Notes.

| Method | Receptiveness (0-5) | Evidence |
|--------|---------------------|----------|
| Quantitative experimental | 3 | Survey, questionnaire, regression or statistical wording 188 (26.2%, M1); experiment wording 29 (4.0%, M2) |
| Qualitative interviews | 3 | Interview, focus-group, thematic, grounded-theory or "qualitative" wording 269 (37.5%, M3) |
| Autoethnography | 1 | 4 of 718 (0.6%, M5). The row fits the field marginally |
| Theoretical / Conceptual | 3 | 161 (22.4%, M4) |
| Mixed methods | 2 | 21 (2.9%, M6) |
| Meta-analysis | 3 | Meta-analysis, systematic, literature or scoping review wording 45 (6.3%, M7) |
| Content analysis (added row) | 3 | 66 (9.2%, M12) |
| Bibliometric and citation work (added row) | 3 | 38 (5.3%, M9); the regex includes the generic word "citation", so it over-counts bibliometrics |
| Computational methods (added row) | 3 | 44 (6.1%, M8) |

### Voice & Style

| Aspect | Detail |
|--------|--------|
| **First-person voice acceptance (0-5)** | Not scored. Abstract-only count: 252 of 718 abstracts (35.1%) contain I, we, our or my (case-sensitive regex M17); title plus abstract 264 (36.8%). The 20 most recent abstracts carry the same date (2026-10-15), 3 of 20 first-person, a conference-batch artefact (Crossref, retrieved 2026-11-23). The instructions say nothing on first person (instructions copy) |
| **Expected density** | Recommended 7,000 to 8,000 words (see Format); the instructions also ask authors to avoid jargon and obscure abbreviations for a wide audience (instructions copy) |
| **Abstract and keywords** | Structured abstract required (instructions copy, https://web.archive.org/web/20260519125033id_/https://publicera.kb.se/ir/instructions); the template's section list and any keyword rule were not read |
| **Writing style notes** | The instructions ask for no contractions, minimal ad hoc abbreviations, minimal capital letters (including in titles and headings), bias-free language with singular "they" endorsed, no footnotes, italics rather than quotation marks for emphasis, and single quotation marks for short quotations (instructions copy). The policies page asks authors to credit quoted and referenced material and to link earlier versions of a manuscript with DOIs (policies page copy 2026-04-09, https://web.archive.org/web/20260409105939id_/https://publicera.kb.se/ir/policies) |
| **Authorship pattern** | Crossref author counts of 726 records: 1 author 190, 2 authors 190, 3 authors 119, 4 or more 227 (https://api.crossref.org/works?filter=issn:1368-1613, retrieved 2026-11-23); records include conference material |

### Reviewer Pool Characteristics

Reviewer behaviour itself is not observable from public pages; what follows is what public pages do show.

| Aspect | Detail | Evidence |
|--------|--------|----------|
| **Dominant tradition** | Information science and LIS: the board entries are mostly professors in information-science, library and information studies and informatics departments, with a few in business schools, history of computing and communication (team page copy) | https://web.archive.org/web/20260519125033id_/https://publicera.kb.se/ir/about/editorialTeam |
| **Reviewer list size** | Blank. No public reviewer list found | — |
| **Review model** | Double-blind; two or more experts per reviewed manuscript (about page copy 2026-05-19) | https://web.archive.org/web/20260519125033id_/https://publicera.kb.se/ir/about |
| **Reviewer competence variance** | Blank. SciRev has no entries for the journal (all fields "n/a") | https://scirev.org/journal/information-research/ |
| **Quantitative mindset bias on qualitative work?** | Blank. No source on reviewer attitudes; qualitative wording appears in 269 of 718 abstracts (M3), so qualitative work is common, which cannot tell how reviewers treat it | Crossref counts, see Methodological Preferences |
| **Discourse community signals (editorial board)** | 49 "Editorial Board" entries, each with institution; by country: USA 7, Sweden 6, UK 4, Japan 3, Canada 2, South Africa 2, Denmark 2, Lithuania 2, Spain 2, Norway 2 (one entry prints no country, Oslo Metropolitan University, assigned to Norway by this pass), Mexico 1, and one each for Israel, Croatia, Germany, Greece, New Zealand, Poland, Australia, France, Malaysia, Belgium, Brazil, Finland, Slovakia, Slovenia, Estonia and China (sums to 49; 27 countries). The editors section adds an Editor-in-Chief (Ireland), an Associate Editor (Sweden) and ten editors, most named by region, including Australasia, India, Africa and North America (team page copy). Reviewer conduct rules read: accept only within subject area, declare conflicts, no abusive language, editors may discount abusive reviews (policies page copy 2026-04-09) | https://web.archive.org/web/20260519125033id_/https://publicera.kb.se/ir/about/editorialTeam; https://web.archive.org/web/20260409105939id_/https://publicera.kb.se/ir/policies |

### Sensitive Topics

> Counts are regex matches (labels in AI-Research Notes) over the abstract of 718 Crossref records, 2021-11-23 to 2026-11-23; lower bounds. "Receptiveness" gives frequency; "High" is used only where the journal states a position or runs a section, and none did.

| Topic Category | Receptiveness | Evidence |
|----------------|---------------|----------|
| AI and large language models | Regularly published | 156 of 718 (21.7%, M10) and 112 record titles; the journal has an AI-use policy (policies page copy 2026-04-09) but no statement on receptiveness; many records are conference-linked |
| Misinformation and propaganda | Present | 31 (4.3%, M18) |
| Surveillance and privacy | Present | 22 (3.1%, M19) |
| Gender, queer and feminist topics | Present | 35 (4.9%, M15) |
| Race and raciolinguistics | Rare | 3 (0.4%, M13) |
| Indigenous, decolonial and colonial topics | Present | 13 (1.8%, M14) |
| Migration | Present | 12 (1.7%, M16) |
| War, violence and conflict | Rare | 9 (1.3%, M20) |

### Practical Concerns

| Concern | Detail |
|---------|--------|
| **IRB requirement strictness** | The submission checklist asks authors to confirm that, "where applicable", an ethics committee reviewed the research and that the committee name and approval reference number are in the manuscript, and that identifiable people gave informed consent (https://web.archive.org/web/20260523200558id_/https://publicera.kb.se/ir/about/submissions); the instructions require compliance with a Policy for Ethical Oversight (instructions copy). The policies page cites COPE ethical guidance and handles misconduct by COPE recommendations (policies page copy 2026-04-09, https://web.archive.org/web/20260409105939id_/https://publicera.kb.se/ir/policies) |
| **Single-author acceptance** | Single-author records are 190 of 726 (26.2%), including conference material (Crossref, https://api.crossref.org/works?filter=issn:1368-1613, retrieved 2026-11-23) |
| **Independent scholar friendliness** | No affiliation rule found; the submission checklist asks for the submitting author's ORCID (submission page copy); authors register on the submission system (information-for-authors page, https://web.archive.org/web/20260409110328id_/https://publicera.kb.se/ir/information/authors). The checklist asks for an ORCID, not an affiliation |
| **Data transparency requirement** | Open data is encouraged under the FAIR principles where funders or universities require it; linked under a special heading in the manuscript (policies page copy 2026-04-09, URL above) |
| **OPSEC compatibility** | Double-blind review; earlier public versions are allowed but full anonymity cannot be guaranteed, and authors cross-link versions with DOIs if published (policies page copy 2026-04-09, URL above) |
| **AI use** | Disclosure required for generative AI in text, images or data work; AI cannot be an author (policies page copy 2026-04-09, URL above) |
| **Open access and cost** | No author or publication fees; CC BY-NC 4.0 from volume 30 (https://web.archive.org/web/20260519125033id_/https://publicera.kb.se/ir/openaccess) |
| **Funding and permissions** | Blank. Authorship criteria: significant contribution to design, data or analysis, writing or editing, and approval of the manuscript; others go in acknowledgments with written approval (policies page copy 2026-04-09). Authors affiliated with the editorial team are removed from handling their article (about page copy) |
| **Prior and parallel publication** | Duplicate or redundant publication is not permitted (about page copy 2026-05-19) |

### AI-Research Notes (sources, blanks, and cross-language checks)

**signal_quality (0-5)**: overall 2. Per layer: Crossref counts 4 (98.9% abstract coverage; no country data); journal policies 4 (about, policies, open-access, author-instructions and submission pages read via Wayback; captures may be out of date); editorial board 3 (team page read via Wayback, 2026-05-19; the Norway assignment for one entry is inferred); experiential layer 0 (SciRev empty).

**Sources cited across this entry:**
- Wayback copies (curl, `id_` route) of publicera.kb.se/ir pages: about (2026-05-19), openaccess (2026-05-19), instructions (2026-05-19), about/editorialTeam (2026-05-19), about/submissions (2026-05-23), policies (2026-04-09), information/authors (2026-04-09); live older site https://informationr.net/ir/
- https://api.crossref.org/journals/1368-1613 and Crossref works for the window (726 records, 718 with an abstract)
- Local spine (OpenAlex snapshot 2026-07-13) via `query_spine.py`; https://scirev.org/journal/information-research/

**Method notes:** Python `re` IGNORECASE except M17, over the abstract only (title not added except where "title+abstract" is stated); regex hits count records. Broad patterns over-count: M9 matches "citation(s)", M10 matches "AI" in any case, M4 matches all "theor-" forms. Conference-proceedings material is inside the window.

**Keyword regexes (exact):**
- M1 `\b(regression|statistical(ly)?|quantitative|surveys?|questionnaires?|panel data|econometric\w*|multilevel|propensity)\b` ; M2 `\b(experiments?|experimental|randomi[sz]ed|quasi-experimental)\b` ; M3 `\b(interviews?|focus groups?|thematic analysis|grounded theory|qualitative)\b`
- M4 `\b(theoretical(ly)?|conceptual(ly)?|theori[sz]\w*)\b` ; M5 `\bautoethnograph\w*\b` ; M6 `\bmixed[- ]methods?\b` ; M7 `\b(meta-analys[ei]s|systematic review|literature review|scoping review|research synthesis)\b`
- M8 `\b(machine learning|computational|topic model\w*|network analysis|natural language processing|deep learning|text mining)\b` ; M9 `\b(bibliometric\w*|scientometric\w*|citation analysis|citations?|altmetric\w*|h-index|co-citation)\b` ; M10 `\b(artificial intelligence|generative AI|ChatGPT|large language models?|LLMs?|AI)\b`
- M12 `\bcontent analysis\b` ; M13 `\b(raci(al|alized|alised|ist|sm)|racio\w*|whiteness|anti-?racis\w*)\b` ; M14 `\b(indigenous|decoloni\w*|postcolonial|colonial\w*)\b` ; M15 `\b(gender(ed)?|queer|LGBT\w*|transgender|non-?binary|sexuality|feminis\w*)\b` ; M16 `\b(migrants?|refugees?|immigrants?|immigration|asylum|migration)\b`
- M17 (case-sensitive) `\b(I|[Ww]e|[Oo]ur|[Mm]y)\b` ; M18 `\b(misinformation|disinformation|fake news|propaganda)\b` ; M19 `\b(surveillance|privacy)\b` ; M20 `\b(war|genocide|Gaza|Ukraine|Palestin\w*|violence)\b`

**Live-site access:** the live publicera.kb.se pages return an Anubis proof-of-work challenge to curl (checked 2026-11-23), and the Wayback captures of 2026-06-27 are challenge pages too. Everything above was read from the earlier captures cited, which can be out of date.

**Fields deliberately left blank, and why:** abbreviation, print ISSN, OpenAlex ID, acceptance and desk rejection rates, time to acceptance and publication, transfer policy, reports published, reviewer list, numeric abstract and reference limits, style-template details: no source read.

**Cross-language and forum checks performed:**
- SciRev: journal page exists, no review data (all fields "n/a"; https://scirev.org/journal/information-research/).
- Chinese-language sources (小木虫, 知乎, fabiaoji), LetPub and Reddit: not searched for this journal in this pass (time box). Not a "0 results" finding.

---

## Strategic Notes

> Each statement follows from a fact recorded above and names it. Where evidence is missing the field says so.

### Hard Blockers

- **User-centred scope**: algorithm-centred work is stated to be outside the journal's interest (Framing Requirements; about page copy 2026-05-19).
- **Disclosure**: generative-AI use in text, images or data work must be disclosed with tool and version (AI Policy).
- **Prior publication**: duplicate publication is not permitted (Practical Concerns).
- **House rules**: per the author instructions, a contribution that breaks them (English, Word template, structured abstract, anonymised file, no prior or parallel submission) "will be rejected without review"; the submission page adds that one outside the stylistic and bibliographic requirements "will be automatically declined" (Format).

### Soft Tax

- **Time**: the journal expects 6 to 8 weeks of review; no measured data exist (Review Cycle Time).
- **Cost**: none; no author or publication fee (Open Access).
- **Anonymity**: double-blind; earlier public versions are allowed but anonymity cannot be guaranteed (Preprint Policy).

### Best Suited For

- Studies of information users and behaviour, literacy, libraries, scholarly communication or knowledge organisation, qualitative or quantitative: qualitative wording in 269 of 718 abstracts and survey or statistical wording in 188 (Orientation; Methodological Preferences).
- Authors who want a no-fee open access route in LIS: the open-access page states no author or publication fees (Open Access).

### Not Recommended For

- Algorithm-centred papers without a user focus (Framing Requirements).
- Authors who need an acceptance rate or a measured review time before choosing: none was found (Metrics).

### Rejection Fallback Chain

> No source states where rejected authors usually go. The rows below are topical neighbours that already exist in this corpus, listed only because they share subject area; they are not claims about acceptance odds.

| Rank | Journal | Why this fallback works |
|------|---------|------------------------|
| 1 | [Journal of Documentation](journal-of-documentation.md) | Topical neighbour in LIS; no fit evidence collected here |
| 2 | [International Journal on Digital Libraries](international-journal-on-digital-libraries.md) | Topical neighbour (digital libraries); no fit evidence collected here |
| 3 | | |

---

## Changelog

| Date | Change | By |
|------|--------|----|
| 2026-11-23 | Initial entry (spine and Crossref scaffold) | AI-assisted (maintainer-directed) |
| 2026-11-23 | AI deep research pass; no first-hand human reports | AI-assisted (maintainer-directed) |
| 2026-11-24 | Corrections after independent verification (author instructions, submission page and editorial team read from Wayback copies; schedule; M4/M5 label; most-cited list; scope line) | @Zaious |
| 2026-11-23 | Promoted to Tier 1 under the written rule: tier1_gate passes; independent spot-check 6 of 6 sampled pairs supported; pages wrongly recorded as unreadable were read from archive copies and used afterwards; banner removed; no first-hand human reports | AI-assisted (maintainer-authorised, not human-verified) |
