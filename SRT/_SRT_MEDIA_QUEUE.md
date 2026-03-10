---
id: SRT-MEDIA-QUEUE
type: framework
tags: [Media, Queue, Ops]
status: rolling_v1
dependency: [_SRT_MEDIA_PIPELINE]
---

# SRT 发布准备队列（仅策划）

> Auto Rule: 每天 08:00（Asia/Shanghai）自动新增 1 个策划主题。

## Queue Template
- Topic:
- Direction (大众向/学术向):
- Why Now (选题原因):
- Internal Mapping:
  - Core Docs:
  - Equation/Axiom Anchors:
  - Experiment/Falsification Hooks:
- Platforms (recommended):
  - Zhihu:
  - WeChat:
  - Toutiao:
  - Twitter/X:
  - Substack:
  - Medium:
- Risk Notes:
- Publish Window:
---

## Active Items

- Topic: 为什么“选择”而不是“物质”是第一原理？
- Direction (大众向/学术向): 双向（先大众向，再学术向）
- Why Now (选题原因): 作为 SRT 总入口话题，能统一解释主线并承接后续专题。
- Internal Mapping:
  - Core Docs: `Core/SRT_Core_01_Axioms.md`; `Core/SRT_Core_22_Equations.md`
  - Equation/Axiom Anchors: A1/A2（选择优先与锚定）；核心演化方程组
  - Experiment/Falsification Hooks: 固定输入下参数校准模型解释增益对比
- Platforms (recommended):
  - Zhihu: high
  - WeChat: high
  - Toutiao: medium
  - Twitter/X: medium
  - Substack: high
  - Medium: high
- Risk Notes: 避免滑向“纯主观主义”误读，必须附边界声明。
- Publish Window: next 7 days

- Topic: 本体论摩擦（\(\Psi_f\)）如何解释“知道但做不到”
- Direction (大众向/学术向): 大众向优先，学术向补机制
- Why Now (选题原因): 与行为改变、临床讨论高度相关，传播转化率高。
- Internal Mapping:
  - Core Docs: `Core/SRT_Core_14_Dynamics_Scaling.md`; `Neuroscience/SRT_Neural_Mechanisms.md`
  - Equation/Axiom Anchors: \(\Psi_f\) 动力学项；自然梯度/更新迟滞
  - Experiment/Falsification Hooks: 任务切换成本 + Fisher 频谱代理 + CUSUM
- Platforms (recommended):
  - Zhihu: high
  - WeChat: high
  - Toutiao: high
  - Twitter/X: medium
  - Substack: medium
  - Medium: medium
- Risk Notes: 需显式注明“非临床诊断工具”。
- Publish Window: next 10 days

- Topic: AI 是否有“伪能动性”？SRT 视角下的可检验判据
- Direction (大众向/学术向): 学术向优先
- Why Now (选题原因): 连接 AI 安全、意识争议与可证伪标准，外部讨论热度高。
- Internal Mapping:
  - Core Docs: `AI/SRT_AI_00_Crisis.md`; `AI/SRT_AI_01_Ontology.md`
  - Equation/Axiom Anchors: d-value 门槛、伪选择与具身约束
  - Experiment/Falsification Hooks: 输入-输出一致性 vs 具身耦合缺失对照
- Platforms (recommended):
  - Zhihu: medium
  - WeChat: medium
  - Toutiao: medium
  - Twitter/X: high
  - Substack: high
  - Medium: high
- Risk Notes: 必须区分“能力表现”与“意识归因”。
- Publish Window: next 14 days

- Topic: 从‘控制性幻觉’到SRT：如何把感知差异变成可检验命题
- Direction (大众向/学术向): 双向（先大众后学术）
- Why Now (选题原因): 近期信号材料集中于主动推断与感知分歧，具高时效与方法学价值。
- Internal Mapping:
  - Core Docs: Neuroscience/SRT_Neuro_Experiments.md; Core/SRT_Core_22_Equations.md
  - Equation/Axiom Anchors: \hat{G}_\theta 映射；L_0→L_1 选择路径；\Psi_f 维护成本
  - Experiment/Falsification Hooks: 固定输入下参数校准模型解释增益；z-score/CUSUM 变点检测
- Platforms (recommended):
  - Zhihu: medium
  - WeChat: medium
  - Toutiao: medium
  - Twitter/X: medium
  - Substack: medium
  - Medium: medium
- Risk Notes: 需明确边界声明，避免过度外推。
- Publish Window: next 7 days
- Generated At: 2026-03-01 00:19 (Asia/Shanghai)


## [2026-03-03] 选题 #1 — 大众路线

