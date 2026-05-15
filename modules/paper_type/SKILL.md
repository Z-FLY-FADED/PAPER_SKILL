---
name: paper-writing-type-input
description: Use this skill when the user wants to write, revise, polish, format, or prepare an academic manuscript and provides, or needs help confirming, the manuscript type, discipline, target journal/conference/school, length, template, figure/table/equation/reference rules, output format, and locked constraints before substantive writing begins.
---

# Paper Type and Requirement Intake

## Purpose

Confirm the writing task before planning, writing, formatting, or auditing. This module defines the manuscript type, target venue, output format, template constraints, and non-negotiable rules.

## I/O Contract

Consume optional prior project context and user-provided templates or guidelines. Produce `paper_type_output`.

`paper_type_output` must include `article_type_profile` and, when available, `template_compliance_profile`. Use `../../references/module_io_schemas.md` for the compact handoff shape.

## Supported Work Types

- conference paper
- SCI or journal article
- master thesis or dissertation chapter
- general academic manuscript
- review, response letter, cover letter, highlights, graphical abstract text
- paper-derived PPTX or presentation package

## Article Type Profiles

Classify the article type as one of:

- `sci_journal`
- `conference_paper`
- `chinese_journal`
- `master_thesis`
- `general`

After classification, load `../../references/article_type_requirements.md` only when type-specific checks are needed.

## Intake Checklist

Confirm or infer:

- manuscript type and article category
- discipline, topic, and technical scope
- discipline domain: experimental science, computational/AI, clinical, engineering, humanities/social science, theoretical mathematics, review/meta-analysis, or other
- target journal, conference, school, advisor requirement, or template
- language: Chinese, English, or bilingual
- expected output: chat text, Markdown, DOCX, LaTeX, PDF, PPTX, or multi-format
- length: words, pages, slide count, or template limits
- required structure: title, abstract, keywords, sections, references, appendices
- figure, table, equation, algorithm, and supplementary material rules
- reference style and citation style
- template source: Word, LaTeX, PDF guideline, author instruction, or plain rules
- terminology, abbreviations, notation, and naming conventions
- available source materials and permitted reuse
- missing data, uncertain claims, and items requiring user confirmation

## Template-Aware Compliance

User-provided templates, author instructions, school guidelines, or journal/conference policy files are the source of truth. If present, load `../../references/template_compliance_extraction.md` and extract a `template_compliance_profile`.

Extract at least:

- required sections
- abstract and keyword rules
- formatting and page or word limits
- reference style
- declaration requirements
- figure, table, supplement, and graphical abstract rules

If no template or official guideline is provided, use article-type defaults from `article_type_requirements.md` and mark them as unverified defaults.

## Routing Output

After intake, produce a short requirement table:

| Item | Confirmed Value | Source | Risk / Missing Item |
|---|---|---|---|

Then recommend the next module:

- `paper_plan` for outline and source mapping
- `paper_content` for writing, rewriting, polishing, translation, or citation-aware drafting
- `paper_document` for formatting, figures, tables, equations, references, DOCX, or LaTeX
- `paper_final` for submission audit
- `paper_ppt` for slides or PPTX

## Discipline Adaptation

Classify the domain before applying style rules:

| Domain | Writing Priority |
|---|---|
| experimental science | evidence, methods, figures, statistics, reproducibility |
| computational/AI | datasets, baselines, metrics, ablations, code/data availability |
| clinical | ethics, population, endpoints, safety, consent, reporting standards |
| engineering | system model, constraints, validation, robustness, deployment boundary |
| humanities/social science | argument, sources, theory, qualitative evidence, interpretive scope |
| theoretical mathematics | definitions, lemmas, theorem-proof structure, rigor, assumptions |
| review/meta-analysis | search strategy, inclusion criteria, synthesis, evidence grading |
| other | ask user to define discipline-specific success criteria |

Nature-style rules are optional outside science, engineering, clinical, and computational domains. For theoretical mathematics, proof rigor outranks experiment-first writing. For humanities/social science, argument and source interpretation outrank figure-driven evidence.

## Rules

- Do not start large-scale writing before key requirements are known.
- If a requirement is missing but low risk, proceed with a clearly stated assumption outside the manuscript body.
- If a requirement is missing and high risk, ask the user to confirm.
- Do not invent journal rules, school rules, page limits, reference styles, DOI metadata, or template requirements.
- Do not treat old project files or examples as evidence for a new manuscript unless the user explicitly authorizes them.
