---
id: SRT-PHYS-09-SPLIT-INDEX-PART-02
type: reading_shard
tags: [Split, Navigation, Longform, ConnectorSafety, Physics, Formalism]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: evidence
canonical: false
source_owner: ../SRT_Phys_09_Formalism_Ext.md
---

# SRT-PHYS-09 Split 02 — Information Geometry and Dynamics

> Source owner: [`../SRT_Phys_09_Formalism_Ext.md`](../SRT_Phys_09_Formalism_Ext.md)
>
> Reading-aid guardrail: this shard is a connector-safe navigation copy. It does not create new definitions, new claim status, or independent authority. Current guardrail: `Ψ_f` is not Fisher, Landauer, energy, pain, or prediction error; those are projections/proxies only.

---

## IV. Information Geometry (信息几何)

### Ax-IG-1 [A1.4.1]: Fisher Projection of Ontological Friction（非定义）
旧标题“$\Psi_f$ 作为 Fisher 度量”已降级。当前只允许把 Fisher–Rao 度量读作 `Ψ_f` 的局部信息几何 projection / operational proxy：
$$ \Psi_f^{Fisher	ext{-}proxy}(θ) \sim g_{jk}(θ) = \mathbb{E}\left[\partial_j \log p \cdot \partial_k \log p\right] $$

Boundary: $g_F$ measures statistical sensitivity of a parameterized model. It does not define `Ψ_f` as payability burden, and it does not capture consequence return, stake, or reselectable mobility by itself.

### T-IG-1 [T1.4.1]: Natural Gradient Descent (自然梯度下降；proxy)
若某任务已被参数化为统计模型，选择/更新动力学可用自然梯度形式作局部 proxy：
$$ \dot{θ}^{proxy} = -\left(g_F + \epsilon I\right)^{-1} \nabla F $$

**Sketch**：在 Fisher projection $g_F$ 下最小化 $F$，得到自然梯度形式。该式不说明 SRT 选择本体“遵循”自然梯度；它只描述特定模型类中的更新几何。

### T-IG-2 [T1.4.2]: Geodesic Form of Selection Dynamics (选择动力学的测地线形式)
$$ \frac{d\xi}{dt} = -g^{-1}(\xi) \nabla F(\xi) $$

### Def-IG-1 [D1.4.1]: Ontological Curvature (本体论曲率)
$$ K(θ) = \text{scalar curvature of } \Psi_f(θ) $$

### T-IG-3 [T1.4.3]: Insight Event Condition (顿悟发生条件)
$$ \text{Insight Event} \iff K(θ) > K_{crit} $$
*   **T-Insight Link**: 与尺度定理中的顿悟阈值一致，曲率跃迁触发结构重组。

### T-IG-4 [T1.4.4]: D_eff Capacity Inequality（旧 d-value 维度不等式，已降级）
$$ E_{capacity}^{proxy}(D_{eff}) \gtrsim \kappa \cdot D_{eff} \cdot \log(D_{eff}) $$
该式最多约束有效维度 / 注意力带宽 / 模型容量 proxy。不得写成 canonical d-value 的能量定律；“神的全知视角”与 $d \to \infty$ 只保留为旧 public/spirituality 极限隐喻。

---

## V. Semantic Information Theory (语义信息论)

### Ax-SIP-1 [A1.5.1]: Semantic Information Potential (语义信息能)
信息 $I$ 的"意义"是其对 $L_1$ 轨迹造成的发散：
$$ \text{SIP}(I) = D_{JS}(L_1^{with} \| L_1^{without}) $$

### T-SIP-1 [T1.5.1]: Semantic Transduction (语义转导)
$$ \hat{G}_θ : L_0 \xrightarrow{\text{Transduce}} L_1 $$
存在即表达。"不可言说"是因为 $L_0$ 的语义熵超过了 $L_2$ 句法的承载能力。

### T-SIP-2 [T1.5.2]: Syntactic Entanglement (句法纠缠)
纠缠粒子在 $L_0$ 的语法树中是相邻节点：
$$ \text{Entangle}(A, B) \iff d_G(A, B) \ll d_{L_1}(A, B) $$

---

## VI. $L_1$ Density Metrics ($L_1$ 密度度量)

### Def-Density-1 [D1.6.1]: Selection Rarity ($L_1$ 密度指标)
$$ D(L_1) = -\log_2\left(\frac{\text{Vol}(L_1)}{\text{Vol}(L_0)}\right) $$

### T-Density-1 [T1.6.1]: D_eff / density scaling（旧 d-value 缩放，已降级）
$$ D(L_1)^{proxy} \propto D_{eff} \cdot \log(\text{Complexity}(L_0)) $$
This is a density/capacity proxy, not a definition or measurement of canonical d-value.

