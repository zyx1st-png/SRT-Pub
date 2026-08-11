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
source_of_truth: "origin/main @ 13d313389c06150bdeadc2ff7f1592ea7fd8d7d1"
dependency:
  - SRT-OPS-AUDIT-ACTIVE-THEORY-ASSIMILATION-2026-08-06
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
> **行为证据纪律**：本轮没有执行新的 bounded retrieval run，因此没有改写任何节点的 Axis B。`untested` 不得因静态文件存在而升级；既有 `observed` / `robustly_observed` 只按现有 run record 继承。

---

## 0. 结论先行

截至基线 `13d313389c06150bdeadc2ff7f1592ea7fd8d7d1`：

- 正式 Material Log 为 **226** 条：A **149** / B **27** / C **50**。
- 档案化层为 **77 SourceCards**；工程化层为 **52 patches / 44 hooks**，hook 状态 **landed 12 / partial 3 / pending 29**。
- 相对 2026-08-06 审计口径，正式材料净增 **19 条，全部为 A**；SourceCard `+18`、patch `+21`、hook `+20`。新增 20 张 hook 全部仍为 `pending`，所以材料增长尚未直接转化为 owner landing。
- 真正达到“值得压缩为稳定 SRT 结构”的三个簇是：
  1. Neuroscience N1–N13，特别是 memory/object/history 链与 embodied-eligibility/temporal-closure 支链；
  2. Philosophy 的 individuation / representation / bearer formation 簇；
  3. AI 的 evidence provenance / reason-trace / goal selection / re-selection / stake gate 架构簇。
- `Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md` 当前仍不存在；本审计判断 **N1–N13 synthesis = GO**，但本 PR 不创建它。
- 新的 bounded `Individuation / Representation / Bearer Formation synthesis` **值得建立**，但不得重复 Agency–Subjecthood v0.2，也不得把 Simondon / Deleuze 的外部趋同改写成 SRT native identity。
- AI Architecture CompactCore **应在一次 bounded hardening pass 中吸收** AIEVID01 / AIREASON01 / AIGOAL01 / AIRESEL01；AICONSC01 作为 stake/subjecthood 边界接口附接。当前不需要新建 `AI/_SRT_AI_Hardening_Index.md`。
- COLL08 已在 `SRT_Collective_Selection.md` 与 `SRT_Reference_Scaling.md` 完成局部落地；“局部落地完成”不等于跨域综合完成，但目前**不值得为了文件对称再建一份独立 collective synthesis**。
- Physics hardening index 的触发条件未改变：E05 尚无已登记 discriminator，故 **Physics synthesis remains deferred**。
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
BASE_SHA=13d313389c06150bdeadc2ff7f1592ea7fd8d7d1
```

原工作区 main 含用户未提交改动，本审计因此从该 SHA 建立独立 worktree 与分支，未清理、覆盖或带入原工作区改动。

执行时 open PR 中，PR #780 正在修改 `Operations/Context_Bundles/`、`Operations/Archive_Records/Large_File_Audit_2026-05-09.md` 与 `Operations/Proposals/`。本审计不把其未合并内容当作 main，不修改这些路径，也不手工混入其派生内容。

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

`STATUS.md §Fast Status` 的摘要数字仍写作较早的 `robustly_observed=2 / observed=3 / effectively_assimilated=2`，与当前 manifest + checker 的 `3 / 2 / 3` 不一致。该差异属于 operations status drift；本 PR 不修改 STATUS。

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

1. **这些 patch 已形成 synthesis cluster。** 共同 SRT-native 增量不是“哲学家都谈个体化”，而是把预成对象拒绝、可重新识别的对象稳定、历史变换、承载位置与现象性残余拆成可判别环节。
2. **它们尚未形成 current-theory synthesis。** 新 ID 在列出的 owner 中没有直接落地；现有 owner 只能提供地基，不能把 pending patch 自动算作 active。

结论：未来建立一个 bounded `Individuation / Representation / Bearer Formation synthesis` **有必要**。它应明确排除 Agency–Subjecthood 已完成内容，并把 phenomenality 留作 residual，不写成 bearer 的自动结果。

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

审计结论：二者属于高价值 P3 hardening / pressure model。它们的共同出现证明“值得做 SRT-native adjudication”，不证明其哲学概念已经成为 SRT native proposition。

---

## 5. Neuroscience delta

### 5.1 Authoritative target

当前 authoritative hardening index 指向：

```text
Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md
```

执行时该文件仍不存在。旧的 `N1_N12_v0_2` 也不存在，并且只剩一张旧 hook 仍指向该过时名字；该 target 在本审计中归为 `obsolete target`，不是再创建 N1–N12 的理由。

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

该链已成熟到足以进入 N1–N13 synthesis，原因不是 patch 数量，而是四个阶段各自有：

- 独立的负控；
- 明确的失败条件；
- 与前后阶段的非同一关系；
- 当前 hardening index 的去材料化结构建议；
- 可进入 Neural CompactCore / predictions 的明确落点。

NEURAL26 必须保持正交：它约束全局 dynamical capacity，不是这条链中的第五个串行阶段。

NEURAL23 + NEURAL30 是另一条短时标支链：

```text
embodied phase-dependent eligibility
-> chronology-preserving temporal integration
-> flexible closure / integrated percept-related state
```

它可以在对象形成之前供给条件，但不能从 phase、P300、decoder 或 report 直接推出 consciousness。

### 5.4 GO / NOT YET

```text
N1-N13 synthesis = GO
```

GO 的含义仅是“值得启动 bounded non-canonical synthesis workline”，不是提升 N1–N13 为 canonical，也不是把 `NODE-NEURAL-DECODABILITY` 的既有 `observed` 行为证据自动转移给新簇。

NO-GO 条件：若施工方案要求把 NEURAL18–30 机械串成单一阶段、把 NEURAL26 串行化、把 proxy 当 SRT primitive、或直接修改 canonical owner，则应停止并重新缩小范围。

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
Is Architecture CompactCore + root index sufficient?  YES, after bounded hardening
```

