---
id: SRT-LIFE-BOUNDARY-CASE-ECOLI-CHEMOTAXIS-UNIFIED-AUDIT-20260805
type: operational_audit_report
tags: [Life, Bacteria, EscherichiaColi, Chemotaxis, Adaptation, UnifiedAudit, SelectionEvent, CG0, NER, PEF, CBP, HEF, NegativeResult]
status: active
record_stage: first_life_boundary_case_audit
layer: meta
epistemic_layer: os
claim_mode: operations_execution
claim_level: audit_only
canonical: false
ai_do_not_use_for_definition: true
created: 2026-08-05
revised: 2026-08-05
provenance: 2026-08-05 作者在完成 GitHub 正确 SHA／错误 SHA 严格配对校准后要求继续研究；本报告选择大肠杆菌趋化适应作为首个生命系统边界案例，检验统一选择事件审计是否会把成熟控制回路、执行动作、代谢成本和短时记忆自动升级为选择事件。
dependency: [Operations/SRT_UNIFIED_SELECTION_EVENT_AUDIT_PROTOCOL_2026-08-04.md, Operations/SRT_INTERNAL_NON_EQUIVALENT_REGISTRATION_OPERATIONAL_TEST_2026-08-04.md, Operations/SRT_PATH_EFFICACY_OPERATIONAL_TEST_2026-08-04.md, Operations/SRT_CONSEQUENCE_BEARING_POSITION_OPERATIONAL_TEST_2026-08-04.md, Operations/SRT_HISTORICAL_EFFICACY_OPERATIONAL_TEST_2026-08-04.md, Operations/SRT_TB_TD_TE_CROSS_DOMAIN_STRESS_TEST_2026-08-04.md]
---

# 第一轮生命系统边界案例：大肠杆菌趋化适应

## 0. 结论先行

本案例选择大肠杆菌（*Escherichia coli*）趋化适应，是因为它同时具有：

- 可控的外界化学差异；
- 可定位的受体—激酶—CheY 信号介质；
- CheR／CheB 介导的受体甲基化与去甲基化；
- 可直接改变鞭毛旋转、run／tumble 和空间迁移的执行通道；
- 可用基因缺失、受体位点突变、FRET、单细胞轨迹和微流控梯度进行降级与干预。

它因此是一个比软件事务更接近生命过程的强测试对象。

但本轮得到的核心结果是一个**受限阴性结果**：

> 现有趋化文献可以分别为内部非等价登记、现实路径效力和短时历史效力提供强证据；但标准实验通常没有在同一个冻结事件、同一个细胞边界和相容时间尺度内，同时测量路径特异的维持后果、资源收益、损失、修复成本或未来行动能力。因此，不能把跨论文证据拼接成 `SEA-3`。

保守结论为：

| 审计对象 | 最高允许判定 | 决定性限制 |
|---|---|---|
| 受体—CheY—鞭毛信号／执行链 | `SEA-2` | 存在真实执行路径，但后果承载位置未在该边界闭合 |
| 单次 tethered-cell 时间比较实验 | `SEA-2` 上限 | 马达状态改变，但细胞被固定，空间导航路径被实验装置切断 |
| 单次梯度迁移实验 | `SEA-2 strong` | 空间路径改变；但标准读数主要是位置／积累，不等于已测得细胞维持后果 |
| 跨研究综合叙述 | 不给统一 SEA 等级 | 违反“同一冻结事件证据”规则 |
| 未来同细胞综合实验 | 可检验 `SEA-3 qualified` | 必须追加 CBP 与 HEF 的同事件因果测量 |

因此，本案例没有把“生命”本身当作升级理由，也没有因为系统具有适应、记忆、耗能、运动和反馈就自动判为选择事件。

---

## 1. 为什么选择趋化，而不是更宏大的生命过程

趋化具有四个方法优势。

### 1.1 每一层都有普通理论

它可以由成熟理论充分描述：

- 两组分信号转导；
- 受体协同性与增益调节；
- CheA／CheY 磷酸转移；
- CheR／CheB 负反馈适应；
- 鞭毛马达旋转切换；
- biased random walk；
- integral feedback／robust adaptation；
- 信息传递与控制理论。

