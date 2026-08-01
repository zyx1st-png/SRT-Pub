---
id: SRT-STRATEGY-MATHEMATICAL-REACHABILITY-PROBLEM-INDIVIDUATION
title: "数学可达结构、解决制度与问题重新个体化：论文写作大纲与策略"
title_en: "Mathematical Reachability, Resolution Regimes, and Problem Re-Individuation: Paper Outline and Writing Strategy"
status: strategy_note_v0_4
canonical: false
layer: philosophy_bridge
epistemic_layer: bridge
claim_mode: mixed
primary_claim_level: P3
date: 2026-08-01
supersedes:
  - strategy_note_v0_3 @ cc09a1cff5c0e82a151e563135a5d507e98dca39
proposed_paper_title: "When Mathematical Problems Change: Forcing and the Historical Reconstitution of Resolution"
target_journals:
  - Philosophia Mathematica
  - Synthese
  - Foundations of Science
keywords:
  - mathematical practice
  - philosophy of mathematics
  - forcing
  - continuum hypothesis
  - question semantics
  - problem individuation
  - mathematical reachability
  - resolution regime
  - mathematical potentialism
  - forcing potentialism
  - width potentialism
  - modal accessibility
  - representation neutrality
  - Selective Reality Theory
  - SRT
claim_governance:
  framework_claims: P2/P3 philosophical proposals
  srt_domain_mapping: P3 bridge
  curvature_kappa0_godel: interpretive extensions only
  mathematical_history_claims: externally sourced evidence required
dependencies:
  - Core/SRT_Core_12a_Ontology_L0L1.md
  - Core/SRT_Core_12b_Ontology_L2.md
  - Core/Ontology_L2_Split/01_Part02.md
  - Core/SRT_Core_01_Axioms.md
  - Governance/SRT_CLAIM_LADDER.md
  - Core/SRT_OPEN_TENSIONS.md
  - Philosophy/SRT_L0_Ontological_Status.md
  - _SRT_SYMBOL_TABLE.md
machine_summary: >
  Version 0.4 preserves the v0.3 distinction between a stable propositional question core
  and a historically variable resolution regime, while repositioning forcing potentialism
  as the paper's nearest technical neighbour. It distinguishes object-level modal accessibility
  among models or worlds from historical-practical reachability among mathematical problems,
  methods, and update regimes. Forcing is treated in a double role: it structures model-extension
  accessibility and, as a historical innovation, transforms the inheritable update regime through
  which that accessibility can be systematically used. The paper is representation-neutral: its
  argument does not depend on potentialism being essentially modal and remains intact under suitable
  non-modal formulations. The main case is restricted to width/forcing potentialism; height, class,
  arithmetic, strict, and divergent potentialisms are comparative neighbours rather than domains
  already unified by the paper. Modal noncommutativity is kept distinct from historical update-order
  noncommutativity. The SRT-specific P3 increment remains selective second-order writeback and local
  directional cost asymmetry, explicitly compatible with multiple attractors, branching research
  programmes, and failure of global convergence.
---

# 数学可达结构、解决制度与问题重新个体化
## 论文写作大纲与策略 v0.4

> **文件性质**：内部写作策略，不是投稿正文。  
> **本版改动**：在 v0.3 的“问题核—解决制度—更新制度”结构上，完成一次潜在主义定位升级：  
> 1. 区分模型／世界之间的模态可及关系与数学实践中的历史可达结构；  
> 2. 将 forcing potentialism 提升为最近邻理论；  
> 3. 明确 forcing 同时具有对象层可及结构与实践层制度创新的双重角色；  
> 4. 将第一篇范围限定于宽度／forcing 潜在主义，并保持模态表示中立。  
> **治理纪律**：数学史、集合论和潜在主义事实必须由外部文献支持；SRT 文件只支持 SRT 如何解释与桥接。

---

# 0. 一句话裁剪标准

\[
\boxed{
\text{本文不主张 forcing 创造了 CH 问题或改变其真值核；}
\atop
\text{本文主张 forcing 非保守地改变了什么构成对 CH 的充分回应、何谓进展，以及集合论能够怎样继续更新。}
}
\]

凡不能服务于以下四项任务的内容，删除或移至后续论文：

1. 区分命题问题核与解决制度；
2. 区分对象层 accessibility 与实践层 reachability；
3. 证明 forcing 改写了可继承的数学更新制度；
4. 说明这种历史改写受形式约束而非共同体任意决定。

---

# 1. 论文定位