原因：当前 root recent-material index 已承担 AI material navigation；active manifest 也已有 `NODE-AI-REASONING`。再建一个目录对称的 index 不增加 owner、fast route 或行为证据。

真正需要的是一次 bounded `AI/SRT_AI_Architecture_CompactCore.md` hardening：先用 `AI/SRT_AI_Claim_Status.md` 的 architecture-state rule 收紧 CompactCore 中未限定的“Transformer 没有 d / scaling 不会生成 judgment / attention-selection isomorphism”表述，再吸收 AIEVID / AIREASON / AIGOAL / AIRESEL。否则新 patch 会落入一个比当前 authority 更宽、更强的旧架构口径。

结论：

```text
AI Architecture CompactCore absorption = GO, with authority-scoping prerequisite
new AI hardening index = NO-GO
```

既有 `NODE-AI-REASONING` 为 `active_complete / robustly_observed`，但这只证明现有节点可用；不证明本轮新增 AIGOAL/AIRESEL/AICONSC 已生效。

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
| AI reasoning/evidence/goal/reselection | `NODE-AI-REASONING` | **No** | existing node and bounded behavior evidence already exist; absorb delta into current owner/compact route |
| Neuroscience memory/object/history | `NODE-NEURAL-DECODABILITY` is adjacent | **Not yet** | candidate after N1–N13 owner + compact/router route; current patches are not one active node by themselves |
| Philosophy individuation/representation/bearer | `NODE-SUBJECTHOOD` is adjacent | **Not yet** | no bounded synthesis owner or fast route; current subjecthood node is only partially active |
| Collective situated individuation | `NODE-SOCIAL-L2` | **No** | COLL08 is locally landed; broader node remains partial for other reasons |
| Physics bridge family | `NODE-PHYSICS-MEASUREMENT` | **No** | physics node exists; new bridge material remains deferred/guardrail |

本轮不批量创建节点。只有在 cluster 获得 SRT-native proposition、owner、fast/compact route、router/deep-map route，并摆脱单篇材料复述后，才进入 active-node proposal。Axis B 在那之后仍从 `untested` 开始，除非另有真实 bounded run。

---

## 11. Table B — Real synthesis candidates

