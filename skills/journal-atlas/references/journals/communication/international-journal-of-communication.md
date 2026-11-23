<!-- schema: v1.3 -->
<!-- AI-researched entry — Journal Atlas v2 coverage pipeline. See docs/ATLAS_V2_DESIGN.md for methodology. -->
<!-- Written by an AI deep research pass (maintainer-directed) on 2026-11-23; scaffold built from the local spine snapshot and Crossref because the OpenAlex scaffold was not used. -->

# International Journal of Communication

> **Last verified**: 2026-11-23
> **Maintainer**: @Zaious
> **Venue type**: Journal
> **Evidence basis**: Tier 1 under the written rule (SEED_DATA_QUALITY.md): deeper per-journal research by an AI model, directed by the maintainer, 2026-11-23; overall signal_quality **3/5**. Claims cite source URLs or counts; blanks are recorded with reasons. Independent spot-check on 2026-11-23: 5 supported and 1 partial of 6 sampled pairs; a wrongly recorded 'no editorial board' was corrected from the live page afterwards. No first-hand human reports; not human-verified.

---

## Identity

| Field | Value |
|-------|-------|
| **Abbreviation** | IJoC, as used by the journal itself on its about page (https://ijoc.org/index.php/ijoc/about; retrieved 2026-11-23) |
| **Venue type** | Journal |
| **Publisher** | USC Annenberg Press, housed at the USC Annenberg School for Communication & Journalism (about page, URL above; Crossref publisher string "USC Annenberg Press", https://api.crossref.org/journals/1932-8036, retrieved 2026-11-23) |
| **ISSN (Print)** | Blank. Crossref lists only the electronic ISSN (https://api.crossref.org/journals/1932-8036) |
| **ISSN (Online)** | 1932-8036 (Crossref, same URL) |
| **Founded** | Blank. The about page says the Press has published open access journals "since 2007" but does not give a founding year for this journal; Crossref's earliest DOI year is 2023 because of the DOI change (https://api.crossref.org/journals/1932-8036) |
| **URL** | https://ijoc.org/index.php/ijoc/index |
| **Author Guidelines** | https://ijoc.org/index.php/ijoc/submission-guidelines (read live 2026-11-23); checklist at https://ijoc.org/index.php/ijoc/about/submissions |
| **Society / Association** | None found: a university press journal (about page). The page lists IAMCR among indexing sources, not as owner |
| **Editorial Board Location** | The editorial board page (https://ijoc.org/index.php/ijoc/about/editorial-board, HTTP 200, retrieved 2026-11-23) lists a Founding Editor (University of Southern California), a Founding Managing Editor (retired, no institution) and 136 board members, each with an institution but no country; countries were assigned by this pass from the institution names (see Editorial-board geography). The editorial team page names the Editor (Silvio Waisbord), two Managing Editors, a Webmaster and four Assistant Editors, 8 entries, without affiliations (https://ijoc.org/index.php/ijoc/about/editorialTeam) |
| **OpenAlex ID** | Not looked up (OpenAlex not called in this pass) |

---

## Metrics

> Source: local spine, an OpenAlex snapshot dated 2026-07-13 (`query_spine.py --issn 1932-8036`, 2026-11-23), and SciRev editor-supplied fields. JCR impact factor and quartile are paywalled and not stated, including the 2-year impact factor SciRev prints.

| Metric | Value | Date |
|--------|-------|------|
| **Impact Factor** | Not stated (JCR is paywalled) | |
| **5-Year IF** | Not stated (JCR is paywalled) | |
| **h-index** | 21 (OpenAlex snapshot via spine, all years) | 2026-07-13 |
| **CiteScore** | Blank. Not read | |
| **Acceptance Rate** | 13% as supplied by the editor to SciRev ("% accepted last year"; year not printed), with 866 manuscripts received and 362 articles published in that year (https://scirev.org/journal/international-journal-of-communication/, retrieved 2026-11-23). Editor-reported to a third party, not on the journal's own pages | 2026-11-23 |
| **Desk Rejection Rate** | Blank. SciRev "immediately rejected last year" is n/a; the journal says some papers are rejected without referee consultation (https://ijoc.org/index.php/ijoc/about/editorialPolicies) but gives no rate | 2026-11-23 |
| **Quartile (by field)** | Not stated. Spine fields (snapshot 2026-07-13): Norwegian level 1, JUFO level 2 | 2026-07-13 |
| **2-yr Mean Citedness (OpenAlex IF proxy)** | 0.085 (OpenAlex proxy via spine, not JCR). Treat as unreliable: the DOI prefix changed and nearly all Crossref-registered articles are from 2026 (see Publication Frequency) | 2026-07-13 |
| **Total Works** | 327 (OpenAlex snapshot via spine, all years); cited-by count 2092 | 2026-07-13 |

### Review Cycle Time

| Stage | Typical Time | Notes |
|-------|-------------|-------|
| **Time to first decision** | Journal statement: reviewers are "initially given five weeks to review", and "most articles go through at least two rounds" (https://ijoc.org/index.php/ijoc/about/editorialPolicies, retrieved 2026-11-23). SciRev, 3 reviews as printed on the page: first review round 2.5 months, 1.7 review rounds on average, 2.3 review reports (https://scirev.org/journal/international-journal-of-communication/) | Self-reported, small n |
| **Time to first review** | Five weeks given to reviewers (editorial policies page) | Instruction to reviewers, not a measured time |
| **Time to acceptance (total)** | SciRev, same 3 reviews: total handling time of accepted manuscripts 3.9 months. Authors have two months to complete requested revisions (editorial policies page) | n = 3, self-reported |
| **Time to publication (after acceptance)** | Accepted authors have "a full year" to submit final versions (editorial policies page); articles post to the current volume on the 15th and 30th of most months (about page). No measured time found | |

### Publication Frequency

| Aspect | Detail |
|--------|--------|
| **Schedule** | One online volume a year; articles post bi-monthly, by the 15th and 30th, except February and December; publishing stops on 30 November (https://ijoc.org/index.php/ijoc/about, retrieved 2026-11-23) |
| **Articles per year (approx.)** | SciRev (editor-supplied): 362 articles published in "last year" (year not printed). Crossref DOI counts by issued year are not usable: the journal endpoint's breakdown gives 2023 = 1 and 2026 = 197 (https://api.crossref.org/journals/1932-8036), while the works endpoint returns 233 records for 2026 and 234 for 2021-11-23 to 2026-11-23, 128 with an abstract (https://api.crossref.org/works?filter=issn:1932-8036, retrieved 2026-11-23). The two endpoints disagree (197 against 233); older articles are not registered under the new DOI prefix |
| **Special issues?** | Yes: Special Sections and Forums are guest-edited and the guest editors must subsidise production costs (https://ijoc.org/index.php/ijoc/submission-guidelines). Featured on the about page copy of 2026-11-23: a Special Section on Climate Change Disinformation and a Forum on SCALE |

---

## Policies

### Peer Review

| Aspect | Detail |
|--------|--------|
| **Type** | Double-blind for articles and features; referees are not compensated; manuscripts must be anonymised, including file properties (https://ijoc.org/index.php/ijoc/submission-guidelines; editorial policies page above) |
| **Transferable / Cascade?** | Blank. No source on the pages read |
| **Reviewer reports published?** | Blank. Not stated on the pages read |
| **Typical R+R rounds** | The journal aims for at most two rounds and rejects papers unlikely to be acceptable by round two, sometimes without consulting referees; "most articles go through at least two rounds" (editorial policies page). SciRev, 3 reviews: 1.7 rounds on average |
| **Reviewer recommendations** | The Editor makes all decisions after peer review; some decisions are made by the Managing Editors; no appeals or reversals of declined submissions except for misconduct allegations (editorial policies page) |

### AI Policy

| Aspect | Detail |
|--------|--------|
| **Has journal-specific AI policy?** | Yes: an "AI Guidelines" section (https://ijoc.org/index.php/ijoc/submission-guidelines, retrieved 2026-11-23) |
| **Explicit permission gate?** | No gate, but a narrow allowance: authors may use AI only for correcting language to improve clarity, and disclose it in a footnote on the title page; reviewers are prohibited from using AI to prepare reviews |
| **Leniency (1-5)** | 2 (this pass's judgement: use restricted to language correction) |
| **Summary** | AI tools or LLMs cannot be listed as authors or contributors (about page, https://ijoc.org/index.php/ijoc/about) |
| **Source URL** | https://ijoc.org/index.php/ijoc/submission-guidelines |

### Preprint Policy

> Source: the about, editorial-policies and submission-guidelines pages of ijoc.org were searched for "preprint", "pre-print", "repository" and "self-archiv" on 2026-11-23: no match. The journal states no preprint policy.

| Stage | Allowed? | Notes |
|-------|----------|-------|
| Pre-submission | Blank | No statement. The checklist says the submission must not have been previously published or be before another journal (https://ijoc.org/index.php/ijoc/about/submissions) |
| Under review | Blank | No statement; double-blind rules apply (see Peer Review) |
| Post-acceptance (AAM) | Blank | No statement. Articles are published open access under CC BY-NC-ND 4.0 (see Open Access) |
| Version of Record | Yes under the licence | Copies may be distributed for research or education without permission under the licence (https://ijoc.org/index.php/ijoc/about/submissions) |

### Open Access

| Aspect | Detail |
|--------|--------|
| **Model** | Fully open access; authors release articles under CC BY-NC-ND 4.0 (https://ijoc.org/index.php/ijoc/about/submissions, retrieved 2026-11-23) |
| **APC (if OA chosen)** | No fee for submission or registration. At acceptance, an overage fee of $30 per 250 words over 9,000 words may apply, plus possible international wire fees; $60 for each proof beyond three and $10 per line change (https://ijoc.org/index.php/ijoc/about, "Author Fees") |
| **Gold OA offered?** | Yes, the only route |
| **Read & Publish agreements** | Not applicable on the pages read |

---

## Format

> Source for the rules below: https://ijoc.org/index.php/ijoc/submission-guidelines and the checklist at https://ijoc.org/index.php/ijoc/about/submissions, read live 2026-11-23.

| Aspect | Detail |
|--------|--------|
| **Article types accepted** | Research articles, Features (opinion or op-ed style), Forum essays (only within Special Sections), Book reviews, Special Sections |
| **Word limit** | Research articles 6,000 to 8,900 words "all-inclusive" (abstract, captions, footnotes, references, appendices); Features 3,500 to 6,000; Forum essays 1,500 to 3,000; book reviews 1,200 to 1,500 on the checklist (about 1,500 including references in the book-review guidelines). Papers "must NOT exceed 8,900 words" on submission |
| **Word limit negotiability** | The about page says the journal is budgeted for 9,000 words per article and charges the overage fee above 9,000 at acceptance (https://ijoc.org/index.php/ijoc/about). The submission limit (8,900) and the fee threshold (9,000) differ on the same site; the pages do not reconcile them |
| **Abstract limit** | No more than 150 words, plus keywords |
| **Reference limit** | No cap beyond the all-inclusive word count. APA 7th edition |
| **Supplementary material** | IJoC does not host supplementary files; authors link to an outside source such as OSF, anonymised for review |
| **Figure/Table limits** | No count limit found; figures and tables go within the text at the reference point, not at the end |
| **Style / submission format** | Microsoft Word file, double-spaced, 12-point font; American English; endnotes converted to footnotes; URLs deactivated; only one submission by an author considered at a time; plagiarism check with iThenticate |

---

## Subject Density

> Based on Crossref records (not OpenAlex), 2021-11-23 to 2026-11-23, which in practice are 2026 articles (233 of 234 records).

### Top Topics (last 5 years)

> Not tabulated: no OpenAlex topic data was fetched.

| Topic | Article Count |
|-------|--------------|
| Not tabulated (OpenAlex not called) | — |

### Orientation

> Counts are word-boundary regex matches (case-insensitive) over the abstract of 128 Crossref records with an abstract out of 234 (54.7%); counts are lower bounds and describe 2026-registered articles only. Denominator for shares: 128. Regexes are listed in AI-Research Notes. Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Empirical vs. Theoretical** | Qualitative wording 41 (32.0%, C3); quantitative, survey or statistical wording 17 (13.3%, C1); "theoretical, conceptual, theorize" 21 (16.4%, C5). The scope says the journal is "centered in communication" and open to many disciplines (https://ijoc.org/index.php/ijoc/about) |
| **Quantitative vs. Qualitative** | Qualitative 41 (32.0%) against quantitative 17 (13.3%); mixed methods 10 (7.8%, C6); content analysis 10 (7.8%, C9); experiments 5 (3.9%, C2); computational wording 12 (9.4%, C8) |
| **Cross-disciplinary openness** | The journal asks for scholarship that "crosses disciplinary lines" and speaks to readers across sub-fields (about page). Politics or democracy wording 24 (18.8%, C13); misinformation wording 21 (16.4%, C10) |

---

## Soft Metadata

### Epistemological & Political Leanings

> Evidence layers: Crossref records of 2026 (234 records, 128 with abstract, regexes in AI-Research Notes); the journal's about page and featured collections. Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Cross-cultural friendliness** | The journal says it "engages established and emerging scholars from anywhere in the world" (https://ijoc.org/index.php/ijoc/about). Author countries were not counted (no country field in Crossref; OpenAlex not called) |
| **Editorial-board geography** | 136 board members, countries assigned by this pass from the printed institutions: USA 74, UK 11, Hong Kong 5, Germany 4, Canada 4, Australia 3, Belgium 3, Israel 3, Spain 3, Austria 2, Brazil 2, Chile 2, mainland China 2, Netherlands 2, Qatar 2, and one each for Argentina, Estonia, India, Italy, Malaysia, Mexico, Portugal, Singapore, South Africa, South Korea, Switzerland, the United Arab Emirates and Uganda (13 more), plus 1 entry with no institution printed; 74+11+5+4+4+3+3+3+3+2*6+13+1 = 136 (editorial board page, https://ijoc.org/index.php/ijoc/about/editorial-board, retrieved 2026-11-23). Two entries print two affiliations (Homero Gil de Zúñiga, Salamanca and Penn State, counted under Spain; Sarah Banet-Weiser, two US universities). 28 countries or territories appear. The separate editorial team page lists 8 people without affiliations |
| **Non-Western epistemology openness** | Indigenous, decolonial or colonial wording in 4 of 128 abstracts (3.1%, C12). No editorial statement read |
| **Diversity topic receptiveness** | Gender, queer or feminist wording 8 (6.2%, C14); race wording 4 (3.1%, C11); migration wording 4 (3.1%, C15). No editorial statement on these topics read |
| **Dominant theoretical tradition** | No single school stated. Featured on the about page: a Special Section on Climate Change Disinformation and a Forum on SCALE: Tracing the Sociotechnical Convenings, Sizes, Transitions, and Measurements Shaping Communication Systems (https://ijoc.org/index.php/ijoc/about). Most-cited 2026 records in Crossref have only 2 to 4 citations as of 2026-11-23: https://doi.org/10.65476/7tp42020 (4), https://doi.org/10.65476/1sxwvg58 (4), https://doi.org/10.65476/rqpmyd95 (3), so no citation-based tradition can be read. The journal states no political position on any page read |

### Framing Requirements

- **Mandatory framing?** Partly: the journal is "an interdisciplinary journal that, while centered in communication, is open and welcoming" to other disciplines, and wants scholarship that addresses "the wider audiences" of communication sub-fields rather than narrow specialist conversations (https://ijoc.org/index.php/ijoc/about, retrieved 2026-11-23).
- **What kind of engagement?** Articles, Features, Forums, Special Sections and Book Reviews are accepted (https://ijoc.org/index.php/ijoc/submission-guidelines). Ethics statements are expected: IRB or ethics approval, or an explanation of why none was required (https://ijoc.org/index.php/ijoc/about/editorialPolicies).
- **Article type and length**: research articles 6,000 to 8,900 words all-inclusive (see Format).
- **Special-issue framing seen**: Special Section on Climate Change Disinformation; Forum on SCALE (about page, retrieved 2026-11-23). Special Sections and Forums are subsidised by guest editors (submission guidelines).
- **Consequences of ignoring it**: papers over 8,900 words breach the submission limit and over 9,000 attract a fee (see Format); the journal does not consider appeals of declined papers (editorial policies page). SciRev reports 13% accepted from 866 manuscripts, editor-supplied (https://scirev.org/journal/international-journal-of-communication/).

### Methodological Preferences

> Counts: regex matches over the abstract of Crossref records dated 2021-11-23 to 2026-11-23 (in practice 2026); 128 of 234 records have an abstract (54.7%); shares use 128. Scoring convention of this research pass (its own, not an external standard): share 0 = 0; under 1% = 1; 1-5% = 2; over 5% = 3; 4-5 only with a cited editorial statement. Scores measure how often a method appears in abstracts, not how a reviewer would judge it. Regexes C1 to C16 are in AI-Research Notes.

| Method | Receptiveness (0-5) | Evidence |
|--------|---------------------|----------|
| Quantitative experimental | 3 | Survey, regression or statistical wording 17 (13.3%, C1); experiment wording 5 (3.9%, C2) |
| Qualitative interviews | 3 | Interview, focus-group, thematic, grounded-theory or "qualitative" wording 41 (32.0%, C3) |
| Autoethnography | 0 | 0 of 128 (C4). The row fits the field marginally |
| Theoretical / Conceptual | 3 | 21 (16.4%, C5); the journal also publishes opinion-style Features of 3,500 to 6,000 words (submission guidelines) |
| Mixed methods | 3 | 10 (7.8%, C6) |
| Meta-analysis | 1 | Meta-analysis or review wording 1 (0.8%, C7) |
| Ethnography (added row) | 3 | 7 (5.5%, C16) |
| Content analysis (added row) | 3 | 10 (7.8%, C9) |
| Computational methods (added row) | 3 | 12 (9.4%, C8) |

### Voice & Style

| Aspect | Detail |
|--------|--------|
| **First-person voice acceptance (0-5)** | Not scored. Abstract-only: 73 of 128 abstracts (57.0%) contain I, we, our or my (case-sensitive regex C17); title plus abstract 74. Among the 20 most recent abstracts (2026-09-29 to 2026-11-13) 16 do (Crossref, retrieved 2026-11-23). The anonymisation rules ask authors to avoid first person in association with their own citations (https://ijoc.org/index.php/ijoc/submission-guidelines) |
| **Expected density** | Research articles 6,000 to 8,900 words all-inclusive (submission guidelines) |
| **Abstract and keywords** | Abstract no more than 150 words, keywords required (submission guidelines) |
| **Writing style notes** | APA 7th edition; American English; footnotes not endnotes; authors give a profile with affiliation and position (https://ijoc.org/index.php/ijoc/about/submissions) |
| **Authorship pattern** | Crossref author counts of 234 records: 1 author 148, 2 authors 45, 3 authors 17, 4 or more 24 (https://api.crossref.org/works?filter=issn:1932-8036, retrieved 2026-11-23) |

### Reviewer Pool Characteristics

Reviewer behaviour itself is not observable from public pages; what follows is what public pages do show.

| Aspect | Detail | Evidence |
|--------|--------|----------|
| **Dominant tradition** | US-centred communication and media studies by institutional geography: 74 of 136 board members list a US institution, followed by UK 11 and Hong Kong 5 (see Editorial-board geography). The institutions do not state a school of thought. The team page has 8 entries (Editor 1, Managing Editors 2, Webmaster 1, Assistant Editors 4), 8 = 1+2+1+4. No reviewer list is published | https://ijoc.org/index.php/ijoc/about/editorial-board ; https://ijoc.org/index.php/ijoc/about/editorialTeam |
| **Reviewer list size** | Blank. No public reviewer list found | — |
| **Review model** | Double-blind; reviewers must follow the Reviewer Guidelines and are given five weeks initially; referees are unpaid | https://ijoc.org/index.php/ijoc/about/editorialPolicies |
| **Reviewer competence variance** | Blank as a judgement. SciRev, 3 reviews as printed: 2.3 review reports per manuscript, 1.7 rounds; one entry rates the overall experience 1 of 5 for a rejection after 13.1 weeks | https://scirev.org/journal/international-journal-of-communication/ ; https://scirev.org/reviews/international-journal-of-communication/ |
| **Quantitative mindset bias on qualitative work?** | Blank. No source on reviewer attitudes; qualitative wording appears in 41 of 128 abstracts (C3), so qualitative work is common, which cannot tell how reviewers treat it | Crossref counts, see Methodological Preferences |
| **Discourse community signals (editorial board)** | Board of 136 with institutions and no countries; 74 US institutions, then UK 11 and Hong Kong 5; 28 countries or territories (country tally under Editorial-board geography) | https://ijoc.org/index.php/ijoc/about/editorial-board |

### Sensitive Topics

> Counts are regex matches (labels in AI-Research Notes) over the abstract of 128 Crossref records with an abstract (2026 output); lower bounds. "Receptiveness" gives frequency; "High" is used only where the journal runs a section or collection on the topic.

| Topic Category | Receptiveness | Evidence |
|----------------|---------------|----------|
| Misinformation, disinformation and propaganda | High | 21 of 128 (16.4%, C10); a featured Special Section on Climate Change Disinformation (https://ijoc.org/index.php/ijoc/about, retrieved 2026-11-23) |
| Politics, democracy and polarisation | Regularly published | 24 (18.8%, C13) |
| AI and large language models | Regularly published | 19 (14.8%, C18) and 18 record titles; the journal has an AI-use policy that limits use to language correction (submission guidelines) |
| Climate and environment | Regularly published | 15 (11.7%, C19); the featured Special Section above |
| Surveillance and privacy | Present | 13 (10.2%, C20) |
| War, violence and conflict | Present | 10 (7.8%, C21) |
| Gender, queer and feminist topics | Present | 8 (6.2%, C14) |
| Race, indigenous and migration topics | Rare to present | race 4 (3.1%, C11); indigenous or decolonial 4 (3.1%, C12); migration 4 (3.1%, C15) |

### Practical Concerns

| Concern | Detail |
|---------|--------|
| **IRB requirement strictness** | Articles should carry statements on IRB or ethics approval, or an explanation of why none was required; approval numbers are redacted for blind review and reinstated if accepted (https://ijoc.org/index.php/ijoc/about/editorialPolicies, retrieved 2026-11-23). A participant-consent statement is asked for where content could identify participants (same page) |
| **Single-author acceptance** | Single-author records are 148 of 234 (63.2%) (Crossref, https://api.crossref.org/works?filter=issn:1932-8036, retrieved 2026-11-23) |
| **Independent scholar friendliness** | Authors give a profile with affiliation and position (https://ijoc.org/index.php/ijoc/about/submissions); no independent-scholar rule found |
| **Data transparency requirement** | Supplementary files are not hosted; authors link to an external source such as OSF and anonymise it for review (https://ijoc.org/index.php/ijoc/submission-guidelines) |
| **OPSEC compatibility** | Double-blind: remove names, acknowledgments, grants and file-property author data; cite own work as "Author, forthcoming"; avoid first person tied to a citation (https://ijoc.org/index.php/ijoc/about/submissions). The journal states no preprint policy |
| **AI use** | Language correction only, disclosed in a title-page footnote; reviewers may not use AI; no AI authors (https://ijoc.org/index.php/ijoc/submission-guidelines) |
| **Open access and cost** | No submission fee; overage fee above 9,000 words ($30 per 250 words), proof and line-change fees, possible wire fees (https://ijoc.org/index.php/ijoc/about) |
| **Funding and permissions** | Funding, conflict-of-interest and IRB statements go in a title-page footnote, and funding is also entered in the Supporting Agencies field, redacted for new submissions and reinstated when accepted (https://ijoc.org/index.php/ijoc/submission-guidelines); the conflict-of-interest rule is also on https://ijoc.org/index.php/ijoc/about/editorialPolicies. Authorship changes during review may need a check that blind review is not compromised (https://ijoc.org/index.php/ijoc/about) |
| **Prior and parallel publication** | The submission must not be previously published nor before another journal, or an explanation is given in "Comments to the Editor" (https://ijoc.org/index.php/ijoc/about/submissions) |

### AI-Research Notes (sources, blanks, and cross-language checks)

**signal_quality (0-5)**: overall 3. Per layer: Crossref counts 2 (abstract coverage 54.7%, only 2026 output); journal policies and guidelines 4 (own pages read live); editorial board 3 (board page read live: names and institutions, no countries; countries assigned from institution names); experiential layer 1 (SciRev n = 3 plus editor-supplied figures).

**Sources cited across this entry:** https://ijoc.org/index.php/ijoc/about ; /about/submissions ; /about/editorialPolicies ; /about/editorialTeam ; /about/editorial-board ; /submission-guidelines (all fetched live with curl on 2026-11-23, HTML comments stripped before reading); https://api.crossref.org/journals/1932-8036 and Crossref works for the window; local spine (OpenAlex snapshot 2026-07-13); https://scirev.org/journal/international-journal-of-communication/ and https://scirev.org/reviews/international-journal-of-communication/.

**Method notes:** Python `re` IGNORECASE except C17; abstracts only; regex hits count records. Broad patterns over-count: C13 "democra-" and "election-", C18 "AI" in any case, C5 all "theor-" forms. The window holds almost only 2026-registered articles, so shares describe the current volume, not five years.

**Keyword regexes (exact):**
- C1 `\b(regression|statistical(ly)?|quantitative|surveys?|questionnaires?|panel data|econometric\w*|multilevel|propensity)\b` ; C2 `\b(experiments?|experimental|randomi[sz]ed|quasi-experimental)\b` ; C3 `\b(interviews?|focus groups?|thematic analysis|grounded theory|qualitative)\b` ; C4 `\bautoethnograph\w*\b`
- C5 `\b(theoretical(ly)?|conceptual(ly)?|theori[sz]\w*)\b` ; C6 `\bmixed[- ]methods?\b` ; C7 `\b(meta-analys[ei]s|systematic review|literature review|scoping review|research synthesis)\b` ; C8 `\b(machine learning|computational|topic model\w*|network analysis|natural language processing|deep learning|text mining)\b` ; C9 `\bcontent analysis\b`
- C10 `\b(misinformation|disinformation|fake news|propaganda)\b` ; C11 `\b(raci(al|alized|alised|ist|sm)|racio\w*|whiteness|anti-?racis\w*)\b` ; C12 `\b(indigenous|decoloni\w*|postcolonial|colonial\w*)\b` ; C13 `\b(populis\w*|authoritarian\w*|polari[sz]ation|election\w*|democra\w*)\b`
- C14 `\b(gender(ed)?|queer|LGBT\w*|transgender|non-?binary|sexuality|feminis\w*)\b` ; C15 `\b(migrants?|refugees?|immigrants?|immigration|asylum|migration)\b` ; C16 `\bethnograph\w*\b` ; C17 (case-sensitive) `\b(I|[Ww]e|[Oo]ur|[Mm]y)\b`
- C18 `\b(artificial intelligence|generative AI|ChatGPT|large language models?|LLMs?|AI)\b` ; C19 `\b(climate|environmental|ecolog\w*)\b` ; C20 `\b(surveillance|privacy)\b` ; C21 `\b(war|genocide|Gaza|Ukraine|Palestin\w*|violence)\b`

**Unreadable pages:** none among the journal's own pages. The "Turnaround Time" section of the editorial-policies page says "We aim to adhere to the following standards for turnaround time" and the page's raw HTML holds no table or list after that sentence, so no turnaround standards are recorded (the page does not list them, as far as the HTML shows).

**Fields deliberately left blank, and why:** print ISSN, founding year, OpenAlex ID, desk rejection rate, transfer policy, reviewer reports, preprint policy (searched, no text), reviewer list. Board countries are this pass's assignment from institution names, not printed on the page.

**Cross-language and forum checks performed:**
- SciRev: journal page and reviews page read (3 reviews; editor-supplied acceptance figures).
- One English web search naming this journal with "reddit", "review time" and "desk reject" returned no thread about it (2026-11-23). Chinese-language sources and LetPub were not searched for this journal in this pass (time box); that is not a "0 results" finding.

---

## Strategic Notes

> Each statement follows from a fact recorded above and names it. Where evidence is missing the field says so.

### Hard Blockers

- **Length**: research articles must stay within 8,900 words all-inclusive (Format).
- **Anonymisation**: manuscripts, file properties and self-citations must be anonymised (Peer Review; Practical Concerns).
- **One submission at a time per author** and no appeals of declined papers (Format; Peer Review).
- **AI**: use limited to language correction with a title-page footnote (AI Policy).

### Soft Tax

- **Time**: reviewers get five weeks initially, most articles need at least two rounds, and SciRev (n = 3) reports 2.5 months to a first round (Review Cycle Time).
- **Cost**: no submission fee, but fees apply above 9,000 words and for extra proofs (Open Access).
- **Selectivity**: 13% accepted of 866 manuscripts, editor-supplied to SciRev, year unstated (Metrics).

### Best Suited For

- Interdisciplinary communication work with a broad readership, qualitative or mixed: qualitative wording in 41 of 128 abstracts, mixed methods in 10 (Orientation; Methodological Preferences).
- Politics, misinformation and platform topics, which the journal features (Sensitive Topics).
- Authors who want free open access with no APC (Open Access).

### Not Recommended For

- Very long manuscripts: the 8,900-word all-inclusive limit includes references (Format).
- Authors who need a preprint policy or a published reviewer pool before choosing: neither exists on the journal's pages (Preprint Policy; Reviewer Pool).

### Rejection Fallback Chain

> No source states where rejected authors usually go. The rows below are topical neighbours that already exist in this corpus, listed only because they share subject area; they are not claims about acceptance odds.

| Rank | Journal | Why this fallback works |
|------|---------|------------------------|
| 1 | [Journal of Communication](journal-of-communication.md) | Topical neighbour in communication; no fit evidence collected here |
| 2 | [Journal of Computer-Mediated Communication](journal-of-computer-mediated-communication.md) | Topical neighbour (platforms and media); no fit evidence collected here |
| 3 | | |

---

## Changelog

| Date | Change | By |
|------|--------|----|
| 2026-11-23 | Initial entry (spine and Crossref scaffold) | AI-assisted (maintainer-directed) |
| 2026-11-23 | AI deep research pass; no first-hand human reports | AI-assisted (maintainer-directed) |
| 2026-11-24 | Corrections after independent verification (editorial board page read and counted by country; 2026 record counts stated for both endpoints; funding-footnote source; turnaround wording) | @Zaious |
| 2026-11-23 | Promoted to Tier 1 under the written rule: tier1_gate passes; independent spot-check 5 supported and 1 partial of 6 sampled pairs; a wrongly recorded 'no editorial board' was corrected from the live page afterwards; banner removed; no first-hand human reports | AI-assisted (maintainer-authorised, not human-verified) |
