---
id: SRT-EQ-HYP-MAP
type: framework
tags: [Mapping, Equations, Hypotheses, Falsification]
status: axiomatic_hybrid_v1
dependency: [SRT-CORE-22, SRT-EXP-CORE]
---

# SRT 方程-假设映射表（Eq ↔ Hypothesis）

> 目的：将 `Core/SRT_Core_22_Equations.md` 与 `Core/SRT_Experimental_Core.md` 的证伪路径对齐，形成可执行实验接口。  
> 版本：P1-2 初版（可持续补全）。

---

## A. 映射规则

1. `Eq-ID` 对应核心动力学/约束方程。  
2. `Hypothesis-ID` 对应实验核心中的可证伪条目（H#/Ax-Exp-*）。  
3. `Bridge` 说明从方程到实验指标的中间变量。  
4. `Status`：`Mapped | Partial | Gap`。

---

## B. 主映射矩阵（v1）

| Eq-ID (Core22) | 语义 | Hypothesis-ID (ExpCore) | Bridge / 可观测量 | Status |
|---|---|---|---|---|
| Eq-Evo-01 | 幽灵演化主方程 | Ax-Exp-01 / H6 | 行为预测残差、具身变量增益（ΔR²） | Mapped |
| Eq-Evo-01b | 代谢增益调制 | Ax-Exp-01 | 代谢应激(血糖/乳酸/HRV) × 任务性能下降斜率 | Partial |
| Eq-Evo-02 | θ 慢变量更新 | H7 | 个体归一化参数与 d-value 纵向变化 | Mapped |
| Eq-Evo-02b | θ 张量惯性 | H7 | 信念网络中心性 vs 干预后更新速度 | Partial |
| Eq-Evo-03 | 快慢耦合系统 | H7 / H6 | 神经快变量(EEG) + 行为慢变量(学习曲线)耦合拟合 | Partial |
| Eq-Force-01 | 本体论摩擦 Ψ_f | H72 (情态力学) | 语言情态比 μ_sem 与摩擦代理相关 | Mapped |
| Eq-Pain-01 | 痛苦≈dΨ_f/dt | H72 | 痛苦评分变化率与 μ_sem、生理唤醒同步 | Partial |
| Eq-Select-Thermo | 选择热力学宪法不等式 | H1 / H6 | 秩序参数 dq/dt 与能耗、噪声熵预算 | Gap |
| Eq-Stab-01 | 固定点稳定条件 | H6 | 扰动恢复时间、吸引域回归概率 | Partial |
| Eq-Phase-01 | 本体论相变阈值 | H6 | 信息量 I 超阈值 τ 的跃迁曲线拟合 | Partial |
| Eq-Sleep-01 | 睡眠 L2 优化 | H7 | 睡眠前后模型复杂度/误差压缩 | Partial |
| Eq-LDP-01 | 水动力极限 | H6 | 群体行为密度场/迁移流拟合 | Gap |
| Eq-LDP-02 | SRT 作用量泛函 | H6 | 路径概率对 I_SRT 的指数衰减检验 | Gap |
| Eq-Phantom-01 | 社会幻肢痛 | H72 | 关系丧失后语言-情绪耦合摩擦轨迹 | Partial |
| Eq-Phantom-02 | 稳态重建时间常数 | H7 / H72 | 可塑性指标 vs 恢复时间 τ_rebuild | Partial |

---

## C. 优先补洞（Gap Backlog）

### G1 — Eq-Select-Thermo ↔ H1/H6（秩序参数 q(L₁) 代理方案）

**缺口根因**：`Eq-Select-Thermo` 中的 $q(L_1)$（L₁ 层秩序参数）需要一个能在行为/神经/社会实验中直接测量的代理量，目前尚无统一标准。

**解决方案：三代理并行（P1 协议）**

| 代理 | 操作定义 | 测量方法 | 数据类型 |
|-----|---------|---------|---------|
| **代理 G1-A**：网络互信息密度 | $q^{(A)} = I(X_{net}) / H(X_{net})$，节点间平均互信息 / 总熵 | fMRI 功能连接矩阵；社交网络边权矩阵 | 神经/社会 |
| **代理 G1-B**：行为可压缩率 | $q^{(B)} = 1 - L_{MDL}(\text{Behavior}) / L_{random}$，最短描述长度比 | 行为序列 MDL 编码（基于 Lempel–Ziv） | 行为 |
| **代理 G1-C**：任务稳态成功率 | $q^{(C)} = \bar{r}_{steady-state}$，训练稳定后的任务成功率均值 | 认知任务学习曲线尾段 | 认知 |

**收敛效度检验**：三代理在独立样本上相关系数 $r > 0.5$ 则认为 $q(L_1)$ 被充分操作化。

**Eq-Select-Thermo 的证伪条件**：若 $dq^{(A,B,C)}/dt$ 与能量预算（血糖、HRV、代谢率）和噪声熵（EEG 高频功率）的线性组合**不**满足宪法不等式方向，则 Eq-Select-Thermo 需修订。

**Status 更新**：Gap → Partial（三代理方案已设计，待实验验证）

---

### G2 — Eq-LDP-01 / Eq-LDP-02 ↔ H6（群体尺度数据管线）

