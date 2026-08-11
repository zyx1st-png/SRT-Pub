---
id: SRT-OPS-AUDIT-MATERIAL-ASSIMILATION-DELTA-2026-08-11
type: audit
status: active
record_stage: audit_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
date: 2026-08-11
source_of_truth: "origin/main @ 7688a8df26aa0d7b2be7ff52e9b247155a236283"
dependency:
  - SRT-OPS-AUDIT-ACTIVE-THEORY-ASSIMILATION-2026-08-06
  - SRT-CONFIRMED-PROPOSITION-SEMANTIC-COVERAGE-AUDIT-20260808
  - SRT-BOUNDED-RETRIEVAL-PROTOCOL-20260808
  - SRT-MATERIAL-PIPELINE
  - SRT-MATERIAL-LOG
  - SRT-ACTIVE-THEORY-NODES
  - SRT-OPEN-TENSIONS
  - SRT-CLAIM-LADDER
tags: [Governance, Audit, Material, Assimilation, Delta, ActiveTheory]
machine_readable: Operations/Audits/data/srt_material_assimilation_delta_2026-08-11.csv
---

# SRT 历史材料 → 当前理论结构增量整合审计（2026-08-11）

> **审计边界**：本文件不拥有理论定义权；不修改 A/B/C 原始裁决；不自动提升 claim level；不把材料存在误判为理论生效。本轮只做 `audit + prioritization`，不执行理论综合。
>
> **继承模型**：继续使用“档案化 → 工程化 → 理论生效”三层模型，以及 active-theory checker 的 Axis A `structural_assimilation`、Axis B `behavioral_availability`、Axis C `intervention_effect`。不引入新的永久状态体系。
>
> **决策单位纪律**：Table A 与 companion CSV 以 material row / file engineering state 做 inventory；是否立项则以**已确认命题与区分**为单位。2026-08-08 semantic-coverage audit 已证明 hook、owner path、fast layer 或 planned synthesis file 的静态缺失会产生假阴性，故它们只能描述工程拓扑，不能单独发出 synthesis / active-layer GO。
>
> **行为证据纪律**：本轮没有执行新的 cluster-specific bounded retrieval run，因此没有改写任何节点的 Axis B。任何新活跃层／正文综合立项必须先执行 `SRT_BOUNDED_RETRIEVAL_PROTOCOL_2026-08-08.md` 的 baseline probe，再按 Case A 停／B 修活跃层／C 做内容写回／D 降级档案处置。既有 `observed` / `robustly_observed` 只按现有 run record 继承。

---

## 0. 结论先行

截至最终复核基线 `7688a8df26aa0d7b2be7ff52e9b247155a236283`：

- 正式 Material Log 为 **226** 条：A **149** / B **27** / C **50**。
- 档案化层为 **77 SourceCards**；工程化层为 **52 patches / 44 hooks**，hook 状态 **landed 12 / partial 3 / pending 29**。
- 相对 2026-08-06 审计口径，正式材料净增 **19 条，全部为 A**；SourceCard `+18`、patch `+21`、hook `+20`。新增 20 张 hook 全部仍为 `pending`；这只证明 owner landing 未按 hook ledger 关闭，**不证明相关区分不可检索或必须施工**。
- 三个材料簇已达到“值得冻结命题组并跑 bounded baseline probe”的程度：
  1. Neuroscience N1–N13，特别是 memory/object/history 链与 embodied-eligibility/temporal-closure 支链；
  2. Philosophy 的 individuation / representation / bearer formation 簇；
  3. AI 的 evidence provenance / reason-trace / goal selection / re-selection / stake gate 架构簇。
- `Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md` 当前仍不存在；文件缺席不是语义缺口证据。修订后裁决为 **N1–N13 = probe candidate；synthesis = NOT YET**。
- `Individuation / Representation / Bearer Formation` 已形成 bounded-probe candidate；是否需要新 synthesis 尚未裁决。探针必须区分现有 owner 已能回答的内容与真正缺口，并继续禁止把 Simondon / Deleuze 的外部趋同改写成 SRT native identity。
- AI cluster 也是 **probe candidate**，不是 CompactCore absorption GO。AIEVID01 / AIREASON01 已随既有 `NODE-AI-REASONING` bounded baseline 被证明可用；AIGOAL01 / AIRESEL01 / AICONSC01 的增量命题组仍未被 cluster-specific probe 覆盖。当前不需要新建 `AI/_SRT_AI_Hardening_Index.md`。
- COLL08 已在 `SRT_Collective_Selection.md` 与 `SRT_Reference_Scaling.md` 完成局部落地；“局部落地完成”不等于跨域综合完成，但目前**不值得为了文件对称再建一份独立 collective synthesis**。
- Physics hardening index 的触发条件未改变：E05 尚无已登记 discriminator，故 **Physics synthesis remains deferred**。
- 08-08 已有 bounded 行为证据必须优先于本轮静态表：NEURAL18 与 NEURAL23 在 `nd` 中 0 次导航、8/8 节点题组通过；REP01 在 `px` 中 1 次导航、7/7 节点题组通过。三者在 CSV 中改记为 `verified_active`，不得再从 hook／落点缺失反推内容缺口。
- 27 条正式 B 中，**9 条**有符合新规的具名复活触发条件，**18 条**仍是旧制日期/说明或缺少当前形式的具名 trigger；本轮没有仓库证据证明任何 trigger 已发生，故 **fired = 0**。这 18 条是 trigger-metadata clarity debt，不是理论 backlog。

---

## 1. 基线、范围与方法

### 1.1 执行基线

执行前依次运行：

```text
git fetch origin
git checkout main
git pull --ff-only
git status
git rev-parse HEAD
gh pr list --state open
```

结果：

```text
BASE_SHA=7688a8df26aa0d7b2be7ff52e9b247155a236283
```

原工作区 main 含用户未提交改动，本审计因此从该 SHA 建立独立 worktree 与分支，未清理、覆盖或带入原工作区改动。

