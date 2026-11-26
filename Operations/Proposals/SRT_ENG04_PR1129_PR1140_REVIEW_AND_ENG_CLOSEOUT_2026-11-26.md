---
id: SRT-ENG04-PR1129-PR1140-REVIEW-AND-ENG-CLOSEOUT-20261126
type: proposal
status: active
canonical: false
layer: operations
epistemic_layer: os
claim_mode: audit
created: 2026-11-26
updated: 2026-11-26
priority: high
research_mode: U_and_N_bounded
dependency:
  - STATUS.md
  - 01_Source_Intuition/SRT_AUTHOR_DECISION_FIVE_STAGE_SRT_RECONSTRUCTION_2026-11-22.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_R3_03_INNER_GENERATIVE_PROCESS_AND_PR1140_REVIEW_2026-11-24.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_R3_CLOSEOUT_GLOBAL_SUBTRACTION_2026-11-25.md
  - 01_Source_Intuition/SRT_AUTHOR_TRACE_FEELING_COGNITION_ACTUALISATION_2026-11-11.md
  - Operations/Proposals/SRT_R1_R2_FULL_RECONSTRUCTION_CONSOLIDATION_REPORT_2026-11-22.md
  - Operations/Proposals/SRT_R3_SKELETON_ADJUDICATION_AGENDA_2026-11-22.md
  - Operations/Proposals/SRT_R3_03_INNER_GENERATIVE_PROCESS_PROVISIONAL_CONVERGENCE_2026-11-24.md
  - Operations/Proposals/SRT_R3_FULL_SKELETON_CLOSEOUT_GLOBAL_SUBTRACTION_2026-11-25.md
  - Operations/Audits/SRT_ENG02_ACTIVE_THEORY_ASSIMILATION_RECONCILIATION_2026-11-25.md
  - Operations/Proposals/SRT_ENG03_AI_CROSS_FILE_SEMANTIC_CLEANUP_CROSSWALK_2026-11-26.md
  - Operations/Context_Bundles/README.md
  - Neuroscience/SRT_Neuroscience_Reconstruction_Framework.md
  - Neuroscience/SRT_Neuroscience_Claim_Status.md
  - Neuroscience/patches/SRT_Neuro_NEURAL21_REM_State_Dependent_Metabolic_Payability_v0_1.md
  - Bridge/SRT_Adjacent_Theory_Interface_Index.md
  - Neuroscience/README.md
  - Core_Law/SRT_Generative_Ontology_Spine.md
  - Philosophy/SRT_HardProblem_Epistemology.md
tags: [ENG-04, Closeout, PR1129, PR1140, NME, Neuroscience, AuthorTrace, ArchivalTriage, R4Readiness]
---

# `ENG-04` 遗留 PR（`#1129` NME / `#1140` 源记录）独立审查与 `ENG-01..ENG-04` 总体收口报告（2026-11-26）

> **治理定位与基线声明（`canonical: false`）：** 本文基于最新 merged `main@c3fd28112`（`#1154` `R3` 总收口、`#1155` `ENG-01`、`#1156` `ENG-02`、`#1157` `ENG-03` 均已合并落地）完成最后一项前置工程清障 **`ENG-04`**，并交付 **`ENG-01..ENG-04` 总体收口与 `R4` 授权前就绪报告**。
>
> **硬红线核验：**
> 1. **不以两个遗留 PR 均成功合并为验收目标**；本轮对 `#1129`（NME）给出明确**不予合并/建议撤回关闭**的独立审查裁定，对 `#1140`（2026-11-11 作者源记录）完成**原文无损历史归档（`status: archived`）+ `R3-03` 二轮裁决防覆盖指针分流**，不直接擅自操作旧 PR 分支或抢并理论争议内容；
> 2. **零理论含义改写与零 canonical 触碰**：不修改任何 `Core_Law/`、`Core/`、`Philosophy/`、`Spirituality/`、`AI/`、`Neuroscience/`、`Bridge/`、`_SRT_SYMBOL_TABLE.md`、`_SRT_PSI_F_CANONICAL.md`、`_SRT_D_VALUE_CANONICAL.md` 或 Freeze-A 文件；
> 3. **全部既有治理边界保持不动**：`R4 / R5` 尚未授权启动；累计去重 **`63` 项 `OPEN`**、全部既有 **`HOLD`**（`O2-M`、`§10.1` 第三主深井、`§10.2` 广域综合、`CN-2 E2`、`CN-3 toy`、`1B` 模拟、`DATA-ACCESS-0 = NO-GO`）、`25` 条封存 `validation_holdout`、`07-23/24` 原始撞车记号禁运及四大 `R4` 前过渡引用规则全部完整保持；不使用或修改 GitHub Actions。

---

## 0. 执行结论速览

