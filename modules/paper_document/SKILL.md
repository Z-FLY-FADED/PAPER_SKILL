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

## Thesis Formatting Guardrails

For thesis or LaTeX conversion work, treat the following as required checks before delivery:

- Cover metadata fields such as candidate, supervisor, major, school, and degree type must either be filled from verified source material or flagged in a report. Do not leave unexplained visible blanks such as "Candidate:", "Supervisor:", or "Major:" in the rendered output.
- Symbol and abbreviation tables must use clean, editable notation. Prefer LaTeX math for variables such as `$F_{\mathrm{H_2,out}}$`, `$Y_{\mathrm{H_2}}$`, `$\eta_{\mathrm{th}}$`, and `$T_{\mathrm{out}}$`; do not leave mojibake or plain-text pseudo-symbols.
- Symbol tables should define ratios and abbreviations with concrete expressions where possible, for example OER as `$F_{\mathrm{O_2}}/F_{\mathrm{DME}}$` and SER as `$F_{\mathrm{H_2O}}/F_{\mathrm{DME}}$`. Check units for alignment, completeness, and consistency.
- Use automatic numbering for LaTeX equations, figures, and tables when possible. Remove bare manual labels such as `(2-1)` when they are separated from the equation, and never leave numbered placeholders without a formula.
- Figure and table references in text must correspond to real `figure` or `table` environments with captions and labels. Placeholder text such as `[image]`, missing graphics, and header/data splits across pages should be repaired or reported.
- Treat `image[[x1, y1, x2, y2]]`-style strings as suspect parser metadata. Before editing the manuscript, verify whether the strings occur in the source file or only in extracted text; then confirm referenced image assets and render representative pages. If rendered pages show the actual images, document the parser artifact instead of replacing or deleting figures.
- In bilingual theses, keep Chinese and English abstract formatting symmetrical: both should include title-level abstract text and keywords, with no extra explanatory notes in only one language.
- Tables should keep captions, headers, and data together when feasible. For long tables, use the template's long-table environment instead of letting headers detach from data.
- Check table of contents page numbers against the rendered PDF after compilation. Flag missing dot leaders, inconsistent indentation, wrong front-matter numbering, chapter page jumps, and section titles that differ between TOC and body.
- Check page style continuity: front matter, symbol pages, chapter openings, headers, footers, and page numbers should follow the target school or venue template without missing or duplicated numbering.
- Check for parser leftovers and extraction artifacts in the source and rendered text, including isolated numbers, `<center>...</center>`, `[image]`, `image[[...]]`, and OCR-like symbol corruption.

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

## Composite Figure Layout

For multi-panel or composite figures in theses:

- Use one overall figure number for the whole composite figure. Mark internal panels with `(a)`, `(b)`, `(c)` in reading order and keep those markers visible in the figure area.
- Figure captions should explain the meaning of each panel when needed, for example: `图3-4 氢产率响应面关系图：（a）...；（b）...；（c）...。`
- Text references should point to the overall figure or a specific panel as appropriate, for example `图3-4(a)` or `Figure 3-4(a)`. Do not create separate captions or independent figure numbers for panels that belong to the same composite figure.
- If source images are pre-composed but can be safely split, crop panels into separate assets and rebuild the figure using `subfigure`, `subcaption`, `subfig`, or `minipage`. Preserve the original data and visual meaning.
- If panel splitting is not possible, keep a single high-resolution composite image but ensure internal labels `(a)`, `(b)`, `(c)` are visible, aligned, and explained in the caption.
- Avoid letting one figure consume a full page unless the figure is genuinely complex and remains readable only at that size.
- Arrange multiple small panels in balanced grids such as 2x2, 2x3, or 3x2; 4-6 panels usually should fit on one page.
- If there are more than 6-8 panels, split the material into two separately numbered figures instead of forcing an overcrowded layout.
- Keep subpanel sizes uniform unless a main panel plus supporting panels is intentionally used.
- Keep spacing moderate. Too little spacing harms readability; too much spacing creates empty-looking pages.
- In LaTeX, prefer `subcaption`, `subfigure`, `minipage`, or a well-prepared composite image with consistent panel labels. Verify the rendered PDF rather than relying on source appearance.
- Do not split one composite figure across pages. If the template allows a continuation, use a continuation caption such as `图3-4（续）` / `Figure 3-4 (continued)` and keep panel labels and captions consistent.
- Check whether single small plots can be reduced in size and placed near the discussing paragraph to avoid caption-only or sparse pages.

## Rendered Figure Verification

For LaTeX/PDF outputs with reported missing figures:

- Search source for literal placeholders such as `image[[`, `[image]`, and `<center>`.
- List all `\includegraphics` targets and verify paths exist relative to the main `.tex` file.
- Render the relevant PDF pages to images and inspect them visually; text extraction alone is insufficient because extracted text omits raster/vector figure content.
- Save a contact sheet or representative page previews in the report folder when the user asks for a formal audit trail.
- Only modify figure sizing, placement, or paths after confirming a genuine rendered-output problem.

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
