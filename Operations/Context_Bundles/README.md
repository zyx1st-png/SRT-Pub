---
id: SRT-CONTEXT-BUNDLES-README
type: index
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
generated: 2026-07-27
source_commit: 23a480e8
source_branch: claude/srt-theory-consolidation-le4fwa
source_dirty: false
---

# SRT 上下文包

由 `scripts/build_srt_context_bundles.py` 自动生成，用于把仓库喂给 Claude Project、
ChatGPT Project 或任何单次对话。**目录内所有文件都是生成物，不要手工编辑**——
改动会在下次运行时被覆盖。要改内容请改来源文件或生成脚本。

## 包清单

| 文件 | 内容 | 来源文件数 | 字符数 | ≈token |
|---|---|---:|---:|---:|
| `SRT_CONTEXT_BUNDLE_SPINE.md` | 骨架 spine | 19 | 377,183 | ~164,845 |
| `SRT_CONTEXT_BUNDLE_COMPACTCORE.md` | CompactCore 全集 | 18 | 136,454 | ~62,255 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_AI.md` | 领域 AI | 6 | 59,838 | ~23,086 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_PHYSICS.md` | 领域 Physics | 11 | 70,720 | ~30,573 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_PHILOSOPHY.md` | 领域 Philosophy | 6 | 83,766 | ~31,387 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_NEUROSCIENCE.md` | 领域 Neuroscience | 5 | 56,127 | ~22,293 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_SPIRITUALITY.md` | 领域 Spirituality | 3 | 32,278 | ~12,302 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_CORE.md` | 领域 Core | 1 | 17,826 | ~7,738 |

## 上下文预算

窗口按 **200,000 token** 计，预留 **30,000** 给系统提示、
用户问题与模型输出，因此单次装载上限 **170,000 token**。

下表由生成脚本计算并校验；**超预算的组合无法作为推荐存在**——`check_budgets()`
会让构建直接失败。

### 推荐装载路线

| 路线 | 装载 | 合计 ≈token | 余量 | 用途 |
|---|---|---:|---:|---|
| 骨架路线（裁定定义时用） | `SPINE` | 164,845 | 35,155 | 需要确定 SRT 术语、公理、方程、符号含义时，只装这一个。 |
| 轻量跨域 | `COMPACTCORE` | 62,255 | 137,745 | 只需领域主线、不需裁定定义时用。 |
| 轻量单域 | `COMPACTCORE` + `DOMAIN_PHILOSOPHY` | 93,642 | 106,358 | 跨域主线 + 单个领域（此处以最大的 Philosophy 为例）。 |
| 最小单域 | `DOMAIN_AI` | 23,086 | 176,914 | 只做单领域问答的最省装法。 |

### 禁止的组合

| 组合 | 合计 ≈token | 为什么禁止 |
|---|---:|---|
| SPINE + COMPACTCORE | **227,100** | 旧版曾把它推荐为跨域方案；两包合计已**超出**整个窗口，装不下。 |
| SPINE + 任一领域包 | **196,232** | 骨架已占大部分预算，叠加后余量不足以容纳系统提示与一次完整回答。 |

**两条路线互斥。** 骨架路线用于裁定定义；轻量路线用于领域问答。不要把 `SPINE`
和其他包叠加——骨架本身已占去大部分预算。

## 三条使用纪律

1. **本目录不是 canonical，也不是定义权的完备闭包。** `SPINE` 是**人工选择的高优先级
   spine**：registry 列名的文件有 90 余个，骨架只取其中一部分。收了什么、漏了什么、
   各自角色如何，见每个包的 **§0.4 Manifest 差异报告**。与仓库来源文件冲突时以仓库为准。
2. **§0.2 状态护栏必读**，并注意其三段的权威等级不同：SOURCE EXTRACT 是逐字原文，
   GENERATED INTERPRETATION 是生成器归纳（可能丢失限定条件），USAGE POLICY 是
   由治理文件授权的规则。有疑问以 SOURCE EXTRACT 为准。
3. **仓库内部工作不要读本目录。** 直接读来源文件。本目录是给外部对话用的。

## 重新生成与校验

```bash
uv run python scripts/build_srt_context_bundles.py
uv run python scripts/build_srt_context_bundles.py --check     # 确定性校验
```

`--check` 按既有产出 frontmatter 记录的 provenance 重新生成到临时目录并逐字比对，
因此可在 CI 中确定性运行。`--source-ref` / `--generated-date` 可固定 provenance。

护栏层按锚点抽取自 `Operations/` 审计台账与 `STATUS.md`。**任一锚点失效，脚本会
直接以非零码退出**，而不会产出一个缺护栏的包。P1-T07 若日后被修订，脚本同样会
失败，强制复核该护栏是否仍适用——这是刻意的防漂移设计。

`source_commit` 记录生成时 HEAD 的来源快照；引入本目录的 commit 必然晚于它，
两者不相等属正常。
