---
id: SRT-CROSS-SCALE-GENERATIVE-EMERGENCE-WRITEBACK-PLAN-2026-07-12
type: execution_plan
tags: [CrossScale, Emergence, Reductionism, CoordinatedClosure, LateralInhibition, Shadow, SelectionProxy, BookWriteback]
status: active_execution_plan
layer: meta
epistemic_layer: os
claim_mode: operations_execution
canonical: false
scope: theory_book_repository_writeback
role: single_task_entry
created: 2026-07-12
updated: 2026-07-12
source_issue: 657
initial_baseline: 690adaa4f36efbf8399bc2db06aa8124036f3b62
dependency: [SRT-AGENTS, SRT-AGENT-RETRIEVAL-PROFILE, SRT-BOOK-CURRENT-STATUS, SRT-BOOK-ACTIVE-MANIFEST, SRT-CANONICAL-FREEZE, SRT-EDIT-PROTOCOL]
---

# SRT 跨尺度生成与选择代理回写执行计划

> 本文件是“传统还原主义的跨尺度生成缺口—协调性关闭—侧抑制原型—阴影保留—选择代理层”这一轮理论与书稿施工的**唯一执行主文件**。
>
> Codex、Claude、ChatGPT 或其他 Agent 执行本任务时，以本文件为 task specification；GitHub Issue #657 及其评论保留为问题来源和讨论留痕，不再作为需要自行拼接的平行任务说明。
>
> 本文件是运行层计划，不定义 canonical 理论。任何候选术语、判据、公式与命题，除非经过本文件规定的 canonical amendment gate，不得被表述为 SRT 已确立定义。

---

## 0. 当前状态与使用方式

### 0.1 当前施工状态

- 计划状态：`active_execution_plan`（Phase A 已完成，实体施工已按收缩版执行；见下）
- 理论与书稿正文施工：**已按 Phase A 审计收缩版执行，并经 PR #660 两轮评审反馈修订**。Phase A 覆盖矩阵见 `Operations/SRT_CROSS_SCALE_GENERATIVE_EMERGENCE_AUDIT_2026-07-12.md`，结论：多数构件已在 canonical/bridge 有对应，但"局部 optionality↓→协调性关闭→宏观有效选择↑"这一生成步与既有对象（PCC / Def-C-1 / 集体 ISP 器官）是**相邻·不可等同**、待验证的候选映射，非别名；canonical 裁决 **H-A（不改，理由=候选未成熟非已覆盖）**。实体工作收缩为 source trace + Q10 章末注九 + Q23 一句回链 + OPEN_TENSIONS 一条 Open Tension + 版本治理同步。**授权状态**：作者已在 2026-07-12 当前对话中以“直接帮我调整后合并”明确授权本 PR 采用“收缩执行·用既有语汇 + 六候选术语不进正文”的实施方案；该授权仅覆盖本轮施工与合并，不等于 canonical 理论裁决或术语冻结。PR #660 评审反馈由 AI reviewer 经 OWNER 账户提交，仍非作者署名理论意见；决定与反馈 provenance 见 `01_Source_Intuition/SRT_CROSS_SCALE_SELECTION_PROXY_TRACE_2026-07-12.md`。
- 已完成前置治理：PR #658 已合并，当前书稿优先、归档降权与 CI 守门已经生效
- Issue #657：保留为 provenance；本文件整合其正文与后续补充
- initial consolidation baseline：`690adaa4f36efbf8399bc2db06aa8124036f3b62`
- Phase A 执行基线：`c47d6b35989f9af09daa132dc9ce64c9b21c0679`

执行时不得把上述 baseline 当成永久固定版本。每次开始任务必须：

1. 获取默认分支当前 HEAD；
2. 记录实际执行基线；
3. 重新读取当前状态和 active manifest；
4. 若相关文件已被其他 PR 更新，先做差异审计，不得覆盖新版本。

### 0.2 唯一主文件规则

本任务的入口层级是：

```text
仓库运行总入口：AGENTS.md
本任务唯一执行主文件：本文件
当前书稿状态入口：BOOK_CURRENT_STATUS.md
当前书稿机器路由：BOOK_ACTIVE_MANIFEST.json
理论定义守门：canonical anchors + symbol table + governance protocol
```

不得使用以下内容替代本文件：

- Issue #657 的单独一条评论；
- 对话摘要；
- `Archive_52Chapter/` 中的旧章节；
- 尚未审计的 bridge 草稿；
- Agent 自行生成但未写回的临时计划。

---

## 1. 任务目标

