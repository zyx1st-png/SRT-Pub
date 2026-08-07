---
id: SRT-OPS-AUDIT-ACTIVE-THEORY-ASSIMILATION-2026-08-06
type: audit
status: active
record_stage: audit_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
date: 2026-08-06
source_of_truth: "origin/main @ a07d2a72"
dependency:
  - SRT-MATERIAL-PIPELINE
  - SRT-OPS-AUDIT-HOOK-CLOSURE-2026-07-25
  - SRT-GOVERNANCE-ANTI-BLOCKING-GATE
  - SRT-ACTIVE-THEORY-NODES
tags: [Governance, Audit, Assimilation, ActiveLayer, ContextBundles, Router, DeepTheoryMap]
machine_readable: Operations/Audits/data/srt_active_theory_assimilation_2026-08-06.csv
manifest: Operations/Audits/data/srt_active_theory_nodes.json
---

# 全仓活跃理论吸收审计（2026-08-06）

> **性质**：运行层审计。本轮**不修改** canonical 定义、公理、方程、符号、claim level 或已投稿论文。对 `Core/SRT_OPEN_TENSIONS.md` 的改动是**新增一条登记**（§14），不改动既有条目。
>
> **本轮改了什么定义**：审计的判据本身。此前"材料已融入"的实际判据是**保存 + 登记 + 安排落点**；本轮改为**能改变下一轮 AI 判断**。这是一次判据收紧，因此几乎所有此前记为"已融入"的项目在新判据下会降级——这是预期结果，不是新发现的失败。
>
> ---
>
> ## 2026-08-07 修订：本文件初版自己犯了它要纠正的错
>
> 初版把 `NODE-CHOICE-GENERATION` 标为 `effectively_assimilated`，依据是「12 道回归题已写好、检查器绿」。**这是把 EA-5「行为回归测试通过」读成了「行为回归测试文件存在」**——与"有 hook 不等于已融入"是同一个错误，只是换了一层。
>
> 初版还有一处事实错误：报告称"14 个节点被同一项拦住：没有行为回归测试"。逐条复核后，**16 个节点里只有 4 个在结构上完整**；其余 12 个中的多数在 EA-5 之前就已经被 EA-1／EA-2／EA-4 拦下，加上行为测试也不会变成 `active_complete`。§4 已按证据重写。
>
> 修订内容：状态拆成两个轴（§4.0），16 节点重新分类（§4），`effectively_assimilated` 改为**推导值**，检查器不再允许在无实跑证据时给出行为结论（§5），并补做了真实的两条件行为回归（`SRT_CHOICE_EVENT_BEHAVIOR_RUN_2026-08-07.md`）。

---

## 0. 一句话结论

> 仓库的**档案化**和**工程化**都相当健康；断裂集中在**工程化 → 理论生效**这一段。
>
> 具体形态：**理论增量存在，但没有任何声明式入口指向它**——它只能靠目录列举和 frontmatter 依赖链被碰上。

**2026-08-07 更正**：初版这句话原本写的是"新会话读不到它，因而判断不会改变"。两条件实跑证伪了后半句。基线会话（`origin/main`）**读到了**，路径是 `STATUS.md` 权威锚点 → `ls Operations/` → frontmatter `dependency:` 链，并且在 18 道题上与 PR #744 条件**打平**。

所以准确的说法是：

> 缺的不是**可达性**，是**声明式可达性**。内容碰得上，但没有任何入口保证碰得上。这个差别是真的，但本轮**没能量化**它——`n=1` 的两条件对照给出的差分是零。

本轮以「选择生成条件与真实选择事件」节点作端到端试点，把声明式通路在一个节点上补通，并留下可复现的检查器、两轴状态模型和可维护的节点清单。**试点的结构部分成功，行为验证部分未通过**（见 `SRT_CHOICE_EVENT_BEHAVIOR_RUN_2026-08-07.md`）。

---

## 1. 三层定义与本轮判据

| 层 | 含义 | 判据 | 本轮状态 |
|---|---|---|---|
| **档案化** | 原始材料、对话、SourceCard、choice trace 已保存 | 文件存在且可检索 | **健康**。59 张 SourceCard、11 份 trace/ghost 卡、10 份对话材料、11 张 EC 卡，全部有 provenance |
| **工程化** | Material Log、patch、hook、registry、未来落点齐备 | 台账有行、patch 有 ID、hook 有 target | **大体健康，有已知缺口**。31 张 patch、24 张 hook（landed 12 / partial 3 / pending 9），2 个 hook target 文件从未创建 |
| **理论生效** | 已压缩为 SRT 原生命题，进入活跃 owner **且**进入 AI 检索路径，旧表述已处理，**并有实跑证据表明判断确实改变** | 见 §5 的 EA-1…EA-5 与 §4.0 的两轴 | **稀缺**。16 个节点中 **4 个**结构完整（Axis A `active_complete`）；行为验证见 §4.2 |

