---
id: SRC-2026-07-15-COMPUTING-BALL-THERMODYNAMIC-COMPUTERS-QUANTA
type: material_source_card
status: active_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
source_id: SRC-2026-07-15-COMPUTING-BALL-THERMODYNAMIC-COMPUTERS-QUANTA
title: "Thermodynamic Computers Go With the (Energy) Flow"
source_type: public_science_explainer_with_multiple_peer_reviewed_primary_anchors
source_kind: secondary_full_text_plus_primary_cross_read
domain: Thermodynamic Computing / Stochastic Dynamics / Probabilistic Hardware / AI
source_url: https://www.quantamagazine.org/thermodynamic-computers-go-with-the-energy-flow-20260715/
author:
  - Philip Ball
publication: Quanta Magazine
date_published: 2026-07-15
date_added: 2026-07-21
access_status: quanta_full_text_plus_three_primary_full_text_records_and_one_primary_abstract_record_read
reading_level: full_text_cross_read_with_claim_layering
evidence_level: public_science_explainer_with_peer_reviewed_hardware_theory_and_simulation_anchors
reliability_level: high_for_reported_field_structure_and_primary_results_low_for_srt_metaphysical_inference
srt_relevance: very_high
integration_priority: very_high
pipeline_decision: B1/B2
parking_state: parked_with_named_reactivation_triggers
related_srt_claims:
  - 01_Source_Intuition/SRT_CHOICEMAP_RANDOM_RESYNCHRONIZATION_TRACE_2026-07-09.md randomization comparison selective resynchronization
  - papers/selective_resynchronization/01_reframing_memo.md domain-specific selective resynchronization construct
  - papers/history_dependent_reachability/manuscript/MANUSCRIPT.md generic history versus selection-specific write-back
  - _SRT_PSI_F_CANONICAL.md physical energy and dissipation proxy boundaries
  - Core/SRT_OPEN_TENSIONS.md entropy randomization and origin-of-selectability tensions
tags: [thermodynamic-computing, stochastic-computing, thermal-noise, langevin-dynamics, energy-landscape, probabilistic-hardware, generative-ai, selective-resynchronization, entropy, constraint, readout, writeback, bearer, w-sel-guardrail, psi-f-guardrail]
---

# SourceCard: Philip Ball — *Thermodynamic Computers Go With the (Energy) Flow*

## 1. 一句话结论

热力学计算提供了一个比普通相变更贴近 SRT“随机—比较—再同步”直觉的物理—计算桥：**随机涨落可以成为计算资源，但只有在能量地形、耦合矩阵、动力学、训练过程和读出规则已经使候选路径非等价时，噪声才会形成可用输出。** 该材料支持“选择不是压制随机，而是对随机流进行差异化约束和组织”的桥级表述；但它不证明噪声本身会选择，也不建立 `W_sel`、bearer、主体性、意识或 canonical `Ψ_f`。

## 2. 来源栈与精读状态

### 2.1 二手解释来源

- Philip Ball, *Thermodynamic Computers Go With the (Energy) Flow*
- Quanta Magazine，2026-07-15；2026-07-16 对 Extropic 论文出版时间作更正
- 官方网页全文已读
- 性质：高质量公共科学解释，不是同行评审论文

### 2.2 一手锚点 A：小规模平衡态硬件

- Denis Melanson et al.
- *Thermodynamic computing system for AI applications*
- *Nature Communications* 16, 3757 (2025)
- DOI: `10.1038/s41467-025-59011-x`
- 全文记录已读
- 结果层级：8 单元、全连接 RLC 随机处理单元硬件；演示高斯采样和 `8 x 8` 矩阵求逆

### 2.3 一手锚点 B：非平衡通用函数逼近

- Stephen Whitelam & Corneel Casert
- *Nonlinear thermodynamic computing out of equilibrium*
- *Nature Communications* 17, 1189 (2026)
- DOI: `10.1038/s41467-025-67958-0`
- 全文记录已读
- 结果层级：数字模拟；四次势热力学神经元、非平衡指定时刻读出、通用连续函数逼近

