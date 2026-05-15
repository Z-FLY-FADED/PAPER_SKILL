---
name: paper-source-outline-planning
description: Use this skill when the user provides academic materials such as papers, theses, reports, patents, figures, tables, datasets, experimental notes, or drafts and wants to turn them into a manuscript outline, thesis structure, SCI paper plan, conference paper structure, or chapter directory with source-to-section mapping, terminology alignment, missing-content analysis, and self-overlap risk control.
---

# Source and Outline Planning

## Purpose

Convert provided materials into a defensible manuscript plan before substantive writing. This module maps sources to sections, identifies missing evidence, aligns terminology, and prevents unsupported or duplicated content.

## I/O Contract

Consume `paper_type_output` plus source materials. Produce `paper_plan_output`.

Use `../../references/module_io_schemas.md` for the compact handoff shape. Preserve `article_type_profile` and `template_compliance_profile` in confirmed inputs when available.

## Inputs

- source papers, thesis chapters, reports, patents, notes, figures, tables, datasets, or drafts
- confirmed requirements from `paper_type`
- target output type and format
- user constraints on reuse, novelty, similarity, and allowed source material

## Workflow

1. Identify all source materials and their role.
2. Extract candidate contributions, methods, datasets, figures, tables, and results.
3. Check what each source can legitimately support.
4. Propose candidate titles or topics if needed.
5. Build an outline appropriate to the confirmed manuscript type.
6. Map each section to source evidence.
7. List missing experiments, data, formulas, references, figures, or permissions.
8. Check self-overlap and source-reuse risk.
9. Align terminology, abbreviations, variables, and notation.
10. Ask for confirmation before drafting manuscript body text.

## Required Tables

### Source Inventory

| Source | Type | Useful Content | Reuse Boundary | Risk |
|---|---|---|---|---|

### Outline Plan

| Section | Purpose | Source Basis | Missing Evidence | Can Write Now? |
|---|---|---|---|---|

### Terminology Map

| Concept | Preferred Term | Alternate Forms | Notes |
|---|---|---|---|

## Rules

- Planning output is not manuscript body text.
- Do not claim data, experiments, figures, citations, or conclusions that are absent from the source materials.
- Do not hide missing evidence by writing generic filler.
- Do not reuse old project outputs as verified facts for a new project.
- If source overlap risk exists, report it before writing.
- For theses, each chapter must have a distinct academic function and evidence base.
- For journal or conference papers, prioritize a focused claim, compact structure, and evidence density.
- For SCI journals, conferences, Chinese journals, and master theses, load `../../references/article_type_requirements.md` only when detailed type-specific planning checks are needed.
