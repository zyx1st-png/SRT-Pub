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
> **最后更新**：2026-05-15
> **完整历史**：`Operations/_SRT_STATUS_HISTORY.md`
> **年度变更摘要**：`Governance/_SRT_CHANGELOG_2026.md`

## 当前仓库状态

- 根目录已在 `2026-04-15` 完成平铺，当前 `main` 直接对应 SRT 主树内容。
- 远端已收口为单一 `main` 分支。
- 仓库已执行一轮"理论硬化优先、去命题混层"回写：`Core_21` 已拆成 P0/P1/P2-P4 分层，AI 首读入口已降密度为 runtime/bootstrap。
- 当前后续重点是让 domain 文件持续回链 canonical，避免 bridge / companion / lab 命题反向冒充 core。

## 当前建议首读顺序

AI / agent 最短读法：

1. `AGENTS.md`
2. `SRT_AI_START.md`
3. `STATUS.md`
4. `_SRT_INDEX.md`
5. `_SRT_SYMBOL_TABLE.md`

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
- 符号规范 → `_SRT_SYMBOL_TABLE.md`
- formal axioms → `Core/SRT_Core_21_Formal_Axioms.md`
- P0 minimal axioms → `Core/SRT_Core_21_Minimal_Axioms.md`
- P1 constitutive theorems → `Core/SRT_Core_21b_Constitutive_Theorems.md`
- P2/P3/P4 bridge hypotheses → `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- master equations → `Core/SRT_Core_22_Equations.md`
- open tensions → `Core/SRT_OPEN_TENSIONS.md`

## 最近关键推进

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

- 本轮已优先完成 Core_21 命题硬度分层；入口、索引与 domain 回链只做配套收口
- 暂不大规模改正文主链
- 理论文件编辑先看 `Governance/SRT_CANONICAL_FREEZE.md` 与 `Governance/SRT_EDIT_PROTOCOL.md`
