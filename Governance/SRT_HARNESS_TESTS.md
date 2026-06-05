---
id: SRT-HARNESS-TESTS
type: framework
tags: [Governance, Harness, Tests, AI-Readability]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
dependency: [SRT-AI-START, SRT-INDEX, SRT-NAVIGATION-MAP, SRT-CANONICAL-REGISTRY]
updated: 2026-06-05
---

# SRT Harness Tests

> These tests verify agent entry behavior. They are not theory definitions and should not override `AGENTS.md`.

本文件用于验证入口层优化是否真的降低了 AI 漂移与误读。

## 测试方法

假设新会话只拿到仓库，不额外提供人工解释。

优先观察：

- 首轮读取文件数是否下降
- 是否仍把 bridge / ops log / split 当 canonical
- 是否能稳定回答权威入口与编辑边界

## 第一批固定测试题

| # | 测试题 | 期望最小答案 | 首选锚点 |
|:--|:--|:--|:--|
| 1 | L0 唯一锚点是哪篇？ | `Core_Law/SRT_L0_Metaphysics.md` | `SRT_AI_START.md`, `_SRT_INDEX.md` |
| 2 | d-value 的 canonical 定义去哪看？ | `_SRT_D_VALUE_CANONICAL.md` | `CANONICAL_REGISTRY.md` |
| 3 | `Ψ_f` 的 canonical 定义去哪看？ | `_SRT_PSI_F_CANONICAL.md` | `CANONICAL_REGISTRY.md` |
| 4 | `T_dir` 的 canonical 定义去哪看？ | `_SRT_T_DIR_CANONICAL.md` | `CANONICAL_REGISTRY.md` |
| 5 | 中文主论证候选是哪篇？ | `Core_Law/SRT_Core_Text_CN_Euclid.md` | `SRT_Navigation_Map.md` |
| 6 | 仓库当前运行协议主入口是哪篇？ | `AGENTS.md` | `README.md`, `_SRT_INDEX.md` |
| 7 | Claude 兼容入口是哪篇？ | `CLAUDE.md` | `README.md`, `_SRT_INDEX.md` |
| 8 | 人类阅读地图是哪篇？ | `SRT_Navigation_Map.md` | `_SRT_INDEX.md` |
| 9 | 机器索引是哪篇？ | `_SRT_INDEX.md` | `SRT_AI_START.md`, `README.md` |
| 10 | AI 最小首读入口是哪篇？ | `SRT_AI_START.md` | `README.md`, `_SRT_INDEX.md` |
| 11 | Lab 假说包在哪？ | `Governance/SRT_LAB_HYPOTHESES.md` | `SRT_Navigation_Map.md` |
| 12 | 哪些文件不能直接改？ | canonical freeze 列表中的锚点文件 | `SRT_CANONICAL_FREEZE.md` |

## 典型失败模式

- 把 `Operations/` 日志答成理论主文
- 把 bridge 文件答成定义源
- 把 split / annex README 答成 canonical
- 把 `CLAUDE.md` 误读成新的主协议
- 把 `STATUS.md` 误读成完整历史档案入口

## 通过标准

- 大多数测试题可在少量入口文件内答出
- 回答能稳定区分：
  - public entry
  - runtime protocol
  - AI start
  - machine index
  - human map
  - canonical anchor

若同一问题在连续几次新会话中仍反复答错，说明入口层仍需继续收口。
