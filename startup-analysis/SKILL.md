---
name: startup-analysis
description: Startup and venture analysis workflow for evaluating startup ideas, companies, products, markets, competitors, business models, financial assumptions, growth strategy, risks, validation plans, and investor memo drafts. Use when Codex needs to analyze an early-stage venture, pitch plan, product opportunity, business idea, or market entry strategy.
---

# Startup Analysis

Use this skill to turn an idea, company, market, or pitch into a structured startup analysis. Keep judgments evidence-aware: separate facts, assumptions, inferences, and unknowns.

## Workflow

1. Clarify the object of analysis: startup name, one-liner, target customer, geography, stage, constraints, and requested output.
2. Build the question tree: market, customer pain, solution, competitors, business model, growth, financial assumptions, risks, and validation.
3. Gather evidence from user-provided material first. For current market data, regulations, funding events, competitor status, or pricing, browse and cite sources.
4. Use `references/analysis-framework.md` to structure reasoning.
5. Use scripts when deterministic processing helps:
   - `scripts/analyze_inputs.py` to turn rough notes into JSON.
   - `scripts/financial_model.py` to calculate a transparent baseline financial model.
   - `scripts/build_report.py` to assemble a Markdown report from JSON, finance output, and a template.
6. Produce the final answer in the format the user needs: founder brief, investor memo, validation plan, or full startup analysis report.

## Output Rules

- Label facts, assumptions, inferences, and open questions.
- Give reasons for key judgments instead of only conclusions.
- Prefer ranges and sensitivity notes for uncertain numbers.
- Treat financial output as scenario modeling, not a prediction.
- End with concrete next validation steps when the user asks for strategy or feasibility.

## References

- `references/analysis-framework.md`: load for full analysis dimensions and scoring guidance.
- `references/report-template.md`: use when generating a full startup analysis report.
- `references/metrics-glossary.md`: use when explaining startup metrics or financial assumptions.
- `references/investor-memo.md`: use when drafting investor-facing analysis.

## Script Quick Start

```bash
python startup-analysis/scripts/analyze_inputs.py --input notes.md --output analysis-input.json
python startup-analysis/scripts/financial_model.py --config assumptions.json --output finance-summary.md
python startup-analysis/scripts/build_report.py --input analysis-input.json --finance finance-summary.md --template startup-analysis/references/report-template.md --output report.md
```
