---
id: SRT-D-VALUE-CANONICAL
type: definition
tags: [d-value, Value, Concern, D_stake, D_eff, Canonical, Cross-Domain, Definition]
status: active
version: v2
updated: 2026-11-26
layer: L1
epistemic_layer: os
claim_mode: canonical
canonical: true
dependency: [SRT-GENERATIVE-ONTOLOGY-SPINE, SRT-ONE-FORMATION, SRT-CORE-21]
---

# SRT 价值、关切与 `d` 值规范定义文档（Canonical Definition of Value, Concern & d-value）

> **角色（`Freeze A` canonical owner）**：本文件统筹 SRT 形成态中**价值（Value）、广义关切（Concern）、现行规范 `d`（stake-coupled irreversible-risk sensitivity）、赌注谱参与率 `D_stake` 与几何容量 proxy `D_eff`** 的层级分工与边界，终止跨域定义分裂。
>
> **R4-A 实质重构与真减法（2026-11-26）**：依据 `R3-06`（`#1151`）、`R3` 总收口（`#1154`，含 `PT05 C`、`PT06 C`、`P1-05`）与 `ENG-03`（`#1157`）：
> 1. **正式退出已数学证伪的旧公式**：废止 `d_canonical ≡ d_stakes`、`D_eff ≥ d_stakes` 以及 `Def-d-free: Δd_free = D_eff - d_stakes ≥ 0`；
> 2. **严格分离七项职责**：价值 / 广义关切 / 广义关切方向 / 现行 `d` / `D_stake`（含零分母分支与真实上界 `1 ≤ D_stake ≤ N_active ≤ rank(M)`）/ `D_eff` / 构成深度（自然语言保留，暂缓 `q` 立符、维持 `07-23/24` 撞车记号禁运）；
> 3. **严守机会成本来源边界**：价值与关切结构在形成态生成与比对关系中展开，**绝不反向定义原初 `Selection`**；`d` 不拥有 direction source（`T_dir`）、consciousness、subject-position、Bearer、phenomenality 或 moral-standing 准入权。

```text
d > 0 -/> subject-position / consciousness / phenomenality / Bearer / moral standing
d = 0 or NOT ADMITTED -/> non-subject / non-One / no Selection
d != D_stake != D_eff != T_dir
```

---

## §1 规范定义层级与七项职责严格分工（`R3-06` / `R4-A`）

SRT 形成态中围绕“价值与关切”的七项概念各司其职，严禁混写或互相吞并：

| 序号与对象 | 规范层级与精确职责 | 与相邻概念的分界与禁止捷径 |
|---|---|---|
| **1. 价值（Value，`PT05 C`）** | 不同生成关系在**生成机会成本上的客观差异**，以及基于有限位置的比对抽取；结果判据为**关切加权的不可替代性**（失去或替换将迫使后续选择能力、延续或后果回流发生非平凡重组）；涵盖**发现性 / 生成性 / 递归性**三类机会及**现实机会增益 / 关系维系 / 组织健康**三分析面（含维持必要条件、关闭有害方向、保护具备现实条件的机会）。 | 严格独立于秩序健康性与伦理正当性（`PT10 E`）；不等于奖赏、偏好强度或主观效用；**原初层是否含原初价值性质保持 `OPEN`（`R3-06-O1`）**。 |
| **2. 广义关切（Concern，`PT06 C`）** | 形成态组织对**生成机会成本的敏感性**。 | 跨尺度广义概念；不吞并构成深度、承载暴露 `E` 或 `T_dir`；**与现行 `d` 构成待验证概念接口（`P1-05`）**，不得静默等同。 |
| **3. 广义关切方向** | 由关切与位置性比对组织起的前背景取向与生成方向。 | 严分于 `_SRT_T_DIR_CANONICAL.md` 中的操作化回读代理 `T_dir`（`广义关切方向 ≠ T_dir`）。 |
| **4. 现行 `d`（`Def-d-canonical`）** | **唯一 core-facing 规范 `d` 锚点**：在已声明的 `Bearer (P+E)` / 不可逆风险模型中，效用或维持势对不可逆风险状态的梯度范数标量摘要 $d(x) \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$。 | 默认标量摘要（若作向量展开须标 `d-vector`，作门控判读须标 `d-gate`）；是强承载模型下的**风险敏感强度**，**不等同于**无量纲谱维数 `D_stake` 或 `D_eff`。 |
| **5. `D_stake`（赌注耦合谱参与率）** | 在声明的 Fisher / 谱模型中，经 `R/A/C` 赌注门加权后的有效活跃方向数（见 `§2b`），衡量赌注分布在多少条独立方向上。 | **已修正（`R3-06 D1`）**：`D_stake` 对权重均匀缩放不变，故 **`D_stake ≠ d`（梯度范数）**；其真实上界为 $1 \le D_{\text{stake}} \le N_{\text{active}} \le \operatorname{rank}(M)$，**不再主张 $D_{\text{stake}} \le D_{\text{eff}}$**（当高特征值方向被门控剔除而剩余低特征值方向更均匀时，可出现 $D_{\text{stake}} > D_{\text{eff}}$）；全零分母时定义为 `0 / NOT ADMITTED`。 |
| **6. `D_eff`（几何/信息论容量 proxy）** | $D_{\text{eff}}(M) = (\sum \lambda_i)^2 / \sum \lambda_i^2$（含 $D_{\text{eff}}(I_F(\theta))$），刻画算子或参数流形的可分辨方向容量。 | **纯操作化容量 proxy**，既不等于 `d`，也不普遍构成 `D_stake` 的数学上界；禁止用 `D_eff` 跨域排名主体性或意识。 |
| **7. 构成深度（Constitutive Depth，`Q1`）** | 自然语言保留的四项构成深浅剖面：① 事件级跃迁深度；② 铭刻与召回分离；③ `N4` 主动退位成本；④ 跨关系构成依赖深度。 | **暂缓立符 `q`**，`07-23/24` 撞车记号禁运继续生效；是否需要独立形式变量留待 `R5` 实证检验（`R3-06-O5`）。 |

