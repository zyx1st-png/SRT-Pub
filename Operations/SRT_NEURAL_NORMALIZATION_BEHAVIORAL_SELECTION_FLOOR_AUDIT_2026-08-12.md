---
id: SRT-NEURAL-NORMALIZATION-BEHAVIORAL-SELECTION-FLOOR-AUDIT-20260812
type: audit
status: active
claim_mode: governance
updated: 2026-08-12
record_stage: audited_and_landed
layer: meta
epistemic_layer: os
canonical: false
related_files:
  - Core/SRT_Core_13a_Operator_Basics.md
  - Core/SRT_Core_14_Dynamics_Scaling.md
  - Core/SRT_Core_21c_Bridge_Hypotheses.md
  - Neuroscience/SRT_Neural_Mechanisms.md
  - Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
  - Neuroscience/SRT_Neuro_Axioms_Claim_Status.md
---

# 地板审计：神经除法归一化能否推出认知／行为选择

## 0. 文件角色

本文件只审计一个连接：

> 神经候选响应接受除法归一化
> → 系统因此做出一个认知／行为选择。

它不重审 P0 actualisation、神经意识、agency、主体性、d-value 或 `\Psi_f`。它是治理留痕，不是定义源。

## 1. 负担标注

| 判断句 | 标签 | 负担结论 |
|---|---|---|
| “除法归一化把一组神经输入映成相对响应。” | **D + C** | 在公式、候选集合、参数与测量窗已声明时成立 |
| “能量／带宽受限使所有选择动力学必然收敛为除法归一化。” | **S / 未成立** | `H-λE` 未指定 `E`、约束集与动力学，不能唯一推出该函数族 |
| “最大归一化响应就是行为选择。” | **S / 未成立** | 还缺候选身份映射、读出、阈值／累积、任务上下文与执行门 |
| “神经响应可以预测任务中的选择概率。” | **C + P3** | 可检验，但须冻结读出并在 held-out 条件上比较观察分布与 rival 模型 |
| “选择概率与一次实际选择事件相同。” | **S / 不成立** | 概率倾向不是事件发生；实际选择还需事件边界与执行／登记条件 |
| “局部预测成功证明 neural `\hat G` 与行为选择同一。” | **S / 不成立** | 最多建立该任务、候选集与读出下的局部结构相容 |

## 2. 裸句测试

删除“本体必然”“同一选择语法”“神经元投票”等修辞后，可保留的裸句是：

> 在一个具名任务中，神经归一化模型把候选输入映成相对响应。若一个预先声明、在训练集后冻结的读出把这些响应映成行为选择分布，并且该分布在 held-out 条件下满足预先声明的误差界、跟踪具名干预且优于不含归一化的 rival，则该神经模型与该任务的行为选择模型获得局部 P3 相容性。

裸句成立，但不推出机制同一、主体选择、意识或 P0 actualisation。

## 3. 最小 P3 合同：P3-Scale-NB1

### 3.1 对象与映射

对一个具名任务声明：

- `X_N`：神经候选输入空间；
- `N_η : X_N → R_N`：除法归一化模型，`η` 含指数、半饱和项与竞争权重；
- `X_B`：任务级候选／上下文空间；
- `π_X : X_N → X_B`：神经候选与任务选项的身份映射；
- `π_R : R_N → Δ(A)`：冻结的神经响应读出，输出行动集合 `A` 上的概率分布；
- `B_φ : X_B → Δ(A)`：行为层选择模型；
- `D`：预先声明的分布距离或评分规则；
- `ε_NB`：预先声明、相对于测量噪声与基线性能有意义的容差。

局部交换残差为：

\[
\mathcal E_{NB}
=
\sup_{x\in\mathcal T_{test}}
D\!\left(
\pi_R[N_\eta(x)],
B_\phi[\pi_X(x)]
\right).
\]

必须另检验神经读出对观察行为分布的 held-out 预测误差；只让两个可自由拟合的模型彼此接近不构成证据。

