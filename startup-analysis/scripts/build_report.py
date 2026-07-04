#!/usr/bin/env python3
"""Build a Markdown startup analysis report from structured inputs."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


DEFAULT_TEMPLATE = Path(__file__).resolve().parents[1] / "references" / "report-template.md"


def stringify(value: Any) -> str:
    if value is None:
        return "待补充"
    if isinstance(value, list):
        if not value:
            return "待补充"
        return "\n".join(f"- {item}" for item in value)
    if isinstance(value, dict):
        if not value:
            return "待补充"
        return "\n".join(f"- {key}: {stringify(item)}" for key, item in value.items())
    text = str(value).strip()
    return text if text else "待补充"


def render_template(template: str, context: dict[str, Any]) -> str:
    def replace(match: re.Match[str]) -> str:
        key = match.group(1).strip()
        return stringify(context.get(key))

    return re.sub(r"{{\s*([a-zA-Z0-9_]+)\s*}}", replace, template)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a startup analysis Markdown report.")
    parser.add_argument("--input", required=True, help="Structured JSON input from analyze_inputs.py or manual editing.")
    parser.add_argument("--finance", help="Optional Markdown finance summary.")
    parser.add_argument("--template", default=str(DEFAULT_TEMPLATE), help="Markdown template with {{placeholders}}.")
    parser.add_argument("--output", required=True, help="Path to write the final report.")
    args = parser.parse_args()

    input_path = Path(args.input)
    template_path = Path(args.template)
    output_path = Path(args.output)

    if not input_path.exists():
        parser.error(f"Input JSON does not exist: {input_path}")
    if not template_path.exists():
        parser.error(f"Template file does not exist: {template_path}")

    context = json.loads(input_path.read_text(encoding="utf-8-sig"))
    if not isinstance(context, dict):
        parser.error("Input JSON must be an object.")

    if args.finance:
        finance_path = Path(args.finance)
        if not finance_path.exists():
            parser.error(f"Finance summary does not exist: {finance_path}")
        context["finance_summary"] = finance_path.read_text(encoding="utf-8-sig").strip()
    else:
        context.setdefault("finance_summary", "待补充")

    rendered = render_template(template_path.read_text(encoding="utf-8"), context)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered.rstrip() + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