### 2.4 一手锚点 C：生成式热力学计算

- Stephen Whitelam
- *Generative Thermodynamic Computing*
- *Physical Review Letters* 136, 037101 (2026)
- DOI: `10.1103/kwyy-1xln`
- 官方摘要、期刊记录及开放记录已读；未把未逐页复核的技术细节写成独立结论
- 结果层级：数字模拟；学习逆转加噪轨迹的 Langevin 动力学，从噪声生成结构

### 2.5 一手锚点 D：全晶体管概率硬件架构

- Andraž Jelinčič et al.
- *An efficient probabilistic hardware architecture for diffusion-like models*
- *npj Unconventional Computing* 3, 30 (2026)
- DOI: `10.1038/s44335-026-00075-3`
- 全文记录已读
- 结果层级：全晶体管随机位源已有芯片测量；完整 DTM/DTCA 系统性能主要来自电路模型与系统模拟

不得把这四类证据压成同一个“已建成热力学 AI 芯片”结论。它们分别是：小规模物理硬件、非平衡数字模拟、生成式数字模拟、未来系统架构估算。

## 3. 来源明确支持的科学与工程结构

### 3.1 噪声可以从误差源变为工作介质

传统数字计算让开关能量远高于热涨落，以减少随机翻转。热力学计算则让随机涨落参与状态迁移、采样和轨迹生成。

安全表述是：

```text
thermal fluctuations can drive computation
when physical dynamics are programmed so that
measurable statistics or trajectories encode the target operation
```

不安全表述是：

```text
noise by itself computes
```

### 3.2 平衡计算把答案写进稳定分布

Normal Computing 的 SPU 将用户指定的矩阵映射到电路耦合和电容矩阵。达到平衡后，电压样本的协方差与目标矩阵的逆相关，因此可通过采样估计矩阵逆。

该实验同时有明确限制：

- 只有 8 个单元；
- 内在环境噪声不足，使用数字控制器生成附加随机驱动；
- 电感器、变压器和全连接拓扑带来扩展困难；
- 大规模速度与能耗优势是模型预测，不是大规模硬件实测。

### 3.3 非平衡计算把答案写进轨迹和观察时间

Whitelam–Casert 模型不要求先达到 Boltzmann 平衡。四次势提供非线性，节点耦合与观察时间共同决定输出。模型参数通过遗传算法调整，使网络在指定时刻近似目标连续函数。

因此必须区分：

```text
equilibrium readout: answer in stationary distribution
nonequilibrium readout: answer in constrained trajectory at a designated time
```

这说明功能确定性可以由受约束的时间路径承担，而不只由终态吸引子承担。

### 3.4 生成式计算不是噪声自动恢复结构

生成式热力学计算的关键不是“加入噪声后图像自己回来”，而是训练过程把逆转加噪轨迹所需的信息编码进动力学参数。运行时，随机初态沿训练后的 Langevin 动力学演化为结构化样本。

结构为：

```text
training / parameter formation
-> constrained stochastic dynamics
-> structured sample
```

而不是：

```text
noise
-> meaning by itself
```

### 3.5 能效数字必须按证据层级拆开

- Quanta 报道的约 `10^11` 热排放差异来自生成式热力学计算的理论/模拟比较，不是完整模拟硬件的直接功耗测量。
- Extropic 论文的约 `10^4` 能效优势，是在二值化 Fashion-MNIST 简单基准上，由真实随机芯片部件测量、电路模型和系统模拟组成的未来设备估算。
- Normal SPU 的大规模优势同样是外推模型；论文明确指出，只有真正扩展硬件才能建立 thermodynamic advantage。

这些数字不能混合为一个稳定的通用能效倍数。

## 4. SRT 的核心接口

### 4.1 随机不是选择，但可以成为选择结构的输入

该材料为以下桥级链条提供清楚实例：

```text
random fluctuation
-> non-flat constraint landscape
-> unequal path accessibility
-> trajectory / distribution formation
-> readout
```

