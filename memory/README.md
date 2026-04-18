---
id: SRT-MEMORY-README
type: index
tags: [Memory, Runtime, Context]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-STATUS]
---

# SRT Memory Layer

`memory/` 用于保存**运行短时上下文**，不是理论权威层。

## 用途

- 记录近期会话的关键决策
- 给 agent 提供 today / yesterday 的短期上下文
- 避免重复执行同一段工作

## 不是用来做什么

- 不是 canonical theory source
- 不是主论证入口
- 不是长期历史总档案

## 默认读取规则

- 会话启动时，只读 today + yesterday（如存在）
- 需要 heartbeat / automation 状态时，再看 `heartbeat-state.json`

## 使用边界

若 `memory/` 与 canonical 文件冲突：

- 以 canonical 文件为准
- `memory/` 只作为运行上下文参考

## 后续分层方向

- 主树保留近期 memory
- 更早的 memory 逐步下沉到 `Archive/`