**以下任一状态，本轮均不计为"已融入理论"**：verdict A、SourceCard 完成、Material Log 已登记、patch 已创建、hook 有 target、文件可被搜索到、内容存在于 `01_Source_Intuition/`、choice trace 已完成 closure pipeline。

---

## 2. AI 活跃理论表面清单

必须区分五种情况，它们**不是**同一件事：

| # | 情况 | 本仓实例 | 是否影响下一轮判断 |
|---|---|---|---|
| 1 | 文件在仓库中存在 | 全部 `.md` | 否 |
| 2 | 文件能通过搜索找到 | 全部 | 否——除非 AI 恰好想到去搜 |
| 3 | 文件被 router / deep map 指向 | 见下 B 层 | **是**，条件是任务被正确分类 |
| 4 | 文件会进入 context bundle | 见下 D 层 | **是**，无条件 |
| 5 | 文件会被默认工作流主动读取 | 见下 A 层 | **是**，无条件 |

### A. 默认启动层（`AGENTS.md §Session Start` 规定的 3 个文件）

```text
SRT_AI_START.md
_SRT_AGENT_RETRIEVAL_PROFILE.md
STATUS.md §Fast Status
```

条件加载：`_SRT_INDEX.md`、`_SRT_SYMBOL_TABLE.md`、`_SRT_CONTEXT_ROUTER.md`、`_SRT_DEEP_THEORY_MAP.md`、`_SRT_PARKED_INDEX.md`、`Operations/Status_History/`。

### B. 检索与理论地图层

- `_SRT_CONTEXT_ROUTER.md`：本轮前 **24 条路由**，本轮后 25 条（新增 §23a）。
- `_SRT_DEEP_THEORY_MAP.md`：本轮前 **19 个节点** + 维护规则，本轮后 20 个（新增 §19a）。
- 各领域 `README.md` / `*_COMPACT_REGISTRY.md` / `_PHILOSOPHY_MACHINE_INDEX.md`。
- `CANONICAL_REGISTRY.md`、`03_Bridges/BRIDGE_INDEX.md`、`Bridge/SRT_Adjacent_Theory_Interface_Index.md`。

### C. 活跃理论 owner

canonical anchors（`_SRT_D_VALUE_CANONICAL.md`、`_SRT_PSI_F_CANONICAL.md`、`_SRT_T_DIR_CANONICAL.md`）、`Core/SRT_Core_21*`、`Core/SRT_Core_22_Equations.md`、`Core_Law/*`、各域主文、`Core/SRT_OPEN_TENSIONS.md`。

### D. 快速理解层与 context bundle

- **19 个 CompactCore**（本轮前 18）。
- **8 个 context bundle**，由 `scripts/build_srt_context_bundles.py` 生成，`--check` 验证内容摘要。
- 装载路线互斥：`SPINE`（144,888 ≈token）用于裁定定义；`COMPACTCORE`（68,377）用于领域问答。预算上限 155,000，由 `check_budgets()` 强制。

### E. 工作线入口

`01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md` + `BOOK_ACTIVE_MANIFEST.json`；`Operations/_SRT_PAPER_PIPELINE.md`；`Operations/SRT_WORKLINE_AUTHOR_PRIORITIES_2026-08-05.md`；`Operations/_SRT_REVIEW_QUEUE.md`。

### 关键发现：`03_Bridges/` 的路由错分

本轮前，`_SRT_AGENT_RETRIEVAL_PROFILE.md` 对 `03_Bridges/` 的**全部**描述是一行：

> `03_Bridges/` 和 `Bridge/` for adjacent theory translation.

但 `03_Bridges/` 里的 T-B、T-D、T-E、MSD 四座桥**不是**邻近理论翻译，而是 SRT 自己的跨域机件。这一行分类错误的后果是可推导的：一个 AI 在做「这算不算真的选择」的判断时，不会认为自己在做"邻近理论翻译"，因此**不会打开这个目录**。

这是本轮发现的最有解释力的单点缺陷：它不是"文件缺失"，而是"入口把内容描述成了别的东西"。已在本轮修正。