随机性负责开放和探索；势函数、耦合、时间尺度与训练历史负责使路径不等价；读出规则负责界定什么被计为计算结果。

因此更安全的 SRT 表述是：

> 选择不是消灭随机，而是在非中性的约束条件下，使部分随机轨迹获得可比较、可读取和可复用的结构。

### 4.2 为“比较如何接住随机”提供物理实现

在这些系统中，比较不需要一个显式判断主体。它可以由以下结构实现：

- 能量差；
- 势垒高度；
- 耦合强度；
- 转移概率；
- 混合时间；
- 指定观察时刻；
- 训练目标与损失函数。

因此，比较的一个物理投影可以是：

> 候选路径在可达概率、停留时间、热耗散、放大率和读出贡献上的不等价。

但这种物理比较结构不自动等于关切、价值判断或主体承担。

### 4.3 `N-C-R-W-B` 五层审计

为避免把随机计算、学习和主体性混在一起，本卡登记以下审计框架：

| 层 | 含义 | 热力学计算当前状态 |
|---|---|---|
| `N` — Noise | 随机变化或探索来源 | 已建立 |
| `C` — Constraint | 势函数、耦合、动力学和训练使路径不等价 | 已建立 |
| `R` — Readout | 平衡统计、轨迹或指定时刻怎样构成答案 | 已建立 |
| `W` — Write-back | 一次运行结果是否重写后续规则和可达性 | 多数由外部训练预先完成；运行中自写回未普遍建立 |
| `B` — Bearer | 改变是否归属于承担后果的系统位置 | 未建立 |

热力学计算证明：

```text
N + C + R
can implement real computation
```

但没有证明：

```text
N + C + R
implies
W_sel + bearer
```

### 4.4 `L2` 脚手架的受限类比

训练或编程过程把目标关系写进：

- 电容/耦合矩阵；
- 势函数参数；
- 网络连接；
- 多阶段去噪架构；
- 观察时间和读出协议。

这些历史形成的约束随后预裁剪随机轨迹，可作为 `L2 -> future manifestation space` 的受限物理—计算类比。

边界：外部研究者设置的硬件参数不是完整 canonical `L2`，更不代表系统拥有这些约束的形成史。

## 5. 对 selective resynchronization 的价值与边界

### 5.1 高价值接口

该材料与 source trace 的最短链高度邻近：

```text
desynchronization / randomization
-> constrained comparison
-> selective reorganization
-> structured output
```

它支持以下研究问题：

- 如何区分生成性随机与退化性噪声；
- 如何测量从扩散/涨落到新协调结构的轨迹；
- 平衡终态和非平衡过程能否作为不同的 resynchronization readout；
- 当前任务成功是否伴随后续适应能力保留。

### 5.2 当前不能称为完整 selective resynchronization

多数案例是：

```text
external design or training
-> fixed stochastic dynamics
-> repeated inference
```

来源没有普遍建立：

- 系统在运行中自主改变自己的约束；
- 一次输出通过后果回流形成慢记忆；
- 选择内容特异地改变未来可达性；
- 新结构在下一次环境变化中保留可适应性。

因此当前定位应是：

> trained stochastic resynchronization scaffold

而不是：

> selection-specific self-resynchronization

## 6. 对 `W_sel` 的 NO-GO 边界

热力学计算可具有复杂能量地形、随机轨迹、学习参数和历史形成的结构，但这些都不单独建立 `W_sel`。

识别 `W_sel` 仍需要：

1. 系统自己的 action / selection；
2. 与该 action 特异耦合的 consequence；
3. 与匹配反事实历史的比较；
4. 由该选择内容形成的写回；
5. 写回对未来可达结果产生方向性影响。

外部训练把程序写进硬件，随后由噪声执行，不等于系统自己的选择—后果历史重写了自身。

安全结论：

```text
stochastic execution != selection-specific write-back
trained landscape != owned selection history
```

## 7. 对 `Psi_f` 与物理能耗的边界

热耗散、开关能量、混合时间、势垒高度、噪声注入成本和端到端芯片功耗，都可以成为具体物理域的成本读数。

