---
name: paper-document-formatting
description: Use this skill when the user wants to format, typeset, standardize, or finalize an academic manuscript document according to confirmed template requirements. It handles DOCX, LaTeX, Markdown, figures, tables, equations, references, page layout, cross-references, supplementary material, and Nature-style publication figure generation or audit without changing technical meaning.
---

# Document Formatting, Figures, and Reference Assets

## Purpose

Apply document-level formatting and prepare publication assets after content requirements are confirmed.

## I/O Contract

Consume `paper_type_output` and `paper_content_output` when manuscript text is involved. Produce `paper_document_output`.

Use `../../references/module_io_schemas.md` for the compact handoff shape. Apply `template_compliance_profile` as the formatting source of truth when present.

Use for:

- DOCX, LaTeX, Markdown, and PDF-ready source formatting
- title, author, abstract, heading, body, caption, and reference formatting
- figure placement, figure generation, figure QA, and caption formatting
- table formatting, including three-line academic tables
- equation alignment, numbering, notation, and LaTeX environment checks
- reference list and in-text citation formatting
- page layout, headers, footers, numbering, appendices, and supplementary material

## Pre-Formatting Gate

Confirm:

- output format and template
- target venue or school rules
- font, spacing, margins, heading style, and page limits
- figure/table/caption rules
- equation and notation rules
- reference style
- manuscript file type and available assets

If rules are unavailable, report missing requirements instead of inventing them.

## Fast-Track Mode

Use `fast_track=true` for a small formatting or document asset task:

- one caption format fix
- one table style adjustment
- one figure placement or label check
- one reference punctuation/style question
- one equation numbering check

Fast-track may skip full document inspection, but it must not change technical meaning, values, formulas, figure content, or reference metadata.

Do not use fast-track for full manuscript formatting, full reference-list repair, multi-figure redesign, or thesis chapter layout work.

Fast-track output must include:

| Checks performed | Checks skipped | Residual risk |
|---|---|---|

## Core Workflow

1. Inspect document structure.
2. Identify all sections, figures, tables, equations, citations, and references.
3. Apply confirmed formatting rules.
4. Check cross-references and numbering.
5. Check Chinese-English spacing only when required or confirmed.
6. Check LaTeX environments and citation keys if applicable.
7. Check figure and table consistency.
8. Output a formatting execution report.

## No Content Change Rule

Do not change technical meaning, data, equations, results, claims, or reference metadata unless the user explicitly asks for content revision.

Allowed minor edits:

- numbering consistency
- punctuation and spacing required by style
- caption format
- reference punctuation
- obvious cross-reference wording when the target is clear

## Nature-Style Figure Contract

Before generating or redrawing a figure, define:

- manuscript claim the figure supports
- figure archetype: chart, mechanism schematic, workflow, image plate, multi-panel story, or graphical summary
- data source and verification status
- panel list and question answered by each panel
- statistics, error bars, `n`, units, and uncertainty
- output format: SVG, PDF, PNG, TIFF, DOCX embedded figure, or slide asset
- caption and source-data notes

Do not invent data, panels, microscopy images, statistics, or source files.

## Publication Figure Defaults

- Prefer one hero panel plus supporting panels.
- No two panels should answer the same question.
- Use readable labels, units, legends, and scale bars.
- Use restrained color: neutral base, signal color, and limited accent color.
- Prefer direct labels when they reduce legend burden.
- Export vector formats when possible, with raster preview if useful.
- Keep figure-processing notes out of the manuscript body.

## Tables and Equations

- Use three-line tables unless the template requires otherwise.
- Keep units in headers where possible.
- Align numerical columns and decimal places.
- Do not change table values without confirmation.
- Equations should be editable when possible.
- Do not leave blank formula placeholders.
- Do not claim LaTeX compilation or MathType compliance unless verified.

## Report

After formatting or asset work, provide:

- completed actions
- unperformed or unverified items
- remaining formatting risks
- required user confirmations
- generated file paths when files are created
