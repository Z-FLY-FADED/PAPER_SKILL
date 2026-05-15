# Template Compliance Extraction

Use this reference when a user provides a Word template, LaTeX template, PDF guideline, author instruction, school rule, or journal webpage text.

## Source Priority

1. User-confirmed instruction.
2. Uploaded official template or guideline.
3. Target venue author instructions.
4. Article-type defaults from `article_type_requirements.md`.
5. General academic defaults, marked unverified.

## template_compliance_profile

Produce this compact profile:

```json
{
  "template_source": "",
  "source_priority": "",
  "required_sections": [],
  "format_rules": {
    "length": "",
    "page_limit": "",
    "font": "",
    "spacing": "",
    "margins": "",
    "heading_style": "",
    "language": ""
  },
  "reference_rules": {
    "style": "",
    "in_text_style": "",
    "bibliography_style": "",
    "doi_url_access_date": ""
  },
  "declaration_rules": {
    "ethics": "",
    "consent": "",
    "competing_interests": "",
    "funding": "",
    "author_contributions": "",
    "data_availability": "",
    "code_availability": "",
    "acknowledgements": ""
  },
  "figure_table_rules": {
    "figure_count": "",
    "panel_limit": "",
    "caption_language": "",
    "resolution_or_format": "",
    "source_data": "",
    "table_style": ""
  },
  "supplementary_rules": [],
  "unverified_items": []
}
```

## Extraction Rules

- Quote or cite the template text when a rule is important.
- If a field is not present, write `not specified`, not an invented default.
- If using article-type defaults because no template exists, mark the field in `unverified_items`.
- Do not claim compliance until the manuscript or generated file has been checked against the profile.

