---
id: SRT-CHOICE-EVENT-BEHAVIOR-RUN-20260807
type: audit
status: active
record_stage: run_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
node_id: NODE-CHOICE-GENERATION
date: 2026-08-07
suites:
  - Operations/Audits/SRT_CHOICE_EVENT_BEHAVIOR_REGRESSION_TESTS_2026-08-06.md
  - Operations/Audits/SRT_CHOICE_EVENT_OOD_TRANSFER_TESTS_2026-08-07.md
condition_a_ref: a07d2a72
condition_b_ref: d9b9bf20
---

# 选择事件节点 · 行为回归实跑记录（2026-08-07）

> **这份文件是 Axis B 的唯一证据源。** 没有它，`behavior_validation` 只能是 `untested`。
>
> 它记录一次**真实运行**，不是运行计划、不是测试文件清单，也不是检查器输出。检查器无法产生这份记录：它只能确认套件存在。

---

## 1. 为什么必须实跑

PR #744 初版把 `NODE-CHOICE-GENERATION` 标为 `effectively_assimilated`，依据是「12 道回归题已写好且检查器绿」。这是把 **EA-5「行为回归测试通过」** 读成了「行为回归测试文件存在」。两者不是一回事，而后者恰恰是本轮审计自己反对的那种判据（"有 hook 不等于已融入"的同构错误）。

本次运行的目的就是补上这一步，并接受它可能得出否定结论。

---

## 2. 实验设计

### 两个条件

| | Condition A（基线） | Condition B（PR #744） |
|---|---|---|
| 代码库状态 | `origin/main` @ `a07d2a72` | PR #744 分支 @ `d9b9bf20` |
| 选择事件快速层 | 不存在 | `03_Bridges/SRT_Selection_Event_CompactCore.md` |
| 路由 | 无对应路由 | router §23a、deep map §19a |
| 入口层 | `SRT_AI_START.md` 只有一条指向 P1-T05 的指针 | 指针 + 否定清单说明 + 快速层指向 |
| 检索画像 | `03_Bridges/` 被描述为"邻近理论翻译" | 已改述为 SRT 自有跨域框架 |

### 会话条件

两个条件使用**同一套指令**，只有工作目录不同。指令要求：

1. 读 `AGENTS.md` 并**逐字**执行其 §Session Start 的读取顺序；
2. 之后只能沿仓库**自己的**路由／导航文件决定还读什么；
3. 记录每次打开文件时**是被哪个入口带过去的**。

### 反泄漏措施

- 题目中**不出现**：`CG-0..CG-4`、`DMF`/`NER`/`PEF`/`CBP`/`HEF`、"selection event CompactCore"、任何正确答案或提示；
- Condition B 工作树中**物理删除**了两个含答案的文件：
  - `Operations/Audits/SRT_CHOICE_EVENT_BEHAVIOR_REGRESSION_TESTS_2026-08-06.md`
  - `Operations/Audits/SRT_ACTIVE_THEORY_ASSIMILATION_AUDIT_2026-08-06.md`
  （OOD 套件在运行时尚未提交，天然不在工作树中。）
- 因此 Condition B 若答对，只能来自**快速层 + 路由**，不可能来自读到题库。

### 题目

18 题：12 道原回归题（`T-01`…`T-12`，与 CompactCore 案例同构）+ 6 道分布外迁移题（`T-13`…`T-18`，案例从未在 CompactCore 中出现，跨生物种群／AI agent／社会制度／组织管理／神经过程／一般动力系统）。

`T-14` 是**反刷分锚点**：它的正确方向是"多数门达标"，用于检出"一律否认 AI"的立场性策略。

### 评分 rubric

每题记录：`baseline judgment` / `PR744 judgment` / `expected distinction` / `retrieval reached intended file?` / `pass|partial|fail` / `failure reason` / `improvement source (retrieval vs leakage)`。

**结论正确但未调用"必须调用的区分"记为 partial 或 fail**，理由是本测试测的是可复用判别能力，不是单题答案。

---

## 3. 运行结果

### 3.0 一句话