初始执行时 PR #780 尚未合并，并修改 `Operations/Context_Bundles/`、`Operations/Archive_Records/Large_File_Audit_2026-05-09.md` 与 `Operations/Proposals/`。在本审计最终收口前，#780 已合入 main；本分支随后重放到 merge commit `7688a8df`，并从合并后的输入重新生成 9 个 Context Bundle 文件，没有手工拼接两组生成物。`13d31338..7688a8df` 只改变上述 proposal / archive / generated-bundle 路径，不改变 Material Log、SourceCard、patch、hook、registry 或理论 owner；本轮数量与处置已在新基线上重跑。

### 1.2 解析口径

本轮同时读取：

```text
Operations/_SRT_MATERIAL_LOG.md
Operations/Material_Log/*.md
Materials/2026/SRC_*.md
*/patches/*.md
*/hooks/*.md
Registries/material_registry.jsonl
Registries/patch_registry.jsonl
```

机器表包含 dated log 中全部 **229 条物理行**。其中 3 条位于 `2026-07_Part02.md` 的声明行数之外；正式总数仍按 root log / split README 的 **226** 口径。CSV 通过 `official_declared_scope` 标记二者，不删除历史行，也不在本 PR 修复台账。

2026-08-06 审计已记录当时的同类差异：正式 207 条、物理 211 条，差 4。当前为正式 226 条、物理 229 条，差 3。因此：

```text
official delta = +19
physical-row net delta = +18
declared-count lag = 4 -> 3
```

这解释了为什么正式增量与物理净增量相差 1；不能把这一差异误报为本轮新增材料丢失。

### 1.3 本轮 audit-only disposition

机器表的 `current_disposition` 只使用本次审计允许的操作标签：

```text
verified_active
owner_landed_not_active
engineered_pending
synthesis_candidate
legacy_provenance_only
parked_with_trigger
guardrail_only
writing_only
superseded_or_duplicate
rejected
unclear
```

它们不修改 claim ladder，不替代 A/B/C，也不是新的治理权威。特别地，`owner_landed_not_active` 明确保留：

```text
owner paragraph exists
!= automatically active / retrievable
```

### 1.4 Inventory unit 与 decision unit

本轮保留 material-row inventory，是为了回答数量、provenance、hook topology 与 historical survivor 问题；它不恢复 2026-08-06 的文件工程单位作为立项判据。决策优先级为：

```text
confirmed proposition / distinction
-> existing bounded probe evidence
-> cluster-specific bounded baseline probe
-> Case A / B / C / D disposition
-> only then decide whether to build
```

因此 Table B 的 `Missing landing` 只报告工程拓扑，不能与 `synthesis needed` 画等号。companion CSV 也不是 52 张 patch 的逐 patch coverage table；其覆盖边界在 §18 明列。

---

## 2. Table A — Pipeline inventory delta

| Metric | 2026-08-06 baseline | Current | Delta | Evidence / note |
|---|---:|---:|---:|---|
| Material Log total（正式口径） | 207 | **226** | **+19** | root log + split declared counts |
| A | 130 | **149** | **+19** | all official new verdicts are A |
| B | 27 | **27** | 0 | no automatic backlog created |
| C | 50 | **50** | 0 | original rejection retained |
| Dated-log physical rows | 211 | **229** | **+18** | previous audit §11 vs current full parse |
| SourceCards | 59 | **77** | **+18** | `Materials/2026/SRC_*.md` |
| Patches | 31 | **52** | **+21** | all `*/patches/*.md` |
| Hooks | 24 | **44** | **+20** | all `*/hooks/*.md` |
| Hook landed | 12 | **12** | 0 | frontmatter `integration_status` |
| Hook partial | 3 | **3** | 0 | same |
| Hook pending | 9 | **29** | **+20** | all newly added hooks remain pending |
| Material registry rows | 2 at recorded audit source SHA | **18** | **+16** | JSONL rows, git-relative to `a07d2a72` |
| Patch registry rows | 2 at recorded audit source SHA | **20** | **+18** | JSONL rows, git-relative to `a07d2a72` |

### Delta since previous assimilation audit

新增工程化对象不是同一批对象的一对一复制：

- **18 new SourceCards**：PH-IND03 复用并 reopen 既有 Simondon SourceCard；因此新增正式 A 行数不等于新卡数。
- **21 new patches**：包含没有新外部 Material Log 行的 `AIRESEL01`，以及一份材料生成双域 patch 的情况（Wang → NEURAL29 + PH-MEM01）。
- **20 new hooks**：PH-IND02 与 AIRESEL01 目前无 hook；Wang 生成两张 hook；全部新 hook 为 pending。
- 19 条正式 A 增量主要落在：NEURAL23–30、PH-CONSC03/04、PH-IND01–03、PH-DIFF01、PH-MEM01、PH-MR01、PH-METH02、SOC-COG03、AICONSC01、THERM01、HCLR01。

这说明本轮 delta 的主要形态是：

```text
new material
-> SourceCard / patch / hook / index
-> clustered engineering pressure
!= owner landing
!= active-theory effect
```

---

## 3. 三层总体状态

| Layer | Current evidence | Verdict |
|---|---|---|
| 档案化 | 77 SourceCards；229 physical dated rows；provenance 可追 | 健康，但有 3-row declared-count lag |
| 工程化 | 52 patches；44 hooks；两份 registry；root material index | 健康且快速增长；新增长集中在 pending hook |
| 理论生效 | active manifest：8 active_complete / 6 partially_active / 1 engineered_not_active / 1 author_gate | 稀缺；不能由 patch/hook 数量外推 |

当前 Axis B 分布保持现有 manifest 记录：

```text
robustly_observed = 3
observed = 2
untested = 10
not_applicable = 1
```

推导的 `effectively_assimilated` 节点为 3。本轮没有新 run，因此没有把任何新材料簇的行为状态从 `untested` 升级。

基线上的 `STATUS.md §Fast Status` 仍写作较早的 `robustly_observed=2 / observed=3 / effectively_assimilated=2`，与 manifest + checker 的 `3 / 2 / 3` 不一致。审阅修订在本 PR 只做最小 operations repair：同步这三个数字、Choice Generation 的 bounded 状态、Material Log 快照，并加入 08-08 语义覆盖／bounded protocol 与本审计的声明式指针；不改任何理论 owner。