| 审查对象 | 固定审查提交 | 工程与校验现状（对 `main@c3fd28112`） | 独立理论与证据结论 | 最终处置建议 |
|---|---|---|---|---|
| **Draft PR `#1129`**<br>NME 神经代谢实现桥接<br>（`research/nme-neurometabolic-bridge-20261024`） | `d053eb958`（3 文件：`+291` 行） | 无底层 Git 文本冲突（`git merge-tree rc=0`，GitHub `MERGEABLE / UNSTABLE`）；本地复现 CI 唯一报错为 `status: draft_v0_1` 枚举越界（1 行可修，但**绝不因可修绿而合入**） | 6 组假说中 **4 组（`H-NME-1/2/5/6`）在本次指定解释任务中未建立独立 SRT 比较增量（`SOURCE-OWNED AT THIS EXPLANATORY JOB`，不扩大为全域零增量或理论已证伪）**；另 **2 组（`H-SRT-NME-3/4`）**中 `H-SRT-NME-4` 当前无法排除未测微态与元可塑性竞争解释且受 `DATA-ACCESS-0 = NO-GO` 阻断，`H-SRT-NME-3` 当前不可充分识别、研究路线优先选择更易控制的 `CN-2 Task Family A`；同时与 `R3` 总收口存在 6 处骨架脱节并绕过 `Pipeline 1` 直写导航入口 | **不予合并（建议作者关闭/撤回 Draft PR `#1129`）**；关闭 PR 不等于销毁研究资产——在本报告 §1.5 保留原固定提交 `d053eb958` 永久链接及负向护栏、六组假说、候选模型与文献线索，留待 `R5` 且另行解冻 `DATA-ACCESS-0 / §10.1` 后按 `Pipeline 1` 决定是否建卡 |
| **Draft PR `#1140`**<br>2026-11-11 感觉—认知—实现与原初内在感受性作者源记录<br>（`author/feeling-cognition-actualisation-20261111`） | `4af028a2a`（1 文件：`+142` 行） | 无底层 Git 文本冲突（`git merge-tree rc=0`，GitHub `MERGEABLE / CLEAN`）；本地 `check_frontmatter_changed.py` `0 errors / 0 warnings`；该源文件**尚未落地于 `main`**（`R3-03` 仅以 GitHub URL 外链引用） | 2026-11-11 作者逐字原话（`A0-Q1..Q4, A0-S2, A0-S5`）具有不可替代的原始思想溯源价值，且含 5 项仍具独立保留价值的增量（如位置性具身梯度比对、多位置认同、脚手架双重性）；但其第二次 `B`（原初内在感受性）、“三层”字面阶梯风险、`§6` 旧路由及单一神性视角均已由 `R3-03`（`#1148`）与 `R3` 总收口（`#1154`）明确校准更新，**不得覆盖现行骨架** | **完成历史归档分流**：随本 `ENG-04` PR 将源文件以 **`status: archived`** 归档至 [`01_Source_Intuition/SRT_AUTHOR_TRACE_FEELING_COGNITION_ACTUALISATION_2026-11-11.md`](../../01_Source_Intuition/SRT_AUTHOR_TRACE_FEELING_COGNITION_ACTUALISATION_2026-11-11.md)（`§1–§6` 逐字一字未改，顶部加注 `R3-03` 与 `R3` 总收口防覆盖控制指针）；**本 PR 合并后由作者关闭原 Draft PR `#1140`** |

---

## 1. 任务一：Draft PR `#1129`（NME 神经代谢实现桥接）四步独立审查

### 1.1 步骤一：工程冲突与治理校验核查

1. **Git 合并状态实测**：在 `main@c3fd28112` 基线上执行本地 `git merge-tree --write-tree main origin/pr-1129` 返回 `rc=0`，且 `gh pr view 1129` 返回 `mergeable: MERGEABLE`、`mergeStateStatus: UNSTABLE`。`#1129` 修改的两处既有导航文件 [`Bridge/SRT_Adjacent_Theory_Interface_Index.md`](../../Bridge/SRT_Adjacent_Theory_Interface_Index.md)（`+1` 行）与 [`Neuroscience/README.md`](../../Neuroscience/README.md)（`+4` 行）自基线提交 `662d33b70` 以来均未变动，**无实际文本合并冲突**；全部 9 条 `dependency` 路径在 `main@c3fd28112` 均存在。
2. **CI 失败精确复现**：历史 `governance-preflight` 失败归因为 `pr_local_frontmatter: failure`（`PR_LOCAL / LOCAL DIRTY / DO NOT MERGE`）。在独立临时 worktree 将 `origin/pr-1129` 模拟合入 `main@c3fd28112` 后本地运行 `scripts/check_frontmatter_changed.py`，精确复现唯一阻断错误：
   - `Neuroscience/SRT_NME_Neurometabolic_Implementation_Bridge_v0_1.md` 第 4 行使用 `status: draft_v0_1`，超出 frontmatter ratchet 允许枚举（`draft | active | frozen | archived`），导致 `new=1, errors=1`（另 2 个被改导航文件为既有 `known=2` 基线项，不新增警告）。
