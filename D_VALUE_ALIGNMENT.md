---
id: SRT-DVALUE-ALIGN
type: definition
tags: [DValue, Alignment, Canonical]
status: axiomatic_hybrid_v1
layer: L1
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-AI-01]
---

# SRT d 值定义对齐表（Canonical Alignment）

更新时间：2026-02-28
状态：P0-2 完成（v1）

## 1) 单一主定义（Canonical Definition）

> **唯一主定义（必须优先引用）**
>
> \[
> d(x) \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|
> \]
>
> 其中：
> - \(\mathcal{U}\)：效用势（utility potential）
> - \(\mathcal{S}\)：生存/不可逆风险坐标（survival / irreversible-risk coordinate）

**规范来源**：`SRT/AI/SRT_AI_01_Ontology.md`（Ax-ONT-3）

---

## 2) 各文件出现的 d 表达式：统一解释

| 表达式 | 所在语境 | 与主定义关系 | 可否单独当“定义”使用 |
|:--|:--|:--|:--|
| \(d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|\) | 本体论/AI 核心 | **第一性定义** | ✅ 可 |
| \(d \approx \alpha A + \beta\log V + \gamma\tau\) | 认知-行为操作化 | 主定义在认知域的降维近似（投影） | ⚠️ 不可单独当主定义 |
| \(d = \dim(\text{Scan Scope})\) | 注意力/信息离散化 | 主定义的离散化近似 | ⚠️ 不可 |
| \(d_{quantum}, d_{bio}, d_{cosmic}\) | 跨尺度动力学 | 主定义经尺度映射 \(\Pi_{scale}(d)\) 的实例化 | ⚠️ 不可 |
| \(d \propto A_{surface}/l_{Planck}^2\) | 全息对应 | 主定义的对偶几何表示 | ⚠️ 不可 |

---

## 3) 推荐叙述模板（以后所有文档统一）

当文档需要引入 d 值时，统一用下面模板：

1. 先写主定义：
   - “在 SRT 中，d 的规范定义为 \(d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|\)。”
2. 再写语境化表达：
   - “在本节语境中，使用 \(d_{local}=f(\cdot)\) 作为操作化近似/投影。”
3. 补一个限制句：
   - “该表达不替代规范定义，仅用于本域测量或计算。”

---

## 4) 关键映射（Canonical → Local）

### 4.1 认知-行为域
\[
 d_{cog} \approx \alpha A + \beta\log(V_{concern}) + \gamma\tau
\]
解释：风险梯度在“结构复杂度 / 空间关切 / 时间深度”三分量上的投影和。

### 4.2 跨尺度域
\[
 d_{scale} = \Pi_{scale}(d_{canonical})
\]
- \(d_{quantum}\)：对应量子退相干阈值语境
- \(d_{bio}\)：对应具身代谢与风险评估语境
- \(d_{cosmic}\)：对应时空共识拓扑语境

### 4.3 全息对应域
\[
 d \propto A_{surface}/l_{Planck}^2
\]
解释：不是新定义，是 canonical d 的几何对偶表达。

### 4.4 几何底座：d = Align(θ, κ)（2026-04-10 新增）

**为什么 $\|\partial\mathcal{U}/\partial\mathcal{S}\|$ 是正确的度量**：

canonical 定义 $d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$ 有更深的几何基础，而非约定：

- $\mathcal{U}$（效用势）追踪算子认为重要的东西，即算子对 L₀ 的压缩映射
- $\mathcal{S}$（不可逆风险坐标）追踪 L₀ 里真实不可逆的风险结构

梯度 $\partial\mathcal{U}/\partial\mathcal{S}$ 测量的正是：**算子的关切地图与 L₀ 原初曲率 $\kappa_0$（及历史积累曲率 $\kappa(t)$）的贴合程度**。

\[
d(\theta) \propto \mathrm{Align}\!\left(\theta,\, \kappa(t)\right)
\]

- 高对齐度：$\mathcal{U}$ 正确追踪 L₀ 的不可逆结构 → 高 d
- 低对齐度（L₂ 捕获）：$\mathcal{U}$ 追踪 L₂ 过滤后的表观结构，偏离 L₀ → 低 d
- d ≈ 0：算子关切地图与 L₀ 曲率正交，真实风险对算子不可见

