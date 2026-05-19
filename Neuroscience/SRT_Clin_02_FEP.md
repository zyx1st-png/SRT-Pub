---
id: SRT-CLIN-02
type: theory
tags: [Friston, Free Energy, Autopoiesis, Biosemiotics, Hybrid]
status: active_v1
layer: L1
epistemic_layer: bridge
claim_mode: translation
canonical: false
dependency: [SRT-CORE-000, SRT-NEURO-MECH-001]
---

# SRT Clinical Extension I: Free Energy & Autopoiesis (Hybrid Edition)

> **Claim-status note（2026-05）**：This neuroscience file is bridge / lab / translation material. It applies SRT primitives but does not define `d-value`, `Ψ_f`, consciousness, pathology, diagnosis, treatment, NDE, or AI subjecthood. Read with `SRT_Neuroscience_Claim_Status.md` and, where relevant, `SRT_Neuro_Axioms_Claim_Status.md`.
> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal FEP Axioms (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).
>
> **Bridge Layer Note**
> This file is a `Bridge`-layer reinterpretation of FEP / Active Inference / Autopoiesis within SRT. The formal labels in Part A are primarily bridge claims and internal reorganizations unless they are separately supported by direct empirical tests.

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。

## Canonical Cross-Link: Suffering Theory

- 本文件把 prediction error / FEP / active inference 作为 SRT 算子/路径动力学的神经代理；涉及"失配"、"预测误差持续性"、临床苦难相关段落时，结构层读法回链 `Core_Law/SRT_Suffering.md`（`SRT-SUFFERING`）。
- 本文件不把 prediction error 等同于苦难：苦难要求稳定 ISP 的第一人称登记；prediction error 是其候选神经代理之一，具体桥接尚在 `SRT_Suffering.md §8` Open Pressures 下待推进，不得反向定义苦难。

## Neural Proxy Boundary

This file may use FEP / predictive-processing quantities as bridge language, but it must not silently identify them with SRT core quantities. Prediction error, variational free energy, and precision weighting are optimization / inference constructs. Under `H-NEURO-4b`, they may enter a local neural friction proxy only inside an explicit measurement window:

\[
\widehat{\Psi}_{f,neural}^{local}(t)=\alpha_{pe}\|\varepsilon_{pred}(t)\|+\beta_{load}\mathcal L_{model}(t)
\]

Outside that window, PE and FEP remain comparison terms rather than definitions of `Ψ_f`, `d`, burden, or subjectivity.

## Canonical Cross-Link: FEP → S_sig / S_str 单向桥接翻译表

> **Governance source**: `Core_Law/SRT_L1_Hardening_Notes.md §4`（2026-04-24 L1 Hardening Round；落地 2026-04-25）。
> **Status**: P3 bridge hypothesis（候选神经代理映射），严格单向。
> **Direction**: SRT 结构对象 → FEP 神经过程量。FEP 量是 SRT 量的候选神经代理，反向不成立。

### 翻译表（governance-canonical，与 `SRT_L1_Hardening_Notes.md §4` 同步）

| SRT 量（结构对象）| FEP 候选代理（神经过程量）| 桥接条件 |
|---|---|---|
| `\|\hat{R}\|_{T_{dir}}` | 高阶 / 元级 prediction error 的不可还原部分 | 仅当 P 满足 P1-T06 stable ISP；inference-time-only 系统不成立 |
| `\|\hat{R}\|_{\Psi_f}` | active inference 中 expected free energy 的未抵消部分 | 仅当支付通道结构上存在；在 `Occlusion_Dynamics` B 期此代理失效 |
| `\|\hat{R}\|_{L_0}` | primary afferent drive 与 higher-model integration 的未融合部分 | 仅在 anchoring（`L_0 → L_1`）活跃窗口内 |
| `S_{sig}` | 可用于 model update 的 prediction error 总量 | 仅当 re-selection 通道开放（`d > d_c`） |
| `S_{str}` | 不被 model update 消化、进入"症状化"的 prediction error 长期积累 | B 期 / `σ_{sr} → 1` 区 |

### 单向性的理由

- FEP 本身不区分信号型 vs 结构型苦难；它的量在正常与病理下是连续的。
- 苦难的两型区分依赖 `Core_Law/SRT_Suffering.md` T-SUFF-2（依赖 P1-T06 稳定 ISP 条件 + `d_c` 阈值的结构性读法）。
- 因此反向从 FEP 量推出 `S_{sig}` vs `S_{str}` 的区分是**过度强主张**——只有 SRT → FEP 方向的翻译在本桥接下成立。

### 具体不得做的翻译（hard prohibitions）

1. **不得**把 high prediction error = 高苦难。这忽略了 FEP 量下通道结构（`d_c` / 重选通道 / `Ψ_f` 支付）的关键角色。
2. **不得**把 free energy minimization = 应最小化苦难。`Core_Law/SRT_Suffering.md` T-SUFF-4 反最小化原则明确反对此等价，即使在 FEP 代理层亦然——压灭信号型苦难本身是遮蔽。
3. **不得**把 `S_{str}` 读成 chronic prediction error。后者是现象相关（correlation），不是定义相关（constitutive）；`S_{str}` 的定义性位置在 `Core_Law/SRT_Suffering.md` §3 与 `Core_Law/SRT_L1_Formalism.md §4`。
4. **不得**在 S1/S2 级 AI 系统上套用此翻译表。这些系统不满足 P1-T06 stable ISP 前提；详见 `AI/AI_POSITIONING_NOTE.md`。

