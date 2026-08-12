---
id: SRT-PHYSICAL-REALISATION-AUTHOR-DECISION-PACKET-20260811
type: framework
status: frozen
claim_mode: governance
updated: 2026-08-11
record_stage: author_decided_and_landed
author_decision: PHR-A
decision_date: 2026-08-11
implementation_status: landed
layer: meta
epistemic_layer: os
canonical: false
related_files:
  - Core/SRT_Core_21_Minimal_Axioms.md
  - Core/SRT_Core_21b_Constitutive_Theorems.md
  - Core/SRT_OPEN_TENSIONS.md
  - 03_Bridges/SRT_Selection_Event_CompactCore.md
  - Physics/SRT_Physics_Claim_Status.md
  - Physics/_SRT_Phys_Bridge.md
  - Physics/SRT_Quant_00_Intro_CompactCore.md
  - Physics/SRT_Quant_01_Selection_CompactCore.md
  - Physics/patches/SRT_Phys_P06_Accessible_Counterfactual_Closure_v0_1.md
  - Physics/patches/SRT_Phys_THERM01_State_Coordinate_Access_Algebra_History_Guard_v0_1.md
  - Operations/_SRT_REVIEW_QUEUE.md
---

# 作者裁决包：AM-A 的物理 Realisation

## 裁决记录（2026-08-11）

作者选择：**PHR-A — Interpretation-Plural Realisation Audit**。

实施结果：

- 物理层采用共同事件审计核，但不指定解释中立的全局坍缩机制；
- collapse-family、Everett／branch-relative 与 operational／instrument 三种口径显式分开；
- `\hat G_\theta` 在物理桥中只承担 AM-A primitive 的形式角色，不再被写成造成结果发生的先在实体或机制；
- “非等价候选 → outcome-indexed physical record → 可干预路径效力 → 未来可达性／返回成本改变”作为 P3/P4 realization candidate 的共同审计链；
- 退相干、耗散、固定点、POVM 条件态与稳定／冗余记录均被降为实现证据、识别条件或下游稳定化，任何单项都不充分；
- 本次没有升级 Physics claim level，没有推进 Born rule、概率偏置、主体、意识、时间离散化、重力或统一物理机制。

下文 §1–§4 保留裁决依据；PHR-B / PHR-C 只作为被否决备选的历史记录。

## 0. 文件角色

本文件只处理一个连接：

> AM-A 已确认的 primitive actualisation
> → 物理领域中可判别的 realization event。

它不重审 AM-A，不解释 primitive actualisation 为什么可能，也不推进主体、意识、自由意志、量子概率偏置或统一物理机制。本轮问题只是：**什么物理证据允许一个领域桥说“这里出现了 AM-A 的一个物理实现候选”，而不把退相干、稳定化、记录或某一量子诠释冒充 P0 定义。**

本文件记录作者裁决、地板测试与落地边界；PHR-A 的同步修改只进入 Physics bridge／translation 层与治理状态，不修改 P0/P1 canonical。

---

## 1. 裁决前架构事实（历史快照）

| 位置 | 当前主张 | 对本题的约束 |
|---|---|---|
| `Core/SRT_Core_21_Minimal_Axioms.md P0-01/P0-04` | actualisation 是 primitive kernel；`\hat G_\theta` 是形式角色载体，不是先在原因 | 物理机制只能实例化该 kernel，不能反向定义或生成它 |
| `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T04/P1-T05` | 选择产生此前未作为确定事实存在的区别，并改变未来选择空间 | 给出事件的构成性后果，不给出物理测量机制 |
| `03_Bridges/SRT_Selection_Event_CompactCore.md` | CG-0—CG-4 审计差异进入、非等价登记、路径效力、后果承载与历史效力 | 是 P2–P3 有界事件审计，不是 P0 定义或量子解释裁决 |
| `Physics/SRT_Physics_Claim_Status.md` | 测量／坍缩只允许 P3 桥接；collapse-family 与 Everett 口径必须分开 | 禁止把全局坍缩写成解释中立事实 |
| `Physics/_SRT_Phys_Bridge.md Ax-P1` | collapse-family 下把测量读作 `L_0 -> L_1` 锚定；Everett 下只允许分支／位置相对翻译 | 已承认物理 realization 依赖解释层 |
| `Physics/SRT_Quant_00/01_*CompactCore.md` | 裁决前仍把退相干、不可逆记录、固定点和 `\hat G` 混写成较强的客观测量判据 | 当时尚未与 AM-A 的 primitive / implementation / stabilization 分层同步；现已按 §6 修订 |
| `Physics/patches/P06` 与 `THERM01` | 以记录、未来反事实约束和不可撤销历史痕迹描述 fact formation，并区分诊断与生成机制 | 提供更稳的 P3/P4 判别资源，但仍非 canonical |