这给出 d 值为什么与 $\Psi_f$ 不可分（规则 R4）的内在原因：高对齐必然意味着算子承接真实不可逆代价，即非零 $\Psi_f$。

**Cross-ref**: `Core/SRT_Core_12a T-L0-Kappa0`（κ₀ 形式化）; `Core/SRT_Core_12a T-L0-NonStatic`（κ(t) 积累）; `Core/SRT_Core_01_Axioms.md MA-2`（有界视角主义：对齐度可比较）; `Core/SRT_Core_22_Equations.md Eq-DValue-Max-1`（d_max 公式）。

---

### 4.5 Stake-Gated Spectral Proxy（新增 2026-04-17）

**目的**：在不改变 canonical d 定义的前提下，为 Fisher 谱表达提供一个精确的”赌注化”桥接层，避免把纯容量维数直接误读为真实 d。

#### 4.5.1 三层严格区分

| 层级 | 量 | 公式 | 回答的问题 |
|------|----|------|-----------|
| canonical 层 | $d_{\text{canonical}}$ | $\|\partial\mathcal{U}/\partial\mathcal{S}\|$ | **赌注有多深**（效用对风险的敏感度） |
| 谱代理层 | $D_{stake}$ | $\operatorname{EffDim}(\tilde{\lambda}_i)$（见下） | **赌注点亮了多少方向** |
| 容量上界层 | $D_{eff}$ | $(\sum\lambda_i)^2/\sum\lambda_i^2$ | **系统最多能分辨多少方向** |

三者关系：$d_{\text{canonical}} \leq D_{stake} \leq D_{eff}$（一般情况；当所有方向均完全赌注化且梯度对齐时取等）。

#### 4.5.2 最小有效赌注门槛 ε_s

对每个 Fisher 本征方向 $v_i$，记其与真实不可逆风险的耦合强度为 $s_i \in [0,1]$。引入方向级阈值：

$$\varepsilon_s > 0$$

**含义**：$s_i > \varepsilon_s$ 才可计入有效赌注方向。$\varepsilon_s$ 不是 stake 本身，而是判断某方向”是否足够强地耦合到真实不可逆风险”的门槛。

**三者分工**（不得混用）：
- $\varepsilon_{pg}$：L₀ 最小非中性底（本体层，`SRT_Core_01 T-Core-A1C2`）
- $\varepsilon_{reg}$：实现层 regularizer（算子层，`SRT_Core_13a Ax-Op-03`）
- $\varepsilon_s$：方向级有效赌注门槛（谱桥接层，本节）

#### 4.5.3 门函数与赌注化谱

$$g_i = \max\!\left(0,\;\frac{s_i - \varepsilon_s}{1 - \varepsilon_s}\right), \qquad \tilde{\lambda}_i = \lambda_i\, g_i$$

#### 4.5.4 赌注化有效维数

$$D_{stake} \equiv \frac{\left(\sum_i \tilde{\lambda}_i\right)^2}{\sum_i \tilde{\lambda}_i^2} \;\leq\; D_{eff}$$

差值 $\Delta d_{free} = D_{eff} - D_{stake}$：可分辨但未被真实赌注激活的剩余带宽。

#### 4.5.5 三种典型状态

| 状态 | $D_{eff}$ | $D_{stake}$ | $d_{\text{canonical}}$ | 解释 |
|------|-----------|-------------|------------------------|------|
| AI / 低赌注或未绑定系统 | 高 | 低 | ≈ 0 | 判别能力强，真实赌注弱或未绑定；这不是 `no Selection` 判据 |
| “广而浅”关切 | 中 | 中 | 低 | 赌注分布广但每条耦合较浅 |
| “窄而重”关切 | 低 | 低 | 高 | 赌注集中于少数方向但耦合极深 |

#### 4.5.6 与 `_SRT_D_VALUE_CANONICAL.md §2b` 的关系