> **2026-08-07 更正**：上一段的**推论**（"因此不会打开这个目录"）经实跑证伪。基线会话确实没有经由检索画像打开 `03_Bridges/`——但它经由 `STATUS.md §当前权威锚点` 点名的 choice-trace 作者裁决文件，列举了 `Operations/` 目录，再沿 frontmatter 的 `dependency:` 字段拿到了 T-D 桥和全部四套操作化测试。
>
> 分类错误本身仍然是真的、仍然值得修。但"分类错了 ⇒ 内容不可达"这一步**不成立**：这个仓库的 frontmatter 依赖链事实上承担了相当一部分路由功能，而本审计的可达性指标完全没有计入它。

---

## 3. 四类输入渠道的实际结构

### 3.1 Pipeline 1 外部材料

| 指标 | 值 | 复现命令 |
|---|---:|---|
| Material Log 条目（STATUS 口径） | 207（A 130 / B 27 / C 50） | `STATUS.md` |
| SourceCard | 59 | `ls -1 Materials/2026/SRC_*.md \| wc -l` |
| patch | 31 | `find . -path '*/patches/*.md' -not -path './.git/*' \| wc -l` |
| hook | 24 | `find . -path '*/hooks/*.md' -not -path './.git/*' \| wc -l` |
| hook `landed` / `partial` / `pending` | 12 / 3 / 9 | `grep -l 'integration_status: X' $(find . -path '*/hooks/*.md')` |

**关键点**：全部 24 张 hook 的 `landing_ledger.target` **无一指向 CompactCore 之外的快速层、router、deep theory map 或 context bundle**。也就是说，hook 机制在设计上就止步于 owner 文件，从不负责让内容进入 AI 的默认读取路径。这不是执行不力，是**管线定义里没有这一段**。

`Operations/_SRT_MATERIAL_PIPELINE.md` 把管线定义为
`SourceCard → PatchNote → Material Log → Index → Registry → IntegrationHook → 正文`。
末端是"正文"，而不是"活跃层"。2026-07-25 的 hook 闭环审计已经给 `hook → 正文` 装了账；本轮发现**`正文 → 活跃层`这一段从未存在**。

### 3.2 书稿与专著融合材料

书稿实际吸收良好：西蒙东出现在 13 章、巴拉德 16 章、迪肯 7 章、Friston 6 章、达马西奥 5 章、詹姆斯 5 章。通道是 `01_Source_Intuition/BOOK/External_Theory_Notes/` 的插入地图 → 章末注。

**未回流理论层的部分**：`03_Bridges/SRT_Book_Vocabulary_Theory_Sync_Bridge_2026-07-05.md` 把书稿术语分为已锚定 / 已在桥 / ⚑新候选 / ✅已裁决四类。⚑新候选中：

- **已回流**：微效价、预裁剪（均已出现在 `_SRT_D_VALUE_CANONICAL.md`）；
- **未回流**：第三态能动性、被排开者去向三分、自检三问——只存在于书稿、该 bridge 与 `Output/` 导出文件中，任何理论 owner 都没有它们。

节点 `NODE-BOOK-BACKFLOW`，状态 `engineered_not_active`。

### 3.3 External Convergence 与外部压力材料

| 指标 | 值 |
|---|---:|
| EC 卡 | 11 |
| `accepted` | **0** |

全部为 `draft_v1; not accepted`。**这不是欠账**：`EVIDENCE_INDEX.md` 明确要求不得把候选列为已接受，`accepted = 0` 是硬度守恒纪律的正确结果。本审计不建议为提高覆盖率而批量升格。

但有一个真实缺口：11 张 EC 卡**无一被任何活跃表面文件命名**。它们形成的理论压力（如 `CL-*` 矛盾台账条目）因此不会进入任何判断。

### 3.4 自觉挖掘与 choice trace

| 类别 | 数量 | 活跃层状态 |
|---|---:|---|
| choice trace / ghost card（`01_Source_Intuition/*.md`） | 11 | 无一被活跃表面文件命名 |
| 对话材料（`Conversations/`） | 10 | 同上 |
| 作者裁决文件 | 2（`SRT_CHOICE_TRACE_AUTHOR_DECISIONS_2026-08-04.md`、`SRT_AUTHOR_DECISION_PACKET_...`） | 本轮前无一进入活跃层 |
| 已建 bridge | T-B / T-D / T-E / MSD | 仅通过 `BRIDGE_INDEX.md` 间接可达，无 router 路由 |

**必须区分 provenance 与理论**：trace 本身是来路记录，不是最终理论。本轮从中提取的是**作者已确认的命题与否定项**，而不是 trace 的全部内容：

- **G1**（2026-08-04）：可再选择性是生成健康度的重要判据，**不是**"选对"的唯一标准，也**不是**一次选择得以发生的必要定义 → 已进入活跃层（compact §6、回归题 T-11）。
- **G2**：耗散结构与选择结构**分层**，耗散不等于选择，也非普遍必要前身 → 已进入活跃层（compact §6、回归题 T-12）。
- **G4**：过程层／事件层／评价层三分 → 已进入活跃层（compact §4、§6）。

