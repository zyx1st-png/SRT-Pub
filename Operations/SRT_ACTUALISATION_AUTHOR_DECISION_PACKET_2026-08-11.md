---
id: SRT-ACTUALISATION-AUTHOR-DECISION-PACKET-20260811
type: framework
status: frozen
claim_mode: governance
updated: 2026-08-11
record_stage: author_decided_and_landed
author_decision: AM-A
decision_date: 2026-08-11
implementation_status: landed
layer: meta
epistemic_layer: os
canonical: false
related_files:
  - Core_Law/SRT_L0_Metaphysics.md
  - Core/SRT_Core_12a_Ontology_L0L1.md
  - Core/SRT_Core_13a_Operator_Basics.md
  - Core/SRT_Core_21_Minimal_Axioms.md
  - Core/SRT_Core_21b_Constitutive_Theorems.md
  - Core/SRT_OPEN_TENSIONS.md
  - 03_Bridges/SRT_Choice_Generation_Conditions_2026-08-04.md
  - 03_Bridges/SRT_Selection_Event_CompactCore.md
  - Operations/_SRT_REVIEW_QUEUE.md
---

# 作者裁决包：`L_0 -> L_1` Actualisation

## 裁决记录（2026-08-11）

作者选择：**AM-A — Primitive Kernel + Implementation Pluralism**。

实施结果：

- P0-01 明确承载 primitive actualisation kernel；没有新增第二个原语或符号；
- P0-04 从“等待机制填补的起源暴露点”改为 declared primitive boundary；
- `\hat G_\theta` 只承担该原始转化的形式角色，不再被写成自身的原因；
- Ax-L0-Bootstrap 保留旧编号和“无先在选择者／时间无前序性”边界，但删除 fixed-point、`argmin`、最陡下降必然实化与意识相变推论；
- `\kappa_0`、梯度、`\Psi_f` 与 payability 被限定为 enabling / admissibility constraints，不再充当 first actualisation 的充分原因；
- 物理、生命、认知与社会层的机制继续保持复数实现地位；稳定化、主体形成与意识不在本裁决中推进。

下文 §1–§4 保留裁决依据；AM-B / AM-C 只作为被否决备选的历史记录。

## 0. 文件角色

本文件只处理一个连接：

> 非对象化潜在受到结构性约束
> → 一个确定的 `L_1` 事件实际发生。

它不处理事件之后的稳定化、`L_2` 沉积、Stable ISP、主体形成或意识，也不引入新符号。作者裁决后，canonical 修改严格限于 AM-A 所需的 primitive / constraint / implementation 分层。

---

## 1. 当前 canonical 同时存在的两种地板

| 位置 | 当前主张 | 实际地位 |
|---|---|---|
| `Core/SRT_Core_21_Minimal_Axioms.md P0-01` | 选择先于存在，存在是选择的像 | 把选择登记为 P0 primitive |
| 同文件 `P0-04 Exposure Note` | well-formed operator 不会推出最初的 selectability；起源问题未解 | 明确开放暴露点 |
| `Core/SRT_Core_12a_Ontology_L0L1.md Ax-L0-Bootstrap` | fixed point、最陡下降与最低摩擦已经“正式消解”第一算子问题 | 声称给出普遍结构性推导 |
| 同文件 `Ax-L1-01`；`Core/SRT_Core_13a Ax-Op-01` | `L_1 = \hat G_\theta[L_0]` | 命名输入、输出和映射，不说明映射为何发生 |
| `Core/SRT_Core_13a Ax-Op-03 / 05` | 归一化与闭包是实现候选／稳定化条件 | 以算子、候选状态或迭代已经可用为前提 |
| `03_Bridges` 的 CG-0—CG-4 | 给出选择候选与事件成立的跨域审计面 | P2–P3 判别框架，不是 P0 起源推导 |

因此仓库目前一面说“这是 primitive / origin open”，一面又说“fixed point 已经正式解决”。这不是措辞差异，而是架构冲突。

---

## 2. 本次地板构建报告

### 2.1 处理对象

只检验：

> `L_0` 的非平坦结构、梯度、代价差异或最低非中立性
> ⇒ 一个确定 `L_1` 事件必然实际化。

