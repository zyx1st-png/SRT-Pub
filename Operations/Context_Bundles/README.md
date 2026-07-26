---
id: SRT-CONTEXT-BUNDLES-README
type: index
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
generated: 2026-07-26
source_commit: 058c82d
---

# SRT 上下文包

由 `scripts/build_srt_context_bundles.py` 自动生成，用于把仓库喂给 Claude Project、
ChatGPT Project 或任何单次对话。**目录内所有文件都是生成物，不要手工编辑**——
改动会在下次运行时被覆盖。要改内容请改来源文件或生成脚本。

## 包清单

| 文件 | 内容 | 来源文件数 | 字符数 | ≈token |
|---|---|---:|---:|---:|
| `SRT_CONTEXT_BUNDLE_SPINE.md` | 骨架 spine | 16 | 320,024 | ~137,320 |
| `SRT_CONTEXT_BUNDLE_COMPACTCORE.md` | CompactCore 全集 | 18 | 128,148 | ~59,215 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_AI.md` | 领域 AI | 6 | 51,954 | ~20,159 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_PHYSICS.md` | 领域 Physics | 11 | 62,564 | ~27,566 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_PHILOSOPHY.md` | 领域 Philosophy | 6 | 75,902 | ~28,465 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_NEUROSCIENCE.md` | 领域 Neuroscience | 5 | 48,290 | ~19,379 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_SPIRITUALITY.md` | 领域 Spirituality | 3 | 24,548 | ~9,419 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_CORE.md` | 领域 Core | 1 | 10,350 | ~4,950 |

## 该用哪个

- **只装一个** → `SPINE`。它含承载定义权的 canonical 主干（`d` / `Ψ_f` / `T_dir`
  定义、核心公理、主方程、符号表、未闭合登记），约 13–14 万 token，可整个塞进
  一次 200K 对话，不必依赖检索命中。
- **要跨域回答** → `SPINE` + `COMPACTCORE`。
- **只做单领域** → `SPINE` + 对应 `DOMAIN_*`。领域包**不含**定义源，单独使用
  不足以裁定任何 SRT 术语。

## 三条使用纪律

1. **本目录不是 canonical。** 与仓库来源文件冲突时以仓库为准。包是快照。
2. **§0.2 状态护栏必读。** 那里记录了正文读不出来的东西——未闭合的证明、
   处于禁运的概念、被冻结挡住的回写。正文里这些命题写得像已经成立。
3. **仓库内部工作不要读本目录。** 直接读来源文件。本目录是给外部对话用的。

## 重新生成

```bash
uv run python scripts/build_srt_context_bundles.py
```

护栏层按锚点抽取自 `Operations/` 审计台账与 `STATUS.md`。**任一锚点失效，脚本会
直接以非零码退出**，而不会产出一个缺护栏的包。P1-T07 若日后被修订，脚本同样会
失败，强制复核该护栏是否仍适用——这是刻意的防漂移设计。
