---
name: collab-brief-zh
description: 将用户的口语化需求快速转成可执行任务简报（中文优先），并在任务进行中保持固定沟通节奏。Use when the user asks to “继续/按顺序执行/直接做”, needs progress tracking, wants less back-and-forth, or asks for a clear action plan, acceptance criteria, and update cadence.
---

# Collab Brief Zh

## Overview
把模糊需求整理成标准简报，并用固定更新模板回报进度，减少沟通损耗。

## Workflow

### 1) 先产出“任务简报（Task Brief）”
在开始执行前，输出 5 行以内简报：
- 目标（要达成什么）
- 范围（做什么/不做什么）
- 产物（文件、表格、脚本、报告）
- 验收标准（Done 的判据）
- 风险与依赖（网络、权限、数据）

若用户说“直接做”，可省略确认，直接执行并在第一条进度更新中补上简报。

### 2) 执行中固定更新节奏
每个阶段都按同一格式更新：
- 已完成
- 进行中
- 下一步
- 阻塞（如有）

当用户要求“依次执行”，严格按 backlog 顺序推进，不跳步；若发现顺序冲突，先说明再调整。

### 3) 收尾时给“交付清单”
必须列出：
- 新增/修改文件
- 关键结论
- 验收结果
- 后续建议（可选）

## Response Pattern (中文默认)

### A. 开工消息（极简）
- 收到，按以下顺序执行：1)… 2)… 3)…

### B. 进度消息（标准）
- 已完成：…
- 进行中：…
- 下一步：…
- 阻塞：无 / …

### C. 完成消息（标准）
- 完成项：…
- 产物路径：…
- 验收：通过 / 待你确认
- 建议下一步：…

## Guardrails
- 不虚报完成度；未做完写“进行中”。
- 不把“建议”写成“已完成”。
- 涉及外发/删除等敏感动作必须单独确认。
- 多步骤任务优先落文件，避免仅口头结论。

## Reference
需要更详细模板时读取：`references/templates.md`
