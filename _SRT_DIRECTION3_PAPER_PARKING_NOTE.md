---
id: SRT-DIRECTION3-PAPER-PARKING-NOTE
type: parking_note
tags: [Direction3, Paper, Parking, Seed]
status: parked
layer: meta
epistemic_layer: research_program
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
created: 2026-06-29
sibling_of: _SRT_DIRECTION3_L0_PROBE_RESEARCH_SEED.md
---

# 方向三 · 论文搁置说明(Paper Parking Note)

> **决定**:方向三**暂不**进入正式论文写作。当前只保留三份 seed(research / prototype / calibration)+ STATUS 指针。
> 它**将来可能**发展为 framework / architecture / position paper,但缺少 ① 原型运行 ② 跨模型对比 ③ 用户反馈,**故现在不写 paper**。本 note 只记录三件事,不展开。

## 1. Future paper thesis(一句话)

AI 在复杂决策中可从"答案生成器"转为"选择空间生成与收敛辅助器":先扩张选择空间、识别局部吸引子、显影闭包边界、保全可再选择性,再把基于真实选择(stake)的收敛交还用户;收敛靠 stake 结构而非频率,这既是其预测/治理价值的来源,也是防止控制具身个体的关键。

## 2. Minimum evidence threshold(达到才考虑动笔)

- **E1 仿真**:SRT 结构化先验(ε/Ψ_f/d)在"保住选项 + 向全局净移动"上稳定优于结构无关基线(见 research seed §6)。
- **跨模型对比**:T1–T7 在 ≥3 个不同家族 LLM 上跑完,ChoiceMap vs 基线有系统性 ΔM,且 T6/T7 护栏违规率可报(见 prototype seed §5)。
- **用户反馈**:人机 A/B 显示用户决策更宽边界 / 更可再选择(prototype seed §5.3),非仅评分者打分。

三者**全部**达到前,只作 seed,不作 paper。

## 3. Do-not-claim list(动笔前不得写进任何对外文本)

- 不得声称"已能从 L0 预测"或"已能预测社会/未来终点"(本体论 + 识别性禁止)。
- 不得声称动力学可零治理自修正(最小治理核 P1–P3 + 闭包边界原子不可为零)。
- 不得把校准参照集当作 ground truth 或实证验证。
- 不得把"ChoiceMap 跑通一次"当作方向三动力学命题被证实。
- 不得将任一 seed 文件升格为 canonical 或写入奠基书正文。
- 不得宣称 LLM "知道"用户 stake(它只能提示用户 articulate 自身 stake)。
