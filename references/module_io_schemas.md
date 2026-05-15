# PAPER Module I/O Contracts

These are mandatory minimal JSON Schema-style contracts for handoff between PAPER modules. They are documentation schemas, not an executable validator. Required fields must appear in every module output. Use empty arrays or objects when no values exist.

## Shared Enums

```json
{
  "stage": ["paper_type", "paper_plan", "paper_content", "paper_document", "paper_final", "paper_revision", "paper_ppt"],
  "status": ["ready", "partial", "blocked", "fallback"],
  "next_recommended_module": ["paper_type", "paper_plan", "paper_content", "paper_document", "paper_final", "paper_revision", "paper_ppt", "paper_writer", "none"],
  "severity_or_level": ["fatal", "major", "minor", "optional"],
  "risk_flag_code": [
    "missing_evidence",
    "unsupported_claim",
    "template_unknown",
    "citation_weak",
    "dependency_missing",
    "format_risk",
    "body_contamination",
    "consistency_issue",
    "user_confirmation_needed",
    "custom_*"
  ]
}
```

Custom risk codes must start with `custom_`.

## Required Item Shapes

### missing_items item

```json
{
  "id": "string",
  "item": "string",
  "reason": "string",
  "required_for": "string",
  "owner": "user | assistant | unknown",
  "severity": "fatal | major | minor | optional"
}
```

### risk_flags item

```json
{
  "code": "missing_evidence | unsupported_claim | template_unknown | citation_weak | dependency_missing | format_risk | body_contamination | consistency_issue | user_confirmation_needed | custom_*",
  "level": "fatal | major | minor | optional",
  "message": "string",
  "action": "string"
}
```

## Mandatory Base Schema

Every module output must extend this base schema:

```json
{
  "type": "object",
  "required": [
    "stage",
    "status",
    "confirmed_inputs",
    "outputs",
    "missing_items",
    "risk_flags",
    "next_recommended_module"
  ],
  "properties": {
    "stage": {
      "type": "string",
      "enum": ["paper_type", "paper_plan", "paper_content", "paper_document", "paper_final", "paper_revision", "paper_ppt"]
    },
    "status": {
      "type": "string",
      "enum": ["ready", "partial", "blocked", "fallback"]
    },
    "confirmed_inputs": {
      "type": "object"
    },
    "outputs": {
      "type": "object"
    },
    "missing_items": {
      "type": "array",
      "items": "missing_items item"
    },
    "risk_flags": {
      "type": "array",
      "items": "risk_flags item"
    },
    "next_recommended_module": {
      "type": "string",
      "enum": ["paper_type", "paper_plan", "paper_content", "paper_document", "paper_final", "paper_revision", "paper_ppt", "paper_writer", "none"]
    }
  }
}
```

## Extension Rules

- Required base fields must never be omitted.
- Use `[]` or `{}` for required fields that have no current values.
- Modules may add useful fields inside `confirmed_inputs` or `outputs`.
- Unknown optional fields must not replace required fields.
- Do not store manuscript body warnings only in prose; also use `missing_items` or `risk_flags`.
- Use `status="blocked"` when a fatal missing item prevents truthful progress.
- Use `status="fallback"` when dependencies or tooling force a degraded output path.

## paper_type_output

Extends the mandatory base schema.

Required module-specific `outputs` keys:

- `article_type_profile`
- `template_compliance_profile`
- `format_constraints`
- `reference_style`
- `declaration_requirements`

```json
{
  "stage": "paper_type",
  "status": "ready",
  "confirmed_inputs": {
    "manuscript_type": "sci_journal | conference_paper | chinese_journal | master_thesis | general",
    "discipline_domain": "experimental_science | computational_ai | clinical | engineering | humanities_social_science | theoretical_math | review_meta_analysis | other",
    "target_venue": "string",
    "language": "string",
    "output_format": "string",
    "template_source": "string"
  },
  "outputs": {
    "article_type_profile": "sci_journal | conference_paper | chinese_journal | master_thesis | general",
    "template_compliance_profile": {},
    "format_constraints": {},
    "reference_style": "string",
    "declaration_requirements": []
  },
  "missing_items": [],
  "risk_flags": [],
  "next_recommended_module": "paper_plan"
}
```

## paper_plan_output

Extends the mandatory base schema.

Required module-specific `outputs` keys:

- `outline`
- `source_to_section_map`
- `terminology_map`
- `evidence_map`