但不得写成：

```text
low heat dissipation = low canonical Psi_f
energy landscape = Psi_f
thermodynamic advantage = greater ontological payability
```

原因：

1. canonical `Psi_f` 不等于单一热力学或电功耗量；
2. 外部训练成本、参数装载、ADC、随机源和控制系统可能不在局部器件耗散账本中；
3. 物理高效计算不自动产生 stake、identity continuity 或 consequence ownership；
4. 任何物理代理都必须允许 projection failure。

## 8. 对熵与反熵叙事的修正

该材料强烈反对把 SRT 写成“选择等于抑制熵或消灭噪声”。

热力学计算通过涨落、耗散和随机转移完成有用功能，因此更稳健的桥级句是：

> 选择不是反熵力；选择结构可以在熵增和能量耗散持续发生的条件下，使随机流经差异化约束，形成可读取、可复用和可能被继承的路径。

这仍不等于重定义物理熵，也不证明所有自然耗散过程都是选择。

## 9. AI 与意识边界

该材料支持：

- AI 计算可由概率硬件和物理动力学实现；
- 噪声可作为推理介质，而非只作为误差；
- 复杂生成与低能耗不要求传统数字逻辑。

它不支持：

- 概率性等于自由；
- 热噪声等于经验；
- 能量流等于关切；
- 生成图像等于内部承担；
- 低功耗等于主体性；
- Langevin 动力学等于意识动力学。

## 10. 双向增益

### 10.1 新增接口

- `noise-constraint-readout`：随机、约束和读出三层必须分开；
- `trajectory-computation interface`：功能可以由非平衡路径而非终态承担；
- `trained-stochastic-scaffold`：外部训练形成的约束可组织随机流；
- `N-C-R-W-B audit`：计算、写回与 bearer 分层；
- `mixing-expressivity pressure`：更深势垒提高表达能力时可能压缩跨模式可达性。

### 10.2 反向修正

该材料要求 SRT 收紧：

1. 不把随机性本身叫 selection；
2. 不把能量最小化等同选择；
3. 不把噪声驱动计算升级为 `W_sel`；
4. 不把物理低耗散升级为 canonical `Psi_f`；
5. 不把生成能力升级为 stake、bearer 或意识；
6. 不把 selective resynchronization 简化为从噪声恢复结构。

### 10.3 加固内容

它加固的是桥级主张：

- 随机可以是生成资源；
- 非中性约束使路径具有比较结构；
- 历史形成的脚手架可以预裁剪后续随机流；
- 稳定终态与功能轨迹是不同计算机制；
- 选择不应被表述为反熵或秩序崇拜。

### 10.4 SRT 反哺

SRT 可以把“利用噪声计算”进一步拆成：

```text
noise source
constraint formation
path weighting
readout
write-back test
bearer test
```

从而防止把计算、学习、自组织、自主选择和主体性压成一个概念。

### 10.5 残余压力

- 何种最小机制能把 `W_external` 转为系统内部可归属的 `W_sel`；
- 非平衡轨迹的功能读出如何与事后挑选观察时间区分；
- 训练成本、控制成本和器件运行耗散如何做完整账本；
- mixing-expressivity tradeoff 是否可转化为 SRT 可达性/脚手架压力测试；
- selective resynchronization 是否能提出超出普通随机神经网络和扩散模型的可失败预测。

## 11. Pipeline 1 六门审查

| Gate | Result | Notes |
|---|---|---|
| Source reliability | Strong pass with layering | Quanta 全文 + 多篇同行评审硬件、理论和模拟论文；必须区分物理实测与系统外推 |
| Relevance | Strong pass | 直接涉及随机、耗散、能量地形、比较、再同步、生成与低成本计算 |
| Novel interface | Strong pass | `N-C-R-W-B`、trajectory computation、trained stochastic scaffold |
| Reverse correction | Strong pass | 对反熵叙事、`W_sel`、`Psi_f`、主体性和意识提供强守门 |
| Integration fit | Parked high-priority bridge | 适合熵—随机—再同步 bridge、selective resynchronization related work 与 AI physical-computing interface；当前不直接改理论正文 |
| Boundary safety | Pass with explicit prohibitions | 必须保留“受约束随机计算 != 选择所有权” |