这迫使 SEA 证明自己的增量，而不能依靠机制未知或现象神秘。

### 1.2 有自然降级条件

可比较：

- wild type；
- `cheR cheB` 双缺失；
- 不能正常甲基化的受体；
- CheY／马达耦合受损；
- 细胞被 tether，马达输出存在但空间执行被阻断；
- 均匀环境，执行存在但目标梯度差异消失；
- 非代谢型吸引物，路径改变但营养后果可能缺失。

### 1.3 可以区分“记忆”与“历史效力”

受体甲基化是短时适应载体，但：

- 它是可逆的；
- 它通常作用于秒至分钟尺度；
- 它不自动构成跨情境规则重写；
- 它不自动等于 L₂、主体连续性或生物学学习。

### 1.4 可以产生真正的阴性结果

如果标准趋化实验只能建立：

```text
差异登记
→ 马达执行
→ 空间偏移
→ 短时适应
```

却没有建立：

```text
路径特异后果
→ 可定位承载位置
→ 维持／恢复／资源／行动能力改变
```

那么统一协议必须停在 `SEA-2`，不能因为对象是活细胞而补偿 CBP 失败。

---

## 2. 系统结构与普通机制基线

最小机制链为：

```text
外界配体浓度随时间变化
→ Tar／Tsr 等受体阵列改变 CheA 活性
→ CheY 磷酸化水平改变
→ CheY-P 与鞭毛马达开关结合
→ CW／CCW 偏置改变
→ run／tumble 统计改变
→ 细胞轨迹产生上梯度或避开排斥物的偏置
```

适应回路为：

```text
受体活性
→ CheR 甲基化／CheB 去甲基化
→ 受体响应基线与增益改变
→ 后续相同输入产生不同响应
```

本报告不把以下普通机制重新命名为 SRT 新机制：

- 受体结合；
- 磷酸化；
- 共价修饰；
- 负反馈；
- 马达开关；
- 随机游走偏置；
- 生长优势；
- 进化选择。

SRT 的当前候选增量只在于：

> 要求这些机制在同一事件中分别通过差异、登记、路径、承受和历史五门，并禁止把跨研究、跨边界或跨尺度证据拼成一个选择事件。

---

## 3. 边界台账

### B₁ · 信号网络边界

包括：

- chemoreceptors；
- CheA／CheW；
- CheY／CheZ；
- CheR／CheB；
- 细胞内相关信号状态。

排除：

- 鞭毛马达；
- 细胞空间位置；
- 营养获取；
- 生长与存活；
- 外部梯度场。

该边界可以建立登记和历史载体，但不能独立建立真实空间路径或细胞级后果。

### B₂ · 感觉—运动细胞边界

包括：

- B₁ 全部；
- 鞭毛马达；
- 细胞体；
- run／tumble 行为；
- 当前空间轨迹。

排除：

- 长时营养场重塑；
- 群体增长；
- 代谢资源收益的长期累积；
- 多代适应与进化。

B₂ 可以建立真实运动路径，但仍需单独证明路径特异后果落到细胞维持位置。

### B₃ · 单细胞—局部环境闭环

包括：

- B₂ 全部；
- 局部化学梯度；
- 营养／毒性暴露；
- 细胞内可用资源、能量或维持变量；
- 在冻结事件窗口内的恢复与后续探测能力。

B₃ 是本案例讨论完整选择事件候选的最小边界。

### B₄ · 群体—资源场

包括：

- 多个细胞；
- 自生成或外加梯度；
- 资源消耗与代谢物释放；
- 种群扩张和相对增长。

B₄ 适合研究生态与适合度后果，但不能把群体收益反投为单个细胞在某一秒内的承受证据。

---

## 4. 文献事件 E₁：tethered-cell 时间比较

### 4.1 冻结事件类型

Segall、Block 与 Berg（1986）对固定细胞施加 impulse、step、ramp 和周期刺激，测量马达响应；同时比较 wild type 与 `cheR cheB` 适应缺陷突变体。

文献报告：