**仍未进入**：`d/q/o` 三轴（`author_gate`，禁运中）、ghost/阴阳/代理对象/协调身份四张 continuation card（`archived_only`，各自停在未决问题）。

---

## 4. 理论节点地图与吸收状态

完整机器可读表：[`data/srt_active_theory_assimilation_2026-08-06.csv`](data/srt_active_theory_assimilation_2026-08-06.csv)
节点清单（人工维护，被生成脚本与检查器读取）：[`data/srt_active_theory_nodes.json`](data/srt_active_theory_nodes.json)

### 4.0 三个轴，不可合并

初版用单一 `assimilation_status` 表达两件事，2026-08-07 拆成两轴。**2026-08-08 再拆一次**，因为实跑暴露了第三个混淆：`behavior_validation = mixed` 这个写法，把"这个 PR 没加东西"记成了"这个理论节点没生效"。而实跑同时证明了另一件事——**两个条件都检索到并正确使用了该节点**。

| 轴 | 问的问题 | 取值 | 谁能设 |
|---|---|---|---|
| **A `structural_assimilation`** | 理论增量在结构上走到哪了？ | `archived_only` / `engineered_not_active` / `partially_active` / `active_complete` / `conflict_with_active_text` / `author_gate` / `rejected_or_parked` | 静态检查器 |
| **B `behavioral_availability`** | 新会话是否被**观察到**检索并用它作判断？**绝对状态，不与 baseline 比较** | `untested` / `observed` / `robustly_observed` / `failed` / `not_applicable` | 只能由有记录的实跑设定 |
| **C `intervention_effect`** | 某一个 PR 相对它自己的 baseline 加了什么？**按干预记录，不是节点属性** | `untested` / `none` / `retrieval_efficiency_only` / `judgment_positive` / `judgment_negative` / `mixed` | 只能由前后对照设定 |

**B 与 C 必须分开的理由，来自一次真实误判**：PR #744 的 judgment delta 是 0，但两个条件都正确检索并应用了该节点。用一个字段记，会把一个**能用、被用、用对了**的理论节点写成"行为上无效"。

- `observed` = 至少一次有记录的运行中被检索并使用（任何检索模式）；
- `robustly_observed` = 至少两次独立的 **bounded** 运行（见 `SRT_BOUNDED_RETRIEVAL_PROTOCOL_2026-08-08.md`）——这一档专门用来区分"快速活跃层"和"深搜能找到"。

`effectively_assimilated` 保留，但**重新定义为只描述节点**：

```text
effectively_assimilated := structural_assimilation == "active_complete"
                       AND behavioral_availability ∈ {observed, robustly_observed}
```

它**不**表示"本次 PR 产生了增量"。后者只存在于该 PR 的 `intervention_effect` 记录里。两者不得共用一个字段。

### 4.1 Axis A：16 节点重新分类

每个未达 `active_complete` 的节点必须写明**是哪一条判据拦住它**，否则清单会退化成没人能行动的悲观情绪。以下 blocker 均经实证核对（命令见 §11）。

| node_id | Axis A | 拦住它的判据（实证） |
|---|---|---|
| `NODE-CHOICE-GENERATION` | **active_complete** | — |
| `NODE-SELECTION-ONTOLOGY` | **active_complete** | — |
| `NODE-L0-L1-L2` | **active_complete** | — |
| `NODE-PSI-F` | **active_complete** | — |
| `NODE-T-DIR` | partially_active | **EA-2**：PH_AG02／PH_AG03 的增量已裁决但未写进 `_SRT_T_DIR_CANONICAL.md`（其内容 0 命中） |
| `NODE-GHOST-OPERATOR` | partially_active | **EA-1**：三张 ghost source card 从未压成命题（`Core_21_Minimal_Axioms.md`、`_SRT_SYMBOL_TABLE.md` 各 0 命中） |
| `NODE-SUBJECTHOOD` | partially_active | **EA-4**：`SRT_Philosophy_Agency_Subjecthood_v0_2.md` 在 8 个 bundle 中出现 **0** 次 |
| `NODE-CONSCIOUSNESS` | partially_active | **EA-1**：五张 2026-08-05 源卡的反向修正在任何快速层中 0 命中 |
| `NODE-LIFE-DISSIPATIVE` | partially_active | **EA-4**：只有 T-E 的分层裁决进了快速层；其"物理底座／组织机制／解释充分性"三分在任何 compact 中 0 命中 |
| `NODE-SOCIAL-L2` | partially_active | **EA-2**：SEA 协议与编码手册只在 Operations 层；两个候选 owner 各 0 命中 |
| `NODE-ENTROPY-REORG` | partially_active | **EA-4**：T-B 过程层与痛苦类型学接口在任何 CompactCore 中 0 命中 |
| `NODE-AI-REASONING` | engineered_not_active | **EA-2**：AIREASON01／AIEVID01 停在 patch 层无 hook；AIGOAL01 的 hook 全 pending |
| `NODE-NEURAL-DECODABILITY` | engineered_not_active | **EA-2**：五张 hook 全 pending；NEURAL18 无 hook；合成落点文件从未创建 |
| `NODE-PHYSICS-MEASUREMENT` | engineered_not_active | **EA-2**：三张 hook 指向不存在的 `Physics/SRT_Physics_Bridge_v0_2.md`；P06/P07/P08/REP01 无 hook |
| `NODE-BOOK-BACKFLOW` | engineered_not_active | **EA-2**：第三态能动性／被排开者去向三分／自检三问**没有任何理论 owner** |
| `NODE-D-VALUE` | author_gate | RQ-2026-08-A02 未裁；`d/q/o` 对书稿、公共内容、bridge、论文禁运 |