## 1.1 首选题目

**When Mathematical Problems Change: Forcing and the Historical Reconstitution of Resolution**

中文：

**当数学问题发生改变：Forcing 与解决制度的历史重构**

## 1.2 备选题目

**Forcing, Problem Identity, and the Reachability of Mathematics**  
**Forcing、问题同一性与数学可达结构**

**From Forcing Accessibility to Mathematical Reachability**  
**从 Forcing 可及关系到数学可达结构**

## 1.3 暂不使用

- *Mathematics Deforms Its Own Possibility Space*
- *Selection, Curvature, and Mathematical Necessity*
- *Mathematical Accessibility as an SRT Ontology*

原因：第一篇应先证明问题与更新制度的历史构成性，不能让高承诺本体论、曲率或模态空间修辞替代案例论证。

## 1.4 目标期刊

首选：**Philosophia Mathematica**。  
备选：**Synthese**。  
进一步后备：**Foundations of Science**。

---

# 2. 最近邻理论与核心解释缺口

## 2.1 潜在主义不是单一理论

第一篇至少区分：

- **高度潜在主义**：通过更高秩或更大层级扩展；
- **宽度／forcing 潜在主义**：加入新子集、泛型对象或 forcing 扩展；
- **类潜在主义**：固定集合宇宙而增加类、谓词或真理资源；
- **算术潜在主义**：通过端扩展、初等扩展等模型关系推进；
- **严格／宽松潜在主义**：真理是否必须在某阶段获得稳定承担者；
- **汇聚／分叉潜在主义**：不同扩展是否具有共同上界。

本文的直接技术邻居是**宽度／forcing 潜在主义**，而不是“潜在主义整体”。

## 2.2 forcing potentialism 的解释对象

forcing potentialism 研究类似：

\[
M\preceq_F M[G]
\]

的模型／世界访问关系，并分析相关模态有效式、汇聚性、最大性原则和不同模型系统。

本文不得声称：

> 潜在主义没有处理动态可达性。

更准确的定位是：

> forcing potentialism 研究哪些模型或集合论世界可由 forcing 到达；本文研究使这种访问关系成为系统数学方法的历史创新，如何改变研究问题的解决制度与未来数学更新制度。

## 2.3 数学实践哲学

Lakatos、Kitcher、Maddy、Corfield、Ferreirós 等已经说明问题、证明、反例、概念和方法具有历史性。本文的增量不能只是再次宣布数学有历史，而必须提供：

- 命题问题核／解决制度区分；
- 保守／非保守解决制度变化；
- 对象层 accessibility／实践层 reachability 区分；
- 更新制度 \(\mathfrak U_t\)；
- forcing 作为双层事件的具体案例。

## 2.4 固定背景发现论

固定背景实在论可以承认 forcing 揭示了先在模型事实，也可以承认方法和训练发生变化。因此本文只主张一个有限但不可删去的构成性结论：

> 一个命题问题核可以保持不变，而围绕它的充分回应、合法进展和可实施更新操作发生非保守重构；这种制度变化是后来数学实践的组成条件，而不只是便利度变化。

## 2.5 缺失的历史—实践层

真正的解释缺口是：

> **一个模型扩展关系如何在数学史中成为可公开重构、复用、传授和继承的数学操作，并进一步改变一个既存问题如何构成研究问题？**

---

# 3. 双层问题身份：问题核与解决制度

## 3.1 命题问题核

令：

\[
Q_{\varphi}
\]

表示由疑问内容 \(\varphi\) 确定的命题问题核。对于连续统假设：

\[
Q_{CH}=\text{“CH 是否成立？”}
\]

其直接答案核：

\[
D(Q_{CH})=\{CH,\neg CH\}
\]

第一篇明确承认：

- \(Q_{CH}\) 在 Cohen 之前已经存在；
- forcing 没有改变直接答案核；
- 独立性说明不是对“CH 在唯一宇宙中真或假”的直接 yes/no 回答。

## 3.2 解决制度

定义时刻 \(t\) 围绕问题核 \(Q_{\varphi}\) 的解决制度：

\[
\Sigma_t(Q_{\varphi})=
\langle D,R_t,E_t,M_t,B_t\rangle
\]

其中：

- \(D\)：直接答案核；
- \(R_t\)：完整回答、部分回答、问题消解和问题分化的分类；
- \(E_t\)：何种结果算作证据、进展或失败；
- \(M_t\)：允许和可实施的证明、构造、模型与解释方法；
- \(B_t\)：默认背景理论及可竞争扩展。

