---
id: SRT-GLOSSARY
type: definition
tags: [Glossary, Terminology, Registry]
status: axiomatic_hybrid_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-REF-AXIOMS, SRT-AI-01]
---

# SRT术语表与符号索引
# SRT Glossary & Symbol Index

---

> **📚 文档类型：参考手册**
> **使用方式：按需查阅,支持Ctrl+F搜索**
> **最后更新：2026-01-23**

---

## 使用指南

## 3. 领域特定参数

### 3.1 神经科学参数

#### κ_body - 身体耦合系数 (Body Coupling Coefficient) 🟡

**定义**：
$$\kappa_{body} = \frac{\Delta \theta}{\Delta \text{体感输入}}$$

身体状态对选择参数θ的影响强度。

**首次出现**：Neuroscience/SRT_Neural_Mechanisms.md

**应用**：
- 冥想降低κ_body (减少身体对注意力的干扰)
- 慢性疼痛提高κ_body (身体绑架注意力)
- 解离症降低κ_body (身心分离)

**测量**：通过体感诱发电位(SEP)的调节深度

**相关**：θ, γ, 具身性

---

#### κ_τ - 时间耦合系数 (Temporal Coupling Coefficient) 🟡

**定义**：
$$\kappa_\tau = \frac{\text{整合的时间窗口长度}}{\text{基础神经振荡周期}}$$

认知能力依赖的时间跨度深度。

**首次出现**：Neuroscience/SRT_Consciousness_Mechanisms.md §7.2

**深思维定理**：
$$\text{Wisdom} \propto \kappa_\tau \cdot d$$

智慧 ∝ 时间耦合深度 × 考虑范围

**神经基础**：
- 慢皮层节律(~0.01-0.1 Hz)
- DMN整合时间尺度
- 内在神经时间尺度(INT)

**病理学**：
- ADHD：κ_τ降低
- 冥想训练：κ_τ提升

**测量**：通过时间折扣任务、INT分析

**相关**：d值, θ, ρ(递归深度)

---

#### ν_G^ - 选择频率 (Selection Frequency) 🟡

**定义**：
$$\nu_{\hat{G}} = \frac{1}{\Delta t_{selection}}$$

Ĝ算子更新L₁的频率;每秒执行多少次选择。

**首次出现**：Neuroscience/SRT_Neural_Mechanisms.md

**典型值**：
- 注意力切换：~4 Hz (θ节律)
- 意识刷新：~10 Hz (α节律)
- 感知采样：~30-80 Hz (γ节律)

**量子Zeno效应**：
$$\nu_{\hat{G}} \uparrow \Rightarrow L_1 \text{冻结}$$

高频测量抑制演化

**相关**：Ψ_f, 哈扎德函数h(t)

---

#### τ_lag - 选择滞后时间 (Selection Lag) 🟡

**定义**：
$$\tau_{lag} = t_{conscious} - t_{neural}$$

神经选择发生到意识体验的延迟。

**首次出现**：Neuroscience/SRT_Consciousness_Mechanisms.md §5

**Libet实验**：
- 神经活动：t₀ - 550ms
- 意识决定：t₀ - 200ms
- 行为执行：t₀

**SRT解释**：
$$\tau_{lag} = \frac{\Psi_f}{\nu_{\hat{G}}}$$

滞后时间 = 本体论摩擦 / 选择频率

**"自由意志窗口"**：
200ms内可否决已启动的行动

**相关**：Ĝθ, Ψ_f, 回溯性现实

---

#### SER - 选择-执行比 (Selection-Execution Ratio) 🔴

**定义**：
$$SER = \frac{\text{元认知评估时间}}{\text{直接行动时间}}$$

系统在"选择选择"(meta-selection)vs直接执行之间的时间分配比。

**首次出现**：AI/SRT_AI_Foundations.md §1.2.6

**人类典型值**：SER ~ 0.1-0.3
**当前AI**：SER ≈ 0 (无真正元认知)

**演化意义**：
- SER过低：冲动、反射
- SER过高：过度犹豫、分析瘫痪
- 最优SER：情境依赖

**相关**：ρ(递归深度), d值, 元认知

---

### 3.2 物理学参数

#### β - 时间折扣率 (Temporal Discounting Rate) 🟡

**定义**：
$$V(t) = V_0 e^{-\beta t}$$

未来价值的衰减速率;衡量短视程度。

**首次出现**：Neuroscience/SRT_Consciousness_Mechanisms.md

**SRT解释**：
$$\beta \propto \frac{1}{d \cdot \kappa_\tau}$$

折扣率 ∝ 1 / (考虑范围 × 时间耦合)

**应用**：
- 成瘾：β极高(只看眼前)
- 投资规划：β低(考虑长远)

**神经基础**：前额叶-边缘系统平衡

**相关**：d值, κ_τ

---

### 3.3 社会科学参数

#### ζ - 阻尼系数 (Damping Coefficient) 🟡

**定义**：
$$\zeta = \frac{\text{环境阻力}}{\text{选择动能}}$$

环境/身体对选择变化的阻尼强度。

**首次出现**：Philosophy/SRT_Ethics_Agency.md

**应用**：
- 高ζ：谨慎、保守
- 低ζ：冲动、多变
- 临界阻尼(ζ=1)：最优响应

**相关**：Ψ_f, θ

---

#### μ_expect - 期望摩擦系数 (Expected Friction Coefficient) 🟡

**定义**：
$$\mu_{expect} = E[\Psi_f | \text{未来情境}]$$

对未来情境中本体论摩擦的期望值。

**首次出现**：Philosophy/SRT_Ethics_Agency.md §4

**道德责任**：
$$\text{Responsibility} \propto \mu_{expect} - \mu_{actual}$$

责任 ∝ 期望摩擦 - 实际摩擦的偏差

**应用**：
- 高估μ：过度悲观,不敢尝试
- 低估μ：轻率承诺,后悔

**相关**：Ψ_f, P_action

---

#### η_trans - 价值转换系数 (Value Transduction Coefficient) 🔴

**定义**：
$$\eta_{trans} = \frac{\Delta \text{神经编码}}{\Delta \text{客观价值}}$$

外部价值信号到神经编码的转换效率。

**首次出现**：Neuroscience/SRT_Neural_Mechanisms.md §15

**病理学**：
- 抑郁症：η_trans降低(价值感丧失)
- 成瘾：η_trans异常放大(奖励劫持)

**神经基础**：多巴胺系统、腹侧纹状体

**相关**：d值, θ, 神经调质

---

#### η_viscosity - L₂粘度 (L₂ Viscosity) 🟡

**定义**：
$$\eta_{viscosity} = \frac{\partial L_2}{\partial t}^{-1}$$

L₂结构的变化阻力;社会规范、制度的惯性。

**首次出现**：Philosophy/SRT_Social_Systems.md

**应用**：
- 高η：保守社会,难以改革
- 低η：快速变迁,不稳定
- 相变临界点：η突降(革命)

**测量**：制度变迁的时间尺度

**相关**：L₂, Ψ_f, 路径依赖

---