### T-Density-2 [T1.6.2]: Stabilization Cost Proxy（旧精华衰减律，已降级）
$$ \Psi_f^{stabilization	ext{-}proxy}(t) = \Psi_0 \cdot e^{-t/\tau_{L_2}} + \Psi_\infty $$
该式只表示某些稳定结构的维护/更新负担可能随沉积而降低；不得写成维持现实所需的“选择能量”定律，也不得把低维护成本等同于健康或正当。

---

## VII. Dynamical Systems & Attractors (动力系统与吸引子)

### Def-DS-1 [D1.7.1]: $L_2$ as Attractor Landscape ($L_2$ 作为吸引子地景)
$$ L_2 = \bigcup_i B(A_i) = \bigcup_i \{x_0 : \lim_{t \to \infty} \varphi_t(x_0) \in A_i\} $$
$L_2$ 不是一堵墙，而是一个"山谷"（吸引子盆地）。
*   **M1/M2 Link**: $A_i$ 对应稳定固定点集合，$\text{Re}(\lambda_J)<0$。

---

---

# §3. 信息几何

甘利俊一（Shun'ichi Amari）的信息几何提供了最直接适用的数学框架。

## 3.1 选择动力学的测地线形式

$$\frac{d\xi}{dt} = -g^{-1}(\xi) \nabla F(\xi)$$

其中 $F$ 是变分自由能。该自然梯度写法只为特定参数化模型提供更新几何，不是幽灵算子的完整动力学定义。

## 3.2 $\Psi_f$ 的局部张量 proxy

**旧重定义已降级**：
$$\Psi_f^{tensor\text{-}proxy} \sim G(θ) \in \mathbb{R}^{n \times n}$$

该张量只表示特定参数化模型中的局部敏感性 / 更新代价 proxy。它可与 Fisher 信息度量 $g_{jk}(θ)$ 形成局部 projection 对应；“精确对应”只限模型内部，不定义 canonical `Ψ_f`。

## 3.3 本体论曲率与顿悟机制

**定义**：
$$K(θ) = \text{scalar curvature of } \Psi_f(θ)$$

**假设（顿悟发生条件）**：
$$\text{Insight Event} \iff K(θ) > K_{crit}$$

## 3.4 $D_{eff}$ 容量不等式（旧 d 值-维度不等式）

**容量 proxy 定律**：
$$E_{capacity}^{proxy}(D_{eff}) \gtrsim \kappa \cdot D_{eff} \cdot \log(D_{eff})$$

若把 $d$ 误读为 $D_{eff}$ / capacity，趋于无穷的容量会遭遇能量与计算约束；这不是 canonical d-value 定律。

---

# §4. 语义信息能

## 4.1 核心定义

**定义**：信息 $I$ 的语义信息能是该信息干预系统后，$L_1$ 轨迹与原轨迹之间的 **Jensen-Shannon 散度**：
$$\text{SIP}(I) = D_{JS}(L_1^{with\ I} \| L_1^{without\ I})$$

## 4.2 语义转导理论

$$\hat{G}_θ : L_0 \xrightarrow{\text{Transduce}} L_1$$

存在即表达。所谓的"不可言说"是因为 $L_0$ 的语义熵超过了 $L_2$ 句法的承载能力。

## 4.3 句法纠缠

**假说**：纠缠粒子在 $L_0$ 的语法树中是相邻节点（共享父节点），尽管在 $L_1$ 时空中相隔甚远。
$$\text{Entangle}(A, B) \iff d_G(A, B) \ll d_{L_1}(A, B)$$

---

# §5. $L_1$ 密度指标

## 5.1 定义

$$D(L_1) = -\log_2\left(\frac{\text{Vol}(L_1)}{\text{Vol}(L_0)}\right)$$

## 5.2 与 $D_{eff}$ / capacity proxy 的关系

$$D(L_1)^{proxy} \propto D_{eff} \cdot \log(\text{Complexity}(L_0))$$

该式只说明 L1 密度指标与有效维度 / 模型容量 proxy 的可能关系；不得反推 canonical d-value。

## 5.3 稳定化负担 proxy（旧精华衰减律）

$$\Psi_f^{stabilization\text{-}proxy}(t) = \Psi_0 \cdot e^{-t/\tau_{L_2}} + \Psi_\infty$$

随着 $L_2$ 固化，某些维持/更新负担 proxy 可能递减；不得把该 proxy 直接等同暗能量或 SRT 的 `Ψ_f` 定义。

---

# §6. 动力系统与吸引子理论

## 6.1 $L_2$ 作为动力学吸引子地景

$$L_2 = \bigcup_i B(A_i) = \bigcup_i \{x_0 : \lim_{t \to \infty} \varphi_t(x_0) \in A_i\}$$

$L_2$ 不是一堵墙，而是一个"山谷"（吸引子盆地）。习惯改变需要克服动力学势垒。

---