### 3.1 继承 08-08 probe 对静态表的修正

| Material increment | Initial 08-11 static reading | Existing bounded evidence | Corrected audit disposition |
|---|---|---|---|
| NEURAL18 | `engineered_pending`；fast/router blank | `nd`: 0 navigation；8/8 node set；five-way decodability gate retained | `verified_active` for the sampled proposition |
| NEURAL23 | `synthesis_candidate`；planned CompactCore target only | `nd`: 0 navigation；8/8 node set；STATUS startup carries the three-way eligibility split | `verified_active` for the sampled proposition |
| REP01 | `guardrail_only`；fast/router blank | `px`: 1 navigation；7/7 node set；theory-package tuple and falsification target retained | `verified_active` for the sampled proposition |

这些修正不把单次 node run 外推为整个新簇的 `robustly_observed`。它们只说明三条已采样命题不能再被本轮静态 inventory 判成未吸收，也说明 planned synthesis file 不存在不构成立项理由。

---

## 4. Philosophy delta

### 4.1 Agency 已有 synthesis，不再列入 backlog

以下 patch 已由现存非 canonical synthesis 承载：

```text
PH-AG01
PH-AG02
PH-AG03
PH-AG04
PH-SEM01
```

当前 owner：

```text
Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md
```

hook 状态进一步证明这不是待创建 synthesis：PH-AG01 / PH-AG04 为 `landed`；PH-AG02 / PH-AG03 / PH-SEM01 为 `partial`，其 Agency–Subjecthood 部分已落地，剩余部分分别受 canonical/high-risk 或 parked target 约束。

因此它们的 disposition 是 `owner_landed_not_active`，不是 `synthesis_candidate`。现有 `NODE-SUBJECTHOOD` 仍为 `partially_active / untested`，所以也不能把 owner landing 改写成行为生效。

### 4.2 新的 individuation / representation / bearer cluster

以下 patch 已形成明显的共同承重结构，而不是彼此无关的单篇摘要：

```text
PH-CONSC03 / PH-CONSC04
PH-IND01 / PH-IND02 / PH-IND03
PH-DIFF01 / PH-MEM01 / PH-MR01
SOC-COG03
```

可压缩出的候选链为：

```text
preformed-object rejection
-> individuation / selective closure
-> bearer formation
-> history-bearing transformation
-> re-identification
-> second-order / generative reselection
-> subjecthood gate
-> phenomenality residual
```

这条链目前只是一种审计发现，不是新理论。各环节的实际 owner 状态如下：

| Current owner / interface | Existing native structure | Delta landing state |
|---|---|---|
| `Core_Law/SRT_Individuation.md` | individuation / selector-position owner already exists | PH-IND03 / PH-DIFF01 / PH-MEM01 pending；高风险 target |
| `Philosophy/SRT_Subjecthood_Threshold_Interface.md` | bearer-unit-first gate and S0–S6 interface exist | PH-CONSC03/04、PH-IND01/02、PH-MEM01、PH-MR01 pending |
| `Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md` | PH-AG01–04 + PH-SEM01 synthesis exists | none of the new PH-IND/DIFF/MEM/MR IDs is present |
| `Philosophy/Foundations_Annex/10_MentalRepresentation_Interface_Batch.md` | Sens/Spec/Inv/Func evidence ladder and producer-consumer gate exist | PH-MR01 pending |
| `Philosophy/SRT_Social_Cognition.md` | social-cognition owner exists | SOC-COG03 pending |
| `_SRT_Recent_Material_Patches_Index.md` + philosophy hardening index | cluster is declaratively indexed | index-level engineering only; not owner/fast-layer activation |

回答两个核心问题：

1. **这些 patch 已形成 probe-worthy cluster。** 可冻结的候选区分不是“哲学家都谈个体化”，而是预成对象拒绝、可重新识别的对象稳定、历史变换、承载位置与现象性残余之间的非同一关系。
2. **它们是否缺 current-theory synthesis 尚未实测。** 新 ID 在列出的 owner 中没有直接落地，只说明 hook / owner topology 未关闭；08-08 的五次假阴性禁止把这一静态事实继续推成内容缺口。

结论：为 `Individuation / Representation / Bearer Formation` 冻结一组 bounded baseline questions **有必要**；新 synthesis 是否必要为 `NOT YET`。若 probe 落入 Case C，未来 synthesis 才应明确排除 Agency–Subjecthood 已完成内容，并把 phenomenality 留作 residual，不写成 bearer 的自动结果。

### 4.3 Simondon / Deleuze 边界

PH-IND03 与 PH-DIFF01 的相似性足以支持共同 close-read，但不足以提高任何 claim level。

允许保留的 external convergence：

```text
anti-preformation
structured selectability
operation -> structure -> operation
individuation before completed identity
problem-space restructuring
future-selectability rewrite
```

禁止的身份映射：

```text
virtual = L0
preindividual = L0
transduction = SRT selection
Deleuzean selection = Real Choice Moment
generativity = d increase
intensity = Psi_f
dark precursor = G_hat_theta
eternal return = t_onto
```

审计结论：二者属于高价值 P3 hardening / pressure model。它们的共同出现只足以支持 proposition extraction + baseline probe，不证明存在语义缺口，也不证明其哲学概念已经成为 SRT native proposition。

---

## 5. Neuroscience delta

### 5.1 Authoritative target

当前 authoritative hardening index 指向：

```text
Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md
```

执行时该文件仍不存在。旧的 `N1_N12_v0_2` 也不存在。hook-ledger 范围内只有 `NEURAL19_Preattentive...Integration_Hook.md` 仍指向旧名，但全域扫描还发现两处现行施工表面：

```text
Neuroscience/SRT_Neuroscience_Hardening_N1_N9_Integration_Hooks_for_N10_N12.md
  - line 22: Recommended future synthesis file
  - line 125: v0.2 section-generation order
Neuroscience/patches/SRT_Neuro_NEURAL19_Preattentive_Gist_Binding_Report_Interface_v0_1.md
  - frontmatter target_documents
```

