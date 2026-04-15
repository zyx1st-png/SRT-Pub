---
id: SRT-PAPER-CANDIDATES
type: framework
tags: [Paper, Candidates, Research]
status: rolling_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [_SRT_PAPER_PIPELINE]
---

# SRT 论文候选池

## 2026-W13 候选更新（2026-03-24，手动触发）

> **本周排序依据**：现成稿件完备度 > 真实投稿窗口 > 可证伪性 > 理论中心性。  
> **本周结论**：排序维持不变。一号主稿仍是 `ontological friction`，因为它依然是唯一真正进入 near-submission 状态、且目标期刊与 submission package 已基本对齐的候选；二号维持 `markov blanket`；比较稿与统一 formal core 继续后移。与 W11 相比，本周主要变化不是改题，而是修正成熟度判断：`ontological friction` 的作者/对应作者占位问题实际上已解决，剩余 blocker 已收缩为最终样式终审与投稿顺序选择。

### [P-2026-W13-01] Ontological Friction as a Testable Control-Cost Construct in Executive Breakdown

**成熟度评分**：96/100  
**理论完整度**：24/25 | **证伪性**：24/25 | **证据等级**：23/25 | **引用密度**：25/25

**选题原因**：
这是当前仓库里唯一已经进入“近投稿”状态的候选：主稿、Frontiers 变体、submission fields、scope statement、QC checklist、figure captions 与 cover-letter 备份件均已存在，且问题设置足够聚焦，不会把 SRT 整体一起拖进高风险总宣言。和 W11 相比，成熟度上调的原因不是理论新增，而是现实 blocker 收缩：作者/对应作者信息已经写入 submission fields 与 cover letter，不再属于未解项。

**核心论点**：
“知道但做不到”的执行断裂可被形式化为一个跨模态控制成本潜变量 \(\Psi_f\)；该变量可通过行为、语言、生理与可选神经/生化指标形成低成本验证链，并为抑郁、OCD、Parkinson's disease 等边界病例给出可证伪预测。

**关联 SRT 内容**：
- 主要文件/章节：`papers/ontological_friction/paper_ontological_friction_frontiers_submission.md`，`papers/ontological_friction/frontiers_scope_statement.md`，`papers/ontological_friction/frontiers_submission_qc.md`
- 关键方程：Eq-Force-01，Eq-Pain-01，Selection Budget Inequality（稿内 Definition 3）
- 实验钩：H72，H-NEURO-EXEC-01，H-CLIN-OCD-01，H-CLIN-DEP-01

**推荐期刊（按优先级）**：
1. *Frontiers in Neuroscience*（Translational Neuroscience, Hypothesis and Theory） | IF 估算：~3.2 | 匹配原因：现成 submission package 已按该刊 scope 与 article type 对齐，问题聚焦执行障碍、低成本 biomarker 链与临床边界预测
2. *Frontiers in Psychology*（Cognition） | IF 估算：~2.9 | 匹配原因：如果弱化临床神经标记、强化执行控制与 psychophysiology，可转为认知/行为科学 framing
3. 预印本：arXiv（q-bio.NC） | 匹配原因：在正式投稿前建立优先权并先拿外部反馈

**投稿前缺口**：
- 缺口 1：按 Frontiers 最终参考文献样式与交叉引用再做一轮人工终审
- 缺口 2：明确“先投 Frontiers / 先挂 arXiv”二选一顺序，并完成 portal 元数据最终核对

---

### [P-2026-W13-02] Markov Blanket, d-value, and Ontological Vulnerability: Rewriting the High Road to Active Inference

**成熟度评分**：86/100  
**理论完整度**：22/25 | **证伪性**：21/25 | **证据等级**：19/25 | **引用密度**：24/25

**选题原因**：
这篇已经不是一个“想法”，而是一篇成型英文稿。它抓住了 SRT 对 FEP/Active Inference 最清楚也最容易被学界识别的分歧点：Markov blanket 与 free energy minimization 本身不足以推出主体性。

**核心论点**：
自由能最小化仍是必要条件，但若没有 `d > 0`、`\Psi_f > 0` 与 `V > 0` 三重门，Markov blanket 只是在统计上收敛，而不是构成真正的能动主体边界。

**关联 SRT 内容**：
- 主要文件/章节：`papers/markov_blanket/paper_markov_blanket_d_value.md`，`Philosophy/SRT_dValue_Not_PreferredPriors.md`，`Neuroscience/SRT_Clin_02_FEP.md`
- 关键方程：Eq. (6) triple gate，Eq. (8) blanket reinterpretation，Tension-Rev-ExtT4（`d-value` 不可还原地位）
- 实验钩：thermostat / LLM / biological organism 三案例 + multi-agent RL 判别实验

