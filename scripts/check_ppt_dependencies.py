#!/usr/bin/env python3
"""Check optional dependencies needed for PAPER PPTX generation."""

from __future__ import annotations

import importlib.util
import json


REQUIRED = {
    "fitz": "PyMuPDF",
    "PIL": "Pillow",
    "pptx": "python-pptx",
    "zipfile": "zipfile",
}


def main() -> int:
    available = {}
    missing = []

    for module, package in REQUIRED.items():
        ok = importlib.util.find_spec(module) is not None
        available[package] = ok
        if not ok:
            missing.append(package)

    can_generate_pptx = available["python-pptx"]
    can_extract_pdf_figures = available["PyMuPDF"] and available["Pillow"]

    if can_generate_pptx and can_extract_pdf_figures:
        status = "ready"
        fallback_mode = None
    elif can_generate_pptx:
        status = "partial"
        fallback_mode = "pptx_without_pdf_figure_extraction"
    else:
        status = "fallback"
        fallback_mode = "markdown_outline_with_figure_placeholders"

    print(
        json.dumps(
            {
                "status": status,
                "available": available,
                "missing": missing,
                "fallback_mode": fallback_mode,
            },
            ensure_ascii=True,
            indent=2,
        )
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