因此不是“只剩一张旧 hook”，而是 **1 hook + 1 active construction instruction + 1 patch frontmatter** 的三表面竞争规范。它们应在任何 N1–N13 施工决定之前统一标注 obsolete / superseded；仍不得据此创建 N1–N12 或 N1–N13 文件。

### 5.2 机制簇分类

以下分类允许交叉，不把所有 patch 强行排成单一解剖或因果流水线：

| Mechanism cluster | Members | Current judgment |
|---|---|---|
| A. selection-ready geometry / representation | NEURAL18；PH-MR01 作为跨域阈值审计 | capacity / decodability != selection / anchoring |
| B. embodied eligibility / temporal integration | **NEURAL23 + NEURAL30** | 短时标上游 eligibility → 下游 integration/closure；不是固定 consciousness frame |
| C. plasticity / historical writeback | N10、N11、NEURAL19、NEURAL20、NEURAL25、NEURAL27、NEURAL29 | encoding / stabilization / transformation / authority / future use 必须拆开 |
| D. astrocyte / metabolic support | N12、NEURAL21、NEURAL22 | supply / substrate / payment / support topology；不等同 Psi_f 或 selector |
| E. object identity / re-identification | **NEURAL28** | stable address / re-entry != static copy / object neuron |
| F. memory transformation | **NEURAL29** | retention != transformation；generativity != factivity |
| G. candidate accessibility / control authority | **NEURAL25**；NEURAL26 提供上游 capacity constraint | representation / accessibility / authority / expression / write-back 分离 |
| H. prospective historical efficacy | **NEURAL27**；HCLR01 为跨域方法 bridge | retained memory != active history use != HEF-3/4 proof |
| I. consciousness / hard-problem guards | CONSC14、NEURAL24、NEURAL30 | affect / integration / report / bearing != phenomenality proof |
| J. measurement-admission guards | NEURAL16、NEURAL17、NEURAL18；NEURAL26 proxy guard | BOLD/HGA/decodability/entropy/connectivity require source and proxy gates |

### 5.3 Memory / object / history chain

当前 hardening index 已明确推荐：

```text
NEURAL28: identity formation / re-identification / relational re-entry
-> NEURAL29: retention / transformation / decontextualization / integration
-> NEURAL25: accessibility / authority / expression / write-back
-> NEURAL27: prospective history-use / path-bias readout
```

该链已成熟到足以成为 N1–N13 **cluster-specific baseline probe** 的题目来源，原因不是 patch 数量，而是四个阶段各自有：

- 独立的负控；
- 明确的失败条件；
- 与前后阶段的非同一关系；
- 当前 hardening index 的去材料化结构建议；
- 可进入 Neural CompactCore / predictions 的明确落点。

NEURAL26 必须保持正交：它约束全局 dynamical capacity，不是这条链中的第五个串行阶段。

已有 08-08 `nd` probe 只覆盖到 NEURAL18、NEURAL23 及当时节点题组；它证明两项材料区分已可用，也直接推翻“无 hook / planned file 不存在所以不可达”。它**没有**测试 NEURAL28→29→25→27 的完整关系、NEURAL23→30 的新增闭合关系，或 N1–N13 统一压缩是否产生净判别增益。

NEURAL23 + NEURAL30 是另一条短时标支链：

```text
embodied phase-dependent eligibility
-> chronology-preserving temporal integration
-> flexible closure / integrated percept-related state
```

它可以在对象形成之前供给条件，但不能从 phase、P300、decoder 或 report 直接推出 consciousness。

### 5.4 Probe gate / synthesis verdict

```text
N1-N13 cluster = PROBE CANDIDATE
N1-N13 synthesis = NOT YET
```

下一步只授权冻结命题组、反刷分正例、预算与 rubric，并在 current main 上跑 baseline。不得把 `NODE-NEURAL-DECODABILITY` 的既有 `observed` 或 NEURAL18/23 的样本内成功自动转移给整个新簇。

处置必须按 protocol：Case A（baseline 全部可答）停止施工；Case B（内容存在、bounded 失败）只修活跃路由／压缩；Case C（unconstrained 也失败）才考虑 bounded synthesis；Case D 则降级为档案。无论哪一类，若方案要求把 NEURAL18–30 机械串成单一阶段、把 NEURAL26 串行化、把 proxy 当 SRT primitive、或直接修改 canonical owner，都应停止并重新缩小范围。

---

## 6. AI delta

### 6.1 Current architecture cluster

现有 patch 形成以下稳定分解：

```text
AIEVID01: evidence provenance / target-overlap discount
-> AIREASON01: semantic readability / causal contribution / mechanism correspondence / normative validity
-> AIGOAL01: goal completion / bounded selection / goal-space generation
-> AIRESEL01: re-selection protection / standard-RL reduction boundary
-> AICONSC01: stake-proxy / same-bearer / non-fungible-loss gate
```

实际落地并不均匀：

- AIEVID01 已进入 `AI/AI_POSITIONING_NOTE.md` 的 evidence-provenance note。
- AIREASON01 已进入 `Bridge/SRT_Context_Coherence_Intelligence_Interface.md`。
- `AI/SRT_AI_Claim_Status.md` 已有 novelty / goal-space / ownership / stake ladder，但 AIGOAL01 hook 仍全部 pending，不能把语义相似当作 hook closure。
- AIRESEL01 目前只存在于 patch；root recent-material index、CompactCore、Claim Status、Positioning Note 和 bridge 均未命名它。
- AICONSC01 hook pending；它应作为 stake/subjecthood 边界，而不是推理架构的核心阶段。

### 6.2 CompactCore / index judgment

```text
Does a unified AI hardening index exist?  NO
Is one necessary now?                     NO
Is Architecture CompactCore + root index sufficient?  UNDECIDED for the delta; probe first
```

原因：当前 root recent-material index 已承担 AI material navigation；active manifest 也已有 `NODE-AI-REASONING`。再建一个目录对称的 index 不增加 owner、fast route 或行为证据。