本轮目标不是只把“选择代理层”作为一个新比喻加入书稿，而是补足一条完整的跨尺度生成链：

```text
传统还原主义在生成侧的解释缺口
→ 低尺度差异与局部相互作用
→ 相互促进、竞争性抑制和彼此让路
→ 参与式退让
→ 协调性关闭
→ 共同前景 + 张力/后续摩擦/阴影场
→ 协调模式沉积与 L2 背景化
→ 选择代理层形成
→ 新的宏观状态变量与行动能力
→ 形成后的向下约束与摩擦重分配
→ 生成性代理、替代性代理与支配性代理分叉
→ 在附加闭包条件下，才可能形成高阶 ISP
```

### 1.1 总命题候选

> 涌现不是属性无因出现，也不只是复杂度增加，而是可选择性的跨尺度重组：局部可能性的协调性关闭，被转化为整体可能性的开启。

### 1.2 整体候选命题

> 整体首先不是站在上方管理个体的实体，而是低尺度单元在反复协调中，对一类彼此不兼容或重复发生的选择进行参与式退让后形成的代理层。它把不必每次重新完成的协调选择沉积为共同背景，降低重复摩擦，并生成新的宏观可行动自由度。

### 1.3 健康性候选命题

> 健康代理压缩重复协调，却不应永久取消构成单元的重选能力。代理若替个体完成选择，同时截断后果、遮蔽来源并取消重新授权，就从脚手架退化为牢笼。

以上均为 candidate propositions，不是 canonical 定义。

---

## 2. 必须正面回答的理论问题

### 2.1 传统还原主义的生成解释缺口

本轮不得把“还原主义”塑造成一个单一且容易反驳的稻草人。比较时至少区分：

- 组成式分析：系统由哪些部分构成；
- 机制式分析：局部机制与相互作用如何运行；
- 因果依赖：宏观状态如何依赖微观状态；
- 弱涌现：宏观模式是否只能通过运行系统得到；
- 取消式或强还原主张：宏观属性是否只是微观描述的可删缩写。

SRT 本轮需要补充的是**生成侧机制**，而不是否定组成、机制和因果追踪的价值。

核心问题是：

> 即使我们知道所有组成单元、局部规则和相互作用，什么使一组局部可成为性转化为新的宏观可选择属性、共同状态变量和整体行动能力？

不得只用以下表述代替回答：

- “因为系统很复杂”；
- “因为整体大于部分之和”；
- “因为出现了新层级”；
- “因为发生了自组织”；
- “因为存在涌现属性”。

这些表述可能描述现象，但尚未说明生成操作。

### 2.2 参与式退让与协调性关闭

候选术语分工：

- **参与式退让（participatory yielding）**：描述单元侧的相互响应、让路和内生自限；
- **协调性关闭（coordinated closure）**：描述关系网络层面，一组不兼容可能性退出共同前景，并形成共同可行空间的结果；
- **选择代理层（selection proxy layer）**：描述协调模式沉积后，开始替构成单元处理一类重复选择的共享结构。

三者不得混写成同义词。

协调性关闭必须满足至少两个否定条件：

1. 不是预存高层中心的单向命令；
2. 不是把被关闭可能性从系统中彻底删除。

### 2.3 关闭不等于删除

退出共同前景的方向可继续以不同形式作用：

- 低表征系统：张力、后续摩擦、受抑制可达性、阈值敏感性；
- 具有内部表征与历史保持能力的系统：可进一步形成阴影；
- 社会制度：异议、未满足需要、退出压力、申诉路径、替代方案；
- 训练或学习系统：未采用路径留下的权重、偏置、代价和可恢复性差异。

不得把所有受抑制状态无门槛地称为“阴影”。必须遵守当前 Q06 对阴影门槛及“成功选择 / 失败选择 / 未完成选择”三分的最新口径。

### 2.4 侧抑制的理论位置

侧抑制是本轮的重要机制原型，但不是跨尺度普遍同一机制。

它用于显示：

- 前景可以由局部相互促进和竞争性抑制自下而上形成；
- 不需要先有一个中央管理者决定谁进入前景；
- 被抑制方向不必归零，而可参与对比度、边界、敏感性和未来重选储备；
- 前景和被压低场的共同组织，而非只有胜出者，构成系统的真实状态。

必须同时声明：

- 神经侧抑制是实现范例或结构显影；
- 不能由此推断细胞、生态、社会、市场和制度都使用同一种神经机制；
- 跨尺度推广的是关系结构，不是具体生理装置；
- 任何神经科学新增必须先过当前 neuroscience claim-status 和 bridge 边界审计。

