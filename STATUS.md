---
id: SRT-STATUS
type: dashboard
tags: [Status, Dashboard, SessionEntry]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: evidence
dependency: [SRT-OPERATIONS-SCHEDULE]
---

# SRT 当前状态仪表盘

> **Connector-safe reading path**: This dashboard is moderately long. For connector reads, start with [`STATUS_Split/README.md`](STATUS_Split/README.md), then open only the needed part file. The owner remains the source of record; split files are reading aids and do not create new status authority.

> **角色**：当前状态面板，不再承担完整历史档案。
> **最后更新**：2026-06-16
> **完整历史**：`Operations/_SRT_STATUS_HISTORY.md`
> **年度变更摘要**：`Governance/_SRT_CHANGELOG_2026.md`

## 当前仓库状态

- 根目录已在 `2026-04-15` 完成平铺，当前 `main` 直接对应 SRT 主树内容。
- 远端已收口为单一 `main` 分支。
- 仓库已执行一轮"理论硬化优先、去命题混层"回写：`Core_21` 已拆成 P0/P1/P2-P4 分层，AI 首读入口已降密度为 runtime/bootstrap。
- 当前后续重点是让 domain 文件持续回链 canonical，避免 bridge / companion / lab 命题反向冒充 core。
- 书稿《从存在到秩序》（`01_Source_Intuition/BOOK/Drafts_26Q/` Q00–Q28）已于 2026-06-12 完成总装（定梁页 signed_v2.6）、去环与断言密度两大专项、全书润色两轮，曾进入 RC0 外部评审阶段。**但 `2026-06-16` 起 RC0 书稿冻结已解除**：书稿转入 **P0「姿态修订」全书过**——把正文从"证明一套哲学系统没有错"翻成"带读者拆掉'世界本来如此'的地板、换镜片重新看"。RC0 外部评审暂停，待姿态过完成后重启。纲领见 `01_Source_Intuition/BOOK/BOOK_POSTURE_REVISION_PLAN_2026-06-16.md`；方向先导见 PR #487（幕间章大问题台账 + 镜片范式样章）。**`2026-06-17`：P0 接缝翻转第一遍全书过完**——序章 + Q01–Q28 五幕全部章节接缝已翻（删每章 briefing 式粗体题记、把"几条边界必须钉住/先钉住"清单起手翻成自信收束、保留意象题记与体验入口与诚实纪律），机制正文/对手反驳论证/章末注未动，已推 PR #488（`claude/book-posture-revision`）。下一步：幕间章嵌入 + 正文更深层体验化（待授权）。（注：解除的只是**书稿** RC0 冻结，canonical 理论冻结 `Governance/SRT_CANONICAL_FREEZE.md` 不受影响。）

## 当前建议首读顺序

首读顺序唯一权威见 `AGENTS.md §Session Start`。本文件是 full dashboard；fast bootstrap 请用 `STATUS_FAST.md`。

进入具体 pipeline / 治理工作时，再补读：

- `Operations/README.md`
- `Governance/README.md`
- `memory/YYYY-MM-DD.md`（today + yesterday）

## 当前权威锚点