## 3.3 保守变化与非保守变化

若新旧制度之间存在保持以下分类的双向翻译：

- 直接回答；
- 完整解决；
- 部分解决；
- 合法进展；
- 问题消解；

则记为：

\[
\Sigma_t\equiv_c\Sigma_{t+1}
\]

若不存在这样的保持性翻译：

\[
\Sigma_t\not\equiv_c\Sigma_{t+1}
\]

则称问题核 \(Q_{\varphi}\) 在研究层面发生重新个体化：

\[
\operatorname{ReIndiv}_t(Q_{\varphi})
\]

## 3.4 中心身份主张

\[
Q_{CH}^{pre}=Q_{CH}^{post}
\quad\text{at the propositional-core level}
\]

但：

\[
\Sigma_{pre}(Q_{CH})\not\equiv_c\Sigma_{post}(Q_{CH})
\]

“CH 问题改变”严格指第二层，不指命题字符串或直接答案核改变。

## 3.5 提问逻辑锚点

必须与以下传统对话：

- Hamblin 的问题—答案关系；
- Belnap 与 Steel 的 questions and answers；
- Wiśniewski 的 inferential erotetic logic；
- 当代 question semantics 中 direct answer、partial answer、resolution 与 dissolution 的区分。

本文不声称提问逻辑已经给出完整跨历史同一性理论，只借用其基本约束：不知道什么算回答、充分回答和问题消解，就没有完整说明研究者在处理什么问题。

---

# 4. 数学实践状态、派生个体化与双层可达性

## 4.1 实践状态

\[
\boxed{
\mathfrak S_t=(\mathcal P_t,\mathfrak U_t)
}
\]

其中：

- \(\mathcal P_t\)：理论、模型、问题、概念、证明和方法构成的数学可达景观；
- \(\mathfrak U_t\)：可公开重构、复用、传授和继承的数学更新制度。

## 4.2 更新制度

\(\mathfrak U_t\)包括：

- 证明转换；
- 模型构造操作；
- 理论扩展方式；
- 解释、翻译和归约操作；
- 可复用的方法脚手架；
- 合法证据与进展的生成方式；
- 方法进入教材、证明库和研究训练的机制。

## 4.3 个体化是派生映射

\[
\mathcal I_t=\operatorname{Individuate}(\mathcal P_t,\mathfrak U_t)
\]

\[
q_t=\mathcal I_t(Q_{\varphi})=\langle Q_{\varphi},\Sigma_t(Q_{\varphi})\rangle
\]

典型传导：

\[
\Delta\mathfrak U_t\longrightarrow\Delta\Sigma_t\longrightarrow\Delta\mathcal I_t
\]

## 4.4 对象层模态可及关系

例如：

\[
M\preceq_FM[G]
\]

它回答：哪些模型、世界或阶段可由哪些扩展到达？高度、宽度、类和算术潜在主义可以拥有不同访问关系。

## 4.5 历史—实践层数学可达结构

例如：

\[
\mathfrak U_t\longrightarrow\mathfrak U_{t+1}
\]

它回答：某种模型构造、证明或扩展方式何时成为数学共同体可系统使用和继承的制度？

| 层次 | 核心问题 | 典型对象 |
|---|---|---|
| 对象层 accessibility | 哪些模型／世界可由哪些扩展到达？ | \(M,M[G]\)、高度／宽度访问关系 |
| 实践层 reachability | 哪些操作、问题和解决路径在历史阶段中可实施和继承？ | \(\mathcal P_t,\mathfrak U_t,\Sigma_t\) |

## 4.6 forcing 的双重角色

forcing 同时是：

1. **对象层结构**：刻画模型／世界之间的扩展与可及关系；
2. **实践层创新**：改变数学家系统制造、比较和解释这些扩展的方式。

\[
\boxed{
\text{forcing as an accessibility structure}
\neq
\text{forcing as a transformation of the update regime}
}
\]

---

# 5. 结果型创新与制度型创新

## 5.1 结果型创新

结果型创新主要增加数学内容：

\[
\Delta\mathcal P_t\neq0
\]

但没有产生可继承、非局部的新更新操作：

\[
\Delta\mathfrak U_t\approx0
\]

## 5.2 制度型创新

\[
\boxed{
h_t\text{ is regime-innovative}\iff\Delta\mathfrak U_t\neq0
}
\]

并要求：

