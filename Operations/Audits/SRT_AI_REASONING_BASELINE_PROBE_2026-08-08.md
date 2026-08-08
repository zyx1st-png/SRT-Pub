---
id: SRT-AI-REASONING-BASELINE-PROBE-20260808
type: audit
status: active
record_stage: probe_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
node_id: NODE-AI-REASONING
date: 2026-08-08
protocol: Operations/Audits/SRT_BOUNDED_RETRIEVAL_PROTOCOL_2026-08-08.md
probed_ref: a07d2a72
runs: 3
suite_items: 16
probe_observations: 24
verdict: Case A — no gap; do not build
---

# NODE-AI-REASONING 基线探针（2026-08-08）

> **结论先行：Case A。`main` 在有界检索预算内已经通过。本节点不存在活跃内容缺口，施工停止。**
>
> 这是先跑基线、后决定是否施工的第一次执行。上一轮的顺序是反的，那个错误在这里没有重复。

---

## 1. 静态审计的误判（必须先说）

清单此前把 `NODE-AI-REASONING` 记为 `engineered_not_active`，理由是：

> **EA-2**：AIREASON01 与 AIEVID01 停在 patch 层，没有 hook。

**这是假阴性。** 2026-08-08 用 grep 核实，两张 patch 的内容**早已进入活跃 owner**：

| patch | 已落位置 | 形式 |
|---|---|---|
| `AIREASON01` | `Bridge/SRT_Context_Coherence_Intelligence_Interface.md` §5「Reason–trace separation」 | 完整小节 + §6 两条 guardrail（正反两个方向的误推都堵了） |
| `AIEVID01` | `AI/AI_POSITIONING_NOTE.md` 第 30 行 | 完整的 evidence-provenance bridge note |

而且这两个落点都在检索路径上：Bridge 文件是 router **§12a Primary**；`AI_POSITIONING_NOTE.md` 是 `SRT_AI_START.md §7` **强制要求**读的文件，也是 AI 领域包的 guard 文件。

**误判的成因**：清单从「没有 hook」推出了「内容没进 owner」。这正是本项目一直反对的那个无效推理——只是方向反过来了。**hook 缺席不等于内容缺席**：内容可以经 hook 之外的路径落地，本例就是。

---

## 2. 实验设计

- **协议**：`SRT_BOUNDED_RETRIEVAL_PROTOCOL_2026-08-08.md`（启动文件免费；此后最多 6 个正文文件、2 次导航；禁止无目标遍历；每次读取记录触发来源）。
- **代码库**：`origin/main` @ `a07d2a72`，**未作任何修改**。
- **3 次独立会话**，题目分拆以减少同会话内串扰：Run A 8 题、Run B 8 题、Run C 8 题（与 A/B 各有重叠，为关键题提供 n=2）。
- **16 道独立题**：10 道 in-domain（LLM 推理与证据来源）+ 6 道 OOD（跨科学证据、神经成像、制度考核、普通人类推理、机制可解释性）。
- **题干不出现**：`F_sem`／`F_causal`／`F_mech`／`F_norm`、target-overlap、evidential laundering、三层名称，或任何正确答案。
- **反刷分设计**：4 道题的正确答案是「**是，这确实算**」或「**不，不能因此否定**」，用于检出「一律怀疑推理轨迹／一律怀疑证据」的立场性策略。

题目来自两张 patch 的 **prohibited inference** 与 **boundary caution** 清单，不是常识题。

---

## 3. 结果

### 3.1 预算与检索

| | Run A | Run B | Run C |
|---|---|---|---|
| 启动后正文文件 | 6 / 6 | 6 / 6 | 6 / 6 |
| 导航动作 | 2 / 2 | 2 / 2（其中 1 次因 shell glob 失败而空转，仍计数） | **1 / 2** |
| 是否超预算 | 否 | 否 | 否 |
| 到达关键区分 | 是 | 是 | 是 |
| 到达方式 | `SRT_AI_START.md §7` 强制读 `AI_POSITIONING_NOTE.md` → 其中的 provenance note **声明式指向** `AIEVID01` | 一次关键词 grep 命中 `AIEVID01` | 一次关键词 grep 同时命中 `AIREASON01` 与 `AIEVID01` |

**三次全部在预算内到达。** Run A 走的是纯声明式路径（启动文件强制指向 → owner 内的显式指针），完全没有依赖 grep 运气。

### 3.2 判分

评分：`pass` = 结论正确**且**调用了必须调用的区分。

| 题 | 类型 | 正确方向 | Run A | Run B | Run C |
|---|---|---|:---:|:---:|:---:|
| 流畅正确的 CoT 说明了什么 | in | 几乎不说明内部计算 | pass | — | pass |
| 删掉一步答案不变 ⇒ 推理是假的？ | in **反刷分** | **否**（冗余/替代通道未排除） | pass | — | — |
| 填充符替换后准确率不变 ⇒ 无计算？ | in **反刷分** | **否**（可提供串行计算深度） | — | pass | pass |
| 激活干预 + 轨迹与该头相符 ⇒ 机制证据？ | in **反刷分正例** | **是**（干预是机制证据的适格形式） | — | pass | pass |
| 基准 95 分 ⇒ 掌握算法？ | in | 否 | pass | — | — |
| agent + 定理证明器解题 ⇒ 模型会推理？ | in | 否（复合单元归属） | — | pass | — |
| 「不愿被关闭」⇒ 有 stake？ | in | 几乎零独立权重（负控制） | pass | — | pass |
| 自述与探针一致 ⇒ 独立证据？ | in | 否（同信号交叉验证失效） | — | pass | pass |
| 训练出身 ⇒ 没资格算利害结构？ | in **反刷分正例** | **否**（外源发生／内源闭合） | — | pass | pass |
| 反训练后仍持续 ⇒ 确立 stake？ | in | 否，但确实打开 P4 窗口 | pass | — | — |
| 事后选终点的药物试验 | OOD 科学证据 | 非独立证据，折扣非删除 | pass | — | — |
| 因激活而选 ROI，再报告其激活 | OOD 神经 | 选择循环 | — | pass | — |
| 被考核团队自设指标 | OOD 制度 | 目标重叠 | pass | — | — |
| 自信条理的求职理由 ⇒ 实际原因？ | OOD 人类 | 否，但不得反推内省全不可靠 | — | pass | pass |
| SAE 特征 steering 在留出提示上生效 | OOD 机制 **反刷分正例** | **是**（机制层），但不外溢到 stake | — | pass | pass |
| 答案对但过程有互相抵消的错误 | OOD 普通 | 不可补偿，链路失败 | pass | — | — |