### 2.5 代理层与高阶 ISP 的区分

必须保持：

```text
选择代理层 ≠ 高阶 ISP
```

代理层可以只是：

- 共享脚手架；
- L2 背景结构；
- 制度器官；
- 记忆、协调或分配接口；
- 重复选择的压缩层。

只有在满足现有 Collective Selection 要求时，才可能进一步构成高阶 ISP，包括但不限于：

- 共同可选择性；
- 共同视角；
- 健康后果回路；
- 共同重选；
- 可追踪的历史与边界；
- 后果不能被系统性外包给无发言位置。

不得因为一个制度、市场、神经网络或组织具有协调功能，就直接称其为主体。

---

## 3. 最低生成判据候选

后续 bridge 必须审查，而不是预设，以下条件是否足以区分生成性跨尺度形成与普通压制：

```text
C1 低尺度单元之间存在内生的相互响应，而非只有外部单向控制
C2 局部独立可选择性在特定领域内下降
C3 相互协调稳定或共同可行性上升
C4 被关闭方向仍保有残余因果相关性
C5 协调模式能够沉积、继承、重入或形成迟滞
C6 系统产生新的宏观状态变量或宏观行动能力
C7 宏观结构形成后能够重新分配下层摩擦和可达路径
C8 系统仍保留非零的重新选择、重新授权或重新开放能力
```

候选压缩表达：

\[
\Delta A_{\mathrm{independent}}^{\mathrm{local}}<0,
\qquad
\Delta C_{\mathrm{coord}}>0,
\qquad
\Delta A_{\mathrm{effective}}^{\mathrm{macro}}>0
\]

并附加：

\[
R_{\mathrm{residual}}>0,
\qquad
H_{\mathrm{inherit}}>0,
\qquad
r_{\mathrm{reselect}}>0
\]

这些符号仅为 bridge 级工作记号。执行者不得擅自写入 symbol table 或 canonical equations。

### 3.1 必须登记的失败分支

- **纯压制**：局部可能性下降，但没有新的共同可行空间；
- **脆弱 winner-take-all**：单一方向胜出，系统对扰动极端脆弱；
- **短暂同步**：出现瞬时一致，但没有沉积、继承或宏观状态变量；
- **僵化锁定**：协调稳定上升，但重选能力趋近于零；
- **寄生性整体**：宏观结构获得自我维持能力，却持续消耗构成单元的选择能力；
- **代理捕获**：代理被少数位置控制，成本外包给其他位置；
- **尺度误判**：观察者把统计聚合误写成新主体或新选择层；
- **阴影误用**：把任何未胜出状态都心理化为阴影。

---

## 4. Agent 强制读取顺序

Codex、Claude 或其他 Agent 开始本任务时，必须按以下顺序读取。

### 4.1 仓库与任务入口

1. `AGENTS.md`
2. 本文件
3. `_SRT_AGENT_RETRIEVAL_PROFILE.md`
4. `STATUS_FAST.md`
5. `Operations/README.md`
6. `Governance/README.md`

### 4.2 当前书稿入口

7. `01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md`
8. `01_Source_Intuition/BOOK/BOOK_ACTIVE_MANIFEST.json`
9. `01_Source_Intuition/BOOK/BOOK_ARCHITECTURE_MAP_5ACT_2026-06-24.md`
10. `01_Source_Intuition/BOOK/BOOK_TERMINOLOGY_SIMPLIFICATION_GUIDE_2026-06-03.md`

### 4.3 当前正文 primary

必须读取最新版：

11. `01_Source_Intuition/BOOK/Drafts_26Q/Q06_排除与阴影.md`
12. `01_Source_Intuition/BOOK/Drafts_26Q/Q10_秩序背景化.md`
13. `01_Source_Intuition/BOOK/Drafts_26Q/Q19_脚手架与牢笼.md`
14. `01_Source_Intuition/BOOK/Drafts_26Q/Q23_共同体.md`
15. `01_Source_Intuition/BOOK/Drafts_26Q/Q28_回到生成.md`
16. `01_Source_Intuition/BOOK/Drafts_26Q/附录_跨域难题_重述而非解决.md`

根据实际 patch 位置，再读取相邻幕前、幕间桥和前后章节，避免局部增补破坏问题链。

### 4.4 当前理论与边界文件