**缺口根因**：`Eq-LDP-01`（水动力极限）和 `Eq-LDP-02`（SRT 作用量泛函）要求种群尺度的连续密度场数据，目前无可用管线。

**解决方案：三阶段验证路径**

**阶段 G2-1（仿真先验）**：
- 工具：Mesa / NetLogo 多智能体仿真
- 设置：$N > 1000$ 智能体，每个智能体遵从 Eq-Evo-01 的个体动力学
- 验证目标：群体密度场 $\rho(\sigma, t)$ 是否收敛至 Eq-LDP-01 预测的流体方程
- 证伪条件：仿真与 Eq-LDP-01 预测偏差 $> 10\%$ → 需修订有效理论假设

**阶段 G2-2（开放数据集预验证）**：

| 数据集 | 类型 | 变量对应 |
|-------|------|---------|
| Wikipedia 编辑流（2001–2024） | 社会 | 话题密度场 = $\rho$；编辑频率 = 流量 $J$ |
| Twitter/X 话题演化（公开子集） | 社会 | 话题扩散 = $\nabla \cdot J$；情感熵 = $S_{noise}$ |
| 城市移民数据（World Bank Open Data） | 人口 | 人口密度 = $\rho$；净迁入率 = $\partial_t \rho$ |

**阶段 G2-3（实验室受控实验，长期）**：
- 小组决策实验（$N = 20-50$）+ 实时行为记录
- 从 Eq-LDP-02 计算预期路径概率 $P_{path} \propto e^{-I_{SRT}[\rho]}$
- 实测路径频率与理论路径概率的指数关系检验

**Status 更新**：Gap → Partial（验证路径已规划，G2-1 可立即执行）

---

### G3 — Eq-Evo-01b / Eq-Sleep-01 ↔ H7（代谢-认知双通道协议）

**缺口根因**：`Eq-Evo-01b`（代谢增益调制）和 `Eq-Sleep-01`（睡眠 L₂ 优化）要求在同一实验中**同步采集**代谢指标与认知/d-value 指标，但标准协议不存在。

**解决方案：代谢-认知双通道模板（G3-Protocol-v1）**

**采集通道对应**：

| 时间窗 | 代谢通道 | 认知通道 | 对应方程变量 |
|-------|---------|---------|------------|
| T0（基线，空腹 12h） | 血糖（指尖血）、HRV（5 min） | 认知任务基线、d-value 代理（时间折扣率） | $\beta \mathcal{M}_{stress}$ 基线 |
| T1（标准餐后 1h） | 血糖峰值、胰岛素 | 相同认知任务 | $\beta \mathcal{M}_{stress}$ 低应激 |
| T2（中度运动后，HR > 140 bpm 持续 20 min） | 血乳酸（3 mM ± 0.5）、HRV 降低 | 相同认知任务 | $\beta \mathcal{M}_{stress}$ 中应激 |
| T3（24h 睡眠剥夺后） | 皮质醇（唾液）、血糖波动 | 认知任务 + 睡眠前模型复杂度（叙事一致性） | 睡眠 L₂ 优化验证 |
| T4（恢复睡眠后 2h） | 皮质醇恢复 | 认知任务 + 睡眠后模型复杂度 | Eq-Sleep-01：$\hat{G}_{sleep} = \arg\min_\theta K(L_2)$ |

**Eq-Evo-01b 的证伪条件**：代谢应激（$\mathcal{M}_{stress}$ 高）时，认知任务性能下降斜率与 $\beta$ 参数的非线性放大系数**不**相关 → Eq-Evo-01b 的乘性形式需修订。

**Eq-Sleep-01 的证伪条件**：T3→T4 过渡中，叙事一致性（模型复杂度代理）**无显著提升** → 睡眠的 L₂ 优化功能假设被否定。

**伦理说明**：T2（中度运动应激）和 T3（睡眠剥夺）需在医学监督下进行，须获得 IRB 批准，禁用于临床人群。

**Status 更新**：Gap → Partial（G3-Protocol-v1 已设计，需经 IRB 审批后执行）

**相关操作**：将 G3-Protocol-v1 纳入 `SRT_EXP_TEMPLATE.md` 的”代谢-认知双通道”节点。

---

## D. 立即可执行实验包（建议）

1. **包 A（低成本）**：H72 语言探针
   - 输入：文本语料 + 自评痛苦量表 + HRV
   - 验证：Eq-Force-01 / Eq-Pain-01

2. **包 B（中成本）**：归一化参数-d 相关
   - 输入：认知任务 + EEG + 行为策略数据
   - 验证：Eq-Evo-02 / Eq-Evo-03 与 H7

3. **包 C（高价值）**：代谢增益劫持
   - 输入：受控代谢扰动（伦理许可）+ 任务切换
   - 验证：Eq-Evo-01b 与 Ax-Exp-01

---

## 【理论边界/防误用声明】

1. 本映射表是“实验设计桥接层”，不等于已证实因果定律。  
2. `Mapped` 仅表示可构造可证伪路径，不代表统计显著性已建立。  
3. 涉及临床/生理干预的实验必须满足伦理审查，不得将理论映射直接用作诊疗结论。  
4. 群体尺度方程（LDP 系列）当前属于有效理论候选，需明确适用条件与失效边界。