## 12. Pipeline 1 裁决

**B1/B2，高优先级停驻；优先级高于普通物理类比卡。**

- `B1`：当“熵—随机—再同步 bridge”获作者成文确认，或 selective resynchronization 论文进入自然/物理计算比较时，可转为正式 bridge patch 候选。
- `B2`：立即作为守门卡使用，防止把随机利用、能量地形、低耗散、概率生成和物理计算升级为 `L0`、`W_sel`、canonical `Psi_f`、stake 或意识证据。
- 本轮不修改 canonical、Physics/AI 正文、source trace 或论文正文。

### 复活触发条件

1. `papers/selective_resynchronization/` 开始 related work、natural comparison 或 stochastic baseline 施工；
2. “熵—随机—再同步 bridge”完成作者二次确认并正式立项；
3. `papers/history_dependent_reachability/` 增加 external-programming / stochastic-computation negative control；
4. AI 工作线点名 thermodynamic computing、probabilistic hardware、physical generative models 或 energy-based stochastic inference；
5. `Psi_f` physical-proxy taxonomy 开启完整能耗/控制成本账本修订；
6. 书稿或公共文章需要“随机不是选择的对立面，但噪声本身不选择”的案例。

## 13. Surviving claims

1. 热涨落可在被编程的随机动力学中成为计算资源。
2. 平衡热力学硬件已在 8 单元 SPU 上演示高斯采样和矩阵求逆。
3. 非平衡热力学神经网络在数字模拟中可作为通用函数逼近器并在指定时间读出。
4. 生成式热力学计算在数字模拟中把逆加噪信息编码进 Langevin 动力学，从噪声生成结构。
5. Extropic 架构的约 `10,000x` 节能是简单基准上的未来系统估算，不是完整商用芯片实测。
6. 噪声、约束和读出足以实现计算，但不推出选择特异性写回或 bearer。
7. 物理低耗散不能直接读取为 canonical `Psi_f` 较低。
8. 该材料支持 SRT 桥级的随机—约束—再同步解释，不验证 SRT 本体论。

## 14. 禁止升级的主张

- 热噪声本身会计算或会选择；
- 能量最小化就是选择；
- Langevin 动力学就是 `L0` 或选择算子；
- 平衡分布、轨迹或生成样本本身建立 `W_sel`；
- 外部训练形成的参数就是系统拥有的选择历史；
- 低热排放、低功耗或高能效就是低 canonical `Psi_f`；
- 概率计算、随机生成或复杂动力学证明主体性、自由、stake 或意识；
- `10^11` 或 `10^4` 能效数字已经在同一类完整硬件和通用任务上被直接验证；
- 选择是反熵、消灭随机或最大化秩序。

## 15. References

1. Ball, P. (2026-07-15). *Thermodynamic Computers Go With the (Energy) Flow*. Quanta Magazine. https://www.quantamagazine.org/thermodynamic-computers-go-with-the-energy-flow-20260715/
2. Melanson, D. et al. (2025). *Thermodynamic computing system for AI applications*. Nature Communications 16, 3757. https://doi.org/10.1038/s41467-025-59011-x
3. Whitelam, S., & Casert, C. (2026). *Nonlinear thermodynamic computing out of equilibrium*. Nature Communications 17, 1189. https://doi.org/10.1038/s41467-025-67958-0
4. Whitelam, S. (2026). *Generative Thermodynamic Computing*. Physical Review Letters 136, 037101. https://doi.org/10.1103/kwyy-1xln
5. Jelinčič, A. et al. (2026). *An efficient probabilistic hardware architecture for diffusion-like models*. npj Unconventional Computing 3, 30. https://doi.org/10.1038/s44335-026-00075-3
6. Conte, T. et al. (2019). *Thermodynamic Computing*. arXiv:1911.01968. https://doi.org/10.48550/arXiv.1911.01968