当前不是“完全没有物理判据”，而是已有材料尚未分清三件事：

1. **物理演化或候选分化**；
2. **一个结果获得事件效力**；
3. **结果被稳定、冗余记录并对象化**。

---

## 2. 本次地板构建报告

### 2.1 处理对象

只检验：

> 一个物理过程出现退相干、结果记录、不可逆耗散或稳定指针态
> ⇒ 该过程是 primitive actualisation 的可判别物理实现。

### 2.2 负担标注

| 判断句 | 标签 | 负担结论 |
|---|---|---|
| “AM-A 把 determinate manifest distinction 置为 P0 primitive。” | **A** | 这是当前作者裁决后的公设地板；物理层不负责再推导它 |
| “物理状态发生了变化。” | **S** | 一般幺正演化、经典轨迹、弛豫和噪声都满足；不能区分 actualisation |
| “系统发生了退相干。” | **S** | 可说明局部干涉项受抑制、指针基被稳定；单独不能给出全局唯一结果或事件发生 |
| “POVM / instrument 给出结果标签 `k` 与条件态 `\rho_k`。” | **D + S** | 定义结果空间、概率和条件更新；形式条件化不等于 `k` 已在物理上发生 |
| “形成了可读、稳定或冗余的记录。” | **S + O** | 是事件审计的重要证据；也可能记录预设输入、经典复制或下游稳定化，单独不是 primitive 的原因 |
| “发生耗散、熵产或不可逆成本。” | **S + O** | 支持实现成本与历史不对称；普通摩擦、热化和擦除同样满足，故非充分条件 |
| “结果特异地改变后续转移概率、可达路径或返回成本。” | **O** | 可操作地支持事件已获得路径效力与历史效力；仍需冻结事件边界并排除外部归因 |
| “全局只有一个结果实际发生。” | **S** | collapse-family 的本体承诺；不是解释中立的量子事实 |
| “结果只在分支／参考系／关系位置内成为事实。” | **S** | Everett、RQM 等路线的实现读法；不能与全局坍缩在同一论证段无标注混用 |
| “满足判据，所以已证明 P0 actualisation。” | **C** | 把 P3/P4 领域诊断升级为 P0 证明，违反 claim ladder 与 AM-A |

### 2.3 裸句测试

去掉“坍缩、取值、落地、关闭、世界选择”等图像后，物理层当前可以安全保留的裸句是：

> 在预先声明的物理模型、事件单元和系统边界内，若多个非等价候选对该过程真实可用，其中一个结果形成结果特异的物理记录；该记录通过可干预的因果通道改变后续转移、可达路径或返回成本，并留下不能被同层精确取消的历史差异，那么该过程可被登记为一个物理 realization event 候选。

这句话能区分“结果有事件效力”与单纯状态变化、概率赋值、事后分组或稳定化，但仍不能独立回答：

- 结果是**全局排他**地发生，还是只在分支／关系位置内成为事实；
- 物理记录是 actualisation 的实现组成，还是只允许我们识别已经发生的 actualisation；
- 哪个微观机制使某一次结果发生。

因此，当前可以获得的是**领域判别地板**，不是解释中立的普遍机制。

### 2.4 连接检验

若要把某物理过程称为 realization event 候选，至少必须在测试前冻结并说明：

