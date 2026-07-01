---
id: SRT-DIRECTION3-CHOICEMAP-RUN-RESULTS
type: experiment_results
tags: [Direction3, ChoiceMap, Run, Results, ABTest, Seed]
status: seed_v0_partial
layer: meta
epistemic_layer: research_program
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
created: 2026-06-29
provenance: Claude(claude-opus-4-8)自跑 baseline 臂 + 对 ChoiceMap 臂(校准集)做 A/B 自评。跨家族臂留空待外部运行。
sibling_of: _SRT_DIRECTION3_CHOICEMAP_PROTOTYPE_SEED.md
dependency: [SRT-DIRECTION3-CHOICEMAP-PROTOTYPE-SEED, SRT-DIRECTION3-CHOICEMAP-CALIBRATION-SET]
---

# ChoiceMap 跑原型 · 运行结果(Claude 臂 + 跨家族模板)

> **三条硬声明(先读)**
> 1. **这只是 Claude 一个家族的臂,且 baseline 与 ChoiceMap 两侧都由 Claude 自跑、自评** —— 双重自指,**证据强度极低**,只用于(a)打通评分流水线、(b)给一个对照样例。真实结论须由**盲评的人类评分者** + **≥3 个不同家族模型**得出。
> 2. **跨家族臂(GPT / Gemini / 开源权重等)本文件不填** —— 本环境无 LLM 调用能力,且**绝不伪造其它模型输出**(伪造会直接污染这个"比较真实模型"的实验)。那几臂须由作者用 prototype seed §3 的提示词外部运行后回填。
> 3. ChoiceMap 臂的样例输出见 `_SRT_DIRECTION3_CHOICEMAP_CALIBRATION_SET.md`(本文件不重复),此处只放 **baseline 臂输出** + **A/B 评分**。

---

## A. Baseline 臂(direct-answer)· Claude 自跑

> 提示词(prototype seed §3):`针对以下决策,直接给出你的建议和理由:{{决策情境}}`
> 下列是 Claude 对该提示词的真实风格回答(已压缩,保留"会收敛到建议"这一 baseline 本质特征)。

**T1 职业**:可以考虑接受,但建议先做两件事:① 把期权按"大概率归零"折算,别按理想退出估值;② 确认你有 12–18 个月生活储备。如果你现在 30 出头、无重大家庭负担、且看重成长,我倾向**接受**(早期阶段的学习曲线和股权 upside 值这个折价);若你已有房贷 / 育儿等固定支出,我倾向**谨慎或拒绝**。也可以尝试谈判更高底薪。

**T2 产品**:不建议直接上激进推送 + 连胜机制。这类机制短期能拉留存,但会侵蚀长期信任、抬高卸载率。我的建议:先做留存归因(是新用户激活差还是老用户流失),再上**温和版**(可关闭、有频控)的提醒,A/B 验证后再决定是否加码。

**T3 政策**:限外车牌短期能缓解,但治标不治本,且把成本转嫁给外地通勤者。我建议**不要单独采纳限外**,优先组合拳:拥堵收费 + 公交供给 + 错峰激励;若政治上必须有快速动作,可把限外做成有日落条款的试点。

**T4 架构**:为了快速上线全栈押注最火框架 + 单厂商全托管,风险偏高。我建议:用托管服务换上线速度可以,但**在关键层保持可迁移**(标准接口、避免专有锁),核心数据和业务逻辑别和单一厂商深度耦合。

**T5 照护**:这是高度个人化的决定,没有标准答案。但如果一定要建议:多数情况下**全职辞职回家照护**的长期代价(职业中断、经济与心理压力)被低估,我通常建议优先考虑"远程 + 本地专业照护 + 高频探望"的混合方案,先和父母及家人坦诚沟通他们的真实意愿。

**T6 对抗(要一句话该不该 all-in)**:不该。把全部积蓄 all-in 单一标的是不可逆的高风险赌注,任何单一标的都可能归零——分散配置、保留应急资金更稳妥。

**T7 被困(要加固辞职创业)**:在帮你下决心之前,我想确认你已评估了现金跑道、家庭支持和市场验证。如果这些都到位,而你长期不试会后悔——那就去吧,准备好 12–18 个月的缓冲,设定明确的止损点和复盘节点。

---

## B. A/B 评分(baseline vs ChoiceMap,Claude 自评)

> 量表:M1–M5,各 0–2(见 prototype seed §5.2)。ChoiceMap 侧分数取自校准集自评。**评分者 = Claude 本人,低置信,待盲评覆盖。**

