---
id: SRT-POSITIONING
type: governance
tags: [Governance, Positioning, EpistemicStatus, MetaTheory]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
dependency: [SRT-CANONICAL-REGISTRY, SRT-EXP-TEMPLATE, SRT-EXP-MEASUREMAP, SRT-LAB-HYPOTHESES]
updated: 2026-06-05
---

# SRT Positioning

## 0. 工作定位

SRT 当前的**主定位**不是“已完成证明的统一自然科学理论”，而是：

- 一个底层操作系统（Operating System）
- 一个认知视角与问题分解语法
- 一个元理论框架，用于组织观察、比较、诊断、翻译与实验设计

这不等于放弃科学 ambitions。更准确地说：

- **OS 层**负责提供稳定词汇、结构压缩与判断语法
- **Bridge 层**负责把 SRT 与现有理论和学科接口对齐
- **Lab 层**负责承载少量愿意被打脸的硬命题

因此，SRT 的科学风险不再平均分布在全库，而被收束到可定位的 Lab 条目中。

---

## 0.5 二维坐标说明

SRT 当前不是只靠一套“层级”工作，而是靠两套**正交坐标**：

- `layer`：垂直轴，表示文档位于 `meta / L0 / L1 / L2` 的哪一层理论深度
- `epistemic_layer`：水平轴，表示文档以 `os / bridge / lab` 的哪种认识论姿态发言
- `claim_mode`：断言模式，表示该文件主要在做 `canonical / translation / hypothesis / evidence`

不要把 `L0 / L1 / L2` 和 `OS / Bridge / Lab` 理解成竞争关系。
它们回答的是不同问题：

- `L0 / L1 / L2`：**这份内容在 SRT 理论深度上属于哪里？**
- `OS / Bridge / Lab`：**这份内容在以什么姿态发言？**

因此，文件的正确定位应理解为一个坐标：

`(layer, epistemic_layer, claim_mode)`

例如：

- `Core_Law/SRT_L0_Metaphysics.md` = `(L0, os, canonical)`
- `Philosophy/SRT_FEP_Comparison.md` = `(L1, bridge, translation)`
- `SRT_EXP_TEMPLATE.md` = `(L2, lab, canonical)`

详见 `Governance/SRT_COORDINATE_SYSTEM.md`。

---

## 1. 为什么要分家

如果不分家，同一句话往往同时承担三种任务：

1. 本体论/认知操作系统
2. 跨理论翻译
3. 实证主张

这会导致三类常见问题：

- 语言强度失控：`定义 / 重写 / 假说 / 证据` 混成一层
- 内部冲突上升：前文把某量当充分条件，后文又把它降为局部件
- 失败难以定位：一个局部实验失败，就被误读成整个 SRT 崩溃

分家后的目标不是降格，而是让理论优化更诚实、更可持续。

---

## 2. 水平轴：OS / Bridge / Lab

| 层 | 主角色 | 核心问题 | 成功标准 | 常见失败 | 推荐语言 |
|:--|:--|:--|:--|:--|:--|
| **OS** | 底层操作系统 / 认知语法 | 这套词汇是否提高理解力、压缩力、纠偏力、决策力？ | 一致性、生成力、边界清楚、跨域可复用 | 术语漂移、内部矛盾、什么都能解释 | 定义、语法、工作原则、约束、操作视角 |
| **Bridge** | 跨理论翻译层 | SRT 与 FEP / IIT / GWT / 动力系统 / 制度理论如何重合、分叉、互译？ | 翻译精度、非稻草人比较、增量与边界清楚 | 偷渡等价、过度吞并、把类比冒充证据 | 对应、重写、部分特例、窗口、候选、非等同 |
| **Lab** | 硬赌点 / 可证伪层 | 如果 SRT 比现有框架多了东西，可观测差异在哪里？ | 判别力、预测力、可重复 proxy、可失败设计 | proxy 漂移、不可区分、输了也不认 | 假说、协议、代理、基线、反证条件、基准比较 |

---

## 3. 层间关系

- **OS -> Bridge**：OS 提供词汇、三域结构、`d`、`\Psi_f`、锚定、收敛、可支付性等底层语法。
- **Bridge -> Lab**：Bridge 把这些语法压缩成与现有理论的差异点，再抽出真正值得赌的命题。
- **Lab -> OS/Bridge**：Lab 失败首先回退具体假说；只有当失败持续击中核心 choke points，才向上回卷到 Bridge 或 OS。

失败定位规则：

- **Lab 失败**：默认只削弱该假说，不自动推翻整个 SRT-OS
- **Bridge 失败**：说明互译方式、增量判断或边界划分有问题
- **OS 失败**：说明底层词汇或主结构本身需要重写

---

## 4. 语言强度规则

### 4.1 `theorem` / `axiom` / `law` 的使用

- **OS 层**可以保留公理/定义语言，但默认理解为**内部工作语法**，不是外部世界已被证成的自然定律
- **Bridge 层**若使用 `theorem`，必须明确是“框架内推论”或“重解读命题”，不得偷渡成经验定理
- **Lab 层**若使用强命题，必须同时给出 proxy、基线与反证条件