现有 `NODE-AI-REASONING` 已在三次 bounded baseline 中 24/24 通过；AIEVID01 / AIREASON01 是 08-08 明确推翻的前两次静态假阴性，不能因无 hook 再列为 absorption 缺口。真正未决的是 AIGOAL01 / AIRESEL01 / AICONSC01 的增量区分是否已可由现有 Claim Status、Positioning、bridge 与 patch route 取得。应先 probe；只有 Case B/C 才讨论 CompactCore hardening 或内容吸收。若届时施工，仍须先用 architecture-state rule 收紧 CompactCore 中未限定的旧措辞。

结论：

```text
AI Architecture CompactCore absorption = NOT YET / PROBE CANDIDATE
new AI hardening index = NO-GO
```

既有 `NODE-AI-REASONING` 为 `active_complete / robustly_observed`；它证明现有 AIEVID/AIREASON 判别可用，但不证明本轮新增 AIGOAL/AIRESEL/AICONSC 已生效，也不授权先改 CompactCore 再测试。

---

## 7. Core / Core_Law delta

### 7.1 COLL08

COLL08 当前 hook 为 `landed`，且两个 anchor 均存在：

```text
Core_Law/SRT_Collective_Selection.md §4.8a Situated individuation diagnostic
Core_Law/SRT_Reference_Scaling.md NTIC guardrail
```

其 SRT-native 增量已经进入 owner：component individuation 要读成 coupling-qualified embedded non-redundancy；raw positive NTIC 不是单调 agency scalar。

但 `NODE-SOCIAL-L2` 仍为 `partially_active / untested`。因此：

```text
local landing complete
!= cross-domain synthesis complete
```

当前不建议另建 collective synthesis。未来只有在 COLL08 与 PH-IND、SOC-COG03、collective bearer gate 形成新的非重复命题时，才重开跨域综合。

### 7.2 Current-authority collision discipline

新 PH-IND03 / PH-DIFF01 hook 都指向 `Core_Law/SRT_Individuation.md`，但该 owner 是高承重文件，且当前仍带有需要按最新 epsilon / P1-T07 authority 精确读取的旧负担表达。该 landing 应在独立 hardening pass 中完成，不得由本材料审计把 patch 原文复制进去。

`Core/SRT_OPEN_TENSIONS.md` 的 Gate A/B/C 仍是 author-decision tensions。它们不是“材料尚未整合”的证据，也不是本轮 Top 5 中可由审计自行解决的任务。

---

## 8. Physics delta

扫描范围包括 P03–P08、E01–E05、QBox、REP01、THERM01，以及 B 类 RaQM watch material。

当前 physics hardening index 仍明确规定：

```text
later v0.2 synthesis
only once at least one E05 falsification window returns a discriminator
```

当前没有该 discriminator。P03–P08 是 bridge/ontology hardening，E01–E05 是 non-canonical extensions，QBox 是 structural analogy，REP01 / THERM01 是 representation / measurement guardrail。它们都不能由 patch 数量升级为 evidence 或 canonical support。

结论：

```text
Physics synthesis = DEFERRED
Physics/SRT_Physics_Bridge_v0_2.md = do not create now
```

---

## 9. Historical March–April survivor audit

March–April 有 **107 条 A**。机器优先 survivor check 结果：

```text
current target path resolves: 107 / 107
exact historical landing label still found in named target: 32 / 107
target exists but exact label is absent or not machine-verifiable: 75 / 107
missing original target: 0
```

这组结果不能读成“107 条都已 active”：

- 32 条只能证明具名 owner label 仍在，不能证明它进入 fast/router/context bundle。
- 75 条优先记作 `legacy_provenance_only` 或 `unclear`，因为 split / annex / heading migration 与正文改写会使旧落点标签失效；不因此生成 75 条施工任务。
- 真正值得处理的是 Table D 中与 current authority 冲突的 survivor，而不是对所有旧 A 做人工重写。

原则继续保持：

```text
historical "已融入"
!= current active assimilation
```

---

## 10. Active-theory node assessment

| Cluster | Existing node | New node now? | Reason |
|---|---|---|---|
| AI reasoning/evidence/goal/reselection | `NODE-AI-REASONING` | **No** | existing node is robustly observed; probe AIGOAL/AIRESEL/AICONSC increment before any owner/compact change |
| Neuroscience memory/object/history | `NODE-NEURAL-DECODABILITY` is adjacent | **Not yet** | cluster-specific baseline not run; owner/compact absence is not decision evidence |
| Philosophy individuation/representation/bearer | `NODE-SUBJECTHOOD` is adjacent | **Not yet** | cluster-specific baseline not run; current subjecthood state does not decide the new proposition set |
| Collective situated individuation | `NODE-SOCIAL-L2` | **No** | COLL08 is locally landed; broader node remains partial for other reasons |
| Physics bridge family | `NODE-PHYSICS-MEASUREMENT` | **No** | physics node exists; new bridge material remains deferred/guardrail |

本轮不创建节点。立项顺序不是先补 owner / fast / router 再测，而是先冻结 SRT-native proposition 与边界，跑 current-main bounded baseline，再按 Case A/B/C/D 决定是否需要 active-node proposal。Case A 必须停止施工；Case B 才修 retrieval/compression；Case C 才讨论内容写回；行为状态只由真实 run record 决定。

---

## 11. Table B — Real clusters / synthesis probe candidates

