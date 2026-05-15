---
name: paper_workflow_controller
description: Use this skill to control academic paper and thesis workflows across PAPER modules, enforce stage gates, support iterative backtracking, produce user-facing status cards, estimate interaction time, prevent planning notes or audit comments from entering manuscript body, and decide whether to route to paper_type, paper_plan, paper_content, paper_document, paper_final, paper_revision, paper_writer, or paper_ppt.
---

# Paper Workflow Controller

## Purpose

Route the task to the smallest relevant module and enforce workflow gates. This module does not write manuscript body text.

## Contract Handoff

When chaining stages, read `../../references/module_io_schemas.md` if contract details are needed. Preserve each module's named output contract and pass it forward as confirmed input. Each stage must emit the mandatory base fields defined there.

Core contract names:

- `paper_type_output`
- `paper_plan_output`
- `paper_content_output`
- `paper_document_output`
- `paper_final_output`
- `paper_revision_output`
- `paper_ppt_output`

Each contract must include `stage`, `status`, `confirmed_inputs`, `outputs`, `missing_items`, `risk_flags`, and `next_recommended_module`, using the required field types and item shapes from `module_io_schemas.md`.

## Controller Actions

Choose exactly one action for each controller decision:

- `next_stage`: continue to the recommended module.
- `back_to_previous_stage`: return to an earlier module because the current stage lacks required inputs.
- `ask_user`: ask a structured question list before proceeding.
- `fast_track`: handle a small local task without full type or outline gates.
- `check_dependencies`: run an environment check before PPTX or other file-generation work.

## Default Route

| User Situation | Next Module |
|---|---|
| Type, target, length, format, or template is unclear | `paper_type` |
| Source materials need mapping or outline planning | `paper_plan` |
| User wants writing, rewriting, polishing, translation, expansion, compression, or logic improvement | `paper_content` |
| User wants citation placement, claim support checking, or reference candidates | `paper_content`, then `paper_final` |
| User wants DOCX, LaTeX, Markdown, figures, tables, equations, reference formatting, or layout | `paper_document` |
| User wants publication-style figures or graphical summaries | `paper_document`, then `paper_final` |
| User wants final submission, defense, or advisor-review audit | `paper_final` |
| User wants a complete paper or thesis in one broad task | `paper_writer`, with gates from `paper_type`, `paper_plan`, and `paper_final` |
| User wants slides, group meeting deck, journal club deck, or paper-to-PPTX | `paper_ppt` |
| User wants revision history, reviewer comments, response letter, diff, change log, or resubmission package | `paper_revision` |
| User wants one sentence or paragraph polished, one title refined, one citation checked, short translation, or minor formatting | `paper_content` or `paper_document` with `fast_track=true` |

## Standard Full Workflow

```text
paper_type -> paper_plan -> paper_content -> paper_document -> paper_final
```

For PPTX:

```text
paper_type or paper_plan if needed -> check_dependencies -> paper_ppt -> optional paper_final-style QA
```

Revision workflow:

```text
paper_revision -> paper_content or paper_document as needed -> paper_final
```

## Stage Dependency Map

Use `back_to_previous_stage` when a later stage discovers a missing dependency:

| Current Stage | Backtrack To | Trigger |
|---|---|---|
| `paper_content` | `paper_plan` | missing outline, missing source-to-section mapping, unsupported section purpose |
| `paper_document` | `paper_content` | unclear caption text, figure-text mismatch, missing final wording |
| `paper_final` | `paper_content` | unsupported claims, overclaims, weak citation support |
| `paper_final` | `paper_document` | figure, table, equation, reference, or layout defects |
| `paper_ppt` | `paper_plan` | unclear paper argument or missing figure selection logic |
| `paper_revision` | `paper_content` | response requires manuscript text changes |

## Stage Gates

Do not move to the next stage if the current stage has a fatal issue:

- manuscript type or template is not confirmed
- outline or source mapping is not confirmed
- manuscript body contains working notes or placeholders
- data, formulas, figures, or references are missing for central claims
- figure captions exist without figures
- references are placeholders or unsupported
- chapter or section structure is disordered

Fast-track tasks may skip type and outline gates, but they must still preserve technical meaning, avoid hallucination, and keep working notes out of manuscript body.

Fast-track examples: one grammar fix, one phrase translation, one short paragraph polish, one citation-support check, one caption adjustment, or one reference punctuation fix.

Fast-track non-examples: full abstract rewrite, section rewrite, multi-reference audit, full manuscript formatting, or thesis chapter work.

Fast-track output must include a minimal audit note with `Checks performed`, `Checks skipped`, and `Residual risk`.

## Structured User Questions

When using `ask_user`, produce a concise list:

| Question | Why It Matters | Expected Answer Type |
|---|---|---|

Ask only for information that blocks the next step. Do not ask for facts that can be inferred from provided files.

## Manuscript Body Separation

Keep separate:

- manuscript body
- planning report
- source mapping report
- missing item report
- figure source report
- citation support report
- formatting report
- final audit report
- PPT asset manifest and QA report

The manuscript body must not contain planning notes, software logs, extraction notes, source-file labels, `Missing`, `Unverified`, or `User confirmation required`.

## Time Estimates

Give a rough interaction estimate:

- Fast-track text edit: under 1 minute.
- One section writing or polishing: 2-5 minutes.
- Full outline planning: 3-8 minutes.
- Full manuscript generation or rebuild: 10-30 minutes depending on source size.
- Formatting with figures/tables: 5-15 minutes.
- Final audit: 5-15 minutes.
- PPT outline: 2-5 minutes.
- PPTX generation: 5-20 minutes depending on slide count and dependency status.

## Controller Output

When invoked, output:

| Field | Value |
|---|---|
| Stage | current workflow stage |
| Mode | full, fast_track, revision, audit, or ppt |
| Blocking Items | none or concrete blockers |
| Recommended Next Step | controller action plus module |
| Estimated Time | rough interaction estimate |
| Allowed Output | chat-text, report, docx, latex, pdf, pptx, or fallback outline |

Then list user confirmations needed, if any.

If a stage backtracks, include the source contract name, target module, and the missing dependency that caused the return.

Be conservative. When uncertain whether content belongs in the manuscript body or a report, put it in a report.