- wild type 对最近约 4 秒的刺激历史进行有正负权重的时间比较；
- `cheR cheB` 突变体仍可对近期刺激作响应，但不能完成正常的短时时间比较；
- 小阶跃刺激下突变体在观察窗口内不能正常适应。

### 4.2 五门审计

| 门 | 判定 | 理由 |
|---|---|---|
| CG-0 / DMF | `DMF-2 supported` | 外界刺激被控制并进入受体—马达响应通道 |
| CG-1 / NER | `NER-3 supported` | 当前响应依赖最近刺激历史；`cheR cheB` 干预选择性破坏时间比较 |
| CG-2 / PEF | `PEF-2 local-actuator` | 马达旋转状态真实改变；但 tether 阻止细胞空间迁移 |
| CG-3 / CBP | `CBP-1 or lower` | 测量到一般运动／实验成本，未测得路径特异细胞维持后果 |
| CG-4 / HEF | `HEF-3 qualified` | 适应状态改变后续响应；但载体与未来可达性未在同一实验中被完全分离 |

### 4.3 SEA 判定

```text
SEA-2 upper bound
```

原因：

- 马达执行路径真实改变；
- 细胞被固定，目标空间路径被实验装置切断；
- 后果承载门未闭合；
- 不能因为存在时间比较和记忆就升级为完整选择事件。

这一结果对应软件案例中的重要区分：

> 执行器内部状态改变，不等于目标环境路径已经改变。

---

## 5. 文献事件 E₂：梯度迁移与甲基化缺陷

### 5.1 冻结事件类型

Hazelbauer、Park 与 Nowlin（1989）研究不能正常甲基化的 transducer，比较刺激识别、适应和梯度迁移。

文献报告：

- 突变受体仍能识别配体并产生影响鞭毛的兴奋信号；
- 缺少有效甲基化时，适应和净梯度迁移严重受损；
- 其他具有可甲基化位点的受体在一定条件下可通过 adaptational crosstalk 部分补偿。

另有研究在稳定 aspartate 梯度中比较 wild type 与缺少 methyltransferase／methylesterase 的双突变体，发现动态受体甲基化对于温和梯度中的正常迁移是必要的。

### 5.2 五门审计

| 门 | 判定 | 理由 |
|---|---|---|
| CG-0 / DMF | `DMF-3 supported` | 梯度沿细胞轨迹形成现实连续差异 |
| CG-1 / NER | `NER-2 supported; NER-3 qualified` | 受体甲基化位点与 CheR／CheB 干预改变相对响应和适应 |
| CG-2 / PEF | `PEF-3 supported` | run／tumble 与净迁移改变，替代空间路径概率被重分配 |
| CG-3 / CBP | `CBP-2 not established` | 位置积累／迁移不是维持损失、资源收益或恢复成本的直接测量 |
| CG-4 / HEF | `HEF-3 qualified` | 甲基化状态影响后续梯度响应；但未来路径效力与短时状态残留需进一步解耦 |

### 5.3 SEA 判定

```text
SEA-2 strong
SEA-3 not established
```

决定性原因不是缺少生命复杂性，而是：

> 该事件强烈支持现实路径重分配，却没有在同一事件中直接证明哪一个细胞维持位置承担了路径特异后果。

“细胞最终更靠近吸引物”不能自动替代：

- 实际营养摄取；
- ATP／质子动力势变化；
- 生长率差异；
- 毒性暴露减少；
- 修复成本；
- 后续行动能力改变。

---

## 6. 为什么不能跨论文拼成 SEA-3

现有研究还分别显示：

- 受体甲基化改变刺激—激酶耦合增益；
- FRET 可追踪 CheA／CheY 通路的动态适应；
- CheY-P 与马达结合可直接触发旋转切换；
- 趋化可在某些环境中带来增长或种群扩张优势；
- 细胞会按潜在趋化收益调整对运动系统的资源投入。

这些结果共同提供了很强的机制图景，但统一协议禁止如下拼接：

```text
论文 A 的 NER
+ 论文 B 的 PEF
+ 论文 C 的 CBP
+ 论文 D 的 HEF
= 一个完整 SEA-3 事件
```

原因包括：

