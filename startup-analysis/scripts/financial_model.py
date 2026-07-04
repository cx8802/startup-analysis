#!/usr/bin/env python3
"""Generate a simple startup financial scenario from JSON assumptions."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class Assumptions:
    months: int = 12
    initial_users: float = 1000
    monthly_growth_rate: float = 0.1
    paid_conversion_rate: float = 0.05
    arpu: float = 100.0
    orders_per_user: float = 1.0
    variable_cost_rate: float = 0.2
    fixed_cost: float = 30000.0
    team_cost: float = 0.0
    cac: float = 0.0
    currency: str = "CNY"


def as_rate(value: Any, default: float) -> float:
    if value is None or value == "":
        return default
    number = float(value)
    return number / 100 if number > 1 else number


def as_float(data: dict[str, Any], key: str, default: float) -> float:
    value = data.get(key, default)
    if value is None or value == "":
        return default
    return float(value)


def load_assumptions(path: Path) -> Assumptions:
    if not path.exists():
        raise FileNotFoundError(f"Config file does not exist: {path}")
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("Config JSON must be an object.")

    return Assumptions(
        months=max(1, int(data.get("months", 12))),
        initial_users=as_float(data, "initial_users", 1000),
        monthly_growth_rate=as_rate(data.get("monthly_growth_rate"), 0.1),
        paid_conversion_rate=as_rate(data.get("paid_conversion_rate"), 0.05),
        arpu=as_float(data, "arpu", 100),
        orders_per_user=as_float(data, "orders_per_user", 1),
        variable_cost_rate=as_rate(data.get("variable_cost_rate"), 0.2),
        fixed_cost=as_float(data, "fixed_cost", 30000),
        team_cost=as_float(data, "team_cost", 0),
        cac=as_float(data, "cac", 0),
        currency=str(data.get("currency", "CNY")),
    )


def build_rows(a: Assumptions) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    previous_users = 0.0
    users = a.initial_users

    for month in range(1, a.months + 1):
        if month > 1:
            users *= 1 + a.monthly_growth_rate
        new_users = max(users - previous_users, 0)
        paying_users = users * a.paid_conversion_rate
        revenue = paying_users * a.arpu * a.orders_per_user
        variable_cost = revenue * a.variable_cost_rate
        gross_profit = revenue - variable_cost
        acquisition_cost = new_users * a.cac
        operating_cost = a.fixed_cost + a.team_cost + acquisition_cost
        contribution_profit = gross_profit - operating_cost
        rows.append(
            {
                "month": float(month),
                "active_users": users,
                "new_users": new_users,
                "paying_users": paying_users,
                "revenue": revenue,
                "variable_cost": variable_cost,
                "gross_profit": gross_profit,
                "acquisition_cost": acquisition_cost,
                "operating_cost": operating_cost,
                "contribution_profit": contribution_profit,
            }
        )
        previous_users = users

    return rows


def money(value: float, currency: str) -> str:
    return f"{currency} {value:,.2f}"


def render_markdown(a: Assumptions, rows: list[dict[str, float]]) -> str:
    break_even = next((int(row["month"]) for row in rows if row["contribution_profit"] >= 0), None)
    total_revenue = sum(row["revenue"] for row in rows)
    total_profit = sum(row["contribution_profit"] for row in rows)
    peak_burn = max(max(-row["contribution_profit"], 0) for row in rows)

    lines = [
        "# 财务假设测算",
        "",
        "## 输入假设",
        "",
        f"- 模型周期：{a.months} 个月",
        f"- 初始活跃用户：{a.initial_users:,.0f}",
        f"- 月增长率：{a.monthly_growth_rate:.2%}",
        f"- 付费转化率：{a.paid_conversion_rate:.2%}",
        f"- ARPU：{money(a.arpu, a.currency)}",
        f"- 人均订单/使用次数：{a.orders_per_user:,.2f}",
        f"- 变动成本率：{a.variable_cost_rate:.2%}",
        f"- 固定成本/月：{money(a.fixed_cost, a.currency)}",
        f"- 团队成本/月：{money(a.team_cost, a.currency)}",
        f"- CAC：{money(a.cac, a.currency)}",
        "",
        "## 汇总",
        "",
        f"- 周期总收入：{money(total_revenue, a.currency)}",
        f"- 周期贡献利润：{money(total_profit, a.currency)}",
        f"- 单月最大现金消耗：{money(peak_burn, a.currency)}",
        f"- 盈亏平衡月份：{break_even if break_even else '模型期内未达到'}",
        "",
        "## 月度明细",
        "",
        "| 月份 | 活跃用户 | 付费用户 | 收入 | 毛利 | 获客成本 | 贡献利润 |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for row in rows:
        lines.append(
            "| {month:.0f} | {active_users:,.0f} | {paying_users:,.0f} | {revenue} | {gross_profit} | {acquisition_cost} | {contribution_profit} |".format(
                month=row["month"],
                active_users=row["active_users"],
                paying_users=row["paying_users"],
                revenue=money(row["revenue"], a.currency),
                gross_profit=money(row["gross_profit"], a.currency),
                acquisition_cost=money(row["acquisition_cost"], a.currency),
                contribution_profit=money(row["contribution_profit"], a.currency),
            )
        )

    lines.extend(
        [
            "",
            "## 使用提醒",
            "",
            "该模型是早期场景测算，不是财务预测。请用真实渠道数据、留存数据和销售数据持续校准假设。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a simple startup financial model.")
    parser.add_argument("--config", required=True, help="JSON file containing financial assumptions.")
    parser.add_argument("--output", required=True, help="Markdown output path.")
    args = parser.parse_args()

    assumptions = load_assumptions(Path(args.config))
    rows = build_rows(assumptions)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_markdown(assumptions, rows), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
