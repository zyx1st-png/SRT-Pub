---
id: SRT-PHIL-ANNEX-09B-FRICTION-PROBING
type: interface
tags:
  - Philosophy
  - Interface
  - Annex
status: active_v1
layer: bridge
epistemic_layer: bridge
claim_mode: translation
canonical: false
parent: Philosophy/SRT_Philosophy_Foundations.md
date: 2026-03-06
---

> **Annex file** — extracted from [`SRT_Philosophy_Foundations.md`](../SRT_Philosophy_Foundations.md). Canonical content.

## 认识论乐观主义的摩擦探测协议（2026-03-06，轻量）

### Def-PHIL-FRIC-1: Friction-Probing Epistemology
在不可直接访问 \(L_0^{abs}\) 的条件下，采用”代价反推结构”协议：
\[
\nabla_\lambda \Psi_f(\mathcal{H}(\lambda)) \mapsto \text{Constraint Signature}(L_0)
\]
其中 \(\mathcal{H}(\lambda)\) 为由参数 \(\lambda\) 连续参数化的候选假设族（\(\lambda \in \Lambda\)，假设参数空间）；若假设族为离散集合 \(\{H_i\}\)，则将 \(\nabla_\lambda\) 替换为跨假设的 $\Psi_f$ 排序（差分代替梯度）。可维持且低摩擦的假设族更可能贴合外部约束地形。

> **符号展开**：
> - $\nabla_\lambda \Psi_f(\mathcal{H}(\lambda))$：假设族在参数 $\lambda$ 方向上的 $\Psi_f$ 梯度（”哪个方向改变假设可以降低维持代价”）。
> - $\text{Constraint Signature}(L_0)$：$L_0$ 约束结构的可观测印记，形式上是约束集合 $\{c_k\}$（使 $\sigma \in L_1$ 成立的必要条件集）在 $\Psi_f$ 代价空间中的投影。$\nabla_\lambda\Psi_f$ 的梯度场的零点和极小值对应约束的”软边界”——摩擦最小的假设最贴合约束。
> - **FEP 对应**：在自由能原理（FEP）语境中，$\nabla_\lambda\Psi_f(\mathcal{H})$ 对应变分自由能对生成模型参数的梯度；Def-PHIL-FRIC-1 是该思路在 SRT 本体论语言（$\Psi_f$ 替代变分自由能）下的表达，两者等价但 SRT 版本强调摩擦作为本体论代价而非纯信息论量。

### T-PHIL-FRIC-1: Constrained-Model Realism
\[
L_1\ \text{is model-dependent but constraint-governed}
\]
\[
\Psi_f\ \text{is not optional}
\]
* **Implication（中文）**：我们并非“直接看见真相”，但可通过失败代价与维持成本对真实结构做间接可证伪逼近。

## 【理论边界/防误用声明】
本段边界声明已 annex 化；详见 `Foundations_Annex/00_General_Boundary_Block.md`。
### 分类映射表（外部讨论分类 → SRT）
| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 受控幻觉/预测编码（可检验） | 中 | Semi-open | payable |
| 泛心论宽解释（弱约束） | 低~中 | Closed 倾向 | 概念上可扩张、实证上易失真 |
| 主观唯我误读（任意构造） | 低 | Closed | overloaded / unsustainable |

### [Lineage/Source]
- Friston 相关圆桌讨论（2026）
- Active Inference / FEP 经典文献语境