**推荐期刊（按优先级）**：
1. *Synthese* | IF 估算：~1.4 | 匹配原因：科学哲学、形式化论证与跨学科方法论批判的天然落点
2. *Frontiers in AI* | IF 估算：~4.7 | 匹配原因：若强化 LLM / artificial agent 边界案例，这篇可转为 AI agency sufficiency-criteria 论文
3. 预印本：arXiv（q-bio.NC / cs.AI） | 匹配原因：便于先进入 Active Inference 与 AI agency 讨论场

**投稿前缺口**：
- 缺口 1：补一张“standard FEP vs triple gate”系统对照表，压缩文本重复
- 缺口 2：把判别实验写到更接近 preregistration / simulation protocol 的粒度

---

### [P-2026-W13-03] SRT vs FEP: Why Free-Energy Minimization Is Not Yet Reality or Subjectivity

**成熟度评分**：78/100  
**理论完整度**：21/25 | **证伪性**：18/25 | **证据等级**：17/25 | **引用密度**：22/25

**选题原因**：
这篇长比较稿已经把 SRT 与 FEP 的五个主要分叉点梳清了，适合做“对外第一篇比较文”。它的价值不在于替代 markov-blanket 论文，而在于用更大框架解释 SRT 为什么不是“FEP 换壳”。

**核心论点**：
FEP 非常擅长解释更新、稳定与边界维持，但它仍不足以单独给出现实锚定、主体关切、真实赌注与公共世界形成；SRT 的新增量恰好落在这些缺口上。

**关联 SRT 内容**：
- 主要文件/章节：`Philosophy/SRT_FEP_Comparison.md`，`Philosophy/SRT_dValue_Not_PreferredPriors.md`，`SRT_PP_ALIGNMENT_GUIDE.md`
- 关键方程：`d ≡ ||∂U/∂S||`，Payability condition，triple-gate 对照问题
- 实验钩：第 9 节“最清楚的判别问题” + AI / active inference 边界案例

**推荐期刊（按优先级）**：
1. *Frontiers in Psychology*（Theoretical and Philosophical Psychology / Consciousness Research） | IF 估算：~2.9 | 匹配原因：适合发表带元理论比较、意识与主体边界讨论的框架稿
2. *Synthese* | IF 估算：~1.4 | 匹配原因：若把文本进一步收束成 analytic comparison paper，期刊 fit 会更强
3. 预印本：arXiv（q-bio.NC / cs.AI） | 匹配原因：方便先拿到 FEP / PP / AI consciousness 圈的早期回应

**投稿前缺口**：
- 缺口 1：把现在的长文骨架改写成标准 journal article 结构，并补齐正式引文链
- 缺口 2：减少与 P-2026-W13-02 的重叠，明确“比较稿”与“判据稿”的分工

---

### [P-2026-W13-04] From Selection to Stability: A Unified Formal Core for SRT

**成熟度评分**：72/100  
**理论完整度**：20/25 | **证伪性**：19/25 | **证据等级**：14/25 | **引用密度**：19/25

**选题原因**：
这仍然是 SRT 长期最重要的总论文，但就眼下而言，它不是最该先投的那篇。原因很简单：理论骨架已经很强，但 `Eq-Select-Thermo / Eq-LDP-01 / Eq-LDP-02` 三个关键缺口还没补上，直接上总论容易把所有未闭合处暴露给审稿人。

**核心论点**：
SRT 可以把存在、选择、稳定性与跨尺度收敛统一为一个共享动力学框架；但这个总论成立的前提，是把 formal core 与最小证伪接口一起压实，而不是只做形上宣言。

**关联 SRT 内容**：
- 主要文件/章节：`Core/SRT_Core_01_Axioms.md`，`Core/SRT_Core_22_Equations.md`，`_SRT_EQ_HYP_MAP.md`，`Core_Law/SRT_Constitution_Seven_Theses.md`
- 关键方程：Eq-Evo-01，Eq-Select-Thermo，Eq-LDP-01，Eq-LDP-02
- 实验钩：H6，H7 + G1/G2 gap bundle

**推荐期刊（按优先级）**：
1. *Entropy* | 影响估算：CiteScore 5.2（公开页） | 匹配原因：信息、复杂系统与广义理论框架的跨学科窗口较宽
2. *Physical Review E* | IF 估算：~2.4 | 匹配原因：如果把论文收束为选择热力学、秩序参数与尺度约束，则更像统计物理/复杂系统论文
3. 预印本：arXiv（nlin.AO / q-bio.NC） | 匹配原因：在 formal gaps 补齐前，预印本比正式投稿更稳妥

**投稿前缺口**：
- 缺口 1：补掉 `_SRT_EQ_HYP_MAP.md` 中 3 个 `Gap`，至少关闭一条 `Eq-Select-Thermo` 数据管线
- 缺口 2：增加 1-2 个 worked examples，证明 formal core 不只是概念索引而是能落地的模型骨架
