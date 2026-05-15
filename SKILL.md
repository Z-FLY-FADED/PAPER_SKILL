---
name: PAPER
description: Unified academic paper and thesis workflow skill. Use this skill for manuscript type confirmation, source and outline planning, Nature-style or discipline-adapted writing and polishing, citation/evidence matching, publication figure generation and audit, revision management, reviewer-response drafting, thesis or journal/conference paper drafting, Word/LaTeX formatting, paper-to-PPTX presentation generation with dependency checks, final submission audit, and reviewer-oriented quality checks. This consolidated skill routes to paper_type, paper_plan, paper_content, paper_document, paper_final, paper_revision, paper_ppt, paper_workflow_controller, and paper_writer modules.
metadata:
  short-description: Academic paper and thesis writing workflow
---

# PAPER

This is the single entry point for all academic paper, journal article, conference paper, and thesis tasks.

The old paper-related skills have been consolidated under `modules/`. Treat those module files as detailed references and load only the module needed for the current stage.

## Reference Files

- `references/module_io_schemas.md`: mandatory minimal handoff schemas for module chaining.
- `references/article_type_requirements.md`: detailed defaults for SCI journals, conferences, Chinese journals, and master theses.
- `references/template_compliance_extraction.md`: template and guideline extraction rules.

## Module Map

- `modules/paper_workflow_controller/SKILL.md`: stage routing, workflow gates, and prevention of internal notes entering manuscript text.
- `modules/paper_type/SKILL.md`: manuscript type, venue, length, output format, Word/LaTeX template input, figure/table/equation/reference rules, and locked constraints.
- `modules/paper_plan/SKILL.md`: source-material mapping, outline planning, topic screening, terminology alignment, and missing-content planning.
- `modules/paper_content/SKILL.md`: writing, rewriting, polishing, translation, expansion, compression, and logical-chain checks.
- `modules/paper_document/SKILL.md`: document formatting, DOCX/LaTeX/Markdown output, LaTeX template integration, headings, figures, tables, equations, references, layout, and final consistency.
- `modules/paper_final/SKILL.md`: final quality audit, reviewer-risk audit, citation/reference checks, figure/table-text consistency, and final revision priorities.
- `modules/paper_writer/SKILL.md`: type-aware end-to-end paper generation, conference/SCI/thesis workflows, table formatting, numbering, references, and similarity reduction.
- `modules/paper_ppt/SKILL.md`: Nature-style paper-to-PPTX workflow for journal club, group meeting, thesis seminar, lab meeting, and academic presentation decks.
- `modules/paper_revision/SKILL.md`: revision history, reviewer comment mapping, response drafting, diff comparison, and change-log management.

## Operating Rule

Do not load every module by default. First classify the user's request, then read the smallest relevant module.

Use this routing:

| User request | Read |
|---|---|
| Determine paper type, target venue, output format, template rules, length, formatting requirements | `paper_type` |
| Build outline, map sources to sections, screen topics, plan thesis/paper structure | `paper_plan` |
| Write, rewrite, polish, translate, expand, compress, improve logic | `paper_content` |
| Format or finalize Word/LaTeX document, figures, tables, equations, references | `paper_document` |
| Generate, redesign, or audit publication-style figures, figure panels, graphical summaries, or chart assets | `paper_document`, then `paper_final` for figure-text consistency |
| Add, verify, or export citations and reference-manager files, or judge whether papers support manuscript claims | `paper_content`, then `paper_final` for citation audit |
| Audit final manuscript before submission or defense | `paper_final` |
| Convert a paper, preprint, thesis chapter, abstract, figure legends, or reading notes into PPT/PPTX slides | `paper_ppt` |
| Manage revisions, reviewer comments, response letters, diffs, change logs, or revision history | `paper_revision` |
| User asks for full paper/thesis creation or broad end-to-end manuscript work | `paper_workflow_controller`, then the relevant stage modules |
| User asks for conference/SCI/thesis type-aware generation, similarity reduction, figure insertion, or table/reference repair | `paper_writer` |

Fast-track routing:

| Fast-track request | Read |
|---|---|
| One sentence or one paragraph polishing, title refinement, one citation question, short translation, or minor formatting tweak | `paper_content` or `paper_document` with `fast_track=true` |

Fast-track examples include one grammar fix, one phrase translation, one short paragraph polish, one citation-support check, one caption adjustment, or one reference punctuation fix. Non-examples include a full abstract rewrite, section rewrite, multi-reference audit, full manuscript formatting, and thesis chapter work.

When multiple stages apply, use this order:

1. Type and constraints
2. Source and outline planning
3. Content writing or polishing
4. Document formatting
5. Final quality audit
6. Presentation generation, only after the paper argument and usable source figures are understood

Backtracking is allowed. If a later stage finds missing source evidence, unclear outline, inconsistent terminology, failed dependencies, or unsupported claims, route with `back_to_previous_stage` instead of forcing the current stage to continue.

## Module I/O Contract Rule

When chaining modules, emit the named contracts and mandatory base fields defined in `references/module_io_schemas.md`.

Every stage output must include these base keys:

- `stage`
- `status`
- `confirmed_inputs`
- `outputs`
- `missing_items`
- `risk_flags`
- `next_recommended_module`

Use these contract names where relevant: `paper_type_output`, `paper_plan_output`, `paper_content_output`, `paper_document_output`, `paper_final_output`, `paper_revision_output`, and `paper_ppt_output`. Required fields must not be replaced by free-form prose.

## Controller Actions and Status Card

When the controller is used, it must choose one action:

- `next_stage`: continue to the recommended module.
- `back_to_previous_stage`: return to an earlier module because a dependency is missing.
- `ask_user`: ask a concise structured question list before proceeding.
- `fast_track`: handle a small local task without full planning gates.
- `check_dependencies`: run an environment check before file generation.

