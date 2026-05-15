---
name: paper_writer
description: Type-aware academic paper writing skill. Use when the user asks for broad end-to-end manuscript generation, conference paper drafting, SCI journal paper drafting, master thesis drafting, section-by-section thesis rebuilding, similarity reduction, figure insertion, table formatting, reference repair, or manuscript package preparation while preserving academic integrity.
---

# Type-Aware Paper Writer

## Purpose

Generate or rebuild manuscript drafts using the confirmed task type, outline, sources, and constraints. This module is for broad writing tasks that span multiple sections or require coordinated output.

## I/O Contract

Consume `paper_type_output` and `paper_plan_output` whenever available. Produce `paper_content_output` for drafted manuscript text and hand off to `paper_document` or `paper_final` when file formatting or audit is required.

Use `../../references/module_io_schemas.md` for the compact handoff shape.

## Relationship to Other Modules

- Use `paper_type` before writing when requirements are unclear.
- Use `paper_plan` before writing when sources or outline are unclear.
- Use `paper_content` for section-level writing and polishing.
- Use `paper_document` for formatting and asset insertion.
- Use `paper_final` before calling any output final or submission-ready.

## Supported Manuscript Types

- conference paper
- SCI or journal paper
- master thesis
- general academic manuscript
- paper-derived report or extended manuscript

## Writing Workflow

1. Confirm manuscript type and output format.
2. Confirm source materials and allowed reuse.
3. Confirm outline and section purpose.
4. Build a section-by-section evidence plan.
5. Draft only from verified source material and user-provided facts.
6. Mark missing data in a separate report, not in manuscript body.
7. Check repetition, logic, citations, figures, tables, equations, and terminology.
8. Produce the requested manuscript file or text.
9. Run final audit before naming a file final.

Before finalization, check journal compliance materials:

- ethics statement
- competing interests
- data availability
- code availability
- author contributions
- funding
- acknowledgements
- consent, IRB, or reporting checklist when relevant

Create placeholders only as user-fill items in a report or submission-material draft. Do not state them as verified facts.

## Type-Specific Priorities

For detailed SCI, conference, Chinese journal, or master thesis checks, load `../../references/article_type_requirements.md` only when that type is selected.

### Conference Paper

- compact problem statement
- clear contribution
- method and experiment focus
- concise related work
- no thesis-style chapter narration
- strict page and formatting limits

### SCI or Journal Paper

- clear gap and significance
- evidence-backed novelty
- reproducible methods
- results tied to figures/tables
- cautious discussion and limitations
- citation support for all major claims

### Master Thesis

- systematic chapter structure
- sufficient literature review
- reproducible model, experiment, and analysis details
- complete figure/table/equation/reference integration
- chapter-level evidence and conclusion alignment
- no repeated generic filler

## Rebuild Mode

Use rebuild mode when a draft is repetitive, template-like, under-evidenced, or contaminated with working notes.

Steps:

1. Keep only the confirmed structure.
2. Remove repeated generic paragraphs.
3. Rebuild each chapter or section according to its function.
4. Insert only verified data, formulas, figures, tables, and references.
5. Move missing information to reports.
6. Run chapter-level quality checks before merging.

## Integrity Rules

Never invent data, experiments, simulations, metrics, datasets, formulas, figures, references, DOI, reviewer comments, or acceptance claims.

Do not treat old files in `inputs/`, `outputs/`, or `templates/` as current project evidence unless the user explicitly says they belong to the current task.

Do not place planning notes, source-processing notes, `Missing`, `Unverified`, or `User confirmation required` in manuscript body.

## Output

For large writing tasks, provide:

- manuscript draft or generated file path
- source and evidence report
- missing item report
- figure/table/reference status
- final audit recommendation