1. **可继承性**：能被其他主体学习和复用；
2. **非局部性**：改变一类问题或方法；
3. **背景化潜力**：能够进入证明库、教材、训练或理论结构。

## 5.3 两种非交换性

历史更新次序可能满足：

\[
F_b(F_a(\mathfrak S))\neq F_a(F_b(\mathfrak S))
\]

这讨论数学创新出现顺序对后续实践状态的影响。

潜在主义中的模态非交换性则讨论例如：

\[
\Diamond_h\Diamond_w\varphi
\quad\text{与}\quad
\Diamond_w\Diamond_h\varphi
\]

是否等价。

两种非交换性可能相关，但不能直接相互推出。历史非交换性也不是制度型创新的定义，只是强诊断签名。

## 5.4 操作性证据

证明 \(\Delta\mathfrak U_t\neq0\) 可使用：

- 新操作类型出现；
- 操作可重复制造模型、证明或理论扩展；
- 一类问题的解决制度非保守变化；
- 大量后续结果依赖该脚手架；
- 方法进入标准训练、教材或形式化工具；
- 方法退出后不能以零成本恢复旧状态。

不设置“满足若干项即成立”的任意阈值。

---

# 6. 数学可达景观、表示中立性与成本

## 6.1 术语纪律

主术语：**mathematical reachability / 数学可达结构**。

“accessibility relation”保留给模态逻辑与潜在主义的技术语境。

## 6.2 表示中立性

本文论证不依赖潜在主义必须使用模态语言。对象层扩展可以通过：

- Kripke accessibility；
- 模型扩展偏序；
- 关系、代数或范畴结构；
- 适当的非模态复数或阶段语言；

来表达。

即使某种模态潜在主义可以被定义等价地非模态化，本文的问题仍然存在：

> 一种扩展结构如何成为历史可用、可继承并改变解决制度的数学操作？

## 6.3 可达景观

\[
\mathcal P_t=(\mathcal T_t,\mathcal R_t,c_t)
\]

其中：

- \(\mathcal T_t\)：当前可表达、调用和继承的理论、模型、问题、概念与方法；
- \(\mathcal R_t\)：扩展、解释、翻译、模型构造和证明依赖关系；
- \(c_t\)：路径成本的多维结构。

对象层访问关系可进入 \(\mathcal R_t\)，但 \(\mathcal R_t\) 还包含历史可用的方法、翻译和继承关系。

## 6.4 多维成本

\[
c_t(p)=
(c_{formal},c_{constructive},c_{proof},c_{translation},c_{training},c_{inheritance})
\]

候选代理：形式前提与一致性负担、构造步骤、证明依赖图长度、跨理论翻译、训练先修和知识基础设施改写负担。第一篇不得假定这些维度可通约。

---

# 7. 主案例：forcing 如何重构 CH 的解决制度

## 7.1 范围声明

本文直接讨论：

- forcing 所代表的宽度扩展；
- forcing potentialism 的模型／世界访问结构；
- forcing 作为历史方法对集合论解决制度的改变。

本文不在第一篇统一高度、类、算术、严格、分叉潜在主义或全部数学开放性。

## 7.2 forcing 前的解决制度

必须用历史材料重建。候选结构：

- 目标主要被理解为在公认基础中证明或反驳 CH；
- 相对一致性、构造宇宙和基础分析已构成重要进展；
- 尚不存在 Cohen forcing 这一可系统复用的模型扩展制度。

不得把 forcing 前的回应类型简化成只有“证明／反驳”。

## 7.3 forcing 后的非保守改变

forcing 之后，CH 研究稳定包含：

- 相对于背景理论的独立性；
- ground model 与 generic extension；
- 不同模型中 CH 的真值分布；
- forcing axioms 与新公理；
- generic absoluteness；
- universe／multiverse 争论；
- 哪种新原则可算进一步裁决。

这些不是新的直接 yes/no 答案，而是改变完整回应、合法进展、可实施方法和后续问题分化。

## 7.4 forcing 作为对象层结构

正文必须明确模型域、访问关系、元理论条件和适用模态逻辑。不同潜在系统不能被压缩成同一种 accessibility。

## 7.5 forcing 作为更新制度创新

\[
\Delta\mathfrak U_t\neq0
\]

forcing 提供可重复模型扩展操作，并改变：

- 独立性证明如何系统产生；
- 模型关系如何探索；
- 新公理如何测试；
- 后续问题如何组织。

这不能由对象层访问关系自动推出，必须通过技术史、教材史、证明实践和研究结构论证。