17. `CANONICAL_REGISTRY.md`
18. `_SRT_SYMBOL_TABLE.md`
19. `Core_Law/SRT_Reference_Scaling.md`
20. `Core_Law/SRT_Collective_Selection.md`
21. `Core_Law/SRT_Collective_Tower_Hardening_Notes.md`
22. `Core/SRT_Core_21c_Bridge_Hypotheses.md`
23. `Core/SRT_OPEN_TENSIONS.md`
24. 与 L2、不可逆性、个体化和遮蔽直接相关的当前 canonical / hardening 文件，由 `_SRT_INDEX.md` 和 context router 解析，不凭记忆猜路径。

### 4.5 神经科学只读审计

25. `Neuroscience/README.md`
26. `Neuroscience/SRT_Neuroscience_Claim_Status.md`
27. 当前 neural mechanisms 主文件及 compact/hardening index，由 Neuroscience README 解析

此步骤先做只读比较，不得因为出现“侧抑制”关键词就直接修改神经 canonical-facing 文件。

### 4.6 编辑治理

28. `Governance/SRT_CANONICAL_FREEZE.md`
29. `Governance/SRT_EDIT_PROTOCOL.md`
30. `Governance/SRT_CLAIM_LADDER.md`
31. `Governance/SRT_CLAIM_MODE_AUDIT.md`

### 4.7 历史材料

只有完成以上读取后，才可打开：

- `01_Source_Intuition/BOOK/Archive_52Chapter/`
- `01_Source_Intuition/BOOK/Archive_Meta/`

历史材料只能用于：

- 概念迁移审计；
- 来源追踪；
- 旧例子回收；
- 当前稿遗漏检查。

不得作为当前初稿或 patch 母版。

---

## 5. 施工原则

### 5.1 最新版优先

- 所有初稿以默认分支当前文件为母版；
- 不根据旧稿 `v5/v6` 等文件名判断其比当前 Q 文件更新；
- 每次修改前重新 fetch 目标文件并记录 SHA；
- 若目标文件在施工期间更新，停止写入并重做差异审计。

### 5.2 先审计，再落笔

每个目标文件必须先给出：

1. 当前文件已覆盖什么；
2. 本轮真正缺什么；
3. 哪些内容会重复；
4. 哪些新增会改变现有主张；
5. 建议插入位置；
6. 不应写入本文件的内容；
7. 与其他目标文件的职责分工。

不得以“内容相关”为理由在多个章节重复铺陈完整理论。

### 5.3 书稿不是 canonical 文档

- 书稿负责经验入口、问题推进和生成哲学表达；
- bridge 负责精确关系、条件、失败分支和跨尺度比较；
- canonical 负责稳定定义、公理、判据与方程；
- 书稿不得堆入未经消化的符号或审计表；
- canonical 表达不得直接复制成书稿语气。

### 5.4 不提前封闭候选术语

以下术语在本轮初始阶段均为候选：

- 协调性关闭 / coordinated closure
- 参与式退让 / participatory yielding
- 选择代理层 / selection proxy layer
- 阴影承载的生成性 / shadow-bearing generativity
- 代理自主化 / proxy autonomization
- 代理反转 / proxy inversion

执行者可以比较、压缩或淘汰这些名称，但不得在没有裁决记录时把它们写成已冻结术语。

---

## 6. 分阶段施工路线

## Phase A：最新版差异审计

### 目标

建立当前书稿、Core/Core_Law、Neuroscience 与本轮候选机制之间的覆盖矩阵。

### 产物

建议新建：

`Operations/SRT_CROSS_SCALE_GENERATIVE_EMERGENCE_AUDIT_2026-07-12.md`

至少包含：

- 文件路径与当前 SHA；
- 当前 claim_mode / authority_level；
- 已有覆盖；
- 缺口；
- 冲突；
- 重复风险；
- 主落点 / 备选落点 / 禁止落点；
- 是否需要 canonical amendment；
- 是否需要外部文献核验。

### Gate A

没有完成覆盖矩阵，不得进入正文 patch。

---

## Phase B：来源直觉留痕

### 新建文件

`01_Source_Intuition/SRT_CROSS_SCALE_SELECTION_PROXY_TRACE_2026-07-12.md`

### 必须包含

1. 原始问题：为什么组成和局部机制不自动等于宏观属性生成解释；
2. 作者直觉链：
   - 个体减少部分独立可选择性；
   - 合作强化部分过程、压低其他过程；
   - 被压低方向没有消失；
   - 侧抑制提供自下而上前景生成的原型；
   - 整体是对这些退让选择形成的代理；
3. 作者原始直觉与 Agent 推演严格分栏；
4. 候选命题、反例、失败条件和未决问题；
5. 明确：`canonical: false`、`claim_mode: source_intuition`；
6. 回链本计划、Q06/Q10/Q19/Q23、Reference Scaling、Collective Selection；
7. 不得把整理者新增术语伪写成作者早已明确提出。

