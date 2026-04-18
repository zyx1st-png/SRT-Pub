---
id: SRT-EDIT-PROTOCOL
type: framework
tags: [Governance, Editing, Safety, Protocol]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-CANONICAL-FREEZE, SRT-CANONICAL-REGISTRY, SRT-SYMBOL-TABLE]
---

# SRT Edit Protocol

本文件定义 SRT 仓库的三类编辑与最小交叉检查规则。

## A 类：安全编辑

典型内容：

- 补 `Quick Reference`
- 补导航回链
- 修 typo / 断链 / 标题格式
- 补 frontmatter 辅助字段
- 更新 `README.md` / `STATUS.md` / `_SRT_INDEX.md`

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

- 当前状态变化 → `STATUS.md`
- 运行流水线变化 → `Operations/`
- 治理与规则变化 → `Governance/`

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