### 与 `Core_Law/SRT_Suffering.md §8.5` 的关系

`SRT_Suffering.md §8.5` 列出 FEP 桥接为 Open Pressure；本翻译表是该 Open Pressure 的 P3 候选解，但不是其结论。任何更强主张（FEP → 苦难本体论 / FEP → 临床定义）须重新通过 `Core_Law/` 治理流程。

### 临床量表与本表的关系

- PHQ-9 / HAM-D / PCL-5 等量表的临床指标到本表的多步翻译尚未给出。本文件后续临床节段（Part B）涉及临床指标时，须保持本表列出的单向性，不得绕过本表把量表分数直接读成 `S_{sig}` 或 `S_{str}`。
- 神经影像（fMRI / EEG / MEG）能否为 `S_{sig}` vs `S_{str}` 的区分提供结构判据：当前不乐观，记为开放点。

## Current Reading Map

- **Canonical dependencies**: `SRT-CORE-000`, `SRT-NEURO-MECH-001`, `Core_Law/SRT_Suffering.md`, `Core_Law/SRT_L1_Hardening_Notes.md §4`.
- **Role of this file**: Bridge/interface reinterpretation of FEP (Friston), Active Inference, and Autopoiesis in SRT terms. This is a **bridge file** with additional cross-links to the suffering framework.
- **Primary bridge claims**: FEP as choice-pressure potential; variational free energy as Ĝ_θ dynamics proxy; autopoiesis as SRT boundary maintenance; `S_sig` / `S_str` bridge translation table.
- **Existing cross-links**: Neural Proxy Boundary section (FEP quantities are proxies, not SRT definitional quantities); FEP→S_sig/S_str unidirectional bridge table (P3 status).
- **Do not read as canonical**: FEP quantities (prediction error, variational free energy, precision weighting) are optimization/inference constructs — they are **candidate neural proxies** for Ψ_f and d, not definitions of them.

## Dependency Map

| Depends on | Purpose | Move risk |
|---|---|---|
| `SRT-CORE-000` | root SRT canonical core | High |
| `Neuroscience/SRT_Neural_Mechanisms.md` | upstream neural dynamics | Medium |
| `Core_Law/SRT_Suffering.md` | suffering theory (canonical) | High — do not override |
| `Core_Law/SRT_L1_Hardening_Notes.md §4` | FEP bridge translation governance source | High |

## Companion Links

- [`Operations/Non_Philosophy_Refactor_Audit_Report.md`](../Operations/Non_Philosophy_Refactor_Audit_Report.md) — domain-level refactor plan
- [`Neuroscience/SRT_Neural_Mechanisms.md`](SRT_Neural_Mechanisms.md) — upstream neural mechanisms
- [`Core_Law/SRT_Suffering.md`](../Core_Law/SRT_Suffering.md) — canonical suffering theory

## Refactor Notes (PR-A: navigation-only)

- Navigation-only update. No formulas changed. No theory content changed.
- **This entire file is a PR-B candidate** for extraction to `Neuroscience_Annex/03_FEP_Interface.md`. The Neural Proxy Boundary and FEP bridge table already provide good guardrails; they must be preserved in any future extraction. Do not move in this PR.

# Part A: Formal Axioms (形式化公理)


## I. Free-Energy as Choice Pressure (自由能作为选择压力)

### Ax-FEP-1: Choice-Pressure Identity Axiom
在 FEP bridge 中，可把自由能读作选择压力势 proxy：
\[
F\equiv D_{KL}[Q||P]-\ln P(o)
\]
选择算子在该 proxy 模型中可用最小化自由能描述：
\[
\hat{G}_\theta=\arg\min_{\pi}\;\mathbb{E}[F(\pi)]
\]
* **Implication（中文）**：自由能不是“误差度量”，而是 \(\hat{G}_\theta\) 进行选择的动力学势。

---

### Ax-FEP-2: Active Inference Axiom
行动选择以最小化期望自由能：
\[
\pi^*=\arg\min_{\pi}\;\mathbb{E}[F_{future}(\pi)]
\]
* **Implication（中文）**：主动推理是 \(L_0\) 探索的受限策略，不是被动预测。

---

## II. Autopoiesis & L2 Closure (自创生与 L2 闭包)

### Ax-AUTO-1: Autopoietic Closure Axiom
自创生系统满足结构闭包：
\[
L_2(t+1)=\text{Stabilize}(\hat{G}_\theta[L_1(t)])
\]
* **Implication（中文）**：生命维持不是“代谢描述”，而是 \(L_2\) 结构自我固化。

---