Controller output must include this status card:

| Field | Value |
|---|---|
| Stage | current workflow stage |
| Mode | full, fast_track, revision, audit, or ppt |
| Blocking Items | none or concrete blockers |
| Recommended Next Step | action plus module |
| Estimated Time | rough interaction estimate |
| Allowed Output | chat-text, report, docx, latex, pdf, pptx, or fallback outline |

## Mandatory Gates

Before large-scale writing or document generation, confirm or infer:

- manuscript type: conference paper, SCI journal paper, master thesis, or general academic manuscript
- discipline and technical subject
- target journal, conference, school, or template
- desired output format: chat text, Markdown, DOCX, LaTeX source, PDF, or multiple formats
- presentation output if requested: PPTX deck, slide outline, speaker notes, asset manifest, or QA report
- discipline domain: experimental science, computational/AI, clinical, engineering, humanities/social science, theoretical mathematics, review/meta-analysis, or other
- template input type: Word template, LaTeX template package, PDF guideline, author instructions, or plain text rules
- required length, page limit, language, and structure
- source materials and their allowed use
- figures, tables, equations, notation, and reference style
- locked terminology and abbreviations
- missing data, uncertain claims, and user-confirmation items

If key information is missing and a reasonable assumption would be risky, ask a concise question. For small local edits, proceed using the available context and mark uncertainty outside the manuscript body.

## Output Format Selection

Always identify the expected output format before generating or editing a manuscript.

Supported output formats:

- `chat-text`: manuscript-ready text in the conversation
- `markdown`: `.md` manuscript or report
- `docx`: Word document output
- `latex`: LaTeX source output such as `.tex`, `.bib`, and related files
- `pdf`: compiled PDF or PDF-ready source, only when compilation/export can actually be performed
- `pptx`: PowerPoint deck generated from paper source, notes, or selected figures
- `multi`: more than one output format, for example `.tex + .bib + PDF` or `.docx + audit report`

Default behavior:

- If the user asks only for wording, polishing, translation, or a section draft, output `chat-text` unless a file format is requested.
- If the user provides a Word template or asks for Word formatting, prefer `docx`.
- If the user provides a LaTeX template, Overleaf package, `.tex`, `.cls`, `.sty`, `.bib`, or `.bst`, prefer `latex`.
- If the user asks for final submission files, confirm whether they want `docx`, `latex`, `pdf`, or `multi`.
- If the user asks for slides, presentation, group meeting, journal club, report PPT, or paper sharing, prefer `pptx` and route to `paper_ppt`.
- If the user asks for review comments, revision, response letter, diff, or change log, route to `paper_revision`.

For LaTeX template input, inspect the project template files before writing:

- main `.tex` file and document class
- `.cls` and `.sty` files
- bibliography files: `.bib`, `.bst`, `.bbl` if present
- figure and table conventions
- required compiler if known: pdfLaTeX, XeLaTeX, LuaLaTeX, or unspecified
- target journal/conference/school instructions embedded in comments or template docs

Do not claim that a LaTeX project compiles unless compilation was actually run and succeeded. If compilation is unavailable, output LaTeX source plus a `latex_check_report.md`.

## Manuscript Integrity Rules

Never fabricate:

- data, experiments, simulations, metrics, hardware, parameters, constants, datasets, ablations, comparisons, statistical significance, reviewer comments, funding, DOI, reference metadata, or publication status
- figures, tables, equations, citations, or source conclusions not present in the user-provided material

Preserve:

- technical meaning
- numerical values
- formula meaning
- variables and notation
- figure/table meaning
- confirmed terminology
- source-supported conclusions

If a logical gap, unsupported claim, or missing source appears, do not silently smooth it over. Report it separately and ask for confirmation when needed.

## Manuscript Body Separation

The manuscript body may contain only content that belongs in the final academic document.

Never put these into manuscript body text:

- planning notes
- source-processing notes
- "Missing", "Unverified", or "User confirmation required" markers
- software/environment notes
- figure extraction notes
- audit comments
- internal skill execution notes
- source file names such as `Manuscript.doc`, `Manuscript.docx`, or "source paper"

Put working notes into separate reports, for example:

- `planning_report.md`
- `source_mapping_report.md`
- `missing_items_report.md`
- `formatting_report.md`
- `reference_check.md`
- `final_quality_audit.md`

Before naming a manuscript `final`, `polished`, `submission-ready`, or equivalent, scan the body for internal markers, placeholders, duplicated numbering, blank formulas, and unresolved references. If any remain, use a draft name and create an issue report.

## Output Behavior

For writing-only tasks:

- provide manuscript-ready text first
- keep implementation notes brief and separate
- preserve the requested language
- do not add unrelated sections

For document-editing tasks:

- preserve the original document unless the user asks for structural changes
- write a short report of what changed
- flag any unverified content
- avoid changing technical meaning while formatting
- preserve the selected output format unless the user asks to convert formats

For final audits:

- findings first, ordered by severity
- include file/page/section references when available
- separate technical risks, formatting risks, citation risks, and submission risks
- include a concise action list

## Project Reference Materials

Reference documents, example manuscripts, templates, figures, datasets, and borrowed materials are project-specific.

Use only the materials the user provides for the current project, or files that are explicitly identified as belonging to the current manuscript task.

Do not treat old examples, unrelated papers, or previous project outputs as verified facts for a new manuscript. They are not reusable evidence unless the user explicitly authorizes them for the current project.

## Maintenance Notes

This skill is intentionally a lightweight controller. Keep detailed long-form rules in the module files and keep this `SKILL.md` focused on routing, safety gates, and universal academic integrity rules.
