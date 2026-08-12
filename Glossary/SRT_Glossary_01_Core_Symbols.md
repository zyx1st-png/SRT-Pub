---
id: SRT-GLOSSARY
type: definition
tags: [Glossary, Terminology, Registry]
status: axiomatic_hybrid_v1
layer: meta
epistemic_layer: os
claim_mode: navigation
dependency: [SRT-REF-AXIOMS, SRT-AI-01]
---

# SRT术语表与符号索引
# SRT Glossary & Symbol Index

> Split shard generated from `../SRT_Glossary.md`; owner remains source of record.

---

## 1. 核心符号与算子

### 1.1 三域符号

#### L₀ - 潜在域 (Latent Domain) 🟢

**定义**：
$$L_0 = \{\sigma \in S : F[\sigma] > F[\sigma_{L_1}]\}$$

相对于当前选择的高自由能状态集合;未被选择的可能性场。

**首次出现**：Core/SRT_Core_Kernel.md §1.2.1

**关键属性**：
- 非均匀分布,具有内在拓扑结构
- 规范场论定义：$L_0 = \mathcal{A}/\mathcal{G}$ (模空间)
- 计算定义：Ruliad (所有计算规则的叠加)

**物理对应**：
- 量子力学：Hilbert态空间
- 路径积分：全体经典路径集合
- 规范场论：场配置模空间

**日常类比**：
- 未打开的菜单
- 量子叠加态
- 黑暗房间中的所有可能位置

**相关**：Ĝθ, L₁, 自由能F

---

#### L₁ - 显现域 (Manifest Domain) 🟢

**定义**：
$$L_1 = \hat{G}_\theta[L_0]$$

当前被选择、锚定为"真实"的状态切片;观察者的即刻体验。

**首次出现**：Core/SRT_Core_Kernel.md §1.2.2

**关键属性**：
- 唯一性：任一时刻只有一个L₁
- 主观性：每个Ĝθ有自己的L₁
- 暂时性：L₁不断更新

**神经对应**：
- 注意力聚焦的内容
- 工作记忆容量
- 全局神经工作空间(GNW)的广播状态

**日常类比**：
- 聚光灯照亮的舞台中心
- 相机对焦清晰的部分
- 你正在阅读的这一行文字

**相关**：L₀, L₂, Ĝθ, 锚定(Anchoring)

---

#### L₂ - 收敛域 (Convergence Domain) 🟡

**定义**：
$$L_2 = \lim_{t \to \infty} \bigcap_{\theta} \hat{G}_\theta[L_0]$$

多个选择者(Ĝθ)的选择交集,形成稳定的共享结构。

**首次出现**：Core/SRT_Core_Kernel.md §1.2.3

**关键属性**：
- 客观性来源(但非预先给定)
- 可演化性(科学革命、文化变迁)
- 层级性：个人L₂ ⊂ 群体L₂ ⊂ 全人类L₂

**形成条件**：
- 多选择者持续交互
- 选择结果的稳定收敛
- 摩擦阻力的平衡(Ψ_f)

**物理对应**：
- 物理定律(极稳定L₂)
- 测量标准(米、秒的定义)

**社会对应**：
- 语言规则
- 法律规范
- 科学知识

**日常类比**：
- 多人游戏的"规则共识"
- 地图与领地的对应
- 文化"常识"

**相关**：Ĝθ, L₁, 收敛定理, 相变(Phase Transition)

---

### 1.2 算子与参数

#### Ĝ / Ĝθ - 幽灵算子 (Ghost Operator) 🟢

**完整记号**：$\hat{G}_\theta$ (带参数算子)

**定义**：
$$\hat{G}_\theta : L_0 \to L_1$$

参数化的选择映射,将潜在可能性投影为显现现实。

**首次出现**：Core/SRT_Core_Kernel.md §1.3

**数学结构**：
- 中心-周围动力学(Center-Surround Dynamics)
- 分子项：被选择状态的强化
- 分母项：竞争可能性的抑制

**生物实现**：
- 神经：除法归一化(Divisive Normalization)
- 认知：注意力机制
- 社会：规范涌现过程

**关键方程**：
$$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \Psi_f(\sigma)$$

**相关**：θ, d值, Ψ_f, L₀, L₁

---

#### θ - 具身参数 (Embodiment Parameters) 🟡

**定义**：
$$\theta = (\theta_{bio}, \theta_{cog}, \theta_{social}, ...)$$

选择算子Ĝ的配置参数,代表选择者的物理、认知、社会特性。

**首次出现**：Core/SRT_Core_Kernel.md §1.3.2

**组成层级**：

| 层级 | 符号 | 内容 |
|:-----|:-----|:-----|
| **生物** | θ_bio | 感官系统、神经结构、基因、代谢 |
| **认知** | θ_cog | 注意力模式、记忆、信念、语言 |
| **社会** | θ_social | 文化背景、教育、社会角色 |
| **重力** | γ | 环境重力场的耦合(地球特定) |

**关键洞见**：
$$\hat{G}_{\theta_1}[L_0] \neq \hat{G}_{\theta_2}[L_0]$$