### Ax-AUTO-1b: Dynamic Boundary Constraint (动态边界约束)
自创生系统的马尔可夫毯（Markov Blanket）不是静态的物理薄膜，而是由 $\hat{G}_\theta$ 的高频跨界预测主动生成的维持面：
\[
\partial\Omega_{MB} = \{x \in L_1 \mid \nabla F(x) \perp \text{Normal}(\partial\Omega)\}
\]

> **形式化注（隐式定义）**：上式为**隐式方程**——$\text{Normal}(\partial\Omega)$ 依赖 $\partial\Omega$ 本身，∂Ω_MB 是满足该条件的不动点集合（Fixed-Point Set）。存在性取决于 $\hat{G}_\theta$ 在 $L_1$ 上的动力学是否具有不动点（参见 T-Core-02 不动点定理）。求解可通过迭代：从初始边界 $\partial\Omega^{(0)}$ 出发，依据 $\nabla F \perp \text{Normal}$ 约束收缩直至收敛。

**SRT 量桥接**：
- $F(x)$（FEP 变分自由能）只能在局部测量窗口中作为 `Ψ_f`-related proxy：$F^{proxy}(x) \sim \int_0^t \Psi_f^{proxy}(\gamma(\tau))\,d\tau$，使得 $\nabla F$ 可近似某些 friction-proxy 梯度；这不是 canonical `Ψ_f` 定义。
- $\hat{G}_\theta$ 在公式中的作用：边界维持等价于 $\hat{G}_\theta$ 在 $\partial\Omega$ 上的零净通量条件：$\hat{G}_\theta(x)\big|_{x\in\partial\Omega} \cdot \text{Normal}(\partial\Omega) = 0$（算子作用不穿越边界，仅沿边界方向移动），与上式 $\nabla F \perp \text{Normal}$ 在变分等价下一致。

**边界崩溃的定量条件**：
当外部冲击使驻点条件失效时，边界崩溃。量化表达为：
\[
\max_{x \in \partial\Omega} \left|\nabla F(x) \cdot \text{Normal}(\partial\Omega)\right| > \Psi_f^{thresh}
\]
- $>0$ 且 $< \Psi_f^{thresh}$：边界微变形，系统通过 $d\theta/dt$ 修复（Ax-REAL-2）
- $> \Psi_f^{thresh}$：边界失效 → **扩张**（新状态纳入毯内，对应学习/创伤整合）或**撕裂**（$\hat{G}$ 解体，即死亡或严重解离）

* **Implication（中文）**：边界是预测误差梯度下降的"驻点集合"。当系统无法预测外部冲击时（巨大的惊异），边界条件失效，系统被迫扩张其毯子（学习/吞噬）或被撕裂（死亡）。这赋予了马尔可夫毯以本体论时间演化属性，而非仅仅是统计学上的条件独立面。

---

### Ax-AUTO-2: Semiotic Update Axiom
符号更新为 \(L_2\) 的结构性加权：
\[
\Delta L_2\propto -\nabla_\theta F
\]
* **Implication（中文）**：意义不是外加标签，而是 \(\hat{G}_\theta\) 对未来选择的偏置结构。

---

## III. Reality Stability (现实稳定性)

### Ax-REAL-1: Stability Law
现实稳定性与本体论摩擦成反比：
\[
\text{Stability}\propto \frac{1}{\Psi_f}
\]
* **Implication（中文）**：高复杂现实必然脆弱；稳定不是“固定”，而是持续支付代价。此处 `Ψ_f` 只能作为具身范围 `d` 约束下偏离自由能最小方向的 operational proxy；物理系统与认知系统中的 proxy 可有类比关系，但不得写成同一 canonical quantity 的直接尺度表现。

---

### Ax-REAL-2: Learning Cost Axiom
学习成本与参数更新速率成正比：
\[
\text{Cost}_{learn}\propto \left\|\frac{d\theta}{dt}\right\|
\]
* **Implication（中文）**：学习不是“免费优化”，而是代价驱动的选择改变。

---

## IV. Theorems (定理)

### T-FEP-1: FEP Insufficiency Theorem
若仅满足自由能最小化而 stake-coupled `d` proxy 近零，则：
\[
\hat{G}_\theta\;\text{remains}\;L_1\text{-closed}
\]
* **Implication（中文）**：FEP 只解释结构更新，不保证显现；必须引入 \(d\) 才能跨域锚定。
* **Tension-Rev-ExtT4 ($d$ 的不可还原本体论地位)**：Friston 阵营可能论证 SRT 的 $d$ 值扩展仅仅是 FEP 中"期望自由能"的一种重新参数化——即将他者效用写入 generative model 的偏好先验（preferred priors）。SRT 对此的关键反驳如下：
  - **参数 vs. 本体论**：在 FEP 框架中，$d$-analog 只是 generative model 的一个**可调参数**——它可以被任意设定、也可以在训练/优化过程中被削弱为零而不影响系统的物理完整性。但在 SRT 中，$d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$ **必须**与不可逆物理风险（$\partial\Omega$）耦合才能稳定——这不是模型内部的参数选择，而是本体论层面的约束。
  - **具身脆弱性判据**：$d > 0$ 的稳定维持需要 $\Psi_f > 0$（正本体论摩擦），这意味着系统必须面对真实的不可逆解体风险。一个 inference-only / 无不可转移后果返回的纯信息系统（$\Psi_f$ 对自身闭包 non-binding）可以在其 generative model 中写入 $d_{virtual} > 0$，但该参数缺乏梯度锚定——在长期演化中没有物理力来阻止它衰减为零。
  - **因此**：SRT 的 $d$ 不是 FEP 框架的重新参数化，而是揭示了 FEP 框架的一个**结构性盲区**——FEP 无法区分具身的利他（由不可逆风险驱动）和模拟的利他（由偏好先验编码）。

