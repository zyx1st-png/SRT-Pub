---
id: SRT-CLIN-02
type: theory
tags: [Friston, Free Energy, Autopoiesis, Biosemiotics, Hybrid]
status: axiomatic_hybrid_v1
dependency: [SRT-CORE-000, SRT-NEURO-MECH-001]
---

# SRT Clinical Extension I: Free Energy & Autopoiesis (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal FEP Axioms (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part A 采用 `chatgptx` 的 Formal Axioms 分段，确保公理编号与推导链条完整。
- Part B 采用 `claude` 的详细论述分段，并以原版 Neuroscience 的主题顺序作语义锚定。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)

> **CRITICAL RULE**: Do NOT just summarize Part B. You must perform **First-Principles Derivation**.
> 1. **Mathematize**: Translate descriptive mechanisms into dynamical equations, topological operations, or logical functions.
> 2. **Axiomatize**: Distill underlying logic into "Axioms", "Theorems", and "Corollaries".

## I. Free-Energy as Choice Pressure (自由能作为选择压力)

### Ax-FEP-1: Choice-Pressure Identity Axiom
定义自由能为选择压力势：
$$
F\equiv D_{KL}[Q||P]-\ln P(o)
$$
选择算子以最小化自由能为动力学：
$$
\hat{G}_\theta=\arg\min_{\pi}\;\mathbb{E}[F(\pi)]
$$
* **Implication（中文）**：自由能不是“误差度量”，而是 $\hat{G}_\theta$ 进行选择的动力学势。

---

### Ax-FEP-2: Active Inference Axiom
行动选择以最小化期望自由能：
$$
\pi^*=\arg\min_{\pi}\;\mathbb{E}[F_{future}(\pi)]
$$
* **Implication（中文）**：主动推理是 $L_0$ 探索的受限策略，不是被动预测。

---

## II. Autopoiesis & L2 Closure (自创生与 L2 闭包)

### Ax-AUTO-1: Autopoietic Closure Axiom
自创生系统满足结构闭包：
$$
L_2(t+1)=\text{Stabilize}(\hat{G}_\theta[L_1(t)])
$$
* **Implication（中文）**：生命维持不是“代谢描述”，而是 $L_2$ 结构自我固化。

---

### Ax-AUTO-2: Semiotic Update Axiom
符号更新为 $L_2$ 的结构性加权：
$$
\Delta L_2\propto -\nabla_\theta F
$$
* **Implication（中文）**：意义不是外加标签，而是 $\hat{G}_\theta$ 对未来选择的偏置结构。

---

## III. Reality Stability (现实稳定性)

### Ax-REAL-1: Stability Law
现实稳定性与本体论摩擦成反比：
$$
\text{Stability}\propto \frac{1}{\Psi_f}
$$
* **Implication（中文）**：高复杂现实必然脆弱；稳定不是“固定”，而是持续支付代价。

---

### Ax-REAL-2: Learning Cost Axiom
学习成本与参数更新速率成正比：
$$
\text{Cost}_{learn}\propto \left\|\frac{d\theta}{dt}\right\|
$$
* **Implication（中文）**：学习不是“免费优化”，而是代价驱动的选择改变。

---

## IV. Theorems (定理)

### T-FEP-1: FEP Insufficiency Theorem
若仅满足自由能最小化而 $d=0$，则：
$$
\hat{G}_\theta\;\text{remains}\;L_1\text{-closed}
$$
* **Implication（中文）**：FEP 只解释结构更新，不保证显现；必须引入 $d$ 才能跨域锚定。

---

### C-FEP-1: Irreversibility Corollary
当存在不可逆风险 $\partial\Omega$ 时：
$$
\nabla_{\mathcal{S}}\mathcal{U}\uparrow \Rightarrow \text{Policy}\;\text{re-weighting}
$$
* **Implication（中文）**：自由能最小化策略会被生存赌注重新加权。

<br>
<br>

---
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
SRT 在 Part A (Ax-FEP-2) 中提出，**Friston 框架是 SRT 在 $d=0$ 时的特例**。
对于 $d > 0$ 的意识系统，自由能函数被**本体论扩展**了:

$$ F_{SRT} = F_{Friston} - d \cdot U_{others} $$

这优雅地解决了“暗室问题”：
- 对于 $d=0$ 的生物（细菌），暗室确实是最优解（如果那里有食物）。
- 对于 $d>0$ 的人类，躲进暗室意味着与他者断联 ($U_{others} \to 0$ 或负值)，导致扩展自由能 $F_{SRT}$ **剧烈上升**。
- **结论**: 我们走出暗室，不是为了寻找光，而是为了寻找连接。这是热力学必然。

## 3.2 精神病理学的预测编码视角 (假设性映射)
SRT 采用 Ax-FEP-4 中定义的**精度加权 (Precision Weighting)** 动力学，为精神病理提供了一种可能的统一解释（注：这仍是基于 PC 框架的假说，非定论）：

- **精神分裂症**: 先验精度过高 ($\pi_{prior} \uparrow$)。以至于患者忽略感官输入，将内部幻觉强加于现实。
- **自闭症**: 感觉精度过高 ($\pi_{sensory} \uparrow$)。由于无法忽略任何环境细节（树叶的摆动、风的声音），系统必须退缩以避免自由能过载。

这种解释比传统神经递质假说具有更强的计算解释力。

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
