---
name: srt-structure-extraction
description: SRT 结构治理与接口抽取工作流的触发器——把内容从大文件安全拆进 split/annex，或做 frontmatter 归一化、导航一致性、closure 报告。三段式固定形状：pre-audit（只读盘点+风险分级）→ adjudication（裁决抽哪些、压成最小可承重接口、定主/备/禁止落点）→ extraction record + closure report。适用时机：用户说"把这块从大文件里拆出来 / 做 split / 抽接口 / 归一化 frontmatter / 做领域 closure / 导航审计"。绝不在没有 pre-audit 的情况下机会主义抽取；绝不移动公式/阈值/AI subjecthood/Physics collapse 类高风险 claim（除非已有对应 adjudication）；绝不把 companion/annex 升格为 canonical 定义。理论定义修改、材料融入、文章写作都不走本 skill。
argument-hint: "[目标领域/文件 | pre-audit | 裁决 | 记录 closure]"
---

# SRT 结构治理与接口抽取工作流（触发器）

规范源：`Operations/README.md`（Structure Governance Stop Rule）、`Governance/_SRT_DOC_ENGINEERING_GUIDE.md`、
`Governance/SRT_EDIT_PROTOCOL.md`、`Governance/SRT_CANONICAL_FREEZE.md`、`scripts/governance_preflight.py`。
本 skill 只装三段式骨架与红线，精确判据以上述文档为准。既有先例可参照 `Operations/` 里的
`PR_*` / `Physics_P*` / `AI_*Annex*` 记录（它们全走同一形状）。

## 为什么是三段式（不可跳步）

历史上"顺手就拆"（无 pre-audit 的机会主义抽取）出过问题，才立了 Stop Rule。
所以抽取**必须**先只读盘点、再裁决、才动手，每段留痕。

## 开工前必读

1. `Operations/README.md` 的 **Structure Governance Stop Rule**（当前禁止直接开始的动作清单）
2. `Governance/SRT_EDIT_PROTOCOL.md` + `Governance/SRT_CANONICAL_FREEZE.md`（编辑前必读）
3. `_SRT_AGENT_RETRIEVAL_PROFILE.md`（定检索深度）
4. 目标领域的既有 index / annex 导航文件 + 对应 `CANONICAL_REGISTRY.md` 条目
5. 同类先例（如做 Physics 就读 `Physics_P*` 记录；做 AI 就读 `AI_*Annex*`）

## 三段式流程

### 段 1 · Pre-audit（只读，不改任何文件）

- 盘点目标文件/领域：现有 frontmatter 状态、章节、公式、阈值、claim level、导航链接。
- 对每个候选抽取块做**风险分级**：低风险（纯导航/表述）vs 高风险（公式/阈值/subjecthood/collapse/常数/MWI/离散时间）。
- 产出 `*_PreAudit_*.md` 记录到 `Operations/`：候选清单 + 风险分级 + 建议是否进入 adjudication。
- **高风险块在本段一律不动**，只标记，交给段 2 裁决。

### 段 2 · Adjudication（裁决，仍不改正文；产出裁决记录）

- 对每个候选：能否压成**最小可承重接口命题**？给主落点 / 备选落点 / **禁止落点**。
- 判 claim level，标注 companion 与 canonical 的关系（companion 永不升格为定义源）。
- 产出 `*_Adjudication_*.md`：逐块 A（抽）/ B（暂缓）/ C（不抽）+ 去材料化主句 + 落点。

### 段 3 · Extraction record + Closure

- 只对段 2 判 A 的块执行**最小定向抽取**（配合 `srt-safe-patch` skill，大文件不整文件重写）。
- 抽取后：更新导航/index/registry 链接，运行 `scripts/governance_preflight.py`、
  `scripts/check_frontmatter.py`、`scripts/check_registry_consistency.py` 自查。
- 产出 `*_Extraction_Record_*.md` 与（领域收口时）`*_Closure_Report_*.md`，写清抽了什么、
  留了什么、导航是否一致、是否有 broken link。

## 硬红线

- **无 pre-audit 不抽取**。不做机会主义 opportunistic extraction。
- **不移动**公式、阈值、AI subjecthood/consciousness claim、Physics gravity/constants/collapse/MWI/离散时间 claim——
  除非已有对应 adjudication 明确批准。
- **companion / annex / split / bridge 永不升格为 canonical 定义**；`canonical: false` 不因抽取改变。
- 大文件**最小定向编辑**，不删不重排既有长段；整文件重写用 `srt-safe-patch` 的纪律。
- frontmatter 归一化按 canonical claim_mode 补齐，不擅自改 claim level。
- 抽取只改结构与导航，**不引入新理论**；引入新理论走 canonical 编辑协议，不在本流程里夹带。
