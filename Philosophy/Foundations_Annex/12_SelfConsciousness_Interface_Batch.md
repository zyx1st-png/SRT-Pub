---
id: SRT-PHIL-ANNEX-12-SELF-CONSCIOUSNESS
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

## Self-Consciousness Interface（2026-03-08）

这条 interface 最重要的修正，不是把第一人称特权神秘化，而是把它降回几个较硬的信息源条件：自我意识不是“对内绝对透明”，而是系统在某些通道上较难认错“是谁在经历”。这也顺手加固了一个更稳的边界：可错的是内容，不一定是主语。

### Def-Phil-SC-1: Self-Consciousness as Self-Specified Awareness
自我意识定义为：系统获得并整合“不可错指向自身”的信息流，从而形成可用于行动与反思的自我指向状态。
\[
SC_t = \mathcal{I}\big(I_{introspection}, I_{proprio}, I_{kinesthetic}, I_{autobio}, I_{self-loc}\big)
\]
其中 \(\mathcal{I}\) 为跨通道整合算子。

### T-Phil-SC-1: Immunity-Grounded First-Person Asymmetry
第一人称特权并非“绝对内省透明”，而是来自若干信息源的免误认结构（immunity to misidentification）：
\[
I_k \in \mathcal{S}_{immune} \Rightarrow P(\text{misidentify subject}\mid I_k)\to 0
\]
这解释了“可错内容 + 不易错主语”的并存。

### Def-Phil-SC-2: Embodied Ownership Window

身体所有感由多模态一致性门控，而非单一最小自我感（mineness，Zahavi）即可决定：

\[
P(Own) = \sigma\!\left(\beta \cdot \text{Sync}(V,T,P,K) - \tau_{own}\right)
\]

其中 $V/T/P/K$ 分别代表视觉、触觉、本体觉、运动觉一致性（对应橡胶手/换身错觉可操纵边界）；$\tau_{own}$ 为动态阈值，受预测误差与具身历史调节，与 $\hat{G}_\theta$ 的 d-value 动态具有结构同构性。

$Own = 1$ 的区域构成 $\hat{G}_\theta$ 当前操作的具身内部空间——身体所有感是 G 算子具身边界的实时确认机制。

### T-Phil-SC-2: Self–Other Co-Development Constraint
自我意识与他心理解存在对称/非对称并存关系：
\[
\text{ToM}_t \leftrightarrow \text{SelfModel}_t,
\quad \text{but }\mathcal{E}_{1p}\neq\mathcal{E}_{3p}
\]
即概念框架可共享（信念/意图等），证据通道不可等同（第一人称与第三人称信息源不同）。

这条线真正加固的，是 SRT 对“自我 / 他者”共同发育但不完全对称的判断：我们可以用相近的概念框架理解自己和别人，却不能假装两边的证据入口是同一条管道。

### 分类映射表（Self-Consciousness Regimes → SRT）
| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 最小具身自我（感知-行动耦合） | 中 | Open↔Semi-open | 低负载可支付 |
| 反思性自我（叙事/自传整合） | 中~高 | Semi-open（跨时整合） | 中负载 |
| 身体边界可塑状态（错觉/VR） | 中 | Open（边界重映射） | 可控波动 |
| 病理性解离/失属（neglect/alien hand） | 低~中 | Closed 倾向（整合断裂） | borderline / overloaded |

### [Lineage/Source]
- José Luis Bermúdez (2026), *Self-Consciousness*.
- 关键脉络：Kant “I think”、生态知觉自指信息、镜像识别、身体所有感与 ToM 互构。

## 【理论边界/防误用声明】
1. 不采纳"镜像识别通过 = 完整反思性自我已形成"的推论；该任务仅覆盖部分自我表征能力。  
2. 不采纳"身体所有感 = 单一内在感觉实体"的推论；所有感可由多模态一致性操纵并解离。  
3. 不采纳"第一人称与第三人称完全同构"的推论；二者共享部分概念但证据机制不同。
