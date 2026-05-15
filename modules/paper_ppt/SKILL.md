---
name: paper_ppt
description: Use this skill when the user wants to turn a scientific paper, thesis chapter, preprint, PDF, article text, abstract, figure legends, supplementary figures, or reading notes into an academic PowerPoint/PPTX deck for journal club, group meeting, paper sharing, thesis seminar, lab meeting, department report, or research presentation. It builds a complete but efficient Nature-style Chinese or bilingual slide deck, selects evidence figures, writes slide titles, bullets, captions, speaker notes, creates the actual .pptx when tooling is available, and performs lightweight PPTX verification.
---

# Paper to PPTX Presentation Skill

## Purpose

Create a presentation deck from academic paper material. The primary deliverable is a usable `.pptx` deck when file generation tools are available. If the user only asks for an outline, provide a slide plan without creating a deck.

## I/O Contract

Consume source materials, optional `paper_type_output`, and the PPT dependency check result. Produce `paper_ppt_output`.

Use `../../references/module_io_schemas.md` for the compact handoff shape.

This module applies to:

- journal club and paper sharing
- group meeting and lab meeting presentations
- thesis seminar and defense-preparation decks
- research progress reports based on manuscript material
- conference-style short talks derived from a paper
- review, method, resource, dataset, benchmark, clinical, engineering, AI, materials, chemistry, physics, environmental, and biomedical papers

## Default Stance

- Explain the paper through evidence, not decoration.
- Identify the paper's argument before designing slides.
- Select only figures and tables that advance the story.
- Keep slide text concise and readable.
- Preserve technical meaning, numerical values, figure content, and source attribution.
- Do not invent results, figures, captions, citations, author claims, or limitations.
- Use Chinese by default for slide titles, bullets, captions, and speaker notes unless the user requests English or bilingual slides.
- Preserve key technical terms in English when translation would reduce precision.

## Accepted Inputs

- full paper PDF
- thesis chapter or manuscript file
- article text, abstract, results, discussion, or figure legends
- structured reading notes
- supplementary figures or tables
- manually pasted paper content
- existing PPTX template
- selected figure image files

If the paper source is incomplete, create a deck only from the available material and list missing sections in `ppt_missing_source_report.md`.

## Lean Operating Mode

Use the smallest reliable extraction path:

1. Read only the source material needed to understand the paper's argument.
2. Extract or crop only figures/tables that will appear in the deck.
3. Create the PPTX as the primary deliverable.
4. Run lightweight structural checks on the PPTX package.
5. Write a short QA report.

Avoid:

- exhaustive extraction of every page, figure, image, table, or supplement
- full OCR unless selectable text extraction fails or the PDF is scanned
- saving full raw extracted paper text unless needed for debugging or reuse
- installing new dependencies when existing tools can complete the task
- GUI automation solely to render previews
- long markdown scripts when the user asked for a deck

## Toolchain Policy

Prefer:

- PyMuPDF for PDF metadata, text extraction, page rendering, and page-level crops
- Pillow for figure crops, contact sheets, and lightweight preview images
- python-pptx for slide authoring and PPTX-safe editing
- zipfile plus a reopen pass through python-pptx for package validation

If a render engine is unavailable, perform structural QA instead of claiming visual verification.

## Dependency Check

Before generating PPTX files, run:

```text
py scripts/check_ppt_dependencies.py
```

Interpret the JSON result:

- `status=ready`: generate PPTX, extract PDF figures when needed, and run structural QA.
- `status=partial`: generate PPTX only from available text/images; do not claim PDF figure extraction works.
- `status=fallback`: do not generate PPTX. Output Markdown slide outline, figure placeholders, and `ppt_dependency_report.md`.

If PyMuPDF or python-pptx is missing, degrade gracefully instead of installing packages automatically.

## Workflow

### 1. Extract the Paper Argument

Identify:

- title, authors, journal/preprint server, year, DOI if available
- discipline and subfield
- paper type
- central problem and knowledge gap
- main claim or thesis
- study design, workflow, model, dataset, or experimental system
- key methods and controls
- main results and quantitative findings
- key figures, tables, and figure legends
- validation, robustness, ablation, or sensitivity analyses
- limitations and unresolved questions
- broader scientific, clinical, technical, engineering, or translational meaning

### 2. Classify the Paper Before Designing Slides

Choose one dominant story pattern:

- `claim-first`: one strong central claim
- `question-to-evidence`: discovery, mechanism, clinical, or population papers
- `problem-to-solution`: methods, AI, tool, algorithm, device, and engineering papers
- `workflow-to-validation`: resource, dataset, atlas, omics, benchmark, and platform papers
- `evidence-map`: reviews, perspectives, and meta-analyses