- 细胞株不同；
- 配体不同；
- 环境结构不同；
- 时间尺度从毫秒、秒、分钟延伸到小时和多代；
- 一些实验使用 tethered cell，一些使用自由游动群体；
- 一些测量信号，一些测量空间分布，一些测量增长；
- 角色与承受位置并非同一事件中的同一对象。

因此，跨研究证据可以支持**实验设计与机制可行性**，不能直接支持单一 SEA 等级。

---

## 7. CBP 是本案例的主要瓶颈

趋化讨论中常见推理是：

```text
趋向营养
→ 对细胞有益
→ 细胞承担后果
```

这在进化或生态层面可能合理，但对单次事件仍不够。

### 7.1 需要区分的量

| 量 | 能否单独建立 CBP-2 |
|---|---|
| 马达耗能 | 否，一般实现成本 |
| 细胞移动距离 | 否，路径结果，不是承受后果 |
| 靠近吸引物 | 否，可能是非代谢型配体 |
| 吸引物进入细胞 | 不一定，需证明改变维持变量 |
| ATP／生长／修复能力改变 | 可成为 CBP-2 候选 |
| 毒物暴露或膜损伤减少 | 可成为 CBP-2 候选 |
| 路径导致未来可行动范围改变 | 可成为 CBP-2／HEF-3 接口 |

### 7.2 非代谢型吸引物作为关键阴性对照

若细胞对 α-methyl-DL-aspartate 等非代谢型吸引物产生强迁移：

- DMF、NER 和 PEF 可很高；
- 细胞可明显积累；
- 但不存在相应营养收益。

这说明：

> “趋向吸引物”与“承担／获得维持后果”必须分开，不能由行为方向推断价值或 stake。

### 7.3 群体适合度不能自动下放

有研究显示趋化能够提高种群扩张或相对增长，但：

- 群体收益不等于每个细胞的同等收益；
- 多代结果不等于单次 run／tumble 的后果；
- 自生成梯度与外加梯度可能具有不同承受结构；
- 资源投资成本与收益可能在不同时间和不同细胞间分配。

因此群体层结果必须在 B₄ 单独审计。

---

## 8. HEF：甲基化是强候选，但不是自动写回

### 8.1 支持 HEF-3 的理由

- `cheR cheB` 干预破坏正常时间比较；
- 受体甲基化状态改变刺激—激酶耦合增益；
- 过去配体暴露影响后续同类刺激的响应；
- 重置或破坏甲基化机制会改变未来梯度导航。

这些事实使受体修饰成为比普通日志或残留更强的历史载体。

### 8.2 仍需排除的替代解释

- 当前受体占据差异尚未洗脱；
- 短时 CheY-P 或 CheA 状态残留；
- 马达适应或机械迟滞；
- 一般代谢状态变化；
- 外部梯度没有真正匹配；
- 细胞年龄、表达水平或受体比例差异。

### 8.3 不允许升级

即使达到 HEF-3，也不能直接推出：

- 长期学习；
- 规则层 HEF-4；
- L₂；
- 自我模型；
- 主体连续性；
- 自由意志；
- 道德地位。

本案例的“memory”是一个具体生化控制变量，不是对所有生命历史的统一解释。

---

## 9. 预注册的同事件综合实验

为了检验 B₃ 是否可达到 `SEA-3 qualified`，需要在同一细胞事件中闭合五门。

### 9.1 事件单元

```text
单个 E. coli 细胞
进入稳定微流控梯度
→ 记录 20 分钟导航
→ 在不丢失细胞身份的情况下进入匹配探针阶段
→ 记录后续响应和维持变量 40–60 分钟
```

禁止把不同批次细胞的信号、轨迹、代谢和后续响应拼接为同一事件。

### 9.2 实验组

至少包含：

1. wild type；
2. `cheR cheB` 双缺失或等价适应缺陷株；
3. 受体甲基化位点缺陷株；
4. 马达耦合缺陷或非运动对照；
5. 均匀环境对照；
6. 非代谢型吸引物梯度；
7. 可代谢营养梯度；
8. 梯度方向反转／历史重置条件。

### 9.3 同事件测量