### 2.2 负担标注

| 判断句 | 标签 | 负担结论 |
|---|---|---|
| “`L_0` 不是完全平坦、完全中性的。” | **S** | 提供差异条件；不自动提供事件发生、唯一结果或终止条件 |
| “某些方向摩擦更低、权重更高或更可支付。” | **S** | 给出序关系或准入条件；不等于其中一个方向已经实际发生 |
| “存在 `\hat G^* = \arg\min ...`。” | **S + A** | 预设可比较的算子空间、定义良好的 `\Psi_f`、极小值存在；若要唯一，还需唯一性条件 |
| “极小值的存在就是算子的实际化。” | **A** | 从数学存在／最优性跳到本体事件发生；缺少 realization bridge |
| “`L_1 = \hat G_\theta[L_0]`。” | **D** | 定义输入—输出关系；不能反过来解释 `\hat G_\theta` 如何获得事件效力 |
| “确定化创造信息并留下不可逆痕迹。” | **S** | 描述事件后果；不能作为事件发生的原因，否则以结果解释自身 |
| “CG-0—CG-4 均达标。” | **O** | 可支持某事件的有界判定；不回答最初 selectability 从何而来 |

### 2.3 裸句测试

去掉“投影、打捞、落地、坍缩、照明”等图像，当前能安全保留的裸句是：

> 潜在条件并非完全等价；有限位置、历史约束与代价结构会限制哪些差异可获得事件效力。若一个确定化事件发生，它会产生此前未作为确定事实存在的区别，并改变后续可达结构。

裸句仍缺一项：**为什么“受约束的差异”会跨成“已有一个确定事件”，而不是继续停留为不等价的倾向、概率分布、并行分支、振荡或无终止演化。**

因此“最陡路径必然实化”和“算子落地”目前承担了缺失桥梁。

### 2.4 连接检验

Ax-L0-Bootstrap 若要成为非循环推导，至少需要补齐：

1. **S：定义域** — `\mathcal F` 所作用的算子候选从何而来，且不能先以“选择算子”定义它们；
2. **S：比较结构** — `\Psi_f` 在第一 actualisation 之前如何定义，尤其不能借用已成形主体、历史或 `L_2`；
3. **S：存在性** — fixed point / argmin 确实存在；
4. **S：唯一性或分支规则** — 多个同值极小、连续谷底、无穷逼近和无极小情形如何处理；
5. **A：实现桥** — 数学上的极小值或不动点为何等于一个确定事件实际发生；
6. **S：非循环性** — 上述任一条件不得用 `\hat G`、selection、anchoring 或 manifestation 的同义词偷偷重写待解释项。

当前六项均未闭合。尤其第 5 项不能由公式记号免费取得。

### 2.5 反例施压

1. **非平坦但不终止。** 梯度流可以无限逼近极小值而从不在有限阶段给出排他性确定事件。
2. **多极小值。** 多个等价极小值仍需要额外的破缺／实现规则；`argmin` 只返回集合，不返回“这一次发生了哪个”。
3. **约束分布。** 归一化或 Softmax 给出相对权重，但权重分布不是单个 `L_1` 事实。
4. **稳定不是发生。** Lyapunov 收敛、闭包或谱隙可以解释已运行过程如何稳定，不能解释过程怎样首次获得事件效力。
5. **后果不是起因。** 信息创造、不可逆痕迹和历史写回区分已经发生的事件；以它们说明事件为何发生会倒置解释方向。

删除测试：删掉 Ax-L0-Bootstrap 的 fixed-point “正式消解”段，P0-01 仍可作为 primitive 维持 SRT 主链；删掉 P0-01 的 primitive 地位，则 fixed-point 段也不能独立重建 actualisation，因为它预设了算子候选及其实现桥。当前两套地板互相借力，却没有任何一套单独闭合。

### 2.6 判决

**🔴 软连接。**

`\hat G_\theta : L_0 -> L_1` 是形式角色；梯度、非中立性、摩擦与 payability 是约束或准入条件；信息创造和写回是后果；CG-0—CG-4 是事件判据。当前没有一个非循环的普遍机制把这些部分连接成“一个确定事件实际发生”。

---

## 3. 作者选项