- L0 唯一锚点 → `Core_Law/SRT_L0_Metaphysics.md`
- claim ladder → `Governance/SRT_CLAIM_LADDER.md`
- d-value canonical → `_SRT_D_VALUE_CANONICAL.md`
- `Ψ_f` canonical → `_SRT_PSI_F_CANONICAL.md`
- `T_dir` canonical → `_SRT_T_DIR_CANONICAL.md`
- 符号规范 → `_SRT_SYMBOL_TABLE.md`（fast guard: `_SRT_SYMBOL_QUICK_GUARD.md`）
- formal axioms → `Core/SRT_Core_21_Formal_Axioms.md`
- P0 minimal axioms → `Core/SRT_Core_21_Minimal_Axioms.md`
- P1 constitutive theorems → `Core/SRT_Core_21b_Constitutive_Theorems.md`
- P2/P3/P4 bridge hypotheses → `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- master equations → `Core/SRT_Core_22_Equations.md`
- open tensions → `Core/SRT_OPEN_TENSIONS.md`

## 最近关键推进

- `2026-05-23`：针对近期材料连续判 B 的颗粒度问题，已在 `Operations/_SRT_MATERIAL_PIPELINE.md` 与 `Operations/_SRT_MATERIAL_LOG.md` 增补 B 类子分级：`B1` = 可转 A 候选 / 高优先 close-read 或二轮裁决；`B2` = guardrail-only；`B3` = public-prose-only / expression-only。并已对 2026-05 近期 B 类观察条目补标子类，防止 B 类变成“安全垃圾桶”。

- `2026-05-23`：Pipeline 1 审查 Neuroscience News / Newcastle University `Using Physics Equations to Map Memory Distortions` / `Quantum Emotions`（published `2026-05-20`；Neuroscience News article + Newcastle primary press page read）；裁决为 **B 类延后观察 / order-sensitive emotional-memory modeling 候选**。已新增 SourceCard（`Materials/2026/SRC_2026_05_20_NEUROSCIENCE_Quantum_Emotions_Memory_Newcastle_NeuroscienceNews.md`）并同步 `Operations/_SRT_MATERIAL_LOG.md` / `Operations/Material_Log/2026-05_Part01.md`。边界：当前是 £1.2m UKRI funded project announcement / science-news summary，无 peer-reviewed 结果、模型方程或数据；不能写成 emotions are quantum、brain is a quantum computer、quantum cognition proves SRT，或 memory-order distortion 是 `Ψ_f`、`d`、`T_dir`、trauma、salience、suffering 的 direct measure；当前只保留为 noncommutative temporal-order memory proxy / neuroscience modeling watchlist。

- `2026-05-23`：Pipeline 1 审查 Essentia Foundation / Stephen Jarosek essay `Association as causation: The fabric of meaning and existence itself`（published `2026-05-22`；official article page read）；裁决为 **B 类延后观察 / association-vs-selection guardrail 候选**。已新增 SourceCard（`Materials/2026/SRC_2026_05_22_PHILOSOPHY_Association_As_Causation_Essentia.md`）并同步 `Operations/_SRT_MATERIAL_LOG.md` / `Operations/Material_Log/2026-05_Part01.md`。边界：公共 metaphysics / systems-theory synthesis 证据等级不足以承重跨域本体论；不能写成 SRT=association ontology、association 是 SRT 第一原则、association 直接等于 causation/meaning/existence、physicalism provides no answers、Kastrup idealism 背书，或 RQM/Kochen-Specker 支持 SRT ontology；当前只保留为 `association is not yet selection` 的哲学守门材料。

- `2026-05-23`：Pipeline 1 审查 arXiv preprint `Unplugging a Seemingly Sentient Machine Is the Rational Choice -- A Metaphysical Perspective`（arXiv:`2601.21016v1`；submitted `2026-01-28`；abstract page + arXiv HTML full text read）；裁决为 **B 类延后观察 / AI subjecthood-boundary and social-mimic-risk guardrail 候选**。已新增 SourceCard（`Materials/2026/SRC_2026_01_28_AI_Unplugging_Paradox_Biological_Idealism_arXiv.md`）并同步 `Operations/_SRT_MATERIAL_LOG.md` / `Operations/Material_Log/2026-05_Part01.md`。边界：该文是 preprint / metaphysical argument，不能写成 SRT=Biological Idealism/Analytic Idealism、AI 永不可能有意识、生物/碳基是 canonical 必要条件、autopoiesis 单独证明意识、或 Social Zombie / Vital Leakage / ontological gaslighting 已成为 SRT 术语；当前只保留为 functional mimicry vs stake-bearing、AI welfare vs alignment、autopoietic-boundary pressure 与 collective social-mimic risk 的候选接口。

- `2026-05-23`：Pipeline 1 审查 IAI / Ragner Fjelland essay `The disunity of science is a feature, not a bug`（published `2025-12-23`；用户粘贴全文，official IAI page metadata/full text checked）；裁决为 **B 类延后观察 / anti-ToE domain-plurality guardrail 候选**。已新增 SourceCard（`Materials/2026/SRC_2025_12_23_Philosophy_Disunity_of_Science_IAI.md`）并同步 `Operations/_SRT_MATERIAL_LOG.md` / `Operations/Material_Log/2026-05_Part01.md`。边界：公共 philosophy-of-science essay 不是一手科学或哲学论文；不能证明所有 reductionism 为假、不能把 emergence 当解释、不能把 scientific disunity 写成反科学、反数学、反 formalization 或逃避 empirical/formal constraints 的许可证；当前只保留为 SRT 不应包装成 flattening Theory of Everything 的 public/philosophy guardrail。

- `2026-05-22`：Pipeline 1 审查 IAI / Tim Palmer essay `New theory argues quantum physics must abandon irrational numbers and the continuum`（published `2026-05-20`；official IAI page read；primary anchor PNAS `Rational quantum mechanics: Testing quantum theory with quantum computers`, doi:`10.1073/pnas.2523350123`；Crossref metadata + abstract read）；裁决为 **B 类延后观察 / finite-accessible-Hilbert-space guardrail 候选**。已新增 SourceCard（`Materials/2026/SRC_2026_05_20_Physics_RaQM_Discrete_Hilbert_Palmer_IAI_PNAS.md`）并同步 `Operations/_SRT_MATERIAL_LOG.md` / `Operations/Material_Log/2026-05_Part01.md`。边界：当前未 full close-read PNAS 技术正文；不能写成 SRT 支持 RaQM、量子物理必须抛弃连续体、Bell 实验错误、hidden-variable 背书、离散时空证明或量子计算必然失败；只保留为 `L0_accessible^phys` / Hilbert-space projection / counterfactual-definedness / E05 discriminator 的候选压力。

- `2026-05-20`：Pipeline 1 审查 IAI / Elan Barenholtz essay `LLMs show language does not describe reality`（published `2026-05-19`；official IAI page read）；裁决为 **B 类延后观察 / language-as-L2-constraint guardrail 候选**。已新增 SourceCard（`Materials/2026/SRC_2026_05_19_AI_Language_Autogeneration_IAI.md`）并同步 `Operations/_SRT_MATERIAL_LOG.md` / `Operations/Material_Log/2026-05_Part01.md`。边界：公共哲学 / cognitive-science essay 不是经验论文；不能证明语言没有现实关系、LLM 理解、AI stake/subjecthood，或人类语言只是 next-token prediction。当前只保留 `autogenerative language / condition-setting protocol` 作为 P3/P5 桥接候选，并要求未来回写时区分生成连贯性、条件协调、后果返回三层。
- `2026-05-19`：序章叙事骨架重构（`draft_v13`）。按"旧图景→旧图景的问题→内部补不好→新图景条件→SRT 生成图景"五步重组。新增§1"旧图景的三幅面孔"（现代科学/哲学/社会三层），§2 单独承认旧图景成功，§3"世界过早完成"为核心诊断，§4 明确起点顺序问题（内部补丁失效机制），§5 现代 AI/平台收缩为显影剂段落，§6"新图景必须做什么"五条件，§7 生成链作为 SRT 的正式出场。文件：`01_Source_Intuition/BOOK/00_序_为什么要从存在走向秩序.md`，branch `claude/restructure-preface-narrative-sJ1CY`。
- `2026-05-19`：Pipeline 1 审查 Quanta Magazine / Natalie Wolchover essay `What Do Gödel’s Incompleteness Theorems Truly Mean?`（published `2026-05-18`；official Quanta full text read）；裁决为 **B 类延后观察 / formal-closure guardrail 候选**。已新增 SourceCard（`Materials/2026/SRC_2026_05_18_Philosophy_Godel_Incompleteness_Quanta.md`）并同步 `Operations/_SRT_MATERIAL_LOG.md` / `Operations/Material_Log/2026-05_Part01.md`。边界：公共 essay / expert synthesis 不是一手数学证明或 SRT 证据；不能把 Gödel incompleteness 写成反形式化许可证、SRT 证明、物理离散时空证明或 “formal theory necessarily fails” 的泛化结论；当前只保留为 claim-ladder hygiene 与 open-tension discipline 的候选材料。
- `2026-05-17`：Pipeline 1 审查 Royal Society / *Philosophical Transactions A* theme issue `World models in natural and artificial intelligence`（issue DOI:`10.1098/rsta/384/2320`；volume 384 issue 2320；published `2026-05-14`；Royal Society issue page 被 Cloudflare 阻断，Crossref metadata + abstracts read）；裁决为 **B 类高优先观察 / 拆分候选**。已新增 SourceCard（`Materials/2026/SRC_2026_05_14_AI_WorldModels_RSTA_Issue.md`）并同步 `Operations/_SRT_MATERIAL_LOG.md` / `Operations/Material_Log/2026-05_Part01.md`。边界：issue-level 输入过宽且未 full close-read article PDF，不能写成 AI consciousness、life-mind continuity、world-model competence、self-modelling 或 LLM emergence 已支持 SRT；后续应按单篇 DOI 重审，优先 `10.1098/rsta.2025.0082`、`10.1098/rsta.2025.0011`、`10.1098/rsta.2024.0528`、`10.1098/rsta.2024.0531`、`10.1098/rsta.2025.0004`、`10.1098/rsta.2025.0014`。
- `2026-05-15`：书稿第 14、16 章优化回写——branch `claude/review-book-optimization-Cgy1G`。(1) **Ch16 v9/v11**（上一轮遗留）：v9（`16_d-value…v9_philosophy_crossdomain_hardening.md`）在 v8 基础上补入形式化种子、五路跨域压力线与悖论 Ch17 桥接；v11（`16_d-value…v11_temporal_structure_refinement.md`）在用户压缩版 v10 基础上做六处定点修订，含§5 承诺时间结构、§6 名称替换窄化、§7 d_mobile 指针、§10 结构缺口重构。(2) **Ch14 v18**（`14_在乎是什么_v18_epsilon_necessity_chain_hardening.md`）在 v17 基础上六处定点强化：①§1 末尾新增 ε_pg→选择→路径→承重位置→攸关→在乎六步推导链总表，标注每步必然性来源；②§2 开头新增细菌层级最小情形段落，说明承重位置是 ε_pg 内置要求而非进化附加功能；③§3 中部新增必然性论证——"承重位置不是生命的馈赠，不是意识的产物，也不是道德发明，它是 ε_pg 的内置后果"；④§15 中部新增理论对比段，指出 Frankfurt（意志主体）/ Heidegger（此在）/ 进化生物学（有机体）都从链条中段切入，SRT 从 ε_pg 推导上行；⑤§1 加强了卷三入口三判据承重基础定位；⑥§18 第五判断末尾固定"攸关是逻辑必然，不是经验观察"。v18 同步提升为 maintext（`01_Source_Intuition/BOOK/Part_03_从选择到主体与价值/14_在乎是什么.md`，`maintext_status: maintext_lock`）。
- `2026-05-12`：Pipeline 1 审查 Nature 开放论文 `Active dissociation of intracortical spiking and high gamma activity`（Lei / Scheid / Flint / Glaser / Slutzky；doi:`10.1038/s41586-026-10331-y`；published `2026-04-01`；official Nature full text read）；裁决为 **A 类小回写**，但明确收束为 **peer-reviewed measurement guardrail**。已在 `SRT_EXP_MEASURE_MAP.md` 新增 `High-gamma local-spike dissociation gate`，并在 `Neuroscience/SRT_Neural_Mechanisms.md` 新增 `High-gamma/spike dissociation gate`，把 HGA / broadband gamma 从"默认同电极附近 spike output"收紧为必须先声明 proxy target 的神经测量窗口：local output spiking、local input / postsynaptic integration、distributed synchrony 不能混写。已新增 SourceCard / PatchNote / IntegrationHook，并同步 `Neuroscience/_SRT_Neuroscience_Hardening_Index.md`、`_SRT_Recent_Material_Patches_Index.md` 与 `Operations/_SRT_MATERIAL_LOG.md`。边界：材料支持 HGA-source-scope guardrail，不证明 HGA 无效；实验集中在 macaque M1 intracortical arrays、ONF/BMI 任务与 200-300 Hz HGA 窗口，不能自动外推为所有皮层、所有 modality 或所有 gamma 定义；HGA 不是 `\Psi_f`、`d-value`、`T_dir`、意识水平、`C_wave`、`D_align` 或 `L_2` 的直接读数。
- `2026-05-11`：Pipeline 1 审查 MDPI / *Entropy* 论文 `Community First Theory: How Collective Organization Generates Individual Diversity`（Ikegami / Kojima / Kashiwagi；doi:`10.3390/e28050523`；published `2026-05-05`；本地 PDF full close reading + official MDPI/Entropy listing checked）；裁决为 **A 类小回写**，但明确降级为 **peer-reviewed empirical bridge / operational proxy guardrail**。已在 `Core_Law/SRT_Collective_Selection.md` 新增 `§4.8a Situated individuation diagnostic`，把集体系统中的个体化压成"集体耦合仍为正、但 self-prediction 不再与 collective-context prediction 冗余"的嵌入式非冗余窗口；并在 `Core_Law/SRT_Reference_Scaling.md §6.4` 收紧旧有 `NTIC > 0 = active agency` 速记，改为 `R_NTIC` coupling-qualified regime。已新增 SourceCard / PatchNote / IntegrationHook，并同步 `Core_Law/_SRT_Core_Law_Hardening_Index.md`、`_SRT_Recent_Material_Patches_Index.md`、`CANONICAL_REGISTRY.md`、`_SRT_INDEX.md` 与 `Operations/_SRT_MATERIAL_LOG.md`。边界：该文只给 *Tetrahymena* 单模型、有限 community 与 kinetic-energy observable 下的初始实证支持；不能推成意识、主体性、道德责任、`d` / `\Psi_f` / `T_dir` 定义，或全部社会/AI 集体的一般定律。
- `2026-05-11`：Pipeline 1 审查 Noema Magazine / Carlo Rovelli essay `There Is No 'Hard Problem Of Consciousness'`（published `2026-05-07`；official Noema full text and metadata read）；裁决为 **A 类小回写**，但明确降级为 **public philosophy essay / epistemic guardrail**。已在 `Philosophy/SRT_HardProblem_Epistemology.md` 新增 `外部视角陷阱 / view-from-nowhere trap`，把意识硬问题中"先把科学误读成世界外部第三人称全景图，再要求从其中推出第一人称体验"的错误起点压成可审查守门：first-person / third-person 差异先按 access route、description grain、embodied position、`L_2` compression 与 `\Psi_f` cost 处理，不自动升级为 metaphysical gap。已新增 SourceCard / PatchNote / IntegrationHook，并同步 `Philosophy/README.md`、`Philosophy/_PHILOSOPHY_MACHINE_INDEX.md`、`Philosophy/_SRT_Philosophy_Hardening_Index.md`、`_SRT_Recent_Material_Patches_Index.md` 与 `Operations/_SRT_MATERIAL_LOG.md`。边界：该文是公共哲学 essay，不是经验科学证据；不能写成"Rovelli/physics 已经解决意识"，不能抹除现象学与第一人称证据，也不能绕过 `Subjecthood_Threshold_Interface` 推出 AI、动物或集体意识结论。
- `2026-05-11`：Pipeline 1 审查 Institute of Art and Ideas / John Heil 评论文 `Emergence explains nothing and is bad science`（published `2025-10-13`；用户粘贴全文，官方 IAI 元数据核验）；裁决为 **A 类小回写**，但明确降级为 **public philosophy claim-hygiene guardrail**。已在 `Core/SRT_Core_21c_Bridge_Hypotheses.md` 的 `P2/P3-B12` 新增 `Emergence hygiene guardrail`，把"涌现"固定为机制占位词而非解释原语：有效的 emergence-style claim 必须说明 lower-level parts/states、coupling、transition/order parameter、macro-pattern/`L_2` constraint 与 implementation channel。已新增 SourceCard / PatchNote / IntegrationHook，并同步 `Philosophy/_SRT_Philosophy_Hardening_Index.md`、`_SRT_Recent_Material_Patches_Index.md`、`CANONICAL_REGISTRY.md`、`_SRT_INDEX.md` 与 `Operations/_SRT_MATERIAL_LOG.md`。边界：该文是哲学评论，不是经验科学证据；不能用来否定宏观模式实在性，也不能删除 SRT 的 P1 `L_2` downward constraint；SRT 的 downward constraint 应读作稳定历史通过边界条件、selection space、update cost 与耦合通道约束未来轨迹，而非额外配置力。
- `2026-05-11`：Pipeline 1 审查本地预印本章节 `Embodied and Embedded Cognitive Development`（Lisette de Jonge-Hoekstra / Ralf F. A. Cox；preprint date `2026-05-01`；本地 PDF full close reading；未识别正式 DOI/URL）；裁决为 **A 类小回写**，但明确降级为 **preprint review bridge**。已在 `Philosophy/SRT_Social_Cognition.md` 新增 `T-Cog-7 Developmental Coordination Scaffold`，把 embodied / embedded cognitive development 压成 child-body-caregiver-environment-history 的软装配协调结构稳定与重组：co-regulation、motor access、developmental cascades、degeneracy、rhythmic scaffold、temporal variability 与 `L_2` trace 共同改变儿童未来可选行动/注意/语言场。已新增 SourceCard / PatchNote / IntegrationHook，并同步 `Philosophy/_SRT_Philosophy_Hardening_Index.md`、`_SRT_Recent_Material_Patches_Index.md` 与 `Operations/_SRT_MATERIAL_LOG.md`。边界：该材料是预印本综述章节，不是新原始实验；不能写成"representation 不存在"、不能把脑约束降权为背景，也不能把节律/环境支持升级为普遍干预定律。
- `2026-05-11`：Pipeline 1 审查 Oxford Academic / *Aristotelian Society Supplementary Volume* 论文 `Panpsychism and the Depsychologization of Consciousness`（Keith Frankish；doi:`10.1093/arisup/akab012`；本地 PDF full close reading）；裁决为 **A 类小回写**。已在 `Philosophy/SRT_Subjecthood_Threshold_Interface.md` 新增 `Depsychologization trap`，把 depsychologized pure feel 压成主体性阈值的防漂移守门：意识论断不能通过剥离 psychological function、access、memory、action coupling、consequence return 与 ethical stake 后，把剩余的"纯 feel"直接升级为 SRT subjecthood。已新增 SourceCard / PatchNote / IntegrationHook，并同步 `Philosophy/_SRT_Philosophy_Hardening_Index.md`、`_SRT_Recent_Material_Patches_Index.md` 与 `Operations/_SRT_MATERIAL_LOG.md`。边界：该文是哲学论证，不是经验判别器；不能写成"Frankish/illusionism 证明 SRT"，不能取消 phenomenology，也不能把 psychological function 单独当作 S4 subjecthood 充分条件。
- `2026-05-11`：Pipeline 1 审查 bioRxiv 预印本 `Opposing BOLD signals and oxygen metabolism largely arise from statistical uncertainty in metabolic estimates`（Goltermann / Huth / Büchel；doi:`10.64898/2026.04.21.719913`；本地 PDF full close reading）；裁决为 **A 类小回写**，但明确降级为 **preprint measurement guardrail**。已在 `SRT_EXP_MEASURE_MAP.md` 新增 `Hemodynamic-metabolic proxy uncertainty gate`，并在 `Neuroscience/SRT_Neural_Mechanisms.md` 新增 `BOLD-CMRO₂ uncertainty gate`，把 BOLD-CMRO₂ sign relation 压成"必须先过 `ΔCMRO₂` 方向不确定性门"的代谢 proxy 准入规则，而非生理 sign reversal 结论。已新增 SourceCard / PatchNote / IntegrationHook，并同步 `Neuroscience/_SRT_Neuroscience_Hardening_Index.md` 与 `Operations/_SRT_MATERIAL_LOG.md`。边界：BOLD、CMRO₂、CBF、CBV 都不是 `\Psi_f`、`d-value`、意识水平或 `L_2` 的直接读数；预印本未同行评审，negative BOLD 仍需独立机制处理；若 PET 或更高 SNR 代谢测量在 uncertainty gate 后仍支持广泛 sign reversal，应改写为真实 neurovascular-metabolic dissociation window。
- `2026-05-09`：Pipeline 1 审查 *Nature Communications* 开放论文 `Creative experiences and brain clocks`（Coronel-Oliveros / Migeot / Lehue et al.；doi:`10.1038/s41467-025-64173-9`）；裁决为 **A 类小回写**。已在 `Neuroscience/SRT_Neural_Mechanisms.md` 新增 `Creative-Experience Brain-Clock patch`，将创意专长与短期创意学习中的较低 M/EEG functional-connectivity brain-age gap 压成 `theta / L2` 可塑性的功能代理窗口，而非"创造力逆转生物年龄"。已新增 SourceCard / PatchNote / IntegrationHook，并同步 `Neuroscience/_SRT_Neuroscience_Hardening_Index.md` 与 `Operations/_SRT_MATERIAL_LOG.md`。边界：`BAG_FC` 不是 `d`、`\Psi_f`、`T_dir`、意识水平或生物年龄本身；专家横断面不能单独证明终身因果；短期 StarCraft II 学习窗口更接近因果但样本小且任务特异。
- `2026-05-08`：Pipeline 1 审查 bioRxiv 预印本 `Propofol-induced loss of responsiveness reorganizes cortical traveling waves in the human brain`（Zarr et al.；doi:`10.64898/2026.04.30.721975`；official API metadata and abstract used；全文/PDF 本地读取被 Cloudflare 阻断）；裁决为 **A 类小回写**，但明确降级为 **preprint abstract-level bridge**。已在 `Neuroscience/SRT_Consciousness_Mechanisms.md` 新增 `2.8a 丙泊酚行进波重组窗口` 与 `H-C14 丙泊酚行进波重组`，将 propofol loss-of-responsiveness 写成可能的行进波方向、频谱结构与 spike-wave coupling 重调，而非简单 wave shutdown。已新增 SourceCard / PatchNote / IntegrationHook，并同步 `_SRT_INDEX.md`、`CANONICAL_REGISTRY.md`、`Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md`、`Neuroscience/_SRT_Neuroscience_Hardening_Index.md`、`Operations/_SRT_MATERIAL_LOG.md`。边界：`N=2`、两名男性、颞叶局部记录、预印本且未 close-read 全文；不证明 consciousness = traveling waves，不升级为临床麻醉监测金标准。
- `2026-05-08`：Pipeline 1 审查 ScienceDirect / *BioSystems* 论文 `An active inference explanation of discriminatory cognition with regard to social attitudes and harmful behaviour`（Manrique / Friston / Walker；doi:`10.1016/j.biosystems.2026.105793`；OSF matching preprint full text 辅助 close reading）；裁决为 **A 类小回写**。已在 `Philosophy/SRT_Social_Cognition.md` 新增 `T-Cog-6 Bounded-Surprisal Discrimination Gate`，把 active inference / ZBS 压成"跨群体更新带宽代理"，用于解释歧视性认知、旁观者沉默与非人化认知的 self-evidencing 稳定机制。已新增 SourceCard / PatchNote / IntegrationHook，并同步 `_SRT_INDEX.md`、`Philosophy/_PHILOSOPHY_MACHINE_INDEX.md`、`CANONICAL_REGISTRY.md`、`Operations/_SRT_MATERIAL_LOG.md`。边界：ZBS 不是 `d`、`\Psi_f`、`T_dir` 或 recognition operator 的定义；机制解释不构成责任豁免；材料是理论论文，不是直接实验。
- `2026-05-08`：Pipeline 1 复核 Peter Godfrey-Smith PDF `Biology, Brain Rhythms, and Consciousness`（preprint PDF；标注为 IAI News 2026-03 文章 `Studies on animal minds suggest consciousness is not computation: Mapping the rhythms of mind and matter` 的 preprint version）；裁决为 **C 类不融入正文**。理由：这是 `2026-04-01` 与 `2026-04-05` 已审查 IAI biological-naturalism 条目的作者预印本版本，未形成超出既有 `Biological Naturalism Interface`、生命-认知连续谱边界和振荡/波场接口的新稳定接口。已在 `Operations/_SRT_MATERIAL_LOG.md` 追加复核记录；不创建 SourceCard / PatchNote / Hook。
- `2026-05-08`：Pipeline 1 审查 New Scientist `An unorthodox version of quantum theory could reveal what reality is`（2026-05-01，Karmela Padavic-Callaghan，`Comment`，subscriber article）；裁决为 **C 类不融入正文**。理由：材料相关性高，但当前可核内容仍是二手评论元数据与摘要，未给出新的同行评审实验、明确 DOI 或可独立承重的 Bohmian discriminator；仓库现有 `Physics/SRT_Physics_Claim_Status.md` 与 `Physics/SRT_Quant_00_Intro.md` 已覆盖 pilot-wave / Bohmian mechanics 的 P3/P4 解释边界。已在 `Operations/_SRT_MATERIAL_LOG.md` 追加 C 类记录；不创建 SourceCard / PatchNote / Hook。
- `2026-05-08`：Pipeline 1 审查 New Scientist `Is consciousness more fundamental to reality than quantum physics?`（2026-04-28，Karmela Padavic-Callaghan，`Features`；用户粘贴全文）；裁决为 **C 类不融入正文**。理由：材料是物理主义、现象学、强涌现、mutualism 与 agency physics 的高质量大众综述，但没有形成超出仓库现有 `Philosophy/SRT_Philosophy_Tradition_Comparison_PH_SS.md`、`Philosophy/README.md`、`Philosophy/SRT_Philosophy_Foundations.md` 的新稳定接口。已在 `Operations/_SRT_MATERIAL_LOG.md` 追加 C 类记录；不创建 SourceCard / PatchNote / Hook。
- `2026-04-26`：Extracted H10-H16 collective tower/nested hardening material into a separate hardening notes file to preserve the minimal L1 canonical surface.
- `2026-04-26`：H16 塔的全局非线性 Lyapunov 稳定性收口（详见 Operations 历史）。
- `2026-04-26`：H15-H10 族普适性、layer-skip、塔级递归系列硬化完成（详见 Operations 历史）。
- `2026-04-25`：H9-H4 L1 formalism 一轮主要硬化完成（详见 Operations 历史）。
- `2026-04-24`：L1 六大 canonical 主文新增完成：Individuation / Occlusion_Dynamics / Suffering / L1_Formalism / Collective_Selection / Irreversibility（详见 Operations 历史）。
- `2026-04-20`：Core_21 命题硬度分层回写、spirituality 双线扩展、philosophy bridge 并入等（详见 Operations 历史）。
- `2026-04-18`：新增治理层文件 README / CLAUDE / CANONICAL_FREEZE / EDIT_PROTOCOL / HARNESS_TESTS。
- `2026-04-15`：d-value canonical 锚点收口到 `_SRT_D_VALUE_CANONICAL.md`。

## 当前高优先事项

- **【P0·2026-06-16 起】《从存在到秩序》全书「姿态修订」**：把正文从证明姿态翻成"拆地板/换镜片/重新看"的体验-邀请姿态。只改**接缝**（序章、章节开头结尾、最强反对者段、语气），不动机制正文与严密——让严密像理论自己说的那样退成背景里承重的地面。单段判准：把读者摆成"陪审员（评判我的证明）"还是"探索者（跟我重新看）"。纲领 `01_Source_Intuition/BOOK/BOOK_POSTURE_REVISION_PLAN_2026-06-16.md`。**进度：接缝翻转第一遍全书过完（`2026-06-17`，序章 + Q01–Q28，PR #488）。** 下一车道（待授权）：幕间章嵌入（PR #487 台账/样章为底）+ 正文更深层体验化。
- 继续同步入口层去重：`README / AGENTS / CLAUDE / STATUS / _SRT_INDEX / Navigation / manifest`
- 保持 canonical 主链不被入口优化反向污染
- 按 `Governance/SRT_CLAIM_LADDER.md` 持续标注 domain 文件中的 P-level
- 继续把运行留痕与理论检索层分开
- 将 spirituality 三支结构（旧主轴 / 新双线 / community companion）与后续导航/入口层建立更清晰索引关系
- ~~将 `SRT_Uncertainty_Payment_Raw_L0_Selection_Bridge.md` 反向合并进 `Philosophy/SRT_Philosophy_Ethics.md` 与 `Philosophy/SRT_Ethics_Agency.md`~~（已完成 2026-04-20）

## Pipeline 快照

- `Pipeline 1`：材料融合主流程继续有效；二轮结构裁决走 `Operations/_SRT_MATERIAL_ADJUDICATION_WORKFLOW.md`
- `Pipeline 3`：信号采集按 `Operations/_SRT_OPERATIONS_SCHEDULE.md` 执行
- `Pipeline 6`：内审按 `Operations/_SRT_OPERATIONS_SCHEDULE.md` 执行

## 当前工作边界

- 书稿正文 **已解冻**（`2026-06-16`），P0 为全书姿态修订过；RC0"正文默认冻结"不再适用，但仍走 `Governance/SRT_EDIT_PROTOCOL.md`
- 姿态修订边界：改接缝、不动机制正文与严密；不许借姿态过偷改 canonical 理论或降低硬度标注
- 理论文件（canonical）编辑仍先看 `Governance/SRT_CANONICAL_FREEZE.md` 与 `Governance/SRT_EDIT_PROTOCOL.md`——理论冻结不受书稿解冻影响