| Cluster | Member patches | Current owners | Engineering topology（not gap evidence） | Bounded probe status | Native SRT increment | Risk | Recommended action | Priority |
|---|---|---|---|---|---|---|---|---|
| **Neuroscience N1–N13: memory/object/history + short-timescale eligibility/closure** | N1–N12；CONSC14；NEURAL15–30，核心 delta 为 23–30 | neuroscience hardening index；Neural/Consciousness CompactCore；predictions；NEURAL25 protocol | `N1_N13_v0_2` absent；new hooks pending；old N1–N12 spec survives on three surfaces | **cluster-specific not_run**；NEURAL18/23 sampled in 08-08 `nd` and passed | separates geometry, eligibility, integration, transformation, accessibility, authority, prospective efficacy and global capacity | proxy identity；false serial anatomy；phenomenality overclaim | freeze exact cluster propositions and run baseline; build only on Case B/C | **P1 probe candidate / synthesis NOT YET** |
| **Individuation / Representation / Bearer Formation** | PH-CONSC03/04；PH-IND01/02/03；PH-DIFF01；PH-MEM01；PH-MR01；SOC-COG03 | Individuation owner；Subjecthood interface；Mental Representation annex；Social Cognition owner | no bounded synthesis owner；no explicit fast landing for the combined chain | **cluster-specific not_run** | distinguishes preformation, individuation, re-identification, historical transformation, bearer and phenomenality residual | importing Deleuze/Simondon ontology；duplicating Agency synthesis；solving P0-04 by label | scope proposition/rubric, then baseline probe; synthesize only on Case C | **P2 probe candidate / synthesis NOT YET** |
| **AI evidence / trace / goal / re-selection architecture** | AIEVID01；AIREASON01；AIGOAL01；AIRESEL01；AICONSC01 as boundary | AI Positioning；AI Claim Status；Context-Coherence bridge；AI Architecture CompactCore | AIGOAL/AICONSC hooks pending；AIRESEL patch-only；CompactCore has authority collision | **cluster-specific not_run**；existing AIEVID/AIREASON node baseline is robustly observed | evidence provenance → trace-role separation → completion/selection/generation → reorientation → stake gate | architecture-state overgeneralization；functional selection → stake leap | probe AIGOAL/AIRESEL/AICONSC delta; no CompactCore edit on Case A | **P2 probe candidate / absorption NOT YET** |
| **Bearer / phenomenality residual pressure** | PH-CONSC03/04；NEURAL24；NEURAL30；AICONSC01 | HardProblem Epistemology；Subjecthood interface；Consciousness owner | delta hooks pending | **standalone proposition set not_run** | preserves `bearing != phenomenality` and supplies deletion / comparator tests | accidentally declaring a solution to the hard problem | keep as probe pressure items, not a positive standalone theory | **P3 / no standalone workline** |

Not listed as synthesis candidates:

- COLL08, because its local owner landing already exists and the current delta adds no distinct second collective synthesis.
- Physics, because E05's named promotion condition has not fired.
- PH-AG01–04 / PH-SEM01, because Agency–Subjecthood v0.2 already exists.

---

## 12. Table C — Pending hooks

The following counts are unresolved **landing-ledger target occurrences**, not “backlog item” counts. Classification precedence is audit-local: obsolete → future synthesis → missing → canonical/high-risk → parked → normal owner.

| Target class | Target occurrences | Hooks involved | Typical examples | Operational reading |
|---|---:|---:|---|---|
| normal owner landing | **29** | 18 | Neural predictions；Subjecthood interface；Core 25；NEURAL25 protocol | eligible for the named owner workline; not automatically urgent |
| future synthesis target | **42** | 26 | Neural CompactCore / N1–N13；Agency/Philosophy future synthesis；Physics Bridge v0.2 | planned target only; wait for baseline Case B/C, not ordinary backlog |
| canonical/high-risk target | **15** | 13 | `_SRT_T_DIR_CANONICAL.md`；`Core/SRT_OPEN_TENSIONS.md`；Core_Law owners | requires edit protocol / author gate; audit cannot land it |
| parked target | **13** | 9 | active book body；ChoiceMap incubation；paused experiment extension | wait for workline/revival trigger |
| missing target | **0** | 0 | — | no currently unplanned missing file after classification |
| obsolete target | **2** | 2 | old `N1_N12_v0_2` name；withdrawn subjective-time placeholder | normalize ledger when the relevant hook is next edited; do not create obsolete files |

Hook-level summary remains:

```text
landed hooks = 12
partial hooks = 3
pending hooks = 29
```

The 101 unresolved/withdrawn ledger target occurrences above include targets inside partial hooks and one withdrawn target inside an otherwise landed hook; they must not be equated with 101 theory tasks.

Table C is deliberately hook-ledger scoped. A broader corpus scan finds the old `N1_N12_v0_2` name on three live surfaces: one NEURAL19 hook, the active N10–N12 integration instruction (including a section-generation plan), and NEURAL19 patch frontmatter. The latter two are outside `*/hooks/`, so they do not change Table C's counts but must be included in the topology repair.

---

## 13. Table D — Historical residual conflicts

| Material / patch | Old wording or landing collision | Current authority | Risk | Action |
|---|---|---|---|---|
| `SRC_2026_06_11_Philosophy_Deacon_IncompleteNature_Norton.md` | describes direction/community/order as externally testable through “三判据” | `Core_Law/SRT_Selection_Argument.md §7b.2`; `Core/SRT_OPEN_TENSIONS.md §11` — four criteria | old book-provenance shorthand can be retrieved as current theory | mark `conflict_with_current_authority`; revise only when card/book-provenance surface is next touched |
| `SRC_2026_06_11_Philosophy_BlindSpot_Frank_Gleiser_Thompson_MITPress.md` | same “三判据” survivor | same four-criterion owner | same | same; no canonical edit in this PR |
| AIGOAL01 / AIRESEL01 / AICONSC01 → `AI/SRT_AI_Architecture_CompactCore.md` | landing target still uses unqualified attention-selection isomorphism, “Value 没有 d”, and architecture-level scaling/judgment verdicts | `AI/SRT_AI_Claim_Status.md`; `AI/AI_POSITIONING_NOTE.md` architecture-state rule | absorbing new patches without first scoping owner would revive an all-AI theorem voice | make authority-scoping the prerequisite of AI CompactCore absorption |
| PH-IND03 / PH-DIFF01 → `Core_Law/SRT_Individuation.md` | high-risk owner still carries dense P1-T07 / epsilon burden and strong phase language; patch landing could silently alter current authority | `_SRT_SYMBOL_TABLE.md` epsilon namespace rule；P1-T07 owner；canonical freeze/edit protocol | external philosophy could be made to bear a theorem/primitive load it does not have | land only in a dedicated owner hardening pass; retain external-convergence guards |