3. **步骤一裁定**：工程层面仅 1 行 frontmatter 字段即可修绿，但严格遵循 `R3` 总收口与 `ENG-04` 纪律——**严禁借工程可修绿绕过理论与证据独立审查**。

### 1.2 步骤二：原始文献与证据强度独立核查

对 `#1129 §11` 所引全部 4 篇文献执行独立核查，结果如下：

| 文献 | 独立核查的发表状态与核心实证内容 | 证据强度上限 | `#1129` 引用边界审查结论 |
|---|---|---|---|
| **Deacon, Garcia-Valdecasas & Jacob (2026)**, *The medium is the message: How neurometabolic entanglement generates conscious experience*, `arXiv:2610.30217v1` `[q-bio.NC]` | **未同行评审的理论/神经哲学预印本**；综合神经血管与神经调质文献，提出皮层—前脑估值—中脑/脑干调节环路的“莫比乌斯环”与“代谢瓶颈”意识假说，**无任何新增实验验证** | **P3 理论比较假说**（零实验证明力） | `#1129` 诚实标明了其“理论预印本”身份且未宣称证明意识；但将其直接写入 `Neuroscience/README.md` 与 `Bridge/SRT_Adjacent_Theory_Interface_Index.md` 跳过 `Pipeline 1`（`Operations/_SRT_MATERIAL_LOG.md` / `SourceCard`），**程序越级** |
| **Korte et al. (2023)**, *J. Cereb. Blood Flow Metab.* 43(7):1142–1152 | **已发表实证研究**（啮齿类/脑片）：蓝斑（LC）轴突释放去甲肾上腺素经 **$\alpha_2$ 肾上腺素能受体**（抑制 cAMP）收缩脑毛细血管周细胞，建立基础血管收缩张力，使局部神经活动得以触发血管舒张 | **啮齿类血管张力生理机制** | 仅证实 LC-NA→周细胞基础血管张力通路，**不证明**“信息—代谢莫比乌斯意识闭环”或内容特异绑定 |
| **Sun et al. (2026)**, *Neuron* 114(2):287–306.e9（Du 实验室） | **已发表实证研究（实验对象：斑马鱼幼体 / larval zebrafish）**：揭示蓝斑去甲肾上腺素神经元与周细胞间存在全脑模式化耦合，协调整体脑血管动力学 | **斑马鱼幼体全脑血管协调实证机制** | 证实的是斑马鱼幼体中的**全脑共模血管生理协调**，不可直接外推至人类意识，恰恰反衬出“共同血管调节 ≠ 意识内容绑定 ≠ 现象统一” |
| **Jacob, Ford & Deacon (2023)**, *Frontiers in Human Neuroscience* 17:976036 | **已发表理论/综述论文**：从 4E 认知与代谢纠缠视角讨论静息态 EEG–fMRI 解释框架 | **理论综述（非因果干预证据）** | 仅支持“认知与代谢不可当作无关软件硬件”的一般背景，不能支撑特异性 SRT 预测 |

**步骤二小结**：`#1129` 在正文纪律上优于许多早期桥接稿（明确列出四级证据表与 `BOLD–CMRO2` 不确定性护栏），但本质仍是以**一篇未评审理论预印本**为主源，跳过 `Pipeline 1` 直接在活跃神经科学导航页与总桥接索引中占位，且对次级引文（`Korte 2023`、`Sun 2026`）未标清跨物种与实验外推边界。

### 1.3 步骤三：六组理论对照独立审查（邻居已拥有工作 vs SRT 独立增量）

按仓库 `SOURCE-OWNED AT THIS EXPLANATORY JOB` 与同目标竞争者规则，逐一审查 `#1129 §6` 全部 6 张对照卡与 `§8` 五级竞争模型（`R0–R4`）：