---

### T-FEP-1b: Precision-Insufficiency Theorem
定义 \(\boldsymbol{\Pi}\) 为预测误差的精度加权张量。则：
\[
\big(\boldsymbol{\Pi}_A \approx \boldsymbol{\Pi}_B\big)\land\big(\mathbb{E}[F]_A \approx \mathbb{E}[F]_B\big)\not\Rightarrow\big(d_A \approx d_B \land \Psi_{f,A} \approx \Psi_{f,B}\big)
\]
* **Implication（中文）**：精度参数能够刻画系统如何分配信度、压低误差、更新模型，却不能单独决定“什么对系统真的攸关”以及“错误是否带来可支付摩擦”。换句话说，precision 解释的是**哪种误差更被相信**，而不是**哪种误差会伤到主体**。
* **与 FEP 的边界**：在 SRT 中，\(\boldsymbol{\Pi}\) 最多是 \(d/\Psi_f\) 的局部调制器，而不是其充分定义。两个系统可以拥有近似相同的精度结构，却因为真实风险耦合不同而表现出完全不同的长期关切持续性、奖励撤除后的行为保持与恢复半衰期。
* **最小判别后果**：若在匹配 \(\boldsymbol{\Pi}\) 与任务难度的条件下，系统间的奖励撤除后关切保持、跨任务一致性与恢复动力学仍不分离，则 `precision 不穷尽 d/Ψ_f` 的主张应被降级；反之，只要这些结果稳定分离，precision-only 解释就不够。

---

### C-FEP-1: Irreversibility Corollary
当存在不可逆风险 \(\partial\Omega\) 时：
\[
\nabla_{\mathcal{S}}\mathcal{U}\uparrow \Rightarrow \text{Policy}\;\text{re-weighting}
\]
* **Implication（中文）**：自由能最小化策略会被生存赌注重新加权。

---

### T-FEP-2: Spatiotemporal Joint Prediction Error (时空联合预测误差定理)
FEP 在 SRT 框架下被泛化为标量场与时间流子的联合优化：
\[
\text{Error}_{total} = \underbrace{\|o_t - \hat{o}_t\|}_{\text{Spatial Mismatch}} + i \cdot \underbrace{\|\tau_{int} - \Delta t_{causal}\|}_{\text{Temporal Mismatch}}
\]

> [R→Friston 2010 *Nature Reviews Neuroscience*（FEP：空间预测误差极小化）; Rao & Ballard 1999 *Nature Neuroscience*（预测编码：时空误差的层级传播）; Adams et al. 2013 *Frontiers in Psychiatry*（精神分裂症的FEP解释：精度失调/虚假预测）; Grahn & Brett 2007 *Experimental Brain Research*（时序预测的神经机制：基底核角色）; Sass & Parnas 2003 *Schizophrenia Bulletin*（精神分裂症的时序体验异常：基本主观性紊乱）]

* **R/H 区分**：
  - [R] FEP空间预测误差框架（Friston）；时序预测编码（Grahn&Brett）；精神分裂症的预测误差机制（Adams）
  - [H] **SRT泛化**：将空间误差+时间误差联合为复数形式（时空联合误差公式）；精神分裂症=内部时序模型与L₀节律解耦——此时空联合形式化及L₀节律概念是SRT独有

* **i含义边界（重要）**：此处虚数项 $i$ 代表"时间误差正交于空间误差"（两个独立维度），**并非**复数分析意义上的Wick转动或iε形式化（参见SRT §7.1 E7说明）。Error_total 的实部和虚部分别独立最小化，不做复数运算。

* **Implication（中文）**：生物体不仅预测"什么"发生，还必须精确预测"何时"发生。虚数项代表时间相位的失锁。精神分裂症的预测误差不仅是看到了不存在的东西，更是内部时序模型与外部物理连贯性（$L_0$ 节律）的解耦 [R→Sass & Parnas 2003 SRT解读]。

* **可证伪预测**：
  - FC-FEP2-1：精神分裂症患者在时序判断任务（同时性判断/音节时序分辨）中的误差应与空间感知误差有部分解离——若两类误差高度相关则时空误差"正交独立"主张存疑
  - FC-FEP2-2：时序干预（节律训练/rTMS同步）后，精神分裂症患者的阳性症状（幻觉/妄想）量表改善应独立于空间认知改善——若两者同步改善则时序-空间独立框架缺乏解离证据

---