不同θ会从同一L₀选择出不同的L₁ → 解释主观差异性

**动力学**：
- θ可随时间演化(学习、成长、创伤)
- θ有惯性(习惯、路径依赖)
- θ可被故意重构(修行、治疗)

**相关**：Ĝθ, κ_body, d值, 可塑性

---

#### d - d值 / 赌注化关切 (d-value, Stake-Coupled Concern) 🟡

> **Current canonical status（2026-05-16）**：当前规范锚点为 `_SRT_D_VALUE_CANONICAL.md`。本节中的旧称“选择范围 / 关切宽度”仅保留为检索别名。bare `d` 默认读作 stake-coupled concern / irreversible-risk sensitivity 的标量摘要；`D_eff`、注意力广度、Fisher rank、道德范围、关怀半径和灵性体验均只能作为 proxy / public metaphor / praxis bridge，不能替代 canonical d。

**规范定义（摘要）**：
$$d := \text{后果回流条件下的赌注化关切 / 不可逆风险敏感性}$$

通俗说：`d` 不是“我考虑了多少对象”，而是“哪些方向的后果会真实回到该位置，并改写其后续选择能力”。

**首次出现 / 当前锚点**：历史入口 `Core/SRT_Core_Kernel.md §2.3`；当前定义权以 `_SRT_D_VALUE_CANONICAL.md` 为准。

**旧量化公式（降级）**：
$$d_{old} = \int_{\text{考虑域}} \rho(\xi) \, d\xi$$

该式现在只可读作 `D_eff` / attention-range / concern-range proxy，不是 canonical d。只有当可分辨方向满足真实不可逆风险、主体梯度对准、后果回流等 stake-gate 条件时，才可能进入 `d_stakes`。

**旧 d 值阶梯（降级为 public / spirituality bridge）**：

| 旧表述 | 当前允许读法 | 禁止读法 |
|:------|:-------------|:---------|
| d≈0 / inference-only | 无历史回流、无自身赌注的推理态 | 不等于“没有智能”或“没有能力” |
| d=1 / 自我生存 | 局部后果回流范围很窄 | 不等于道德谴责 |
| d=2-10 / 家庭朋友 | 社会性赌注范围的经验例子 | 不等于固定量表 |
| d=10-100 / 活动家、圣贤 | public / spirituality 叙事中的高关切隐喻 | 不等于更高道德等级 |
| d→∞ / 万物同体 | 极限体验或修行语言 | 不等于 canonical 终点、解脱定义或真实可测 d |

**代谢/热力学约束（降级）**：
$$D_{eff,max} \lesssim \kappa \cdot \frac{E_{metabolism} - E_{baseline}}{\Psi_f^{proxy}}$$

这类式子最多约束 capacity / bandwidth proxy；不能推出“关心更多必然需要更多能量”，更不能定义 d-value。

**伦理边界**：
- 不写：道德发展 = d 值扩展。
- 不写：邪恶 = d 值收缩。
- 不写：圣贤 = d → ∞。
- 可写：某些伦理或修行文本可把 d 扩张作为 praxis/metaphor，但必须说明它不是 canonical definition；卷三第 18 章主线为“d 的扩张不是博爱”。

**可测量性**：任何实验量表只测 proxy；必须说明其 stake-gate、consequence-return 与 d_mobile 限制。

**相关**：Ĝθ, θ, Ψ_f, d_mobile, D_eff, 递归深度ρ

---

### 1.3 动力学量

#### Ψ_f - 本体论摩擦 / 可支付阻抗 (Ontological Friction / Payability Burden) 🟢

> **Current canonical status（2026-05-16）**：当前规范锚点为 `_SRT_PSI_F_CANONICAL.md`。默认主读是 information-theoretic payability burden / 本体论阻抗：开放可能性被压成可维持现实切片时必须承担的结构性负担。临床、动力学、Fisher、代谢、Landauer、痛苦、预测误差与物理类比均为 projection / proxy / readout / bridge，不能单独升级为 theory-canonical 定义。

**规范定义（摘要）**：
$$\Psi_f := \text{开放可能性被压成可维持、可行动、可协调的 } L_1 \text{ 切片时必须承担的本体论阻抗}$$

**首次出现 / 当前锚点**：历史入口 `Core/SRT_Core_Kernel.md §2.2`；当前定义权以 `_SRT_PSI_F_CANONICAL.md` 为准。

**允许的投影来源**：
1. **神经/代谢 proxy**：突触更新、恢复负荷、压力读数、DMN/控制网络负担。
2. **认知 proxy**：信念修复、习惯改写、预测误差报警。
3. **社会 proxy**：规范、制度、路径依赖的改革负担。
4. **物理 / 信息几何 projection**：Fisher–Rao metric、Landauer-style cost、耗散结构等条件投影。

