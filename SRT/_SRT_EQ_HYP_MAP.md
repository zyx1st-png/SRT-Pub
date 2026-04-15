---
id: SRT-EQ-HYP-MAP
type: framework
tags: [Mapping, Equations, Hypotheses, Falsification]
status: axiomatic_hybrid_v1
layer: L1
epistemic_layer: os
claim_mode: canonical
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
| Eq-Select-Thermo | 选择热力学宪法不等式 | H1 / H6 | `q(L_1)` 三代理（网络互信息密度 / 行为可压缩率 / 稳态成功率）与 `P_sel` 预算侧、`S_noise` 噪声侧联读 | Partial |
| Eq-Stab-01 | 固定点稳定条件 | H6 | 扰动恢复时间、吸引域回归概率 | Partial |
| Eq-Phase-01 | 本体论相变阈值 | H6 | 信息量 I 超阈值 τ 的跃迁曲线拟合 | Partial |
| Eq-Sleep-01 | 睡眠 L2 优化 | H7 | 睡眠前后模型复杂度/误差压缩 | Partial |
| Eq-LDP-01 | 水动力极限 | H6 | 粗粒化密度场 `\rho(x,t)`、局部流量 `J(x,t)`、相关长度与阈值动力学的联合拟合 | Partial |
| Eq-LDP-02 | SRT 作用量泛函 | H6 | 对粗粒化路径频率做 `\log P_{path}` vs 候选 `I_{SRT}[\rho]` 的指数衰减检验 | Partial |
| Eq-Phantom-01 | 社会幻肢痛 | H72 | 关系丧失后语言-情绪耦合摩擦轨迹 | Partial |
| Eq-Phantom-02 | 稳态重建时间常数 | H7 / H72 | 可塑性指标 vs 恢复时间 τ_rebuild | Partial |
| Eq-Multi-01 | 集体自由能景观 | —（新增理论框架） | 多算子系统的整体摩擦测量（待操作化） | Gap |
| Eq-Multi-02 | 个体算子为集体景观梯度 | —（新增理论框架） | 个体行为方向与集体梯度场对齐度（待设计） | Gap |
| Eq-Multi-03 | 集体 d-value 为景观有效维度 | —（新增理论框架） | 团队/组织的 Hessian 曲率测量（待操作化） | Gap |
| Eq-IT-A | Ψ_f = Landauer 原理在 Fisher 几何中的推广 | —（新增，IT Bridge） | 同等信息量选择在不同参数曲率下的能耗比较 | Gap |
| Eq-IT-B | d = D_eff(I_F) Fisher 有效维度 | —（新增，IT Bridge） | 神经 Fisher 信息矩阵特征谱与 d 值测量的对比实验 | Gap |
| Eq-IT-B' | d×Ψ_f ≥ k_BT·𝒦 不确定性关系候选 | —（新增，IT Bridge） | 操控 d-Ψ_f 权衡的实验验证；常数 𝒦 的测定 | Gap |
| Eq-IT-C | 复杂性棘轮（第二定律为生成压力） | —（新增，IT Bridge） | 纵向演化实验：高 d/Ψ_f 效率种群的复杂度增长率 | Gap |
| Eq-IT-D | Boltzmann 为 SRT d→0 退化极限 | —（新增，IT Bridge） | 低 d 系统行为与 Boltzmann 分布的 KL 散度测量 | Gap |
| Eq-IT-E | I_created = I(L₀;Ĝ_θ) 选择创造信息 | —（新增，IT Bridge） | 选择事件前后的互信息变化量测量 | Gap |

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

**文献锚点（2026-03-16，桥接层）**