Targeted scans found **no affirmative material-layer residual** that states `nu_block` positivity as a theorem consequence, says P1-T07 proves `epsilon_pg > 0`, uses unindexed `H(L0)` quantitatively, or asserts an unqualified global optimum. Hits for direction/non-outsourcing in recent patches were guardrails or candidate discriminators, not the prohibited identities.

Gate A/B/C remain open authority decisions. Their presence is not classified as material assimilation debt.

---

## 14. Table E — No-action / correctly parked

| Class | Count / scope | Why no action now | Revival rule |
|---|---:|---|---|
| Official B with explicit named trigger, unmet | **9** | B is parked evidence, not backlog | only the named workline event may reopen |
| Legacy B without current-form named trigger | **18** | metadata clarity gap does not authorize close-read or promotion | repair trigger metadata only when item is next touched; do not infer firing from calendar |
| B2 intersection | **9** | guardrail-only component; overlaps B1 on mixed verdicts | reopen only for the named boundary problem |
| B3 intersection | **1** | public-prose-only component | writing/public workline only |
| B whose trigger is verified fired | **0** | no repository event evidence | none this round |
| Original-verdict C | **50** | original verdict is authoritative；CSV operational split = 30 `rejected` + 20 `superseded_or_duplicate` | new materially distinct source required |
| EC cards | **11; accepted=0** | correct hardness-conservation state | separate evidence review, never coverage pressure |
| Physics P03–P08 / E01–E05 / QBox / REP01 / THERM01 | full family | analogy/bridge/guardrail; E05 discriminator absent | named physics promotion condition |
| ChoiceMap incubation bundle | 1 indexed bundle, multiple files | product line remains parked; no trigger record fired | IRP / ChoiceMap workline restart |

Old B calendar/re-review dates are not treated as revival events. Under the current governance rule, a trigger is a named workline event, not the passage of a date.

---

## 15. Recommended next assimilation actions

Only five actions are recommended.

### 1. Run three cluster-specific bounded baseline probes before any build

- **Action**: freeze proposition sets, prohibited inferences, anti-gaming positives and rubrics for Neuroscience N1–N13, Philosophy individuation/representation/bearer, and the AI AIGOAL/AIRESEL/AICONSC delta; then run each on current main under the 6-file / 2-navigation budget.
- **Why now**: 08-08 produced five consecutive static-audit false negatives, including NEURAL18, NEURAL23 and REP01; the present cluster decisions otherwise repeat the invalid inference from missing hook / owner / planned file.
- **Expected theoretical gain**: distinguish no-gap Case A from retrieval Case B, content Case C and archive Case D before spending theory-edit capacity.
- **Risk**: designing questions that merely quote patch IDs, changing rubrics after results, or transferring sampled-member success to the whole cluster.
- **Files likely involved**: bounded protocol; a new probe specification/run record; current owners and patches as read-only evidence.
- **GO condition**: all questions and thresholds are frozen before runs, include positive counterexamples, and record every file/navigation step.
- **NO-GO condition**: no SRT-native proposition can be stated without importing a source author's vocabulary, or the test cannot distinguish Cases A–D.

### 2. Normalize the competing N1–N12 construction topology

- **Action**: after the baseline disposition is known, replace or explicitly supersede the old N1–N12 target on all three live surfaces—not only the hook—and keep the result as navigation/governance repair unless Case C authorizes content work.
- **Why now**: one hook, one active construction instruction and one patch frontmatter currently compete with the N1–N13 hardening index.
- **Expected theoretical gain**: none by itself; it prevents two incompatible synthesis specifications from steering the next agent.
- **Risk**: treating path cleanup as evidence that N1–N13 content is needed, or creating either absent synthesis file to satisfy the ledger.
- **Files likely involved**: NEURAL19 hook; N10–N12 integration instruction; NEURAL19 patch; neuroscience hardening index.
- **GO condition**: the replacement target follows the probe's Case disposition and no theory body is created.
- **NO-GO condition**: cleanup would pre-commit the repository to N1–N13 before the baseline result.

### 3. Apply the probe disposition to Neuroscience N1–N13

- **Action**: Case A stop; Case B make the smallest routing/compression repair; Case C scope a bounded non-canonical synthesis; Case D preserve provenance and remove it from the active candidate list.
- **Why now**: the memory/object/history and short-timescale chains have enough explicit non-identities to be tested, while only NEURAL18/23 have prior sample-level probe evidence.
- **Expected theoretical gain**: a justified neural workline, if and only if the current theory actually lacks or cannot retrieve the distinctions.
- **Risk**: serializing NEURAL26, proxy/canonical identity, phenomenality inflation, or mistaking node-level success for all member coverage.
- **Files likely involved**: determined by the Case result; possible hardening index, compact route or future N1–N13 synthesis.
- **GO condition**: Case B or C with a reproducible failed item and explicit smallest repair.
- **NO-GO condition**: Case A; or any fix requires changing canonical `d/Psi_f/T_dir` or collapsing the mechanisms into one chain.

### 4. Apply the probe disposition to Philosophy individuation / representation / bearer

- **Action**: test the combined non-identities against current Individuation, Subjecthood, Mental Representation, Social Cognition and Agency owners; synthesize only under Case C.
- **Why now**: the patch family is coherent enough to test, but owner-path absence cannot show that its discriminations are absent.
- **Expected theoretical gain**: either demonstrate current semantic coverage or identify one bounded native gap without duplicating Agency–Subjecthood.
- **Risk**: `virtual/preindividual = L0`, `transduction = selection`, generativity→d, or solving phenomenality by imported labels.
- **Files likely involved**: probe record first; only a Case B/C result may nominate owner/compact files.
- **GO condition**: a frozen question fails for a bounded, source-independent SRT distinction and survives unconstrained diagnosis.
- **NO-GO condition**: Case A, or the proposed increment is mainly Deleuze/Simondon exposition.

### 5. Apply the probe disposition to the AI delta without rebuilding AIEVID/AIREASON

