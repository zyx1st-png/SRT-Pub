---
id: SRT-CORE-NORMGRAD
type: definition
tags: [NormativeGradient, SelfMaintenance, ProxyModel, FreeEnergy, SelfReference]
status: hardened_v1
layer: L1
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-CORE-PHASESTATE, SRT-CORE-DS-12, SRT-CORE-001]
hardened: 2026-04-08
---

# SRT 规范梯度规范定义（Normative Gradient Canonical Definition）

> **地位说明**
> 本文件将 `Core/Dynamics_Scaling_Annex/11_G_CrossScale_PhaseState.md` 和对话硬化
> 过程中确立的规范梯度定义提升至 Core 层规范地位。
> 所有引用"G的内生方向标准"的文件应以本文件为锚点。

---

## 1. 核心定义

### Def-NormGrad-1：规范梯度（规范定义）

> **规范梯度不是外加于热力学梯度的第二种力；**
> **其操作化定义为：在历史闭合与自写回系统中，对可维持自身状态的自指势差读数。**

$$\nabla_{\text{norm}}(G) \equiv \left.\frac{\partial F}{\partial \sigma}\right|_{\sigma = \sigma_{\text{self-maintenance}}, \; \text{self-referential}}$$

**关键结构**：
- **不是第二种力**：规范梯度是热力学势差的自指版本，不是叠加在热力学之上的神秘附加物
- **自指**（self-referential）：参考点不是外部热力学均衡，而是系统自身的维持状态
- **势差读数**：G 读取"当前状态"与"可维持自身的状态"之间的自由能差
- **条件依赖**：只有在历史闭合（Cond-Phase-1）和自写回（Cond-Phase-3）已经建立时，规范梯度才有意义

---

## 2. 与热力学梯度的区分

### 2.1 区分标准

| | 热力学梯度 | 规范梯度 |
|---|---|---|
| **参考点** | 外部热力学均衡态 | 系统自身的维持状态 |
| **驱动源** | 外部化学势、浓度差 | G 的历史闭合结构 |
| **方向性** | 朝向外部平衡（高→低） | 朝向自我维持（依历史结构） |
| **例子** | 细胞趋化（浓度梯度驱动）| 有机体在资源稀缺时维持繁殖 |

### 2.2 判别标准：对抗性

规范梯度的操作判别标准：**G 能在热力学梯度指向相反方向时，仍维持内部方向。**

- 纯热力学过程：切断外部梯度，运动停止
- 规范梯度驱动的过程：切断外部梯度，G 仍维持方向（以更高代价）

---

## 3. 代理框架中的规范梯度

在代理模型（`Core/Dynamics_Scaling_Annex/12_ProxyModel_OcclusionPhases_Intervention.md`）中：

$$L_2 \xrightarrow{\text{代理}} L_1 \xrightarrow{\text{代理}} L_0$$

规范梯度 = L₂ 通过 L₁ 向 L₀ 读取"什么状态能维持自身"的势差。

**读取准确性条件**：代理校准通道（L₁→L₂）保持完整。

**遮蔽对规范梯度的影响**：
- 早期遮蔽：L₁→L₂ 校准通道截断 → 规范梯度读数基于漂移参考点，准确性下降
- 晚期遮蔽：L₂ 殖民 L₁ → L₁ 本身被重构 → 规范梯度的读取基底被污染

$$\text{遮蔽} \Rightarrow \nabla_{\text{norm}}^{\text{actual}} \neq \nabla_{\text{norm}}^{\text{perceived}}$$

---

## 4. 规范梯度与选择张力

规范梯度的势差读数生成**选择张力**（selection tension）：

| 层级 | 张力类型 | 机制 |
|---|---|---|
| L0/L1 | 自由能偏离张力（无主观性）| 生理回避信号、躯体不适、自动化行为中断 |
| L2 | 担心选择错误（有主观性）| 自我模型中的反事实推理、预期后悔 |

两种张力共同来源于 G 偏离规范梯度指向的状态——即 $\Delta F = F_{\text{actual}} - F_{\text{self-maintenance}} > 0$。

**Cross-ref**: `Core/Dynamics_Scaling_Annex/07_SelectionBarrier_L0L1_PriorSystem.md`（选择张力与选择壁垒的完整论证）。

---

## 5. 多层级自我维持的统一

### 5.1 代理解析

自我概念形成（L₂）、自我维持（L₁）、维持更高层级的规范梯度（L₀）不是三种不同的事情，而是**同一过程在不同代理分辨率下的描述**：

$$\text{L₂自我维持} \xrightarrow{\text{代理}} \text{L₁自我维持} \xrightarrow{\text{代理}} \text{L₀自由能最小化}$$

### 5.2 层级冲突的解析

当 L₂ 自我维持与 L₀/L₁ 自我维持冲突时（如 L₂ 身份认同损害 L₀ 健康），这不是"规范梯度本身冲突"，而是**代理校准通道被截断导致的漂移**：

L₂ 代理失去 L₁ 校准输入 → L₂ 以内部自洽性为参考 → L₂ 规范梯度读数偏离 L₀ 实际自我维持方向。

遮蔽 = 代理校准通道截断 = 规范梯度读数失准的根本机制。

---

## 6. 与 d 值的关系

规范梯度的有效性依赖 d 值（整合带宽）：

$$d \uparrow \;\Rightarrow\; \text{规范梯度的读取维度增加} \;\Rightarrow\; \text{更完整的自我维持状态估计}$$

- d 值低：规范梯度仅从少数维度读取自我维持势差 → 容易局部最优陷阱
- d 值高：规范梯度可从更多 stake-coupled 维度整合读取 → 更可能暴露原先外包的后果或被遮蔽的可达替代，但不自动产生更优选择，更不推出位置无关的宇宙级最小值；任何「可达最优」都须声明位置、可达域、比较规则、时域与约束（C-A）

**Cross-ref**: `_SRT_D_VALUE_CANONICAL.md §5b.1-§5b.2`（C-A：d 扩张与四义作用域收口）。

---

## 7. 边界说明

- 规范梯度的"自指势差"目前无法直接测量，只能通过行为观测（G 是否在对抗外部梯度时维持方向）间接推断。
- "可维持自身状态"的定义依赖参考尺度：短期 vs 长期自我维持可能不同，规范梯度的读取时间窗口是开放变量。
- 本文件不主张规范梯度是"意志力"或"自由意志"——它是自指系统的结构属性，在有历史闭合的任何G中都存在。