- **Casali et al. 2013（*Sci Transl Med*）**：PCI 以扰动后时空响应的算法可压缩性为核心，支持“压缩率/复杂度”可作为高门槛神经秩序代理，而非纯幅值读数。
- **Schartner et al. 2015（*PLoS ONE*）**：自发 EEG 信号多样性在丙泊酚麻醉下降，支持“信号多样性/可压缩性”可作为秩序崩塌或可用状态空间收缩的神经侧 proxy。
- **Peng et al. 2014（*Front Hum Neurosci*）**：Lempel-Ziv complexity 可操作化人类动作序列的时间结构，支持行为可压缩率作为 `q^{(B)}` 的低成本代理。
- **Stender et al. 2016（*Curr Biol*）**：持续意识存在最低代谢需求，提供 `P_sel` 预算侧 proxy（FDG-PET / 葡萄糖代谢）的实证锚点。
- **Weninger et al. 2022（*Phys Rev E*）**：形式化讨论神经网络能量学与信息论量之间的关系，为 `P_sel - q - S_{noise}` 的联读提供理论桥接，而不是单一指标替代。

**代理配套（P1-Bridge-v2）**

| 项 | 最小 proxy 组 | 说明 |
|-----|---------|---------|
| `q(L_1)` | `q^{(A)}` 网络互信息密度；`q^{(B)}` 行为 Lempel–Ziv / MDL；`q^{(C)}` 稳态成功率 | `q^{(A)}` 仍偏设计态，`q^{(B)}` 与神经复杂度代理已有较稳一手锚点 |
| `P_{sel}` | HRV 恢复斜率；血糖/乳酸；FDG-PET 或同类代谢预算 | 读作“可用选择预算”，不等于单一脑区激活 |
| `S_{noise}` | EEG 高频功率/熵；任务冲突熵；环境波动负荷 | 读作噪声侧抽头，而非系统全部随机性 |

**收敛效度检验**：三代理在独立样本上相关系数 $r > 0.5$ 则认为 $q(L_1)$ 被充分操作化。

**Eq-Select-Thermo 的证伪条件**：若 $dq^{(A,B,C)}/dt$ 与能量预算（血糖、HRV、代谢率）和噪声熵（EEG 高频功率）的线性组合**不**满足宪法不等式方向，则 Eq-Select-Thermo 需修订。

**Status 更新**：Gap → Partial（三代理方案已设计，且 `q^{(B)}` / `P_{sel}` 已获得一手文献锚点；`q^{(A)}` 与完整联立验证仍待实验推进）

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

**文献锚点（2026-03-16，桥接层）**

- **Toner & Tu 1998（*Phys. Rev. E*）**：经典 flocking 连续体理论，证明大量局部相互作用主动体可由宏观速度场/密度场描述；为 Eq-LDP-01 中“群体 = 有效连续介质”的合法性提供基础窗口。
- **Bain & Bartolo 2019（*Science*）**：真实人群（数万名起跑排队者）的速度信息以系统尺度传播，而方向涨落局部受抑；直接支持在真实人群中用 `\rho / J` 与传播模态来读群体动力学，而不是只停留在个体规则层。
- **Gu et al. 2025（*Nature*）**：高密度真实人群在阈值上方出现大尺度相关与自发振荡，说明 `\rho(x,t)`、相关长度、谱峰与相变窗口是可测的群体变量，可直接服务 Eq-LDP-01。
- **Bertini et al. 2001 / 2005 / 2015（*PRL* / *RMP*）**：宏观涨落理论将密度-电流联合时空涨落写成大偏差率函数控制的路径概率，为 Eq-LDP-02 的 `P_{path} \asymp e^{-N I[\rho]}` 提供最稳的统计力学母语。
- **Agranov et al. 2023（*SciPost Phys.*）**：即便在非平衡主动粒子系统中，也可导出 fluctuating hydrodynamics 与 current large deviations，并出现动力学相变；支持把 Eq-LDP-02 读作“有效理论窗口”，而非只适用于平衡或被动系统。

**代理配套（G2-Bridge-v2）**