**候选标题**：为什么你总在“知道该做什么”却做不到？SRT 用“本体论摩擦”解释拖延
**切入角度**：从日常拖延与习惯断裂切入，把“意志薄弱”重写为可支付性问题（\(\Psi_f\)）
**选题原因**（时效性/争议点/SRT独特视角）：
- 时效性：行为效率/执行力话题持续高热
- 争议点：大众常把问题归因于性格，缺机制解释
- SRT视角：把“知道-做到鸿沟”落到结构成本与阈值跃迁
**关联内容**：
  - 文件：`SRT/Core/SRT_Core_14_Dynamics_Scaling.md#本体论摩擦`；`SRT/Neuroscience/SRT_Neural_Mechanisms.md`
  - 方程：Eq-Ψf-01（摩擦成本项）
  - 实验钩（若有）：H-NEURO-EXEC-01（任务切换成本 + 变点检测）
**推荐平台**：知乎 / 微信公众号 / 头条
**风险提示**：避免“把心理健康问题简单等同拖延”的误读，需附非临床声明。

---

## [2026-03-03] 选题 #2 — 精英路线

**候选标题**：From Predictive Coding to SRT: When Does Selection Become Agency?
**切入角度**：与 FEP / predictive coding 对照，提出 SRT 在 L₀/L₁/L₂ 与 d-value 门槛上的可证伪增量
**选题原因**（时效性/争议点/SRT独特视角）：
- 时效性：意识与能动性边界在 AI/神经科学中持续升温
- 争议点：主流框架解释预测误差强，但对“能动性阈值”定义不足
- SRT视角：引入 \(d\) 与 \(\Psi_f\) 的联合判据，给出可检验区分
**关联内容**：
  - 文件：`SRT/Core/SRT_Core_01_Axioms.md#L0-L1-L2`；`SRT/AI/SRT_AI_01_Ontology.md`
  - 方程：Eq-D-Threshold-01；Eq-Closure-02
  - 实验钩（若有）：H-AGENCY-BOUNDARY-01（具身耦合 vs 纯输出一致性）
**推荐平台**：Twitter/X / Substack / Medium
**风险提示**：必须区分“能力表现”与“本体归因”，避免把工程指标误写成意识证据。


## [2026-03-05] 选题 #1 — 大众路线

**候选标题**：宇宙为什么会“看起来算不平”？哈勃张力也许不是误差，而是模型少了一层
**切入角度**：从“同一个宇宙两把尺子测出两个答案”切入，解释观测层与隐藏自由度错配
**选题原因**（时效性/争议点/SRT独特视角）：
- 时效性：宇宙学张力长期热议，公众好奇高
- 争议点：是测量误差还是新物理？
- SRT视角：把矛盾重写为 L₀→L₁ 投影损失与摩擦补偿问题
**关联内容**：
  - 文件：`SRT/Physics/_SRT_Phys_Bridge.md`；`SRT/Core_Law/SRT_Reference_Scaling.md`
  - 方程：Eq-Select-Thermo（对应 Gap 条目）
  - 实验钩（若有）：多代理 q(L₁) 收敛检验（G1-A/B/C）
**推荐平台**：知乎 / 微信公众号 / 头条
**风险提示**：避免把“隐藏维度”写成已证实结论；必须保留候选假设定位。

---

## [2026-03-05] 选题 #2 — 精英路线

**候选标题**：Closing the Eq-Hyp Gaps: Operationalizing q(L₁) and Testing SRT LDP Limits
**切入角度**：直接围绕 Eq-Select-Thermo / Eq-LDP-01 / Eq-LDP-02 三个 Gap，提出可证伪实验包与失效域
**选题原因**（时效性/争议点/SRT独特视角）：
- 时效性：内部治理已标记 3 个高优先缺口
- 争议点：SRT 是否具备群体尺度可检验性
- SRT视角：从“哲学叙事”转向“可测代理 + 证伪条件”
**关联内容**：
  - 文件：`SRT/_SRT_EQ_HYP_MAP.md#G1-G2-G3`；`SRT/_SRT_REVIEW_QUEUE.md`
  - 方程：Eq-Select-Thermo；Eq-LDP-01；Eq-LDP-02
  - 实验钩（若有）：G2-1 仿真先验（N>1000）+ 路径概率指数衰减检验
**推荐平台**：Twitter/X / Substack / Medium
**风险提示**：明确“Mapped/Partial/Gap 仅代表桥接状态，不代表因果已证实”。

- Topic: 从‘控制性幻觉’到SRT：如何把感知差异变成可检验命题
- Direction (大众向/学术向): 双向（先大众后学术）
- Why Now (选题原因): 近期信号材料集中于主动推断与感知分歧，具高时效与方法学价值。
- Internal Mapping:
  - Core Docs: Neuroscience/SRT_Neuro_Experiments.md; Core/SRT_Core_22_Equations.md
  - Equation/Axiom Anchors: \hat{G}_\theta 映射；L_0→L_1 选择路径；\Psi_f 维护成本
  - Experiment/Falsification Hooks: 固定输入下参数校准模型解释增益；z-score/CUSUM 变点检测