```json
{
  "stage": "paper_plan",
  "status": "ready",
  "confirmed_inputs": {
    "paper_type_output": {},
    "source_materials": []
  },
  "outputs": {
    "outline": [],
    "source_to_section_map": [],
    "terminology_map": [],
    "evidence_map": []
  },
  "missing_items": [],
  "risk_flags": [],
  "next_recommended_module": "paper_content"
}
```

## paper_content_output

Extends the mandatory base schema.

Required module-specific `outputs` keys:

- `manuscript_text`
- `citation_support_table`
- `logic_gap_report`

Example unsupported citation risk:

```json
{
  "stage": "paper_content",
  "status": "partial",
  "confirmed_inputs": {
    "paper_type_output": {},
    "paper_plan_output": {},
    "target_section": "string"
  },
  "outputs": {
    "manuscript_text": "string",
    "citation_support_table": [],
    "logic_gap_report": []
  },
  "missing_items": [],
  "risk_flags": [
    {
      "code": "citation_weak",
      "level": "major",
      "message": "A cited source lacks extractable quote or data for the claim.",
      "action": "Downgrade to partial support or ask user for full-text evidence."
    }
  ],
  "next_recommended_module": "paper_document"
}
```

## paper_document_output

Extends the mandatory base schema.

Required module-specific `outputs` keys:

- `formatted_files`
- `figure_table_status`
- `formatting_report`

```json
{
  "stage": "paper_document",
  "status": "ready",
  "confirmed_inputs": {
    "paper_type_output": {},
    "paper_content_output": {}
  },
  "outputs": {
    "formatted_files": [],
    "figure_table_status": [],
    "formatting_report": "string"
  },
  "missing_items": [],
  "risk_flags": [],
  "next_recommended_module": "paper_final"
}
```

## paper_final_output

Extends the mandatory base schema.

Required module-specific `outputs` keys:

- `readiness_level`
- `audit_findings`
- `global_consistency_report`
- `article_type_audit`

Example consistency risk:

```json
{
  "stage": "paper_final",
  "status": "partial",
  "confirmed_inputs": {
    "paper_type_output": {},
    "paper_plan_output": {},
    "paper_content_output": {},
    "paper_document_output": {}
  },
  "outputs": {
    "readiness_level": "minor revision required",
    "audit_findings": [],
    "global_consistency_report": [],
    "article_type_audit": []
  },
  "missing_items": [],
  "risk_flags": [
    {
      "code": "consistency_issue",
      "level": "minor",
      "message": "Core method name appears in multiple variants.",
      "action": "Normalize all variants to the confirmed preferred term."
    }
  ],
  "next_recommended_module": "none"
}
```

## paper_revision_output

Extends the mandatory base schema.

Required module-specific `outputs` keys:

- `reviewer_comment_map`
- `response_draft`
- `revision_log`
- `diff_summary`

```json
{
  "stage": "paper_revision",
  "status": "ready",
  "confirmed_inputs": {
    "reviewer_comments": [],
    "manuscript_versions": []
  },
  "outputs": {
    "reviewer_comment_map": [],
    "response_draft": "string",
    "revision_log": [],
    "diff_summary": []
  },
  "missing_items": [],
  "risk_flags": [],
  "next_recommended_module": "paper_final"
}
```

## paper_ppt_output

Extends the mandatory base schema.

Required module-specific `outputs` keys:

- `presentation_file`
- `slides_outline`
- `asset_manifest`
- `ppt_qa_report`

Example dependency fallback:

```json
{
  "stage": "paper_ppt",
  "status": "fallback",
  "confirmed_inputs": {
    "paper_type_output": {},
    "source_materials": [],
    "dependency_check": {}
  },
  "outputs": {
    "presentation_file": "",
    "slides_outline": [],
    "asset_manifest": "",
    "ppt_qa_report": "string"
  },
  "missing_items": [
    {
      "id": "ppt-dep-001",
      "item": "PyMuPDF or python-pptx",
      "reason": "Required dependency is unavailable.",
      "required_for": "PPTX generation",
      "owner": "user",
      "severity": "major"
    }
  ],
  "risk_flags": [
    {
      "code": "dependency_missing",
      "level": "major",
      "message": "PPTX generation cannot run in the current environment.",
      "action": "Output Markdown slide outline with figure placeholders."
    }
  ],
  "next_recommended_module": "none"
}
```
