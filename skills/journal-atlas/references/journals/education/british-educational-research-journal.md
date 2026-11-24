<!-- schema: v1.3 -->
<!-- AI-researched entry — Journal Atlas v2 coverage pipeline. See docs/ATLAS_V2_DESIGN.md for methodology. -->
<!-- Scaffold values from the OpenAlex Sources API (scripts/import_openalex.py dry-run, 2026-11-23), then filled by an AI deep research pass (maintainer-directed) on 2026-11-23. -->

# British Educational Research Journal

> **Last verified**: 2026-11-24
> **Maintainer**: @Zaious
> **Venue type**: Journal
> **Evidence basis**: Sourced under the written rule (SEED_DATA_QUALITY.md): deeper per-journal research by an AI model, directed by the maintainer, 2026-11-23; overall signal_quality **3/5**. Claims cite source URLs or counts; blanks are recorded with reasons. Independent spot-check on 2026-11-23: 7 of 7 sampled pairs supported; wrong 'no copy' and founding-date claims corrected. No first-hand human reports; not human-verified.

---

## Identity

| Field | Value |
|-------|-------|
| **Abbreviation** | BERJ (used by the society's own journal page, https://www.bera.ac.uk/publication/british-education-research-journal; retrieved 2026-11-23). No ISO abbreviation source read |
| **Venue type** | Journal |
| **Publisher** | Wiley, for the British Educational Research Association. Source: https://api.crossref.org/journals/0141-1926 (publisher string "Wiley (John Wiley & Sons)"; title "British Educational Research Journal"; print ISSN 0141-1926 and electronic ISSN 1469-3518 both returned), and the society's statement that Wiley is the sole publisher (https://www.bera.ac.uk/publication/british-education-research-journal), retrieved 2026-11-23. Note: a Taylor & Francis Online page for the title exists (https://www.tandfonline.com/journals/cber20, Wayback copy 2023-08-20) but is a legacy back-file archive that says "Published by Wiley from 2013" and shows content only up to 2012; Crossref DOIs for 2021 to 2026 are all Wiley (prefix 10.1002/berj) |
| **ISSN (Print)** | 0141-1926 |
| **ISSN (Online)** | 1469-3518 |
| **Founded** | 1975. The society's page says the journal "was established in 1975" and marked its 50th anniversary in 2025 (https://www.bera.ac.uk/publication/british-education-research-journal; the link https://www.bera.ac.uk/?p=326 redirects to it; retrieved 2026-11-23). The page also lists five anniversary virtual issues, the first covering 1975 to 1984 (2022 editorial https://doi.org/10.1002/berj.3830, record in Crossref) |
| **URL** | https://onlinelibrary.wiley.com/journal/14693518 (society page: https://www.bera.ac.uk/publication/british-education-research-journal) |
| **Author Guidelines** | https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html (the older address https://onlinelibrary.wiley.com/page/journal/14693518/homepage/forauthors.html redirects to it), read in full in a real browser on 2026-11-24 (it returned HTTP 403 to curl on 2026-11-23; the page prints no date). The Wayback copy of 2024-02-01 (https://web.archive.org/web/20240201104500id_/https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html) is older; the word range, abstract limit, double-blind rule and preprint rule are unchanged on the live page, and the live page adds a journal-specific AI paragraph. Notes: chrome2/berj-pages.txt in the researcher's scratch folder |
| **Society / Association** | British Educational Research Association (BERA); BERJ is described as BERA's flagship journal (https://www.bera.ac.uk/publication/british-education-research-journal; retrieved 2026-11-23) |
| **Editorial Board Location** | OpenAlex source country code: GB (https://openalex.org/S60281869). The society announced a six-editor team from January 2024 at Sheffield Hallam University, Brunel University London, Queen's University Belfast, University of Glasgow, University of Reading and University of Nottingham (https://bera.ac.uk/?p=43438, posted 2023-07-07; retrieved 2026-11-23). The live board page (https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/editorialboard.html, read in a real browser 2026-11-24, no date printed) lists 6 editors at Sheffield Hallam University, King's College London, Queen's University Belfast, University of Glasgow, University of Reading and University of Nottingham, a social media editor at Brunel University London, and 75 people in all (see Editorial-board geography). Older, kept as older: the Wayback copy of 2024-02-28 (https://web.archive.org/web/20240228050059id_/https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/editorialboard.html) listed 6 editors and 20 board members |
| **OpenAlex ID** | https://openalex.org/S60281869 |

---

## Metrics

> Source: OpenAlex (CC0), retrieved 2026-11-23 (scaffold values from the Sources API). JCR impact factor and quartile are paywalled and deliberately not stated, and figures quoted on the publisher's and society's pages are not repeated here. The 2-year mean citedness below is an OpenAlex proxy, not a JCR figure. The local spine (an OpenAlex snapshot dated 2026-07-13, `scripts/query_spine.py`) gives works_count 3011 and h-index 142 for the same ISSN; the live scaffold values below are newer.

| Metric | Value | Date |
|--------|-------|------|
| **Impact Factor** | Not stated (JCR is paywalled) | |
| **5-Year IF** | Not stated (JCR is paywalled) | |
| **h-index** | 174 (OpenAlex) | 2026-11-23 |
| **CiteScore** | 5.2, labelled "2025 CiteScore (Scopus)" on the publisher's metrics page (https://bera-journals.onlinelibrary.wiley.com/journal/14693518/journal-metrics, read in a real browser 2026-11-24); Scopus itself was not opened. The same page prints Clarivate figures, which are deliberately not recorded here | 2025 (label on page) |
| **Acceptance Rate** | 11% under the label "2025 Acceptance rate" on the live publisher metrics page (https://bera-journals.onlinelibrary.wiley.com/journal/14693518/journal-metrics, read 2026-11-24; the page also prints 188 as "2025 Total articles published"). The editors' editorial of 17 January 2025 says they handled 1,167 original articles in 2024 with an 11.5% acceptance rate (Accepted Version, https://shura.shu.ac.uk/34874/1/Final_BERJ%20Editorial.pdf; repository record https://shura.shu.ac.uk/34874/; read 2026-11-23). SciRev's editor-provided fields are empty (https://scirev.org/journal/british-educational-research-journal/) | 2025 (publisher page); 2024 data (editorial) |
| **Desk Rejection Rate** | Blank. No rate found. The same 2025 editorial (https://shura.shu.ac.uk/34874/1/Final_BERJ%20Editorial.pdf) says out-of-scope submissions are the main reason the editors desk reject papers, and that they transfer papers to sister journals where possible. The guidelines say editors may reject before peer review when scope or basic quality is not met (Wayback copy 2024-02-01, https://web.archive.org/web/20240201104500id_/https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html). SciRev, n=4: decision time for immediate rejection 66 days (https://scirev.org/journal/british-educational-research-journal/) | 2026-11-23 |
| **Quartile (by field)** | Not stated (SJR not read). The local spine records JUFO level 3 for this ISSN (Finnish publication forum, spine snapshot 2026-07-13) | |
| **2-yr Mean Citedness (OpenAlex IF proxy)** | 6.02 (OpenAlex proxy, not JCR) | 2026-11-23 |
| **i10-index** | 1751 (OpenAlex) | 2026-11-23 |
| **Total Works** | 3086 (OpenAlex, all years and work types) | 2026-11-23 |

### Review Cycle Time

| Stage | Typical Time | Notes |
|-------|-------------|-------|
| **Time to first decision** | Publisher metrics page, 2025 median of 7 days from submission to first decision (https://bera-journals.onlinelibrary.wiley.com/journal/14693518/journal-metrics, read 2026-11-24). The live guidelines say the editors aim for a first decision within 12 weeks of submission (read 2026-11-24; same in the Wayback copy 2024-02-01, https://web.archive.org/web/20240201104500id_/https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html). SciRev, n=4 reviews: first review round 1.4 months on average and 66 days for an immediate rejection (https://scirev.org/journal/british-educational-research-journal/; retrieved 2026-11-23) | The 12 weeks is a stated aim, not a measured figure. The 2025 editorial (https://shura.shu.ac.uk/34874/1/Final_BERJ%20Editorial.pdf) says up to 20 reviewer invitations are not unusual before reviewers are secured, which it gives as the main reason review sometimes takes long |
| **Time to first review** | Blank. No separate figure found | |
| **Time to acceptance (total)** | Publisher metrics page, 2025 median of 154 days from submission to acceptance (https://bera-journals.onlinelibrary.wiley.com/journal/14693518/journal-metrics, read 2026-11-24). SciRev: 4.0 months average total handling time for accepted manuscripts, n=4 reviews (https://scirev.org/journal/british-educational-research-journal/; the page does not say how many of the four were accepted). LetPub page for the title was not located by search | n is very small |
| **Time to publication (after acceptance)** | Publisher metrics page: median 17 days from acceptance to publication for 2025 (https://bera-journals.onlinelibrary.wiley.com/journal/14693518/journal-metrics, read 2026-11-24) | Publisher figure, labelled 2025 |

### Publication Frequency

| Aspect | Detail |
|--------|--------|
| **Schedule** | Six issues per year, one every two months: Crossref lists issue records v47.1 to v47.6 for 2021, v48.1 to v48.6 for 2022, v49.1 to v49.6 for 2023, v50.1 to v50.6 for 2024, v51.1 to v51.6 for 2025 and v52.1 to v52.5 for 2026 up to October (https://api.crossref.org/journals/0141-1926/works?filter=from-pub-date:2021-01,until-pub-date:2026-12, 35 journal-issue records; retrieved 2026-11-23) |
| **Articles per year (approx.)** | Crossref journal-article records by published year (https://api.crossref.org/journals/0141-1926/works?filter=from-pub-date:2021-01,until-pub-date:2026-12, 839 articles): 2021 = 76, 2022 = 77, 2023 = 104, 2024 = 156, 2025 = 211, 2026 = 215 (partial year, latest record dated 2026-11-17). Output has risen year on year; the cause was not investigated. Retrieved 2026-11-23 |
| **Special issues?** | Yes, called "special sections" and "special issues": the guidelines copy links a call for special section proposals and a special-issues list (https://web.archive.org/web/20240201104500id_/https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html). Crossref records 2021 to 2023 include special-section introductions, for example "Right-wing populism and education" (https://doi.org/10.1002/berj.3726) and "Refugee education" (https://doi.org/10.1002/berj.3764) |

---

## Policies

### Peer Review

| Aspect | Detail |
|--------|--------|
| **Type** | Double-blind. The live guidelines say "this journal operates on a double-blind peer review process", with author names, affiliations, acknowledgements and explicit mentions of the author's institution on a separate page; articles will usually be peer reviewed anonymously by at least two reviewers; the editors reserve the right to reject before peer review when scope or basic quality standards are not met; and the editors' decision is final. Authors upload an anonymised and a full version and cite their own work in the third person (https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html, read 2026-11-24; the same in the Wayback copy 2024-02-01, https://web.archive.org/web/20240201104500id_/https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html). Retrieved 2026-11-24 |
| **Transferable / Cascade?** | Yes, within Wiley: the journal participates in the Wiley Education publishing network and Wiley's Refer & Transfer program; at the editors' judgement a manuscript may be recommended to another journal in the network, and the author may transfer with any earlier reviewer reports (same guidelines copy). Which journals are in the network was not read |
| **Reviewer reports published?** | Blank. No statement found in the pages read |
| **Typical R+R rounds** | Blank. No stated figure; SciRev, n=4, reports 2.0 review rounds and 2.0 review reports on average (https://scirev.org/journal/british-educational-research-journal/) |
| **Reviewer recommendations** | Blank. No source found |

### AI Policy

| Aspect | Detail |
|--------|--------|
| **Has journal-specific AI policy?** | Yes. The live guidelines have an "Artificial Intelligence Generated Content" paragraph that points to the BERA AI Statement and COPE's position: AI tools cannot be listed as authors; use of an AI tool to develop any portion of a manuscript "must be described, transparently and in detail" in the Methods or Acknowledgements; tools for spelling, grammar, language polishing and formatting need no disclosure; and the journal's editor decides whether use is permissible. Authors must also include an "AI Use Declaration Statement" at the end of the paper, alongside the conflict-of-interest and data-availability statements, naming the tool and the purpose, or stating that no AI tools were used (https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html, read in a real browser 2026-11-24). The 2024-02-01 copy had no such rule. The publisher-wide Wiley policy also applies |
| **Explicit permission gate?** | No gate; the editor decides on permissibility case by case (live guidelines, read 2026-11-24). Disclosure is mandatory for anything beyond spelling, grammar, language polishing and formatting |
| **Leniency (1-5)** | 3 (allowed with mandatory disclosure and an AI Use Declaration Statement; same rubric as other entries in this corpus) |
| **Summary** | Wiley guidance: authors must disclose use of AI technologies when submitting to a Wiley-published journal and keep documentation of the tool, its purpose and how they verified the output; AI may be a companion to writing, not a replacement; AI tools cannot be authors because they cannot be held accountable. Retrieved 2026-11-23 |
| **Source URL** | https://www.wiley.com/en-us/publish/article/ai-guidelines/ |

### Preprint Policy

> Journal statement from the guidelines (Wayback copy 2024-02-01) plus the publisher's self-archiving page (https://authorservices.wiley.com/author-resources/Journal-Authors/licensing/self-archiving.html; retrieved 2026-11-23).

| Stage | Allowed? | Notes |
|-------|----------|-------|
| Pre-submission | Yes | The journal will consider articles previously available as preprints, and authors may post the submitted version to a preprint server at any time (guidelines copy 2024-02-01, https://web.archive.org/web/20240201104500id_/https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html). Wiley's page says the submitted version has no embargo and need not be removed from not-for-profit preprint servers before submission. Because review is double-blind, a public preprint may identify the author to reviewers; the guidelines do not discuss this |
| Under review | Yes | The guidelines say the submitted version may be posted at any time |
| Post-acceptance (AAM) | Yes, with embargo | The guidelines say the embargo for sharing the accepted version is 18 months for BERJ; Wiley's general page gives 12 to 24 months by field. Embargo: 18 months (journal-specific, guidelines copy 2024-02-01) |
| Version of Record | Open access articles per licence | Per the publisher's page; non-open-access articles are not freely postable |

### Open Access

| Aspect | Detail |
|--------|--------|
| **Model** | Hybrid (subscription with optional open access). Evidence: the society says no fee is charged for publishing in BERJ other than optional open access charges and colour (https://www.bera.ac.uk/publication/british-education-research-journal; retrieved 2026-11-23), and the guidelines say authors who choose open access are charged a fee (Wayback copy 2024-02-01) |
| **APC (if OA chosen)** | Blank. The live guidelines say authors who choose open access are charged a fee and point to the journal's Open Access page for the APC (https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html, read 2026-11-24); that page was not read |
| **Gold OA offered?** | Yes, per the two statements above |
| **Read & Publish agreements** | Blank. The guidelines point to Wiley's author compliance tool and funder agreement pages, which were not read |

---

## Format

> Source for the general rules: the journal's live author guidelines (https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html), read in a real browser on 2026-11-24; the page prints no date. Retrieved 2026-11-24. The Wayback copy dated 2024-02-01 (https://web.archive.org/web/20240201104500id_/https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html) is older, and a copy dated 2019-12-09 (https://web.archive.org/web/20191209183236id_/https://onlinelibrary.wiley.com/page/journal/14693518/homepage/forauthors.html) gave 5000 to 8000 words and an abstract of 200 to 250 words, unchanged on the live page.

| Aspect | Detail |
|--------|--------|
| **Article types accepted** | Original Article (reports of original research with methods, findings and conclusions); Response (an opinionated piece by one or more experts on a topic or publication); Editorial (by the editor or someone invited). The journal offers "Free Format" submission (2024-02-01 copy) |
| **Word limit** | Articles should normally be between 5000 and 8000 words, excluding the title page, references and figures/tables (live guidelines, read 2026-11-24; same in the 2024-02-01 copy). A Taylor & Francis legacy page for the title says normally 6000 to 8000 words (https://www.tandfonline.com/journals/cber20, Wayback copy 2023-08-20), which differs and is not used. Crossref page ranges give a median article length of 20 pages (quartiles 18 and 24) over 667 of 839 records with parseable ranges, 2021 to 2026 |
| **Word limit negotiability** | Blank. The guidelines word the range as "normally"; no statement on exceptions found |
| **Abstract limit** | Abstract of 200 to 250 words; up to four keywords. On invitation to revise, authors add a "Key Insights" section under the abstract with two answers of up to 50 words each (2024-02-01 copy) |
| **Reference limit** | No cap found; references are excluded from the word range (2024-02-01 copy) |
| **Supplementary material** | Blank. The guidelines copy links a supplementary-materials page that was not read |
| **Figure/Table limits** | No count limit found. Tables go in separate files and captions in a separate file; figures are uploaded separately at revision (2024-02-01 copy) |
| **Style / submission format** | British spelling; APA-style references with authors' own work cited in the third person; Word format; two files (anonymised and full); submission through the Research Exchange portal (all new manuscripts since 2021-12-07 per the guidelines copy); Crossref-style similarity screening by iThenticate before peer review; manuscript structure left to the authors ("introduction, literature review, research design, empirical findings, discussion and conclusion" for some empirical work, with other structures expected for interpretative, theoretical, historical and policy research) (2024-02-01 copy) |

---

## Subject Density

> Top Topics come from the OpenAlex works API, retrieved 2026-11-25 (request URL under the table); the Orientation counts below come from Crossref records, with abstracts from Semantic Scholar where stated there, retrieved 2026-11-23.

### Top Topics (last 5 years)

> Source: OpenAlex works API, source S60281869, works of type article dated 2021-11-23 to 2026-11-23 (673 works), grouped by topic: https://api.openalex.org/works?filter=primary_location.source.id:S60281869,type:article,from_publication_date:2021-11-23,to_publication_date:2026-11-23&group_by=topics.id . Retrieved 2026-11-25. 200 topic groups were returned, which is the API's per-page cap of 200, sorted by count; only the top 10 are shown. The 10th and 11th topics are tied at 28; the order between tied topics is the API's. These are OpenAlex topic-assignment counts, not article counts: a work can carry several topics, so the counts do not sum to 673.

| Topic | Article Count |
|-------|--------------|
| Teacher Education and Leadership Studies | 109 |
| School Choice and Performance | 98 |
| Higher Education Governance and Development | 53 |
| Higher Education Research Studies | 50 |
| Teacher Professional Development and Motivation | 45 |
| Early Childhood Education and Development | 40 |
| Global Educational Policies and Reforms | 39 |
| International Student and Expatriate Challenges | 31 |
| Cultural Capital and Social Class | 30 |
| Children's Rights and Participation | 28 |

### Orientation

> Counts come from 839 Crossref journal-article records published 2021-01 to 2026-11 (https://api.crossref.org/journals/0141-1926/works?filter=from-pub-date:2021-01,until-pub-date:2026-12), of which 778 (92.7%) carry an abstract in Crossref. Hits are counted over title plus abstract as a share of the 778; they are lower bounds because 61 records have no abstract. Regexes are listed in AI-Research Notes. Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Empirical vs. Theoretical** | Mixed, empirical wording more frequent: "interview" 230 (29.6%), "survey/questionnaire" 135 (17.4%), "regression/longitudinal/cohort" 102 (13.1%) alongside "theor-" 182 (23.4%) and "conceptual" 108 (13.9%) of 778 records with abstracts |
| **Quantitative vs. Qualitative** | Both present: "qualitative" 142 (18.3%), "quantitative" 35 (4.5%), "randomised/experiment" 36 (4.6%), "mixed methods" 9 (1.2%) of 778 |
| **Cross-disciplinary openness** | The society describes the journal as interdisciplinary, including case studies, experiments and surveys, discussions of conceptual and methodological issues, and accounts of research in progress (https://www.bera.ac.uk/publication/british-education-research-journal; retrieved 2026-11-23). Policy 223 (28.7%; regex `\bpolicy\b|\bpolicies\b`), teacher 307 (39.5%; `\bteachers?\b`), higher education 114 (14.7%; `\bhigher education\b`) and assessment 63 (8.1%; `\bassessments?\b`) of 778 (case-insensitive over title plus abstract; the earlier higher-education and assessment figures of 193 and 145 came from unrecorded regexes, one of which also matched the pronoun "he", and were replaced) |

---

## Soft Metadata

### Epistemological & Political Leanings

> Evidence layers: Crossref records (839, with abstracts for 778); the society's pages; the 2022 outgoing-editors' editorial (abstract read in Crossref). OpenAlex country and keyword counts were not obtained (rate limit). Retrieved 2026-11-23.

| Dimension | Assessment |
|-----------|------------|
| **Cross-cultural friendliness** | Author countries taken from Crossref affiliation strings (2213 of 2255 authors, 98%, name a recognised country; counts are articles with at least one author in the country, of 839 articles): United Kingdom 445, China 83, Australia 80, United States 41, Turkey 38, Hong Kong 33, Ireland 26, Netherlands 20, Canada 17, Germany 15 (https://api.crossref.org/journals/0141-1926/works; the pattern lists country names and abbreviations such as UK and USA, and an affiliation naming Northern Ireland counts for both the United Kingdom and Ireland). The society describes the journal as publishing by and for researchers throughout the world while showcasing British educational research (https://www.bera.ac.uk/publication/british-education-research-journal). The live board page (https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/editorialboard.html, read 2026-11-24) lists 75 people, 41 of them in the United Kingdom, China 6, Ireland 4, Hong Kong 3, Australia 3 (counts under Editorial-board geography); the older Wayback copy of 2024-02-28 listed 20 board members, 12 of them outside the United Kingdom, and the 2019-12-09 copy listed a smaller board and is superseded; the publisher's metrics page prints "2025 Top Author Countries/Regions": United Kingdom 45%, China 8%, Turkey 8%, Netherlands 3%, Australia 3% (https://bera-journals.onlinelibrary.wiley.com/journal/14693518/journal-metrics) |
| **Editorial-board geography** | Live board page (https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/editorialboard.html, read in a real browser 2026-11-24, no date printed): 75 people, namely 6 editors, 1 social media editor, 66 editorial board members, 1 Chair and 1 Vice-Chair (6 + 1 + 66 + 1 + 1 = 75). The 6 editors and the social media editor are at United Kingdom universities. Of the 66 board members, 33 are in the United Kingdom, China 6, Ireland 3, Hong Kong 3, Australia 3, Turkey 2, the United States 2, and one each in Germany, Bulgaria, Sweden, Finland, Taiwan, Canada, Oman, South Korea, Poland, Egypt, Ghana, Chile, New Zealand and Spain (33 + 6 + 3 + 3 + 3 + 2 + 2 + 14 = 66). The Chair is in Ireland and the Vice-Chair in the United Kingdom. All 75 by country: United Kingdom 41, China 6, Ireland 4, Hong Kong 3, Australia 3, Turkey 2, United States 2, and 14 countries with one each (41 + 6 + 4 + 3 + 3 + 2 + 2 + 14 = 75). The editors' 2025 editorial says the board was enlarged to 40 members (https://shura.shu.ac.uk/34874/1/Final_BERJ%20Editorial.pdf), which is fewer than the 66 plus Chair and Vice-Chair now listed. Older, kept as older: the Wayback copy of 2024-02-28 listed 6 editors and 20 board members (26 names; 8 board members in the United Kingdom and 12 elsewhere: Germany 1, Bulgaria 1, Sweden 1, Malta 1, Ireland 1, Canada 1, Poland 1, Australia 3, Spain 1, New Zealand 1) |
| **Non-Western epistemology openness** | Keyword count, title plus abstract of 778 records: "decolonial/Indigenous/Maori/Aboriginal" 20 (2.6%); "war, conflict, refugee, migra-" 59 (7.6%). The 2022 outgoing-editors' editorial argues for methodological, conceptual and theoretical diversity in educational research (abstract read, https://doi.org/10.1002/berj.3777) |
| **Diversity topic receptiveness** | Counts of 778 records with abstracts: gender/feminism/women/girls 73 (9.4%), race/racism/ethnic 63 (8.1%), social class/inequality/disadvantage 128 (16.5%), disability/special needs/inclusion 125 (16.1%), queer/LGBT/transgender/sexuality 12 (1.5%). The guidelines ask for writing free from gender or ethnic bias and link the society's diversity statement (2024-02-01 copy, https://web.archive.org/web/20240201104500id_/https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html) |
| **Dominant theoretical tradition** | No single tradition. Named theorists (Bourdieu, Foucault, Marx, Freire, Dewey, Deleuze, Arendt, Habermas) appear in 31 of 778 records (4.0%); "theor-" appears in 182 (23.4%). The most cited 2021-2026 items in Crossref (citation counts at retrieval) include "The effect of school closures on standardised student test outcomes" (297; https://doi.org/10.1002/berj.3754), "Reshaping curriculum adaptation in the age of artificial intelligence" (116; https://doi.org/10.1002/berj.4068), a study of factors affecting generative AI use among students (111; https://doi.org/10.1002/berj.4084), "Putting climate change at the heart of education" (96; https://doi.org/10.1002/berj.3816) and "Grading exams using large language models" (90; https://doi.org/10.1002/berj.4069). The journal states no political position on any page that could be read |

### Framing Requirements

- **Mandatory framing?** The editors' criteria on the journal's legacy Taylor & Francis page ask whether the article is of sufficient general interest to the educational research community, adding that a specialist focus need not exclude an article if it makes a general contribution to method or raises issues of wider interest; also international pitch and originality (https://www.tandfonline.com/journals/cber20, Wayback copy 2023-08-20; retrieved 2026-11-23). The current guidelines copy ties scope to rejection before review (https://web.archive.org/web/20240201104500id_/https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html).
- **What kind of engagement?** The society describes an interdisciplinary journal that includes case studies, experiments, surveys and discussions of conceptual and methodological issues (https://www.bera.ac.uk/publication/british-education-research-journal). The guidelines encourage authors to structure the manuscript to fit their research, noting that interpretative, theoretical, historical and policy research often does not fit an empirical template.
- **Article type and length**: Original Article, Response and Editorial in the guidelines; normally 5000 to 8000 words excluding references, abstract of 200 to 250 words, up to four keywords (live guidelines, read 2026-11-24).
- **Special-issue framing seen**: special sections are called for through a proposals page linked from the guidelines; recent examples in Crossref include right-wing populism and education (https://doi.org/10.1002/berj.3726) and care-experienced people's educational engagement (https://doi.org/10.1002/berj.3942).
- **Consequences of ignoring it**: the guidelines say editors reserve the right to reject papers before peer review when scope or basic quality standards are not met (2024-02-01 copy). SciRev, n=4: the latest review reports an immediate rejection for "not appropriate / relevant" after about three months (https://scirev.org/journal/british-educational-research-journal/).

### Methodological Preferences

> Counts are Crossref records (839) published 2021-01 to 2026-11 whose title or abstract matches the regex; shares use the 778 records with abstracts as denominator. Scoring convention of this research pass (its own, not an external standard): share 0 = 0; under 1% = 1; 1-5% = 2; over 5% = 3; 4-5 only with a cited editorial statement, and none was found that favours a single method (the 2022 editorial favours diversity of methods generally). Scores measure how often a method appears, not how a reviewer would judge it. Regexes are in AI-Research Notes.

| Method | Receptiveness (0-5) | Evidence |
|--------|---------------------|----------|
| Quantitative experimental | 2 | "randomised/randomization/RCT/experiment" 36 of 778 (4.6%); "quantitative" 35 (4.5%) |
| Survey and regression / longitudinal | 3 | "survey/questionnaire" 135 (17.4%); "regression/longitudinal/panel data/cohort" 102 (13.1%) |
| Qualitative interviews | 3 | "interview" 230 (29.6%); "qualitative" 142 (18.3%) of 778 |
| Case study | 3 | "case study" 53 (6.8%) of 778 |
| Ethnography | 2 | "ethnograph" 17 (2.2%) of 778; "autoethnography" was not counted separately |
| Discourse analysis | 3 | "discourse" 67 (8.6%) of 778 |
| Theoretical / Conceptual | 3 | "theor-" 182 (23.4%); "conceptual" 108 (13.9%); "philosoph-" 18 (2.3%) |
| Mixed methods | 2 | "mixed method" 9 (1.2%) of 778 |
| Systematic / literature review | 2 | "systematic review, meta-analysis, scoping review, literature review" 22 (2.8%) of 778 |

### Voice & Style

| Aspect | Detail |
|--------|--------|
| **First-person voice acceptance (0-5)** | Not scored. Sample: of the 100 most recently dated articles with a Crossref abstract (dated up to 2026-11-17), 35 abstracts contain I, my, we or our and 2 contain I or my; across all 778 abstracts, 296 contain one of those words (plural "we" may be generic rather than authorial). Records containing I or my include https://doi.org/10.1002/berj.70312 and https://doi.org/10.1002/berj.70232. The guidelines give no rule on first person. Retrieved 2026-11-23 |
| **Expected density** | Crossref page ranges give a median article length of 20 pages (quartiles 18 and 24) across 667 of 839 records (2021-2026; https://api.crossref.org/journals/0141-1926/works?filter=from-pub-date:2021-01,until-pub-date:2026-12). Length range: 5000 to 8000 words excluding references (guidelines copy 2024-02-01) |
| **Abstract and keywords** | Abstract of 200 to 250 words giving the rationale, methods if relevant and conclusions; up to four keywords; a Key Insights box on invited revision (guidelines copy, https://web.archive.org/web/20240201104500id_/https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html) |
| **Writing style notes** | Guidelines (2024-02-01): British spelling used throughout; APA-style references; authors' own work cited in the third person for anonymity; footnotes to the text avoided; free-format structure allowed; a title with the major keywords and no abbreviations |
| **Authorship pattern** | Of 779 Crossref records with author lists (2021-01 to 2026-11): 182 single-author, 215 two authors, 180 three, 202 four or more (retrieved 2026-11-23); 22 of the 100 most recent records with an abstract are single-author |

### Reviewer Pool Characteristics

Reviewer behaviour itself is not observable from public pages; what follows is what public pages do show.

| Aspect | Detail | Evidence |
|--------|--------|----------|
| **Dominant tradition** | Six editors at United Kingdom universities (Sheffield Hallam, King's College London, Queen's Belfast, Glasgow, Reading, Nottingham) and a social media editor at Brunel University London on the live board page; 66 board members, 33 of them in the United Kingdom, plus a Chair and a Vice-Chair (counts under Editorial-board geography). The page lists no disciplines | https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/editorialboard.html (live, counted 2026-11-24); https://bera.ac.uk/?p=43438 ; https://shura.shu.ac.uk/34874/1/Final_BERJ%20Editorial.pdf ; retrieved 2026-11-23 |
| **Review model** | Double-blind; usually at least two anonymous reviewers; editors may reject before review | https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html (live guidelines, read 2026-11-24) |
| **Reviewer competence variance** | Blank. One SciRev quality indicator exists, n=4: quality of review reports 4.5 of 5 and difficulty of reviewer comments 4.0 of 5 (difficult); n is too small to infer variance | https://scirev.org/journal/british-educational-research-journal/ |
| **Quantitative mindset bias on qualitative work?** | Blank. No source. Both interview-based and survey or regression work appear (interview 29.6%, survey 17.4%, regression/longitudinal 13.1% of 778 records), which cannot tell how reviewers treat either | Counts in Methodological Preferences |
| **Discourse community signals (editorial board)** | Editors' and board members' institutions as a proxy, not a reviewer list: 6 of 6 current editors at United Kingdom universities and, and, on the live board page (2026-11-24), 41 of 75 listed people in the United Kingdom (33 of 66 board members) and 34 elsewhere; authors, by Crossref affiliation, are from the United Kingdom in 445 of 839 articles (53%), then China 83, Australia 80 and the United States 41. The journal's reviewer list is not on any page read; the 2020 home page invites new reviewers to register with the editorial office (https://web.archive.org/web/20200605034806id_/https://onlinelibrary.wiley.com/journal/14693518) | https://bera.ac.uk/?p=43438 ; https://web.archive.org/web/20240228050059id_/https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/editorialboard.html |

### Sensitive Topics

> Counts are Crossref records (839) with abstracts for 778, title plus abstract, as shares of 778 (lower bounds). "Receptiveness" cells give frequency only; no editorial statement on these topics was found beyond the diversity editorial, so no row is rated High.

| Topic Category | Receptiveness | Evidence |
|----------------|---------------|----------|
| Decolonial / Indigenous | Present, small | 20 of 778 (2.6%) |
| Gender and feminism | Present | 73 of 778 (9.4%) |
| Race and ethnicity | Present | 63 of 778 (8.1%) |
| Sexual and gender minorities | Present, small | 12 of 778 (1.5%) for queer, LGBT, transgender or sexuality |
| Religion | Rare | 14 of 778 (1.8%) |
| Political conflict, migration | Present | "war, conflict, refugee, migra-" 59 of 778 (7.6%); special section on refugee education (https://doi.org/10.1002/berj.3764) |
| AI and technology | Present, rising | "artificial intelligence, AI, ChatGPT, generative, machine learning, algorithm" 66 of 778 (8.5%); three of the five most cited items of the window concern AI (https://doi.org/10.1002/berj.4068, https://doi.org/10.1002/berj.4084, https://doi.org/10.1002/berj.4069) |
| Climate | Present | "climate, sustainab-, Anthropocene, ecolog-" 104 of 778 (13.4%); https://doi.org/10.1002/berj.3816 |
| Inequality, disability, COVID-19 | Frequently published | social class/inequality 128 (16.5%); disability/special needs/inclusion 125 (16.1%); COVID/pandemic 49 (6.3%) of 778 |

### Practical Concerns

| Concern | Detail |
|---------|--------|
| **IRB requirement strictness** | The guidelines list an ethics approval statement among the statements on the title page ("which may include" data availability, funding, conflict of interest, ethics approval, patient consent and permissions) and point to the society's ethical guidelines for educational research (2024-02-01 copy, https://web.archive.org/web/20240201104500id_/https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html). No stricter journal-specific IRB rule was found |
| **Single-author acceptance** | Single-author papers are a minority but regular: 182 of 779 Crossref records (23.4%) published 2021-01 to 2026-11 (https://api.crossref.org/journals/0141-1926/works?filter=from-pub-date:2021-01,until-pub-date:2026-12; retrieved 2026-11-23) |
| **Independent scholar friendliness** | The guidelines give the affiliation as where the work was conducted and state no independent-scholar rule (2024-02-01 copy). No affiliation breakdown was obtained |
| **Data transparency requirement** | The live guidelines list a data availability statement among the statements and say the journal expects supporting data to be deposited in a public archive where possible (https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html, read 2026-11-24); the 2024-02-01 copy added that a data archiving statement is required on all papers, with the dataset cited in the Methods and exceptions for legal or ethical reasons if the editors are told at submission |
| **OPSEC compatibility** | Double-blind: the manuscript must carry no names, affiliations or acknowledgements, and own work is cited in the third person (2024-02-01 copy). Preprints may be posted at any time per the same page, which can reveal identity to reviewers |
| **AI use** | Disclosure required by the publisher; AI cannot be an author (https://www.wiley.com/en-us/publish/article/ai-guidelines/), retrieved 2026-11-23 |
| **Open access and cost** | Hybrid; no submission fee per the society, with optional open access and colour charges (https://www.bera.ac.uk/publication/british-education-research-journal); APC amount not read |
| **Originality screening** | Papers are routinely screened with iThenticate before being considered for peer review (2024-02-01 copy) |

### AI-Research Notes (sources, blanks, and cross-language checks)

**signal_quality (0-5)**: overall 3. Per layer: Crossref keyword counts 4 (778 of 839 records with abstracts, lower bounds); Crossref affiliation-based author countries 3; OpenAlex 1 (scaffold values only; no keyword counts were obtained because the shared rate limit was reached before this entry's queries; the topic table was added on 2026-11-25 from one OpenAlex request); publisher-wide policies 4; journal-specific policies and guidelines 4 (live guidelines, metrics and board pages read in a real browser 2026-11-24, undated; the 2024 Wayback copies, a 2020 home copy and the 2025 editorial from SHURA are kept as labelled older sources); experiential layer 2 (SciRev n=4).

**Method note**: keyword counts use Crossref records (journal-article type, published 2021-01-01 to 2026-11-23, `select` fields DOI, title, abstract, author, page) with Crossref's own abstracts (778 of 839). Matching is case-insensitive over title plus abstract with these regexes (Python `re`, `\b` word boundary at the start): qualitative `\bqualitative`; quantitative `\bquantitative`; interview `\binterview`; survey `\bsurvey|\bquestionnaire`; randomised/experiment `\brandomi[sz]ed|\brandomi[sz]ation|\bRCT\b|\bexperiment`; mixed methods `\bmixed[- ]method`; reviews `\bsystematic review|\bmeta-analys|\bscoping review|\bliterature review`; ethnography `\bethnograph`; case study `\bcase stud`; theory `\btheor(y|ies|etical|ising|izing|ise|ize)\b`; conceptual `\bconceptual`; philosophy `\bphilosoph`; regression/longitudinal `\bregression|\blongitudinal|\bpanel data|\bcohort`; discourse `\bdiscourse`; decolonial/Indigenous `\bdecolon|\bindigenous|\bfirst nations|\bm[aā]ori|\baboriginal`; gender `\bgender|\bfeminis|\bwomen\b|\bgirls\b`; race `\brac(e|ism|ist|ial|ialised|ialized)\b|\bwhiteness|\bblack\b|\bethnic`; class/inequality `\bsocial class|\bworking[- ]class|\binequalit|\bsocio-?economic|\bdisadvantage`; AI `\bartificial intelligence|\bAI\b|\bChatGPT|\bgenerative|\bmachine learning|\balgorithm`; queer `\bqueer|\blgbt|\btransgender|\bsexualit`; religion `\breligio|\bislam|\bmuslim|\bchristian|\bspiritual`; named theorists `\bbourdieu|\bfoucault|\bmarx|\bfreire|\bdewey|\bdeleuze|\barendt|\bhabermas`; climate `\bclimate|\bsustainab|\banthropocene|\becolog`; conflict `\bwar\b|\bconflict|\brefugee|\bmigra`; disability `\bdisabilit|\bspecial (educational )?needs|\bautis|\bdyslexi|\binclusi` plus `(?-i:\bSEND?\b)`, matched case-sensitively as an acronym only (the first version matched `\bSEND?\b` case-insensitively, which also counted the verb "send" and the surname "Sen's": 129 became 125, 16.1%; the same pattern without the acronym gives 124, 15.9%); COVID `\bcovid|\bpandemic`; first person `\b(I|my|we|our)\b` on abstracts. Correction 2026-11-23, same 839 records and 778 abstracts, case-insensitive: policy `\bpolicy\b|\bpolicies\b` 223 (28.7%, reproduces); teacher `\bteachers?\b` 307 (39.5%, reproduces); higher education `\bhigher education\b` 114 (14.7%; adding `|\bHE\b` would add the pronoun "he" and give 115); assessment `\bassessments?\b` 63 (8.1%; the stem `\bassess` gives 110, 14.1%, but also counts the verb in methods sentences). Country counts match country names and abbreviations (for example `\bUK\b`, `\bUSA\b`, `\bUS\b`) in Crossref affiliation name and place strings; affiliations without a country name are unmatched. Some patterns are broad ("black", "conflict", "experiment", "inclusi") and may over-count; others may miss synonyms.

**Sources cited across this entry:**
- https://web.archive.org/web/20240201104500id_/https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html (author guidelines, Wayback copy 2024-02-01)
- https://web.archive.org/web/20191209183236id_/https://onlinelibrary.wiley.com/page/journal/14693518/homepage/forauthors.html (author guidelines, Wayback copy 2019-12-09)
- https://web.archive.org/web/20240228050059id_/https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/editorialboard.html (editorial board, Wayback copy 2024-02-28)
- https://shura.shu.ac.uk/34874/1/Final_BERJ%20Editorial.pdf (editors' editorial, 17 January 2025, Accepted Version, read 2026-11-23)
- https://www.bera.ac.uk/publication/british-education-research-journal (society page; founding year 1975)
- https://web.archive.org/web/20191209034852id_/https://onlinelibrary.wiley.com/page/journal/14693518/homepage/editorialboard.html (older board copy 2019-12-09, superseded)
- https://web.archive.org/web/20200605034806id_/https://onlinelibrary.wiley.com/journal/14693518 (journal home, Wayback copy 2020-06-05)
- https://www.tandfonline.com/journals/cber20 (legacy Taylor & Francis page, Wayback copy 2023-08-20)
- https://www.bera.ac.uk/publication/british-education-research-journal and https://www.bera.ac.uk/?p=326 (society page, read live)
- https://bera.ac.uk/?p=43438 (society news: new editorial team, 2023-07-07)
- https://api.crossref.org/journals/0141-1926 and https://api.crossref.org/journals/0141-1926/works (839 journal-article and 35 journal-issue records 2021-01 to 2026-11)
- https://doi.org/10.1002/berj.4130, https://doi.org/10.1002/berj.3777 and https://doi.org/10.1002/berj.3830 (editorials, via Crossref)
- https://www.wiley.com/en-us/publish/article/ai-guidelines/
- https://authorservices.wiley.com/author-resources/Journal-Authors/licensing/self-archiving.html
- https://scirev.org/journal/british-educational-research-journal/

**Unreadable pages (never filled from memory):**
- None among the journal's own main pages as of 2026-11-24: the guidelines (https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/forauthors.html), the metrics page (https://bera-journals.onlinelibrary.wiley.com/journal/14693518/journal-metrics) and the board page (https://bera-journals.onlinelibrary.wiley.com/hub/journal/14693518/editorialboard.html), all unreadable to curl on 2026-11-23, were read in a real browser; nothing was clicked, and a Cloudflare check on the metrics page cleared on a second navigation. None of the three prints a date. The metrics page prints Clarivate figures, which are deliberately not recorded. The editors' 2025 editorial said the board had 40 members; the live board lists 75 people, so the board has grown or the editorial counted differently. Notes: chrome2/berj-pages.txt in the researcher's scratch folder.
- not read: the Open Access page with this journal's APC and the supplementary-materials page
- Correction 2026-11-23: https://shura.shu.ac.uk/34874/1/Final_BERJ%20Editorial.pdf is not blocked; it was fetched with curl and a browser User-Agent (valid 4-page PDF, about 156 KB), read in full and used above (acceptance rate, desk-rejection reason, reviewer invitations, board size). Still unreadable: https://bura.brunel.ac.uk/bitstream/2438/30866/3/FullText.pdf (connection refused when first tried; not re-tried in this correction), said by a search to be a BERJ editorial; only its Crossref abstract was read

**Fields deliberately left blank, and why:**
- Acceptance rate, desk rejection rate, reviewer culture, reviewer competence variance, quantitative bias: no first-hand source beyond four SciRev reviews; a LetPub page for the title was not located by search.
- APC: the Open Access page was not read.
- Impact factor, quartile: paywalled, not stated by policy. OpenAlex topic table: added on 2026-11-25 from one works-API request (see Subject Density).

**Cross-language and forum checks performed (all returned zero journal-specific first-hand reports):**
- SciRev (English): journal page exists with 4 reviews (https://scirev.org/journal/british-educational-research-journal/).
- LetPub: search for the journal returned LetPub pages for other education titles only; no BERJ page located.
- 小木虫 (muchong) and 知乎 (zhihu): web search "British Educational Research Journal BERJ 投稿 审稿 周期 经验 小木虫 知乎" returned no muchong or zhihu thread; one Chinese journal-listing site (iikx.com) came back.
- fabiaoji: not reached by the web search; not checked directly.
- Reddit: web search for the journal name with "submission experience reviewers desk rejected reddit" returned no Reddit thread. A BERA blog post reporting a 63 per cent desk-rejection rate (https://www.bera.ac.uk/?p=42570) is about a different journal (System) and is not used.

---

## Strategic Notes

> Each statement below follows from a fact recorded above and names it. Where the evidence does not support a statement, the field says so.

### Hard Blockers

- **Anonymisation**: the guidelines require an anonymised manuscript with no names, affiliations or acknowledgements, and own work cited in the third person (Peer Review, Practical Concerns; guidelines copy 2024-02-01). A manuscript that identifies its authors does not meet the stated submission format.
- **Length**: articles should normally be 5000 to 8000 words excluding references (Format). A much longer manuscript departs from the stated norm; whether exceptions are granted is not stated.
- **Data statement**: all papers need a data archiving statement with the dataset cited in the Methods, except where legal or ethical limits are explained to the editors at submission (Practical Concerns).
- **AI use**: undisclosed AI use breaches the publisher policy (AI Policy, https://www.wiley.com/en-us/publish/article/ai-guidelines/).
- **AI use**: the live guidelines require an AI Use Declaration Statement and a detailed description of any non-trivial AI use in the Methods or Acknowledgements (AI Policy; read 2026-11-24). No other hard blocker is supported by a fact read.

### Soft Tax

- **Time**: editors aim for a first decision within 12 weeks (Review Cycle Time); SciRev, n=4, reports 4.0 months total handling for accepted manuscripts and 66 days for an immediate rejection. Both are small-n.
- **Open access cost**: green deposit of the accepted manuscript is subject to an 18-month embargo for this journal (Preprint Policy); gold open access carries an APC whose amount was not read (Open Access).
- **Structure and extras**: a Key Insights box on invited revision, two manuscript files and a separate title page add preparation work (Format).

### Best Suited For

- Empirical education research across policy, teachers and higher education: policy 28.7%, teacher 39.5%, higher education 14.7% and assessment 8.1% of 778 records with abstracts (Orientation).
- Interview-based and survey or longitudinal studies: interview 29.6%, survey 17.4%, regression/longitudinal 13.1% (Methodological Preferences), and conceptual or theoretical papers: theor- 23.4%, conceptual 13.9%; the guidelines explicitly leave structure open for non-empirical research (Format).
- Papers on inequality, disability, gender, race or AI in education: 16.5%, 16.1%, 9.4%, 8.1% and 8.5% of 778 records (Sensitive Topics).
- Authors wanting a referral route: the Wiley Education publishing network may pass a rejected manuscript with its reports to another Wiley journal (Peer Review).

### Not Recommended For

- Papers needing a verified acceptance rate or current turnaround: none was found, and SciRev has only four reviews (Metrics, Review Cycle Time).
- Work in which the identity of authors or a named case institution cannot be removed: double-blind review and the third-person self-citation rule (Peer Review, Format).
- Religion-focused work as a main topic: 14 of 778 records (1.8%) match (Sensitive Topics); this shows low frequency, not rejection.

### Rejection Fallback Chain

> No source states where rejected authors usually go. The rows below are topical neighbours that exist in this corpus, listed only because they share the subject area (general education research); they are not a claim about acceptance odds. The guidelines name a Wiley referral network but not its members, so no Wiley journal is claimed here as a transfer target.

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
| 2026-11-23 | Correction after independent check: founding year 1975 taken from the BERA page; board recounted from the Wayback copy of 2024-02-28 (6 editors, 20 board members, 12 outside the UK), replacing the no-copy statement and readings drawn from the 2019 copy; SHURA editorial PDF read and used (11.5% acceptance in 2024, board of 40); disability count 129 to 125 (16.1%) with the acronym matched case-sensitively; policy, higher-education and assessment counts recomputed with stated regexes (223, 114, 63 of 778) | AI-assisted (maintainer-directed) |
| 2026-11-23 | Promoted to Tier 1 under the written rule: tier1_gate passes; independent spot-check 7 of 7 sampled pairs supported; wrong 'no copy' and founding-date claims corrected; banner removed; no first-hand human reports | AI-assisted (maintainer-authorised, not human-verified) |
| 2026-11-24 | Live Wiley pages read in a real browser: guidelines (word range, abstract, double-blind and preprint rules unchanged; a journal-specific AI paragraph and an AI Use Declaration Statement now present), metrics page (2025 acceptance 11%, first decision median 7 days, acceptance median 154 days, CiteScore 5.2 as labelled) and board page (75 = 6 + 1 + 66 + 1 + 1, was 26 names in the 2024-02-28 copy); 'unreadable' statements replaced; Clarivate figures on the metrics page not recorded | AI-assisted (maintainer-directed) |
| 2026-11-25 | Added the OpenAlex Top Topics table (dimension was missing) | @Zaious |
