---
id: SRT-NEURO-MECH-COMPACT-CORE
type: theory
tags: [Neuroscience, Mechanisms, Compact Core, Ghost Operator]
status: active_v1
layer: L1
epistemic_layer: os
claim_mode: bridge
canonical: false
dependency: [SRT-NEURO-AXIOMS-001, SRT-NEURO-MECH-001]
---

# SRT Neural Mechanisms — Compact Core

> **Claim-status note（2026-05）**：This neuroscience file is bridge / lab / translation material. It applies SRT primitives but does not define `d-value`, `Ψ_f`, consciousness, pathology, diagnosis, treatment, NDE, or AI subjecthood. Read with `SRT_Neuroscience_Claim_Status.md` and, where relevant, `SRT_Neuro_Axioms_Claim_Status.md`.
> **定位**：本文件是 `SRT_Neural_Mechanisms.md` 的紧凑主干版。  
> **用途**：用于快速把握 SRT 如何把神经机制重写为选择动力学，而不是单纯信息处理。  
> **关系**：不替代原文；原文保留病理参数化、免疫接口、量子基质与工作记忆振荡等展开层。  
> **2026-04 hardening note**：本版吸收 `SRT_Neuroscience_Hardening_N1_N9_v0_1.md` 的神经选择主干，尤其是 N1-N5 / N8-N9。新增内容在功能上是 bridge / lab hardening；除非另经 claim-ladder 提升，不自动升格为 primitive axiom。

## 1. 核心问题

这篇最核心的问题是：

> **神经系统到底是在“处理信息”，还是在执行一种具身选择？**

SRT 的压缩回答是：
- 神经系统不是被动传输器
- 而是 `\hat G_\theta` 的具身实现
- 它在神经流形上把 `L_0` 压成可显现的 `L_1`

### 1.1 2026 hardening: neural selection before representation

本轮神经科学硬化把本文件的核心命题压成更可防守的形式：

> **神经系统不只是表征器；表征是选择稳定后的产物。**

因此，感知、行动、判断与意识内容不应被理解为外部输入的直接复制，而应被理解为候选状态在身体状态、注意增益、行动准备、历史权重与关切价值约束下被稳定出来的 `L_1`。

| SRT term | Neuroscience-facing interpretation |
|---|---|
| `L_0^{accessible}` | 当前系统可访问、可激活、可竞争的候选知觉 / 行动 / 解释空间 |
| `\hat G_\theta` | 竞争、增益、门控、稳定化构成的具身选择过程 |
| `L_1` | 当前被锚定的知觉、行动、判断、意识内容 |
| `L_2` | 选择历史沉积成的先验、习惯、图式、技能、情绪标记与规范内化 |
| `\Psi_f` | 候选状态稳定为 `L_1` 所需支付的多维选择摩擦 |
| `d-value` | 候选状态对身体调节、行动后果、自我模型与未来可选择性的关切权重 |

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

### 2.3 Composite `\hat G_\theta` architecture

2026 hardening 将神经层面的 `\hat G_\theta` 明确写成复合选择架构，而不是单一脑区或单一机制：

\[
\hat G_\theta^{neural}\approx \text{Stabilization}\circ \text{Gating}\circ \text{Gain}\circ \text{Competition}
\]

| Stage | Role | Candidate neural realization |
|---|---|---|
| Competition | 多个候选状态共激活但尚未稳定为 `L_1` | 侧抑制、多稳态知觉、表征竞争 |
| Gain modulation | 根据身体、注意、情绪、精度与 `d-value` 改变候选胜率 | 注意增益、精度加权、神经调质、salience network |
| Gating | 决定候选能否进入行动、报告、工作记忆或意识通达 | 基底节-丘脑-皮层环路、前额叶门控、动作选择 |
| Stabilization | 候选获得持续性并可指导行为或报告 | 递归加工、工作记忆、全局通达、可塑性 |

约束条件：不是所有神经活动都算完整的 `\hat G_\theta` 实例。只有当存在候选竞争、theta/d/L2/Psi_f 相关偏置、门控许可与稳定化结果时，才构成 SRT 意义上的现实锚定事件。

---

## 3. 归一化的 P3 机制地位

### 3.1 Canonical Normalization
\[
R_i = \frac{L_i^n}{\sigma^n + \sum_j w_{ij}L_j^n}
\]

SRT 在这里保留的主张是：
> **除法归一化是具名代谢／带宽约束下的神经竞争机制候选，不是所有选择系统的必然形式。**