- Platforms (recommended):
  - Zhihu: medium
  - WeChat: medium
  - Toutiao: medium
  - Twitter/X: medium
  - Substack: medium
  - Medium: medium
- Risk Notes: 需明确边界声明，避免过度外推。
- Publish Window: next 7 days
- Generated At: 2026-03-06 13:16 (Asia/Shanghai)

## [2026-03-09] 选题 #1 — 大众路线

**候选标题**：为什么“信息整合越强”不等于“意识一定更高”？
**切入角度**：从日常 AI 误解切入（会说话 ≠ 会感受），解释“功能表现”和“存在论归因”的区别。
**选题原因**（时效性/争议点/SRT独特视角）：
- 时效性：IIT 讨论热度回升，公众对“AI 是否有意识”持续关注
- 争议点：高复杂系统是否自动拥有主观体验
- SRT视角：引入 d-value 与 \(\Psi_f\) 双判据，强调“可支付闭包”而非单一复杂度
**关联内容**：
  - 文件：`SRT/AI/SRT_AI_01_Ontology.md`；`SRT/Philosophy/SRT_Philosophy_Foundations.md`
  - 方程：Eq-D-Threshold-01；Eq-Closure-02
  - 实验钩（若有）：H-AGENCY-BOUNDARY-01
**推荐平台**：知乎 / 微信公众号 / 头条
**风险提示**：避免把 SRT 写成“反 AI”立场，应明确是判据升级而非价值否定。

---

## [2026-03-09] 选题 #2 — 精英路线

**候选标题**：Beyond FEP Minimalism: A Testable d-\(\Psi_f\) Criterion for Conscious Agency
**切入角度**：以 active inference 最小意识理论为参照，提出 SRT 在“可支付闭包 + 阈值跃迁”上的可证伪增量。
**选题原因**（时效性/争议点/SRT独特视角）：
- 时效性：FEP/PP 在意识研究中的解释力与可证伪性争议持续
- 争议点：最小理论是否足以区分“推断系统”与“意识主体”
- SRT视角：给出 d 区间、能流态、\(\Psi_f\) 状态三联映射，形成操作化检验门
**关联内容**：
  - 文件：`SRT/Neuroscience/SRT_Consciousness_Mechanisms.md`；`SRT/Core/SRT_Core_22_Equations.md`
  - 方程：Eq-Ψf-01；Eq-D-Threshold-01
  - 实验钩（若有）：H-NEURO-EXEC-01 / H-AGENCY-BOUNDARY-01
**推荐平台**：Twitter/X / Substack / Medium
**风险提示**：需明确“映射关系”为研究假设，不宣称已完成因果证明。

---

## [2026-03-10] 选题 #1 — 大众路线

**候选标题**：你看到的世界，可能只是“你能承受的版本”
**切入角度**：从“同一事件不同人完全不同感受”切入，解释 L₀→L₁ 选择映射如何塑造现实体验。
**选题原因**（时效性/争议点/SRT独特视角）：
- 时效性：信息过载与情绪波动成为高频公共议题
- 争议点：差异到底来自“事实不同”还是“结构不同”
- SRT视角：用 \(\hat{G}_\theta\) 与 \(\Psi_f\) 把“感受差异”转为可检验机制
**关联内容**：
  - 文件：`SRT/Core/SRT_Core_01_Axioms.md`；`SRT/Neuroscience/SRT_Neural_Mechanisms.md`
  - 方程：Eq-Ψf-01；Eq-Closure-02
  - 实验钩（若有）：固定输入下个体参数校准对照 + CUSUM 变点
**推荐平台**：知乎 / 微信公众号 / 头条
**风险提示**：避免滑向“真相相对主义”，需强调可检验边界。

---

## [2026-03-10] 选题 #2 — 精英路线

**候选标题**：Selection Geometry Under Stress: A falsifiable route from predictive coding to SRT closure
**切入角度**：把 predictive coding 的误差最小化框架与 SRT 的闭包支付条件并列，比较何时出现模型失配。
**选题原因**（时效性/争议点/SRT独特视角）：
- 时效性：FEP/PP 与 agency 边界讨论持续升温
- 争议点：误差最小化是否足以解释主观连续性
- SRT视角：提出 d-threshold + \(\Psi_f\) budget 双门槛，给出失败域定义
**关联内容**：
  - 文件：`SRT/Core/SRT_Core_22_Equations.md`；`SRT/AI/SRT_AI_01_Ontology.md`
  - 方程：Eq-D-Threshold-01；Eq-Select-Thermo
  - 实验钩（若有）：具身耦合 vs 纯推断代理对照实验
