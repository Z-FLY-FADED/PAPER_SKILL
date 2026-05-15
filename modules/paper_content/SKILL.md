---
name: paper-content-writing-polish
description: Use this skill when the user wants to write, rewrite, expand, compress, polish, translate, or academically improve manuscript content after manuscript type, template requirements, outline, source mapping, and terminology rules have been confirmed. It preserves technical meaning, avoids hallucination, checks logic, supports Nature-style writing, and performs citation-aware claim review.
---

# Academic Content Writing and Polishing

## Purpose

Write and improve academic manuscript content while preserving evidence, technical meaning, and confirmed constraints.

## I/O Contract

Consume `paper_type_output` and, for non-local tasks, `paper_plan_output`. Produce `paper_content_output`.

Use `../../references/module_io_schemas.md` for the compact handoff shape.

Use for:

- titles, abstracts, keywords, introductions, methods, results, discussion, conclusion
- Chinese-English academic translation
- Nature-style or SCI-style polishing
- expansion, compression, restructuring, and logical improvement
- reviewer-risk and overclaim checks
- citation-aware writing and claim segmentation

## Pre-Writing Gate

Before major writing, confirm:

- manuscript type, target venue, language, and length
- outline and section role
- source-to-section mapping
- terminology, notation, and reference style
- available figures, tables, equations, datasets, and citations
- missing evidence and unsupported claims

For small paragraph polishing, proceed if the task is clear, but preserve meaning and report uncertainty outside the manuscript body.

## Fast-Track Mode

Use `fast_track=true` for:

- one grammar fix in one sentence
- one phrase translation
- one short paragraph polishing
- title refinement
- one citation-support question
- one caption adjustment
- one reference punctuation issue
- short translation
- local clarity or tone improvement

Do not use fast-track for a full abstract rewrite, section rewrite, multi-reference audit, full manuscript formatting, or thesis chapter work.

Fast-track skips full type and outline gates, but it must still:

- preserve technical meaning, numbers, citations, and terminology
- avoid inventing data, references, mechanisms, or results
- keep assumptions and uncertainty outside manuscript body
- report any claim that cannot be supported by the provided text

Fast-track output must include:

| Checks performed | Checks skipped | Residual risk |
|---|---|---|

## Core Workflow

1. Identify the target section and its function.
2. Extract the claim, evidence, boundary, and intended reader takeaway.
3. Check technical meaning, numbers, notation, and terminology.
4. Check logical chain: gap -> method -> evidence -> conclusion.
5. Check reviewer risk and overclaim risk.
6. Draft or revise the text.
7. Keep manuscript body clean.
8. Put missing items, assumptions, and audit notes in a separate report.

## Nature-Style Writing Rules

- Write the argument before writing sentences.
- Use the hourglass pattern when suitable: broad context -> gap -> question -> approach -> evidence -> implication.
- Results should report what was observed, under what conditions, and with what evidence.
- Discussion should explain meaning, relation to prior work, limitations, and boundary.
- Abstracts should follow one clear pattern: challenge -> contribution -> evidence -> implication.
- Methods papers must emphasize reproducibility, fair comparison, datasets, metrics, parameters, and validation.
- Use ambitious but bounded claims.
- Avoid unsupported novelty, causality, clinical relevance, or generality.
- Prefer clear sentences of roughly 10-30 words in polished English.
- Avoid em dashes by default unless the user requests that style.

## Citation-Aware Writing

When adding or checking citations:

- Split text into citable segments with stable IDs such as `S001`.
- Extract the exact claim in each segment.
- Search using English concept queries when needed, even for Chinese input.
- Classify support as `strong support`, `partial support`, `background support`, `contradictory/limiting`, or `metadata-only candidate`.
- Do not cite a paper as support only because its title is related.
- Prefer primary sources for data, methods, and direct conclusions.
- If support is weak, weaken the claim, replace the citation, or mark missing evidence in a report.
- Require a direct quoted source sentence, extracted data, or precise source statement for every support judgment.
- If no source sentence or data can be extracted, the maximum support level is `partial support` unless the user confirms full-text evidence.

### Citation Support Decision Tree

Use this deterministic tree:

1. If the source directly tests or reports the same claim, relationship, result, method, population/data, and conclusion, classify as `strong support`.
2. If the source supports a similar relationship or method but differs in dataset, species, population, condition, metric, implementation, or scope, classify as `partial support`.
3. If the source only establishes field context, motivation, prior terminology, or general background, classify as `background support`.
4. If the source only has title/topic overlap or requires unsupported extrapolation, classify as `weak/not suitable`.
5. If the source narrows, contradicts, or limits the manuscript claim, classify as `contradictory/limiting`.

Citation audit rows must use:

| Claim | Candidate Source | Source Evidence Quote/Data | Support Level | Reason | Required Action |
|---|---|---|---|---|---|

## Manuscript Body Separation

Manuscript body must not contain:

- planning notes
- source-processing notes
- `Missing`, `Unverified`, or `User confirmation required`
- software or extraction logs
- audit comments
- old source file names
- notes about where material came from

Use separate reports such as:

- `missing_items_report.md`
- `source_mapping_report.md`
- `citation_support_report.md`
- `logic_gap_report.md`
- `overclaim_risk_report.md`

## No Hallucination Rules

Never invent:

- data, results, experiments, simulations, metrics, datasets, parameters, hardware, statistics, or comparisons
- formulas, figures, tables, references, DOI, publication metadata, or reviewer comments
- claims not supported by the user's material

If information is unavailable, report it separately and ask for confirmation when needed.