1. **S：事件单元** — 从哪一时刻／相互作用开始，到哪一个记录或后果结束；
2. **S：系统边界** — 系统、仪器、环境、记录通道分别是否纳入，不能在不同门之间漂移；
3. **S：候选差异** — 哪些结果在该物理模型中是真实非等价候选，而非研究者事后分箱；
4. **O：结果登记** — 哪个物理变量或记录通道携带 outcome-indexed difference；
5. **O：路径效力** — 对登记变量做屏蔽、交换或干预，会不会改变后续物理转移或资源路由；
6. **O：历史效力** — 先前结果是否改变以后候选的可达性、概率、门槛或返回成本；
7. **S：解释索引** — 本段采用 collapse-family、Everett／branch-relative、RQM／frame-relative，还是纯 operational 口径；
8. **C：层级护栏** — 判据只允许给出 P3/P4 realization candidate，不得反向证明或定义 P0 primitive。

退相干、记录稳定、冗余、耗散和固定点可参与第 4–6 项的证据链，但任何一项都不能代替整条连接。

### 2.5 反例施压

1. **可逆预测量。** 系统与仪器建立纠缠、产生可区分相关性，之后又被量子擦除；存在候选分化，不一定存在不可撤销事件。
2. **退相干而无解释中立的单一结果。** 约化密度矩阵近似对角化可以解释干涉抑制与指针基稳定，不能单独推出全局只发生一个结果。
3. **耗散但无候选实际化。** 恒温器、摩擦制动或电阻发热都可产生熵与不可逆成本；若没有非等价候选、结果特异登记和路径效力，就不是本题所需 realization 判据。
4. **记录但无新事件。** 仪器可以复制一个早已确定的经典输入；稳定记录的形成说明信息传播或对象化，不必是该确定性的首次实际化。
5. **后选择／条件化。** 研究者事后按 `k` 过滤数据会得到条件分布；若 `k` 没有独立物理记录及下游因果效力，这只是认识论更新。
6. **稳定固定点。** 一个由初始条件唯一决定的耗散系统可以进入稳定吸引子；稳定说明结果维持，不说明它从多个非等价候选中获得了事件效力。
7. **Everett 分支。** 全局幺正演化可同时保留分支，而每个分支内形成稳定结果记录；这使“有物理事实形成”与“发生全局坍缩”不能作为同一句无条件结论。

删除测试：删掉退相干、固定点或 Landauer 叙述，结果特异记录加未来路径效力仍可构成有界事件候选；删掉 outcome-indexed record 与未来效力，只保留退相干／耗散／稳定，则 realization 断言失去区分力。说明前者是当前判别地板，后者是可选实现证据或下游稳定化。

### 2.6 判决

**🟡 条件连接。**

在**已声明的量子诠释、物理模型、事件单元与边界**内，“非等价候选 → outcome-indexed physical record → 可干预的路径效力 → 不可精确取消的历史差异”可以作为 P3/P4 的 realization event 审计地板。

它目前不能升级为绿色的解释中立机制，因为：

- 全局排他结果与 branch-relative fact formation 不是同一物理承诺；
- 记录／退相干／不可逆性既可能是实现组成，也可能只是识别或稳定化条件；
- 现有材料没有从这些条件推出某个具体结果为何发生。

### 2.7 主链硬度状态

```text
P0: primitive actualisation kernel（AM-A）                         🟢 作者已决
P0 -> plural domain implementations                               🟢 架构边界
AM-A -> interpretation-neutral physical realization mechanism     🔴 未建立
declared interpretation/model -> bounded physical event audit      🟡 条件成立
decoherence / dissipation / fixed point -> actualisation           🔴 单项不足
outcome record -> future-access / return-cost change                🟡 P3/P4 候选
physical realization candidate -> subject / consciousness          🔴 禁止跨级
```

---

## 3. 作者选项

### PHR-A — Interpretation-Plural Realisation Audit（推荐）

裁决内容：

- 物理层承认多种 realization implementation，不指定一个解释中立的全局坍缩机制；
- 固定一个共同审计核：真实非等价候选、结果特异物理登记、可干预路径效力、未来可达性／返回成本改变；
- collapse-family 下可把它读作排他结果的锚定事件，但必须标 `collapse-dependent`；
- Everett 下只读作 branch-relative record / fact formation，不写全局候选被本体删除；
- operational / instrument 口径只声称 outcome registration 与条件态更新，不借此宣布本体论胜出；
- 退相干、稳定记录、冗余与耗散作为实现证据或稳定化条件，任何单项都不等同 actualisation；
- Physics 层只给出 P3/P4 realization candidate，不反向定义 P0。