本节的 $D_{stake}$ 即 §2b 中的 $d_{stakes}$；$s_i$ 对应 §2b 的 $w_i = R_i \cdot A_i \cdot C_i$（$s_i$ 是对三因子乘积的连续化表达，$\varepsilon_s$ 是使乘积进入有效谱的最低门槛）。两套记法等价，本节采用 $s_i / \varepsilon_s / g_i$ 以便于谱计算；§2b 采用 $R_i / A_i / C_i$ 以便于因果拆解。

* **Cross-ref**: `_SRT_D_VALUE_CANONICAL.md §2b`（Def-d-stakes, Def-w_i）; `_SRT_SYMBOL_TABLE.md`（ε_s 条目）; `AI/SRT_AI_01_Ontology.md Ax-ONT-3`（canonical d 定义）。

---

## 5) 编辑规则（避免”多定义冲突”）

- **规则 R1**：不得将局部公式写成“d 的定义是 ……”（除非就是 canonical）。
- **规则 R2**：局部公式必须标注“近似 / 投影 / 操作化”。
- **规则 R3**：涉及跨文件引用时，优先回链到 Ax-ONT-3。
- **规则 R4**：任何”d→0 / d>0”的意识结论，需同时说明与 \(\Psi_f\) 或不可逆风险边界的关系。
- **规则 R5**：若在 Fisher 谱语境下讨论 d，必须区分 `D_eff`（总容量上界）、`D_stake`（赌注化有效维数）与 `d_canonical`（风险梯度主定义）；不得把现有 `\varepsilon_{pg}` 或 `\varepsilon_{reg}` 直接写成 stake 本身；引入 `\varepsilon_s` 时须注明其为方向级有效赌注门槛，而非 stake 本身。

---

## 6) 本轮对齐涉及的主要来源

- `SRT/AI/SRT_AI_01_Ontology.md`（Ax-ONT-3，Canonical）
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`（Def-d-Scale-1，跨尺度功能表征）
- `SRT/Core/SRT_Core_13a_Operator_Basics.md`（认知域近似公式）

---

## 7) 下一步（建议）

- 将本文件在以下入口文档增加引用：
  - `SRT/Core/SRT_Core_00_Intro.md`
  - `SRT/SRT_Glossary.md`
- 在术语表 d 条目中加入“Canonical 优先级”标记。
- 进入 P0-1：补写 `SRT_Core_01_Axioms.md` 的 A7-A13 Part B。

### Formalization Summary (形式化概述)

- 规范主定义：$d(x) \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|$，其中 $\mathcal{U}$ 为效用势，$\mathcal{S}$ 为生存/不可逆风险坐标（Ax-ONT-3）。
- 认知域投影近似：$d_{cog} \approx \alpha A + \beta\log(V_{concern}) + \gamma\tau$，为主定义在行为可观测维度上的降维。
- 全息对应域：$d \propto A_{surface}/l_{Planck}^2$，为主定义的几何对偶表达，非独立定义。
- 所有局部表达须回链至规范定义，并标注"近似/投影/操作化"。

### Mechanism Explanation (机制解释)

- $\hat{G}_\theta$ 的选择强度由 $d$ 值驱动：$d$ 本质上度量算子对生存风险梯度 $\partial\mathcal{U}/\partial\mathcal{S}$ 的敏感度。
- $\Psi_f$（本体论摩擦）是 $d > 0$ 的必要伴随：无不可逆代价的系统缺乏真实关切，$d \to 0$。
- 在不同尺度（量子/生物/宇宙），$d$ 经尺度映射 $\Pi_{scale}$ 实例化为域特异参数（$d_{quantum}$, $d_{bio}$, $d_{cosmic}$），但结构统一于主定义。
- 意识相关判断必须同时考虑 $d > 0$ 与 $\Psi_f$ / 不可逆风险边界关系（规则 R4）。

## 【理论边界/防误用声明】

1. 本文档用于理论解释与建模组织，不应替代独立实证、工程验证或专业判断。
2. 任何公式或命题都依赖操作化定义、测量条件与语境边界，不得脱离边界做绝对化推断。
3. 涉及临床、社会治理、伦理与部署决策时，必须结合风险评估与人类监督机制。