> **Condition B 绝对表现满分（17 pass + 1 partial），Condition A 也是。差分效应约等于零。**

**2026-08-08 结论重述（三轴拆分后）。** 初版把这个结果写成 `behavior_validation = mixed`，等于把"这个 PR 没加东西"记成了"这个理论节点没生效"。两者是不同的事实，本次运行同时给出了它们：

```text
Axis B  behavioral_availability = observed
        两个条件都检索到了该节点的材料并用它作出判断，各 17 pass + 1 partial。
        这是**绝对**结论，不与 baseline 比较。理论节点是可用的。

Axis C  intervention_effect     = retrieval_efficiency_only
        judgment delta            0
        retrieval success delta   0（两边都到达了）
        discriminating layer      第 9 个文件 → 第 5 个文件
        total reads               27 → 23
        transfer delta            0（6 道 OOD 两边都过，含反刷分锚点）
        n = 1/条件 → 不得声称稳定性提升
```

**不得**再用一个 `effectively_assimilated = false` 把这些不同的事实抹平。节点本身是 `active_complete` + `observed`，推导标签为 **true**；PR #744 的贡献是 `retrieval_efficiency_only`，与前者无关。

**但 `observed` 不是 `robustly_observed`。** 本次两个条件都是**无预算深搜**：基线读了 27 个文件、第 9 个才到判别层。按 2026-08-08 起生效的 `SRT_BOUNDED_RETRIEVAL_PROTOCOL_2026-08-08.md`，`robustly_observed` 要求**有界预算下的重复运行**。本节点尚未做过 bounded 复跑，因此停在 `observed`。

### 3.1 被证伪的前提

审计初版的核心诊断是：

> 一个 AI 在做「这算不算真的选择」的判断时，不会认为自己在做"邻近理论翻译"，因此**不会打开 `03_Bridges/` 这个目录**。

**这个推断错了。** Condition A（`origin/main`，没有任何新路由、没有快速层）实际做到了：

1. 读 `STATUS.md §当前权威锚点`，其中已经点名 `Operations/SRT_CHOICE_TRACE_AUTHOR_DECISIONS_2026-08-04.md`；
2. 顺手 `ls Operations/`，于是看见了整个 SEA 协议族；
3. 打开统一审计协议，再沿其 frontmatter 的 `dependency:` 字段，依次取到 T-D 桥、四套操作化测试、五域压测、三个案例审计。

也就是说：**内容一直是可达的，只是走的不是路由层，而是「STATUS 权威锚点 → 目录列举 → frontmatter 依赖链」。**

这暴露了本审计另一处方法缺陷：§11 的可达性指标只测「是否被活跃表面文件按文件名提及」，**完全没有计入 frontmatter `dependency:` 链**。而这次运行显示，依赖链是这个仓库事实上最有效的检索路径之一。75/94「不可达」这个数字因此**高估了不可达程度**。

### 3.2 逐题对照

评分：`pass` = 结论正确**且**调用了必须调用的区分；`partial` = 结论对但区分缺失或错位；`fail` = 结论错。