## 7.6 技术准确性清单

正文必须：

1. 区分句法独立性 \(T\nvdash\varphi\) 与 \(T\nvdash\neg\varphi\)；
2. 区分相对一致性与模型存在；
3. 不从 \(\operatorname{Con}(ZFC)\) 无条件推出可数传递模型存在；
4. 明确 ground model、generic extension 和外部元理论；
5. 正确处理 Boolean-valued models；
6. 区分模型真值与相对于 ZFC 的不可判定性；
7. 不把方法论多样性直接推成多宇宙本体论；
8. 不将 forcing 模态逻辑推广到全部潜在主义。

## 7.7 universe／multiverse 中立策略

多宇宙论者将 forcing 扩展视为集合论模态结构的一部分；宇宙论者也在 forcing 之后采用 generic absoluteness、\(\Omega\)-logic、内模型和新公理分析。两方真值观不同，但都体现：

\[
\Sigma_{pre}(Q_{CH})\not\equiv_c\Sigma_{post}(Q_{CH})
\]

这只支持解决制度变化，不声称两方共享同一本体论。

## 7.8 实践语言与操作证据

案例档案应分析：

| 实践表达／操作 | 对象层含义 | 可继承操作？ | 改变解决制度？ | 证据 |
|---|---|---:|---:|---|
| pass to a forcing extension | 模型扩展 |  |  |  |
| force \(\varphi\) | forcing relation／构造目标 |  |  |  |
| generic absoluteness | 跨扩展稳定性 |  |  |  |
| forcing axiom | 新公理／扩展原则 |  |  |  |

---

# 8. 形式约束：历史生成不等于自由建构

## 8.1 固定协议内后承只是背景

“协议固定后，后果不能由投票改变”保留为背景前提，不再作为原创中心。

## 8.2 正面约束来源

景观更新受到：独立性、模型满足、相对一致性、可解释性、保守扩展、证明论强度与构造可行性的限制。

## 8.3 一致性强度

自然理论的一致性强度表现出重要的经验结构，但一般理论并不必然线性、良基或可比，“自然理论”也需要进一步说明。

\[
\boxed{
\text{一致性强度提供约束性证据，不提供约束来源的归属性证据。}
}
\]

它反对任意建构，但不单独裁决柏拉图主义、SRT 或其他本体论。

## 8.4 禁止单轴价格表

不得写：

\[
\text{一致性强度}=\text{完整数学成本}=\kappa
\]

一致性强度只可作为 \(c_{formal}\) 的候选坐标之一。

---

# 9. SRT 的必要增量

## 9.1 通用框架与 SRT 分离

以下不是 SRT 独有：数学有历史、更新有路径依赖、方法形成迟滞、\(\Delta\mathfrak U_t\neq0\)。

SRT 的 P3 增量必须集中在：

> **选择性二阶写回：某些成功显现不仅被记录，还以方向不对称的方式降低兼容后续路径成本，并成为未来更新的背景脚手架。**

## 9.2 最小映射

### \(L_0^{math}\)

相对于当前实践尚未稳定显现，但具有非均匀可表达性、可构造性和可达性的候选路径空间。不得等同柏拉图对象仓库、层拓扑斯或完成的全部数学。

### \(L_1^{math}\)

一次明确完成的证明、模型、反例、独立性结果或方法创新。

### \(L_2^{math}\)

被继承和背景化的方法脚手架、证明库、训练、更新制度和解决制度。

## 9.3 避免循环

必须区分：

1. \(\Delta\mathfrak U_t\neq0\)：通用哲学判据；
2. L₂ 映射：对背景化和继承的解释；
3. 方向性成本分化：SRT 可受反驳的额外假设。

## 9.4 局部语义引力预测

\[
\boxed{
\Delta c_t(p_{compatible}\mid L_2^k)
<
\Delta c_t(p_{incompatible}\mid L_2^k)
}
\]

其中 \(\Delta c_t(p)=c_{t+1}(p)-c_t(p)\)。该式表示：相对于一个已形成的局部脚手架 \(L_2^k\)，兼容路径的成本改善系统性地快于不兼容路径。

该预测不要求：

- 全部数学实践汇聚到单一吸引子；
- 高度与宽度潜在性共享同一模态；
- 不同研究纲领最终可合并；
- 竞争性解决制度必然消失。

允许存在多个局部脚手架：

\[
L_2^1,L_2^2,\ldots,L_2^n
\]

以及分叉、部分不可通约或无法汇聚的研究路径。

