---
name: paper_revision
description: Use this skill when the user needs revision management for an academic manuscript, including reviewer comments, editor decisions, response letters, revision history, diff comparison, change logs, point-by-point response drafting, reviewer-action mapping, resubmission packages, or records of manuscript changes.
---

# Paper Revision Management

## Purpose

Manage manuscript revision work without mixing revision notes into the manuscript body.

## I/O Contract

Consume reviewer/editor comments, manuscript versions, and optional `paper_type_output`. Produce `paper_revision_output`.

Use `../../references/module_io_schemas.md` for the compact handoff shape.

Use for:

- editor decision letters and reviewer comments
- point-by-point response letters
- author rebuttal or response drafting
- revision history and change logs
- diff comparison between manuscript versions
- mapping reviewer comments to manuscript actions
- resubmission package planning

## Inputs

- editor decision letter
- reviewer comments
- previous and revised manuscript versions
- author notes or planned changes
- line numbers, page numbers, figure/table references
- journal instructions for revisions
- `paper_type_output` when target venue, article type, or template rules affect response style

## Workflow

1. Preserve every editor and reviewer comment faithfully.
2. Assign stable IDs such as `E.1`, `R1.1`, `R1.2`, and `R2.1`.
3. Classify each comment by concern type, severity, evidence need, and required action.
4. Map each comment to a manuscript change, analysis, citation, explanation, or unresolved item.
5. Draft a professional response only from verified changes and supplied facts.
6. Produce revision artifacts separately from manuscript body.

## Action Types

- `ACCEPT_TEXT`: revise wording or explanation.
- `ACCEPT_ANALYSIS`: add analysis, experiment, table, or figure if provided or confirmed.
- `ADD_CITATION`: add or replace citation support.
- `SOFTEN_CLAIM`: weaken unsupported or overbroad claims.
- `CLARIFY_SCOPE`: explain boundary or limitation.
- `DISAGREE_WITH_REASON`: respectfully disagree with evidence or scope reasoning.
- `AUTHOR_INPUT_NEEDED`: missing information prevents a truthful response.

## Required Outputs

Use these files or equivalent report sections when generating artifacts:

- `revision_log.md`
- `reviewer_comment_map.md`
- `response_draft.md`
- `diff_summary.md`

Core table:

| ID | Original Comment | Concern Type | Required Action | Manuscript Location | Status | Response Basis |
|---|---|---|---|---|---|---|

## Rules

- Do not invent reviewer comments, experiments, analyses, citations, line numbers, figure panels, or manuscript changes.
- Do not claim a revision was made unless the user supplied the revised text or confirmed the change.
- Keep tone professional, concise, and non-defensive.
- If reviewers conflict, map the conflict and propose a balanced editor-readable response.
- If a requested experiment is impossible or out of scope, acknowledge the concern and give a scientific or scope-based reason.
- Keep response strategy notes and missing items outside the manuscript body.
