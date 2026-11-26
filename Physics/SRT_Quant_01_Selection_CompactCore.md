---
id: SRT-QUANT-01-COMPACT-CORE
type: core_module
tags: [Quantum, Selection, Measurement, RelativePosition, Compact Core]
status: active
version: v2
layer: L1
epistemic_layer: os
claim_mode: translation
canonical: false
updated: 2026-11-26
dependency: [SRT-PHYSICS-COMPACT-REGISTRY, SRT-QUANT-01, SRT-PHYS-BRIDGE, SRT-GENERATIVE-ONTOLOGY-SPINE]
---

# SRT Quantum Mechanics: Selection & Measurement — Compact Core

> **定位**：本文件是 `SRT_Quant_01_Selection.md` 的紧凑主干版（已随 `R4-C2` 校准）。  
> **用途**：用于快速把握 SRT 对量子测量、有限相对位置接口（`QRF / RQM / REP01`）、`PHR-A` 事件审计与非定域性的最短论证骨架。  
> **关系**：不替代原文；原文保留详细量子诠释整合、概率流假说与实验讨论。
>
> **PHR-A & `R4-C2` 护栏（2026-11-26）**：量子测量采用 interpretation-plural P3/P4 event audit。`\hat G_\theta` 仅是形成态/模型级形式角色载体，不是原初 `Selection` 或先在主体；POVM 条件态不等于结果已发生；退相干、耗散、固定点或稳定记录中的任一项都不充分；遵守 `REP01` 表征协变护栏，且物理相对位置不等于 `One` 或意识。

## 1. 核心问题

这篇处理的是 SRT 在量子层面的最关键问题：

> **哪些物理证据允许我们把一个过程登记为 AM-A 的 physical realisation candidate？**

SRT 的压缩回答是：
- 先声明模型、事件单元、系统边界与量子诠释
- 再检验 outcome-indexed record、路径效力与历史效力
- collapse-family、Everett 与 operational 口径共享审计，不共享一个已证的全局坍缩机制

---

## 2. 量子测量即选择

### 2.1 Quantum Selection Operator
\[
\hat{G}_\theta: \mathcal{H} \to \mathcal{P}(\mathcal{H})
\]

SRT 把量子 instrument 读作：
- 候选结果、概率与条件态的形式载体
- PHR-A 事件审计的一个输入，而不是结果发生的充分证明

在密度矩阵表达下：
\[
p_k=\text{Tr}(M_k \rho M_k^\dagger),\qquad \rho_k=\frac{M_k \rho M_k^\dagger}{p_k}
\]

最压缩句子：
> **`\hat G_\theta` 标记转化角色；POVM 给出条件更新；物理发生还需要 outcome record、路径效力与历史效力。**
>
> **Cost boundary**: Generalized Second Law、Landauer cost、耗散或 `\Psi_f` proxy 可以约束实现和记录稳定化；它们不说明“谁在取值”，也不造成 primitive actualisation。

### 2.2 Bounded Physical Realisation Audit
PHR-A 使用四项有界审计：
- 真实进入过程的非等价候选
- outcome-indexed physical record
- 可干预的 downstream path efficacy
- 未来可达性、概率、门槛或返回成本改变

压缩含义：
> **审计不需要意识，但通过审计也不证明主体或意识。**

### 2.3 Physical Measurement Interface & Relative Position（`QRF / RQM` 对接）
历史符号 `\hat{G}_{proxy}` 只允许表示把候选差异耦合到记录通道的 physical measurement interface（对应跨尺度五机制中无主体物理中介，严分于具主体与规范条件的 `Delegation`）。装置、参考系（`E02 QRF`）与交互边界（`\theta_{basis}, \theta_{boundary}, \theta_{H_{int}}`）共同构成物理有限相对位置并可形成测量记录；这不把装置升级为 `One`、proxy subject、agent 或 conscious observer。

---

## 3. 比特生成与发生/持续分离（`EX-A` 校准）

### 3.1 Wheeler-SRT Bit Generation（P3 类比，区分发生与累积）
\[
\text{Retained Content}_M(\Omega)=\int H_M(\hat{G}_\theta[\Psi])\,dt \quad \text{(declared model } M\text{)}
\]

SRT 对 Wheeler 的结构性补充：
> **It from Bit 聚焦可编码比特，SRT 进一步追问比特差异如何经由有限位置实际化与记录留存而形成。**

遵循 `EX-A`（`OPEN_TENSIONS §15`）：单次原初实际化不等于持久实体（`occurrence != persistence != One`）；宏观物理对象的“硬度”对应闭合记录的冗余稳定化（`P07`）与低边际读出摩擦。

---

## 4. 概率流偏置假说与物理闭合边界（`P4` 探索假说 · `R3-03-O6` 护栏）

### 4.1 Probabilistic Bias Hypothesis（`P4` Speculative Bridge，非规范结论）
\[
P_{obs}(x)=P_{Born}(x)+\delta_\theta(x),\qquad \int \delta_\theta\,dx = 0
\]

