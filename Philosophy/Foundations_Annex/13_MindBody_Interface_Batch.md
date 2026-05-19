---
id: SRT-PHIL-ANNEX-13-MIND-BODY
type: interface
tags:
  - Philosophy
  - Interface
  - Annex
status: active_v1
layer: bridge
epistemic_layer: bridge
claim_mode: navigation
canonical: false
parent: Philosophy/SRT_Philosophy_Foundations.md
date: 2026-03-08
---

> **Annex file** — extracted from [`SRT_Philosophy_Foundations.md`](../SRT_Philosophy_Foundations.md). Extracted current bridge/interface content; `canonical: false` means this file does not define Core primitives.

## Mind–Body Problem Interface（2026-03-08）

这条 interface 真正想避免的，不是选边站在“物理主义”或“二元论”某一侧，而是把心身问题重新压回它最硬的双重压力：一边是因果闭包，一边是主观体验的解释负担。它也顺手修正了一种常见误解：只要承认心理依赖物理，就等于解释已经完成。

### Def-Phil-MB-1: Two-Horn Constraint (Causation vs Consciousness)
心身问题在 SRT 中被表述为双约束：
\[
\text{Horn A: } \neg Physical\_mind \Rightarrow \text{mental causation gap}
\]
\[
\text{Horn B: } Physical\_mind \Rightarrow \text{consciousness explanation gap}
\]
即：若心灵非物理，因果闭包受压；若心灵全物理，主观体验解释受压。

### Def-Phil-MB-2: Layered Realization without Category Collapse（分层实现-非塌缩框架）

SRT 采用”分层实现 + 非塌缩”框架，三域转化链的每个箭头语义严格区分：

$$L_0 \xrightarrow{\hat{G}_\theta} L_1 \xrightarrow{\;\int_{L_2}\;} L_2$$

- $L_0 \xrightarrow{\hat{G}_\theta} L_1$：**选择性涌现**（instantiation）——选择算子 $\hat{G}_\theta$ 从 $L_0$ 中锚定一个 $\theta$-特异的显现态。此过程引入了 $L_0$ 中不存在的信息：具身参数 $\theta$ 的历史轨迹。
- $L_1 \xrightarrow{\;\int_{L_2}\;}L_2$：**跨算子收敛**（stabilization via social consensus）——多个独立 $L_1$ 显现在反复交互中收敛为共享的 $L_2$ 吸引子。此过程引入了单一 $L_1$ 中不存在的信息：跨主体验证结构。

**非塌缩的正面定义（三条）**：

1. **弱随附而非强还原**：SRT 接受弱随附性（Weak Supervenience：$L_1/L_2$ 的任何差异必有 $L_0$ 差异与之对应），但拒绝强还原（$L_1/L_2$ 可被 $L_0$ 的函数完全决定）。原因：$\hat{G}_\theta$ 是 $\theta$-参数化的，同一 $L_0$ 基底可以涌现出不同的 $L_1$——多重可实现性（Multiple Realizability）在 SRT 中不是例外而是必然结构。

2. **解释不可消除性**：$L_1$ 和 $L_2$ 层的解释（意识、社会规范、意义）不因底层 $L_0$ 描述完备而变得”冗余”（Epiphenomenal）——它们是跨层选择过程的**独立因果信道**，不能被还原为 $L_0$ 的重新描述。

3. **塌缩的操作化判据（可证伪）**：若存在函数 $f$ 使得 $L_1 = f(L_0)$（即 $L_1$ 可被 $L_0$ 的完备描述决定论性重建，无需 $\theta$），则 Def-Phil-MB-2 失效，SRT 退化为标准物理主义还原论。

> **[R]** 分层实现与非塌缩的哲学基础：Putnam 1967 *Art, Mind, and Religion*（多重可实现性原始论证：疼痛可由不同物理基底实现，反驳类型同一论，R基线）；Kim 1993 *Supervenience and Mind*（弱/强随附性的系统区分，弱随附允许解释自主性，R概念框架）；Fodor 1974 *Synthese*（特殊科学：高层科学（心理学/经济学）的解释律不可被低层科学（物理学）取代，解释不可消除性的R论证）。**[H]** 以L₀/L₁/L₂三域+Ĝ_θ参数化为多重可实现性提供具体机制（同一L₀因θ差异涌现不同L₁）、并给出塌缩的操作化可证伪判据为本框架新增贡献。
>
> **与T-Phil-MB-1/MB-2的逻辑关系**：Def-Phil-MB-2（非塌缩定义）是前提；T-Phil-MB-1（因果闭包相容定理）是在此前提下的推论（分层实现保留物理闭包）；T-Phil-MB-2（解释缺口持续定理）是进一步推论（随附性不蕴含现象透明性）。三者构成SRT心身问题立场的完整论证链。

### T-Phil-MB-1: Causal Closure Compatibility Theorem
在不放弃物理因果闭包的前提下，心理因果可被解释为跨层同一事件的双重描述：
\[
E_{mental} \equiv E_{physical}^{realization},
\quad \Delta a_{body}=f(E_{mental})=f(E_{physical})
\]
从而避免“心因果 vs 物因果”机械叠加式过度决定。

更稳的结论因此不是“心身问题已经被取消”，而是：SRT 允许我们同时保住物理闭包与心理解释的必要性，但前提是承认跨层实现不等于范畴塌缩，依赖关系也不等于现象透明性。

### T-Phil-MB-2: Explanatory Gap Persistence under Ontic Dependence
即便承认本体依赖（supervenience），意识解释缺口仍可存在：
\[
\text{Ontic dependence} \nRightarrow \text{full phenomenological transparency}
\]
该条款吸纳 bat/Mary/zombie 类论证的启发价值，但不把“可想象性”直接升级为“形上断言”。

### 分类映射表（Mind–Body Positions → SRT）
| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 强还原物理主义 | 中 | Semi-open（实现优先） | 解释缺口压力上升 |
| 非还原物理主义 | 中~高 | Open↔Semi-open（分层协同） | 可支付但边界敏感 |
| 属性二元论 | 中 | Open（本体扩展） | 因果闭包压力上升 |
| 中性一元/泛心向 | 中高 | Open（本体重述） | 组合问题负载高 |

### [Lineage/Source]
- Tim Crane (2026), *The Mind-Body Problem*.
- 关键脉络：Cartesian dualism、物理主义/超覆(supervenience)、心因果论证、解释鸿沟与可想象性挑战。

## 【理论边界/防误用声明】
1. 不采纳"承认解释鸿沟 = 物理主义必假"的推论；语义-解释难题不自动转成本体否定。  
2. 不采纳"因果闭包成立 = 心理层无效"的推论；心理描述可对应同一实现事件的高层因果刻画。  
3. 不采纳"中性一元/泛心 = 已解决意识难题"的推论；组合问题与可检验性仍是硬约束。