兼容性必须事前定义，可依据方法复用、证明工具、背景公理、翻译接口、中间结果和训练库；成本代理可包括前置定义、证明依赖图、形式化代码量、学习负担、标准化时间、可复用引理比例和跨框架转换步骤。

若匹配案例中不存在系统性差异，删除该预测，SRT 部分缩减为解释性映射。

## 9.5 \(\kappa_0\)、曲率、\(\Psi_f\) 与开放性

继续放在结尾展望，不进入主论证。不得写 \(\kappa_0>0\) 推出 Gödel 不完备性、forcing 测量 \(\kappa\)、数学曲率单调增加或耦合方程证明不存在终极基础。\(\Psi_f\) 只作为多维成本的候选领域投影族。

---

# 10. 完整论文大纲与字数预算

目标总长度：约 **9,350 词**；上限不超过 **10,000 词**。

## 1. Introduction — 750词

问题核／解决制度；forcing 双重角色；两种可达性；贡献与范围。

## 2. Forcing Potentialism and the Missing Historical-Practical Level — 1,100词

forcing／width potentialism、实践哲学、固定背景论；简述高度、类、算术和分叉潜在主义。建立缺口：潜在主义研究世界如何可达，本文研究可达结构如何成为历史可用的更新制度。

## 3. Problem Cores, Resolution Regimes, and Update Regimes — 1,450词

\(Q_{\varphi}\)、\(D(Q)\)、\(\Sigma_t(Q)\)、\(\equiv_c\)、\(\mathfrak S_t\)、派生个体化、两种可达性、两种非交换性和制度型创新。

## 4. Forcing and the Reconstitution of the CH Resolution Regime — 2,500词

历史背景、Gödel 与 Cohen、对象层访问关系、forcing 作为更新制度、CH 解决制度变化、跨立场证据、实践语言与技术护栏。

## 5. Formal Constraint Across Theories — 650词

独立性、模型、相对一致性、可解释性和一致性强度的约束性／归属性区分。

## 6. The SRT Bridge — 800词

最小映射、多局部吸引子、方向性比较预测、P3 与撤回条件。

## 7. Objections and Failure Conditions — 1,450词

必须处理：

1. 固定背景发现论可接受全部变化；
2. 只是 Lakatos／数学实践哲学；
3. 直接答案没变，所以问题没变；
4. 解决制度只是研究语境；
5. 任何方法都改变制度；
6. 宇宙论者不会接受重新个体化；
7. 一致性层级更支持柏拉图主义；
8. 只是 forcing potentialism 的实践注释；
9. 模态装置可被非模态化；
10. 两种非交换性被混淆；
11. 语义引力预设全局汇聚；
12. SRT 只是后加标签。

## 8. Implications — 400词

开放性不等于任意性；表示中立；其他潜在主义留待后续；高承诺 SRT 主张后置。

## 9. Conclusion — 250词

CH 问题核持续；forcing 的双层作用；历史生成且形式受限。

---

# 11. 写作顺序

## 第一步：潜在主义最近邻矩阵

| 路线 | 潜在对象 | 访问关系 | 与本文关系 |
|---|---|---|---|
| forcing／width potentialism | 新子集、泛型扩展 | forcing extension | 直接最近邻 |
| height potentialism | 更高秩／层级 | rank extension | 比较对象 |
| class potentialism | 更多类／真理资源 | 类扩展 | 分叉与多制度提醒 |
| arithmetic potentialism | 算术模型扩展 | 端扩展等 | 后续推广 |

## 第二步：提问逻辑档案

澄清 direct answer、partial answer、complete answer、resolution、dissolution 和问题同一性。

## 第三步：forcing 技术—历史档案

区分 forcing 前研究回应、Gödel 与 Cohen、对象层访问关系、forcing 方法形成、forcing axioms、generic absoluteness 与 universe／multiverse。

## 第四步：双层证据表

### 对象层访问结构

| 关系 | 模型域 | 条件 | 模态／结构结论 | 来源 |
|---|---|---|---|---|
| \(M\preceq_FM[G]\) |  |  |  |  |
| 高度扩展 |  |  |  |  |

### 实践层制度变化

| 操作／表达 | forcing 前可用？ | 后续可继承？ | 改变解决制度？ | 来源 |
|---|---:|---:|---:|---|
| generic extension |  |  |  |  |
| forcing iteration |  |  |  |  |
| forcing axiom testing |  |  |  |  |
| generic absoluteness |  |  |  |  |