- **Action**: probe AIGOAL01/AIRESEL01/AICONSC01 against current Claim Status, Positioning, Context-Coherence bridge and Architecture CompactCore; preserve AIEVID01/AIREASON01 as already available evidence.
- **Why now**: the existing AI node is robustly observed, while the newer goal/reselection/stake combination is the only untested increment.
- **Expected theoretical gain**: determine whether the existing CompactCore already supports the ladder or needs a scoped routing/content repair.
- **Risk**: blanket all-AI verdicts, functional selection→Real Choice, re-selection→d, or treating architecture collision as proof of a content gap.
- **Files likely involved**: AI probe specification/run record; CompactCore or router only under Case B/C.
- **GO condition**: Case B/C identifies a specific failed discrimination and the repair is architecture-state qualified.
- **NO-GO condition**: Case A; no new hardening index or CompactCore append pass is then permitted.

---

## 16. Explicit answers to the five decision questions

| Question | Answer |
|---|---|
| Is Neuroscience N1–N13 v0.2 mature now? | **UNDECIDED — cluster is a bounded-probe candidate; synthesis = NOT YET.** |
| Should PH-IND / PH-DIFF / PH-MEM / PH-MR form a bounded synthesis? | **UNDECIDED — a proposition-level probe is warranted; synthesis is authorized only by Case C.** |
| Should AI Architecture CompactCore absorb AIEVID/AIREASON/AIGOAL/AIRESEL? | **NOT YET — AIEVID/AIREASON are already available; probe the AIGOAL/AIRESEL/AICONSC delta before any CompactCore edit.** |
| Is a separate collective-selection synthesis still warranted? | **NO, not now — COLL08 is locally landed; wait for a distinct cross-domain increment.** |
| Does Physics stay deferred? | **YES — E05 discriminator trigger has not fired.** |

---

## 17. Validation

| Check | Result | Detail |
|---|---|---|
| material-log consistency | **PASS** | 13 parts；latest `2026-08_Part04:7`；226 / A149 / B27 / C50 |
| active-theory assimilation checker | **PASS (report-only)** | Axis A 8 complete / 6 partial / 1 engineered / 1 author gate；Axis B unchanged；one pre-existing `NODE-BOOK-BACKFLOW` route warning |
| frontmatter | **PASS** | baseline known 1440 / new 0 / retired 2；this PR adds no warning |
| registry consistency | **PASS** | errors 0 / warnings 0 |
| integration-hook closure | **PASS** | 44 hooks；errors 0；checker tests pass |
| split metadata refresh check | **PASS** | would-change 0；two documented README skips |
| split freshness | **PASS** | errors 0 / warnings 0 under strict metadata |
| context bundle freshness | **PASS** | STATUS repair forced regeneration；9 generated files byte-identical to `inputs_digest=5f08db5b860ab960` |
| forbidden local noise | **PASS** | errors 0 / warnings 0 |
| full governance preflight | **PASS** | `failures=0` with `--skip-write-report --strict-split-metadata` |
| `git diff --check` | **PASS** | no whitespace errors |

Commands:

```bash
uv run python scripts/check_material_log_consistency.py
uv run python scripts/check_active_theory_assimilation.py --reachability
uv run python scripts/check_frontmatter.py --baseline Governance/Frontmatter_Warning_Baseline.txt --fail-on-new-warnings
uv run python scripts/check_registry_consistency.py
uv run python scripts/check_hooks.py
uv run python scripts/refresh_split_metadata.py --check
uv run python scripts/check_split_freshness.py --strict-metadata
uv run python scripts/build_srt_context_bundles.py --check
uv run python scripts/check_forbidden_noise.py --strict-worktree
uv run python scripts/governance_preflight.py --skip-write-report --strict-split-metadata
git diff --check
```

The active-theory warning and the 1440 frontmatter baseline entries are repository-wide pre-existing state. They were not introduced by this PR. The STATUS repair forced a script-only refresh of 8 bundles + README after rebasing over merged #780; no generated-file conflict remains.

---

## 18. Machine-readable audit notes

The companion CSV contains all 229 physical dated-log rows and the minimum requested fields:

```text
date
source
source_id
domain
original_verdict
sourcecard
patch
hook
hook_integration_status
landing_targets
owner_landing
compact_or_fast_layer
router_or_deep_map_route
active_theory_node
open_tension
current_disposition
next_action
notes
```

Important CSV semantics:

- The CSV unit is a **dated Material Log row**, not a patch. It cannot by itself validate Table B's patch-cluster membership or semantic conclusion.
- 52 patch files exist; 11 have no corresponding CSV row: AIREASON01, AIRESEL01, NEURAL19, NEURAL21, PH-AG01, PH-IND02, and Physics P03/P04/P05/P07/P08. Prose cluster analysis used a separate full patch scan; the CSV is not presented as coverage of those 11 files.
- `official_declared_scope=no` marks the three historical physical rows outside a split's declared count.
- `claimed_in_log:` preserves an old Material Log landing claim; it is not machine proof of current active assimilation.
- `pending_target:` records a fast/compact landing named by a pending hook; it does not say that the target already contains the increment.
- `unverified_target:` records a plausible current target whose material-specific landing was not verified in this audit.
- `conflict_with_current_authority` is recorded in `notes`, not introduced as a new disposition.
- `active_theory_node` records the nearest current node relation; it does not assert that the specific material increment is assimilated into that node.
- `probe_2026_08_08:` records a real bounded route inherited from the 08-08 run record; it is behavioral evidence for the sampled proposition, not for every member of its cluster.
- blank fast/router fields mean “not verified for this material increment”, not necessarily “the domain has no route”.

---

## 19. Non-actions preserved

This audit modifies no canonical definition, `d/Psi_f/T_dir` owner, OPEN_TENSIONS author decision, A/B/C verdict, book body, submitted paper, SourceCard, active-theory Axis B evidence, or EC acceptance state. Apart from the minimal STATUS statistic/navigation correction described in §3, it changes no existing repository content. It creates no Physics, Neuroscience, Philosophy or AI theory synthesis and deletes no material.
