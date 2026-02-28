---
id: SRT-PROJ-OPT-2026Q1
type: framework
tags: [Project, Optimization, Documentation]
status: planning_v1
dependency: [_SRT_DOC_ENGINEERING_GUIDE, _SRT_MANIFEST]
---

# SRT 内部优化总计划（2026Q1）

更新时间：2026-02-28  
状态：Planning v1（可直接转执行）

---

## 0) 目标与原则

本计划用于系统提升 SRT 文档体系在以下四个维度的质量：

1. **专业性（Professionalism）**：概念一致、引用可追溯、推导可审计。  
2. **解释性（Explainability）**：读者可快速建立“定义→机制→证伪”理解路径。  
3. **可扩展性（Scalability）**：新增领域可无冲突接入，索引与依赖自动更新。  
4. **AI 理解性（AI Readability）**：结构稳定、元数据齐全、跨文件语义可解析。

核心约束：
- `Core_Law/` 作为最高规范层（不承载杂项）。
- d 值 canonical 只认 `AI/SRT_AI_01_Ontology.md`。
- 所有新术语必须具备 `[Lineage/Source]`。
- 所有关键主张必须可定位到“方程/假设/边界”。

---

## 1) 现状诊断（基于当前仓库结构）

### A. 结构层问题
- 目录存在历史遗留别名路径与“同义文件名映射”，阅读成本高。
- `SRT/_SRT_INDEX.md` 体量过大，混合了：索引、增量日志、历史变更、旧路径兼容说明。
- 存在 `.DS_Store` 噪声文件（多目录）。

### B. 元数据层问题
- `_SRT_DOC_ENGINEERING_GUIDE.md` 要求 frontmatter，但当前大量文档未统一。
- `_SRT_MANIFEST.yaml` 已建立，但未形成稳定自动化流水线（项目中未见 `scripts/`）。

### C. 内容层问题
- 核心公理、核心方程、领域扩展之间的“映射表”仍偏分散。
- 新增条目速度快于“术语去重/依赖规范化”速度，未来有漂移风险。

### D. AI 可读性问题
- 同一概念在不同文档可能出现多种表述风格（虽多已改善，但仍有残差）。
- 机器抽取时，`索引信息` 与 `理论正文` 混合，容易误检为同层知识。

---

## 2) 目标架构（建议）

建议将 SRT 文档体系分为 5 层：

1. **L0 Canonical Law Layer（规范层）**  
   - 路径：`Core_Law/`
   - 仅存放：公理、核心定义、跨尺度总映射。

2. **L1 Core Theory Layer（核心理论层）**  
   - 路径：`Core/`
   - 存放：本体论、算子、动力学、方程、实验核心。

3. **L2 Domain Layer（领域扩展层）**  
   - 路径：`Physics/ Neuroscience/ Philosophy/ AI/ Spirituality/`
   - 要求：每个领域文档必须引用至少一个 Core 或 Core_Law canonical 条目。

4. **L3 Evidence & Experiment Layer（证据与实验层）**  
   - 路径：`SRT_EXP_*` + `diff.md`（外部材料映射流水）
   - 要求：假设、指标、证伪条件统一模板。

5. **L4 Ops & Registry Layer（工程层）**  
   - 路径：`_SRT_INDEX.md`, `_SRT_MANIFEST.yaml`, `_SRT_SYMBOL_TABLE.md`
   - 要求：仅做索引与注册，不承载理论正文。

---

## 3) 优先级任务清单（可执行）

## P0（1周内）——稳定性与一致性

### P0-1 索引解耦（强烈建议）
- 新建：`SRT/_SRT_CHANGELOG_2026.md`
- 动作：把 `_SRT_INDEX.md` 中大段历史增量日志迁移至 changelog。
- 目标：`_SRT_INDEX.md` 只保留导航与入口，不再混入长篇历史。

### P0-2 元数据最小闭环
- 为所有入口文档补齐 YAML frontmatter：`id/type/tags/status/dependency`。
- 建立 `SRT/_SRT_FRONTMATTER_AUDIT.md`，列出覆盖率与缺失项。

### P0-3 仓库卫生
- 删除全部 `.DS_Store`。
- 新增 `.gitignore` 规则防止再次进入版本库。

---

## P1（2~3周）——解释链重构