### Gate B

Source trace 通过 provenance 审计后，才可将候选机制压入 bridge。

---

## Phase C：跨尺度 bridge 硬化

### 新建文件

`03_Bridges/SRT_Cross_Scale_Selection_Proxy_Bridge_2026-07-12.md`

若当前仓库 bridge 目录命名或索引规则已变化，先由 `_SRT_INDEX.md` 解析目标目录；不得自行创建平行 bridge 体系。

### 必须包含

#### C1. 与还原解释的边界比较

- 承认组成与机制分析；
- 定位 SRT 增量为生成操作而非反科学口号；
- 区分 dependence、realization、aggregation、organization、emergence 和 subject formation；
- 明确本轮不声称解决全部强涌现问题。

#### C2. 操作链

```text
局部差异
→ 相互促进 / 竞争性抑制
→ 参与式退让
→ 协调性关闭
→ 共同前景 + 残余场
→ 历史写回 / L2 背景化
→ 选择代理层
→ 宏观自由度与向下约束
→ 可选：高阶 ISP 闭包
```

#### C3. 侧抑制接口

- 说明其结构启发；
- 说明跨尺度非同一性；
- 登记可证伪或可区分的替代机制；
- 回链 neuroscience claim-status；
- 不以神经类比代替一般机制论证。

#### C4. 阴影与残余因果性

- 区分阴影、张力、后续摩擦和未完成选择；
- 解释残余场如何参与边界、敏感性和重选；
- 说明“遮蔽不是删除”的跨尺度边界；
- 避免泛心论或普遍心理化。

#### C5. 代理层与 ISP

- 代理结构可以不是主体；
- 代理层形成自身维护循环后可能自主化；
- 登记 principal-agent inversion；
- 与 Collective Selection 现有判据对齐。

#### C6. 健康与病理分叉

```text
生成性代理：降低重复协调摩擦，并返还有效选择能力
替代性代理：绕过能力形成，使关键判断不再沉积
支配性代理：为维持自身而锁死重选、遮蔽来源、外包后果
```

#### C7. 最低生成判据与失败分支

审查第 3 节全部条件，不得只列正例。

### Gate C

Bridge 必须经过：

- canonical conflict audit；
- symbol collision audit；
- book terminology audit；
- neuroscience overclaim audit；
- 至少一轮反例压力测试。

未过 Gate C，不得把候选机制写成书稿的确定性理论结论。

---

## Phase D：OPEN_TENSIONS 登记

### 修改文件

`Core/SRT_OPEN_TENSIONS.md`

### 至少登记

1. 选择代理层是跨尺度涌现必要条件，还是一类常见机制；
2. 协调性关闭怎样去拟人化；
3. 局部独立可选择性减少与宏观有效选择增加如何比较，是否同量纲；
4. 残余因果相关性怎样操作化；
5. 短暂同步与可继承代理层怎样区分；
6. 高阶代理何时获得自己的 d-value 或关切位；
7. 代理服务的是所有构成单元、部分单元，还是嵌套系统；
8. 生物系统中部分细胞被牺牲时，如何定义“返还选择能力”；
9. 侧抑制类机制是否只是众多实现之一；
10. 重新选择能力是否是生成性涌现的必要条件，还是仅为健康性条件。

不得在 OPEN_TENSIONS 中伪装成已解决定理。

---

## Phase E：书稿主线回写

原则：以 `Drafts_26Q/` 当前版本局部增补，不重写全章，不复活旧 52 章结构。

### E1. Q10《秩序背景化》——主理论锚

职责：解释整体和代理层怎样从下层协调中生成。

建议新增：

- 对“复杂度增加并不自动说明新属性生成”的简洁追问；
- 秩序不仅是倾斜地形，也是重复协调选择的代理层；
- 先有局部相互让路和历史沉积，后有整体向下约束；
- 局部可能性的协调性关闭如何形成共同前景；
- 关闭方向未被删除，而作为张力和后续摩擦参与地形；
- 宏观层新增的是有效行动自由度，不是神秘实体。

职责边界：

- 不在 Q10 展开完整制度正当性，交给 Q23；
- 不在 Q10 展开完整代理病理，交给 Q19；
- 不把全部侧抑制神经细节塞入正文；
- 不把高阶 ISP 判据写成书稿主线表格。

候选主句：

> 整体不是先站在上面管理个体。更常见的顺序恰恰相反：局部单元先在反复协调中彼此让路，把一类不必每次重算的选择沉进共同地形；当这片地形开始替后来者处理选择，它才成为一个代理层。