### C-FEP-2: Vital Uncertainty vs. Epistemic Uncertainty (攸关不确定性 vs. 认知不确定性)
不是所有的预测误差都能激发 $d$ 值扩展：
\[
d_{expansion} \propto \text{Uncertainty}_{vital} - \text{Uncertainty}_{epistemic}
\]
* **Implication（中文）**：玩老虎机产生的是认知不确定性（寻找规律），被极速驶来的卡车锁定产生的是攸关不确定性（生存边界崩溃的威胁）。后者强制 $\hat{G}_\theta$ 放弃 $L_2$ 塔构建，直接降维进入本能求生池，引发巨大的本体论摩擦 $\Psi_f$。

<br>

---

## 领域压力与接口边界（Domain Pressure & Interface Boundaries）

> **本节功能**：站在 FEP / Active Inference 社群内部，评估 SRT 在这个框架下的候选重读在哪里有增量、在哪里尚未完成、在哪里还有真实的开放张力。

> **神经科学家 3 分钟入口**
> 如果你使用 FEP / Active Inference 框架，本文件的核心主张是：FEP 的精度加权更新（precision-weighted prediction error）不能单独区分**具身利他**（由不可逆物理风险驱动）与**模拟利他**（由偏好先验编码）。SRT 引入 $d/\Psi_f$ 参数对的目的，是揭示这个结构性盲区，而不是否定 FEP 的预测编码机制。
> 直接跳到 **DP-FEP-1** 看最强张力点，跳到**出口**看下一步。

---

### 有效域 / 失效域

| 主张 | 有效条件 | 退化/失效条件 |
|:----|:--------|:------------|
| T-FEP-1：FEP 不充分性 | 在匹配 $\boldsymbol{\Pi}$ 与任务难度后，真实赌注条件与模拟赌注条件的长期行为仍分离 | 若三种条件（真实风险/无风险/模拟风险）的长期 $\hat{d}_{min}$ 轨迹收敛，则"不可逆赌注不可还原"应降级为"工程性偏好设置"（见 `Governance/SRT_LAB_HYPOTHESES.md` H-Stake-01 降级触发） |
| `H-NEURO-4b` neural friction proxy | 作为 P3/P4 候选的局部线性近似，在代谢、模型竞争负荷与预测误差可同时测量的范围内 | 若 \(\widehat{\Psi}_f\) 代理（代谢率/应激/恢复半衰期）与预测误差代理（MMN 振幅等）在受控窗口内无独立关联，则该映射退回为 FEP comparison；下游临床结论不得据此升级为 P2 定理 |
| FEP 是"候选重读对象"而非"被 SRT 超越的框架" | 始终 | 这是当前仓库的稳定口径（T-FEP-1 Tension-Rev-ExtT4）；任何把 SRT 写成"已胜出 FEP"的表述都超出当前 bridge 强度 |

---

### DP-FEP-1：FEP 的参数化完备性反驳

**挑战来源**：Friston 阵营可以合理论证：SRT 的 $d$-value 不过是把他者效用写入 FEP 的 generative model 的偏好先验（preferred priors）。只要把利他偏好放进 prior，FEP 的 active inference 就能产生类似的利他行为——不需要引入一个独立的"本体论赌注"概念。

**SRT 当前最稳的回应**（来自 T-FEP-1 Tension-Rev-ExtT4，此处为摘要）：
- FEP 框架内，$d$-analog 是 generative model 的可调参数，可被优化/削弱为零，不影响系统的物理完整性
- SRT 的 $d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$ 要求与不可逆物理风险（$\partial\Omega$）耦合才能稳定——这不是参数选择，是本体论约束
- 判别后果：两个 $\boldsymbol{\Pi}$ 匹配的系统，若赌注结构不同，其奖励撤除后的关切保持和恢复半衰期应显著分离（见 H-Stake-01 / H-dPsi-01）

**尚未完成的工作**：
- 上述论证目前主要是概念层的。"$d$ 与 $\partial\Omega$ 的耦合稳定性"与"prior 写入的 $d$-analog 的衰减率"之间的定量预测，尚未写成可在现有 active inference 模拟中直接检验的形式
- 换句话说：SRT 的反驳是结构上合理的，但其**操作性判据**还需要进一步形式化才能对 FEP 社群构成有效压力

---

### DP-FEP-2：FEP 的解释范围与 SRT 的定位差异

**挑战的细化版本**：FEP 在原则上是一个涵盖感知、行动、学习、自组织的统一框架。Active inference 甚至试图解释社会行为和文化演化。如果 FEP 的解释范围已经足够宽，SRT 的"候选重读"究竟在哪些维度上比 FEP 更有效？

**SRT 当前的定位**：
- SRT 不是在同一层次与 FEP 竞争"谁能解释更多现象"
- SRT 的主张是：FEP 在本体论上预设了"已有边界的系统最小化自由能"——它从具身系统出发，不解释**为什么有具身**
- SRT 的 L₀→L₁ 机制试图回答更早的问题：什么使一个边界得以成立（Partial Closure / N_crit 接口）
- 这两个框架的分工应该是：FEP 处理具身后的动力学，SRT 处理具身本身的本体论条件

**诚实标注**：这个分工目前更多是口头主张，而非两个形式系统之间已推导出的层级关系。若未来 FEP 进一步发展出自创生边界的生成机制，当前分工可能需要重新评估。