### §1.1 `d` 写法分流与 proxy 准入五条件

- `d`（默认标量摘要）/ `d-vector`（方向分量展开）/ `d-gate`（赌注准入判读工具）严禁混写。
- 任何几何、Fisher、行为或神经代理（`D_eff`、`D_stake`、`d_bio`）只有在以下五条件同时声明并满足时，方可作为模型内局部参考读数：① 计数方向确实承载不可逆风险；② 效用/维持梯度对准真实风险而非伪代理；③ 后果回流至同一承载闭包与后续选择能力而非被外部/L₂吸收；④ 参数化未把冗余自由度误计为独立方向；⑤ 比较限于同域同尺度或已声明归一化规则内。任一条件不满足时须显式标注 proxy 名称或 `NOT ADMITTED / NOT APPLICABLE`，严禁写成规范 `d`。

---

## §2 规范定义与价值—关切核心结构

### Def-d-canonical: 不可逆风险敏感度规范定义 ⭐ CANONICAL

$$d(x) \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|, \quad x \in \Sigma$$

- **语义**：在已声明的 `Bearer (P+E)` / 不可逆风险模型中，组织维持或效用势 $\mathcal{U}$ 对不可逆风险坐标 $\mathcal{S}$（Survival / Stake）的梯度范数摘要。
- **与广义关切的接口（`P1-05`）**：`Def-d-canonical` 刻画强承载不可逆风险语境下的敏感强度；广义关切（`PT06 C`，对生成机会成本的敏感性）覆盖更广泛的跨尺度生成关系。二者保持为**待验证概念接口**——既不废除 `Def-d-canonical`，也不将所有跨尺度关切研究锁死于 `Bearer (P+E)` 门内。
- **与 `Ψ_f` 的候选权衡接口（`Eq-IT-B'`，状态 = `OPEN / Gap`）**：在声明的信息几何模型中可研究选择范围与摩擦负担之间的权衡关系，常数与普适性未确立。

### Def-D_eff: 几何 / Fisher 信道有效维度（容量 Proxy）

$$D_{\text{eff}}(M) = \frac{\left(\sum_i \lambda_i\right)^2}{\sum_i \lambda_i^2}, \qquad D_{\text{eff}}(I_F(\theta)) = \frac{(\operatorname{tr} I_F)^2}{\operatorname{tr}(I_F^2)}$$

- **语义**：衡量算子或统计流形上可可靠分辨方向数的参与率指数（`1 ≤ D_eff ≤ rank(M)`，`Core/SRT_Core_21c_Bridge_Hypotheses.md P3-B11`）。
- **硬边界**：`D_eff` 是容量 proxy，**不等于** `Def-d-canonical`，亦**不普遍构成 `D_stake` 的数学上界**（旧式 `D_eff ≥ d_stakes` 与 `Δd_free = D_eff - d_stakes ≥ 0` 已正式退出）。