### 3.2 Energy–Information Extremum
\[
\mathcal J = H(\sigma) - \lambda E(\sigma)
\]

压缩结论：
- 神经系统同时受信息收益与能量成本约束
- 归一化可作为两者权衡下的候选解；目标泛函若未指定成本函数、约束与动态，不能推出唯一解
- 相对神经响应通向行为选择还需冻结读出、阈值／累积或采样规则、执行门与 held-out 检验（P3-Scale-NB1）
- 首个具名 P4 工作线为 `SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md`；当前只到 card-defined 黄灯，跨研究证据不可拼成通过

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

### 4.2 L2 as sedimented selection constraint

2026 hardening 将 `L_2` 的神经科学解释从“记忆/先验”扩展为：

> **`L_2` 是过往选择沉积形成的结构，它通过降低稳定路径内部的 `\Psi_f`、提高不兼容替代路径的 `\Psi_f`，来约束未来选择动力学。**

| Phenomenon | SRT reading |
|---|---|
| Habit | 重复 `L_1` 行动沉积为低摩擦 `L_2` 路径 |
| Expert intuition | 专业图式降低领域相关候选的锚定摩擦 |
| Trauma | 高 `d-value` 事件异常硬化为威胁型 `L_2` |
| Bias | 某些解释路径低摩擦化，导致过早现实锚定 |
| Norm internalization | 社会 `L_2` 被内化为个体选择地形的一部分 |

核心预测：
\[
\Psi_f(\text{trained path})\downarrow,\qquad \Psi_f(\text{incompatible alternative})\uparrow
\]

这意味着 `L_2` 硬化同时带来效率提升与可能性收缩。

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

### 6.4 `\Psi_f` as multidimensional selection friction

2026 hardening 将 `\Psi_f` 明确降格为可测潜变量，而非单一神经标记：

\[
\Psi_f(\theta)=\alpha_\theta C+\beta_\theta E+\gamma_\theta M+\delta_\theta A+\eta_\theta B+\lambda_\theta H+\rho_\theta R
\]

| Term | Meaning |
|---|---|
| `C` | 候选冲突 |
| `E` | 预测违背 / epistemic mismatch |
| `M` | 模型重构成本 |
| `A` | 行动切换与门控成本 |
| `B` | 身体负荷 / interoceptive strain |
| `H` | 历史惯性 / `L_2` 阻力 |
| `R` | 情绪、社会或实际风险 |

区别：
- `\Psi_f` 不是 cognitive effort；effort 只是其主观/行为表现之一。
- `\Psi_f` 不是 prediction error；PE 衡量不匹配，`\Psi_f` 衡量锚定成本。
- `\Psi_f` 不是 uncertainty；uncertainty 衡量候选分布分散，`\Psi_f` 衡量把分散压缩成现实承诺的成本。

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

### 8.2 Anchoring-dynamics pathology bridge

2026 hardening 对病理学作出更细分的 reality-anchoring 解释：

| Condition | Core SRT imbalance |
|---|---|
| Anxiety | 威胁候选获得过高 `d-value`，模糊输入过早锚定为危险 `L_1` |
| Compulsion / OCD-like closure failure | 低概率高后果风险候选进入 `L_1` 后无法关闭，`\Psi_f(closure)` 持续升高 |
| Trauma | 高 `d-value` `L_1` 事件异常沉积为威胁型 `L_2` |
| Depression | 面向未来的可访问 `L_0` 收缩，正向行动候选难以锚定 |
| Addiction | 即时奖赏路径低摩擦化，替代路径摩擦升高 |
| Delusion-like salience abnormality | 低证据候选获得不成比例现实锚定权 |

原则：治疗不是把正确信息塞入系统，而是帮助系统形成新的、可重复、低摩擦、可行动的 `L_1` 锚定，并逐渐重塑 `L_2`。

---

## 9. `d-value`: concern-weighted selectability

本文件把 `d-value` 明确区别于 salience、attention、reward 与 precision：

| Concept | Question answered |
|---|---|
| Salience | 什么突出？ |
| Attention | 什么被资源处理？ |
| Reward | 什么被趋近或强化？ |
| Precision | 什么被系统信任为信息源？ |
| `\Psi_f` | 锚定需要支付多大成本？ |
| `d-value` | 什么真正关系到系统？ |

核心句：

> **Salience makes a signal noticeable; d-value makes a signal matter.**

神经层面，`d-value` 不定位于单一区域，而是内感受、奖赏/威胁、行动后果、自我相关、社会评价和未来可选择性系统的整合变量。