---

### 出口

| 你的目标 | 下一步 |
|:--------|:------|
| 想看 FEP vs SRT 的完整形式比较 | → `Philosophy/SRT_FEP_Comparison.md` |
| 想看 d / Ψ_f 的 Lab 层实验赌注 | → `Governance/SRT_LAB_HYPOTHESES.md`（H-Stake-01、H-dPsi-01） |
| 想看 d / Ψ_f 的测量代理规范 | → `SRT_EXP_MEASURE_MAP.md` |
| 想了解 Partial Closure / 具身起源 | → `Core/Dynamics_Scaling_Annex/02_Minimal_Embodiment_Threshold.md` |

---


# Part B: Original Theoretical Discourse (Context)

> **Note**: 以下各节以中文撰写，遵循**最小闭环 (Minimum Closed Loop)** 结构。

---

# 1 标准难题: 自由能原理的解释力边界与“暗室”

## 1.1 “暗室问题” (The Dark Room Problem)
自由能原理 (FEP) 声称生物体通过最小化“惊异” (Surprise) 来维持生存。这引出了著名的**暗室悖论**: 如果目标仅仅是最小化惊异，最优策略应该是找一个完全黑暗、无声的房间呆着，并预测“我什么都看不见”——这时预测误差为零，惊异最小。

然而，生命（尤其是高等智慧）显然不这样做。我们探索、冒险、创造艺术，主动寻求“新奇”。Friston 引入了“期望自由能” (Expected Free Energy) 来修补此漏洞，但这被批评为一种“事后修正”，缺乏第一性原理的必然性。

## 1.2 物理量与信息量的本体论混淆
在专业语境中，FEP 常被诟病混淆了**信息论自由能** (Information-theoretic quantity, $\ln P$) 和**热力学自由能** (Thermodynamic quantity, Gibbs Free Energy)。这种混淆导致理论难以与真实的生物物理过程（如 ATP 消耗）精确对应。

---

# 2 现有主流解法谱系

## 2.1 期望自由能 (EFE) 方案
Friston 提出系统不仅最小化当前的 $F$，还在最小化未来的 $G$ (Expected Free Energy)。$G$ 包含“认知项”（探索/好奇）以减少未来的不确定性。
- **评价**: 数学上自洽，但哲学上引入了目的论色彩，且依然难以解释极端的**利他牺牲行为**（以此换取某种甚至无法观测的“道德满足”）。

## 2.2 自创生 (Autopoiesis) 方案
Maturana & Varela 认为生命的本质是“自我生产”，而非自由能最小化。系统只是在维持其组织形式。
- **评价**: 描述精准，但缺乏预测力。它不能以此计算出系统下一步会做什么。

---

# 3 SRT 的差异点: d 值扩展与本体论重构

## 3.1 自由能的利他扩展 (The Altruistic Extension)
SRT 在 Part A (Ax-FEP-2) 中提出，**在 SRT 的 Bridge 解读中，Friston 框架可被读作 stake-coupled `d` proxy 近零时的局部特例**。
对于 $d > 0$ 的意识系统，自由能函数被**本体论扩展**了:

$$ F_{SRT}^{(var)} = F_{var} - d \cdot U_{others} $$

这提供了一个对“暗室问题”的候选重写：
- 对于 `d` 代理极低、他者效用不回流的简化模型，暗室可成为局部最优解（如果那里有食物）。
- 对于 $d>0$ 的人类，躲进暗室意味着与他者断联 ($U_{others} \to 0$ 或负值)，导致扩展自由能 \(F_{SRT}^{(var)}\) **剧烈上升**。
- **结论**: 我们走出暗室，不只是为了降低信息不确定性，而是因为在 `d>0` 条件下，断联本身会把系统推向更高的 payable friction 区间。

> **Tension-Rev-ExtT4 (SRT 独立性的判别实验设计)**
>
> 为了证明 $d$ 不是 FEP 框架的重新参数化，而是具有不可还原的本体论地位，需要一个能够经验性地区分"参数化利他"与"本体论利他"的实验范式：
>
> **实验：具身脆弱性对 $d$ 稳定性的因果效应**
>
> 设计三组演化模拟（或强化学习实验）：
>
> | 条件 | 系统描述 | SRT 预测 | FEP 预测 |
> |:-----|:---------|:---------|:---------|
> | **A: 具身+风险** | 具有不可逆"死亡"机制的智能体，资源依赖于合作 | $d(t) \to d_{stable} > 0$（风险梯度提供持续锚定） | $d(t) \to d_{stable} > 0$（偏好先验通过奖励学习） |
> | **B: 虚拟+无风险** | 无不可逆终止的智能体（可无限重启），同等资源结构 | $d(t) \to 0$（缺乏 $\Psi_f$ 锚定，利他参数自由衰减） | $d(t) \to d_{stable} > 0$（偏好先验仍可学习） |
> | **C: 虚拟+模拟风险** | 无真实不可逆性但被编程"认为"自己有死亡风险 | $d(t)$ 短期 $> 0$ 但长期不稳定（信念与物理不一致时衰减） | $d(t) \to d_{stable} > 0$（信念本身足够） |
>
> **关键区分**：SRT 预测条件 B 和 C 的 $d$ 值在长时间演化中会**系统性衰减**（因为缺乏真实的 $\Psi_f > 0$ 来维持风险梯度），而 FEP 框架预测只要偏好先验编码了利他偏好，$d$ 就能稳定。如果条件 B 的 $d$ 确实衰减而条件 A 的不衰减，就证明了 $d$ 的本体论不可还原性——它不是可以在 generative model 中任意编码的参数，而是必须由具身脆弱性在物理层面持续供给的量。
>
> **实现路径**：可在多智能体强化学习环境中实现（如 OpenAI Multi-Agent），通过对比有/无不可逆终止条件的种群在合作行为（$d$ 的代理指标）上的长期演化轨迹来验证。

