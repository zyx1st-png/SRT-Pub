---
id: SRT-CONTEXT-BUNDLES-README
type: index
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
generated: 2026-08-08
source_commit: 515052c5
source_branch: HEAD
source_dirty: false
inputs_digest: a72b0c0b34c5fa8c
---

# SRT 上下文包

由 `scripts/build_srt_context_bundles.py` 自动生成，用于把仓库喂给 Claude Project、
ChatGPT Project 或任何单次对话。**目录内所有文件都是生成物，不要手工编辑**——
改动会在下次运行时被覆盖。要改内容请改来源文件或生成脚本。

## 包清单

| 文件 | 内容 | 来源文件数 | 字符数 | ≈token |
|---|---|---:|---:|---:|
| `SRT_CONTEXT_BUNDLE_SPINE.md` | 骨架 spine | 16 | 328,850 | ~142,481 |
| `SRT_CONTEXT_BUNDLE_COMPACTCORE.md` | CompactCore 全集 | 18 | 136,755 | ~62,473 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_AI.md` | 领域 AI | 6 | 60,156 | ~23,310 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_PHYSICS.md` | 领域 Physics | 11 | 71,038 | ~30,796 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_PHILOSOPHY.md` | 领域 Philosophy | 6 | 84,084 | ~31,610 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_NEUROSCIENCE.md` | 领域 Neuroscience | 5 | 56,445 | ~22,517 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_SPIRITUALITY.md` | 领域 Spirituality | 3 | 32,596 | ~12,525 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_CORE.md` | 领域 Core | 1 | 18,144 | ~7,961 |

## 上下文预算

> **这里的 token 数是字符启发式估算，不是任何目标模型的真实 tokenizer 计数。**
> 系数刻意取在偏高一侧（CJK 按 1.2 tok/字，实际约 1.0–1.1；拉丁按 0.29，实际约 0.25），
> 所以估算值倾向于**高估**——对预算而言这是安全方向。但偏保守不等于精确，因此预留量
> 里额外含一段误差缓冲，且本节不把校验结果称作"保证"。

窗口按 **200,000 token** 计，预留 **45,000** 给系统提示、
用户问题、模型输出**与估算误差**，因此单次装载上限 **155,000 token**。

下表由生成脚本计算并校验：**超出上限的组合不能作为推荐出现**——`check_budgets()`
会让构建直接失败。

### 推荐装载路线

| 路线 | 装载 | 合计 ≈token | 余量 | 用途 |
|---|---|---:|---:|---|
| 骨架路线（裁定定义时用） | `SPINE` | 142,481 | 57,519 | 需要确定 SRT 术语、公理、方程、符号含义时，只装这一个。 |
| 轻量跨域 | `COMPACTCORE` | 62,473 | 137,527 | 只需领域主线、不需裁定定义时用。 |
| 单域（体量最大者：Philosophy） | `DOMAIN_PHILOSOPHY` | 31,610 | 168,390 | 单领域问答；领域包自带 claim-status 护栏与导航。 |
| 单域（体量最小者：Core 动力学） | `DOMAIN_CORE` | 7,961 | 192,039 | 最省的一种装法。 |

### 禁止的组合

| 组合 | 合计 ≈token | 为什么禁止 |
|---|---:|---|
| SPINE + COMPACTCORE | **204,954** | 旧版曾把它推荐为跨域方案；两包合计已**超出**整个窗口，装不下。 |

### `SPINE` + 各领域包（逐个列出，均不推荐）

| 组合 | 合计 ≈token | 是否在预算内 |
|---|---:|:---:|
| `SPINE` + `DOMAIN_AI` | 165,791 | **超预算** |
| `SPINE` + `DOMAIN_PHYSICS` | 173,277 | **超预算** |
| `SPINE` + `DOMAIN_PHILOSOPHY` | 174,091 | **超预算** |
| `SPINE` + `DOMAIN_NEUROSCIENCE` | 164,998 | **超预算** |
| `SPINE` + `DOMAIN_SPIRITUALITY` | 155,006 | **超预算** |
| `SPINE` + `DOMAIN_CORE` | 150,442 | 在预算内（但仍不推荐，见下） |

**两条路线互斥。** 骨架路线用于裁定定义；轻量路线用于领域问答。

上表中部分组合虽在预算内，仍不推荐叠加：领域包已自带 claim-status 护栏与导航，
叠加骨架会把大量与该领域无关的定义正文压进上下文，稀释注意力，收益远低于成本。
需要裁定定义时，**换一次对话只装 `SPINE`**。

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

`--check` 先核对 `inputs_digest`（输入闭包的联合内容摘要，覆盖生成脚本、护栏来源与
全部正文），再按既有产出 frontmatter 记录的 provenance 重新生成到临时目录逐字比对。
唯一的固定参数是 `--generated-date`，且它只是日期标签，不声称内容来源。

护栏层按锚点抽取自 `Operations/` 审计台账与 `STATUS.md`。**任一锚点失效，脚本会
直接以非零码退出**，而不会产出一个缺护栏的包。P1-T07 若日后被修订，脚本同样会
失败，强制复核该护栏是否仍适用——这是刻意的防漂移设计。

真实性判据是 `inputs_digest`（输入闭包的联合内容摘要），不是 `source_commit`。
后者仅供参考——squash / rebase 合并会重写它，拿它做祖先校验会让合并后的 main 必红。