### 3.2 防循环门

1. `η` 主要由神经数据估计，不得用同一行为结果同时调参并回报拟合；
2. `π_X`、`π_R`、`D`、`ε_NB`、训练／测试分割与 rival 集合在测试前冻结；
3. 行动集合、任务上下文、时间窗与缺失／拒答规则明确；
4. 若输出是离散事件，另声明阈值、证据累积或采样规则以及运动／执行门；
5. 至少比较一个不依赖除法归一化的 rival，如线性读出、独立累积器或 rank-based 模型；
6. 干预神经归一化参数时，行为层效应必须按预注册方向和幅度窗口变化，并排除感觉可见度、运动能力或总体唤醒等替代解释。

### 3.3 通过与失败

只有同时满足下列条件，才记为该任务上的局部 P3 通过：

1. `\mathcal E_NB ≤ ε_NB`；
2. 神经来源参数在 held-out 行为预测上提供超过最佳 rival 的预声明判别增益；
3. 具名干预的神经变化与行为变化方向相符；
4. 读出无需逐条件任意改写。

以下任一项构成失败或降级：

- 神经归一化显著变化而行为分布不按预测改变；
- rival 在 held-out 数据上相当或更好；
- 只有更换读出／阈值才能逐条件追上行为；
- 相容性只在训练条件成立；
- 候选神经通道与行为选项之间没有稳定身份映射；
- 效应可被感觉输入、运动输出、总体唤醒或任务策略完整解释。

## 4. 反例施压

1. **同响应异选择**：同一归一化响应可被不同阈值、证据累积器、奖励策略或运动门读成不同动作。
2. **异响应同选择**：不同神经模式可经退化读出产生同一行为，单次 choice label 无法反推归一化机制。
3. **共同分母不改排序**：在所有候选共享同一分母的简化模型中，归一化可改变增益而不改变候选排序，因此本身不决定赢家。
4. **目标泛函欠定**：`\mathcal J=H-\lambda E` 若不指定 `E`、约束和动态，可有多种稳态；变分符号不唯一推出除法归一化。
5. **替代理论**：softmax、rank normalization、drift／race accumulator、attention gating 或 learned policy 可解释同类行为背景效应。
6. **下游补偿**：神经归一化受干预后，下游读出可补偿，行为不变；这会否定当前桥，而不否定神经归一化本身存在。

## 5. 判决

广义连接：

```text
neural divisive normalization
-> cognitive / behavioral choice
```

**🔴 软连接。** 相对响应不是离散选择，能量约束也不唯一推出除法归一化。

收窄后的合同：

```text
declared neural normalization + frozen readout + held-out behavior
+ rival comparison + intervention tracking
-> local neural-to-behavioral compatibility                    P3
```

**🟡 条件接口。** 形式上可失败，但尚无一组具名数据、阈值和干预使其转绿。

## 6. 落地范围

- `Core_14 P3-Scale-NB1`：登记首个有界尺度相容实例；
- `Core_13a Ax-Op-03`：保留 neural implementation candidate，删除“任意选择域”泛化，并补行为读出门；
- Neural Mechanisms owner／CompactCore 与 Neuro Axioms bridge：撤销“本体必然／唯一交点／所有选择系统”口径；
- claim-status、registry、status、open tensions、review queue 与 parked trigger 同步；
- 不改 P0/P1，不推进 agency、subjecthood 或 consciousness。

## 7. 主链与支链硬度状态（更新后）

```text
neural inputs -> normalized relative response                  🟡 model-level
normalized response -> task choice probability                 🟡 P3 contract
choice probability -> actual behavioral event                  🔴 without event/readout gate
behavioral prediction -> mechanism identity                    🔴
behavioral event -> agency / subjecthood / consciousness        🔴
```

SRT 十一步主链硬度不因本审计改变；本轮只约束一个 neural-to-behavioral 支链。