| Cluster | Member patches | Current owners | Missing landing | Native SRT increment | Risk | Recommended action | Priority |
|---|---|---|---|---|---|---|---|
| **Neuroscience N1–N13: memory/object/history + short-timescale eligibility/closure** | N1–N12；CONSC14；NEURAL15–30，核心 delta 为 23–30 | neuroscience hardening index；Neural/Consciousness CompactCore；predictions；NEURAL25 protocol | `N1_N13_v0_2` absent；new hooks pending | separates geometry, eligibility, integration, transformation, accessibility, authority, prospective efficacy and global capacity | proxy identity；false serial anatomy；phenomenality overclaim | create bounded non-canonical N1–N13 synthesis in a separate PR | **P1 / GO** |
| **Individuation / Representation / Bearer Formation** | PH-CONSC03/04；PH-IND01/02/03；PH-DIFF01；PH-MEM01；PH-MR01；SOC-COG03 | Individuation owner；Subjecthood interface；Mental Representation annex；Social Cognition owner | no bounded synthesis owner；no fast route | distinguishes preformation, individuation, re-identification, historical transformation, bearer and phenomenality residual | importing Deleuze/Simondon ontology；duplicating Agency synthesis；solving P0-04 by label | write a scope/adjudication packet, then one bounded synthesis if scope passes | **P2 / warranted** |
| **AI evidence / trace / goal / re-selection architecture** | AIEVID01；AIREASON01；AIGOAL01；AIRESEL01；AICONSC01 as boundary | AI Positioning；AI Claim Status；Context-Coherence bridge；AI Architecture CompactCore | AIGOAL/AICONSC hooks pending；AIRESEL patch-only；CompactCore not yet scoped | evidence provenance → trace-role separation → completion/selection/generation → reorientation → stake gate | architecture-state overgeneralization；functional selection → stake leap | harden and extend existing Architecture CompactCore; do not create a new index | **P2 / GO with prerequisite** |
| **Bearer / phenomenality residual pressure** | PH-CONSC03/04；NEURAL24；NEURAL30；AICONSC01 | HardProblem Epistemology；Subjecthood interface；Consciousness owner | all delta hooks pending | preserves `bearing != phenomenality` and supplies deletion / comparator tests | accidentally declaring a solution to the hard problem | keep as a pressure-test subsection, not a positive standalone theory | **P3 / NOT YET as standalone** |

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
| future synthesis target | **42** | 26 | Neural CompactCore / N1–N13；Agency/Philosophy future synthesis；Physics Bridge v0.2 | wait for bounded synthesis workline; not ordinary backlog |
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
| Rejected C | **50** | original verdict is authoritative | new materially distinct source required |
| EC cards | **11; accepted=0** | correct hardness-conservation state | separate evidence review, never coverage pressure |
| Physics P03–P08 / E01–E05 / QBox / REP01 / THERM01 | full family | analogy/bridge/guardrail; E05 discriminator absent | named physics promotion condition |
| ChoiceMap incubation bundle | 1 indexed bundle, multiple files | product line remains parked; no trigger record fired | IRP / ChoiceMap workline restart |

Old B calendar/re-review dates are not treated as revival events. Under the current governance rule, a trigger is a named workline event, not the passage of a date.

---

## 15. Recommended next assimilation actions

Only five actions are recommended.

### 1. Create the bounded Neuroscience N1–N13 v0.2 synthesis

- **Action**: create `Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md` in a separate PR, following the current hardening index structure.
- **Why now**: the memory/object/history sequence and the NEURAL23→30 short-timescale branch now have independent stages, negative controls, failure conditions and declared landings.
- **Expected theoretical gain**: one native neural architecture separating capacity, eligibility, integration, transformation, accessibility, authority and prospective efficacy.
- **Risk**: turning overlapping mechanisms into a mandatory serial anatomy; proxy/canonical identity; phenomenality inflation.
- **Files likely involved**: neuroscience hardening index; new N1–N13 synthesis; Neural/Consciousness CompactCore; predictions; NEURAL18–30 hooks.
- **GO condition**: preserve NEURAL26 as orthogonal, keep NEURAL23→30 separate from the longer memory chain, and make all proxy/claim-level guards explicit.
- **NO-GO condition**: synthesis requires modifying canonical `d/Psi_f/T_dir`, asserts behavior evidence for the new cluster, or collapses all patches into one scalar/stage chain.

### 2. Scope a bounded Philosophy individuation / representation / bearer synthesis

- **Action**: first write a short adjudication/scope packet; create the synthesis only if the scope cleanly excludes existing Agency–Subjecthood content.
- **Why now**: PH-IND/DIFF/MEM/MR and PH-CONSC03/04 now form a shared explanatory sequence rather than isolated comparisons.
- **Expected theoretical gain**: a native account of how non-preformed structure becomes re-identifiable, history-bearing and bearer-qualified while leaving phenomenality residual.
- **Risk**: `virtual/preindividual = L0`, `transduction = selection`, generativity→d, or solving P0-04 by imported vocabulary.
- **Files likely involved**: philosophy hardening index; Individuation owner; Subjecthood interface; Mental Representation annex; Social Cognition owner; Agency synthesis only as a boundary reference.
- **GO condition**: one SRT-native proposition, explicit owner split, no duplicated Agency synthesis, and external-philosophy guards retained.
- **NO-GO condition**: the draft is mainly Deleuze/Simondon exposition or needs a new primitive/equation to connect the material.

### 3. Harden and extend the existing AI Architecture CompactCore

