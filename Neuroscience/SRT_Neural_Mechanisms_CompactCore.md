---
id: SRT-NEURO-MECH-COMPACT-CORE
type: theory
tags: [Neuroscience, Mechanisms, Compact Core, Ghost Operator]
status: active_v1
layer: L1
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-NEURO-AXIOMS-001, SRT-NEURO-MECH-001]
---

# SRT Neural Mechanisms — Compact Core

> **定位**：本文件是 `SRT_Neural_Mechanisms.md` 的紧凑主干版。  
> **用途**：用于快速把握 SRT 如何把神经机制重写为选择动力学，而不是单纯信息处理。  
> **关系**：不替代原文；原文保留病理参数化、免疫接口、量子基质与工作记忆振荡等展开层。

## 1. 核心问题

这篇最核心的问题是：

> **神经系统到底是在“处理信息”，还是在执行一种具身选择？**

SRT 的压缩回答是：
- 神经系统不是被动传输器
- 而是 `\hat G_\theta` 的具身实现
- 它在神经流形上把 `L_0` 压成可显现的 `L_1`

---

## 2. 神经流形与选择投影

### 2.1 Neural Manifold
\[
\sigma(t)\in \mathcal M \subset \mathbb R^N,\qquad \dot\sigma = F(\sigma,\theta,u)
\]

最压缩解释：
> **神经状态不是离散标签，而是高维流形上的连续轨迹。**

### 2.2 L0 → L1 Projection
\[
\Pi_{ignite}: \mathcal M \to \mathcal M_*
\]

其中 `\mathcal M_*` 是满足点燃阈值的稳定子集。

最短说法：
> **意识相关显现不是“活动更强”，而是轨迹被成功投影到可锚定区域。**

---

## 3. 为什么归一化是本体必然

### 3.1 Canonical Normalization
\[
R_i = \frac{L_i^n}{\sigma^n + \sum_j w_{ij}L_j^n}
\]

SRT 在这里的强主张是：
> **除法归一化不是电路细节，而是在代谢受限条件下执行选择的必然形式。**

### 3.2 Energy–Information Extremum
\[
\mathcal J = H(\sigma) - \lambda E(\sigma)
\]

压缩结论：
- 神经系统同时受信息收益与能量成本约束
- 归一化是两者的交点

---

## 4. 学习不是记忆堆叠，而是 L2 收敛

### 4.1 Predictive Update
\[
\Delta\theta \propto -\nabla_\theta F
\]

最压缩解释：
> **学习不是在 L1 上堆内容，而是在 L2 上重写未来选择规则。**

也就是说：
- 突触改变不是“存东西”这么简单
- 而是在塑造下一次 `\hat G_\theta` 如何取值

---

## 5. 多尺度神经算子

### 5.1 Loop-Gating
丘脑—基底节回路不是简单通路，而是：
> **决定哪些轨迹有资格进入显现层的门控结构。**

### 5.2 Meso-Operator / Glial Pruning
\[
\hat G_{meso}: L_2^{micro} \to L_2^{pruned}
\]

压缩含义：
- 胶质剪枝不是附属维护
- 而是慢时标的结构性选择

### 5.3 Stability–Pruning Link
过度剪枝会导致：
- `L_2` 硬化
- 可塑性下降
- 病理锁定增加

---

## 6. 点燃、离散帧与摩擦

### 6.1 Ignition as Candidate Gate Family
\[
\mathcal A(\sigma) \ge \tau_{ignite} \land \Phi_{proxy}\cdot d_{proxy} > C_{critical}
\]

> **Level**: hypothesis / operational proxy. The product gate is a current structural preference; ignition as threshold or phase transition is not yet a proven neural theorem.

最短说法：
> **点燃不是激活增强；当前最小模型把它写成整合度 proxy 与关切梯度 proxy 共同约束的候选门。**

| Gate | Use | What would favor it |
|------|-----|---------------------|
| Multiplicative | structural preference when both integration and concern-gradient look jointly necessary | Either factor being low blocks ignition, and an interaction term predicts access better than linear terms alone. |
| Additive | operational fallback when compensation is observed | High integration can partly compensate low `d_proxy`, or high `d_proxy` can partly compensate low integration. |
| Probabilistic | lab-facing model for noisy / graded reports | Trial-level access is better fit by sigmoid probability than by hard threshold. |