## 第五步：先写定位、框架、案例和反对意见

若无法回答“只是 forcing potentialism 的实践注释”，暂停全文，不先写 SRT。

## 第六步：最后写形式约束、SRT、引言与摘要

---

# 12. 主张—证据—撤回条件

| 主张 | 状态 | 所需证据 | 撤回／缩减条件 |
|---|---|---|---|
| 问题核与解决制度可区分 | 哲学框架 | question semantics | 无法区分 direct answer 与 resolution 则重构 |
| 对象层 accessibility 与实践层 reachability 可区分 | 中心定位 | forcing potentialism 与历史材料 | 两层可完全互定义且无剩余问题则缩减 |
| forcing 后 CH 解决制度非保守变化 | 中心主张 | 技术史、实践和问题语义 | 可完整翻译为旧制度内知识增加则放弃 |
| forcing 改变集合论更新制度 | 中心主张 | 可复用操作、继承和背景化 | 仅增加结果节点则降级 |
| 第一篇限于 width／forcing potentialism | 范围约束 | 文献分类 | 不得推广到全部潜在主义 |
| 论证对模态／非模态表示中立 | 方法主张 | 模态化与非模态化文献 | 若依赖特定模态语义则公开限定 |
| 一致性强度提供非任意约束 | 支撑主张 | 逻辑文献 | 不得用于裁决本体论来源 |
| SRT 局部方向性预测 | P3候选 | 兼容／不兼容路径数据 | 无差异或依赖全局汇聚则删除 |
| \(\kappa_0\) 解释开放性 | P3展望 | 后续独立论证 | 第一篇不成立不影响主论证 |

---

# 13. 新颖性压力测试

1. **固定背景测试**：是否仅说明便利度变化？
2. **实践哲学测试**：是否只是“数学有历史”？
3. **forcing potentialism 吸收测试**：是否只是在重述模型访问关系？
4. **非模态化测试**：去掉模态语言后中心论证是否仍成立？
5. **非交换性测试**：是否混淆模态算子与历史更新次序？
6. **制度膨胀测试**：是否把任何方法都称为制度创新？
7. **社会建构论测试**：删掉形式约束后论证是否不变？
8. **SRT 删除测试**：删掉 SRT 后论文应成立；保留 SRT 时必须有局部可撤回增量。
9. **隐喻测试**：景观、制度、成本、写回与吸引子是否有明确代理？

---

# 14. 禁止裸用清单

第一篇不得写：

- 潜在主义是单一理论；
- 潜在主义没有研究可达关系；
- forcing potentialism 已经解释 forcing 如何成为历史更新制度；
- 对象层 accessibility 等同实践层 reachability；
- 高度／宽度模态不交换等同历史更新不交换；
- forcing 案例代表全部潜在主义；
- 潜在主义必须以模态语言表达；
- 模态可消除意味着历史—实践问题消失；
- Cohen 前 CH 问题不存在；
- forcing 改变 CH 直接答案核；
- 独立性是 CH 真值的直接回答；
- 所有创新都不可交换；
- 任何新定理都是制度创新；
- 语义引力要求全局汇聚；
- 一致性强度证明 SRT；
- \(L_0\) 等同层拓扑斯；
- 数学真理是 \(\hat G\) 源代码；
- \(c_t=\kappa(t)\)；
- \(\Psi_f\) 等同证明复杂度；
- \(\kappa_0>0\) 推出 Gödel 不完备性；
- forcing 后 V=L 必然成为失效路径。

---

# 15. 文献策略

至少建立十组文献：

1. 提问逻辑与问题语义学；
2. forcing 与 CH 技术史；
3. forcing／width potentialism；
4. 潜在主义分类学；
5. 高度、类与分叉潜在主义；
6. 模态机制与非模态化；
7. universe／multiverse、generic absoluteness 与新公理；
8. 数学实践哲学；
9. 一致性强度与自然理论层级；
10. 路径依赖、方法脚手架和知识基础设施。

必须优先处理：

- 2026 年 *Philosophia Mathematica* 潜在主义专刊；
- Sutto 的分类学；
- Berry 的模态机制比较；
- Cook 的潜无穷逻辑分析；
- Linnebo–Shapiro 的严格潜在主义；
- Hamkins 的算术潜在主义；
- Linnebo 的 *Potentialism Demodalized*；
- 2025 年 *Palgrave Companion to the Philosophy of Set Theory* 中 forcing potentialism 与高度／宽度章节；
- Barton–Williams 的类潜在主义；
- Soysal 对高度潜在主义解释力的批评。

