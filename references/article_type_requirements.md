# Article-Type Requirements

Load this reference when `paper_type` selects an article type, or when `paper_final` performs a type-specific audit. If a user-provided template conflicts with this file, the template wins and these become unverified defaults.

## sci_journal

- Structure: Title, Abstract, Keywords, Introduction, Methods, Results, Discussion, Conclusion if required, References, Supplementary if any.
- Optional venue items: Highlights, Graphical Abstract, Cover Letter, reviewer suggestions, response letter for resubmission.
- Length: usually 3000-8000 words, but use the journal template when available.
- Innovation: end Introduction with a clear knowledge gap and contribution statement.
- Reproducibility: include instruments, reagents, software versions, statistical parameters, randomization/blinding when applicable, data/code availability.
- References: check recent-reference ratio, self-citation risk, and primary-source citation for methods and datasets.
- Declarations: conflict of interest, funding, author contributions, data availability, code availability, ethics approval, consent when relevant.
- Figures: source data, statistical test, sample size, error-bar meaning, microscopy scale bars, main figure count and panel density.
- Final audit mode: `SCI_audit`.

## conference_paper

- Structure: Title, Abstract, Introduction, Method, Experiments, Conclusion, References; add Limitations or Broader Impact when required.
- Length: enforce page limit and template, often 4-8 pages for main text.
- Contributions: Introduction should contain explicit contribution bullets or numbered list when field norm allows.
- Experiments: datasets/tasks, baselines, metrics, main results, ablation study, statistical analysis when applicable.
- References: include recent top-conference work and official BibTeX style where provided.
- Figures: model/data-flow diagram, readable result tables, best results highlighted only when verified.
- Supplement: appendix, video, code, or zip if required.
- Double blind: remove author names, affiliations, acknowledgements, and identifying self-citations.

## chinese_journal

- Structure: Chinese title, authors, affiliations, Chinese abstract, keywords, optional classification number, English title, English abstract, English keywords, main text, references, acknowledgements, funding, author contributions, conflict of interest.
- Keywords: usually 3-8.
- Abstract alignment: Chinese and English abstracts should match in meaning, numbers, terms, and structure.
- Terms: first Chinese technical term may need English full name and abbreviation, for example Chinese term (English Full Name, ABBR).
- Funding: include project name and number in the required location.
- Ethics/data: include ethics approval, data availability, and code/data repository when relevant.
- References: use GB/T 7714 when required; mark Chinese references in English lists according to venue rules.
- Figures/tables: bilingual captions when required; check Chinese/English consistency.

## master_thesis

- Front/back matter: cover, originality statement, copyright authorization, Chinese abstract, English abstract, table of contents, optional symbol list, main text, references, acknowledgements, author CV and publications.
- Chapters: usually 5-7 chapters with clear progression from background/literature to method, experiments, discussion, and conclusion.
- Literature review: sufficient depth, organized by research direction, not a short generic overview.
- Logic: each chapter should have a distinct function and connect to the next.
- Originality: include originality statement and avoid unsupported novelty claims.
- Similarity risk: produce a potential repetition/similarity-risk report template; do not claim official plagiarism-check results.
- Formatting: use school Word or LaTeX template; chapter-based figure/table numbering such as Fig. 1-1.
- References: often 60-100 references, foreign-language share and recent-reference share should follow school rules; use school template first.
- Defense: route to `paper_ppt` for defense deck with background, method, key results, innovations, outlook, and acknowledgements.

