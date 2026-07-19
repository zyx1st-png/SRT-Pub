---
id: SRT-EDIT-PROTOCOL
type: framework
tags: [Governance, Editing, Safety, Protocol]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
dependency: [SRT-CANONICAL-FREEZE, SRT-CANONICAL-REGISTRY, SRT-SYMBOL-TABLE]
updated: 2026-06-05
---

# SRT Edit Protocol

> 2026-06-05 scope note: this is an editing workflow. It protects authority boundaries but does not create theory definitions or current book-status facts.

本文件定义 SRT 仓库的三类编辑与最小交叉检查规则。

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