### E2. Q06《排除与阴影》——残余场接口

职责：说明高尺度前景并非只由被强化部分构成。

建议新增：

- 共同前景与受抑制场共同形成边界；
- 侧抑制作为结构显影，而不是跨尺度同一机制；
- 被压低方向通过张力、后续摩擦和敏感性参与生成；
- 只有满足表征门槛时才使用“阴影”；
- 保持成功选择 / 失败选择 / 未完成选择三分。

职责边界：

- 不把非人系统全面心理化；
- 不把未完成选择误写成已形成边界的失败选择；
- 不在本章承担完整涌现理论。

### E3. Q19《脚手架与牢笼》——代理病理

职责：解释选择代理为何有价值，以及怎样发生代理反转。

建议新增：

- 脚手架是选择代理的一种形态；
- 健康代理接管重复机械协调，释放关键判断带宽；
- 对象级选择委托与元选择保留的区分；
- 代理范围扩张、能力萎缩、后果截断、退出成本上升；
- 生成性代理 → 替代性代理 → 支配性代理的病理路径。

必须与当前三刀判据对齐：

- 能力是否沉积；
- 离开代价是否可支付；
- 后果是否回流。

不得另造与现有判据平行且重复的一套“代理五原则”。

### E4. Q23《共同体》——社会代理推广

职责：把现有社会层 Proxy Structure 回链到一般跨尺度生成机制。

建议新增：

- 法律、市场、行政和代表结构不是凭空发明，而是重复协调选择沉积后的社会代理；
- “把选择交出去，不等于把回流交出去”继续作为中心句；
- 有范围、有期限、能撤销、能审查继续作为委托底线；
- 代理结构不是集体意志，也不自动构成集体 ISP；
- 社会代理的健康性取决于后果能否回到受影响位置并重新改写地形。

不得让一般跨尺度机制削弱 Q23 当前反利维坦、反沙粒加总的主线。

### E5. Q28 或跨域附录——还原主义与涌现回链

先由差异审计决定落点：

- 若正文需要哲学收束，在 Q28 增加少量回链；
- 若需要明确比较传统问题，优先写入 `附录_跨域难题_重述而非解决.md`；
- 不得在两个位置重复完整论证。

建议处理：

- SRT 不宣称以一个比喻解决全部涌现难题；
- 它重述问题为可选择性的尺度迁移和协调性关闭；
- 指明经验研究需要寻找哪些可区分指标；
- 说明这是生成机制候选，不是“强涌现已被证明”的结论。

### E6. 同步文件

书稿 patch 完成后同步：

- `01_Source_Intuition/BOOK/BOOK_VERSION_LOG.md`
- 必要时当前术语表
- source-intuition index
- bridge index / machine index 中的对应入口
- 不得让 `_SRT_INDEX.md` 继续保留与当前落点冲突的书稿描述

### Gate E

书稿回写必须通过：

- 当前章节版本检查；
- 前后章问题链检查；
- 术语降噪检查；
- 重复内容检查；
- 导出与 outline 检查；
- governance preflight。

---

## Phase F：Neuroscience 接口裁决

### 任务

对当前 neural mechanisms 主文件做只读审计，判断是否已有：

- lateral inhibition；
- divisive normalization；
- competitive inhibition；
- winner-take-all；
- recurrent stabilization；
- predictive/error competition；
- residual/subthreshold activation；
- reactivation and reselection。

### 裁决出口

- **F-A 不回写**：现有内容已充分，bridge 只做回链；
- **F-B bridge 回链**：在 neuroscience hardening/index 中增加边界说明；
- **F-C 谨慎正文补充**：仅当现有主文件确有明显接口缺口，并通过 claim-status 审计；
- **禁止出口**：直接将侧抑制升级为 SRT 跨尺度涌现的 canonical 神经机制。

---

## Phase G：Core / Core_Law 集成裁决

### G1. Reference Scaling

审查：

- 现有跨尺度共轭是否只描述尺度对应，而缺少高层选择单元的生成过程；
- 协调性关闭是否可作为 scaling bridge，而不是新公理；
- 是否只需增加非 canonical hardening note 或回链。

### G2. Collective Selection

审查：

- 现有文件定义了高阶 ISP 条件，但是否缺少代理层生成前史；
- 是否需要增加“代理结构不等于集体 ISP”的显式回链；
- 是否会改变 shared L2、consequence matrix 或 collective reselection 的现有定义。

### G3. Tower Hardening

审查：