### AM-A — Primitive Kernel + Implementation Pluralism（推荐）

裁决内容：

- 明确把最小 actualisation kernel 保留为 P0 primitive：一个非等价潜在差异获得确定的事件效力；SRT 不再声称从更早的非选择结构推出这一步；
- `\hat G_\theta` 只形式化该 primitive 的角色与受约束方式，不被称为它自身的原因；
- `L_0` 非中立性、位置、历史、`\Psi_f` 与 payability 是 enabling / admissibility conditions，不是充分原因；
- 确定区别、不可逆痕迹与未来可达性改变是 postconditions，不倒写为起因；
- 物理、生命、认知和社会层可有不同实现机制；任何实现只能证明“实例化这个 kernel”，不能反向定义 P0；
- Ax-L0-Bootstrap 的“正式消解”、fixed-point 必然实化和第一算子推导降为候选或改写为边界说明：不需要预先存在的 chooser，但 selectability 不因此被推导。

影响：最贴合现有 P0-01，改动最小，也最诚实。代价是承认 actualisation 是 SRT 的本体论地板，而不是 SRT 已解释掉的对象。

### AM-B — Universal Structural Derivation

裁决内容：

- 保留“actualisation 可由 `L_0` 结构普遍推出”的目标；
- 在 canonical 升格前，先补齐 §2.4 的定义域、比较结构、存在性、唯一性／分支规则、实现桥与非循环证明；
- 明确哪些额外命题是新公设，不能把它们包装成 Ax-L0-03 或 `\kappa_0 > 0` 的免费推论；
- P0-04 在证明完成前继续保持开放，Ax-L0-Bootstrap 暂不得称“正式消解”。

影响：若成功，SRT 会得到更强的生成论；但证明负担最高，且可能需要重写 P0-01 的 primitive 身份。

### AM-C — Subtractive Reconstruction / Selection De-priming

裁决内容：

- 不再寻找一个额外 actualisation primitive；
- 执行 `Core/SRT_OPEN_TENSIONS.md §13` 已登记的 deletion test，用非对称约束、可达集改变、代价、不可逆写回与后果返回重建现有工作；
- 只有当限定 refit budget 下仍出现不可替代残余，才保留 selection primitive；若无残余，则降级 P0-01 并把 `L_0 -> L_1` 改写为结构分类而非本体原语。

影响：可最大限度减少原语，但会触及 SRT 的 selection-first 身份，是三项中架构改动最大的一项。

---

## 4. 推荐与裁决前护栏

**推荐 AM-A。** 理由是当前 claim ladder 已把 selection 放在 P0，而 fixed-point 段没有完成它声称完成的推导。AM-A 不用一个假机制掩盖 primitive，也不阻止各领域继续寻找可检验实现。

以下为裁决前护栏，现作为历史执行边界保留：

- 以 P0-04 的“origin unresolved”作为当前控制性护栏；
- Ax-L0-Bootstrap 不得被引用为已经解决第一 actualisation；
- fixed point、argmin、最陡下降、`\kappa_0`、归一化、闭包、谱隙和 CG-0—CG-4 均不得单独称为 universal actualisation mechanism；
- 不新增 actualisation 符号，不推进 stabilization、subject 或 consciousness；
- 不修改 canonical，只登记冲突与决策面。

---

## 5. 最小裁决格式

```text
Actualisation = AM-A
```

或：

```text
Actualisation = AM-B
```

```text
Actualisation = AM-C
```

---

## 6. 实施后的持续边界

- **已执行 AM-A**：actualisation 是既有 selection primitive 的最小内核，不是另增一个并列原语。
- **未执行 AM-B**：fixed point、最陡下降、非平坦性或最低摩擦不构成 universal derivation。
- **未执行 AM-C**：P0-01 未被删除或降级；`Core/SRT_OPEN_TENSIONS.md §13` 的 deletion test 仍是独立的可减性研究，不反向取消本次作者裁决。
- **持续开放**：各领域怎样实例化该 kernel、选择事件阈值怎样操作化、selector 如何个体化，以及稳定化／主体／意识问题。
- **持续禁止**：把 domain mechanism 反向定义为 P0，把数学存在等同事件发生，或用事件后果解释事件为何发生。
