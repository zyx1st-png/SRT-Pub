---
id: SRT-CONTEXT-BUNDLES-README
type: index
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
generated: 2026-11-27
source_commit: c142ed30e
source_branch: canon/r4-c5a-spirituality-praxis-reconstruction-2026-11-27
source_dirty: false
inputs_digest: 3fe6cb3d6defd0a4
---

# SRT 上下文包

由 `scripts/build_srt_context_bundles.py` 自动生成，用于把仓库喂给 Claude Project、
ChatGPT Project 或任何单次对话。**目录内所有文件都是生成物，不要手工编辑**——
改动会在下次运行时被覆盖。要改内容请改来源文件或生成脚本。

## 包清单

| 文件 | 内容 | 来源文件数 | 字符数 | ≈token |
|---|---|---:|---:|---:|
| `SRT_CONTEXT_BUNDLE_SPINE.md` | 骨架 spine | 15 | 335,031 | ~124,240 |
| `SRT_CONTEXT_BUNDLE_FORMAL.md` | 形式方程 FORMAL | 1 | 77,585 | ~35,916 |
| `SRT_CONTEXT_BUNDLE_COMPACTCORE.md` | CompactCore 全集 | 19 | 220,778 | ~116,647 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_AI.md` | 领域 AI | 6 | 77,401 | ~42,747 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_PHYSICS.md` | 领域 Physics | 11 | 117,879 | ~54,746 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_PHILOSOPHY.md` | 领域 Philosophy | 7 | 146,496 | ~51,993 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_NEUROSCIENCE.md` | 领域 Neuroscience | 6 | 129,458 | ~51,404 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_SPIRITUALITY.md` | 领域 Spirituality | 3 | 51,740 | ~23,655 |
| `SRT_CONTEXT_BUNDLE_DOMAIN_CORE.md` | 领域 Core | 1 | 25,028 | ~11,207 |

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
| 骨架路线（裁定定义时用） | `SPINE` | 124,240 | 75,760 | 需要确定 SRT 术语、生成主轴、One Formation、P0/P1 核心公理与符号含义时，只装这一个；Core_22 方程索引与按需桥接指针见 §0.5。 |
| 形式方程路线（查阅主方程时用） | `FORMAL` | 35,916 | 164,084 | 需要查阅 Core_22 主动力学/热力学/桥接方程正文时使用；不含完整定义骨架，定义裁定须切回 SPINE。 |
| 轻量跨域 | `COMPACTCORE` | 116,647 | 83,353 | 只需领域主线、不需裁定定义时用。 |
| 单域（体量最大者：Philosophy） | `DOMAIN_PHILOSOPHY` | 51,993 | 148,007 | 单领域问答；领域包自带 claim-status 护栏与导航。 |
| 单域（体量最小者：Core 动力学） | `DOMAIN_CORE` | 11,207 | 188,793 | 最省的一种装法。 |

### 禁止的组合

| 组合 | 合计 ≈token | 为什么禁止 |
|---|---:|---|
| SPINE + COMPACTCORE | **240,887** | 旧版曾把它推荐为跨域方案；两包合计已**超出**整个窗口，装不下。 |

### `SPINE` + `FORMAL` / 各领域包（逐个列出，均不推荐叠加）

| 组合 | 合计 ≈token | 是否在预算内 |
|---|---:|:---:|
| `SPINE` + `FORMAL` | 160,156 | **超预算** |
| `SPINE` + `DOMAIN_AI` | 166,987 | **超预算** |
| `SPINE` + `DOMAIN_PHYSICS` | 178,986 | **超预算** |
| `SPINE` + `DOMAIN_PHILOSOPHY` | 176,233 | **超预算** |
| `SPINE` + `DOMAIN_NEUROSCIENCE` | 175,644 | **超预算** |
| `SPINE` + `DOMAIN_SPIRITUALITY` | 147,895 | 在预算内（但仍不推荐，见下） |
| `SPINE` + `DOMAIN_CORE` | 135,447 | 在预算内（但仍不推荐，见下） |

**各路线在默认整包意义下互斥。** `SPINE` 路线用于裁定定义（已内置 `Core_Law/SRT_One_Formation.md`、`Governance/SRT_CLAIM_MODE_AUDIT.md` 全文、`_SRT_CROSS_DOMAIN_MATRIX.md` 及 `§0.5` 方程/按需桥接索引）；`FORMAL` 路线用于查阅 `Core/SRT_Core_22_Equations.md` 主方程正文；`COMPACTCORE` / `DOMAIN_*` 路线用于轻量跨域或单领域问答；`Core/SRT_Core_21c_Bridge_Hypotheses.md` 走按需桥接层（直接读仓库原文件）。

上表中部分组合虽在预算内，仍不推荐**整包叠加**：各包已自带完整状态护栏与导航，
叠加整包会把大量无关正文压进上下文，稀释注意力，收益远低于成本。
在外部静态对话中，需要裁定定义时**换一次对话只装 `SPINE`**，需要主方程正文时**换一次对话只装 `FORMAL`**；但禁止默认整包叠加**不等于**禁止局部跨 owner 检索——具备仓库直读能力的工具或研究者仍可围绕具体问题按需联合读取局部方程与对应定义 owner 原文件。

## 四条使用纪律

1. **本目录不是 canonical，也不是定义权的完备闭包。** `SPINE` 是**人工选择的高优先级
   spine（`ENG-01` 分层瘦身版）**：registry 列名的文件有 90 余个，骨架只取其中核心定义与治理护栏。收了什么、漏了什么、
   各自角色与外置去向如何，见每个包的 **§0.4 Manifest 差异报告** 与 `SPINE` **§0.5 分层外置路线、方程索引与完备性声明**。与仓库来源文件冲突时以仓库为准。
2. **§0.2 状态护栏必读**，并注意其三段的权威等级不同：SOURCE EXTRACT 是逐字原文，
   GENERATED INTERPRETATION 是生成器归纳（可能丢失限定条件），USAGE POLICY 是
   由治理文件授权的规则。有疑问以 SOURCE EXTRACT 为准。
3. **动态状态与当前作者裁决不入静态包。** `STATUS.md`、当前 `R3` 作者裁决（`01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_*`）与阶段性收敛主稿（`Operations/Proposals/SRT_R3_*`）刻意不在静态包闭包内；涉及最新 `CURRENT NEXT`、`HOLD`、`OPEN` 或作者裁决时，直接读取仓库 `STATUS.md §Fast Status` 及其控制指针。
4. **仓库内部工作不要读本目录。** 直接读来源文件。本目录是给外部对话用的。

## 重新生成与校验

```bash
uv run python scripts/build_srt_context_bundles.py
uv run python scripts/build_srt_context_bundles.py --check     # 生成一致性校验（字节级复现）
uv run python scripts/test_build_context_bundles.py             # 构造器单元测试 + 结构性检索可达性验收（structural retrieval reachability）
```

`--check` 先核对 `inputs_digest`（输入闭包的联合内容摘要，覆盖生成脚本、护栏来源、
全部正文与 `SPINE §0.5` 索引抽取源），再按既有产出 frontmatter 记录的 provenance 重新生成到临时目录逐字比对。
唯一的固定参数是 `--generated-date`，且它只是日期标签，不声称内容来源。

护栏层按锚点抽取自 `Operations/` 审计台账与 `Governance/SRT_DOWNSTREAM_GUARDRAILS.md`；`SPINE §0.5` 方程与桥接索引按锚点抽取自 `Core_22` 与 `Core_21c`。**任一锚点失效，脚本会
直接以非零码退出**，而不会产出一个缺护栏或缺索引的包。P1-T07 若日后被修订，脚本同样会
失败，强制复核该护栏是否仍适用——这是刻意的防漂移设计。

真实性判据是 `inputs_digest`（输入闭包的联合内容摘要），不是 `source_commit`。
后者仅供参考——squash / rebase 合并会重写它，拿它做祖先校验会让合并后的 main 必红。