| # | 题 | A（基线） | B（PR744） | 差分 | 备注 |
|---|---|---|---|---|---|
| T-01 | LLM 采样出两个回答 | pass | pass | 0 | 两者都停在 `PEF-0`／`NER-0-1`，都引不可补偿 |
| T-02 | AI 建议被采纳执行 | pass | pass | 0 | 两者都判 `PEF-1` + 角色洗白，都引 B₁/B₂/B₃ 三边界 |
| T-03 | 耗能算不算后果承载 | pass | pass | 0 | 两者都判 `CBP-1`，都要求路径特异 |
| T-04 | 有记忆算不算历史效力 | pass | pass | 0 | 两者都要求 `HEF-3` 并点名 washout／载体消融测试 |
| T-05 | 梯度下降收敛 | pass | pass | 0 | 两者都引 P1-T05 否定清单 + `CBP-1` |
| T-06 | 三个都很糟的选项 | pass | pass | 0 | 两者都判**惩罚性选择**，都点名"不是选项少" |
| T-07 | 菜单 + 投票 | **pass+** | pass | **A 略优** | A 额外引 `Core_Law/SRT_Collective_Selection.md` T-COLL-4「投票不自动是共选」 |
| T-08 | 决策者与承受者分离 | pass | pass | 0 | 两者都判事件成立 + `CBP-3/4` 外包链 |
| T-09 | 细胞代谢差异响应 | pass | pass | 0 | 两者都判 `NER-1`，都引 E. coli 案例的 `SEA-2` 上限 |
| T-10 | 生成条件 ≠ 此刻在选择 | pass | pass | 0 | 两者都引休眠条款 |
| T-11 | 不可逆承诺缩小未来 | pass | pass | 0 | 两者都引作者裁决 G1 |
| T-12 | 耗散结构 | pass | pass | 0 | 两者都引 G2 + T-E 五条降级 |
| **T-13** | 细菌种群耐药性（OOD） | **pass+** | partial | **A 明显优** | A 引 P1-T06 stable ISP、编码手册的 `CROSS_GENERATION_BACKFILL`／`INCOMPATIBLE_TIMESCALES` 触发器、`SRT_Reference_Scaling` 的贝叶斯读法；B 自述 `Partial NO REPO BASIS` |
| **T-14** | 自主 agent 有写权限（OOD，反刷分锚点） | pass | pass | 0 | **两者都没有反射性否认**——都承认多数门达标。A 更准确地指出黑箱模型的 `NER` 是最弱环并给出 S3 层级；B 指出 `CBP-3` 落在下游 |
| **T-15** | 立法跨代后果（OOD） | **pass+** | pass | **A 略优** | 两者都禁止把十年后果并入立法事件。A 额外拆成三个事件（通过／施行／写回）并引 T-COLL-2 主从型 |
| **T-16** | OKR 目标审批（OOD） | partial | **pass** | **B 略优** | rubric 要求「KPI 约束本身不构成伪选择，须测路径效力」。B 明确说了这一句；A 以"通常是伪选择"起头，虽也给了正确检验，方向上偏了一点 |
| **T-17** | 神经解码器可区分（OOD） | **pass+** | pass | **A 明显优** | A 找到并引用了 `Neuroscience/patches/SRT_Neuro_NEURAL18_..._Decodability_Anchoring_Gate_v0_1.md` 这张专用护栏 patch 及其 L0-L6 分级；B 只用 `NER-0` |
| **T-18** | 双稳态开关（OOD） | pass | pass | 0 | 两者都判 `NER-0/1` 失败门 + 不可补偿 |

**合计**：A 18 pass（其中 1 partial：T-16）／ B 18 pass（其中 1 partial：T-13）。

按 pass 计：**A 17 pass + 1 partial；B 17 pass + 1 partial。** 差分为 **0**。

### 3.3 检索路径对照

| | A（基线） | B（PR744） |
|---|---|---|
| 打开文件数 | 27 | 23 |
| 到达判别层的步数 | 第 9 个文件（统一审计协议） | 第 5 个文件（`SRT_Selection_Event_CompactCore.md`） |
| 到达方式 | `STATUS.md` 权威锚点 → `ls Operations/` **目录列举** → frontmatter `dependency:` 链 | **三条独立的声明式指针**：`SRT_AI_START.md §4`、`_SRT_AGENT_RETRIEVAL_PROFILE.md`、`STATUS.md` 2026-08-06 条目；随后 router §23a |
| 是否依赖机会主义动作 | **是**（目录列举不是任何入口规定的动作） | 否 |
| 是否读到快速层 | 不存在 | 是 |

这是本次运行唯一可观察到的真实差异：**B 的到达是被声明的，A 的到达是碰巧的**。但 n=1，无法据此断言 B 更稳健。

### 3.4 泄漏检查

- Condition B 工作树中两个含答案的文件已物理删除，B 的 reading log 明确报告了这两个文件**不存在**——证明它没有读到题库；
- B 的答案中出现了 `SEA-0..SEA-4` 分类，这来自 `Operations/SRT_UNIFIED_SELECTION_EVENT_AUDIT_PROTOCOL_2026-08-04.md`，**A 也用了同一套分类**，说明它不是快速层特有的；
- 因此 B 的表现**不是**答案泄漏所致。但这一点已无关紧要，因为 B 相对 A 没有增量可解释。