- **Action**: reconcile the CompactCore with AI Claim Status first, then absorb AIEVID01/AIREASON01/AIGOAL01/AIRESEL01; attach AICONSC01 as a stake gate.
- **Why now**: the architecture cluster has a stable ladder, but AIRESEL remains patch-only and current owner wording predates the architecture-state hardening.
- **Expected theoretical gain**: a single fast AI route that separates evidence, trace function, goal competence, reorientation, standard-RL reduction and constitutive stake.
- **Risk**: blanket all-AI verdicts; functional selection→Real Choice; re-selection protection→d; architecture-state leakage.
- **Files likely involved**: AI Architecture CompactCore; AI Claim Status; AI Positioning Note; Context-Coherence bridge; Choice Generation bridge; root material index.
- **GO condition**: every claim declares architecture state and withdrawal conditions; no new hardening index is needed.
- **NO-GO condition**: the pass merely appends patch summaries or preserves unqualified theorem-like architecture claims.

### 4. Normalize hook topology after the three bounded decisions

- **Action**: retire the old N1–N12 target, preserve planned/parked/high-risk distinctions, and batch only normal owner landings authorized by the chosen synthesis scopes.
- **Why now**: 29 pending hooks contain 101 heterogeneous ledger target occurrences; treating them as one backlog would cause unsafe ordering.
- **Expected theoretical gain**: a truthful engineering→owner transition without reviving parked work or bypassing canonical gates.
- **Risk**: status laundering, creating missing files solely to satisfy hooks, or marking partial semantic overlap as landed.
- **Files likely involved**: the affected hooks, domain hardening indexes, hook-closure audit derivatives.
- **GO condition**: each landing includes anchor evidence and preserves target class.
- **NO-GO condition**: a batch operation touches canonical/high-risk, book, ChoiceMap or Physics targets without their own workline authorization.

### 5. Run a bounded active-layer routing pass after synthesis landing

- **Action**: after actions 1–3 land, decide whether the philosophy and neuroscience subclusters merit new active-theory nodes or should remain inside existing nodes; then add owner/compact/router routes and run bounded behavior tests.
- **Why now**: current material indexes make clusters searchable, but searchability is not declarative retrieval; creating nodes before owners would repeat the 2026-08-06 error.
- **Expected theoretical gain**: converts one or two completed syntheses from owner text into reliably retrievable theory.
- **Risk**: creating nodes for patch bundles, faking Axis B from static checks, or colliding with PR #780 context-bundle work.
- **Files likely involved**: active-theory manifest/checker outputs; router; deep map; relevant CompactCore; context bundles only after open-PR reconciliation.
- **GO condition**: native proposition + owner + fast layer + router/deep-map route all exist, followed by a real bounded run.
- **NO-GO condition**: any structural carrier is missing or the open context-bundle PR still overlaps the intended derivative edits.

---

## 16. Explicit answers to the five decision questions

| Question | Answer |
|---|---|
| Is Neuroscience N1–N13 v0.2 mature now? | **YES — GO for a bounded non-canonical synthesis; do not execute in this PR.** |
| Should PH-IND / PH-DIFF / PH-MEM / PH-MR form a bounded synthesis? | **YES — warranted after a scope/adjudication pass; do not merge Agency or phenomenality into it.** |
| Should AI Architecture CompactCore absorb AIEVID/AIREASON/AIGOAL/AIRESEL? | **YES — after owner wording is scoped through AI Claim Status; AICONSC is a boundary attachment.** |
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
| context bundle freshness | **PASS** | 9 generated files byte-identical to provenance `849a5e63 @ 2026-08-11` |
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

The active-theory warning and the 1440 frontmatter baseline entries are repository-wide pre-existing state. They were not introduced by this PR. No governance-generated derivative needed updating.

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

- `official_declared_scope=no` marks the three historical physical rows outside a split's declared count.
- `claimed_in_log:` preserves an old Material Log landing claim; it is not machine proof of current active assimilation.
- `pending_target:` records a fast/compact landing named by a pending hook; it does not say that the target already contains the increment.
- `unverified_target:` records a plausible current target whose material-specific landing was not verified in this audit.
- `conflict_with_current_authority` is recorded in `notes`, not introduced as a new disposition.
- `active_theory_node` records the nearest current node relation; it does not assert that the specific material increment is assimilated into that node.
- blank fast/router fields mean “not verified for this material increment”, not necessarily “the domain has no route”.

---

## 19. Non-actions preserved

This audit modifies no canonical definition, `d/Psi_f/T_dir` owner, OPEN_TENSIONS author decision, A/B/C verdict, book body, submitted paper, SourceCard, active-theory Axis B evidence, or EC acceptance state. It creates no Physics, Neuroscience, Philosophy or AI theory synthesis and deletes no material.