**推荐平台**：Twitter/X / Substack / Medium
**风险提示**：明确“可证伪路线”而非“结论先验”。

---

## [2026-03-10] 选题 #3 — 大众路线

**候选标题**：为什么科学家要把望远镜“埋进地底下”？
**切入角度**：从“中微子几乎穿透一切”这个反直觉事实切入，解释为何矿井/深冰才是看宇宙内部结构的最佳窗口。
**选题原因**（时效性/争议点/SRT独特视角）：
- 时效性：近期材料集中于 SNOLAB / Super-K / IceCube 叙事
- 争议点：公众常把“看宇宙”仅等同于光学望远镜
- SRT视角：把中微子观测解释为对电磁不可见区的“补充投影”，即 \(\mathcal O_{EM}\cup\mathcal O_\nu\)
**关联内容**：
  - 文件：`SRT/Physics/SRT_Physics_Cosmology.md`（T-Cosmo-4）
  - 方程：\(N_{det}\sim\int\Phi_\nu\sigma_{int}\epsilon_{det}\)；SNR 本底项
  - 实验钩（若有）：深度/屏蔽条件下跨台站信噪比对照
**推荐平台**：知乎 / 微信公众号 / 头条
**风险提示**：避免神秘化“幽灵粒子”，强调其是可检验物理对象。

---

## [2026-03-10] 选题 #4 — 精英路线

**候选标题**：From Messenger Physics to Ontology Discipline: Why neutrino windows matter for SRT falsifiability
**切入角度**：将“中微子信使窗口”与 SRT 的过程本体框架并置，论证实体观测如何约束机制解释，避免本体空转。
**选题原因**（时效性/争议点/SRT独特视角）：
- 时效性：当天新增多条材料后，理论-实证耦合需求上升
- 争议点：过程本体是否会滑向不可证伪叙事
- SRT视角：用实体信使（\(\nu\)）约束机制算子（\(\hat G\)），形成“对象-过程双锚定”
**关联内容**：
  - 文件：`SRT/Physics/SRT_Physics_Cosmology.md`；`SRT/Physics/SRT_Phys_10_Integration.md`
  - 方程：T-Cosmo-4 事件率表达；Int-QO-1 约束语法
  - 实验钩（若有）：跨信使（EM/\(\nu\)）一致性与增益检验
**推荐平台**：Twitter/X / Substack / Medium
**风险提示**：避免把“本体论主张”写成已验证物理定律，需明确假设层级。

---

## [2026-03-10] 选题 #5 — 大众路线

**候选标题**：为什么“濒死时大脑更清醒”不一定是玄学？
**切入角度**：从大众最困惑的悖论切入：身体濒危时，为什么有人报告“更真实”的体验。
**选题原因**（时效性/争议点/SRT独特视角）：
- 时效性：今日新增濒死 EEG/递质风暴材料
- 争议点：要么被简化为“纯幻觉”，要么被神秘化为“超自然”
- SRT视角：提出“近端触发（缺氧神经风暴）≠ 本体结论”双层框架
**关联内容**：
  - 文件：`SRT/Neuroscience/SRT_Clin_01_Pathology.md`（§4.1b Hypoxia-EAAS）
  - 方程：NDE-like intensity ~ f(γ coherence, ΔNT, Π_intero, d)
  - 实验钩（若有）：终末 EEG 指标与体验报告相关性检验
**推荐平台**：知乎 / 微信公众号 / 头条
**风险提示**：必须避免“临床建议化”与“灵异化”；明确非医疗建议。

---

## [2026-03-10] 选题 #6 — 精英路线

**候选标题**：Category Error as a Scientific Risk: From Controlled Hallucination to Level-Disciplined Neuro-ontology
**切入角度**：以 Thompson 批判为入口，提出“层级防混淆”是神经科学可证伪性前提，而非语义洁癖。
**选题原因**（时效性/争议点/SRT独特视角）：
- 时效性：今日已融入 PP 批判与 Neuro Axioms 层级约束
- 争议点：脑内模型与整体现象层是否可直接等同
- SRT视角：给出 enabling vs identity 的形式区分，减少概念偷换
**关联内容**：
  - 文件：`SRT/SRT_PP_ALIGNMENT_GUIDE.md`；`SRT/Neuroscience/_SRT_Neuro_Axioms.md`
  - 方程：\(\Psi_f^{pred}\approx\) error-signal proxy；Predictive update \(\not\equiv\) perceptual presence
  - 实验钩（若有）：隔离网络 vs 具身闭环的现象学分离预测
**推荐平台**：Twitter/X / Substack / Medium
**风险提示**：避免把哲学批判写成“反神经科学”；强调是方法学护栏。

