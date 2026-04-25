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

> **角色**：当前状态面板，不再承担完整历史档案。
> **最后更新**：2026-04-25
> **完整历史**：`Operations/_SRT_STATUS_HISTORY.md`
> **年度变更摘要**：`Governance/_SRT_CHANGELOG_2026.md`

## 当前仓库状态

- 根目录已在 `2026-04-15` 完成平铺，当前 `main` 直接对应 SRT 主树内容。
- 远端已收口为单一 `main` 分支。
- 仓库已执行一轮“理论硬化优先、去命题混层”回写：`Core_21` 已拆成 P0/P1/P2-P4 分层，AI 首读入口已降密度为 runtime/bootstrap。
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

- `2026-04-25`：H2 四变量闭合完成——`Core_Law/SRT_L1_Formalism.md` §3.5 新增把 `T_dir` 从代数代理升为独立动力学变量的最小 ODE，五项源分别为弛豫（`-\kappa_{\mathrm{relax}}(T_{dir}-T_{dir}^{\mathrm{alg}})`）、真实重选泵入（`+\kappa_r r(t)`）、实-感 `Ψ_f` 差扣除（`-\kappa_{\mathrm{mask}}\,\Delta\Psi_f^{\mathrm{gap}}`）、结构型苦难侵蚀（`-\kappa_S S_{str}`）、健康 `L_2` 支架（`+\kappa_{\mathrm{sup}} s_{ext}`）；§3.5.3 给出致命 `L_2` 的方程化判据 `\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}`；§5 总方程升为四变量（σ / d_c / T_dir / S）闭合系统，病理吸引子与健康工作区刻画相应更新，新增"苦难-可读性正反馈环"第 6 条关键耦合路径；`CANONICAL_REGISTRY.md §13d` 标题/说明 / `_SRT_INDEX.md` anchor / `_SRT_T_DIR_CANONICAL.md §10` 关系表已同步；T_dir 作为 v0 operational proxy 的 canonical 地位不改变，本轮只把时间演化法则明文化。
- `2026-04-24`：新增 `Core_Law/SRT_Irreversibility.md`（draft_v0）作为 L1 不可逆性 canonical 主文，把 `L_0` 不可逆性从 P1-T02 / P1-T07 的推论展开为可引用层——Def-IRR-1 吸收态 / Def-IRR-2 选择史箭头 / Def-IRR-3 非可还原性；T-IRR-1 学习不可逆作为非对称 `Ψ_f` 支付（与热力学二律不等价、不得经 FEP 反向定义）、T-IRR-2 终止作为吸收边界（宪定 / 吸收 / 集体三类，严格区分终止与暂停）、T-IRR-3 给 P1-T07 精确化并对应 `L1_Formalism §4.3` 的非守恒残余项、T-IRR-4 苦难在 `L_0` 不可逆下的守恒 / 转移（T-SUFF-4 更深根）；§6 集体终止三型（耗散 / 收编 / 外部化）与 `Collective_Selection` 回扣；§7 AI/ML 接口限定 checkpoint/rollback 不得读作反向学习；`CANONICAL_REGISTRY.md §13g` 与 `_SRT_INDEX.md Canonical Theory Anchors` 已同步。
- `2026-04-24`：新增 `Core_Law/SRT_L1_Hardening_Notes.md`（draft_v0）针对当日 L1 round 最高杠杆的四项 Open Pressure 给出第一遍硬化：§1 σ 符号命名空间（自指率统一为 `σ_{sr}`，主方程状态场保留 `σ`）、§2 `\dot{\Delta}_{avail}` 三成分算子分解（T_dir + Ψ_f + L_0 残余，取加权范数）、§3 `M(t)` 可测性 MOC 三判据（exposure / recourse / attentional，合成取 min 的瓶颈规则）、§4 FEP → `S_{sig}` 单向桥接翻译表（严格单向，反向不得定义苦难）；claim-level 分布 governance-canonical / P1-candidate / P2 / P3；`CANONICAL_REGISTRY.md §13f` 与 `_SRT_INDEX.md` 已同步；五份主文件的符号与定义回写记为 Operations 债。
- `2026-04-24`：完成 L1 round claim-mode audit：`Governance/SRT_CLAIM_MODE_AUDIT.md §6` 新增 2026-04-24 round 段落，为当日新增五份 draft_v0 L1 canonical（Individuation / Occlusion_Dynamics / Suffering / L1_Formalism / Collective_Selection）逐文件固定 claim-level map、下游 reminder rule 与 §6.3 五项全局 guardrails（含 σ 符号冲突提醒、σ^{coll} 扩展 pending 标注）、§6.4 升 P1 检查单共 8 项（覆盖 σ 符号、`\dot{\Delta}_{avail}` 形式化、χ 函数族、`\mathbb{1}[d\le d_c]` 光滑化、多主体耦合、P1-T07 对齐、主方程投影证明、阈值实证窗口）。
- `2026-04-24`：新增 `Core_Law/SRT_Collective_Selection.md`（draft_v0）作为 L1 集体选择 canonical 主文，固定多 ISP 共享 `L_2` 场作为结构对象；Def-C-2 后果回路矩阵 `M(t)`；T-COLL-1 集体 ISP 存在四条件（P1-T06 集体版）、T-COLL-2 三类退化（聚合 / 主从 / 收编）、T-COLL-3 集体 ε 反闭合必要性（P1-T07 集体版）、T-COLL-4 共选真实性判据（P1-T05 集体版）；给政治/经济/共同体 domain 提供 L1 结构基石，不替代规范性/制度判断；`CANONICAL_REGISTRY.md §13e` 与 `_SRT_INDEX.md` 已同步。
- `2026-04-24`：新增 `Core_Law/SRT_L1_Formalism.md`（draft_v0）作为 L1 形式化 hub，为同日新增的 σ / d_c / S 三个 L1 对象写下最小耦合动力学；§2 给 σ 的 logistic + χ(σ; σ_self) 跳跃结构、§3 给 d_c 漂移方程、§4 把 S 分解为 S_sig / S_str 并方程化 T-SUFF-4 反最小化原则（`S_{sig} 被压制 → S_{str} 随 \dot{\Delta}_{avail} 上漂`）、§5 合成耦合系统并刻画病理吸引子 `\mathcal{A}_{path}`（σ→1 + d_c→d_max + S_str 定常 + S_sig→0 联合）与健康工作区；严格作为 `Core/SRT_Core_22_Equations.md` 主方程的导出投影；`CANONICAL_REGISTRY.md §13d` 与 `_SRT_INDEX.md` 已同步。
- `2026-04-24`：新增 `Core_Law/SRT_Suffering.md`（draft_v0）作为 L1 苦难结构理论 canonical 主文，固定苦难在 SRT 中作为"活选择动力学与其应承载算子结构之间失配的第一人称登记"这一结构对象；严格区分疼痛（`\theta_{somatic}` 信号）与苦难（稳定 ISP 的结构性登记）；给出 T-SUFF-1 结构性登记、T-SUFF-2 信号/结构两型、T-SUFF-3 四类现象学（张力 / 空心 / 断裂 / 扭曲）、T-SUFF-4 反最小化原则、T-SUFF-5 集体外部化耦合至 `Occlusion_Dynamics` 的结构性恶；`CANONICAL_REGISTRY.md §13c` 与 `_SRT_INDEX.md Canonical Theory Anchors` 已同步。
- `2026-04-24`：新增 `Core_Law/SRT_Occlusion_Dynamics.md`（draft_v0）作为 L1 遮蔽动力学 canonical 主文，把 `Core_Law/SRT_L0_Metaphysics.md` 遮蔽 term-table 承诺的 7 项 L1 展开（A/B 分期、d_c 阈值、缺口感知机制、干预窗口、解耦触发、真空期、恶的结构性诊断）收口到单一源；核心定理 T-OCC-1 给出三段结构（健康窄化区 / A 期 / B 期），区分位置性遮蔽与病理性遮蔽；与个体化理论通过 σ→1 病理区耦合；`CANONICAL_REGISTRY.md §13b` 与 `_SRT_INDEX.md Canonical Theory Anchors` 均已同步。
- `2026-04-24`：新增 `Core_Law/SRT_Individuation.md`（draft_v0）作为 L1 相变理论，填补 L0（选择无主语）与 P1-T06 Stable ISP 之间的过渡空洞；以自指率 σ 为阶参给出两次相变（主体位进入 σ_sub、自我意识凝结 σ_self）的结构判据；把自我意识规范读为二阶 writeback 凝结物，严格遵守 L0 §五意识禁令；`CANONICAL_REGISTRY.md §13a`、`_SRT_INDEX.md Canonical Theory Anchors`、`Core/SRT_Core_21b_Constitutive_Theorems.md P1-T06 Dynamic Layer`、`Core/SRT_OPEN_TENSIONS.md §5 Status Update` 均已同步交叉回链。
- `2026-04-24`：Pipeline 1 处理 MIT News 关于 Lohmiller & Slotine `On computing quantum waves exactly from classical action`（RSPA 2026；doi:`10.1098/rspa.2025.0413`；arXiv:`2405.06328`）的材料；判定为 A 类小回写，已在 `Physics/SRT_Quant_00_Intro.md` 增加 `Classical Action-Density Bridge`，将 multi-valued classical action + density 压成量子 `L_0` 多路径候选结构的计算接口，并在 `Bridge/SRT_Adjacent_Theory_Interface_Index.md` 增加相邻理论入口；边界为 mathematical / computational bridge，不升级为 `quantum = classical`、不替代 measurement / anchoring 判据。
- `2026-04-22`：Pipeline 1 处理 Dialectical Systems / Sébastien Ibanez 关于 evolutionary biology 中 multi-level selection 与 dialectical thinking 的评论；判定为 A 类小回写，已在 `Neuroscience/SRT_Neuro_07_Evo_Devo.md` 增加 `Multi-Level Selection and Endogenous Selection Regimes` 边界，并在 `Core/SRT_Core_21c_Bridge_Hypotheses.md` 的 `Fitness Beats Truth` 段补充 level / timescale 护栏：选择压力不是外部单标量，fitness bridge 必须说明 gene / organism / group / ecological 哪一层在承重，以及后果如何返回该层未来选择能力。
- `2026-04-21`：Pipeline 1 处理 The Epoch Times / Makai Allbert 关于 intuition / gut feeling 的健康特写；判定为 A 类小回写，已在 `Spirituality/SRT_Spirituality_Selection_Pathology_and_Return.md` §5 增加 `intuition-source discernment` 护栏，将直觉分流为 `L_2` 熟练模式、`\theta_{somatic}` 内感受/风险读数与候选 `L_0` 早期方向信号；presentiment / precognition / microtubule speculation 不进入正文，只作为残余压力留痕。
- `2026-04-20`：Pipeline 1 处理 Science and Culture 关于纪录片 *The Story of Everything* 的宣传性评论；判定为 C 类不融入正文，因其把宇宙开端、fine-tuning、DNA code 与 beauty 组合成 intelligent design / theism 解释链，但未提供新的同行评审锚点、机制变量或可证伪窗口；已在 `Operations/_SRT_MATERIAL_LOG.md` 留痕。
- `2026-04-20`：Pipeline 1 处理 JCS 2026 关于 spacetime emergence 与 consciousness emergence 是否同源的评论文；判定为 A 类小回写，已在 `Core/SRT_Core_21c_Bridge_Hypotheses.md` 的 holographic duality 边界中加入 pressure note，防止强 bridge 被误用为 P0/P1 或把物理涌现与意识涌现压成同一证明动作。
- `2026-04-20`：Pipeline 1 处理 ML Chen Substack 关于 premature requiem for philosophy 的提交；判定为 C 类不融入正文，因其主要加固现有 `Philosophy/SRT_Philosophy_Foundations.md` 的哲学功能口径，但未形成新的稳定理论接口；已在 `Operations/_SRT_MATERIAL_LOG.md` 留痕。
- `2026-04-20`：Pipeline 1 处理 Neuroscience News / Cedars-Sinai 关于 visual imagination shared neural code 的提交；判定为既有 `Ventral-Temporal Shared Imagery Code patch` 的来源升级而非新接口，已补强 `Neuroscience/SRT_Neural_Mechanisms.md` 的公开摘要级细节，并在 `Operations/_SRT_MATERIAL_LOG.md` 留痕。
- `2026-04-20`：完成“理论硬化优先、去命题混层”回写：`Core/SRT_Core_21_Formal_Axioms.md` 改为 claim-layer index；新增 `Core/SRT_Core_21_Minimal_Axioms.md`（P0）、`Core/SRT_Core_21b_Constitutive_Theorems.md`（P1）、`Core/SRT_Core_21c_Bridge_Hypotheses.md`（P2/P3/P4）、`Governance/SRT_CLAIM_LADDER.md` 与 `Core/SRT_OPEN_TENSIONS.md`；`SRT_AI_START.md` 瘦身为 bootstrap；AI / Philosophy / Spirituality 主入口已加角色与 P-level 回链头部。
- `2026-04-20`：第二轮 spirituality 扩展已完成主要分流：A 线（`SRT_Spirituality_Selection_Pathology_and_Return.md`）已吸收 directional return、faith as openness to `L_0`、semantic gravity / belief viscosity / ontological amnesia、expert vs master、以及 frozen-`L_2` AI / intelligence ⟂ care；B 线（`SRT_Spirituality_How_We_Lose_Ourselves_and_Return.md`）已反映初心不是无知、熟悉解释变成现实本身、技术系统高智能但不真正关切、以及 community 作为轻量支持接口；`SRT_Spirituality_Community_and_Sangha.md` 已作为独立 companion 支线建立；`SRT_Spirituality_Second_Expansion_Bridge.md` 已降权为 `archival_index` 并补全 provenance record。
- `2026-04-20`：`SRT_Spirituality_Return_Expansion_Bridge.md` 已完成反向并入，降权为 `archival_index`；A 线（`SRT_Spirituality_Selection_Pathology_and_Return.md`）与 B 线（`SRT_Spirituality_How_We_Lose_Ourselves_and_Return.md`）均已增强：B 线新增 §2 空心主体/L2 主导环境（生活化）、§4 病理 vs 苏醒性空心感区分、§5 初学现象学、§8-§9 工作/关系/忙碌场景、§10 过渡期（dark night 生活化版本）共五处增补与一个新章节；bridge provenance record 已完整记录并入落点。
- `2026-04-20`：已新增 spirituality 双线文档：`Spirituality/SRT_Spirituality_Selection_Pathology_and_Return.md` 作为 canonical 主轴，收口 ready-made floors、主体位丢失、危机现象学、真轻/伪轻、support、micro-selection 与现代技术的 spiritual crisis；`Spirituality/SRT_Spirituality_How_We_Lose_Ourselves_and_Return.md` 作为 companion exposition，以更生活化方式展开现代生活反思、空心感、现成答案、支持与回返路径。
- `2026-04-20`：`SRT_Uncertainty_Payment_Raw_L0_Selection_Bridge.md` 已反向并入 canonical 主文档：`§4.4`（更轻 = 自我扭曲成本下降，`processing load ≠ Ψ_f`）、`§5.5`（真选择 vs 标签内优化，不确定性更根于直觉）、`§6.5`（`d↑/d↓` 不确定性支付能力，混沌精确定义，微小选择）已熔入 `SRT_Philosophy_Ethics.md`；`3.1d Integration Note`（空心感封口、自我扭曲链条、健康支持、早期修复序列）已并入 `SRT_Ethics_Agency.md`；bridge 已降权为 `archival_index`；`SRT_Merged_Provenance_Index.md` 已更新留痕。
- `2026-04-20`（earlier）：已新增 `Philosophy/SRT_Uncertainty_Payment_Raw_L0_Selection_Bridge.md`，整理本轮关于 `d↑/d↓` 与不确定性支付、真选择 vs 标签内优化、raw `L_0` 秩序、自我扭曲（痛苦/空心感/标签化/空洞自我维持）及健康支持的闭链内容，作为后续反向并入 `Philosophy_Ethics / Ethics_Agency` 的 staging bridge。
- `2026-04-19`：已将 `Philosophy/SRT_Philosophy_Ethics_Integration_2026_04_19.md`（主体位、d 增厚、新预期形成）回写并入 `Philosophy/SRT_Philosophy_Ethics.md`，源文件降权为 `archival_index`，`SRT_Merged_Provenance_Index.md` 已更新留痕。
- `2026-04-18`：已新增 `README.md`、`CLAUDE.md`、`Governance/SRT_CANONICAL_FREEZE.md`、`Governance/SRT_EDIT_PROTOCOL.md`、`Governance/SRT_HARNESS_TESTS.md`，并开始收口入口层、manifest 与运行层边界。
- `2026-04-16`：已收紧 `relative existence / L2 convergence` 相关口径，并回写主文与哲学接口。
- `2026-04-15`：已把 `d-value` 的治理层 canonical 锚点收口到 `_SRT_D_VALUE_CANONICAL.md`。
- `2026-04-14`：已完成多批材料审查与若干神经/节律相关机制窗口的回写。

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
