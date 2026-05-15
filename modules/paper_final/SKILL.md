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

- each figure/table supports a specific claim
- each panel has a distinct function
- caption matches the visual
- values in text match values in figures/tables
- axes, units, legends, colorbars, scale bars, and statistics are complete
- visual style is readable at target size
- source and processing notes stay outside manuscript body

Do not invent missing figures, tables, values, or metadata.

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
