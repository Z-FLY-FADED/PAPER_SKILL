---
name: paper-final-quality-audit
description: Use this skill when the user wants a final academic quality audit before submission, defense, revision, or advisor review. It checks proofreading, citations, reference metadata, figure and table quality, figure/table-text consistency, terminology, equations, cross-references, logical risk, reviewer risk, Nature-style readiness, and final revision priority.
---

# Final Quality Audit

## Purpose

Audit an academic manuscript or submission package before delivery. This module finds risks; it does not silently rewrite the manuscript unless the user asks for direct correction.

## I/O Contract

Consume any available prior contracts: `paper_type_output`, `paper_plan_output`, `paper_content_output`, and `paper_document_output`. Produce `paper_final_output`.

Use `../../references/module_io_schemas.md` for the compact handoff shape.

## Audit Scope

- proofreading and academic tone
- Chinese-English abstract consistency and academic abstract structure
- terminology, abbreviation, symbol, unit, and notation consistency
- citation-reference matching
- missing or suspicious reference metadata
- citation support for specific claims
- figure quality, table quality, captions, and numbering
- figure/table-text consistency
- equations, variables, and cross-references
- LaTeX structure and supplementary material if applicable
- logical chain, overclaims, and reviewer-risk issues
- final required revisions and optional improvements
- scoped global terminology, symbol, abbreviation, dataset, method, figure-label, and equation-variable consistency
- journal compliance items such as ethics, competing interests, data availability, code availability, author contributions, funding, acknowledgements, consent, and IRB statements where relevant

## Thesis-Specific Red Flags

For graduate theses, always check and prioritize:

- English abstract not matching the Chinese abstract in method sequence, indicators, or quantitative results.
- English abstracts with overlong sentence chains, inconsistent hyphenation such as "Vehicle- mounted", malformed terms such as "reaction- mechanism", or missing key numbers that appear in the Chinese abstract.
- Abstracts containing work-report or defense-style prose, such as explaining "independent modules", dataset boundaries, or figure/evaluation separation instead of summarizing the study.
- Repeated defensive limitation sentences across chapter endings. If limitations are valid, recommend consolidating them into methods, discussion, or "Limitations and Future Work".
- Repetitive chapter summaries that merely restate preceding sections rather than synthesizing the chapter's central finding.
- Template-like prose with frequent "结果表明", "这说明", "可以看出", "therefore", or repeated paragraph openings. Treat this as a polish risk when it affects readability.
- Long, multi-clause sentences that combine background, methods, results, and caveats. Recommend splitting into direct active statements.
- Overuse of negative framing such as "不是...而是..." and "不应...而应..."; prefer affirmative academic statements.
- Unfilled bilingual cover fields, mojibake in symbol tables, inconsistent abbreviation definitions, or mixed notation for the same variable.
- Repeated definitions of the same core concept across chapters when one notation or model section should define it once.
- Formula-number jumps, blank formulas, bare manual equation numbers, missing figures behind figure references, table captions detached from table bodies, and unresolved cross-references.
- TOC-page mismatch, missing dot leaders, inconsistent section indentation, wrong front-matter numbering, missing headers/footers, and discontinuous page numbering.
- Parser-generated image boundary strings such as `image[[429, 170, 590, 280]]`, `[image]`, or similar OCR/PDF extraction artifacts must not be treated as actual manuscript content until verified against source files and rendered pages. They may be bounding-box metadata from an external parser rather than missing images.
- Contribution or innovation sections that overclaim with unsupported "first", "new", or self-evaluative wording.
- Innovation sections written as slogans, such as "采用...思路", "建立...方法", or "构建...策略", should be checked for objective evidence-facing phrasing.
- Reference-list inconsistencies: partial DOI coverage, missing access dates for online policy documents, mixed Chinese/English punctuation, and ordering that conflicts with the target style.

## Readiness Levels

Use one clear judgment:

1. Ready for submission
2. Minor revision required
3. Major revision required
4. Not usable in current form

## Severity

| Severity | Meaning | Examples |
|---|---|---|
| Fatal | Blocks use or submission | fabricated data, blank formulas, placeholder references, missing central figure, manuscript body contaminated by notes |
| Major | Strongly weakens quality | unsupported claim, weak citation support, figure-text mismatch, missing method details |
| Minor | Fix during polishing | grammar, punctuation, spacing, caption clarity |
| Optional | Improvement only | stronger framing, more concise wording, optional visual simplification |

## Core Workflow

1. Confirm manuscript type, language, target venue, and audit scope.
2. Check body text for contamination and placeholders.
3. Check proofreading, tone, terminology, units, and abbreviations.
4. Check citations and references.
5. Check figure/table quality and consistency.
6. Check equations and cross-references.
7. Check logical chain and reviewer-risk issues.
8. Produce a prioritized audit report.

## Citation Support Audit

For each important claim:

- identify the exact claim
- check whether the cited source directly supports it
- classify support as `strong support`, `partial support`, `background support`, `contradictory/limiting`, or `metadata-only candidate`
- flag title-only relevance
- flag secondary-source overuse when primary evidence is needed
- flag medical, clinical, safety, or policy claims that need current direct evidence
- require a direct quoted source sentence, extracted data, or precise source statement for each support judgment
- if no source sentence or data can be extracted, the maximum support level is `partial support` unless the user confirms full-text evidence

Use this decision tree:

1. `strong support`: same claim, same relationship/result/method, direct evidence, compatible scope.
2. `partial support`: similar claim or method but different dataset, population, species, metric, condition, or scope.
3. `background support`: field context only.
4. `weak/not suitable`: title/topic overlap only or unsupported extrapolation.
5. `contradictory/limiting`: conflicts with or narrows the manuscript claim.

Audit rows must use:

| Claim | Candidate Source | Source Evidence Quote/Data | Support Level | Reason | Required Action |
|---|---|---|---|---|---|

If support is weak, recommend one of:

- replace citation
- weaken claim
- add evidence
- move to background context
- remove claim

## Figure and Table Audit

Check:

- whether suspected image placeholders are present in the source manuscript body, in the LaTeX/DOCX structure, or only in text extracted by an external parser
- whether each referenced image file exists and is nonzero-size
- whether rendered pages visually contain the expected figure rather than only a caption or bounding-box text
- each figure/table supports a specific claim
- each panel has a distinct function
- caption matches the visual
- values in text match values in figures/tables
- axes, units, legends, colorbars, scale bars, and statistics are complete
- visual style is readable at target size
- composite figures do not waste pages: a multi-panel figure should normally fit on one page when it has 4-6 small panels, using a balanced 2x2, 2x3, or similar layout
- subpanels are visually uniform in size and aligned; one oversized panel should not squeeze or marginalize the other panels unless it is intentionally the main panel
- spacing between subpanels is neither cramped nor excessive; excessive white space, caption-only pages, and single small plots occupying a full page should be flagged
- large composite figures are not split awkwardly across pages. If unavoidable and allowed by the template, use continuation captions such as "Figure X (continued)" or the Chinese equivalent, and keep panel labels consistent
- source and processing notes stay outside manuscript body

Do not invent missing figures, tables, values, or metadata.

### Image Placeholder Verification

When a report or extracted text shows items such as `image[[x1, y1, x2, y2]]`, perform this sequence before labeling the manuscript as missing images:

1. Search source files for literal placeholders: `image[[`, `[image]`, `<center>`, or similar artifacts.
2. Inspect figure/table environments or DOCX media relationships to confirm whether a real image is referenced.
3. Verify referenced image files exist and are nonzero-size.
4. Render representative pages to PNG/PDF previews and inspect whether the figure is visible.
5. If the rendered PDF shows the figure, report the issue as an extraction/parser artifact, not a manuscript defect.
6. If only captions or empty frames remain after rendering, classify it as a major/fatal figure-placement defect depending on the importance of the figure.

Include a contact sheet or page-preview artifact in the audit report when file artifacts are requested.

### Composite Figure Layout Audit

When auditing figures in theses or LaTeX/PDF outputs:

1. Identify figures that are likely composites, especially response surfaces, multi-curve comparisons, residual plots, control inputs, and multi-panel performance summaries.
2. Check whether 4-6 panels could be arranged on one page without loss of readability. Prefer 2x2, 2x3, or 3x2 panel grids.
3. If a composite has more than 6-8 panels, recommend splitting it into two separately numbered figures rather than forcing one oversized figure.
4. Check panel dimensions, axis-label readability, legend placement, and white-space ratio in the rendered page.
5. Flag pages where a small figure or caption occupies a full page, unless the template or figure complexity justifies it.
6. For LaTeX source, recommend `subfigure`, `subcaption`, `minipage`, or a pre-composed high-resolution raster only after verifying the rendered result.

## Global Consistency Audit

By default, check only high-priority items:

- acronym definitions
- core method names
- primary dataset names
- key symbols and equation variables
- main figure and table labels

Use user-provided `focus_terms` for deeper checks. Build or infer a compact consistency table:

| Item Type | Preferred Form | Variant Found | Location | Required Action |
|---|---|---|---|---|

Output `global_consistency_report.md` only when file artifacts are requested; otherwise summarize findings in chat or the audit report.

## Article-Type Audit Modes

Use `paper_type_output.article_type_profile` when available. Load `../../references/article_type_requirements.md` only when detailed checks are needed.

- `sci_journal`: structure, word count, reproducibility, recent-reference ratio, self-citation risk, required declarations, figure statistics, cover letter and response letter readiness.
- `conference_paper`: page limit, contribution bullets, datasets, baselines, metrics, ablation, double-blind anonymization, limitations or broader impact, supplement and code readiness.
- `chinese_journal`: Chinese/English title and abstract alignment, 3-8 keywords, funding note, author contributions, GB/T 7714 references, bilingual figure/table captions, ethics and data statements.
- `master_thesis`: front and back matter, 5-7 chapter logic, literature-review depth, originality statement, similarity-risk report template, chapter progression, reference-count targets, defense PPT route.

## Journal Compliance Placeholders

Check whether the target venue requires:

- ethics statement
- consent or IRB approval
- competing interests
- data availability
- code availability
- author contributions
- funding
- acknowledgements
- clinical trial registration or reporting checklist when relevant

Generate placeholders only in a report or submission-material draft. Do not present placeholders as verified manuscript facts.

## Output Format

Findings first:

| Severity | Location | Issue | Why It Matters | Required Action |
|---|---|---|---|---|

Then provide:

- overall readiness level
- required revisions
- optional improvements
- user confirmations needed
- residual risk

For English manuscripts, include concise Chinese explanations for major audit comments when useful for the user.
