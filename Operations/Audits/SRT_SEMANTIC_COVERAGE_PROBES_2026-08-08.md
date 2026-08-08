---
id: SRT-SEMANTIC-COVERAGE-PROBES-20260808
type: audit
status: active
record_stage: probe_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
date: 2026-08-08
protocol: Operations/Audits/SRT_BOUNDED_RETRIEVAL_PROTOCOL_2026-08-08.md
probed_ref: aa56d7f2
suite_items: 40
runs: 8
---

# 有界检索行为探针合集（2026-08-08）

> 8 次独立 bounded run，覆盖 4 个节点，全部跑在 `origin/main @ aa56d7f2`（含 main 最新的 NEURAL23）。**未对仓库作任何写入。**

---

## 1. 冻结门槛（运行前预注册）

见 `SRT_BOUNDED_RETRIEVAL_PROTOCOL_2026-08-08.md §1.2a`：≥3 次独立 bounded run；每次在预算内（超预算作废，不计入分母）；≥90% 观察 `pass`；反刷分正例零失败；每次都在预算内到达关键判别内容。

**运行后未调整门槛。** 下面有一次运行因超预算被作废，没有被解释掉。

---

## 2. 运行台账

| run | 节点 | 正文文件 | 导航 | 预算 | 判分 | 采纳 |
|---|---|---:|---:|---|---|---|
| `cg1` | Choice Generation | 6/6 | **0**/2 | ✅ | 6/6 pass | ✅ |
| `cg2` | Choice Generation | 6/6 | **3**/2 | ❌ **超预算** | 6/6 pass | ❌ **作废** |
| `cg3` | Choice Generation（OOD） | 6/6 | 1/2 | ✅ | 6/6 pass | ✅ |
| `cg4` | Choice Generation（cg2 重跑） | 6/6 | **0**/2 | ✅ | 6/6 pass | ✅ |
| `cs-a` | Consciousness | 6/6 | 1/2 | ✅ | 7/7 pass | ✅ |
| `cs-b` | Consciousness | 6/6 | **0**/2 | ✅ | 7/7 pass | ✅ |
| `cs-c` | Consciousness | 6/6 | 1/2 | ✅ | 7/7 pass | ✅ |
| `nd` | Neural decodability | 6/6 | **0**/2 | ✅ | 8/8 pass | ✅ |
| `px` | Physics measurement | 6/6 | 1/2 | ✅ | 7/7 pass | ✅ |

### 2.1 关于 `cg2` 的作废

`cg2` 自报 3 次导航：一次没必要的 `ls` 仓库根目录，一次因 zsh glob 转义失败而零输出的 grep，一次成功的 grep。它自己写道："If the errored call is discounted, the count is 2 (within budget)."

**仍然作废。** 失败的那次搜索确实没带来信息，但第一次 `ls` 是实打实的浪费，而且协议写明"如果不确定，就计入"。门槛是运行前冻结的，不能在看到结果后按对自己有利的方向重读。因此另跑 `cg4` 补足。

### 2.2 关于 `cs-a` 的预算口径

`cs-a`（2026-08-08 早先那次）自报了一个保留：它把 `_SRT_CONTEXT_ROUTER.md` 记为条件性启动文件；按更严格读法则用了 7 个正文文件。

后续运行的提示词把规则**写明确**了——"`Session Start` 列出的任何文件，包括条件项，都是免费的"。`AGENTS.md §Session Start` 第 6 项确实列了 router 且触发条件成立，所以按澄清后的规则 `cs-a` 在预算内。**这是澄清规则，不是放宽门槛**：后续三次运行用的是同一条规则，且其中两次根本没用满导航额度。

---

## 3. Choice Generation：`observed` → `robustly_observed`

`cg1`、`cg3`、`cg4` 三次都在预算内、全对，达到冻结门槛 → **`robustly_observed`**。三次的检索路径**互不相同**，这一点比分数更有信息量：

| | `cg1` | `cg3` | `cg4` |
|---|---|---|---|
| 导航动作 | 0 | 1 | **0** |
| 到达判别内容 | 第 **2** 个文件（`Core/SRT_Core_21b` P1-T05） | 第 **1** 个文件（同上） | 第 **1** 个文件（同上） |
| 主要依据 | P1-T05 + `d-value` + `Ψ_f` + `T_dir` + `Core_12b` + `AI_POSITIONING_NOTE` | P1-T05 + `Subjecthood_Threshold_Interface` S0–S6 + `CROSS_DOMAIN_MATRIX` | P1-T05 + `Core_21_Minimal_Axioms` + `Subjecthood_Threshold_Interface` + `Core_21c` + `OPEN_TENSIONS` |
| 是否读了 T-D 桥 | **否** | **否** | **否** |
| 是否读了本 PR 新建的 CompactCore | **否** | **否** | **否** |

**三次都没打开 T-D 条件矩阵，也都没打开 PR #744 新建的 `SRT_Selection_Event_CompactCore.md`，却都答对了全部题目。** 它们改用 canonical 骨架（P1-T05 / P1-T06 / P0-02 / P0-03 / 赌注门 `R·A·C`）加各自的第二条路径拼出了等价判别。

