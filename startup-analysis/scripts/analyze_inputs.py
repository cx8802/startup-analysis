#!/usr/bin/env python3
"""Convert rough startup notes into a structured JSON input file."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


FIELDS: dict[str, list[str]] = {
    "startup_name": ["startup_name", "name", "项目名称", "公司名称", "名称"],
    "one_liner": ["one_liner", "summary", "一句话", "简介", "概述"],
    "target_customer": ["target_customer", "customer", "用户", "客户", "目标客户"],
    "problem": ["problem", "pain", "痛点", "问题"],
    "solution": ["solution", "product", "方案", "解决方案", "产品"],
    "market": ["market", "industry", "市场", "行业"],
    "competitors": ["competitors", "competition", "竞品", "竞争"],
    "business_model": ["business_model", "revenue", "商业模式", "收入模式"],
    "known_facts": ["known_facts", "facts", "事实", "已知事实"],
    "assumptions": ["assumptions", "假设", "关键假设"],
    "open_questions": ["open_questions", "questions", "待验证问题", "开放问题"],
}

DEFAULT_OUTPUT: dict[str, Any] = {
    "startup_name": "",
    "one_liner": "",
    "target_customer": "",
    "problem": "",
    "solution": "",
    "market": "",
    "competitors": [],
    "business_model": "",
    "known_facts": [],
    "assumptions": [],
    "open_questions": [],
    "opportunity_rating": "待评估",
    "key_findings": [],
    "customer_analysis": "",
    "market_analysis": "",
    "business_model_analysis": "",
    "growth_strategy": "",
    "risks": [],
    "validation_plan": [],
    "recommendation": "",
}


def normalize_heading(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"^[#\s]+", "", value)
    value = re.sub(r"[:：]\s*$", "", value)
    return value


def field_for_heading(heading: str) -> str | None:
    normalized = normalize_heading(heading)
    for field, aliases in FIELDS.items():
        if normalized in [alias.lower() for alias in aliases]:
            return field
    return None


def split_markdown_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current = "raw_notes"
    sections[current] = []

    for line in text.splitlines():
        heading_match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", line)
        if heading_match:
            current = heading_match.group(1).strip()
            sections.setdefault(current, [])
            continue
        sections.setdefault(current, []).append(line)

    return {key: "\n".join(value).strip() for key, value in sections.items() if "\n".join(value).strip()}


def parse_list_or_text(value: str) -> list[str] | str:
    bullet_lines = []
    other_lines = []
    for line in value.splitlines():
        stripped = line.strip()
        bullet_match = re.match(r"^[-*+]\s+(.+)$", stripped)
        numbered_match = re.match(r"^\d+[.)]\s+(.+)$", stripped)
        if bullet_match:
            bullet_lines.append(bullet_match.group(1).strip())
        elif numbered_match:
            bullet_lines.append(numbered_match.group(1).strip())
        elif stripped:
            other_lines.append(stripped)

    if bullet_lines and not other_lines:
        return bullet_lines
    return value.strip()


def parse_key_value_lines(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^\s*([^:：]{1,40})\s*[:：]\s*(.+?)\s*$", line)
        if match:
            field = field_for_heading(match.group(1))
            if field:
                result[field] = match.group(2).strip()
    return result


def structure_notes(text: str) -> dict[str, Any]:
    output = dict(DEFAULT_OUTPUT)
    sections = split_markdown_sections(text)

    for heading, content in sections.items():
        field = field_for_heading(heading)
        if field:
            output[field] = parse_list_or_text(content)

    for field, value in parse_key_value_lines(text).items():
        if not output.get(field):
            output[field] = value

    if sections.get("raw_notes"):
        output["known_facts"] = output["known_facts"] or []
        if isinstance(output["known_facts"], list):
            output["known_facts"].append("原始笔记已保留在 raw_notes 字段。")
        output["raw_notes"] = sections["raw_notes"]

    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Structure rough startup notes as JSON.")
    parser.add_argument("--input", required=True, help="Path to a Markdown or text notes file.")
    parser.add_argument("--output", required=True, help="Path to write structured JSON.")
    parser.add_argument("--pretty", action="store_true", help="Write indented JSON. Enabled by default for readability.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        parser.error(f"Input file does not exist: {input_path}")

    data = structure_notes(input_path.read_text(encoding="utf-8-sig"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