### 6.2 Discrete Frame Theorem
\[
L_1(t)=\sum_n \text{Frame}_n\,\delta(t-t_n)
\]

压缩结论：
- 显现是离散更新帧
- 连续意识感是高频帧序列的结果

### 6.3 Prediction Error as Local Friction Proxy
\[
\widehat{\Psi}_{f,neural}^{local}(t)=\alpha_{pe}\|\varepsilon_{pred}(t)\|+\beta_{load}\mathcal L_{model}(t)
\]

> **Level**: hypothesis / operational proxy, downstream of `H-NEURO-4b`. This bridge must not be used to promote PE-based conclusions to theorem level.

这一步很关键，因为它把：
- 预测误差
- 自由能更新
- 模型竞争负荷
- 局部摩擦 proxy

压到同一条可测桥上，但不把它们写成同一对象。

`L_model` 在此指竞争内部假设的负荷：候选 latent cause、行动策略、身体状态解释或社会意图解释之间的后验歧义、有效复杂度与分歧度。实验上可用解码器后验熵、候选解释数量、ACC/PFC conflict proxy、反应时/眼动歧义指标近似；这些近似不能单独定义 `Ψ_f`。

---

## 7. 工作记忆与时间复用

### 7.1 Theta–Gamma Dual Mode
SRT 将工作记忆重写为：
- 持续活动模式
- theta 节律下的多吸引子分时复用模式

最压缩句子：
> **工作记忆容量不是神秘常数，而是时间调度带宽的结果。**

这也意味着：
- `d_temporal` 有可计算上限
- 容量限制是动力学结果，不是简单缺陷

---

## 8. 病理学：参数漂移，而不是症状堆叠

### 8.1 Parameter Drift
\[
\theta = \theta_{healthy} + \Delta\theta
\]

SRT 对病理学的最强改写之一是：
> **精神病理首先是参数空间的偏移，其次才表现为症状。**

这带来三个后果：
- 病理可几何化
- 病理可量化
- 治疗目标变成参数校正而不是只压表象

---

## 9. 最压缩结论

`SRT Neural Mechanisms` 可以压缩成五句话：

1. **神经系统不是单纯信息处理器，而是具身选择算子的实现。**
2. **神经显现来自流形轨迹被门控并投影进可锚定的点燃子空间。**
3. **除法归一化是受限选择的本体必然，不只是经验电路技巧。**
4. **学习、剪枝与工作记忆都可被统一写成多时标选择动力学。**
5. **病理最深层上是参数漂移与选择失衡，而不是表面症状清单。**

---

## 10. 阅读路径

- 全量原文：`SRT_Neural_Mechanisms.md`
- Neuro bridge：`_SRT_Neuro_Axioms.md`
- Consciousness 机制：`SRT_Consciousness_Mechanisms.md`
- canonical 总注册表：`../CANONICAL_REGISTRY.md`

---

## Hardest Objections

本域若以下任一成立，则本域主张会被显著削弱：

1. Prediction error is not an independent friction proxy.
   - 当前承受方式：`H-NEURO-4b` only treats PE as a local measurable candidate, not an identity with `Ψ_f`.
   - 若成立需撤回什么：撤回 PE-to-local-friction-proxy 的局部线性桥，把相关段落降为普通 FEP comparison.

2. `Φ` and `d` cannot be independently measured in neural systems.
   - 当前承受方式：the product gate is an operational proxy and can be replaced by additive or probabilistic gates.
   - 若成立需撤回什么：撤回 `Φ_proxy·d_proxy` candidate gate as a subjectivity criterion and keep only separated diagnostic dimensions.

3. Ignition is continuous, report-mediated, or task-dependent rather than a phase transition.
   - 当前承受方式：phase-transition language is marked as hypothesis and must be tied to explicit observation windows.
   - 若成立需撤回什么：撤回 “crossing threshold” as ontology and rewrite ignition as graded stabilization.

4. Neural burden is fully reducible to generic predictive error.
   - 当前承受方式：`H-NEURO-4b` requires residual burden proxies such as metabolic cost, recovery half-life, stress load, or position-bound consequence beyond PE itself.
   - 若成立需撤回什么：撤回 SRT-specific neural burden language and keep the section as a predictive-processing translation note.