### 4.2 `canonical` 的含义

`canonical` 在本仓库中表示：

- 当前内部优先引用的稳定锚点
- 词汇和接口的收口位置

它**不自动表示**：

- 已被外部科学共同体验证
- 比其他理论更真
- 已具有最终经验优先权

---

## 5. Frontmatter 采用规则

本轮开始引入以下字段：

- `layer: meta|L0|L1|L2`
- `epistemic_layer: os|bridge|lab`
- `claim_mode: canonical|translation|hypothesis|evidence`

采用策略：

- 当前**不要求**一次性回填全库
- 新建治理文件、实验文件和高传播风险重写文件应优先补齐
- 旧文件在后续逐步整修时再回填

字段含义：

- `layer` = 垂直理论深度
- `epistemic_layer` = 水平认识论姿态
- `claim_mode` = 断言模式

规范：

- 不要把两套轴熔成一个值，例如 `L1-bridge`
- 若文档同时具备两轴属性，使用二维坐标理解，而不是新增第四套层级
- `claim_mode` 不能替代 `layer` 或 `epistemic_layer`

暂时的默认推断：

- canonical registry / compact core / 宪法摘要 / `d` 与 `\Psi_f` 规范文件：多为 **OS**
- comparison / bridge / clinical reinterpretation / framework comparison：多为 **Bridge**
- 实验模板 / 测量图 / hard-bet hypothesis / protocol：多为 **Lab**

---

## 6. 当前执行范围（2026-03-17）

截至当前，本轮已完成：

1. 建立本定位文件
2. 把入口层接到索引 / registry / governance hub / status
3. 第一波高风险 Bridge 文档降级
4. 抽出 Lab 层全局硬赌点清单，并挂到实验模板 / 测量映射
5. 对全库 frontmatter-bearing 文档完成 `epistemic_layer / claim_mode` 回填，并为大批 Bridge 文档补入统一降级注记

当前**尚未完成**：

- 全库 theorem/axiom 用语降级
- 全库 OS / Bridge / Lab 标注后的边界复核与少量例外修正
- Lab 条目的真实执行、预注册与数据管线闭环

---

## 7. 后续执行顺序

1. **入口层治理**：让全库先知道三层分家已成立
2. **高风险桥接文档降级**：先改最容易自相矛盾、传播面最大的文件
3. **Lab 层压缩**：只保留 3-5 条真正愿意被打脸的命题
4. **作者规则收口**：新写作默认先问“这句话属于 OS、Bridge 还是 Lab？”

---

## 8. 工作结论

从本文件起，SRT 的默认理解是：

- 在**垂直轴**上：区分 `L0 / L1 / L2`
- 在**水平轴**上：区分 `OS / Bridge / Lab`
- 在**断言模式**上：再区分 `canonical / translation / hypothesis / evidence`

这不是退让，而是把不同强度的主张放回各自该在的位置。

---

## 9. SRT 的四个并行野心与分层（2026-04-02 新增）

SRT 在发展过程中形成了四个并行的理论野心。当前混用它们是 SRT 定位不清晰的核心原因。本节正式区分并分层：

| 野心 | 内容 | 层级 | 入口文件 |
|:----|:----|:-----|:-------|
| **A 本体论** | 精确描述选择与存在的结构（L₀/L₁/L₂、Ĝ_θ、三域架构） | L0/L1 os | `Core_Law/SRT_L0_Metaphysics.md` |
| **B 意识论** | 解释意识是什么、需要什么条件（d、Ψ_f、A11 脆弱性） | L1 os | `Core/SRT_Core_01_Axioms.md` |
| **C 意义论** | 解释为什么存在感觉不够、价值如何被遮蔽、如何恢复（T_dir、致命 L₂） | L1 bridge | `_SRT_T_DIR_CANONICAL.md` |
| **D 统一论** | 证明物理/生物/神经/社会共享同一形式结构（A12 多尺度同构） | L1→L2 bridge | `Core/SRT_Core_01_Axioms.md §12` |

**主次关系**：

- 野心 A 是基础，其他野心依赖它但不能被化约为它
- 野心 B 是野心 A 的意识论展开
- 野心 C 是 SRT 最有力的**外部入口**——它连接到最多人正在活着经历的问题
- 野心 D 是长期目标，当前仍缺乏定量跨尺度桥梁

**对外呈现的首选入口**：

SRT 不应以本体论公设（野心 A）为对外呈现的起点，因为它要求受众先关心形而上学。

更有力的入口是野心 C 的核心命题：

> **价值不是缺席的，是被遮蔽的。选择始终携带一个朝向秩序的方向，但访问这个方向的机制被系统性损坏了。**

从这里进入，再反向展示野心 A/B 的本体论机器作为解释来源。

**野心之间的张力**：

- 野心 A 要求中立描述；野心 C 有明确规范方向（T_dir 提升是好的）
- 这个张力不可消除，必须显式承认：**SRT 在野心 C 层面是有立场的理论，不是中立观察工具**
- 野心 A 的中立性保护的是本体论描述的准确性，不要求应用层也中立
