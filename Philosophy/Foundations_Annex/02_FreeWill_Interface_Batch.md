---
id: SRT-PHIL-ANNEX-02-FREEWILL
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
date: 2026-03-02
---

> **Annex file** — extracted from [`SRT_Philosophy_Foundations.md`](../SRT_Philosophy_Foundations.md). Extracted current bridge/interface content; `canonical: false` means this file does not define Core primitives.

## Free-Will Compatibility Interface（2026-03-02）

### Def-Phil-FW-1: Reasons-Responsive Freedom (SRT 映射)
将自由意志的最低充分条件映射为：
\[
\mathfrak{F}_{free}=\mathbf{1}[\mathcal{R}_{resp}\ge\tau_r]\cdot\mathbf{1}[\mathcal{R}_{react}\ge\tau_a]\cdot\mathbf{1}[\mathcal{C}_{coercion}<\tau_c]
\]
其中 \(\mathcal{R}_{resp}\) 为理由识别能力，\(\mathcal{R}_{react}\) 为理由驱动更新能力。

### Def-Phil-FW-2: Determinism-Compatibility Clause
在 SRT 中，”是否决定论”为背景本体问题；”是否自由”由算子在给定约束下的理由响应与可更新性决定：
\[
\text{Determinism status} \perp_{\text{type}} \mathfrak{F}_{free}(\hat{G}_\theta)
\]
其中 $\mathfrak{F}_{free}$ 来自 Def-Phil-FW-1。

**正交性说明**：$\perp_{\text{type}}$（**类型正交**）表示两量分属不同的描述层次，赋值域不重叠——“决定论状态”是关于物理定律结构的本体论断言（真/假），”$\mathfrak{F}_{free}$”是关于算子属性的功能性量度（0 或 1）。两者的赋值相互不制约：$\mathfrak{F}_{free}$ 的计算不引用决定论状态，决定论状态的真值也不改变 $\mathfrak{F}_{free}$ 的评估条件。这不同于统计独立（统计独立需要两者都是概率变量），也不同于数学正交（数学正交需要内积定义）。

**d 值连接**：
- $\mathcal{R}_{resp}$（理由识别能力）$\propto d(\theta)$：关切带宽越高，算子能识别更多种类的理由；低 d 值算子对与当前 $\vec{v}$ 方向不符的理由视而不见。
- $\mathcal{R}_{react}$（理由驱动更新能力）$\propto \|\partial\theta/\partial(\text{prediction error})\|$（θ 参数对预测误差的敏感度，见 Eq-Evo-02）：可塑性高的 θ 能在理由呈现后快速更新锚定点，反之则是”知道理由但改变不了行为”的解离态。

**连续版扩展**（可选）：若需要连续的”自由度评分”，可定义 $\mathfrak{F}_{free}^{cont} = \mathcal{R}_{resp} \cdot \mathcal{R}_{react} \cdot (1 - \mathcal{C}_{coercion}/\tau_c)$，将三项阈值条件替换为连续乘积，量纲为 $[0,1]^3$；但 Def-Phil-FW-1 的二元版本已足够满足伦理责任归属的分类需求。

### Taxonomy Mapping: 自由意志立场 → SRT

| 外部分类 | SRT 对应 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
|:--|:--|:--|:--|:--|
| 兼容论（reasons-responsive） | 理由门控可运行的 \(\hat G_\theta\) | 中~高 | Open / Semi-open | payable |
| 非兼容论（强调替代可能） | 对 \(L_0\) 分支可达性要求更强 | 中高 | Open（高探索） | payable~borderline |
| 强取消主义（意志幻觉） | 将 \(L_1\) 能动归属压缩为后验叙事 | 低~中（定义上） | Closed 倾向 | 易出现解释失衡 |

### [Lineage/Source]
- 术语来源：Levy, N. (2024), *Free Will*, OECS (DOI: 10.21428/e2759450.dd89f27c)。
- 接口语义：与 SRT 既有能动性滞后定理（Libet 窗口）和 \(\hat G_\theta\) 门控框架对齐。

## 【理论边界/防误用声明】
1. **SRT 不采纳**"决定论真/假可单独裁定责任归属"的简单化推论。  
2. **SRT 不采纳**"意识仅是幻觉因此规范评价无效"的全盘取消主义推论。  
3. 适用边界：本接口用于解释与建模，不直接替代法律伦理裁判标准。
---