### P1-1 核心解释链统一（Definition → Mechanism → Falsification）
- 新建：`SRT/_SRT_EXPLANATION_PROTOCOL.md`
- 规定每个核心条目必须含 5 段：
  1) 定义
  2) 形式化
  3) 机制解释
  4) 可证伪条件
  5) 边界声明

### P1-2 方程-假设-实验三联映射
- 新建：`SRT/_SRT_EQ_HYP_MAP.md`
- 把 `SRT_Core_22_Equations.md` 的关键方程映射到 `SRT_Experimental_Core.md` 的假设编号。

### P1-3 术语治理升级
- 在 `SRT_Glossary.md` 增加字段：
  - `Canonical Scope`
  - `Confusable With`
  - `Lineage/Source`
- 优先处理高频高风险术语：`d, Ψ_f, Ĝθ, L_0/L_1/L_2, ii, RLI/EDPS/COF`。

---

## P2（3~5周）——可扩展与自动化

### P2-1 自动化脚本落地（补齐当前缺失）
建议新增 `scripts/`：
- `srt_lint_frontmatter.py`：frontmatter 合规检查
- `srt_check_links.py`：跨文档链接检查
- `srt_check_symbols.py`：符号冲突检查
- `srt_build_index.py`：从 manifest 生成索引区块

### P2-2 领域接入模板化
- 新建：`SRT/_SRT_DOMAIN_TEMPLATE.md`
- 新增领域文档必须按模板生成，确保 AI 可解析结构一致。

### P2-3 diff 流水线规范化
- 新建：`SRT/_SRT_DIFF_PIPELINE_GUIDE.md`
- 固定格式：Target Files → Unified Diff → Boundary Header → Validation Hooks。

---

## P3（持续）——质量评估与发布

### P3-1 质量评分卡（每周）
新建：`SRT/_SRT_QUALITY_SCORECARD.md`，指标建议：
- 元数据覆盖率
- 断链率
- 术语冲突率
- 可证伪条目覆盖率
- 边界声明覆盖率

### P3-2 发布节奏
- 每两周一次 `SRT Release Note`（文档架构变化、理论变化、实验变化分开记录）。

---

## 4) 重构建议（文件级）

### 建议新建
- `SRT/_SRT_CHANGELOG_2026.md`
- `SRT/_SRT_FRONTMATTER_AUDIT.md`
- `SRT/_SRT_EXPLANATION_PROTOCOL.md`
- `SRT/_SRT_EQ_HYP_MAP.md`
- `SRT/_SRT_DOMAIN_TEMPLATE.md`
- `SRT/_SRT_DIFF_PIPELINE_GUIDE.md`
- `SRT/_SRT_QUALITY_SCORECARD.md`

### 建议调整
- `_SRT_INDEX.md`：仅保留导航，迁移历史长日志。
- `SRT_Glossary.md`：扩展字段，减少语义漂移。

### 建议删除/清理
- 全目录 `.DS_Store`。

---

## 5) AI 友好优化（针对后续协作）

1. 所有核心文档标题级别固定（H1 唯一、H2语义稳定）。
2. 每个方程紧邻“含义句 + 变量表”。
3. 每个新条目添加 `Depends-On: [IDs...]`。
4. 对外部预印本条目增加 `Evidence-Level: preprint|peer-reviewed|editorial`。
5. 强制 `## 【理论边界/防误用声明】` 为正式 header（你当前流程已满足）。

---

## 6) 推荐执行顺序（最小阻力）

1. 先做 P0-3（仓库卫生）
2. 再做 P0-1（索引解耦）
3. 同步做 P0-2（frontmatter覆盖）
4. 进入 P1（解释链与方程-假设映射）
5. 最后做 P2（自动化与模板化）

---

## 7) 完成定义（Definition of Done）

当以下条件全部满足，视为“内部优化一期完成”：
- 索引与变更日志解耦完成
- 入口文档 frontmatter 覆盖率 ≥ 95%
- 关键术语冲突清单清零（或有明确别名声明）
- 方程-假设映射覆盖核心方程 ≥ 80%
- 自动化检查脚本可一键运行并输出报告

---

如需，我可直接进入执行模式，从 **P0-3 + P0-1** 开始落地（含文件创建、迁移、清理、提交）。