**Axis A 统计**：`active_complete` **4** ／ `partially_active` **7** ／ `engineered_not_active` **4** ／ `author_gate` **1**。

`archived_only`、`conflict_with_active_text`、`rejected_or_parked` 本轮未使用——不等于不存在，只等于本轮 16 节点范围内未发现符合的实例。

### 4.2 初版的错误结论与更正

> 初版写："14 个节点被同一项拦住：没有行为回归测试。"

**这是错的。** 逐条核对后，只有 3 个节点（`SELECTION-ONTOLOGY`、`L0-L1-L2`、`PSI-F`）加上试点节点，是"结构已完整、只缺行为验证"。其余 12 个中：

- **7 个** 在 EA-1／EA-2／EA-4 就被拦下——**给它们写回归测试不会改变 Axis A 状态**；
- **4 个** 连 owner 都没进（`engineered_not_active`）；
- **1 个** 是作者门。

换句话说：初版把"没有行为测试"当成了普遍瓶颈，实际上对四分之三的节点而言，行为测试根本轮不到成为瓶颈。

"仅缺 EA-5"这个说法，**只对 4 个节点成立**。

## 5. 有效吸收的五项判据（EA-1…EA-5）

| 判据 | 内容 | 可机检？ |
|---|---|---|
| **EA-1** | 形成 SRT 原生命题：新增区分／修正／降级／反例／失败条件／可检验差异／新张力，而非复述外部作者观点 | **否**（内容判断） |
| **EA-2** | 进入活跃 owner：canonical / Core / major bridge / domain owner / CompactCore / OPEN_TENSIONS。只在 SourceCard、patch、hook、trace 或计划文件中**不算** | 是 |
| **EA-3** | 进入 AI 检索路径：router 指向 / deep map 纳入 / registry 指向 / bundle 装载 / workline manifest 要求读取 | 是 |
| **EA-4** | 处理旧表述：记录旧表述、新表述、修改原因、旧表述仍适用的范围、需同步的 CompactCore | 是（记录是否存在） |
| **EA-5** | 行为回归测试通过：设计问题证明下一轮判断会改变 | 是（测试是否存在且数量达标） |

### 5.1 检查器的边界（2026-08-07 收紧）

| 检查类型 | 谁做 | 内容 |
|---|---|---|
| **structural check**（Axis A） | `scripts/check_active_theory_assimilation.py`，可进 CI | owner 存在；router／deep map 锚点解析且**确实点名**该节点的文件；快速层存在；bundle manifest 生效；旧表述处理有记录；回归套件存在且非空 |
| **behavioral check**（Axis B/C） | **不可静态验证** | 检查器**不得**因回归文件存在就判 `observed`。无实跑证据时，CI 能报的最强结论是 `behavioral_availability = untested`。`robustly_observed` 额外要求 `behavior_observation_mode: bounded` |

具体实现的三条硬规则：

1. 检查器**从不设置** Axis B 或 Axis C，只读取并校验它们；
2. 任何 `behavioral_availability ∈ {observed, robustly_observed, failed}` 必须同时给出 `behavior_evidence` 且该文件存在；
3. `robustly_observed` 还必须有 `behavior_observation_mode: bounded`——无预算深搜不得记为快速层结果；
4. 每条 `interventions` 记录必须有合法的 `intervention_effect` 与指向真实运行记录的 `ref`；
5. `active_complete`、`observed`、`intervention_effect` 是三个独立断言，检查器不会由任何一个推出另一个。