| 项 | 最小 proxy 组 | 说明 |
|-----|---------|---------|
| `\rho(x,t)` | 空间 occupancy histogram；topic share density；人口/细胞局部密度 | 统一读作粗粒化密度场，不要求微观机制同构 |
| `J(x,t)` | 光流/轨迹有限差分；编辑流量；净迁入率矩阵 | 统一读作局部流量或通量 |
| `\xi, \omega_0, \rho^*` | 相关长度、谱峰、临界密度 | 用于识别 Eq-LDP-01 的相变/模态窗口 |
| `I_{SRT}^*[\rho]` | 运动学代价 + 摩擦/噪声预算 + 吸引势近似的粗粒 surrogate | 当前先作候选 rate-function proxy，不冒充唯一 canonical action |

**最小证伪模板（P2）**

- 若群体密度场与局部流量不能形成稳定的连续描述，且 coarse-graining 后预测力不优于个体级启发式模型，则 Eq-LDP-01 应降级。
- 若粗粒化路径频率与任何合理的 `I_{SRT}^*[\rho]` surrogate 都不呈近似指数衰减，则 Eq-LDP-02 的作用量读法需修订。
- 若只在单一数据域成立、跨 crowd / cell sheet / online collective 完全失配，则应把 LDP 条款收窄为域特异有效理论。

**Status 更新**：Gap → Partial（验证路径已规划，且已获得 density/current 与 path-LDP 的一手文献锚点；开放数据与实验室实现仍待执行）

**G2-2a 开放数据 MVP（2026-03-16）**

优先选用**Wikimedia 双源组合**，因为它同时提供低门槛的长期聚合数据与实时事件流：

| 数据源 | 官方接口 | 在 SRT 中的读法 |
|-------|---------|---------|
| Wikimedia pageviews | public pageviews dataset / AQS pageviews API | 主题箱 `k` 的注意密度 `\rho_k(t)` |
| Wikimedia EventStreams `recentchange` | `stream.wikimedia.org/v2/stream/recentchange` | 主题箱 `k` 的编辑流量 `J_k(t)` 与事件冲击项 |

**最小变量构造**

1. 先将页面映射到有限个主题箱 `k = 1...K`（例如 politics / science / sport / crisis / entertainment）。
2. 定义：
   \[
   \rho_k(t)=\frac{\text{pageviews in bin }k \text{ at } t}{\sum_j \text{pageviews in bin }j \text{ at } t}
   \]
   \[
   J_k(t)=\frac{\text{recent changes in bin }k \text{ during }[t,t+\Delta t]}{\Delta t}
   \]
3. 对外部冲击窗口（breaking news / coordinated edit burst）抽取 24h–72h 轨迹，聚类成有限路径类 `\Gamma_m`。
4. 估计路径频率 `P(\Gamma_m)`，再检验：
   \[
   \log P(\Gamma_m)\approx -a\, I_{SRT}^*(\Gamma_m)+b
   \]

**最小成功判据**

- `Eq-LDP-01`：topic-bin 级的 `\rho_k(t)` 与 `J_k(t)` 联动优于独立 AR 基线，且冲击传播可由相关长度/时滞结构总结。
- `Eq-LDP-02`：路径类频率对 `I_{SRT}^*` 出现稳定负斜率，而非纯随机散点。

**边界**

- 这只是 online collective 的 MVP，不自动外推到国家迁移、线下 crowd 或细胞层。
- `J_k(t)` 在这里是“主题箱流量”而非严格空间通量；若需要连续体极限，后续必须转入真实轨迹数据。

**实现挂钩**

- 脚本骨架：`scripts/g2_wikimedia_open_data_mvp.py`
- 主题映射样例：`data/g2_open_data/topic_mapping.example.json`
- 首轮样本输出：`data/g2_open_data/sample_run/`

**首轮执行注记（2026-03-16）**

- pageviews 端已真实跑通，得到 `pageviews_raw.csv -> rho.csv`。
- `EventStreams` 直播采样在短窗口下命中稀薄且易超时，因此 MVP 首轮改用 `fetch-recentchanges-api` 作为 bounded sample fallback。
- 当前已在 `sample_run/` 中闭合出 1 条 trajectory 与 1 个 path class，证明 `rho -> J -> path_label` 的最小链路可运行；但样本仍过小，不足以支撑任何率函数拟合结论。

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