### 3. Build the Slide Plan

For each slide, define:

- Chinese or bilingual slide title
- slide purpose
- selected evidence figure/table if any
- 3-4 concise bullets at most
- one takeaway sentence
- speaker note when oral explanation is useful
- source label for paper, page, figure, or table

Default deck structure:

1. Cover
2. Background and problem
3. Knowledge gap or unmet need
4. Study design, method, or workflow
5. Main result 1
6. Main result 2
7. Validation, robustness, controls, or ablation
8. Mechanism, model, or synthesis
9. Limitations and open questions
10. Take-home message

Adjust slide count to the requested talk length.

### 4. Select Figures as Evidence

Use figures and tables only when they answer a slide question.

Prioritize:

- graphical abstracts or summary models
- study design and workflow diagrams
- central result figures
- microscopy, imaging, spatial, heatmap, map, network, or dimensionality reduction panels
- statistical result plots, survival curves, forest plots, calibration curves, or benchmark plots
- materials characterization and performance plots
- model architecture, ablation, validation, or error analysis figures
- key tables that cannot be replaced by a concise bullet

Do not shrink dense multipanel figures into unreadable thumbnails. Crop relevant panels when appropriate and preserve a source label.

### 5. Extract and Prepare Figure Assets

When source files permit:

- extract original embedded images first
- render high-resolution page images only for pages containing selected figures/tables
- crop figure panels tightly
- keep original data visuals unchanged
- save assets under `output/assets/figures/`
- use clear filenames such as `fig1_workflow.png`, `fig2b_main_result.png`, or `fig4ef_validation.png`
- record source page, figure number, panel, crop status, and intended slide in `output/asset_manifest.md`

If a figure cannot be extracted reliably, use a clearly labeled placeholder in the slide plan or ask the user for the source figure. Do not fabricate the figure.

### 6. Design Slide Layouts

Use 16:9 widescreen by default.

Layout rules:

- Result/evidence slides should be figure-first.
- Use full-width or near-full-width visuals for complex evidence.
- Use a narrow interpretation rail only when it helps the audience read the figure.
- Use top/bottom stack when the figure needs horizontal room.
- Use asymmetric split such as 70/30, 75/25, or 65/35 when one side clearly dominates.
- Avoid equal split layouts when the figure is the main evidence.
- Avoid text-only result slides when visuals are available.
- Avoid overloaded bullets and crowded captions.

Slide archetypes:

- Cover: one dominant visual or typographic idea.
- Background/problem: short setup text plus one compact context visual.
- Workflow/method: process diagram, pipeline, or major method figure.
- Result/evidence: dominant figure or table crop plus concise interpretation.
- Comparison/table: full-width table or split across slides if cramped.
- Model/summary: large central model with a short takeaway strip.
- Conclusion: 2-4 concise bullets with clear final message.

## Content Rules

- Write titles as claims, not vague labels, when evidence supports them.
- Keep bullets short and specific.
- Explain what the figure shows, why it matters, and what the audience should believe after seeing it.
- Preserve uncertainty and limitations.
- Do not overstate causality, generality, clinical relevance, or engineering applicability.
- Do not replace figure evidence with decorative images.
- Keep citations and source labels outside the main visual area.

## Output Package

When generating files, create:

- `output/presentation.pptx`
- `output/asset_manifest.md`
- `output/ppt_qa_report.md`
- selected figure assets under `output/assets/figures/`

If the user requests an outline only, output:

- slide list
- selected figures/tables
- speaker notes
- missing source items

If dependency fallback is active, output:

- `slides_outline.md`
- `ppt_dependency_report.md`
- figure placeholder list with source pages or requested assets

For master thesis defense decks, use the master thesis requirements in `../../references/article_type_requirements.md` when detailed defense structure is needed.

## PPTX QA

After creating a deck, check:

- slide count matches the requested scope
- images are embedded
- figure assets exist at referenced paths
- speaker notes exist when planned
- slide order follows the paper argument
- text does not obviously overflow
- figures are not visibly distorted
- source labels are present on figure slides
- dense figures are cropped or split instead of unreadable
- deck can be reopened by the generation library

If visual rendering is unavailable, say that only structural QA was performed.

## Report Format

After deck generation, report:

```text
Generated deck:
- [absolute path to PPTX]

Supporting files:
- [asset manifest]
- [QA report]

Verification:
- slide count: ...
- embedded media: ...
- speaker notes: ...
- unchecked items: ...
```

Do not claim final visual perfection unless screenshots or rendering were actually inspected.