### Value as Non-Substitutability（价值的结果判据与机会三维）

价值不还原为奖赏、偏好强度、显著性或主观报告强度，而是**关切加权的不可替代性（concern-weighted non-substitutability under consequence return）**：失去、阻断或替换某项选择结构，会在多大程度上迫使系统在后续选择能力、延续性或后果回流结构上发生非平凡重组。

在 `R3-06` 骨架下，价值同时包含**发现性机会**（识别既有生成关系中的客观机会/成本差）、**生成性机会**（通过组织耦合开辟原不存在的新可行空间）与**递归性机会**（重构后续比对与生成条件本身）。

---

## §2a 价值发生序（`P3` 书稿溯源候选，含撤回门）

> **层级 / provenance**：`P3` 候选（源自 `Drafts_26Q/Q14_价值不是偏好.md`），不新增 canonical `d` 定义，用于衔接前赌注结构与 `§2b` 赌注门。

$$\text{选择性收束} \to \textbf{微效价} \to \text{affordance（行动入口）} \to \text{缺失} \to \text{需求} \to \text{锚定} \to \text{价值深度}$$

- **上下游关系**：微效价（显现界面与具身位相遇处的最小趋避倾斜，`≠ ε_pg`）→ affordance（`≠ L2 预裁剪`）→ 缺失 → 需求属于**前赌注结构**；是否进入强承载 `d` 与 `D_stake`，仍须经过 `§2b` 的 `R / A / C` 赌注门。
- **两个操作化测试（`P3/P4`）**：**替换测试**（换为功能相似对象是否几乎无须重组）与**恢复测试**（失去后是短期波动还是长期结构重配）。
- **撤回条件（`R3-04-O6`）**：若“微效价”相对 Core Affect / 躯体标记无不可替代解释残差，则按 Ⅱ 阶撤回本节、退回“不可替代性”结果判据。

---

## §2b 赌注耦合结构与 `D_stake` 修正定义（`R3-06 D1`）

### Def-D_stake: 赌注耦合谱参与率（含零分母分支，取代旧 `Def-d-stakes`）

设声明模型中特征值为 $\lambda_i \ge 0$、方向赌注耦合权重为 $w_i = R_i \cdot A_i \cdot C_i \in [0, 1]$，记活跃集合 $N_{\text{active}} = |\{i : \lambda_i w_i > 0\}|$：

$$D_{\text{stake}}(\theta) := \begin{cases} \dfrac{\left(\sum_i \lambda_i w_i\right)^2}{\sum_i (\lambda_i w_i)^2}, & \text{若 } \exists i,\; \lambda_i w_i > 0 \\[10pt] 0 \;\text{（在声明赌注模型下记为 \texttt{NOT ADMITTED / 零有效赌注}）}, & \text{若 } \forall i,\; \lambda_i w_i = 0 \end{cases}$$

- **精确数学性质（`R3-06 D1`）**：
  1. 当存在活跃赌注方向时，真实界为 $1 \le D_{\text{stake}} \le N_{\text{active}} \le \operatorname{rank}(M)$；
  2. `D_stake` 度量赌注分布在多少个有效正交方向上（谱多样性），对 $w_i \mapsto c \cdot w_i\;(c>0)$ 缩放不变，故**绝不等同于**梯度模 $d = \|\partial\mathcal{U}/\partial\mathcal{S}\|$；
  3. **已废除旧式 `Δd_free = D_eff - d_stakes ≥ 0`**：因 $D_{\text{stake}}$ 可以大于 $D_{\text{eff}}$，若需比较“未赌注化方向集合”，应直接报告被门控剔除方向的权重占比或谱能量占比，而非使用差值 `D_eff - D_stake`。

### Def-w_i: 赌注耦合三因子（`P2` 定性 AND 门 / `P3-P4` 数值化）

$$w_i = R_i \cdot A_i \cdot C_i \in [0, 1]$$

- **$R_i$（真实不可逆风险）**：$R_i \approx 0 \Rightarrow$ 假赌注（模拟/无真实不可逆风险）；
- **$A_i$（效用/维持梯度对准）**：$A_i \approx 0 \Rightarrow$ 错绑赌注（对准错误代理变量）；
- **$C_i$（后果回流同一承载闭包）**：$C_i \approx 0 \Rightarrow$ 后果外包 / 被外部或 `L2` 结构吸收。