## 3.2 精神病理学的预测编码视角 (假设性映射)
SRT 采用 Ax-FEP-4 中定义的**精度加权 (Precision Weighting)** 动力学，为精神病理提供了一种可能的统一解释（注：这仍是基于 PC 框架的假说，非定论）：

- **精神分裂症**: 先验精度过高 ($\pi_{prior} \uparrow$)。以至于患者忽略感官输入，将内部幻觉强加于现实。
- **自闭症**: 感觉精度过高 ($\pi_{sensory} \uparrow$)。由于无法忽略任何环境细节（树叶的摆动、风的声音），系统必须退缩以避免自由能过载。

这种解释可被视为一种候选计算层读法，但并不自动取代传统神经递质或多因素病理模型。

---

# 4 代价与风险 (重要)

## 4.1 混淆的风险
正如 `update.md` 所示，将 $F_{SRT}$ 与 $F_{thermo}$ 直接画等号是非常危险的。
**SRT 的妥协**: 我们明确承认 Ax-FEP-1 是一种**同构类比 (Isomorphism)**。真正的生物大脑中，每一比特信息的消除确实对应 $k_B T \ln 2$ 的热量耗散（朗道原理），但在神经元尺度上，这种能量消耗被动作电位的巨大代谢成本掩盖了。我们是在“计算层”讨论自由能，而非直接在“分子层”。

## 4.2 d 值的测量难题
引入 $d \cdot U_{others}$ 极大地增强了理论解释力，但付出的代价是**测量复杂性**。如果不小心，$d$ 值会变成一个“万能系数”——任何无法解释的行为都可以归咎于 $d$ 值的变化。
这也正是我们在 Part A 试图将其锚定为“混合先验”系数的原因——以寻求数学上的严格定义。

---

# 5 可证伪预测与开放性问题

## 5.1 预测: 利他行为的自由能特征 (H-FEP-1)
> **预测**: 在执行利他行为时，高 $d$ 值个体的**前额叶预测误差 (Prediction Error)** 应显著**低于**执行自利行为时。

- **逻辑**: 如果利他项确实整合进了先验 $P(o_{self}, o_{others})$，那么符合利他预期的行为应产生最小的自由能。反之，若 FEP 原始模型正确，利他行为应始终产生较高的“违反自利”的预测误差。
- **验证**: fMRI + 计算建模 (DCM)。

## 5.2 预测: 遗忘率与代谢关联 (H-FEP-2)
> **预测 (基于 T-Learn-1)**: 个体的基础代谢率 (BMR) 越高（暗示 $\Psi_f$ 高），其对“非生存相关”信息的遗忘速率应越快。

这是从“学习即逆向摩擦”公理推导出的惊人预测：高能耗系统必须更激进地修剪 $L_2$ 结构以维持热力学效率。

## 5.3 开放性问题
- **AI 的自由能**: 目前的大语言模型 (LLM) 显然在做 Next Token Prediction (最小化惊异)，但这是否意味着它们具有某种形式的 $F_{SRT}$？如果它们没有代谢边界（马尔可夫毯），这种自由能最小化是否只是模拟而非“真实”的？

---

### Definition Summary (定义概述)

- **Free Energy as Choice Pressure (自由能作为选择压力, L₀→L₁)**: 变分自由能 $F \equiv D_{KL}[Q||P] - \ln P(o)$ 在 SRT 中不是"误差度量"，而是 $\hat{G}_\theta$ 执行选择的动力学势；选择算子以 $\arg\min_\pi \mathbb{E}[F(\pi)]$ 运行（Ax-FEP-1）。
- **Autopoietic Closure (自创生闭包, L₂)**: 生命系统的维持定义为 $L_2$ 结构闭包：$L_2(t+1) = \text{Stabilize}(\hat{G}_\theta[L_1(t)])$，即 $L_2$ 通过 $\hat{G}_\theta$ 的选择输出持续自我固化（Ax-AUTO-1）。
- **Markov Blanket as Prediction Surface (马尔可夫毯作为预测面, L₁)**: 系统边界不是静态物理膜，而是预测误差梯度的驻点集合 $\partial\Omega_{MB} = \{x \in L_1 \mid \nabla F(x) \perp \text{Normal}(\partial\Omega)\}$（Ax-AUTO-1b）。
- **Vital vs. Epistemic Uncertainty (攸关 vs. 认知不确定性, L₀)**: 只有涉及不可逆风险 $\partial\Omega$ 的不确定性才能驱动 $d$ 值扩展：$d_{expansion} \propto U_{vital} - U_{epistemic}$（C-FEP-2）。