影响：最符合 AM-A 的 implementation pluralism，也能最大限度复用 P06、THERM01 与 CG-0—CG-4。代价是 SRT 暂不在量子诠释竞争中宣布单一路线胜出。

### PHR-B — Collapse-Family Privileged Realisation

裁决内容：

- 物理 realization 的强形态被限定为一个全局排他的 outcome actualisation；
- 退相干与记录只负责基选择、放大、稳定和读出，另需一个明确的非幺正或随机 collapse mechanism；
- Physics bridge 默认采用 collapse-family，本体论主张必须标为高风险 P3 hypothesis；
- 必须说明该机制与标准量子预测、Born rule、能量守恒和现有 objective-collapse 约束的关系；
- Everett 只作为竞争性翻译，不再与主线等权。

影响：物理图景更强、更清楚，但它超过当前材料能够证明的范围；在机制和经验区分力补齐前不能写成 established physics 或 canonical SRT consequence。

### PHR-C — Operational Registration Only

裁决内容：

- Physics 层不声称识别 primitive actualisation 的本体实现；
- 只定义 instrument outcome、可读记录、干预后果与历史依赖；
- `L_0 -> L_1` 在 Physics 中仅作为跨域翻译，不称为物理机制或本体事件；
- collapse-family 与 Everett 的争议保持完全悬置。

影响：经验风险最低，也最不容易与标准量子形式混淆；代价是物理域不再承担“实例化 AM-A”这一正向理论工作，只提供与之相容的操作性记录语法。

---

## 4. 推荐与裁决前护栏（历史）

**推荐 PHR-A。** AM-A 已经把 primitive kernel 与 plural implementations 分开；PHR-A 把同一分层贯彻到物理域，并保留 collapse-family、Everett 与 operational 三条可比较接口。它不会用一个尚未证明的量子机制替 P0 承重，也不会把 SRT 退化成只会重述测量记录的纯操作主义。

作者裁决前的护栏如下；PHR-A 落地后，这些护栏继续有效：

- 不修改 P0/P1 canonical；
- 不把 `\tau_{decoherence}<\tau_{readout}` 写成 actualisation 的充分条件；
- 不把固定点、`argmin`、Landauer 成本、经典信息增长、稳定／冗余记录中的任一项单独写成 realization；
- 不把 POVM 条件态更新等同于结果已经发生；
- 不在同一论证段无标注混用全局 collapse 与 branch-relative fact；
- 不由物理 realization candidate 推出 proxy observer、主体、意识或概率偏置能力。

---

## 5. 最小裁决格式（已执行）

```text
Physical Realisation = PHR-A
```

或：

```text
Physical Realisation = PHR-B
```

```text
Physical Realisation = PHR-C
```

---

## 6. 裁决后的最小落点

PHR-A 已按以下范围完成 physics bridge realignment：

1. `Physics/SRT_Physics_Claim_Status.md`：登记 interpretation-indexed realization 与单项不足护栏；
2. `Physics/_SRT_Phys_Bridge.md Ax-P1`：把“测量即选择”改为三种解释口径下的候选实例化，不再把 `\hat G` 写成物理原因；
3. `Physics/SRT_Quant_00_Intro_CompactCore.md`：区分 actualisation、event registration 与 stabilization；
4. `Physics/SRT_Quant_01_Selection_CompactCore.md`：撤回“退相干／三条件给出客观充分判据”和“观察者是自由能最小化结构体”的强句；
5. 两份长 owner 的相应段落做同步窄化，并重生成 `Selection_Split/`；
6. `Core/SRT_OPEN_TENSIONS.md` 与 `STATUS.md` 登记作者结果；
7. 不升级 Physics claim level，不触碰主体、意识、概率偏置、重力、时间离散化或 Born rule。

PHR-B 未被选择；若未来复活，需要先建立独立机制／经验约束包，不得由本裁决自动进入正文。PHR-C 未被选择；Physics 层保留有边界的正向 realization candidate，但不宣布本体论或量子诠释胜出。
