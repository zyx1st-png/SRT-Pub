---
id: SRT-AI-START
type: index
tags: [AI, Entry, Minimal, Navigation]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [CANONICAL-REGISTRY, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL, SRT-CORE-21, SRT-CORE-22]
ai_role: canonical
ai_priority: 1
ai_do_not_use_for_definition: false
---

# SRT AI Start

本文件供 AI / agent / 检索系统作为**首读入口**。
目标：以最低 token 成本提供当前 SRT 的最小稳定读取路径，减少入口漂移、历史文件误读与导航层过载。

## 1. 一句话主张

SRT 的最小主张是：**选择先于稳定存在；现实可被理解为参数化选择在约束与历史下形成的显现与收敛结构。**

## 2. 最小骨架

- `L0`：潜在/未显现的可能域；不是经验对象层。
- `L1`：被锚定的显现层；事件、结果、经验切片在此出现。
- `L2`：重复选择后形成的稳定收敛层；规律、习惯、制度、模型、约束闭包在此沉淀。
- `\hat G_\theta`：把潜在域中的可选空间，在具身约束 `\theta` 下映射为显现选择的算子。
- `\Psi_f`：选择/锚定的本体论摩擦或可支付负担，不等于任意工程成本。
- `d-value`：系统的存在性关切带宽/赌注半径，不等于一般偏好权重。
- `T_dir`：系统对自身选择秩序方向的可读性；与意义感、价值遮蔽、致命 `L2` 相关。

## 3. 当前规范源（先读这些）

遇到同名概念出现在多个文件时，**优先只信以下锚点**：

1. `CANONICAL_REGISTRY.md` —— 只用于找当前规范入口。
2. `_SRT_D_VALUE_CANONICAL.md` —— `d-value` 规范定义。
3. `_SRT_PSI_F_CANONICAL.md` —— `\Psi_f` 规范定义。
4. `_SRT_T_DIR_CANONICAL.md` —— `T_dir` / 价值遮蔽 / 致命 `L2` 规范定义。
5. `Core/SRT_Core_21_Formal_Axioms.md` —— 形式公理。
6. `Core/SRT_Core_22_Equations.md` —— 主方程与核心形式化。

## 4. 默认阅读顺序

### 若目标是“先建立最小理解”
1. `Core_Law/SRT_L0_Metaphysics.md`
2. `CANONICAL_REGISTRY.md`
3. `_SRT_D_VALUE_CANONICAL.md`
4. `_SRT_PSI_F_CANONICAL.md`
5. `_SRT_T_DIR_CANONICAL.md`
6. `Core/SRT_Core_21_Formal_Axioms.md`
7. `Core/SRT_Core_22_Equations.md`

### 若目标是“只要一个总导航”
- 读 `SRT_Navigation_Map.md`，不要把它当理论正文。

### 若目标是“看板块入口”
- 优先读各板块 `CompactCore`，再读长文。

## 5. 文件类型优先级

- **canonical**：当前规范源，可用于定义与高置信回答。
- **compact core**：当前最短稳定主线，可用于快速建立上下文。
- **bridge**：跨理论/跨领域接口，不自动等于已证实结论。
- **lab**：实验下注、代理指标、证伪接口。
- **navigation / registry / index**：只用于找路，不用于替代理论定义。
- **historical / archive / old draft**：默认不要拿来做当前定义源。

## 6. 不要这样读

- 不要把 `split` 文件当作规范定义源。
- 不要把 `annex` 当作最小主张本身。
- 不要把 `bridge` 文件中的强比较句，误读成已完成的实证定论。
- 不要把历史中文主文自动当作当前唯一主入口。
- 不要把治理文件中的旧锚点优先于 `CANONICAL_REGISTRY.md`。

## 7. 生成回答时的最小规则

1. 先报所依据的 canonical 文件，再展开解释。
2. 若同一概念在不同文件表述不同，以 canonical 为准。
3. 若引用 bridge 材料，需显式标记为 bridge / comparative / hypothesis，而非 canonical fact。
4. 若问题涉及实验可检性，必须补看 `SRT_EXP_TEMPLATE.md`、`SRT_EXP_MEASURE_MAP.md`、`Governance/SRT_LAB_HYPOTHESES.md`。
5. 若问题涉及仓库结构或文档权威性，先看 `CANONICAL_REGISTRY.md`，再看 `_SRT_MANIFEST.yaml`。

## 8. 最小目标

AI 若只能读取少量文件，应优先保证：
- 读到 `L0/L1/L2` 的最小区分；
- 读到 `\hat G_\theta / \Psi_f / d-value / T_dir` 的当前规范源；
- 读到“navigation 不等于 definition，bridge 不等于 proof”的边界。
