---
id: SRT-CORE-PHASESTATE
type: definition
tags: [PhaseState, HistoryClosure, NormativeGradient, SelfWriteback, Life, Consciousness]
status: hardened_v1
layer: L1
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-CORE-001, SRT-CORE-12A, SRT-CORE-DS-11]
hardened: 2026-04-08
---

# SRT 高阶相态三条件（Triple Condition for High-Order Phase State）

> **地位说明**
> 本文件将 `Core/Dynamics_Scaling_Annex/11_G_CrossScale_PhaseState.md` 中硬化的
> 三相态条件从 Annex 层提升至 Core 层，作为生命/意识判定标准的规范定义。
> 所有引用"为什么G在生命层不同于物理层"的文件应以本文件为锚点。

---

## 1. 核心主张

$$\text{生命/意识} \neq \text{G的起点} \quad \text{而是} \quad \text{G达到三条件后的高阶相态}$$

G（选择算子）是跨尺度的选择结构，在物理层已以低阶形式存在（proto-G）。生命与意识是 G 的相变状态——当 G 同时满足以下三个条件时发生相变：

---

## 2. 三个相态条件

### Cond-Phase-1：内部历史闭合（Internal History Closure）

**定义**：系统形成**可被写回的自身连续体**——历史痕迹被整合进当前选择结构，形成闭合的自我参照回路。

不只是有记忆，而是：记忆在选择时刻被主动读取并参与当前 G 的运作。

$$\text{历史闭合} \iff \exists \; h(t): \hat{G}_{\theta}(t) = f(\hat{G}_{\theta}(t-\Delta t), h(t))$$

**缺失时的失败模式**：解离状态——有记忆但无连贯自我（记忆与当前选择断联）。

---

### Cond-Phase-2：规范梯度（Normative Gradient）

**定义**：系统具有**内生方向标准**，产生写回的方向——不只是跟随外部热力学梯度，而是有"应当"方向，驱动选择遮蔽的不对称性。

**精确操作化**（见 `Core/SRT_Core_NormativeGradient.md`）：

> 规范梯度不是外加于热力学梯度的第二种力；其操作化定义为：在历史闭合与自写回系统中，对可维持自身状态的**自指势差读数**。

$$\nabla_{\text{norm}} \equiv \left.\frac{\partial F_{\text{self-maintenance}}}{\partial \sigma}\right|_{\text{self-referential}}$$

**缺失时的失败模式**：漂移状态——有历史但无方向（G随机游走于可能性空间）。

---

### Cond-Phase-3：自写回强度（Self-Writeback Intensity）

**定义**：系统的选择**真能改写自身未来的选择空间**——遮蔽不只影响当前状态，而是重构 G 自身的可能性地图。

强度不足时，G 有方向但无法在自身结构上留下持久印记。

$$\text{自写回强度} > \Theta_{\text{writeback}} \iff \frac{\partial \Omega_G(t+\Delta t)}{\partial \text{selection}(t)} \neq 0$$

**缺失时的失败模式**：成瘾/强迫结构——有方向但无法改变自身（G的选择不写入自身的可能性地图）。

---

## 3. 三条件的结构关系

### 3.1 定义地板：时序依赖

$$\text{历史闭合} \xrightarrow{\text{逻辑前提}} \text{规范梯度} \xrightarrow{\text{逻辑前提}} \text{自写回强度}$$

- 无历史闭合 → 规范梯度无从建立（无自身连续体可读取）
- 无规范梯度 → 自写回是无方向噪声（强度再大也无意义）

### 3.2 相态判别：三个独立维度

三者在定义地板上有依赖，但在相态判别上是**独立维度**：

| 条件 | 提供什么 | 缺失时 |
|---|---|---|
| 内部历史闭合 | 可被写回的自身连续体 | 解离 |
| 规范梯度 | 写回方向 | 漂移 |
| 自写回强度 | 方向是否真能改写未来选择空间 | 成瘾/强迫 |

各条件可独立缺失，产生不同的病理模式，因此是独立的诊断维度。

---

## 4. 与 T-L0-02 相变锚点的对应

T-L0-02 用 κ（稳定化程度）描述三域相变。三相态条件对应κ的具体演化：

| κ 阶段 | G形态 | 三条件状态 |
|---|---|---|
| $\kappa \approx 0$ | proto-G（物理层）| 三条件均未满足 |
| $\kappa_{c1}$ 附近 | 低阶G（细胞/分子）| 历史闭合开始形成 |
| $\kappa_{c1} < \kappa < \kappa_{c2}$ | 中阶G（有机体）| 历史闭合+规范梯度，自写回强度弱 |
| $\kappa > \kappa_{c2}$ | 高阶G（意识）| 三条件齐备，完整相态 |

---

## 5. 与意识三充要条件的关系

`_SRT_D_VALUE_CANONICAL.md §3.1` 的意识三条件：
$$\text{Consciousness} \iff \Psi_f > 0 \;\land\; d > 0 \;\land\; \hat{G}[\theta] \neq \emptyset$$

三相态条件是该框架的**内部机制补充**，不是替代：

| 意识条件 | 三相态条件的对应 |
|---|---|
| $d > 0$（有关切维度）| 历史闭合 + 规范梯度 → d 有实质内容 |
| $\Psi_f > 0$（有摩擦成本）| 自写回强度 → 选择有真实代价 |
| $\hat{G}[\theta] \neq \emptyset$（有参数化算子）| 三条件合并保证算子的参数化是非空的 |

---

## 6. 边界说明

- 三个相变点（历史闭合形成、规范梯度出现、自写回强度达阈值）的量化标准是 SRT 当前开放变量。
- 本文件不主张三条件是意识的充分条件——它们是 G 从低阶向高阶相变的**必要结构条件**；完整的意识充要条件还需 `_SRT_D_VALUE_CANONICAL.md §3.1` 的三项。
- "自写回强度不足 = 成瘾结构"是说明性类比，不是临床诊断定义。