绿色只意味着"结构上没有缺件"，不意味着"理论是好的"，更不意味着"已被验证会改变判断"。EA-1（是否形成真正的原生命题）是内容判断，不可机检。

---

## 6. 陈旧与冲突

### 6.1 已在本轮处理

| 项 | 旧表述 | 新表述 | 原因 | 旧表述仍适用的范围 |
|---|---|---|---|---|
| `SRT_AI_START.md` "Real Choice Moment" | 全文只有一条指针："use `Core/SRT_Core_21b_...`" | 保留该指针并标明它**只给否定清单**，另指向 `03_Bridges/SRT_Selection_Event_CompactCore.md` 取肯定判别程序 | 旧文本不错，但**欠定**：只有否定清单没有判别程序，具体案例只能靠直觉外推 | P1-T05 仍是 real choice moment 的 canonical 承载点，任何定义级引用仍走它 |
| `_SRT_AGENT_RETRIEVAL_PROFILE.md` 的 `03_Bridges/` 描述 | "for adjacent theory translation"（与 `Bridge/` 合并成一行） | 拆开；`03_Bridges/` 改述为 SRT 自有跨域框架，并点名 T-B/T-D/T-E/MSD 与选择事件入口 | 分类错误导致 AI 在做选择判断时不会打开该目录 | `Bridge/`（旧目录）的邻近理论翻译定位不变 |

需同步的快速层：`03_Bridges/SRT_Selection_Event_CompactCore.md`（新建）、`SRT_CONTEXT_BUNDLE_COMPACTCORE.md`（已重生成）。

### 6.2 已知但本轮未处理

| 项 | 性质 | 为什么不处理 |
|---|---|---|
| 两张 PH_AG hook 的 `_SRT_T_DIR_CANONICAL.md` 回写 | C 类编辑 | 需 `SRT_EDIT_PROTOCOL` 单独授权，不随本轮一并授权 |
| `Physics/SRT_Physics_Bridge_v0_2.md` 与 neuro 合成文件从未创建 | 作者裁决 | RQ-2026-08-A04 待裁；neuro 合成文件的存废本轮新增为待裁项 |
| `d/q/o` 三轴 | 作者门 | RQ-2026-08-A02 待裁，禁运有效，本轮不申请豁免 |
| `Neuroscience/SRT_Neuroscience_Hardening_N1_N12_v0_2.md` vs `..._N1_N13_v0_2.md` | 命名不一致 | 两个名字指同一个从未创建的文件；创建与否属作者裁决 |

### 6.3 本轮发现的一个本地-only 工具缺陷（未修）

`scripts/governance_common.py` 的 `ARTIFACT_PREFIXES` 用小写 `"papers/"` 做前缀匹配。git 跟踪的目录名是小写 `papers/`，但在大小写不敏感的文件系统（macOS）上工作树解析为 `Papers/`，前缀不匹配，导致 123 个论文文件被扫描并在本地 preflight 报 `errors=123`。**Linux CI 不受影响**，`origin/main` 的 preflight 是绿的。本轮未修，因为它与本审计主题无关且涉及全部检查器的共享模块；建议单独一个 PR 处理。

---

## 7. "A 类材料数量" vs "有效吸收数量"

| 口径 | 数量 | 含义 |
|---|---:|---|
| Material Log verdict A | **130** | 已裁决可融入，并已写入某个落点 |
| 有 patch 的材料 | 31 | 已形成域内 bounded 补丁 |
| 有 hook 的 patch | 24 | 已有落点账 |
| hook `landed` | 12 | 内容已进入 owner 文件正文 |
| 节点级 Axis A `active_complete` | **4**（16 个节点中） | 结构齐备：原生命题／owner／检索路径／快速层／旧表述处理 |
| 节点级 Axis B `passed` | **0** | 有实跑证据表明判断确实改变 |
| **`effectively_assimilated`（推导）** | **0** | 两轴同时满足 |

这七个数字**不可互相替代**。此前把第一个当作"融合进度"，会把 130 读成"130 条材料已进入 SRT 理论"——实际含义只是"130 条材料已被裁决并归档到某处"。

而 2026-08-07 的实跑给出了第二个教训：**第五个数字也不能替代第六个**。`active_complete` 只说结构齐备，唯一一个做过实跑的节点得到的是 `mixed`，不是 `passed`。

---

## 8. 不得声称已融合的项目

以下项目在本轮之后**仍不得**被描述为"已融入 SRT 理论"：