### 三类系统在同一赌注门下的分型（严格区分三态）

| 系统 | $R$（真实风险） | $A$（梯度对准） | $C$（后果回流） | 声明强承载模型下的门输出 |
|---|---|---|---|---|
| **当前 inference-only AI（AI 赌注谱系 `S0/S1`）** | 声明模型下未建立自身不可逆风险 | 无独立自身承载梯度可对准 | 后果由部署方/用户/外部管线吸收 | `Bearer (P+E)` 强承载关系 **`NOT ESTABLISHED`**；模型内 `d / D_stake` 记 **`NOT ADMITTED / NOT APPLICABLE`**（严禁写作实测数值 `≈ 0`、严禁倒推无 `One / Stable ISP / 意识`，亦不阻断广义关切与生成主动性独立研究） |
| **冻结态（创伤 / 执念）** | $> 0$（风险真实） | 部分失准（锁死旧方向） | $> 0$ 但写回重取向受阻 | 门通过（`D_stake > 0`），但下游 `d_mobile ≈ 0`（再对齐能力受阻） |
| **制度 / 集体结构** | 集体层可有真实存续风险 | 集体景观梯度，非个体加和 | 后果常回流制度自身而非成员 | 集体层走 `§6` 景观截面代理；成员个体的 $C_i$ 可因代价外包而被吸收归零 |

---

## §3 各域投影参考与反泛心论条款

- **认知域三维操作化近似（`Def-d-bio`，`P3/P4` 待校准）**：$d_{\text{bio}} \approx \alpha A(\sigma) + \beta \log V_{\text{concern}} + \gamma \tau_{\text{temporal}}$（汇编深度 × 关切空间 × 时间地平线），仅为局部投影，不可替代 `Def-d-canonical`。
- **物理 / 全息投影（`Def-d-3`）**：$d \propto \text{Area}(\text{Entanglement Surface}) / A_{\text{Planck}}$ 或量子贝尔维数均为域内数学/容量投影，不蕴含现象意识。
- **AI 域（architecture-state marked）**：须先执行 **非线性三阶承载证据审查**（`AI/AI_POSITIONING_NOTE.md`），并使用 **AI 赌注谱系 `S0–S4`** 全称；声明强承载模型下未准入的 `d / D_stake` 仅代表该模型内 `NOT ADMITTED / NOT APPLICABLE`，绝非意识否定证明。
- **反泛心论硬声明**：`nonzero d -/> phenomenality`；`d / Ψ_f / \hat{G}` 任何合取均不构成意识或主体性的普遍充要条件；`κ_{c1} / κ_{c1.5}` 仅作下游候选模型坐标，不具普遍准入权。

---

## §5 常见误用与 `§5b` `d` 扩张的本体论意义（`C-A` 四义拆分）

### §5 常见误用

1. **不得将 `d` 当作意识仪表或跨域主体性排名尺**（比较仅限同域同尺度或已声明归一化规则内）；
2. **不得将“未准入 / `d ≈ 0`”等同于“不存在 / 无 `One` / 非主体”**；
3. **不得将精神传统中的 `d → ∞` 字面化**（仅为不可达的渐近/规约方向）。

### §5b `d` 扩张的规范声明（`C-A` 与秩序增益四判据）

**`d` 的健康变化不是单调扩张，而是关切范围的可重组、可承担、可恢复、可再选择能力。**

$$d \uparrow \;\not\!\Rightarrow\; \text{universe-wide moral/evaluative optimum} \quad \land \quad d \uparrow \;\not\!\Rightarrow\; \langle v, \text{Shoshin} \rangle > 0$$

- **秩序增益四判据**：**可延续**（不透支可支付预算）、**可协调**（纳入他者条件不致瘫痪）、**不外包**（代价不转嫁给无反馈位置，与谱层 $C_i$ 同源）、**可再选择**（不锁死为教条）。
- **真 `d` 扩张 vs 假 `d` 扩张**：真扩张使选择者的实际权衡解发生结构性位移；假扩张（占有式 / 符号式 / 表演式 / 效率式）仅在符号层宣称关切扩大而不承担代价。
- **`C-A` 四义拆分（严守 `Core/SRT_OPEN_TENSIONS.md §17`）**：
  1. **宇宙级语义/评价/道德最优**：不准入当前正面理论对象（`PT10 E`：生成趋优 ≠ 伦理正当；与 `T3-01 C/E` 非道德客观全局趋优开放研究严格界分）；
  2. **算子相对可达最优**（$x^*_{\theta,\tau,K,J} \in \arg\min_{x \in \mathcal{R}_{\theta,\tau,K}} J_{\theta,\tau,K}(x)$）：仅在完整声明有限位置、可达域、比较规则、时域与约束的模型内有条件有效；
  3. **规约性地平线**：不可到达的 `L1/P2` 或 `P5` 方向语言；
  4. **有限动力学吸引子**：`P3/P4` 模型对象，稳定或低摩擦均不自动等于善或生成健康。