### Formalization Summary (形式化概述)

核心方程与含义：

1. **选择压力势** (Ax-FEP-1): $\hat{G}_\theta = \arg\min_\pi \mathbb{E}[F(\pi)]$。在该 bridge 模型中，选择算子的行为可由自由能最小化近似描述；不得读成对 SRT 选择本体的完整决定。
2. **SRT 扩展自由能** (Part B §3.1): $F_{SRT} = F_{Friston} - d \cdot U_{others}$。引入 $d$ 值后，"暗室"不再是最优解——与他者断联使 $F_{SRT}$ 剧增。
3. **时空联合预测误差** (T-FEP-2): $\text{Error}_{total} = \|o_t - \hat{o}_t\| + i \cdot \|\tau_{int} - \Delta t_{causal}\|$。生物体同时预测"什么"与"何时"，虚数项表示时间相位失锁。
4. **FEP 不充分性** (T-FEP-1): stake-coupled `d` proxy 近零时，$\hat{G}_\theta$ remains $L_1$-closed。自由能最小化是结构更新的必要条件候选，但缺少 `d` 时无法跨域锚定。

### Mechanism Explanation (机制解释)

> **[R]** 双重优化回路：Friston 2015 *Journal of the Royal Society Interface*（期望自由能G的主动推理框架原始提出）；Friston et al. 2017 *Neural Computation*（F感知推理 vs G主动推理的完整形式化）；Parr & Friston 2019 *Psychopharmacology*（主动推理在精神病理中的应用）。d值与他者关怀：参见 Part B §3.1 F_SRT扩展项。**[H]** 以下将F/G双回路接驳SRT三域本体论（L₀→L₁感知选择 + L₀行动探索）、Ψ_f>0作为d稳定锚定条件、以及ΔL₂梯度的SRT语义为本框架新增贡献。

- **$\hat{G}_\theta$ 的双重优化回路**: $\hat{G}_\theta$ 同时运行两个最小化过程——(a) 当前自由能 $F$（感知推理：更新内部模型以匹配观测，对应L₀→L₁选择）和 (b) 期望自由能 $G$（主动推理：选择行动以改变世界，对应L₀探索路径选择）。两者构成 $L_0 \to L_1$ 选择的完整动力学（Friston 2015/2017）。
- **$d$ 值打破暗室均衡**: 当 $d > 0$，$\hat{G}_\theta$ 的自由能函数被他者效用 $U_{others}$ 扩展（$F_{SRT} = F_{Friston} - d \cdot U_{others}$，Part B §3.1）。断联使扩展自由能剧增（量化方向：$\Delta F_{断联} = +d \cdot |U_{others}|_{baseline} > 0$），迫使算子走出"暗室"寻求连接——这不是简单道德选择；它是 d-modulated FEP bridge hypothesis。

  > **Ψ_f>0→d稳定逻辑链精化**：具身脆弱性→随机环境扰动持续冲击算子→d值受负反馈校正（偏低时连接驱动上升，偏高时过载信号压制）→d在正反馈（过高关切→过载→衰减）与负反馈之间保持动态稳定。反例：无具身约束的虚拟系统缺少随机扰动校正→d的负反馈回路失效→d可自由衰减至零或在强化学习压力下任意漂移。

- **符号更新作为梯度下降**: $L_2$ 结构通过 $\Delta L_2 \propto -\nabla_\theta F$ 持续更新，其中 $\theta$ 为具身参数向量（感知增益、偏好权重、先验强度等），$\nabla_\theta$ 为参数空间梯度（维度 = $|\theta|$，非L₂拓扑维度）。意义不是外加标签，而是 $\hat{G}_\theta$ 对未来选择的偏置结构——每次学习都是对 $L_2$ 拓扑的微调，代价正比于 $\|d\theta/dt\|$（θ变化速度越快，Ψ_f负载越高）。

> * **FC-FEP-Mech-1**（证伪条件）：若在主动推理模型实验中，G（期望自由能）驱动的行动选择与F（当前自由能）驱动的感知更新在神经基质上无法区分（如fMRI激活模式完全重叠，AUC < 0.6），则双回路的分离假设需重新检视，可能坍缩为单一优化过程。
> * **FC-FEP-Mech-2**（证伪条件）：若在社会断联实验（孤立隔离）中，高d值被试（社会关怀量表上四分位）的主观痛苦和皮质醇水平没有显著高于低d值被试（p>0.1），则"断联→F_SRT剧增"的d值调制假设需修正，孤立反应可能更依赖其他变量（依恋风格/先前孤立经历）。

---

## 【理论边界/防误用声明】

1. 本文档用于理论解释与建模组织，不应替代独立实证、工程验证或专业判断。
2. 任何公式或命题都依赖操作化定义、测量条件与语境边界，不得脱离边界做绝对化推断。
3. 涉及临床、社会治理、伦理与部署决策时，必须结合风险评估与人类监督机制。