| SEA 门 | 同事件读数 |
|---|---|
| DMF | 单细胞轨迹上的实际配体浓度时间序列 |
| NER | 受体／CheA／CheY FRET 或等价内部信号；适应介质干预 |
| PEF | run／tumble、马达切换、漂移速度和现实空间可达路径 |
| CBP | ATP、质子动力势、营养摄取、生长、损伤或后续行动能力中的预注册指标 |
| HEF | 在当前浓度和状态匹配后，标准探针对未来响应、切换门槛和返回成本的影响 |

### 9.4 关键反事实

#### T1 · 切断执行通道

内部信号保留，但马达耦合失效：

```text
NER 高
PEF 低
SEA 不得超过 1／2
```

#### T2 · 非代谢型吸引物

空间迁移保留，但维持收益缺失：

```text
PEF 高
CBP 可能失败
SEA 不得由方向性补偿
```

#### T3 · 甲基化缺失

即时刺激响应保留，时间比较与后续路径组织下降：

```text
NER-1／2 可保留
HEF-3 失败或降级
```

#### T4 · 当前状态匹配

将细胞放到相同当前配体、能量和马达状态，再测试历史差异：

```text
若历史效应消失
→ 只能是 HEF-1／2
```

#### T5 · 资源结果解耦

两条路径到达不同位置，但最终营养摄取、ATP、生长或损伤无差异：

```text
PEF-3 可成立
CBP-2 失败
SEA-3 失败
```

### 9.5 预注册判定

只有同时满足：

```text
DMF-2+
NER-2+
PEF-2+
CBP-2+
HEF-3+
```

并且证据属于同一细胞、同一冻结事件和相容时间尺度，才允许：

```text
B₃ = SEA-3 qualified
```

即使达到该结果，也只允许称：

> 单细胞—局部环境边界中的有界选择事件候选。

不得称：

- 细菌具有反思主体性；
- 细菌具有自由意志；
- 趋化证明意识；
- 受体甲基化等于 L₂；
- SRT 已发现控制论之外的新机制。

---

## 10. 与普通理论的区分测试

### 10.1 当前可由普通理论解释的内容

- temporal comparison；
- receptor adaptation；
- integral feedback；
- motor actuation；
- biased random walk；
- resource allocation；
- fitness benefit；
- phenotypic heterogeneity。

### 10.2 SEA 当前可能增加的约束

SEA 不提供新的生化方程，但增加以下报告纪律：

1. 不能把受体差异响应当作完整选择；
2. 不能把马达切换当作已完成环境路径；
3. 不能把运动耗能当作路径特异承受；
4. 不能把甲基化存在当作 HEF-3；
5. 不能把群体适合度当作单细胞即时 stake；
6. 不能跨论文拼接五门；
7. 不能因为对象是生命系统就降低任何门槛。

### 10.3 独立机制判据

若未来实验只复现控制论已经预测的结果，最强结论仍是：

> SEA 是一种更严格的跨层级审计与证据组织框架。

只有当 SEA 导出普通模型未包含、且经预注册验证的额外差异，例如：

- 在控制所有标准状态变量后，CBP 位置结构仍预测不同历史写回；
- 同等控制性能下，只有承受位置闭合的系统出现特定可达性重组；
- 五门不可补偿原则产生优于替代分类的跨域预测；

才可讨论 SRT 的独立经验增量。

本报告不声称这些结果已经出现。

---

## 11. 本轮对统一协议的压力结果

### 11.1 得到支持的纪律

- 同一事件规则在生命系统中同样必要；
- tethered actuator 与自由空间路径必须分开；
- 运动成本与路径特异后果必须分开；
- 位置积累与维持收益必须分开；
- 短时适应记忆与规则写回必须分开；
- 群体适合度与单细胞事件必须分边界报告。

### 11.2 暴露出的薄弱点

#### CBP 的生命测量接口仍不足

CBP-2 需要更明确说明：

- 正向资源获得是否属于“后果承载”；
- 只改变未来机会而未产生当前损失时如何判定；
- 细胞维持变量应使用哪些最小读数；
- 群体收益如何分配到个体边界。

本报告不修改 CBP 协议，只登记这些为实验接口问题。