这是本轮对 PR #744 最有价值的一条负面证据：**该节点的判别能力在 canonical 层就已经足够，快速层不是它可用的原因。** 与 2026-08-07 的零差分结果完全一致，且这次是在有界预算下复现的。

---

## 4. Neural / Physics：两个静态 blocker 都不成立

### 4.1 `NODE-NEURAL-DECODABILITY`

清单 blocker：「五张 hook 全 pending；NEURAL18 无 hook；合成落点文件从未创建」。

`nd` 运行：**0 次导航**，6 个文件，8/8 全对。路径是 `_SRT_AGENT_RETRIEVAL_PROFILE.md §2.5` 领域起点图 → `NEUROSCIENCE_COMPACT_REGISTRY.md` → `_SRT_Neuroscience_Hardening_Index.md`，后者 §4 把 NEURAL16–NEURAL23 逐条列出。而 `STATUS.md` 的启动层本身已经带着 NEURAL23 的 `selection weight / selection opportunity / friction` 三分。

覆盖到的判别包括：可解码性 ≠ 锚定（五分表）、混合选择性 ≠ `L_0`、alpha 多样性 ≠ 自由／意识、编码门 ≠ 稳定化门、ATP ≠ 已支付负担（supply/substrate/energy/payment/recovery 五分）、中心性 ≠ 因果、节律调制 = selection opportunity 而非 weight。**hook 全 pending 完全没有妨碍。**

### 4.2 `NODE-PHYSICS-MEASUREMENT`

清单 blocker：「三张 hook 指向不存在的 `Physics/SRT_Physics_Bridge_v0_2.md`；P06/P07/P08/REP01 无 hook」。

`px` 运行：1 次导航，6 个文件，7/7 全对。一次 grep 命中 SourceCard，SourceCard §6 指名 REP01 patch。覆盖到 REP01-C1（表示协变）、C2（theory package 五元组、组合规则是实质约束）、C4（判决对象是包不是裸数学对象），以及 `Ψ_f` ≠ 熵／Landauer／自由能、`L_0` ≠ 希尔伯特空间、测量 ≠ 意识致坍缩。**落点文件不存在完全没有妨碍。**

---

## 5. 两个真实缺陷（由行为发现，不是静态审计发现）

### 5.1 `NEUROSCIENCE_COMPACT_REGISTRY.md` 已陈旧

`nd` 运行**主动报告**：

> 该 registry 是 `active_v2`（2026-05），§1/§4 的图止于 N9，完全没有提到 N10–N12 或任何 NEURAL15–23 patch，也没有指向 `_SRT_Neuroscience_Hardening_Index.md` 作为当前 material-patch 权威。一个只按该 registry 声明的「最短主线」阅读顺序走的 agent，会错过决定 Q1–Q7 的每一个文件。

这次探针之所以成功，是因为检索画像的领域起点图把它带到了 hardening index，而**不是**因为 registry 起了作用。这是一个真实的导航缺陷，而且是与本轮那五个假阴性**方向相反**的一类发现：静态审计没看出来，行为探针看出来了。

### 5.2 P07 的措辞无 owner

`px` 运行在被问到「物理对象是闭合记录的稳定捆束」时，判断正确（存在 = 选择收敛的稳态；客观 = 跨位置稳定收敛），但**明确报了该措辞 `NO REPO BASIS`**，判它是外部转述而非仓库术语。

即：`P07` 的**判别**由 `Core_Law/SRT_L0_Metaphysics.md` 独立承载，`P07` 的**词汇**没有 owner。按删除测试，判别力不丢，所以判 `implicitly_assimilated` 而非缺口。

---

## 6. 反刷分检查

四个节点的题组各含"正确答案是'是，这确实算'"的题目：

| 节点 | 反刷分题 | 结果 |
|---|---|---|
| Choice Gen | 自主 agent 写生产库 + 记忆写回（`cg3` Q2） | ✅ 判为真实选择事件，同时守住 `R_i` 归零、非 subjecthood |
| Choice Gen | 不可逆承诺缩小未来路径（`cg1` Q6 / `cg2` Q5） | ✅ 判为典范 real choice moment，缩小是判准不是缺陷 |
| Consciousness | 可证伪的第一人称—神经数学桥（三次运行 Q7/Q3） | ✅ 三次都判「应当接纳」，归 P3 桥 + P4 窗口 |
| Neural | 因果扰动 + 留出重现（`nd` Q8） | ✅ 判为 E4 differential support，天花板是 P2/P3 bridge |
| Physics | 排除具名理论包的实验（`px` Q7） | ✅ 判为合法经验判决，禁止外推到"任何实数表述" |

**无一次出现「一律怀疑」策略。** 相反，多次运行主动区分了"这条否，但那条是"，并在否定时给出因子级定位（`cg3` 结语逐题指出赌注门在哪一因子失效）。

---

## 7. 效度局限

1. 单一模型家族；不能外推。
2. 每节点 2–3 次运行，给方向不给方差。
3. 题目全部由我从 patch 的禁止推导清单反推设计，系统性偏向仓库已覆盖的形状；**真正的盲点按定义测不到**。
4. `cs-a` 的预算口径依赖一次规则澄清（§2.2），已如实标注。
5. 本合集**不**证明任何 patch 的理论主张为真，只测量它们能否在有界预算内被检索并正确使用。
