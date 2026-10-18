---
id: SRT-EDIT-PROTOCOL
type: framework
tags: [Governance, Editing, Safety, Protocol]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
dependency: [SRT-CANONICAL-FREEZE, SRT-CANONICAL-REGISTRY, SRT-SYMBOL-TABLE, SRT-MAIN-WRITE-GOVERNANCE]
updated: 2026-09-24
---

# SRT Edit Protocol

> 2026-06-05 scope note: this is an editing workflow. It protects authority boundaries but does not create theory definitions or current book-status facts.

本文件定义 SRT 仓库的三类编辑与最小交叉检查规则。

> **Two-axis guard (2026-09-24):** 本文件的 A/B/C 是**编辑风险 / 语义风险**分类；`SRT_MAIN_WRITE_GOVERNANCE.md` 的 M0/M1/M2 是**授权 / 裁决模式**分类。两者正交，不得互相替代。一个 A 类编辑仍可能因改变 CURRENT NEXT / authority 而成为 M2；一个 C 类编辑在已有显性 bounded author authorization 下仍须执行本文件的 C 类独立复审。

## A 类：安全编辑

典型内容：

- 补 `Quick Reference`
- 补导航回链
- 修 typo / 断链 / 标题格式
- 补 frontmatter 辅助字段
- 更新 `README.md` / `AGENTS.md` / `SRT_AI_START.md` / `_SRT_INDEX.md`
- 更新治理入口、归档索引、工具 baseline

默认要求：

- 不改变理论定义
- 不改变 canonical 优先级
- 不改变公理/方程语义

## B 类：谨慎编辑

典型内容：

- 收紧 bridge 文件口径
- 压缩 compact core 说明
- 调整入口层职责
- 重写状态面板结构
- 调整 manifest / registry / navigation 关系

默认要求：

1. 核对是否影响权威层级
2. 核对是否把展开层误写成定义层
3. 核对是否影响已有回链

## C 类：高风险编辑

典型内容：

- 改 canonical 定义
- 改核心公理/方程
- 改 L0 主文负担
- 改 d / `Ψ_f` / `T_dir` 主定义
- 改中文主论证核心链条

高风险编辑必须做三项交叉检查：

1. `_SRT_SYMBOL_TABLE.md`
2. 对应 canonical file
3. 相关主文 / compact core / registry 回链

### C 类语义编辑的 pre-merge 独立复审

对 **C 类 / foundation-level canonical semantic edit**，上述交叉检查之外，还必须在 merge 前完成一次独立内容复审。

最低要求：

1. 先形成可审的 final semantic diff / target head；
2. 复审者不能与同一 semantic edit pass 混为一体；可由作者本人、独立人工 reviewer，或独立 session / model context 执行，但必须能重新读取 owner / source / OPEN guards，而不是仅复述编辑者结论；
3. 复审记录至少写明 target head、控制 owner / source、PASS / REVISE / FAIL 判据，以及被刻意保持 OPEN 的问题；
4. 只要结论为 REVISE / FAIL，该 canonical semantic edit 就不得 merge；
5. 语义 head 已独立 PASS 后的纯 mechanical / deterministic generated closure 可单独提交；但生成面仍须通过 owning generator / consistency check，不得手改制造一致。

这条规则不把普通 A/B 类编辑升级成 C 类，也不要求为纯 typo、导航、版本号或 deterministic regeneration 重复做内容复审。

### Same-day rapid author-dialogue guard

当同一天的 author dialogue 仍在快速生成、修正或相互覆盖 foundation-level 概念时：

~~~text
dialogue / analysis
-> source-intuition / adjudication record
-> bounded conflict / OPEN map
-> only then consider Freeze-A semantic landing
~~~

在该对话尚未形成稳定的 bounded author decision 之前，不得直接把其中的新定义 / 新判据 / 新等价关系写入 Freeze-A canonical owner。

允许例外仅限：

- 已有明确作者裁决足以机械执行的 bounded correction；
- typo / link / metadata / provenance-only 等不改变理论语义的编辑；
- 为防止下游误读而做的 fail-closed guard，但该 guard 不得替作者关闭尚未裁决的理论问题。

目的不是延迟作者直觉，而是防止同日仍在演化的 machine consolidation 被过早固化成 canonical authority。

## 默认工作流

### 1. 先判断文件类型

- canonical anchor
- core main text
- bridge / compact / split / annex
- status / index / runtime / governance

### 2. 再判断编辑级别

- 不改理论定义 → A 类
- 影响入口层或桥接口径 → B 类
- 影响理论核心定义 → C 类

### 3. 最后决定留痕位置

- fresh-session / agent read order → `AGENTS.md`
- current status → `STATUS.md`（§Fast Status 兼任 compact 入口）
- historical status → `Operations/Status_History/`
- 运行流水线、材料、信号、队列 → `Operations/`
- 治理规则、质量 baseline、归档说明 → `Governance/`
- 当前书稿事实 → `01_Source_Intuition/BOOK/` 当前正文与当前 book meta 文件

## 明确禁止

- 用 bridge 文件替代 canonical 定义
- 用运行日志替代理论主文
- 在导航文件里偷偷新增理论口径
- 在未 cross-check 的情况下改写核心定义

## 进入高风险编辑前的最小问题

动笔前至少回答：

1. 这次改的是定义、展开，还是导航？
2. 真正的 canonical source 是哪篇？
3. 是否会让 AI 把非权威文件误读成权威文件？

只要第三问答案可能是“会”，就不能按 A 类处理。

## Book and Governance Boundary

Book drafts and book meta files are writing context unless they explicitly declare otherwise. Governance files may guide editing workflow, but they must not be used as the primary basis for judging the current book's literary or argumentative quality.