1. 全部 27 条 B 类材料（合规停驻，有具名触发条件，不是欠账）；
2. 全部 11 张 EC 证据卡（`accepted = 0` 是正确状态）；
3. 9 张 `pending` hook 与 3 张 `partial` hook 的未落地靶点；
4. 7 张无 hook 的 patch（Physics P06/P07/P08/REP01、NEURAL18、AIREASON01、AIEVID01）；
5. `d/q/o` 三轴（禁运中）；
6. 四张 ghost / 阴阳 / 代理对象 / 协调身份 continuation card（各自停在未决问题）；
7. 三个未回流的书稿术语（第三态能动性、被排开者去向三分、自检三问）；
8. T-B / T-E 桥的跨域压力测试结论（首轮已建，压测未完成）；
9. 本轮试点的 `CG-0..CG-4` 门槛值本身——它们是审计默认约定，不是已证定理（见 `Core/SRT_OPEN_TENSIONS.md §14`）；
10. **`NODE-CHOICE-GENERATION` 本身**。它的 Axis A 是 `active_complete`，Axis B 是 `mixed`，推导标签为 **false**。不得称它 effectively assimilated，也不得说 PR #744 已证明活跃层改变了判断。

---

## 9. 后续队列（2026-08-08 再次重排）

这一节已经被推翻两次，两次都是被实跑推翻的，值得把过程留着。

| 版本 | 排序依据 | 被什么推翻 |
|---|---|---|
| 08-06 初版 | 活跃层**缺口大小** | 缺口最大的 `NODE-CHOICE-GENERATION` 补通后行为差分为零 |
| 08-07 第二版 | **预期行为差分**，把 `NODE-AI-REASONING` 排第一，理由是"内容缺口，基线拿不到" | 08-08 基线探针：`main` 有界预算下 **24/24 通过**，根本没有缺口 |
| **08-08 当前版** | **先探针，后排序**——不再预先排序 | — |

### 9.1 现在的规则

**不再维护一份预测性的施工队列。** 两次预测都错了，而且错的方式相同：从静态特征（缺口大小、有没有 hook）推断行为缺口。

取而代之的是一条流程：

```text
候选节点
  → bounded 基线探针（3 次独立运行，题目取自 patch 的禁止推导清单，含反刷分正例）
  → Case A 通过：停止，记录，换下一个
  → Case B 只有 unconstrained 过：这是真的检索/压缩缺口，允许做活跃层
  → Case C 都不过但 patch 能给出区分：这是真的内容缺口，允许完整写回
  → Case D patch 也给不出稳定区分：降级为档案材料，不升格
```

### 9.2 已探针的节点

| 节点 | 探针 | 结果 |
|---|---|---|
| `NODE-CHOICE-GENERATION` | 2026-08-07（unconstrained，两条件） | 可用，但 PR 增量为零；**未做 bounded 复跑** |
| `NODE-AI-REASONING` | 2026-08-08（bounded，3 次） | **Case A**：24/24，零施工即 `robustly_observed` |

### 9.3 下一批该探针（不是该施工）的

1. **`NODE-CONSCIOUSNESS`** — 按 Case A 协议指定的下一候选；本轮已启动 bounded 探针。
2. **`NODE-NEURAL-DECODABILITY`** 与 **`NODE-PHYSICS-MEASUREMENT`** — 这两个的 `engineered_not_active` 与 `NODE-AI-REASONING` **同源**，都是从"没有 hook"推出来的，而那条推理已被证伪两次。**必须先探针**。08-08 的一次运行里，模型自发引用了 `Neuroscience/patches/SRT_Neuro_NEURAL18_...` 这张 patch——正是 `NODE-NEURAL-DECODABILITY` 被判"未激活"的依据之一。
3. **`NODE-CHOICE-GENERATION` 的 bounded 复跑** — 现有观察全是 unconstrained（27 文件、第 9 个才到判别层），不足以判断它是否属于**快速**活跃层。
4. `NODE-BOOK-BACKFLOW` — 唯一一个 `engineered_not_active` 依据不是 hook 推理而是内容层核实（三个术语确实没有任何理论 owner）。它仍是最可能的真缺口，但也要先探针。

## 10. 需要作者拍板

1. **Neuroscience 合成文件**：创建 `N1_N12_v0_2`（hook 写法）／ `N1_N13_v0_2`（索引写法）／ 改把 NEURAL18/21/22 的落点指向已存在的 compact core／继续停驻？
2. **Physics 落点**：RQ-2026-08-A04 已在队列，本审计不重复提问，仅确认它挡住 3 个 hook。
3. **7 张无 hook 的 patch**：补 hook ／ 判"有意无 hook + 写触发条件" ／ 降级停驻？
4. **书稿三术语**（第三态能动性、被排开者去向三分、自检三问）：进理论 owner ／ 明确判为书稿专用 ／ 继续挂在 sync bridge？