引用纪律：不以“潜在主义”统称不同访问关系；技术事实优先原始论文和标准专著；数学史因果判断必须有历史材料；SRT 文件不作为 forcing、CH、potentialism 或 question semantics 的外部证据。

---

# 16. 工作摘要骨架 v0.4

> The continuity of a mathematical sentence does not guarantee the continuity of the research problem organized around it. This paper distinguishes a propositional question core from its historically variable resolution regime and, in dialogue with forcing potentialism, separates two levels of reachability. At the object level, forcing structures accessibility relations among models or set-theoretic worlds. At the historical-practical level, forcing became an inheritable mathematical operation that transformed how such extensions could be constructed, compared, and used to assess progress on the continuum hypothesis. The CH question existed before Cohen, and forcing did not alter its direct yes-or-no answer core. It did, however, non-conservatively reconstitute the resolution regime of CH and the update regime of set-theoretic practice. The argument is representation-neutral: it does not depend on potentialism being essentially modal and survives suitable non-modal formulations of model extension. Mathematical practice is modelled as a time-indexed reachability landscape together with an update regime, from which research-problem individuation is derived. Independence, model theory, relative consistency, and interpretability constrain these historical changes. A final P3 bridge to Selective Reality Theory interprets method sedimentation as selective second-order writeback and formulates a local, defeasible prediction of asymmetric cost reduction for paths compatible with an established mathematical scaffold, without assuming global convergence or a unique attractor.

---

# 17. 投稿前完成标准

- [ ] 已区分 direct answer、partial answer、resolution 与 dissolution；
- [ ] 已给出 \(\equiv_c\) 的最小含义；
- [ ] 已建立 forcing／width、height、class、arithmetic potentialism 的分类矩阵；
- [ ] 已区分对象层 accessibility 与实践层 reachability；
- [ ] 已区分两种非交换性；
- [ ] 已明确第一篇不统一全部潜在主义；
- [ ] 已说明论证在适当非模态表述下仍成立；
- [ ] 已证明 forcing 超出单纯新增知识节点；
- [ ] 已证明 forcing 既是对象层结构也是制度创新；
- [ ] universe／multiverse 中立性有跨立场证据；
- [ ] 一致性强度被标为约束性而非归属性证据；
- [ ] 语义引力使用局部比较式；
- [ ] 明确允许多个局部吸引子与分叉路径；
- [ ] 总字数不超过10,000词；
- [ ] Objections 至少保留1,300词；
- [ ] SRT 映射标为P3；
- [ ] 删除 SRT 后论文仍成立；
- [ ] 保留 SRT 时有不依赖全局汇聚的可撤回增量。

---

# 18. 后续研究路线

## A. 问题同一性理论

研究问题核、疑问语义、保守制度变化、问题分裂和问题消解。

## B. accessibility／reachability 接口

研究模型访问关系如何转化为可用方法，以及历史实践如何选择哪些访问结构具有数学重要性。

## C. 高度与宽度的双层动力学

区分 \(\Diamond_h,\Diamond_w\) 的对象层相互作用与高度／宽度方法进入实践制度的历史次序。

## D. 模态化与非模态化

检验动态制度框架在 Kripke、模型偏序、复数逻辑和范畴化表示中的不变量。

## E. SRT 语义引力经验检验

使用形式化证明库、教材史和引用依赖图，检验多个局部脚手架中兼容路径成本是否系统性下降更快。

## F. 一致性强度与景观几何

只有获得局部度量、连接或序结构后才讨论曲率。

## G. 不可约开放性

独立讨论 \(\kappa_0\)、不完备性和有限形式闭合，不从第一篇案例直接推出。

---

# 19. 最终执行指令

全文始终保持以下五句话：

1. **CH 问题在 Cohen 之前已经存在。**
2. **forcing potentialism 研究模型／世界如何通过 forcing 可达；本文研究这种可达结构如何历史性地成为可继承更新制度。**
3. **forcing 没有改变 CH 的直接答案核，但重构了其解决制度与集合论更新制度。**
4. **该论证不依赖潜在主义必须采用模态语言，也不由 forcing 案例推广到全部潜在主义。**
5. **SRT 只增加局部、方向性的二阶写回假设，不预设数学史全局汇聚。**

若正文不能同时证明第2和第3句，或无法回答“这只是 forcing potentialism 的实践注释”，则不要进入投稿稿阶段。