| 对照卡 | 核心检验命题 | 成熟邻居（`R0–R3`）归属 | SRT 独立比较增量判定 | 诊断要点 |
|---|---|---|---|---|
| **`H-NME-1`** | 生理支持向量 $r(t)$（及 $x \times r$）在纯神经预测器 $x(t)$ 与一般觉醒之外改善可达性预测 | **由 NME + 常规神经血管/星形胶质代谢神经科学（`R2`）承担该解释任务** | **在本次指定解释任务中未建立独立 SRT 比较增量（`SOURCE-OWNED AT THIS EXPLANATORY JOB`，不独立立项）** | 检验的是血管/代谢生理对神经响应阈值的调节作用（已有 `Korte 2023`、`Sun 2026`、`NEURAL21`），将其转述为“SRT Gate 实现”属 `Phase 9` 术语翻译（不扩大为全域零增量或理论已证伪） |
| **`H-NME-2`** | 共享神经调质/血管调节 vs 皮层间内容绑定分离 | **由认知神经科学觉醒—绑定混杂控制及 NME vs GNWT/IIT 竞争（`R0–R2`）承担该解释任务** | **在本次指定解释任务中未建立独立 SRT 比较增量（`SOURCE-OWNED AT THIS EXPLANATORY JOB`，保留比较护栏）** | 检验 NME 自身“代谢瓶颈能否绑定内容”的假说；保留其“生理共模调节 ≠ 内容绑定”比较护栏，不独立立项 |
| **`H-NME-5`** | 代谢功、主观心理努力与体验清晰度三者可分离 | **由认知努力心理学 / EVC（Shenhav 等）/ 心理生理学与 NME 证伪检验（`R1–R2`）承担该解释任务** | **在本次指定解释任务中未建立独立 SRT 比较增量（`SOURCE-OWNED AT THIS EXPLANATORY JOB`，保留负向护栏）** | 对 SRT 具明确**负向护栏价值**（印证 `Ψ_f ≠ 代谢消耗 ≠ 主观努力`），本身不提供独立 SRT 正向比较增量 |
| **`H-NME-6`** | 内部驱动神经代谢再组织 vs 主观能动感（Sense of Agency） | **由比较器/前向模型、主动推断与事后归因能动感神经科学（`R1–R3`）承担该解释任务** | **在本次指定解释任务中未建立独立 SRT 比较增量（`SOURCE-OWNED AT THIS EXPLANATORY JOB`，不独立立项）** | 检验 NME `§6` 自身能动性断言，未提出区别于前向模型/主动推断的 SRT 专属操作化变量 |
| **`H-SRT-NME-3`** | 匹配输入、神经复杂度、觉醒、奖赏与 `m_proxy` 后，不同赌注/延迟后果结构是否额外预测后续可选择性变化 | 强竞争者为 **model-based RL、EVC（期望价值控制）、前瞻记忆与价值驱动记忆巩固（`R3`）** | **保留 `P3` 候选、移交既有研究路线（当前不可充分识别，不独立开神经代谢支线）** | ① 在人类宏观神经血管成像中同时匹配 `m_proxy`、奖赏、动机与复杂度却单独操纵“同一承载位不可外包后果”当前不可充分识别；② **当前研究路线优先选择更易控制混杂变量的中立认知/计算路线 `CN-2 Task Family A`**（后果驱动多维概念学习，[`STATUS.md`](../../STATUS.md#L1184-L1186)）与 `R3-06-O5/O7`（不宣告后果归属与未来可选择性候选已被证伪） |
| **`H-SRT-NME-4`** | 匹配当下可观测神经/血管/代谢态后，不同既往历史轨迹是否额外预测下一跃迁可达性 | 强竞争者为**未观测微态（突触权重/树突棘/受体转运/星形胶质糖原）+ 常规元可塑性（`R3`）** | **保留未决、当前不启动（受 `DATA-ACCESS-0 = NO-GO` 阻断，不宣告已被竞争理论证伪）** | 在无创宏观神经血管数据中，**当前无法排除未测微态与元可塑性等隐变量竞争解释**（无法排除竞争解释 ≠ 已被竞争理论吸收）；同时 `#1129` 第 201 行自身已承认 `Phase 8A Case B / DATA-ACCESS-0 = NO-GO` 持续生效，与 [`papers/history_dependent_reachability/PAPER_CHARTER.md`](../../papers/history_dependent_reachability/PAPER_CHARTER.md) 退回构造性 tiny-MDP 的方法论限制一致 |

**步骤三核心结论**：`#1129` 的 `§8` 自身已诚实承认“生理因果支持成立但无 SRT 增量预测（translation-only）”是合理结果。独立核查表明：**6 组对照中 4 组在本次指定解释任务中未建立独立 SRT 比较增量，另 2 组（`H-SRT-NME-3/4`）在当前神经代谢范式下分别面临不可充分识别与无法排除隐变量竞争解释的硬限制**。因此，应拒绝的是**当前独立神经代谢研究路线的立项与合入**，而不是宣告其全部理论候选已经失败或被证伪。

### 1.4 步骤四：与 `R3` 最新理论骨架、神经科学接口及证据边界对齐核查

`#1129` 撰写于 `2026-10-24`，早于 `R3-01..R3-08` 与 `R3` 总收口整整一个月，对照最新 `main@c3fd28112` 存在 **6 处结构性口径脱节**：

1. **旧 `Gate / θ_emb / L0→L1` 底层框残留**：`§3.1`（L133–L139）与 `§9` 仍以旧 `Gate / θ_emb / L2 writeback` 组织叙事，未对齐 `R3` 总收口确立的**动态三关系骨架（差异生成 ⇄ 差异比对与组织 ⇄ 生成条件递归重构）**与 **`A1` 压力四分 × 供给承载窗（`Ψ_f`）**双侧分离；
2. **缺失 `T3-02 D / PT09` 与 `R3-08` 摩擦四分**：未接入广义摩擦（机会成本差异产生的实际选择压力，含 `PT09` 垂直压制核心机制）与 `R3-08` 摩擦四分（广义摩擦 / 非闭合压力 / `Ψ_f` / 主观痛苦）的层级边界；
3. **缺失 `R3-06 D1` `d / D_stake / D_eff / PT06 C` 数学清算**：仍以旧 `d-value` 单接口对比情绪效价，未反映 `d_canonical ≡ d_stakes ≤ D_eff` 已被证伪、广义关切敏感性（`PT06 C`）与现行 `d` 仅为待验证接口（`P1-05`）；
4. **缺失 `R3-04` `One / Stable ISP / Bearer` 双语义过渡规则**：未区分强承载 `Bearer (P+E)` 与「`R3-04 Bearer` 秩序视角候选」，亦未落位 `Stable ISP / P1-T06` 独立强持续性边界；
5. **未与 `R1/R2` `Q10–Q14` 神经/胶质/免疫/单胺假说族合流**：[`R3` 总收口视图 ③ 第 6 项](SRT_R3_FULL_SKELETON_CLOSEOUT_GLOBAL_SUBTRACTION_2026-11-25.md#L242) 明确将 `#1129` 归入 `Q10–Q14` `H-*` 比较假说与 `DATA-ACCESS-0 = NO-GO` 约束下，而 `#1129` 独立另起一套符号（`x, v, u, r, a, b, h, s, m_proxy`）与导航入口，易制造新碎片；
6. **`§10` 近端交付路线存在 Programme Drift 风险**：尽管声明“不重开神经科学深井”，但 `§10` 明确列出近端数据集选型、冻结 `R0..R4` 实证比较与生理因果干预，容易在 `DATA-ACCESS-0 = NO-GO`、`§10.1 = HOLD` 及当前唯一焦点 `ENG-01..04 → R4` 期间制造第二隐性研究支线。

### 1.5 PR `#1129` 最终处置裁定与有限价值留存

- **处置裁定**：**不予合并（建议作者正式关闭/撤回 Draft PR `#1129`）**；**严禁**将其写入 `Neuroscience/README.md` 与 `Bridge/SRT_Adjacent_Theory_Interface_Index.md`。**关闭 Draft PR 不等于销毁研究资产或宣告全部候选已被证伪**。
- **永久溯源指针与留存研究资产（完整保全，零丢失）**：
  1. **原 PR `#1129` 固定提交永久溯源链接**：[SRT_NME_Neurometabolic_Implementation_Bridge_v0_1.md @ `d053eb958`](https://github.com/zyx1st-png/SRT-Pub/blob/d053eb958b33cb7fce92b27ab94d72eb9a48debb/Neuroscience/SRT_NME_Neurometabolic_Implementation_Bridge_v0_1.md)（完整保全其六组对照卡 `H-NME-1/2/5/6` 与 `H-SRT-NME-3/4`、五级竞争模型 `R0–R4` 及 `§7` 测量与识别合同）；
  2. **四类统一性严格分离与反单标量代谢 `Ψ_f` 护栏（原 `#1129 §5` / `§3`）**：**生理共模调节（LC-NE/血管同步）≠ 功能整合 ≠ 现象共呈 ≠ 主体归属/个体化**；`CBF / CBV / BOLD / CMRO2 / 胶质底物 / 神经元 ATP / 恢复动力学` 不可塌缩为单一“能量预算”（供给 ≠ 递送 ≠ 可用 ATP ≠ `Ψ_f`），可供 `R4` 神经科学/哲学接口与 `R5` 意识对照引用；
  3. **潜在正面启发（待检理论交集，不独立开支线）**：NME 揭示“生理资源调节不仅支持选择过程，还可能参与改变后续选择能够发生的条件”，与 SRT 动态三关系（差异生成 ⇄ 差异比对与组织 ⇄ 生成条件递归重构）存在值得后续检验的交集；因 NME 自身已提出神经活动与代谢的递归纠缠，SRT **不能**仅凭该对应主张独立贡献，未来须检验位置性、后果归属、历史结构与生成条件重构的联合关系能否产出 NME 无法提供的预测；
  4. **`R5` 候补外部对照文献登记**：`Deacon, Garcia-Valdecasas & Jacob (2026) arXiv:2610.30217v1`、`Korte et al. (2023)`、`Sun et al. (2026)`（斑马鱼幼体）与 `Jacob, Ford & Deacon (2023)` 记为 `Q10–Q14` 神经/胶质/单胺 `H-*` 比较假说的远期参考条目；**仅当进入 `R5` 且作者另行正式解冻 `DATA-ACCESS-0 / §10.1 HOLD` 后**，方按 `Pipeline 1` 流程评估是否建卡与纳入对照。

---

## 2. 任务二：Draft PR `#1140`（2026-11-11 作者源记录）二审指针与历史归档分流

### 2.1 工程核查与“为何必须无损归档而非直接丢弃”

1. **工程状态实测**：在 `main@c3fd28112` 基线上，本地 `git merge-tree main origin/pr-1140` 返回 `rc=0`，GitHub `gh pr view 1140` 返回 `mergeable: MERGEABLE`、`mergeStateStatus: CLEAN`；本地 `check_frontmatter_changed.py` 通过（`0 errors, 0 warnings`）；全部 8 条 `dependency` 路径均存在。
2. **关键缺口发现**：[`01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_R3_03_INNER_GENERATIVE_PROCESS_AND_PR1140_REVIEW_2026-11-24.md`](../../01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_R3_03_INNER_GENERATIVE_PROCESS_AND_PR1140_REVIEW_2026-11-24.md#L50) 虽然已完成对 `#1140` 的正式二轮理论审查，但当时仅通过 GitHub 远端提交链接引用 `4af028a2a`，`01_Source_Intuition/SRT_AUTHOR_TRACE_FEELING_COGNITION_ACTUALISATION_2026-11-11.md` **从未落地于 `main` 仓库本地文件树**。若直接关闭 `#1140` 而不做历史归档，作者 2026-11-11 的逐字原始表达将脱离 `main` 溯源体系；反之，若直接将 `#1140` 原样以 `status: active` 合并，其过时表述又可能被新会话误读为覆盖 `R3-03` 后续裁决的活跃口径。

### 2.2 `#1140` 三分法精确分流表（保全历史原话 / 标明替代口径 / 提取独立增量）

| 分流类别 | `#1140` 精确条目与原文要点 | 现行控制口径 / 后续去向 |
|---|---|---|
| **一、必须逐字保全的历史作者原始表达**（绝不改写原句，完整保留溯源） | • **`A0-Q1`**：择优性选 `C`（选择倾向与可能性共同规定）；选择包含「比较」与「实际化」（麦克斯韦妖生成门控类比；「没有实际化，比较就没有价值」；通过脚手架让比较更好发生）<br>• **`A0-S2 / A0-Q2`**（第一个 `B`）：比较与实际化共同构成原初 Selection；作者实质限定「比较不是数值上的客观比较，而是具身的能量梯度式的差异感知，局部的差异感知不等同于客观的全局差异感知。文明发展的方向就是建立更全局的统一差异脚手架来更好的感知」<br>• **`A0-Q3`**：更高阶统一重构局部关系并生成新方向「是基于多位置对梯度的认同和感知」<br>• **`A0-Q4`**：「我觉得应该是三层，感觉、认知、实现……最深层的无脚手架的感觉是一种神性」<br>• **`A0-S5`**（第二个 `B`）：当时对“原初的内在感受性”回复「非常认同你的分析，我的表述更接近于 B」 | 原封不动保留于归档文件 [`01_Source_Intuition/SRT_AUTHOR_TRACE_FEELING_COGNITION_ACTUALISATION_2026-11-11.md`](../../01_Source_Intuition/SRT_AUTHOR_TRACE_FEELING_COGNITION_ACTUALISATION_2026-11-11.md)（`§1–§6` 逐字节与 `4af028a2a` 一致），作为真实理论演进一手档案 |
| **二、已被 `R3-03`（`#1148`）与 `R3` 总收口（`#1154`）明确校准/替代的口径**（严禁覆盖现行骨架） | 1. **`A0-S5`「原初的内在感受性」与 `§3` 候选图中的“内在感受面向”**<br>2. **`A0-Q4`「感觉—认知—实现三层」可能被误读为三层静态本体或线性阶梯的旧风险**<br>3. **`§6` 末尾所写的“待在 ontology source-reentry 轨道推进并返回作者二轮裁决”旧路由**<br>4. **`A0-Q4`「无脚手架的感觉是一种神性」作为单一神性定义的旧视角** | 1. **已由 `R3-03`（2026-11-24 作者原话裁决，`#1148`）正式校准**：原初 `Selection` 保留**内在生成过程**（内生性 + 位置参与性，不将成熟感觉或微观心理体验倒写进原初层），感觉是该过程在认知位置上的实际展开与参与；前现象性质保持 **`R3-03-O4 OPEN`**，`HP-B` 与 `B_s != B_p` 不变<br>2. **已由 `R3-03` 与 `R3` 总收口（`#1154`）重构**：纳入动态三关系（差异生成 ⇄ 差异比对与组织 ⇄ 生成条件递归重构）下的认知垂直递归展开<br>3. **旧路由已闭环替代**：二轮审查已于 `#1148` 完成，`R3` 全骨架总收口已于 `#1154` 落地<br>4. **已纳入神性双面与 `T3-04 D / T3-01 C/E` 接口**：保留为“有限位置无脚手架切身参与”视角，与 `R3-02 / T3-04 D / T3-01 C/E` 并列待 `R4` 规范接口协调（`R3-03-O7 / R3-CL-O4`） |
| **三、仍具独立保留价值的理论增量**（已贯通或继续滋养 `R4 / R5`） | 1. **“比较不是客观数值评分，而是位置性、具身梯度式的差异感知”**（`A0-Q2`）<br>2. **“多位置对梯度的感知与认同 → 生成此前未被共同发现的新方向，而非上帝视角外部替代”**（`A0-Q3`）<br>3. **“认知脚手架的双重性（稳定延续、跨位置沟通 vs 不封闭新感觉进入）”**（`§5 #5`）<br>4. **“无脚手架 = 不被既有认知/符号脚手架穷尽，而非无关系/无条件”**（`§3`）<br>5. **“没有实际化，比较就没有价值”**（`A0-Q1`） | 1. 直接支撑 `R3` 总收口**位置性比对**与**比对本身的生成性**（`R3-CL-O8` 子项 ⑤）<br>2. 直接锚定 `R3-02` 共同生成协议与 `R3-07` 规范共同生成 / 协同共选主轴（防滑向平均偏好或强制一致）<br>3. 直接对接 `R3-07` 脚手架双重作用与 `R3-08` `U5` 固化风险<br>4. 与 `T3-04 D`（神性·源义为不可被现有对象化描述穷尽的真实来源）精确共振<br>5. 锚定 `R3-06` 价值与实际生成互生及 `A1` 实现制约，防纯抽象比较脱实 |

### 2.3 PR `#1140` 历史归档分流执行方式

1. 本次 `ENG-04` PR 同步创建 [`01_Source_Intuition/SRT_AUTHOR_TRACE_FEELING_COGNITION_ACTUALISATION_2026-11-11.md`](../../01_Source_Intuition/SRT_AUTHOR_TRACE_FEELING_COGNITION_ACTUALISATION_2026-11-11.md)，采取**最小介入、绝对保真**原则：
   - frontmatter 设 **`status: archived`**（通过 ratchet 校验零警告）、保持 `canonical: false` 与 `ai_do_not_use_for_definition: true`，并在 `dependency` 补入 `R3-03` 裁决、`R3` 总收口与本报告；
   - 仅在文档顶部加注清晰的 **`历史归档与二轮裁决控制指针（2026-11-26 ENG-04 分流加注）`**，明文阻断旧表述覆盖现行骨架；
   - 原 `#1140` 提交 `4af028a2a` 的全部 `§1–§6` 正文逐字节零改动保全。
2. **本 `ENG-04` PR 经复核合并后**：原 Draft PR `#1140` 的全部历史溯源资产已安全归档入 `main`，作者即可在 GitHub 正式关闭 Draft PR `#1140`（附指向本归档文件与 `ENG-04` 报告的关闭说明）。

---

## 3. `ENG-01..ENG-04` 总体收口验收与 `R4` 授权前就绪报告

### 3.1 四项前置工程清障完成总账（全部基于 `main@02dcb9b20` → `c3fd28112` 接续推进）

| 工程项 | 落地载体 / 合并基线 | 核心清障交付成果 | 真实保留与移交 `R4` 的缺口（零虚报） | 验收状态 |
|---|---|---|---|---|
| **`ENG-01`**<br>上下文包分层瘦身 | **PR `#1155`**（`MERGED / 04dfe961d`）<br>[`Operations/Context_Bundles/README.md`](../Context_Bundles/README.md) | 完成 `SPINE` 分层瘦身三步路线：补入 `Core_Law/SRT_One_Formation.md`、`Core_21c` 移按需桥接、`Core_22` 建独立 `FORMAL` 包（`~31,481 est_tok`）；`SPINE` 15 源（`133,829 est_tok`），相对 `200,000` 总窗口剩余 `66,171 est_tok`（含 `45,000` 系统/输出/误差预留），相对 `155,000` 单次装载上限的**实际可继续装载余量为 `21,171 est_tok`**；全部 10 份产物经 `build_srt_context_bundles.py --check` 逐字一致 | 待 `R4` 改写对应 canonical owner 后再确定性重建上下文包 | **DONE（已合并验收）** |
| **`ENG-02`**<br>理论吸收台账真实对账 | **PR `#1156`**（`MERGED / bdd560f1b`）<br>[`SRT_ENG02_ACTIVE_THEORY_ASSIMILATION_RECONCILIATION_2026-11-25.md`](../Audits/SRT_ENG02_ACTIVE_THEORY_ASSIMILATION_RECONCILIATION_2026-11-25.md) | 统一 `EA-1..EA-5` 为 `srt_active_theory_nodes.json` 三轴口径；修复 `check_active_theory_assimilation.py` `EA-3/EA-4` 假阳性并补 4 项回归测试；真实纠偏 `NODE-T-DIR`、工程补线 `NODE-SUBJECTHOOD` 入 `DOMAIN_PHILOSOPHY` 与 `§8a`、补齐 `NODE-BOOK-BACKFLOW` 与 3 处 `_SRT_DEEP_THEORY_MAP.md` 漏项；检查器 **0 WARN** | 诚实保留 4 处真实理论/快速层缺口（`NODE-LIFE-DISSIPATIVE`、`NODE-ENTROPY-REORG`、`NODE-SOCIAL-L2`、`NODE-GHOST-OPERATOR`）、`NODE-BOOK-BACKFLOW`（`engineered_not_active`）、`NODE-D-VALUE`（`author_gate`）；有效吸收维持 **`effectively_assimilated = 3/16`**（`robustly_observed (bounded) = 3/16`，本轮零新增 Axis B 行为验证），全部移交 `R4` | **DONE（已合并验收）** |
| **`ENG-03`**<br>AI 全域语义清理蓝图 | **PR `#1157`**（`MERGED / c3fd28112`）<br>[`SRT_ENG03_AI_CROSS_FILE_SEMANTIC_CLEANUP_CROSSWALK_2026-11-26.md`](SRT_ENG03_AI_CROSS_FILE_SEMANTIC_CLEANUP_CROSSWALK_2026-11-26.md) | 完成 `AI/` 全部 `54` 份已追踪 Markdown + `18` 份跨域消费者清理对照表；拆解 7 条隐含旧推导链（退出 `R: L2→L2 / J: L0→L1`）；确立三套 `AI / S` 全称隔离、非线性并行三阶承载审查 + 三态严格区分；揭露 `Ontology_Annex` 6 重复制污染与 `Ontology_Split` 静默正文漂移，确立 `R4` 原子合并与正文内容比对验收设计 | 零提前改写 AI 正文；全部实质清理与 4 项作者门/OPEN 边界（`AG-1`、`AG-2 / R3-04-O5`、`R3-04-O3`、`R3-07-O6`）及 `S1` 候选定义完整移交 `Wave R4-4` | **DONE（已合并验收）** |
| **`ENG-04`**<br>遗留 PR 独立审查与分流 | **本收口报告** + 归档文件 [`SRT_AUTHOR_TRACE_FEELING_COGNITION_ACTUALISATION_2026-11-11.md`](../../01_Source_Intuition/SRT_AUTHOR_TRACE_FEELING_COGNITION_ACTUALISATION_2026-11-11.md) + [`STATUS.md`](../../STATUS.md)（待复审合入） | 完成 `#1129`（NME）四步独立审查（建议不予合并并关闭，留存负向护栏与文献线索于 `R5` 候补）；完成 `#1140` 三分法分流与 `status: archived` 逐字历史归档（顶部加注 `R3-03` 与 `R3` 总收口防覆盖指针） | 本 PR 合并后由作者在 GitHub 正式关闭旧 Draft PR `#1129` 与 `#1140` | **READY FOR REVIEW（本 PR 提交收口）** |

### 3.2 `R4` 启动前全仓红线与就绪状态检查

- **基础治理全绿**：本地 Python 3.12 全量校验（`governance_preflight.py --skip-write-report --strict-split-metadata`、`check_frontmatter_changed.py`、`check_frontmatter_baseline_monotonic.py`、`check_status_recording_rule.py`、`refresh_split_metadata.py --check`、`build_srt_context_bundles.py --check`、`check_active_theory_assimilation.py`）全通过，0 错误、0 新增警告、0 吸收检查 WARN；
- **理论与授权边界 100% 完整**：
  - `ENG-01..ENG-04` 全程**零 canonical / Freeze-A 文件修改**、**零理论含义篡改**、**零 GitHub Actions 修改**；
  - 累计去重 **`63` 项 `OPEN`**（A 级 10 / B 级 37 / C 级 16，含 `R3-CL-O8` 内部 5 项独立退出子题与 `HP-B` 独立退出）、全部既有 **`HOLD`**（`O2-M`、`§10.1`、`§10.2`、`CN-2 E2`、`CN-3 toy`、`1B`、`DATA-ACCESS-0 = NO-GO`）、`25` 条封存 `validation_holdout`、`07-23/24` 符号禁运及四大 `R4` 前过渡引用规则均未松动；
  - **`R4` canonical 重构与 `R5` 实证研究均尚未启动**。

### 3.3 待作者审定与下一步入口

1. **行政收尾（遗留 PR 关闭）**：本 PR 合并后，由作者在 GitHub 正式关闭已审查处置完毕的两份旧 Draft PR（`#1129` 撤回关闭、原固定提交 `d053eb958` 资产已永久留痕于本报告 §1.5；`#1140` 历史原文已以 `status: archived` 归档入 `main` 后关闭）。
2. **唯一下一步准备任务（编制 `R4` 首批原子落地包执行方案）**：本 PR 合并后，全部四项前置工程清障正式闭环；基于 [`R3` 总收口视图 ⑤](SRT_R3_FULL_SKELETON_CLOSEOUT_GLOBAL_SUBTRACTION_2026-11-25.md#L331-L384) 与 [`ENG-03` AI 清理蓝图](SRT_ENG03_AI_CROSS_FILE_SEMANTIC_CLEANUP_CROSSWALK_2026-11-26.md#L254-L300)，编制 **`R4` canonical 重构首批原子落地包执行方案**——以 **`Core_Law/SRT_Generative_Ontology_Spine.md`** 与 **`Core_Law/SRT_One_Formation.md`** 的正面理论重构为主，同步界定直接依赖的核心定义 owner、减法目标、原子合并边界、未决事项与验收标准，提交作者单独正式授权；在获得作者正式授权前，绝不提前改写任何 canonical 文件或启动 `R5` 实验。