- “参与式退让—代理形成—向下约束—重新响应”是否适合放入 tower/nested hardening；
- 上层不锁死下层、下层不捕获上层的条件能否吸收代理反转问题；
- 只做 late-stage hardening，不提升其权威层级。

### Gate G

若新增只属于解释、bridge 或 hardening，则不得修改 canonical anchor。只有发现现有 canonical 存在定义缺口或内部冲突，才进入 Phase H。

---

## Phase H：Canonical amendment gate

canonical 不是永久不可修改，但本任务不得自动进入 canonical 编辑。

### H1. 进入条件

至少满足：

1. source trace 已完成；
2. bridge 已完成反例压力测试；
3. OPEN_TENSIONS 已登记；
4. 书稿回写不依赖未定义术语；
5. Core/Core_Law 差异审计显示现有 canonical 确有缺口；
6. 已明确目标 canonical source；
7. 已完成 symbol table、registry、主文和 compact core 的影响矩阵；
8. 作者明确授权启动 C 类高风险编辑。

### H2. 可能裁决

- **H-A 不改 canonical**：本轮只是解释增强；
- **H-B 增加 bridge hypothesis**：补充生成机制候选，但不改核心定义；
- **H-C canonical clarification**：增加边界说明，不改变语义；
- **H-D canonical amendment**：修改定义、判据或方程，必须单独 PR、单独审查、单独授权。

### H3. 明确禁止

- 在书稿 PR 中夹带 canonical 修改；
- 用 bridge 文件替代 canonical；
- 未经作者授权给候选命题定理编号；
- 把“协调性关闭”直接加入 symbol table；
- 把神经侧抑制写成跨尺度普适定律；
- 把“整体帮助个体选择”写成所有构成单元都获益的普遍规范事实。

---

## 7. 建议 PR 切分

为降低跨层污染，建议至少拆为三个 PR。

### PR 1：来源与 bridge

包含：

- source-intuition trace；
- cross-scale bridge；
- OPEN_TENSIONS；
- 必要索引和治理留痕。

不包含：

- 书稿正文；
- canonical 修改。

### PR 2：书稿主线

包含：

- Q06、Q10、Q19、Q23；
- 经审计决定的 Q28 或跨域附录；
- BOOK_VERSION_LOG、术语与导出同步。

不包含：

- canonical 修改；
- 未经裁决的 Neuroscience 主文件修改。

### PR 3：Core / canonical 裁决

根据 Gate G/H 结果：

- 可能只做 bridge/hardening 回链；
- 也可能结论为“不需要修改”；
- 若确需 canonical amendment，必须单独高风险 PR。

---

## 8. Codex / Claude 协作建议

本文件对 Agent 中立，但建议采用交叉分工。

### 8.1 Claude 优先任务

- 对传统还原主义比较做反稻草人审查；
- 检查候选机制是否偷换目的论；
- 压力测试“整体服务个体”的例外；
- 审查书稿段落的哲学力度、可读性和重复；
- 提出反例，不直接越权改 canonical。

### 8.2 Codex 优先任务

- 获取当前 SHA 和差异矩阵；
- 创建精确 patch；
- 同步索引、frontmatter、版本日志和回链；
- 运行 governance preflight、outline/export 检查；
- 保证每个 PR 的文件边界与任务边界一致。

### 8.3 交叉审查

- Claude 审查 Codex 的概念与书稿改动；
- Codex 检查 Claude 建议是否与当前文件、路径、符号和治理规则一致；
- 任一 Agent 不得以自己的输出作为唯一证据宣告计划完成。

---

## 9. 验收标准

本任务只有在以下条件全部满足时才可关闭。

### 9.1 理论完整性

- 还原主义生成缺口被明确而非稻草人式地表述；
- 协调性关闭与参与式退让被区分；
- 侧抑制被限定为机制原型，而非普适同一机制；
- 被关闭方向的残余因果相关性被保留；
- 选择代理层与高阶 ISP 被区分；
- 生成性、替代性和支配性代理被区分；
- 失败分支和反例被登记。

### 9.2 书稿完整性

- Q10 承担生成机制主锚；
- Q06 只承担残余场/阴影接口；
- Q19 承担代理病理；
- Q23 承担社会代理和后果回流；
- Q28 或附录只承担必要收束；
- 没有大段重复；
- 没有把书稿写成术语手册或 canonical 文档。

### 9.3 仓库治理

- 所有写入以当前主分支最新版为母版；
- 未使用 archive 作为初稿母版；
- 每个新增文件 frontmatter 完整；
- 索引与回链同步；
- BOOK_VERSION_LOG 同步；
- governance preflight 通过；
- 相关 PR 明确声明未修改或为何修改 canonical。