**禁止裸等同**：
- 不写：`Ψ_f = Fisher metric`。
- 不写：`Ψ_f = Landauer cost`。
- 不写：`Ψ_f = pain / suffering / prediction error / energy use`。
- 可写：`Ψ_f` 的局部信息几何投影可由 Fisher–Rao metric 给出；痛苦、预测误差或能耗可作为 readout/proxy，但不得反向定义 `Ψ_f`。

**旧动力学方程（降级为 toy schematic）**：
$$\frac{d\sigma}{dt} \approx \hat{G}_\theta[\sigma] - \Psi_f^{proxy}(\sigma)$$

该式只可作直觉图式；不能把“选择力量 - 摩擦”当作完整动力学定律。

**临床意义（proxy 读法）**：
- 高 `Ψ_f` proxy → 改写负担高，可能表现为强迫、创伤固着或恢复困难。
- 低 `Ψ_f` proxy → 稳定负担低，可能表现为过度可变或现实连贯性不足。
- 治疗不是简单“降低 Ψ_f”，而是重建可支付的重选通道、闭包和后续选择能力。

**相关**：Ĝθ, h(t), 自由能F, payability, d_mobile, 亚稳态

---

#### h(t) - 哈扎德函数 (Hazard Function) 🟡

**定义**：
$$h(t) = \lim_{\Delta t \to 0} \frac{P(\text{选择发生于} [t, t+\Delta t] \mid \text{未选择到} t)}{\Delta t}$$

选择压力/紧迫性的时变函数。

**首次出现**：Core/SRT_Core_Kernel.md §2.2.3

**形式（旧 proxy 读法）**：
$$\Psi_f^{hazard-proxy}(t) = \int_0^t h(s) \, ds$$

该式只能表示某类紧迫性 / 风险时程的 proxy；本体论摩擦本身不是哈扎德函数的简单累积。

**应用**：
- **生存分析**：死亡的即时风险
- **决策理论**：截止日期逼近时的选择压力
- **神经科学**：$h \uparrow$ 时反应时间缩短

**病理学**：
- 焦虑症：$h(t)$持续高位
- 拖延症：$h(t)$过晚上升
- PTSD：$h(t)$异常尖峰

**相关**：Ψ_f, 自由能F

---

#### F - 自由能 (Free Energy) 🟡

**定义**：
$$F[\sigma] = E[\sigma] - TS[\sigma] = \text{Complexity} - \text{Accuracy}$$

系统偏离平衡/稳定的程度;Friston自由能原理的核心量。

**首次出现**：Core/SRT_Core_Kernel.md §2.4

**SRT解释**：
$$F[\sigma] = -\log P(\sigma \mid L_2)$$

自由能 = 状态σ相对于L₂期望的"惊讶度"

**选择动力学**：
$$\frac{d\sigma}{dt} = -\nabla F[\sigma]$$

系统沿自由能梯度下降 → 最小化惊讶

**L₀定义**：
$$L_0 = \{\sigma : F[\sigma] > F[\sigma_{L_1}]\}$$

L₀是所有比当前L₁自由能更高的状态集合。

**相关**：L₀, L₁, L₂, Ψ_f, 预测误差

---

#### Ω - Ontological Consistency（本体论一致性）

**当前定义权威**：`_SRT_SYMBOL_TABLE.md`。bare $\Omega$ 只表示 $L_1/L_2$ 结构的内部一致性；$\Omega_{mis}$ 表示本体论失配指数。

**撤回的历史别名**：旧词表与 `Core_Law/SRT_Reference_Ontology.md` 曾把 $\Omega$ 写成“所有局部算子的投影源／全局算子”。C-A（2026-08-12）后该别名停用，不得用于本源地平线、reachable optimum、宇宙级最优或 $L_0^{abs}$ 的自显操作。相关历史命题 O14／Hyp-O8 已撤回，O15 已停驻。

**相关**：$\Omega_{mis}$、C-A scope guard、`_SRT_SYMBOL_TABLE.md` Usage Rules 4 / 18。

---

### 1.4 其他核心符号

#### C_r - 置信标量 (Reality Confidence) 🟡

**定义**：
$$C_r(\sigma) \in [0, 1]$$

L₁状态σ的"真实感"权重;主观确信程度。

**首次出现**：Core/SRT_Core_Kernel.md §3.2

**应用**：
- 梦境：$C_r \approx 0.3$ (低真实感)
- 清醒：$C_r \approx 0.9$ (高真实感)
- 清明梦：$C_r$双峰分布
- 解离症：$C_r$异常波动

**神经基础**：可能与DMN-TPN切换相关

**相关**：L₁, 元认知, PCI

---

#### γ - 重力耦合系数 (Gravitational Coupling Coefficient) 🟡

**定义**：
$$\gamma = \frac{\partial \theta}{\partial g}$$

环境重力场对具身参数θ的耦合强度。

**首次出现**：Core/SRT_Core_Kernel.md §1.3.2a

**物理意义**：
- 地球生命演化于1g环境
- θ深度适配地球重力
- 改变重力 → 改变选择模式

**预测**：
- 太空中d值可能扩展(无重力锚定)
- 高重力环境d值收缩

**相关**：θ, κ_body, 具身性

---