**`R4-C2` 严格边界**：
- 上式是针对“若具身系统在微观窗口存在统计偏置而不引入新力”的 **P4 探索性可证伪假说**（具体实验证伪窗口见 `Extensions/SRT_Phys_E05_Falsifiability_Program.md`），**不是 SRT 规范理论前提，亦不宣称已观测到玻恩规则偏离**；
- SRT 的物理因果兼容主张（`R3-03-O6`、`Philosophy/SRT_Causality_Time.md §1.4`）**不依赖**违反玻恩规则或引入宏观超自然效应——高层约束主要通过物理闭合内的边界条件与耦合拓扑（`T-Phys-5` $\mathcal{C}_{down}^{macro} \subseteq \Pi_{kernel}$）运作；
- 宏观尺度下由于环境退相干与多体耦合，任何假定微观偏置项均指数衰减（`e^{-N/N_{coherence}}`），严格排除宏观“心物超能力”宣称。

---

## 5. 纠缠、非定域性与表征协变（`REP01` 校准）

### 5.1 Entanglement as Pre-Factorized Relational Structure
\[
\text{Entanglement}(A,B) \iff \text{non-factorizable joint state in } \pi_{\text{phys}}(L_0)
\]

纠缠在 SRT 中不是“超距神秘连接”，而是：
> **在所声明的物理投影下，联合系统尚未被局域边界与交互记录分解为相互独立的局域子系统。**

同时遵守 **`REP01` 表征协变护栏**（`Physics/patches/SRT_Phys_REP01_Representation_Covariance_and_Composition_Guard_v0_1.md`）：实/复数域 Hilbert 空间与配置空间 $\mathbb{R}^{3N}$ 皆为可替换的形式脚手架，真正承重的是在等价表征变换下保持不变的操作、组合、概率与读出结构包；严禁把 $\mathcal{H}$ 或 $\mathbb{R}^{3N}$ 直接等同于 `L_0^{abs}`。

---

## 6. 退相干的必要性与不完备性

SRT 对退相干的最关键判断是：

> **退相干可以支持相干抑制与记录稳定化，但单独不能裁决全局坍缩、branch-relative fact formation 与 operational update。**

PHR-A 不再用 `\hat G_\theta` 填补一个“最终决定机制”。它要求实际审计 outcome record 是否获得路径效力与历史效力，并把本体读法交给已声明的诠释。

---

## 7. 采样率与时间接口边界（对齐 `Causality_Time §2.2`）

### 7.1 Operational Sampling Window（模型内体验/观测窗口代理）
\[
t_\Psi \approx \frac{1}{\nu_{neural}}
\]

该关系仅刻画有限具身/仪器接口的积分与采样时间窗（对应七项时间接口中的体验/仪器观测窗口 `t_{exp}` / `t_{instrument}`），**不推出普朗克物理时间离散化定理**（`H-Phys-2` 保持独立假说，`E04` Page–Wootters 关系时间并行保留）。

---

## 8. 诠释综合与双向反馈

SRT 在量子测量层整合：
- **RQM / QRF** 的位置与参考系相对性（为 SRT 原初分化与有限相对位置提供硬物理抽象来源）；
- **QBism** 的有限代理更新视角（去主体化后仅在具主体层适用）；
- **Wheeler** 的参与性信息记录；
- **退相干 / 量子达尔文主义** 的环境稳定化机制。

其最压缩兼容句是：
> **物理测量描述必须固定位置、边界、interaction 与 record channel；这些条件定义审计位置，不构成一个先在主体，亦受 `REP01` 表征协变与 `PHR-A` 多诠释审计约束。**

---

## 9. 最压缩结论

`Quant 01` 校准后可以压缩成五句话：

1. **量子 instrument 的概率和条件态不自动等于结果已发生；`PHR-A` 需 outcome record、路径效力与历史效力，不要求意识。**
2. **装置、参考系（QRF）与交互边界定义物理有限相对位置，不构成 `One`、主体或规范 `Delegation`。**
3. **单次发生不等于持久实体（`EX-A`）；物理对象的稳定来自闭合记录累积与低边际读出摩擦。**
4. **任何微观概率流偏置均属可证伪 P4 探索假说，SRT 物理闭合兼容（`R3-03-O6`）不依赖违反玻恩规则或引入新力。**
5. **纠缠反映联合态未局域分解，且一切数学表征均遵守 `REP01` 协变护栏，不得等同于 `L_0^{abs}`。**

---

## 10. 阅读路径

- 全量原文：`SRT_Quant_01_Selection.md`
- split 导航：`Selection_Split/README.md`
- REP01 协变护栏：`patches/SRT_Phys_REP01_Representation_Covariance_and_Composition_Guard_v0_1.md`
- 量子仪器与 QRF 桥：`Extensions/SRT_Phys_E01_Quantum_Instrument_Bridge.md`、`Extensions/SRT_Phys_E02_Quantum_Reference_Frames_Bridge.md`
- Physics compact registry：`PHYSICS_COMPACT_REGISTRY.md`
- Physics bridge：`_SRT_Phys_Bridge.md`
- Cosmology compact core：`SRT_Physics_Cosmology_CompactCore.md`
- canonical 总注册表：`../CANONICAL_REGISTRY.md`