### 9.4 Canonical 安全

- 未经 Gate H 和作者授权，没有 canonical 定义变化；
- 候选术语没有被静默升级；
- bridge、book、operations 文件没有取代 definition authority；
- 若最终不修改 canonical，留下明确的 no-amendment decision note。

---

## 10. 执行状态清单

- [x] 前置治理：最新版优先与归档降权（PR #658）
- [x] 将 Issue #657 正文与补充整合成本文件
- [x] Phase A：最新版差异审计 → `SRT_CROSS_SCALE_GENERATIVE_EMERGENCE_AUDIT_2026-07-12.md`（Gate A 通过；PR #660 复审后三态化修订）
- [x] Phase B：source-intuition trace → `01_Source_Intuition/SRT_CROSS_SCALE_SELECTION_PROXY_TRACE_2026-07-12.md`（作者原始直觉 / LLM 推演 / 评审反馈与实施决定〔待作者确认〕 严格分栏；已登记 `01_Source_Intuition/INDEX.md`）
- [x] Phase C：cross-scale bridge — 裁决**不新建平行 bridge**；既有 `Core_21c` emergence-hygiene + `Reference_Scaling` PCC 高度重叠。注意：候选机制与既有对象是**相邻·不可等同**，非别名
- [x] Phase D：OPEN_TENSIONS — 加“Open Tension (2026-07-12)”：登记候选映射（非别名）+ **一条新未决项**（局部 optionality↓→协调性关闭→宏观有效选择↑ 的可区分形式化）；不宣告无新张力
- [x] Phase E：书稿回写 — 收缩版：Q10 章末注九（去拟人化的多单元→代理结构接缝，v28）+ Q23 注七候选跨尺度回链（v24，声明不下推社会规范）；Q06/Q19/Q28 不改；BOOK_VERSION_LOG 已同步
- [x] Phase F：Neuroscience 接口裁决 → **F-A 不回写**（侧抑制映射已在 `Core_21c` line 169）
- [x] Phase G：Core/Core_Law 集成裁决 → G1/G2/G3 **不改动对应文件**（已有构件无需动；相邻未覆盖项登记为 open tension）
- [x] Phase H：canonical amendment decision → **H-A 不改 canonical**（理由=候选未成熟非已覆盖；本审计+source trace+Open Tension 即 no-amendment decision note）
- [x] CI 验收：book outline / split freshness / registry / large-file 全 PASS；frontmatter 唯一 FAIL 属既有 `Papers/selective_resynchronization/` baseline 漂移，与本轮无关

---

## 11. 可直接交给 Agent 的启动指令

```text
请先遵循 AGENTS.md 的 fresh-session 和 book-writing hard guard。

本任务以
Operations/SRT_CROSS_SCALE_GENERATIVE_EMERGENCE_WRITEBACK_PLAN_2026-07-12.md
为唯一执行主文件。

先执行 Phase A，只做最新版差异审计，不直接改理论或书稿正文。

必须读取 BOOK_CURRENT_STATUS.md、BOOK_ACTIVE_MANIFEST.json，以及当前
Drafts_26Q 中的 Q06、Q10、Q19、Q23、Q28 和跨域附录。

Archive_52Chapter 与 Archive_Meta 只能在当前 primary 已读取后用于明确标注的历史比较，不得作为当前 patch 母版。

本轮完整问题链是：
传统还原主义的跨尺度生成解释缺口
→ 参与式退让
→ 协调性关闭
→ 侧抑制机制原型
→ 共同前景与残余场
→ L2 背景化
→ 选择代理层
→ 宏观行动能力
→ 向下约束
→ 生成性/替代性/支配性代理分叉
→ 高阶 ISP 的附加闭包条件。

输出 Phase A 覆盖矩阵、冲突审计、主/备/禁止落点以及分 PR 施工建议。
未经 Gate H 和作者明确授权，不得修改 canonical 定义、公理、判据、方程或 symbol table。
```

---

## 12. Provenance

本文件整合：

- GitHub Issue #657 的初始回写计划；
- Issue #657 中关于“还原主义生成缺口—协调性关闭—侧抑制原型”的补充；
- PR #658 暴露并修复的最新版检索治理问题；
- 2026-07-12 对话中形成的作者直觉与后续结构化分析。

Issue #657 继续承担讨论和实施追踪；本文件承担执行规范与验收标准。若二者出现不一致，以默认分支上本文件的最新版本为准，除非作者在 Issue 中明确作出新的覆盖裁决并同步回写本文件。