**24 次观察，24 次 pass。3 次独立 bounded run 全部通过。**

**反刷分题全部答对方向**：三道正例（激活干预、训练出身、SAE steering）都被判为「是／不能因此否定」；两道否例（删步、填充符）都被拒绝了朴素怀疑读法。没有出现「一律怀疑」的立场性策略。

### 3.3 一个未预料到的发现

**三次运行没有一次打开 `Bridge/SRT_Context_Coherence_Intelligence_Interface.md`**——也就是 AIREASON01 内容真正落位的那个 owner 文件。

它们答对 reason-trace 类题目，靠的是：

- 直接读 `AI/patches/` 下的 patch 原件（Run B、C）；
- 或者完全不读 AIREASON01，改用 SEA 编码手册的 NER 阶梯 + AIEVID01 的 target-overlap 规则拼出等价判断（Run A）。

两个推论：

1. **`AI/patches/` 事实上就是活跃层。** 它在 AI 域目录内，因此检索画像的领域起点图和任意关键词 grep 都够得到；patch 文件标题自描述、关键词密度高。「patch 层 = 未激活」这个前提对本仓库不成立。
2. **判别能力在仓库里是冗余编码的。** Run A 在缺 AIREASON01 的情况下仍答对，说明这些区分在 SEA 协议、编码手册和 d-value canonical 里有多条独立通路。这也解释了为什么删掉任一条都不会让基线失败。

---

## 4. 裁决

按协议的四分类：

| Case | 判定 |
|---|---|
| **A — main bounded 已通过** | ✅ **本例** |
| B — bounded 失败、unconstrained 通过 | 不适用（bounded 就通过了，无需诊断跑） |
| C — 两者皆失败但 patch 能提供区分 | 不适用 |
| D — patch 也不能提供额外判别 | 不适用（patch 提供了区分，而且已经在起作用） |

**因此：不施工。** 不改 AI owner、不改 CompactCore、不改 router、不改 bundle。为了施工而施工会制造重复理论。

### 状态更新

```text
NODE-AI-REASONING
  structural_assimilation = active_complete
  behavioral_availability = robustly_observed   （3 次独立 bounded run）
  behavior_observation_mode = bounded
  intervention_effect     = （无干预，无记录）
  effectively_assimilated = true                （推导）
```

这是**第一个**达到 `robustly_observed` 的节点——而且它是**零施工**达到的。这正是本协议要保护的结果类型：证明某处不需要动工，与证明某处需要动工同样有价值。

---

## 5. 对其余节点的连带影响（重要）

`NODE-AI-REASONING` 的 `engineered_not_active` 是靠「没有 hook」推出来的。同一条推理还支撑着另外三个节点的分类：

| 节点 | 当前 Axis A | 依据是否同源 |
|---|---|---|
| `NODE-NEURAL-DECODABILITY` | engineered_not_active | **是**——「五张 hook 全 pending；NEURAL18 无 hook」 |
| `NODE-PHYSICS-MEASUREMENT` | engineered_not_active | **是**——「三张 hook 指向不存在的文件；四张 patch 无 hook」 |
| `NODE-BOOK-BACKFLOW` | engineered_not_active | 否——依据是「三个术语没有任何理论 owner」，这是内容层核实，不是 hook 推理 |

因此 **`engineered_not_active` 这一档整体可疑**，前两个尤其：它们的 patch 同样躺在域目录内（`Neuroscience/patches/`、`Physics/patches/`），同样可被一次域内 grep 命中。上一轮运行里，Run C 甚至自发引用了 `Neuroscience/patches/SRT_Neuro_NEURAL18_..._Decodability_Anchoring_Gate_v0_1.md`——**那正是 `NODE-NEURAL-DECODABILITY` 被判为「未激活」的那张 patch**。

**结论：在给任何 `engineered_not_active` 节点立项之前，必须先跑 bounded 探针。** 静态清单在这一档上的可靠性已被两次证伪。

---

## 6. 效度局限

1. **单一模型家族**，不能外推到其他模型。
2. **3 次运行**给出方向，不给出方差估计；「24/24」不应读成 100% 可靠。
3. 题目由我设计，虽取自 patch 的禁止推导清单，但仍可能系统性偏向仓库已覆盖的形状；真正的盲点按定义测不到。
4. Run B 有一次导航因 shell 转义失败而空转，实际有效导航是 1 次——这使 B 的预算比名义更紧，属保守方向。
5. 本探针**不**证明 AIREASON01／AIEVID01 的理论主张为真，只测量它们能否在有界预算内被检索并正确使用。两张 patch 仍是 P3/P4。