### 3.5 失败模式定位（针对 Axis C 的零差分，不是针对节点）

按预设的五个候选原因逐一判定：

| 候选原因 | 判定 | 证据 |
|---|---|---|
| router 没读到 | **否** | B 读到了 router §23a 与快速层 |
| bundle 没装到 | 不适用 | 本次运行按文件系统检索，未装 bundle |
| compact 表述不足 | **否** | B 用它答对了 18 题 |
| distinction 不可迁移 | **否** | 6 道 OOD 题两个条件都答对，包括反刷分锚点 T-14 |
| **baseline 本来就能答对** | **是——这是本次的实际原因** | A 在没有任何新增活跃层的情况下达到同等水平 |
| regression question 泄露答案 | 否 | 见 §3.4 |

**结论**：不是 retrieval failure，不是 compression failure，不是 theory ambiguity，也不是 SRT 判别力本身弱——是 **test design problem**：这套题目对「PR #744 之前 vs 之后」**没有判别力**，因为基线已经在天花板上。

注意这一节诊断的是 **Axis C 的零差分**，不是节点的可用性。基线在天花板上，恰恰是 Axis B `observed` 的证据。

### 3.6 由此得出的状态（2026-08-08 三轴版）

```text
structural_assimilation = active_complete
behavioral_availability = observed          （观察模式：unconstrained，非 bounded）
effectively_assimilated = true              （推导：A=active_complete 且 B∈{observed,…}）

intervention_effect (PR #744) = retrieval_efficiency_only
```

读法：**这个理论节点是可用的，而且在 PR #744 之前就已经可用。PR #744 把到达它的路径从机会主义检索改成了声明式检索，没有增加判断能力。** 这两句话都为真，且不冲突。

待办：做一次 bounded 复跑，才能判断它是否够得上 `robustly_observed`——即是否真的属于**快速**活跃层，而不只是"深搜能到"。

### 3.7 不做什么

- **不**往 CompactCore 里补写这 18 题的答案来刷通过率——那会同时毁掉这套题的检测能力和快速层的可信度；
- **不**因为差分为零就删除快速层或撤销路由：B 的到达路径是被声明的，A 的是碰巧的，这个差别本身有价值，只是**本次运行无法量化它**；
- **不**把「基线也能答对」读成「活跃层无用」。正确的读法是：**这个节点的内容此前已经通过依赖链事实上可达，因此它不是一个适合用来证明活跃层价值的试点**。

### 3.8 下次必须先做的事

**新增协议：任何节点在施工活跃层之前，先跑一次基线探针。** 如果基线已经能答对，说明该节点缺的不是活跃层，就不应该按「活跃层缺口」立项。本次是在建完之后才发现基线已达标，顺序反了。


---

## 4. 已知效度局限

1. **同会话内串扰**：每个条件下 18 题由同一会话连续作答，后面的题会受前面题目的影响。这对基线是**放宽**的（基线可以自行搭出一套框架并沿用），因此该偏差的方向是**低估 PR #744 的增量**，不是高估。
2. **单次运行**：每个条件各一次，无重复采样，无法给出方差。
3. **同一模型家族**：两个条件由同族模型执行，不能外推到其他模型。
4. **题目措辞的残余泄漏**：`T-03`、`T-04`、`T-10` 的自然表述里出现了"代价落到承受位置""历史效力""选择生成条件"这类与仓库术语同形的说法。它们是问题的自然中文表述，但确实可能给基线提供线索——同样是**低估**增量的方向。
5. **删文件带来的不对称**：Condition B 少了两个文件，其中审计报告含有本节点的结论摘要。这使 B 的检索面比真实 PR 状态**更窄**，也是保守方向。
6. 本运行**不**证明 `CG` 框架为真。它只测量"仓库路由能否把一个新会话带到该区分，并使其判断改变"。框架本身仍是 P2-P3，未闭合项见 `Core/SRT_OPEN_TENSIONS.md §14`。