---

## 11. 统计方法与局限

### 复现方式

```bash
uv run python scripts/check_active_theory_assimilation.py --reachability \
  --csv Operations/Audits/data/srt_active_theory_assimilation_2026-08-06.csv
```

### 搜索范围

- **活跃表面**：`AGENTS.md §Session Start` 的 3 个 bootstrap 文件 + 条件加载的路由层 + 各域 README / registry / machine index + 全部 `*CompactCore*.md`（排除 `Operations/Context_Bundles/`，那是生成物）。共 49 个文件。
- **理论承载候选**：`03_Bridges/*.md`、`Bridge/*.md`、`*/patches/*.md`、`Operations/SRT_*.md`、`01_Source_Intuition/*.md`、`01_Source_Intuition/Conversations/*.md`、`04_External_Convergence/*/*.md`。共 94 个文件。
- **排除规则**：`README.md`、`BRIDGE_INDEX.md`、`BRIDGE_TEMPLATE.md`、`INDEX.md`——是索引不等于承载理论。

### 结果

| 指标 | `origin/main @ a07d2a72` | 本轮后 |
|---|---:|---:|
| 活跃表面文件 | 48 | 49 |
| 理论承载候选 | 93 | 94 |
| **无任何活跃表面文件命名** | **75（80.6%）** | **74（78.7%）** |

### 局限（必须与结果一起读）

1. **可达性指标偏宽松**。它只问"有没有被命名"，一次 `BRIDGE_INDEX.md` 的表格提及即算可达。但 `BRIDGE_INDEX.md` 自身此前只通过 `_SRT_AGENT_RETRIEVAL_PROFILE.md` 的一行**错误分类**可达。因此**真实可达性低于 78.7% 所暗示的水平**——T-D 桥在本轮前按此指标算"可达"，实际没有任何路由会把选择判断类问题送到它那里。
2. **数字变化小不代表改动小**。本轮只有 1 个文件从"无人命名"变为"被命名"，但节点级的变化是：一类高频问题从**无路由**变为有路由 + 有快速层 + 有 bundle + 有 12 道回归题。指标不度量这个。
3. **可达性指标完全没有计入 frontmatter `dependency:` 链**（2026-08-07 新增，最重要的一条）。指标只问"是否被活跃表面文件按文件名提及"。但两条件实跑显示，基线会话是靠 `STATUS.md` 权威锚点 + 目录列举 + `dependency:` 字段拿到全部关键文件的——那条路径完全不在指标视野内。因此 **75/94（80.6%）"不可达"这个数字高估了不可达程度**，不应被引用为"八成内容读不到"。它准确度量的是"没有声明式入口指向"，不是"读不到"。
4. **节点清单是人工的**。16 个节点由本轮判断划定，不是从仓库自动导出，可能遗漏节点或切分不当。可达性调查是它的无偏补充，但两者都不是完备普查。
5. **EA-1 不可机检**。"是否形成 SRT 原生命题"是内容判断，检查器只验证载体。
6. **未覆盖**：`Papers/` 内部的理论一致性、`Spirituality/` 域、`90_Backstage/` 停驻区、书稿正文自身的理论一致性。
7. **Material Log 计数差**。STATUS 记 207（A 130 / B 27 / C 50），按表格列解析得 211（A 132 / B 29 / C 50）。差值 4 条未对账，本审计沿用 STATUS 口径并标注该差异。

---

## 12. 本轮对此前"材料融合计划"的处理

`Operations/Proposals/SRT_MATERIAL_INTUITION_INTEGRATION_PLAN_2026-08-05.md` 中的以下工作**不作废，但降级**为 provenance、可追溯性与工程闭环辅助线：

| 工作 | 改善哪一层 | 是否可作为"已进入理论"的判据 |
|---|---|---|
| standalone Material Log 条目合并 | 档案化 | **否** |
| Material Log 统计纠正（207 vs 211） | 档案化 | **否** |
| patch / hook ID 对表 | 工程化 | **否** |
| 补齐缺失 hook | 工程化 | **否** |
| Neuroscience `N1_N12` / `N1_N13` 路径修正 | 工程化 | **否** |
| report-only checker（材料闭环） | 工程化 | **否** |
| 按章材料输入包 | 工程化（书稿侧） | **否** |
| **本轮新增：节点清单 + 活跃层检查器 + bundle 清单通道** | **理论生效** | **是**（EA-2…EA-5 的载体） |

前六项仍应做——没有可追溯性，理论生效层的来源无法审计。但它们完成后，**不得**据此宣布材料已进入理论。
