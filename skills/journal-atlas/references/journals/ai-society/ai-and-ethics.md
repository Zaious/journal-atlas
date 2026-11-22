<!-- schema: v1.3 -->
<!-- AI-researched entry — Journal Atlas v2 coverage pipeline. See docs/ATLAS_V2_DESIGN.md for methodology. -->
<!-- Scaffold written by hand on the section structure of an existing finished entry, with Identity and Metrics from the OpenAlex-derived spine snapshot (2026-07-13) and Crossref, because the live OpenAlex daily budget was exhausted on 2026-11-23; policy and count evidence added by hand on 2026-11-23. -->

# AI and Ethics

> **Last verified**: 2026-11-23
> **Maintainer**: @Zaious
> **Venue type**: Journal
> **Evidence basis**: Tier 1 under the written rule (SEED_DATA_QUALITY.md): deeper per-journal research by an AI model, directed by the maintainer, 2026-11-23; overall signal_quality **3/5**. Claims cite source URLs or counts; blanks are recorded with reasons. Independent spot-check on 2026-11-23: 8 supported and 2 partial of 10 sampled pairs over two independent rounds. No first-hand human reports; not human-verified.

---

## Identity

| Field | Value |
|-------|-------|
| **Abbreviation** | not stated on the pages read |
| **Venue type** | Journal |
| **Publisher** | Springer Nature (Springer-Verlag in Crossref); page footer reads "Springer Nature Switzerland AG" — https://web.archive.org/web/20260910030133/https://link.springer.com/journal/43681 (archive 2026-09-10) |
| **ISSN (Print)** | 2730-5953 (Crossref https://api.crossref.org/journals/2730-5953, retrieved 2026-11-23) |
| **ISSN (Online)** | 2730-5961 (same Crossref record and the journal homepage) |
| **Founded** | not stated on the pages read; the Crossref journal record shows 29 DOIs issued in 2020 and 92 in 2021 (https://api.crossref.org/journals/2730-5953, retrieved 2026-11-23), so output started in 2020 |
| **URL** | https://link.springer.com/journal/43681 |
| **Author / Submission Guidelines** | https://link.springer.com/journal/43681/submission-guidelines (the live page redirects through a cookie handshake; a cookie-aware client (curl -sL with a cookie jar) reads it. Re-read live on 2026-11-23: the abstract (150 to 250 words), keyword (4 to 6), LLM-authorship, copy-editing and double-blind statements still hold, and the only word count on the page is the abstract limit. Facts below that are not marked otherwise were first read in the archive copy of 2025-12-05) |
| **Society / Association** | none stated on the pages read; the "Journal updates" menu lists an announcement of cooperation with the AI Asia Pacific Institute and an annual best human-centred AI paper award (homepage, archive 2026-09-10); the content of those updates was not read |
| **Editorial Board Location** | CH (OpenAlex country code in spine); the two Editors-in-Chief list affiliations in the United Kingdom and the United States (editorial board page, archive 2025-12-04: https://web.archive.org/web/20251204162417/https://link.springer.com/journal/43681/editorial-board) |
| **OpenAlex ID** | not recorded (live OpenAlex lookup unavailable on 2026-11-23) |

---

## Metrics

> Source: OpenAlex-derived spine snapshot 2026-07-13 (h-index, 2-yr mean citedness, works count) + JUFO + Norwegian Register; the journal's own speed figure (archived homepage); Crossref (counts and publication-history dates, retrieved 2026-11-23). JCR impact factor and quartile are paywalled and not stated here.

| Metric | Value | Date |
|--------|-------|------|
| **Impact Factor** | not stated (JCR is subscription-only) | |
| **5-Year IF** | not stated (JCR is subscription-only) | |
| **h-index** | 63 | 2026-07-13 (OpenAlex, via spine) |
| **2-Year Mean Citedness (OpenAlex IF proxy)** | 5.20 — an OpenAlex proxy on 1,195 total works; not comparable to a JCR impact factor | 2026-07-13 (OpenAlex, via spine) |
| **Total Works** | 1,195 (OpenAlex, spine snapshot). Crossref's journal record states 1,409 total DOIs, while the works endpoint returned 1,482 journal-article records for 2021-01-01 to 2026-11-23 (the counts differ and the discrepancy was not resolved; the journal record may lag the works index) | 2026-07-13 / 2026-11-23 |
| **CiteScore** | not stated (Scopus not read) | |
| **Acceptance Rate** | The journal publishes no acceptance rate on the pages read. | 2026-11-23 |
| **Desk Rejection Rate** | no percentage published; the journal homepage shows a median of 4 days from submission to first decision (archive 2026-09-10: https://web.archive.org/web/20260910030133/https://link.springer.com/journal/43681), a figure the page does not define | archive 2026-09-10 |
| **Quality-tier facts (not JCR/SJR quartile)** | JUFO (Finland): level 1; Norwegian Register: level 1; no CAS 中科院分区 row in the spine; not in DOAJ (hybrid journal) | 2026-07-13 (spine) |

### Review Cycle Time

> Three kinds of figure are given and they differ: the journal's own median, publisher-deposited dates measured from Crossref (accepted papers only, so a lower bound on a typical submitter's wait), and user-reported experience (none found).

| Stage | Typical Time | Notes |
|-------|-------------|-------|
| **Time to first decision** | Journal's own median: 4 days (homepage "Journal metrics", archive 2026-09-10) | Self-reported; the page does not say whether desk rejections are included |
| **Time to first review** | not available: SciRev has no page for this journal (https://scirev.org/journal/ai-and-ethics/ returned HTTP 404 on 2026-11-23); no LetPub page was found | |
| **Time to acceptance (total)** | Crossref publication-history dates, n=1,417 accepted articles (2021 to 20 Nov 2026) with both received and accepted dates: received to accepted median 98 days (interquartile range 60 to 138; range 0 to 549). By first-online year: 2021 median 70.5 days (n=84); 2022 90 (n=122); 2023 85 (n=132); 2024 104 (n=214); 2025 109 (n=283); 2026 100 (n=582). | https://api.crossref.org/journals/2730-5953 |
| **Time to publication (after acceptance)** | Crossref dates, n=1,423: accepted to first online median 22 days (interquartile range 14 to 35; range 3 to 220). | Online publication date |

### Publication Frequency

| Aspect | Detail |
|--------|--------|
| **Schedule** | Continuous online publication with article numbers; the homepage of archive 2026-09-10 lists articles numbered 501 to 505 published on 7 to 9 September 2026. |
| **Articles per year (approx.)** | Crossref journal-article records by first-online year: 2021 92; 2022 125; 2023 141; 2024 244; 2025 289; 2026 to 20 Nov 591 (total 1,482). Output more than doubled between 2023 and 2025 and 2026 is already double 2025. |
| **Special issues?** | Yes: topical collections run alongside regular submissions. The homepage (archive 2026-09-10) lists two open calls: one on participatory AI co-design (deadline 7 October 2026) and one on AI ethics for children and adolescents (deadline 30 November 2026). Guest editors handle those papers and assign at least two referees; the Editors-in-Chief make the final decision (submission guidelines, archive 2025-12-05). |

---

## Policies

### Peer Review

| Aspect | Detail |
|--------|--------|
| **Type** | Double-blind: authors stay anonymous to reviewers; the author must anonymise the manuscript and associated files, and a separate title page carries names and affiliations. Authors should avoid citing their own work in a way that reveals identity. https://web.archive.org/web/20251205033213/https://link.springer.com/journal/43681/submission-guidelines |
| **Transferable / Cascade?** | not stated on the pages read |
| **Reviewer reports published?** | Not mentioned; reviewers are anonymous. |
| **Typical R+R rounds** | Not stated as a number. The guidelines say suggested major revisions are commonly re-evaluated by the original referees while minor revisions are often handled by the Associate Editor and Editors-in-Chief alone (same page). |
| **Reviewer recommendations** | Manuscripts are usually reviewed by two referees plus one Associate Editor; no article is accepted without two complete and final reviews; Associate Editors are chosen by the Editors-in-Chief, referees are invited by the Associate Editors, and only the Editors-in-Chief can make the final accept or reject decision (same page). Editorial-board members may submit, with the handling editor and referees kept confidential. |

### AI Policy

| Aspect | Detail |
|--------|--------|
| **Has journal-specific AI policy?** | Yes, in the submission guidelines: large language models such as ChatGPT do not meet authorship criteria because accountability cannot be assigned to them (archive 2025-12-05). Springer Nature's house policy adds a framework (below). |
| **Explicit permission gate?** | conditional — use is allowed but must be documented. |
| **Leniency (1-5)** | 3 |
| **Summary** | Use of an LLM is to be documented in the Methods section, or a suitable alternative part if there is none. The guidelines say "AI assisted copy editing" (language, grammar, style improvements to human-written text) does not need to be declared, but human accountability for the final text is required. The Springer Nature page "AI use in manuscript preparation" (retrieved 2026-11-23: https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation) groups uses into low risk (language editing, translation), a middle tier requiring clear labelling (drafting sections, outlines) and a not-permitted tier (listing AI as an author, generating results or interpretations without oversight). The leniency score is this atlas's own 1-5 convention. |
| **Source URL** | https://web.archive.org/web/20251205033213/https://link.springer.com/journal/43681/submission-guidelines |

### Preprint Policy

> Source: Springer Nature's journal-policies page, "Preprint sharing" section (retrieved 2026-11-23: https://www.springer.com/gp/editorial-policies/preprint-sharing, which redirects to https://link.springer.com/brands/springer/journal-policies). No journal-specific preprint paragraph was found on the guidelines page.

| Stage | Allowed? | Notes |
|-------|----------|-------|
| Pre-submission | Yes (publisher policy) | Springer Nature encourages preprints on servers of the authors' choice. |
| Under review | Yes under the publisher policy, which says preprints may be posted at any time during peer review and are not prior publication | The journal reviews double-blind, and a public preprint can reveal authors (inference, not a journal statement); the guidelines page does not say how the two interact. |
| Post-acceptance (AAM) | not stated for this journal | Hybrid journal: the author chooses subscription or open access after acceptance (How to publish with us, archive 2025-12-05). |
| Version of Record | Open access (CC BY or CC BY-NC-ND) if the author pays the APC; otherwise subscription | https://web.archive.org/web/20251205041211/https://link.springer.com/journal/43681/how-to-publish-with-us |

### Open Access

| Aspect | Detail |
|--------|--------|
| **Model** | Hybrid: after acceptance the author chooses subscription publishing (no APC) or open access with an APC; open access articles are CC BY or CC BY-NC-ND 4.0 and authors keep copyright (How to publish with us, archive 2025-12-05). The homepage counts 695 open access articles (archive 2026-09-10). |
| **APC (if OA chosen)** | The journal page lists £2,290 / $3,190 / €2,590 plus any VAT (archive 2025-12-05). The OpenAlex-derived spine shows 2,890 USD for the same journal, which differs from the journal's own USD figure; the journal page is the better source and may itself have changed since the archive date. https://web.archive.org/web/20251205041211/https://link.springer.com/journal/43681/how-to-publish-with-us |
| **Read & Publish agreements** | The page points to Springer Nature open access agreements with institutions and a funding-eligibility check; whether this journal is covered depends on the institution and was not checked. |

---

## Format

> Sources: archived submission guidelines (https://web.archive.org/web/20251205033213/https://link.springer.com/journal/43681/submission-guidelines, snapshot 2025-12-05). The page says the journal recently switched submission and peer review system and that the guidelines were being revised, so check the live guidelines before submitting.

| Aspect | Detail |
|--------|--------|
| **Article types accepted** | The guidelines page gives no formal list of article types, but it mentions some in passing: "non-research articles (e.g. Opinion, Review, and Commentary articles)" in the citation guidance, and "editorials, book reviews, comments" among types that may need a disclosure statement (archive 2025-12-05: https://web.archive.org/web/20251205033213/https://link.springer.com/journal/43681/submission-guidelines). The homepage labels recent items "Research" and "Review" (archive 2026-09-10); the contents of any other type were not read. |
| **Word limit** | None stated on the guidelines page (searched for "words": only the abstract limit appears). |
| **Word limit negotiability** | not stated |
| **Abstract limit** | 150 to 250 words, with no undefined abbreviations or unspecified references. Keywords: 4 to 6. |
| **Reference limit** | No numeric limit stated; reference entries are numbered consecutively, DOIs as full links are requested where available, and journal names are abbreviated per the ISSN list. |
| **Supplementary material** | A "Supplementary Information (SI)" section exists in the guidelines; its rules were not extracted. |
| **Figure/Table limits** | No more than three levels of headings; footnotes rather than endnotes; figure widths follow Springer's column widths. Required "Statements and Declarations" section (competing interests, funding, author contributions and others); the guidelines say submissions without relevant declarations are returned as incomplete. Author contributions and competing interests are entered in the submission system, not in the manuscript. Manuscripts are submitted as .docx or LaTeX, with a separate title page. |

---

## Subject Density

> Source: OpenAlex per-source topics (spine snapshot 2026-07-13). These are OpenAlex topic-assignment counts, all-time and not a 5-year window; a work can carry several topics, so counts are not additive and are not article counts.

### Top Topics

| Topic | Topic-assignment count |
|-------|------------------------|
| Ethics and Social Impacts of AI | 800 |
| Artificial Intelligence in Healthcare and Education | 320 |
| Neuroethics, Human Enhancement, Biomedical Innovations | 234 |
| Explainable Artificial Intelligence (XAI) | 182 |
| Psychology of Moral and Emotional Judgment | 162 |
| Adversarial Robustness in Machine Learning | 88 |
| Law, AI, and Intellectual Property | 61 |
| Blockchain Technology Applications and Security | 56 |
| AI in Service Interactions | 56 |
| Digital Economy and Work Transformation | 43 |

### Orientation

> Counts below come from keyword searches over title plus abstract of Crossref-deposited journal articles published 2021-01-01 to 2026-11-20 (1,482 records, of which 684, or 46.2%, carry an abstract). Hits are counted among records with abstracts only, so every count is a lower bound; percentages divide by 684. Hits are not mutually exclusive.

| Dimension | Assessment |
|-----------|------------|
| **Empirical vs. Theoretical** | Conceptual or normative wording ("conceptual analysis", "philosoph", "normative", "we argue", "argue that") appears in 241 of 684 abstracts (35.2%); the word "empirical" in 65 (9.5%); experiment, randomised or vignette designs in 27 (3.9%). The aims page says submissions whose contribution is descriptive or empirical without normative engagement are out of scope (https://web.archive.org/web/20261106205802/https://link.springer.com/journal/43681/aims-and-scope). |
| **Quantitative vs. Qualitative** | Both appear in small shares: survey or questionnaire 35 (5.1%); qualitative, thematic or content analysis, focus group 52 (7.6%); interview 32 (4.7%); mixed methods 6 (0.9%); case study 40 (5.8%); systematic, scoping or literature review 36 (5.3%). |
| **Cross-disciplinary openness** | The aims page (snapshot 2026-11-06) says the journal brings together computer science, engineering, law, philosophy, social science and policy; technical papers with no ethical analysis are out of scope; the technical-vocabulary share is 148 of 684 abstracts (21.6%). |

**Current positioning (what the journal accepts now):** The aims page of archive 2026-11-06 says every manuscript must engage substantively with an ethical dimension of AI, either as the central contribution or through a substantial, reasoned discussion. It names three exclusions: primarily technical work without ethical analysis, descriptive or empirical societal-effects work without normative engagement, and passing mention of ethics. It also says the journal differs from "AI and Society" publications and purely philosophical venues. Its listed topics include foundation models and generative AI, agentic systems, governance and regulation including the EU AI Act, fairness, safety, human-in-the-loop, AI literacy, privacy, healthcare, labour, law and rights, AI companionship, and synthetic media.

**Methods noted as welcome:** no method is named on the aims page; the page frames scope by normative engagement, not by method.

---

## Soft Metadata

### Epistemological & Political Leanings

- Aims page (archive 2026-11-06): the journal places the ethical dimension itself at the centre and asks for a position on "what is right, fair, harmful, or just" defended with reasoning, evidence or cases. https://web.archive.org/web/20261106205802/https://link.springer.com/journal/43681/aims-and-scope
- Theory vocabulary in the 684 abstract-bearing Crossref records (2021-2026): principles, guidelines or trustworthiness 190 (27.8%); sociotechnical or STS 40 (5.8%); decolonial, postcolonial, Global South or colonial 18 (2.6%); critical theory, power asymmetry, Marxism or capitalism 17 (2.5%); capabilities or justice theories 17 (2.5%); virtue ethics or Aristotle 16 (2.3%); consequentialism or utilitarianism 14 (2.0%); Kant or deontology 10 (1.5%); feminist 7 (1.0%); phenomenology or Heidegger 7 (1.0%); care ethics 2 (0.3%); Floridi or information ethics 1 (0.1%). Principle-based and governance framing dominates; named ethical traditions each appear in 1 to 2% of abstracts.
- Most-cited records of the window by Crossref citation count (retrieved 2026-11-23): 10.1007/s43681-021-00096-7 (1,364, AI in education, K-12 ethical challenges), 10.1007/s43681-021-00043-6 (885, sustainable AI), 10.1007/s43681-024-00653-w (364, AI governance systematic review), 10.1007/s43681-022-00209-w (356, "The uselessness of AI ethics"), 10.1007/s43681-021-00041-8 (327, autonomous-vehicle acceptance review).
- Political and economic framing appears in several topics: bias, fairness or discrimination 206 of 684 abstracts (30.1%); governance 133 (19.4%); law or regulation 175 (25.6%); labour or work 69 (10.1%).
- Board composition (editorial board page, archive 2025-12-04; per-entry recount on 2026-11-23, replacing an earlier string count): 103 board entries plus two Editors-in-Chief. Each entry's country is the last comma-separated item of its affiliation line: United States 41, United Kingdom 22, India 5, Spain 4, Italy 3, China 3, The Netherlands 3, Australia 3, and 14 further place names with 2 or fewer entries each (one of them "Georgia" as written on the page, which could be the US state) plus one entry with no country. Affiliation split by a crude keyword rule (case-insensitive match of university, institut, college, school, academy, polytechnic, hochschule, universidad, université, universität, research cent, laborator in the affiliation line): 57 entries match and 46 do not (mostly companies, consultancies, non-profits and independent consultants); an independent recount with a slightly different rule gave 54 versus 48 of 102, so the split is keyword-dependent and is roughly half and half. https://web.archive.org/web/20251204162417/https://link.springer.com/journal/43681/editorial-board

### Framing Requirements

- **Mandatory framing?** Yes, stated outright: the aims page (archive 2026-11-06) calls the AI-ethics connection a "core requirement" and gives self-check questions (does the paper take a position on what is right, fair, harmful or just, and defend it). https://web.archive.org/web/20261106205802/https://link.springer.com/journal/43681/aims-and-scope
- **Article-type framing:** the homepage labels items "Research" and "Review" (archive 2026-09-10, items numbered 501 to 505); the guidelines page gives no formal type list but mentions Opinion, Review and Commentary articles, editorials, book reviews and comments in passing (archive 2025-12-05: https://web.archive.org/web/20251205033213/https://link.springer.com/journal/43681/submission-guidelines). https://web.archive.org/web/20260910030133/https://link.springer.com/journal/43681
- **Declarations:** a "Statements and Declarations" section is required, and submissions without relevant declarations are returned as incomplete (guidelines, archive 2025-12-05: https://web.archive.org/web/20251205033213/https://link.springer.com/journal/43681/submission-guidelines).
- **Topics of interest named:** foundation models and generative AI, agentic systems, governance and regulation, fairness, safety, human-in-the-loop, AI literacy, privacy and surveillance, healthcare, labour, law and rights, AI companionship, synthetic media (aims page, same URL as above).
- **Consequences of ignoring it:** the aims page says submissions without substantive ethical engagement are out of scope; what happens procedurally (desk rejection or redirection) is not described on the pages read.

### Methodological Preferences

> Scoring rule applied (this pass's own convention): hits divided by the 684 Crossref records with abstracts (2021-01-01 to 2026-11-20, keyword in title or abstract) = 0 gives 0; under 1% gives 1; 1% to 5% gives 2; over 5% gives 3. A 4 or 5 needs a cited editorial statement. Counts are lower bounds because 53.8% of records have no deposited abstract, and they show how often a method appears, not how reviewers treat it.

| Method | Receptiveness (0-5) | Evidence |
|--------|---------------------|----------|
| Conceptual / normative argument | 5 | 241 of 684 abstracts (35.2%); the aims page makes a normative position the central test of scope (archive 2026-11-06: https://web.archive.org/web/20261106205802/https://link.springer.com/journal/43681/aims-and-scope). |
| Systematic / scoping / literature review | 3 | 36 of 684 abstracts (5.3%); one of the top-cited records is a systematic review (10.1007/s43681-024-00653-w). |
| Case study | 3 | 40 of 684 abstracts (5.8%). |
| Qualitative (interviews, thematic or content analysis, focus groups) | 3 | 52 of 684 abstracts (7.6%); interview wording alone 32 (4.7%, score 2). |
| Survey / questionnaire | 3 | 35 of 684 abstracts (5.1%), a borderline case. |
| Stakeholder, Delphi or participatory methods | 3 | 84 of 684 abstracts (12.3%); an open topical collection concerns participatory co-design (homepage, archive 2026-09-10). |
| Quantitative experiment (randomised or vignette) | 2 | 27 of 684 abstracts (3.9%). |
| Mixed methods | 1 | 6 of 684 abstracts (0.9%). |
| Technical / algorithmic contribution | 3 by count, capped by scope | 148 of 684 abstracts (21.6%) use algorithm, benchmark or model vocabulary, but the aims page excludes primarily technical contributions with no substantive ethical analysis. |
| Autoethnography, design-based research, structural equation modelling | not counted | not searched in this pass; no evidence either way. |

### Voice & Style

- Guidelines (archive 2025-12-05): abstract of 150 to 250 words, 4 to 6 keywords, no more than three heading levels, footnotes not endnotes, numbered references with DOI links, a separate title page for anonymous review. https://web.archive.org/web/20251205033213/https://link.springer.com/journal/43681/submission-guidelines
- Measured abstract length over the 684 abstracts: median 197 words (range 47 to 497), so most sit inside the stated 150 to 250 band.
- First person: 481 of 684 deposited abstracts (70.3%) contain we, our, us, I or my (Crossref, 2021-2026; a heuristic that also catches "our lives" and similar); 457 (66.8%) use "this paper", "this article", "this study" or "this essay" framing. The 10 most recent abstracts retrieved (published 2026, for example 10.1007/s43681-026-01527-z, 10.1007/s43681-026-01516-2, 10.1007/s43681-026-01496-3) open with a topic-level statement, not "we" or "I"; 10.1007/s43681-026-01496-3 describes itself as a "hybrid essay".
- No style guide beyond the Springer house rules is stated; tone of the argument is not specified on any page read.

### Reviewer Pool Characteristics

- Review model: double-blind; usually two referees plus one Associate Editor; two complete final reviews required before acceptance; only the Editors-in-Chief can accept or reject (guidelines, archive 2025-12-05). https://web.archive.org/web/20251205033213/https://link.springer.com/journal/43681/submission-guidelines
- Board page (archive 2025-12-04): two Editors-in-Chief and about 100 editorial board members (the page lists 103 board entries, 102 carrying a "PhD" marker and one without, plus the two Editors-in-Chief; recounted 2026-11-23), with the geographic and affiliation split recorded under Epistemological & Political Leanings; by the keyword rule above, 57 of 103 entries are affiliated with a university or institute and 46 with industry, consultancies, non-profits or independent work. https://web.archive.org/web/20251204162417/https://link.springer.com/journal/43681/editorial-board
- Observed output (OpenAlex-derived spine, 2026-07-13): "Ethics and Social Impacts of AI" (800 topic assignments) dominates, followed by AI in healthcare and education (320) and neuroethics (234), which indicates the subject areas reviewers are drawn from.
- Reviewer behaviour itself (tone, competence variance, quantitative bias) is not observable from public pages; SciRev has no page for this journal (HTTP 404 on 2026-11-23) and no LetPub page or first-hand report was found.

### Sensitive Topics

> Counts are keyword hits in title or abstract among 684 Crossref abstract-bearing records (2021-2026). Receptiveness is "High" only where the journal's own aims page or an open call names the topic, "Medium" for 1% or more of the window without such a statement, and "Low" under 1%. The aims page does not state a stance on any topic beyond naming it as in scope.

| Topic Category | Receptiveness | Evidence |
|----------------|---------------|----------|
| Bias, fairness, discrimination | High | 206 of 684 abstracts (30.1%); named in the aims page (fairness, bias, discrimination across social groups). |
| Gender | High | 35 of 684 (5.1%); the homepage overview lists "discrimination and unfairness with respect to race and gender" as examples of harm (archive 2026-09-10). |
| Race / ethnicity / indigenous | High | 17 of 684 (2.5%); same overview sentence. |
| Disability | Low | 5 of 684 (0.7%); no editorial statement found. |
| Children and adolescents | High | 12 of 684 (1.8%); an open topical collection on AI ethics for children and adolescents closes 30 November 2026 (homepage, archive 2026-09-10). |
| Healthcare and bioethics | High | 107 of 684 (15.6%); a named topic on the aims page. |
| Surveillance, privacy, data ethics | High | 93 of 684 (13.6%); a named topic on the aims page. |
| Military and autonomous weapons | High | 19 of 684 (2.8%); the homepage overview names weaponization and the aims page names autonomous weapons. |
| Labour and economy | High | 69 of 684 (10.1%); a named topic on the aims page. |
| Generative AI and chatbots | High | 126 of 684 (18.4%); a named topic on the aims page. |
| Environment, climate, sustainability | Medium | 60 of 684 (8.8%); the aims page names environmental and resource ethics of large-scale AI. |
| Democracy and elections | Medium | 45 of 684 (6.6%); the aims page names electoral and civic processes. |
| Copyright and creative work | Medium | 28 of 684 (4.1%); the aims page names consent and intellectual property in training data. |
| Religion and spirituality | Medium | 13 of 684 (1.9%); no editorial statement found. |
| Africa, Asia, Latin America (regional wording) | Medium | 26 of 684 (3.8%); no editorial statement found. |

### Practical Concerns

| Concern | Detail |
|---------|--------|
| **IRB requirement strictness** | The guidelines carry Springer's "Ethical Responsibilities of Authors" and informed-consent sections and state COPE membership; sample consent statements are given (guidelines, archive 2025-12-05: https://web.archive.org/web/20251205033213/https://link.springer.com/journal/43681/submission-guidelines). The journal's separate "Ethics and disclosures" page has no archive copy and was not read. |
| **Single-author acceptance** | No restriction stated; author contribution information must be entered in the submission interface (https://web.archive.org/web/20251205033213/https://link.springer.com/journal/43681/submission-guidelines, archive 2025-12-05). |
| **Independent scholar friendliness** | Provision exists: for temporarily unaffiliated authors the journal records only city and country of residence, not an e-mail address, unless requested (https://web.archive.org/web/20251205033213/https://link.springer.com/journal/43681/submission-guidelines, archive 2025-12-05). |
| **Data transparency requirement** | A data availability statement is required for all original research; sharing in a public repository is strongly encouraged (same page, following Springer Nature's research data policy; https://web.archive.org/web/20251205033213/https://link.springer.com/journal/43681/submission-guidelines). |
| **OPSEC compatibility** | Double-blind with a separate title page; acknowledgements, funding and disclosures go on that page; self-citation that would reveal identity should be avoided (same page). Preprints are allowed during review under the Springer Nature policy (see Preprint Policy). |
| **Fees and OA** | Hybrid: APC £2,290 / $3,190 / €2,590 for open access, or free subscription route; CC BY or CC BY-NC-ND (https://web.archive.org/web/20251205041211/https://link.springer.com/journal/43681/how-to-publish-with-us, snapshot 2025-12-05). |
| **Competing interests** | Required declaration; editorial-board members who are authors must declare it in the interface (guidelines, archive 2025-12-05). |

### AI-Research Notes (sources, blanks, and cross-language checks)

**Overall signal_quality: 3/5.** Layer scores: policy and format 3/5 (guidelines read through an archive copy of 2025-12-05 that the page itself says was under revision; aims page read through a copy of 2026-11-06); soft-metadata counts 3/5 (Crossref counts, keyword-based, only 46.2% abstract coverage, so lower bounds); experiential 1/5 (the journal's own 4-day median and Crossref-derived dates only; no SciRev, LetPub, Chinese-language or Reddit report found).

**Method note:** the live OpenAlex API was out of budget on 2026-11-23 (daily budget used). All keyword counts therefore use Crossref-deposited records (1,482 journal articles, first-online date 2021-01-03 to 2026-11-20), not OpenAlex. The spine snapshot of 2026-07-13 supplies the OpenAlex-derived metrics. Keyword families are regular expressions on title plus abstract and some are broad (for example "framework", "principles", "governance", "health").

**Sources cited across this entry:**
- https://web.archive.org/web/20260910030133/https://link.springer.com/journal/43681
- https://web.archive.org/web/20261106205802/https://link.springer.com/journal/43681/aims-and-scope
- https://web.archive.org/web/20251205033213/https://link.springer.com/journal/43681/submission-guidelines
- https://web.archive.org/web/20251205041211/https://link.springer.com/journal/43681/how-to-publish-with-us
- https://web.archive.org/web/20251204162417/https://link.springer.com/journal/43681/editorial-board
- https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation
- https://www.springer.com/gp/editorial-policies/preprint-sharing
- https://api.crossref.org/journals/2730-5953

**Fields deliberately left blank, and why:**
- **Abbreviation, founding year, society, article-type list, word limit, transferability, R+R round count, supplementary-material rules:** not stated on the pages read.
- **Impact factor, CiteScore, quartile:** paywalled.
- **Special-issue content and the "Ethics and disclosures" page:** no archive copy available for the latter; the topical-collection details were not read beyond the homepage listing.
- **Autoethnography, design-based research, SEM method counts:** not searched.

**Unreadable pages:** cookie-gated pages: https://link.springer.com/journal/43681/submission-guidelines (re-read live on 2026-11-23 with a cookie-aware client; archive 2025-12-05 used for the facts), https://link.springer.com/journal/43681/aims-and-scope and https://link.springer.com/journal/43681 (live pages redirect through a cookie handshake; not re-read live, archive copies used); unreadable: https://link.springer.com/journal/43681/ethics-and-disclosures, /editors and /editorial-policies (no archive snapshot returned by the Wayback availability API on 2026-11-23); https://scirev.org/journal/ai-and-ethics/ (HTTP 404).

**Cross-language and experiential checks performed:**
- SciRev: page for this journal returned 404 (also /reviews/ai-and-ethics/); 0 reviews.
- LetPub: search returned a LetPub page for a different journal (AI & Society); 0 for this journal.
- 小木虫 (muchong) and 知乎: search for the journal name with 投稿, 审稿周期 and 经验 returned 0 posts about this journal; only the publisher and database pages appeared.
- fabiaoji (发表记): search with the ISSN returned 0 results about this journal.
- Reddit: search for submission, review and desk-reject experience returned 0 relevant threads.
- Note: other, similarly named venues exist (for example the journal AI & Society and an independent site called "AI Ethics Journal"); the ISSN 2730-5953 was used to keep them apart.

---

## Strategic Notes

> Each statement below follows from a fact recorded above; the source row is named in brackets.

### Hard Blockers

- The aims page makes substantive ethical engagement a core requirement and excludes primarily technical work, descriptive-only societal studies and passing mention of ethics [Subject Density > Current positioning; Framing Requirements].
- Anonymous submission for double-blind review, with a separate title page and anonymised files, is required [Peer Review > Type].
- A "Statements and Declarations" section and, for original research, a data availability statement must be present [Format > Figure/Table limits; Practical Concerns].
- Any LLM use beyond copy editing has to be documented in the Methods, and an LLM cannot be listed as an author [AI Policy].

### Soft Tax

- Time to acceptance for accepted papers has a median of 98 days from received to accepted, with an interquartile range of 60 to 138 days; the journal's own median to first decision is 4 days [Review Cycle Time].
- Volume and competition: output rose from 141 records in 2023 to 289 in 2025 and 591 so far in 2026 [Publication Frequency], so papers sit among many generative-AI and governance papers (126 of 684 abstracts mention generative AI or chatbots, 18.4%) [Sensitive Topics].
- Open access costs £2,290 / $3,190 / €2,590 if chosen; the subscription route is free but not suitable where a funder requires immediate open access [Open Access].
- No stated word limit and no formal article-type list (the guidelines only mention Opinion, Review, Commentary, editorial, book-review and comment articles in passing), so length and format norms have to be inferred from recent articles [Format].

### Best Suited For

- Normative, conceptual or governance arguments about AI that take a position and defend it [Subject Density > Current positioning; Methodological Preferences: score 5 with editorial statement].
- Empirical, review or case-based work that carries a dedicated, reasoned ethical analysis, since the aims page accepts technical, social, legal or policy topics with that section [Subject Density > Current positioning; Methodological Preferences].
- Work on topics the aims page names: generative AI, agentic systems, fairness, privacy, healthcare, labour, law, AI companionship, synthetic media [Framing Requirements; Sensitive Topics].
- Authors without a university affiliation, since the guidelines provide for recording only city and country [Practical Concerns].

### Not Recommended For

- Papers that mainly describe or measure societal effects of AI without normative engagement; the aims page directs these to AI-and-society or STS venues [Subject Density > Current positioning].
- Primarily technical contributions (new models, benchmarks) [Subject Density > Current positioning; Methodological Preferences].
- Authors who need an immediate open-access licence without paying: only the APC route gives immediate open access [Open Access].

### Rejection Fallback Chain

| Rank | Journal | Why this fallback works |
|------|---------|------------------------|
| 1 | [AI & Society](../hci/ai-and-society.md) | The aims page of this journal itself names "AI and Society" publications as the home for societal-effects work without normative engagement. |
| 2 | [Big Data & Society](big-data-and-society.md) | "Ethics and Social Impacts of AI" is the largest OpenAlex topic for both journals (800 and 327 assignments in the spine snapshot); the spine lists Big Data & Society as double-anonymous. |

---

## Changelog

| Date | Change | By |
|------|--------|----|
| 2026-11-23 | Initial entry: structural fields from OpenAlex-derived spine snapshot (2026-07-13) and Crossref; policies from archived journal pages; counts from Crossref (live OpenAlex unavailable) | @Zaious |
| 2026-11-23 | AI deep research pass; no first-hand human reports | AI-assisted (maintainer-directed) |
| 2026-11-23 | Verifier corrections: Springer cookie redirect reworded (a cookie-aware client reads the live page; guideline facts re-read live) | AI-assisted (maintainer-directed) |
| 2026-11-23 | Verifier corrections: editorial-board counts recounted per entry from the 2025-12-04 archive (US 41, UK 22, Spain 4, Italy 3, Australia 3; 103 entries; affiliation split 57/46 by a stated keyword rule) | AI-assisted (maintainer-directed) |
| 2026-11-23 | Second verifier corrections: statements that the guidelines name no article types softened to: no formal type list, but Opinion, Review and Commentary articles (non-research) and editorials, book reviews and comments are mentioned in passing (archive 2025-12-05) | AI-assisted (maintainer-directed) |
| 2026-11-23 | Promoted to Tier 1 under the written rule: tier1_gate passes; independent spot-check 8 supported and 2 partial of 10 sampled pairs over two independent rounds; banner removed; no first-hand human reports | AI-assisted (maintainer-authorised, not human-verified) |