概念式：
\[
d(x)=w_bB(x)+w_aA(x)+w_rR(x)+w_sS(x)+w_mM(x)+w_fF(x)
\]

其中 `B` 为身体相关性，`A` 为行动后果，`R` 为奖赏/威胁，`S` 为自我模型相关性，`M` 为记忆/身份共振，`F` 为未来选择空间影响。

---

## 10. Experimental roadmap and mainstream-theory distinction

### 10.1 Minimal experimental variables

| SRT variable | Manipulation | Measures |
|---|---|---|
| `L_0^{accessible}` | 模糊图像、多稳态刺激、多义词、动作选择 | 候选报告、选择分布、眼动 |
| `d-value` | 自我相关、健康风险、金钱、威胁、身份、声誉 | 记忆、行动改变、生理唤醒、主观重要性 |
| `\Psi_f` | 冲突、规则切换、不确定反馈、关闭需求、责任负荷 | RT、错误率、瞳孔、皮电、信心、修改率 |
| `L_2` | 训练、重复、情绪标记、奖惩强化 | 迁移、偏置、逆转成本、保持率 |

旗舰实验候选：
1. 模糊知觉 × `d-value` × `L_2` 训练；
2. 规则硬化与逆转成本；
3. 高责任关闭成本任务；
4. 安全重锚定任务；
5. 未来 `L_0` 可访问性任务；
6. 成瘾替代路径摩擦任务。

### 10.2 Distinction from neighboring frameworks

| Theory | SRT absorbs as | SRT distinction |
|---|---|---|
| Predictive processing | 候选生成、误差、precision/gain | SRT 解释现实锚定，不只是模型更新 |
| FEP | 自维持底层与稳定约束 | SRT 加入 lived anchoring、`d-value` 与 `L_1 -> L_2` 沉积 |
| Active inference | 行动门控与策略选择层 | SRT 把行动解释为现实承诺与沉积路径 |
| Global workspace | `L_1` 稳定化/通达路径之一 | SRT 包含通达前竞争与通达后硬化 |
| IIT | 可能的整合结构约束 | SRT 强调关切加权锚定，而非整合度本身 |
| Reinforcement learning | `L_2` 形成机制之一 | `d-value` 宽于 reward；`\Psi_f` 宽于 prediction error |
| Embodied cognition | `\theta`、身体 d、行动 affordances | SRT 主张 reality-selection itself is bodily |

压缩区分：
> Predictive processing explains how the brain guesses the world. FEP explains how systems maintain themselves. Global workspace explains access. RL explains value updating. Embodied cognition explains bodily dependence. SRT explains how a candidate possibility, under bodily, concern-weighted, cost-constrained, and historically sedimented conditions, becomes real for the system.

---

## 11. 最压缩结论

`SRT Neural Mechanisms` 可以压缩成七句话：

1. **神经系统不是单纯信息处理器，而是具身选择算子的实现。**
2. **表征不是选择之前的原始事实，而是选择稳定后的产物。**
3. **神经显现来自流形轨迹经竞争、增益、门控、稳定化后投影进可锚定区域。**
4. **除法归一化是受限神经竞争的 P3 机制候选；它不单独产生行为选择，也不是本体必然。**
5. **学习、剪枝与工作记忆都可被统一写成多时标选择动力学。**
6. **`\Psi_f` 是候选进入 `L_1` 的多维锚定成本；`d-value` 是候选对系统的关切后果。**
7. **病理最深层上是现实锚定动力学的扭曲，而不是表面症状清单。**

---

## 12. 阅读路径

- 全量原文：`SRT_Neural_Mechanisms.md`
- Neuro bridge：`_SRT_Neuro_Axioms.md`
- Consciousness 机制：`SRT_Consciousness_Mechanisms.md`
- N1-N9 hardening draft：`SRT_Neuroscience_Hardening_N1_N9_v0_1.md`
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

5. `d-value` collapses into salience, reward, precision, or motivational relevance.
   - 当前承受方式：`d-value` is defined as concern-weighted consequence for body, action, self-model, and future selectability, not as stimulus prominence or reward alone.
   - 若成立需撤回什么：撤回 d-value as an independent bridge variable and reclassify it as a terminological aggregation of existing constructs.

6. `L_2` hardening improves trained-path efficiency without increasing alternative-path friction.
   - 当前承受方式：the efficiency-flexibility tradeoff is an explicit empirical prediction, not a definitional truth.
   - 若成立需撤回什么：weaken the `L_2` basin-hardening model and treat hardening as ordinary learning unless alternative-path cost is demonstrated.
