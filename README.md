# startup-analysis

公开创业分析项目：围绕行业研究、商业模式、竞品、财务假设与增长策略，沉淀一套可复用的创业分析 Skill 与 Python 工具。

## 项目定位

`startup-analysis` 旨在帮助创始人、产品负责人、投资研究者和独立开发者，把一个创业想法或早期项目拆解成结构化分析报告。项目会优先建设 Codex Skill，再逐步补齐 Python 脚本、模板和样例数据。

核心输出包括：

- 创业机会评估
- 行业与市场分析
- 用户痛点与解决方案拆解
- 竞品矩阵与差异化判断
- 商业模式与财务假设
- 增长策略与验证计划
- 投资备忘录草稿

## 当前状态

项目处于早期设计阶段。已完成创业分析 Skill 的设计文档：

- [创业分析 Skill 项目设计](docs/startup-analysis-skill-design.md)

后续会基于该设计补充 `SKILL.md`、参考模板和 Python 脚本。

## 规划目录

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

## 计划能力

### Skill 工作流

- 澄清创业项目的目标用户、场景、地区、阶段和约束。
- 按市场、痛点、方案、竞品、商业模式、增长、财务、风险建立问题树。
- 区分事实、推断、假设和待验证问题。
- 输出创业分析报告、投资备忘录或验证路线图。

### Python 工具

- `analyze_inputs.py`：把用户笔记整理成结构化 JSON。
- `financial_model.py`：根据关键假设生成基础财务测算。
- `build_report.py`：合并结构化输入、财务结果和模板，生成 Markdown 报告。

## MVP 路线

1. 完成 Skill 骨架：`SKILL.md`、`agents/openai.yaml`、核心参考文档。
2. 完成报告模板：分析框架、指标词汇表、投资备忘录模板。
3. 完成 Python 脚本：基础财务模型和报告生成器。
4. 添加样例：用 2 到 3 个创业想法验证输出质量。
5. 增强研究能力：支持竞品矩阵、验证实验设计和多读者输出模式。

## 使用方式

当前版本以文档为主，可先阅读：

```bash
docs/startup-analysis-skill-design.md
```

当 Skill 与脚本完成后，推荐流程会是：

```bash
python startup-analysis/scripts/financial_model.py --config assumptions.json --output finance-summary.md
python startup-analysis/scripts/build_report.py --input analysis-input.json --finance finance-summary.md --output report.md
```

## 输出原则

- 明确区分事实、推断和假设。
- 对关键判断给出理由和证据来源。
- 对高不确定性问题给出验证方法。
- 财务模型展示输入假设，不伪装成精确预测。
- 涉及实时市场、法规、融资事件和竞品状态时，应联网核实并标注来源。

## 贡献方式

欢迎提交以下内容：

- 创业分析框架和报告模板
- 行业研究样例
- 财务模型参数和脚本改进
- 竞品分析模板
- README、文档和示例报告优化

建议流程：

1. Fork 本仓库。
2. 新建功能分支，例如 `feat/financial-model`。
3. 提交代码或文档。
4. 发起 Pull Request，并说明变更目的和验证方式。

## 免责声明

本项目用于创业分析、战略研究和学习参考，不构成投资、法律、财务、税务或经营建议。任何商业决策都应结合一手调研、专业意见和实际经营数据。