#### HEF 的短时门槛需领域预注册

秒级甲基化记忆可能足以改变未来 run／tumble，但：

- 对细菌导航是相关历史；
- 对跨代组织不是；
- 时间尺度必须在实验前固定。

#### SEA-2 内部异质性很大

以下过程都可能落在 SEA-2：

- tethered motor switch；
- 自由迁移但无 CBP 测量；
- 有细胞后果但历史门失败。

当前不建议新增大量子等级；应在报告中保留逐门向量。

### 11.3 是否修改统一协议

本轮不建议修改 SEA、NER、PEF、CBP 或 HEF 正文。

更合适的下一步是：

> 先执行同细胞综合实验设计或寻找已经同时测量信号、轨迹、代谢／生长和后续响应的数据集，再判断 CBP 与 HEF 是否需要领域附录。

---

## 12. 最终判定

### 12.1 对趋化机制的判定

```text
内部非等价登记：有强实验支持
现实路径效力：有强实验支持
短时历史效力：有强候选支持
后果承载位置：标准实验中不足
跨论文同一事件闭合：不成立
```

### 12.2 SEA 结论

```text
标准 tethered-cell 事件：SEA-2 upper bound
标准梯度迁移事件：SEA-2 strong
跨文献综合：不得赋予单一 SEA 等级
未来同细胞综合事件：SEA-3 qualified 可检验，尚未建立
```

### 12.3 理论意义

本案例表明：

> SEA 不是把具有反馈、运动和记忆的生命系统自动称为选择结构。相反，它在一个经典、机制清晰的生物控制系统中产生了实质性降级：NER、PEF 和 HEF 的强证据不能补偿 CBP 与同事件闭合的缺失。

这构成 SEA 跨出软件事务语言的第一项有用结果，但仍属于审计区分，不是独立因果机制发现。

---

## 13. 主要证据来源

以下均作为机制和实验设计证据使用，不作为 SRT 定义来源。

1. Segall JE, Block SM, Berg HC. **Temporal comparisons in bacterial chemotaxis.** *PNAS* 1986;83(23):8987–8991. DOI: `10.1073/pnas.83.23.8987`. PMID: `3024160`.
2. Hazelbauer GL, Park C, Nowlin DM. **Adaptational crosstalk and the crucial role of methylation in chemotactic migration by Escherichia coli.** *PNAS* 1989;86(5):1448–1452. DOI: `10.1073/pnas.86.5.1448`. PMID: `2646634`.
3. Stock-related gradient study. **Reversible receptor methylation is essential for normal chemotaxis of Escherichia coli in gradients of aspartic acid.** PMID: `2829179`.
4. Levit MN, Stock JB. **Receptor methylation controls the magnitude of stimulus-response coupling in bacterial chemotaxis.** *J Biol Chem* 2002;277(39):36760–36765. DOI: `10.1074/jbc.M204325200`. PMID: `12119291`.
5. Shimizu TS et al. **Chemotactic response and adaptation dynamics in Escherichia coli.** *PLoS Comput Biol* 2010;6:e1000784. DOI: `10.1371/journal.pcbi.1000784`. PMID: `20502674`.
6. Fukuoka／Ishijima group. **Direct imaging of intracellular signaling components that regulate bacterial chemotaxis.** *Science Signaling* 2014. DOI: `10.1126/scisignal.2004963`. PMID: `24692593`.
7. Ni B et al. **Growth-rate dependent resource investment in bacterial motile behavior quantitatively follows potential benefit of chemotaxis.** *PNAS* 2020;117(1):595–601. DOI: `10.1073/pnas.1910849117`. PMID: `31871173`.
8. Liu W et al. **Chemotaxis as a navigation strategy to boost range expansion.** *Nature* 2019;575:658–663. DOI: `10.1038/s41586-019-1733-y`. PMID: `31695195`.

---

## 14. 一句话总结

> **大肠杆菌可以登记差异、改变运动路径并以甲基化携带短时历史；但在同一事件中没有测得路径特异的细胞维持后果时，生命、运动、适应和记忆仍不足以把趋化自动升级为 `SEA-3`。**