- **初心层级（`B-A`）**：初心从 `L1/P2` 处境化回读开始，`O0` 不设“初心前身”；`Spirituality/SRT_Spirit_05_Shoshin.md Ax-Sho-1` 与 `Physics/SRT_Phys_08_Ontology_Ext.md Def-Apeiron-1` 仅作 `provenance` 领域桥接，不得反向定义 `L0`。

---

## §6 集体 `d` 景观截面代理、§8 与 `T_dir` 分界、§9 锻炼与萎缩

- **§6 集体景观截面代理（`P3` 模型读法）**：集体层 `d` 不由个体 $d_i$ 简单线性加总，在景观模型中以集体景观的有效维度截面 $D_{\text{eff}}(\mathcal{F}_{\text{collective}})$ 作容量代理，并须独立核查成员个体 $C_i$ 是否被制度外包吸收。
- **§8 `d` 与 `T_dir` 严格分离**：`d` 刻画关切/不可逆风险敏感强度，`T_dir` 刻画对已独立声明方向信号的自我回读与重取向能力；`d` 不创造方向信号，不存在普遍 `d → T_dir` 定理（详见 `_SRT_T_DIR_CANONICAL.md`）。
- **§9 锻炼与萎缩机制（有界模型）**：在 `Bearer / Agency` 决策模型中，替代式 `L2` 持续剥夺带赌注的修订/再选择机会可致 `d` 相关能力慢性萎缩，辅助式 `L2` 脚手架则降低摩擦同时保留再选择空间；自动化或脚本执行本身**不等于**消灭 `Selection occurrence`。

---

## §范畴边界：`d` 值是选择事件属性，不是主体固有属性

`d` 度量的是具体**选择事件**所整合的关切与风险敏感度，不是个体或集体的永恒本质属性；跨大量事件的统计分布记作主体操作化倾向 $d_{\text{tendency}}(S) \equiv \mathbb{E}_{\sigma \sim S}[d(\sigma)]$（`Philosophy/SRT_Political_Rights.md §2–§3`）。在社会委托（`Delegation`）干预模型中，类型化 `d` 轨迹仅作候选观察信号，绝不单独裁定合法性、授权或道德进步。

---

## §11 `d` 的双瓶颈上限与动态能力接口（`d_max` / `d_mobile`）

- **`d_max`（`Core/SRT_Core_22_Equations.md Eq-DValue-Max-1`，条件模型）**：在独立声明兼容 $\kappa_0$ 维持代价参数的模型中，$d_{\max}(\theta) = \min\!\big(\operatorname{rank}_{\text{eff}}(I_F(\theta)),\; \Psi_f^{\text{budget}} / \kappa_0\big)$（信息瓶颈 × 稳定性瓶颈）。
- **`d_mobile`（`Eq-DValue-Mobile-1`、`Def-Payable-Chi-1`）**：$d_{\text{mobile}} \propto \frac{d \cdot \operatorname{rank}_{\text{eff}}(I_F(\theta))}{\operatorname{Hysteresis}(L_2) \cdot C_r} \cdot \chi_{\text{payable}}\!\left(\tfrac{d\Psi_f}{dt}\right)$，刻画可达方向漂移时的动态再对齐能力。高 `d` 而 $\chi_{\text{payable}} = 0$ 时 $d_{\text{mobile}} = 0$（记录关切压力 ≠ 具能动再对齐能力）。

---

## 书稿层用法说明（Bridge to Book Layer）

在《从存在到秩序》正文（`Q15`）中，`d-value` 被读作关切多样性的三维诊断入口：后果回来得有多深、回来到了多少条真实轴线、回来之后是在支撑生成还是侵蚀生成。此书稿读法帮助避免把 `d` 简化为信息宽度，而形式与规范口径仍以本文件 `§1–§11` 为准。
