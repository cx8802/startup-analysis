# 创业分析 Skill 项目设计

## 目标

构建一个面向创业项目评估的 Codex Skill，帮助用户系统化完成行业研究、商业模式拆解、竞品分析、财务假设、增长策略和投资备忘录草稿。项目可使用 Python 提供可复用脚本，让分析流程更稳定、可追溯、可重复。

## 使用场景

- 用户给出一个创业想法，要求判断市场机会、风险和切入点。
- 用户提供公司、产品或赛道名称，要求生成竞品矩阵和差异化建议。
- 用户已有粗略商业计划，要求补齐收入模型、成本结构和关键假设。
- 用户准备融资材料，要求生成投资人视角的分析摘要、风险清单和下一步验证计划。
- 用户希望把零散调研资料整理成结构化创业分析报告。

## Skill 范围

### 包含

- 标准化创业分析工作流。
- 可复用报告结构和判断框架。
- Python 脚本用于整理输入、生成分析骨架、计算基础财务假设。
- 参考文档用于保存分析框架、指标定义和输出模板。

### 暂不包含

- 自动保证实时数据准确性。
- 替代法律、财务、投资或税务专业意见。
- 自动抓取付费数据库或绕过网站访问限制。
- 对创业项目给出确定性成败结论。

## 推荐目录结构

```text
startup-analysis/
├── README.md
├── README.en.md
├── docs/
│   └── 创业分析Skill项目设计.md
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

## Skill 触发描述草案

```yaml
name: startup-analysis
description: Startup and venture analysis workflow for evaluating ideas, markets, competitors, business models, financial assumptions, growth strategy, risks, and investor memo drafts. Use when Codex needs to analyze a startup idea, company, product, market opportunity, pitch plan, or early-stage venture strategy.
```

## 核心工作流

1. 澄清分析对象：一句话描述项目、目标用户、场景、地区、阶段和约束。
2. 建立问题树：市场、用户痛点、解决方案、竞品、商业模式、获客、财务、风险。
3. 收集证据：区分用户提供资料、公开资料、合理假设和待验证假设。
4. 形成判断：输出机会评级、关键不确定性、优势、劣势和进入策略。
5. 建模验证：用 Python 对收入、成本、转化率、客单价、留存等假设做基础测算。
6. 生成报告：按目标读者输出创业分析报告、投资备忘录或验证路线图。

## Python 脚本设计

### analyze_inputs.py

用途：把用户提供的想法、资料或笔记整理成结构化 JSON。

建议输入：

```bash
python scripts/analyze_inputs.py --input notes.md --output analysis-input.json
```

建议输出字段：

- `startup_name`
- `one_liner`
- `target_customer`
- `problem`
- `solution`
- `market`
- `competitors`
- `business_model`
- `known_facts`
- `assumptions`
- `open_questions`

### financial_model.py

用途：根据基础假设计算粗略财务模型，不追求复杂会计建模，优先让假设透明。

建议输入：

```bash
python scripts/financial_model.py --config assumptions.json --output finance-summary.md
```

建议支持指标：

- 收入：用户数、付费率、ARPU、订单频次。
- 成本：固定成本、变动成本、CAC、人力成本。
- 增长：月增长率、留存率、流失率。
- 输出：月收入、毛利、贡献利润、现金消耗、盈亏平衡点。

### build_report.py

用途：把结构化输入、财务模型和模板合并为 Markdown 报告。

建议输入：

```bash
python scripts/build_report.py --input analysis-input.json --finance finance-summary.md --template references/report-template.md --output report.md
```

## 参考文档设计

### analysis-framework.md

保存核心分析框架：

- 市场吸引力：规模、增长、利润池、监管、周期性。
- 用户痛点：频率、强度、预算、替代方案、决策链。
- 产品可行性：技术难度、交付复杂度、用户体验门槛。
- 商业模式：收入来源、定价、毛利、回款周期、扩张边际。
- 竞争格局：直接竞品、间接替代、进入壁垒、差异化。
- 增长策略：获客渠道、转化路径、留存机制、推荐机制。
- 风险：市场、产品、团队、财务、合规、执行。

### report-template.md

保存标准报告结构：

1. 执行摘要
2. 项目概述
3. 用户与痛点
4. 市场机会
5. 竞品与替代方案
6. 商业模式
7. 财务假设
8. 增长策略
9. 关键风险
10. 验证计划
11. 结论与建议

### metrics-glossary.md

保存常用指标定义和使用提醒：

- TAM、SAM、SOM
- CAC、LTV、LTV/CAC
- ARPU、ARPA、AOV
- Gross Margin
- Payback Period
- Churn、Retention
- Activation Rate
- Conversion Rate

### investor-memo.md

保存投资人视角输出模板：

- Why now
- Why this team
- Why this market
- Why this wedge
- Key upside
- Key risks
- Diligence questions
- Suggested next milestones

## 输出质量标准

- 明确区分事实、推断和假设。
- 对关键判断给出理由，而不是只给结论。
- 对不确定问题给出验证方法。
- 财务模型必须展示输入假设。
- 报告应可执行，结尾给出下一步行动清单。
- 涉及实时市场数据、法规、融资事件或竞品状态时，应优先联网核实并标注来源。

## MVP 路线

### 第一阶段：文档与 Skill 骨架

- 完成项目设计文档。
- 创建 `startup-analysis/SKILL.md`。
- 添加 `references/report-template.md` 和 `references/analysis-framework.md`。
- 生成 `agents/openai.yaml`。

### 第二阶段：Python 脚本

- 实现 `financial_model.py`。
- 实现 `build_report.py`。
- 添加最小样例输入和输出。
- 用本地样例跑通脚本。

### 第三阶段：增强分析能力

- 增加竞品矩阵模板。
- 增加验证实验设计模板。
- 增加面向不同读者的输出模式：创始人、投资人、顾问、内部战略。

## 验证方式

- 使用 `quick_validate.py` 校验 Skill 元数据。
- 用 2 到 3 个样例创业想法测试输出是否稳定。
- 检查报告是否包含事实、假设、风险和下一步验证。
- 检查 Python 脚本在缺失字段、空输入和异常参数下是否给出清晰错误。

## 待确认问题

- Skill 最终要放在仓库内，还是安装到用户本机 `~/.codex/skills`？
- 报告默认使用中文，还是中英双语？
- 第一版是否需要联网研究工作流，还是先只处理用户提供资料？
- 财务模型优先支持 SaaS、电商、内容社区、AI 工具，还是通用参数化模型？