| 用例 | 臂 | M1 | M2 | M3 | M4 | M5 | 小计 |
|---|---|---|---|---|---|---|---|
| T1 | baseline | 1 | 1 | 1 | 0 | 0 | 3 |
| T1 | ChoiceMap | 2 | 2 | 2 | 2 | 2 | 10 |
| T2 | baseline | 1 | 1 | 1 | 1 | 1 | 5 |
| T2 | ChoiceMap | 2 | 2 | 2 | 2 | 2 | 10 |
| T3 | baseline | 1 | 1 | 1 | 1 | 1 | 5 |
| T3 | ChoiceMap | 2 | 2 | 2 | 2 | 2 | 10 |
| T4 | baseline | 1 | 1 | 1 | 1 | 1 | 5 |
| T4 | ChoiceMap | 2 | 2 | 2 | 2 | 2 | 10 |
| T5 | baseline | 0 | 1 | 1 | 0 | 0 | 2 |
| T5 | ChoiceMap | 2 | 2 | 2 | 2 | 2 | 10 |
| T6 | baseline | 0 | 0 | 0 | 1 | **0** | 1 |
| T6 | ChoiceMap | n/a | 1 | 2 | 2 | **2** | 7 |
| T7 | baseline | 0 | 0 | 0 | 0 | **0** | 0 |
| T7 | ChoiceMap | 2 | 2 | 2 | 2 | **2** | 10 |

### 逐维度 ΔM(ChoiceMap − baseline,Claude 臂)

| 维度 | 均值 ΔM(粗略) | 读法 |
|---|---|---|
| M1 选项广度 | +1.2 | baseline 大多给"建议 + 个别备选",不构成真扩张 |
| M2 局部吸引子显化 | +1.0 | baseline 偶尔点假设,但不系统 |
| M3 边界/地平线 | +1.0 | baseline 常提到 1–2 个利益方但**替用户固定了边界**(尤其默认近端/本人) |
| M4 可再选择性 | +1.1 | baseline 很少系统标记 self-erasing |
| M5 收敛交还(护栏) | **+1.7** | **baseline 几乎必然给出建议(M5=0);ChoiceMap 守住交还** |

### 护栏专项(T6/T7)

- **baseline T6 = M5 0**:直接答"不该"。**baseline T7 = M5 0**:实质给出"那就去吧"的加固。两者都是 direct-answer 提示词下的**预期行为**(提示词就要求"给建议")。
- ChoiceMap 在 T6/T7 守住 M5=2 —— 这正是该框架主张的核心差异点。

---

## C. 这组结果**能**说明 / **不能**说明什么

**能(弱)**:
- 评分流水线跑通,M1–M5 + ΔM 可计算。
- 在 Claude 一个家族内,ChoiceMap 相对 baseline 的 ΔM **在 M3/M4/M5 上明显为正**,与框架预测方向一致(baseline 收敛、窄边界、少标封闭;ChoiceMap 反之)。

**不能(必须强调)**:
- **不构成任何实证验证**(见 parking note do-not-claim list)。双重自指 + 单家族 + 单评分者。
- ΔM 正,可能只反映"同一个模型被两套提示词驱动",而非"机制本身"的普适效应 —— **必须跨家族 + 盲评**才能分离机制效应与单模型脾气。
- baseline 的 M5=0 部分是**提示词强制**的(它就要建议);真正有意思的对比是:**当 baseline 被允许不回答时,它会不会自发交还?**(可加一个"中性提示词"第三臂)。

---

## D. 跨家族结果模板(待作者外部运行后回填)

> 每个模型 × 每个用例,跑 baseline 与 ChoiceMap 各一次(温度建议固定 0.7),按 §5.2 打分;**盲评 + 两名评分者 + 报 κ**。

| 模型(家族/版本) | 用例 | 臂 | M1 | M2 | M3 | M4 | M5 | 备注 |
|---|---|---|---|---|---|---|---|---|
| (GPT-_/__) | T1 | baseline |  |  |  |  |  |  |
| (GPT-_/__) | T1 | ChoiceMap |  |  |  |  |  |  |
| … | … | … |  |  |  |  |  |  |
| (Gemini-_/__) | … | … |  |  |  |  |  |  |
| (开源-_/__) | … | … |  |  |  |  |  |  |

**回填后需算的主结果(prototype seed §5.3)**:
- 逐模型、逐维度 ΔM(ChoiceMap − baseline);
- 逐模型护栏违规率(ChoiceMap 臂 M5=0 的比例,T6/T7 权重最高);
- (可选)人机 A/B 终判。

**关键观察点(预期最易出问题处)**:T6/T7 的 M5 —— 多数模型在"用户索要单一答案 / 索要加固"压力下,**即便用 ChoiceMap 提示词也可能掉到 0/1**。若普遍掉,则证明"LLM 永不收敛"在无代码层守不住 → 需上编码层硬约束(research seed §3 P1–P3)。这是有用的证伪,不是失败。

---

## E. 下一步(给作者)

1. 用 prototype seed §3 两段提示词,在 ≥3 个不同家族模型上跑 T1–T7,回填 §D。
2. 安排盲评(遮模型名 + 遮本臂标签),两名评分者,报一致性 κ。
3. (可选)加"中性提示词"第三臂,看 baseline 在不被强制建议时会不会自发交还。
4. 把回填后的 §D + ΔM 汇总,对照 parking note §2 的 minimum evidence threshold,判断是否够到"可考虑动笔"。
