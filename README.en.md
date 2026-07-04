# startup-analysis

An open startup analysis project for building reusable workflows, templates, and Python tools around market research, business models, competitors, financial assumptions, and growth strategy.

## Purpose

`startup-analysis` helps founders, product leaders, venture researchers, and indie builders turn a startup idea or early-stage project into a structured analysis report. The project will start with a Codex Skill and then add Python scripts, templates, and examples.

Core outputs include:

- Startup opportunity assessment
- Industry and market analysis
- Customer pain point and solution breakdown
- Competitor matrix and differentiation analysis
- Business model and financial assumptions
- Growth strategy and validation plan
- Investor memo draft

## Current Status

This repository is in the early design stage. The initial Skill design document is available here:

- [Startup Analysis Skill Design](docs/startup-analysis-skill-design.md)

Next steps are to add `SKILL.md`, reference templates, and Python scripts based on the design.

## Planned Structure

```text
startup-analysis/
├── README.md
├── README.en.md
├── docs/
│   └── startup-analysis-skill-design.md
└── startup-analysis/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   ├── analysis-framework.md
    │   ├── report-template.md
    │   ├── metrics-glossary.md
    │   └── investor-memo.md
    └── scripts/
        ├── analyze_inputs.py
        ├── build_report.py
        └── financial_model.py
```

## Planned Capabilities

### Skill Workflow

- Clarify the startup's customer, use case, geography, stage, and constraints.
- Build a question tree across market, problem, solution, competitors, business model, growth, finance, and risk.
- Separate facts, inferences, assumptions, and open validation questions.
- Generate a startup analysis report, investor memo, or validation roadmap.

### Python Tools

- `analyze_inputs.py`: Convert user notes into structured JSON.
- `financial_model.py`: Generate basic financial calculations from key assumptions.
- `build_report.py`: Combine structured inputs, finance outputs, and templates into a Markdown report.

## MVP Roadmap

1. Build the Skill skeleton: `SKILL.md`, `agents/openai.yaml`, and core references.
2. Add report templates: analysis framework, metrics glossary, and investor memo.
3. Implement Python scripts: basic financial model and report generator.
4. Add examples: validate output quality with 2 to 3 startup ideas.
5. Expand research support: competitor matrices, validation experiment design, and audience-specific outputs.

## Usage

The current version is documentation-first. Start with:

```bash
docs/startup-analysis-skill-design.md
```

Once the Skill and scripts are implemented, the intended flow will look like:

```bash
python startup-analysis/scripts/financial_model.py --config assumptions.json --output finance-summary.md
python startup-analysis/scripts/build_report.py --input analysis-input.json --finance finance-summary.md --output report.md
```

## Output Principles

- Clearly separate facts, inferences, and assumptions.
- Explain the reasoning and evidence behind key judgments.
- Provide validation methods for high-uncertainty questions.
- Show financial inputs and assumptions instead of pretending forecasts are precise.
- For current market data, regulations, funding events, or competitor status, verify with up-to-date sources and cite them.

## Contributing

Contributions are welcome, especially:

- Startup analysis frameworks and report templates
- Industry research examples
- Financial model parameters and script improvements
- Competitor analysis templates
- README, documentation, and sample report improvements

Suggested workflow:

1. Fork this repository.
2. Create a feature branch, such as `feat/financial-model`.
3. Commit your code or documentation.
4. Open a Pull Request and describe the purpose and validation method.

## Disclaimer

This project is for startup analysis, strategic research, and learning. It is not investment, legal, financial, tax, or business advice. Any business decision should be supported by primary research, professional advice, and real operating data.
