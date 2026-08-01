---
id: SRT-STRATEGY-MATHEMATICAL-REACHABILITY-PROBLEM-INDIVIDUATION
title: "数学可达结构、解决制度与问题重新个体化：论文写作大纲与策略"
title_en: "Mathematical Reachability, Resolution Regimes, and Problem Re-Individuation: Paper Outline and Writing Strategy"
status: strategy_note_v0_3
canonical: false
layer: philosophy_bridge
epistemic_layer: bridge
claim_mode: mixed
primary_claim_level: P3
date: 2026-08-01
supersedes:
  - strategy_note_v0_2 @ c82c7d596345ee7c068151c1e415ada02610a76d
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
  - reachability
  - resolution regime
  - path dependence
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
  Version 0.3 resolves the identity and double-counting problems in v0.2. It distinguishes
  a stable propositional question core Q_phi from a historically variable resolution regime
  Sigma_t. Forcing did not create the CH question or change its direct yes/no answer core;
  it non-conservatively changed what counts as a sufficient response, legitimate progress,
  and an admissible mathematical operation. The mathematical-practice state is reduced to
  S_t=(P_t,U_t); problem individuation I_t is derived from the reachability landscape P_t
  and update regime U_t rather than counted as an independent component. Landscape innovation
  is defined by an inheritable, non-local change in U_t. Noncommutativity remains a diagnostic
  signature. Consistency-strength order is treated as constraint evidence, not evidence for
  any particular ontology. The SRT-specific increment is a P3 hypothesis of selective
  second-order writeback and directional cost asymmetry between compatible and incompatible
  paths. Kappa0, curvature, Psi_f and Goedel-style openness remain non-premissive extensions.
---

# 数学可达结构、解决制度与问题重新个体化
## 论文写作大纲与策略 v0.3

> **文件性质**：内部写作策略，不是投稿正文。  
> **核心改动**：解决 v0.2 的两个根本问题：  
> 1. “问题重新个体化”缺少同一性条件；  
> 2. 更新制度 \(\mathfrak U_t\) 与问题个体化 \(\mathcal I_t\) 被重复记账。  
> **治理纪律**：数学史与集合论事实必须由外部文献支持；SRT 文件只支持 SRT 如何解释和桥接，不支持“数学界事实上如此”。

---

# 0. 一句话裁剪标准

\[
\boxed{
\text{本文不主张 forcing 创造了 CH 问题或改变其真值核；}
\atop
\text{本文主张 forcing 非保守地改变了什么构成对 CH 的充分回应、何谓进展，以及集合论能够怎样继续更新。}
}
\]

凡不能服务于以下三项任务的内容，删除或移至后续论文：

1. 区分命题问题核与解决制度；
2. 证明 forcing 改写了可继承的数学更新制度；
3. 说明这种历史改写受形式约束而非共同体任意决定。

---

# 1. 论文定位

## 1.1 首选题目

**When Mathematical Problems Change: Forcing and the Historical Reconstitution of Resolution**

中文：

**当数学问题发生改变：Forcing 与解决制度的历史重构**

## 1.2 备选题目

**Forcing, Problem Identity, and the Reachability of Mathematics**  
**Forcing、问题同一性与数学可达结构**

或：

**Result Innovation and Regime Innovation in Mathematics**  
**数学中的结果型创新与制度型创新**

## 1.3 暂不使用

- *Mathematics Deforms Its Own Possibility Space*
- *Selection, Curvature, and Mathematical Necessity*
- *Mathematical Accessibility as an SRT Ontology*

原因：

- “可能性空间改变”会把实践—结构主张误读成数学真值或全部模态事实随历史变化；
- “曲率”在 SRT 当前文本中承担稳定度、几何下界、历史积累和成本结构等多重角色；
- 第一篇必须先证明问题与更新制度的历史构成性，不能让高承诺本体论替代案例论证。

## 1.4 目标期刊

首选：**Philosophia Mathematica**。  
理由：论文核心是数学问题身份、集合论哲学、forcing 的历史—形式作用和数学实践结构。

备选：**Synthese**。  
进一步后备：**Foundations of Science**。

---

# 2. 核心解释缺口

固定背景发现论可以接受：

- 数学家拥有不同方法；
- 数学史具有路径依赖；
- 新工具使某些证明更容易；
- 共同体的知识与训练会改变。

因此，论文不能只证明：

> 数学实践中的可达性和成本会变化。

真正的解释缺口是：

> **重大数学创新是否会改变一个既存命题问题如何构成研究问题，以及后来数学活动能够使用哪些可继承的更新操作？**

该问题比“知识增加”更强，但不要求宣称：

- 数学真理由历史创造；
- 给定模型中的满足关系随共同体改变；
- Cohen 之前 CH 这个问题不存在。

---

# 3. 双层问题身份：问题核与解决制度

## 3.1 命题问题核

令：

\[
Q_{\varphi}
\]

表示由疑问内容 \(\varphi\) 确定的命题问题核。

对于连续统假设：

\[
Q_{CH}=\text{“CH 是否成立？”}
\]

其直接答案核可写为：

\[
D(Q_{CH})=\{CH,\neg CH\}
\]

第一篇明确承认：

- \(Q_{CH}\) 在 Cohen 之前已经存在；
- forcing 没有把直接答案核改成另一个集合；
- 独立性说明不是对“CH 在唯一宇宙中究竟真还是假”的直接 yes/no 回答。

## 3.2 解决制度

定义时刻 \(t\) 围绕问题核 \(Q_{\varphi}\) 的解决制度：

\[
\Sigma_t(Q_{\varphi})
=
\langle
D,\,R_t,\,E_t,\,M_t,\,B_t
\rangle
\]

其中：

- \(D\)：直接答案核；
- \(R_t\)：完整回答、部分回答、问题消解和问题分化的分类；
- \(E_t\)：何种结果算作证据、进展或失败；
- \(M_t\)：允许和可实施的证明、构造、模型与解释方法；
- \(B_t\)：默认背景理论及可竞争的扩展背景。

这里的 \(\Sigma_t\) 不是“答案集合”的简单扩大，而是围绕同一问题核组织研究活动的**解决制度**。

## 3.3 保守变化与非保守变化

若新旧制度之间存在保持下列分类的双向翻译：

- 直接回答；
- 完整解决；
- 部分解决；
- 合法进展；
- 问题消解；

则记为：

\[
\Sigma_t\equiv_c\Sigma_{t+1}
\]

即解决制度只发生保守扩充或表示变化。

若不存在这样的保持性翻译：

\[
\Sigma_t\not\equiv_c\Sigma_{t+1}
\]

则称问题核 \(Q_{\varphi}\) 在研究层面发生重新个体化：

\[
\operatorname{ReIndiv}_t(Q_{\varphi})
\]

## 3.4 中心问题身份主张

\[
\boxed{
Q_{CH}^{\text{pre-Cohen}}
=Q_{CH}^{\text{post-Cohen}}
\quad\text{at the propositional-core level,}
}
\]

但：

\[
\boxed{
\Sigma_{\text{pre}}(Q_{CH})
\not\equiv_c
\Sigma_{\text{post}}(Q_{CH})
}
\]

论文所说的“CH 问题改变”，严格指第二个层次，而不是第一个层次。

## 3.5 提问逻辑／问题语义学锚点

该区分必须与以下传统对话：

- Hamblin 的问题—答案关系；
- Belnap 与 Steel 的 questions and answers；
- Wiśniewski 的 inferential erotetic logic；
- 当代 question semantics 中直接答案、部分答案和问题消解的区分。

论文不能声称提问逻辑已经自动提供跨历史问题同一性的完整理论。本文只借用其核心约束：

> 不知道什么算作回答、充分回答和问题消解，就没有完整说明研究者正在处理什么问题。

---

# 4. 数学实践状态与派生个体化

## 4.1 状态缩减

取消 v0.2 的三元状态：

\[
(\mathcal P_t,\mathfrak U_t,\mathcal I_t)
\]

改为：

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
- 合法证据和进展的生成方式；
- 方法进入教材、证明库和研究训练的机制。

## 4.3 个体化是派生映射

问题个体化不再作为第三个独立状态量，而由当前景观与更新制度派生：

\[
\mathcal I_t
=
\operatorname{Individuate}(\mathcal P_t,\mathfrak U_t)
\]

对于问题核：

\[
q_t
=
\mathcal I_t(Q_{\varphi})
=
\langle Q_{\varphi},\Sigma_t(Q_{\varphi})\rangle
\]

因此典型传导关系是：

\[
\Delta\mathfrak U_t
\longrightarrow
\Delta\Sigma_t
\longrightarrow
\Delta\mathcal I_t
\]

这消除了 v0.2 中 \(M_t\)、\(\Sigma_t\)、\(\mathfrak U_t\) 和 \(\mathcal I_t\) 的双重记账。

---

# 5. 结果型创新与制度型创新

## 5.1 结果型创新

结果型创新主要增加数学内容：

\[
\Delta\mathcal P_t\neq0
\]

但没有产生一个可继承、非局部的新更新操作：

\[
\Delta\mathfrak U_t\approx0
\]

它可以非常重要，也可以降低局部证明成本，但仍在成熟更新制度内完成。

## 5.2 制度型／景观型创新

定义：

\[
\boxed{
h_t\text{ is regime-innovative}
\iff
\Delta\mathfrak U_t\neq0
}
\]

并要求该变化满足三个范围约束：

1. **可继承性**：不是一次性技巧，能被其他主体学习和复用；
2. **非局部性**：改变一类问题或方法，而非只服务单一步骤；
3. **背景化潜力**：能够进入证明库、教材、标准训练或后续理论结构。

制度型创新可能产生：

- 已有问题的重新个体化；
- 新问题族的生成；
- 理论间新可达关系；
- 解决标准的非保守改变。

## 5.3 非交换性是强签名，不是定义

若：

\[
F_b(F_a(\mathfrak S))
\neq
F_a(F_b(\mathfrak S))
\]

则说明更新顺序可能改变后续状态。

但不可交换性不能作为定义，因为：

- 普通引理依赖也可能产生顺序不对称；
- 某些重大方法创新最终可能在抽象层面可交换；
- 更深的变化可能表现为 \(F_b\) 在 \(a\) 出现前根本无定义。

因此，非交换性只作为制度变化的强诊断证据。

## 5.4 操作性证据类型

取消“六项中至少满足三项”的任意阈值。以下仅作为证明 \(\Delta\mathfrak U_t\neq0\) 的证据类型：

- 新操作类型出现；
- 新操作可重复制造模型、证明或理论扩展；
- 一类问题的解决制度发生非保守变化；
- 大量后续结果依赖该方法脚手架；
- 该操作进入标准训练、教材或形式化工具；
- 方法退出后无法以零成本恢复旧的默认研究状态。

---

# 6. 数学可达景观与成本

## 6.1 术语纪律

主术语：**mathematical reachability / 数学可达结构**。

“accessibility relation”保留给模态逻辑与潜在主义的技术语境。

论文必须明确：

> Reachability concerns historically available transitions among mathematical problems, methods, models, and theories. It is not identical to a possible-world accessibility relation, although the two may later be formally related.

## 6.2 可达景观

\[
\mathcal P_t=(\mathcal T_t,\mathcal R_t,c_t)
\]

其中：

- \(\mathcal T_t\)：当前可表达、调用和继承的理论、模型、问题、概念和方法；
- \(\mathcal R_t\)：扩展、解释、翻译、模型构造和证明依赖关系；
- \(c_t\)：路径成本的多维结构。

## 6.3 多维成本

第一篇不建立统一标量成本。

\[
c_t(p)=
\big(
c_{formal},
c_{constructive},
c_{proof},
c_{translation},
c_{training},
c_{inheritance}
\big)
\]

候选代理：

- 形式前提与一致性负担；
- 构造所需的技术步骤；
- 证明依赖图长度；
- 跨理论翻译负担；
- 学习该方法所需前置训练；
- 改写证明库、教材和研究习惯的负担。

不得假定这些维度可通约。

---

# 7. 主案例：forcing 如何重构 CH 的解决制度

## 7.1 核心纪律

不能写：

- Cohen 之前 CH 问题不存在；
- forcing 直接回答了 CH 的绝对真值；
- 独立性自动证明多宇宙论；
- 所有 forcing 叙述都必须以同一元理论技术实现。

可以写：

> forcing 与独立性结果保持了 CH 的命题问题核，却重构了什么算作对 CH 的充分回应、何谓进展，以及集合论可以使用哪些模型扩展操作。

## 7.2 forcing 前的解决制度

需要通过历史材料论证，而不是凭印象假定。候选重建：

- 默认目标主要被理解为在公认集合论基础中证明或反驳 CH；
- 可接受进展包括相对一致性、构造性宇宙结果和基础分析；
- 尚不存在 Cohen forcing 这一可系统复用的模型扩展制度。

不得把 forcing 前的解决制度简化成只有：

\[
\{\text{证明},\text{反驳}\}
\]

因为 Gödel 的相对一致性与构造宇宙工作已经扩展了研究回应类型。

## 7.3 forcing 后的非保守改变

forcing 之后，围绕 CH 的研究制度稳定包含：

- 相对于背景理论的独立性说明；
- ground model 与 generic extension 的关系；
- 不同模型中 CH 的真值分布；
- forcing axioms 与新公理纲领；
- generic absoluteness；
- universe／multiverse 的集合论哲学争论；
- 哪种新原则能算作对 CH 的进一步裁决。

这些变化不是把独立性当作 CH 的直接 yes/no 答案，而是改变：

- 完整回应的分类；
- 合法进展的标准；
- 可实施方法；
- 后续问题分化。

## 7.4 forcing 作为更新制度创新

forcing 的承重点不是单个结果，而是：

\[
\Delta\mathfrak U_t\neq0
\]

它提供一种可重复的模型扩展操作，并改变：

- 独立性证明如何系统产生；
- 哪些模型间关系可被探索；
- 新公理如何被测试；
- 后续问题怎样组织。

## 7.5 技术准确性清单

正文必须选择清晰的技术呈现并说明元理论条件，不得混用以下层次：

1. 区分句法独立性：
   \[
   T\nvdash\varphi,
   \qquad
   T\nvdash\neg\varphi
   \]
2. 区分相对一致性陈述与模型存在陈述；
3. 不从 \(\operatorname{Con}(ZFC)\) 无条件推出“存在 ZFC 的可数传递模型”；
4. 明确 ground model、generic extension 与外部元理论视角；
5. 若使用 Boolean-valued models，不能同时假装只是在普通模型中直接加对象；
6. 区分 CH 在特定模型中的真值与相对于 ZFC 的不可判定性；
7. 不把方法论多样性直接推成集合论多宇宙本体论。

## 7.6 宇宙观／多宇宙观中立策略

第一篇保持本体论中立，但不能仅说“两边都兼容”。必须提供跨立场证据：

- 多宇宙论者把 forcing 扩展理解为集合论模态结构的重要组成；
- 宇宙论者仍在 forcing 之后采用 generic absoluteness、\(\Omega\)-logic、内模型和新公理分析等此前不可实施的研究制度。

因此，两边对 CH 的最终真值观不同，但双方的实际研究都表明：

\[
\Sigma_{pre}(Q_{CH})
\not\equiv_c
\Sigma_{post}(Q_{CH})
\]

该论证只支持“解决制度发生变化”，不声称宇宙论者承认 CH 的直接问题核已改变。

---

# 8. 形式约束：历史生成不等于自由建构

## 8.1 固定协议内后承只是背景

“协议固定后，后果不能由投票改变”仍然保留，但只作为背景前提。

## 8.2 正面约束来源

景观更新受到：

- 独立性；
- 模型存在与模型满足；
- 相对一致性；
- 可解释性；
- 保守扩展；
- 证明论强度；
- 构造可行性；

的限制。

这些约束使共同体不能任意决定什么操作有效、什么理论扩展可行。

## 8.3 自然理论的一致性强度结构

大量自然发生的理论在一致性强度上呈现近似预良序的经验规律，而一般理论并不必然线性、良基或可比。“自然理论”的范围本身也是开放问题。

该现象在论文中的作用必须双向限定：

\[
\boxed{
\text{一致性强度结构提供约束性证据，不提供约束来源的归属性证据。}
}
\]

它支持：

- 理论景观并非共同体自由排列；
- 跨理论方向存在非任意结构。

它不单独支持：

- 柏拉图主义；
- SRT；
- 形式主义；
- 任何特定本体论。

柏拉图主义者可以把它解释为固定形式事实；SRT 若要增加解释力，必须说明这些约束如何进入历史更新、写回和背景化。

## 8.4 禁止单轴价格表

不得写：

\[
\text{一致性强度}
=
\text{完整数学成本}
=
\kappa
\]

一致性强度只作为 \(c_{formal}\) 的候选坐标之一。

---

# 9. SRT 的必要增量

## 9.1 通用框架与 SRT 增量分离

以下内容不是 SRT 独有：

- 数学有历史；
- 更新具有路径依赖；
- 方法可形成迟滞；
- \(\Delta\mathfrak U_t\neq0\)。

这些首先属于通用数学实践框架。

SRT 的 P3 增量必须集中在：

> **选择性二阶写回：某些成功显现不仅被记录，还以方向不对称的方式降低兼容后续路径成本，并成为未来更新的背景脚手架。**

## 9.2 最小映射

### \(L_0^{math}\)

相对于当前数学实践尚未稳定显现，但具有非均匀可表达性、可构造性和可达性的候选路径空间。

不得等同：

- 柏拉图对象仓库；
- 层拓扑斯；
- 全部完成数学结构。

### \(L_1^{math}\)

一次明确完成的：

- 证明；
- 模型；
- 反例；
- 独立性结果；
- 方法创新。

### \(L_2^{math}\)

被继承和背景化的：

- 方法脚手架；
- 证明库；
- 标准训练；
- 更新制度；
- 解决制度。

## 9.3 避免循环

不能把：

\[
\Delta\mathfrak U_t\neq0
\]

直接定义为“L₂ 级写回”，然后声称 SRT 解释了它。

应区分：

1. \(\Delta\mathfrak U_t\neq0\)：通用哲学判据；
2. L₂ 映射：SRT 对背景化和继承的解释；
3. 方向性成本分化：SRT 可受反驳的额外假设。

## 9.4 语义引力的比较式预测

Ax-L2-08 的 P3 数学桥接不应写成单边恒真式：

\[
c_{t+1}(p_{compatible})<c_t(p_{compatible})
\]

而应写成比较式：

\[
\boxed{
\Delta c_t(p_{compatible})
<
\Delta c_t(p_{incompatible})
}
\]

其中：

\[
\Delta c_t(p)=c_{t+1}(p)-c_t(p)
\]

若成本下降为负值，则该式表示：沉积以后，兼容路径的成本改善系统性地快于不兼容路径。

### 兼容性必须事前定义

候选判据：

- 复用同一模型构造操作；
- 依赖同一证明工具；
- 接受相同背景公理或翻译接口；
- 可以继承既有中间结果；
- 使用同一训练和形式库。

不得根据最后成功者反向定义“兼容”。

### 成本代理

候选指标：

- 前置定义数量；
- 证明依赖图长度；
- 形式化代码量；
- 学习先修负担；
- 工具从提出到标准化的时间；
- 可复用引理比例；
- 跨框架转换步骤。

### 撤回条件

若匹配案例中兼容路径与不兼容路径没有系统性差异，删除该预测，SRT 部分缩减为解释性映射。

## 9.5 \(\kappa_0\)、曲率与开放性

继续放在结尾展望，不进入主论证。

允许写：

> 若任何有限更新制度都无法穷尽未来合法数学操作，这一现象可被 SRT 解释为不可约开放性的领域表现。

禁止写：

- \(\kappa_0>0\) 推出 Gödel 不完备性；
- forcing 直接测量 \(\kappa\)；
- 数学曲率单调增加；
- 耦合方程已经证明没有终极基础。

## 9.6 \(\Psi_f\)

只作为多维成本的候选领域投影族，不建立统一数值同一性。

---

# 10. 完整论文大纲与字数预算

目标总长度：约 **9,300 词**；上限不超过 **10,000 词**。

## 1. Introduction: When Does a Mathematical Problem Change? — 800词

- CH 问题持续存在与解决制度改变的区分；
- forcing 作为制度型创新；
- 核心贡献与边界；
- 不宣称数学真理随历史改变。

## 2. Existing Accounts and the Missing Level — 900词

重点：

- 固定背景柏拉图主义；
- 数学实践哲学；
- 潜在主义。

简述：

- 结构主义；
- Carnap／形式主义。

建立缺口：现有路线缺少“问题核—解决制度—更新制度”的统一分析。

## 3. Problem Cores, Resolution Regimes, and Update Regimes — 1,500词

合并 v0.2 的问题个体化与实践构成性两节：

- \(Q_{\varphi}\)；
- \(D(Q)\)；
- \(\Sigma_t(Q)\)；
- 保守等价 \(\equiv_c\)；
- \(\mathfrak S_t=(\mathcal P_t,\mathfrak U_t)\)；
- \(\mathcal I_t\) 作为派生映射；
- 结果型与制度型创新；
- 非交换性签名。

## 4. Forcing and the Reconstitution of the CH Resolution Regime — 2,500词

- forcing 前的历史背景；
- Gödel 与 Cohen 的技术角色；
- 独立性与直接回答的区分；
- forcing 作为可复用模型扩展制度；
- CH 解决制度的非保守变化；
- universe／multiverse 跨立场证据；
- 技术准确性清单。

## 5. Formal Constraint Across Theories — 750词

- 独立性、模型、相对一致性和可解释性；
- 自然理论一致性强度的经验结构；
- 约束性证据／归属性证据区分。

## 6. The SRT Bridge: Selective Second-Order Writeback — 850词

- \(L_0^{math}/L_1^{math}/L_2^{math}\)；
- 通用框架与 SRT 增量分离；
- 方向性比较预测；
- P3 与撤回条件。

## 7. Objections and Failure Conditions — 1,300词

### Objection 1：固定背景发现论仍可接受全部变化

回答：论文不试图从一致性序推出本体论，而是主张解决制度与更新制度具有真实构成作用；若对手把这些全部降为“外部认识史”，必须解释为什么完整回应和合法进展的分类不是研究问题身份的一部分。

### Objection 2：这只是 Lakatos／Kitcher／数学实践哲学

回答：承认历史性，新增：问题语义的解决制度、保守等价、派生个体化和更新制度判据。

### Objection 3：直接答案没变，所以问题没变

回答：明确承认命题问题核与直接答案核连续；重新个体化发生在研究解决制度层，不通过偷换直接答案完成。

### Objection 4：解决制度只是研究语境，不是问题身份

回答：使用 question semantics 说明回答、完整回答、问题消解与合法进展对研究问题识别具有构成作用；同时明确这是“研究问题身份”，不是命题字符串身份。

### Objection 5：任何方法都改变更新制度

回答：要求可继承性、非局部性与背景化潜力；一次性技巧不满足。

### Objection 6：宇宙论者不会接受重新个体化

回答：不要求其改变 CH 真值观，只要求承认 forcing 后实际使用的证据、进展和操作制度不可保守翻译回 forcing 前。

### Objection 7：一致性层级更支持柏拉图主义

回答：承认其本体论中立；它只证明非任意性，不证明约束来源。

### Objection 8：SRT只是后加标签

回答：SRT 的可区别增量只在方向性二阶写回；若比较预测失败，缩减 SRT 节。

## 8. Implications — 400词

- 开放性不等于任意性；
- 更强数学模态主张留待后续；
- \(\kappa_0\)／不完备性只作解释性展望。

## 9. Conclusion — 300词

重申：

1. CH 问题核没有被 forcing 创造；
2. forcing 重构了其解决制度与集合论更新制度；
3. 该变化既历史生成，又受形式约束。

---

# 11. 写作顺序

## 第一步：提问逻辑文献档案

先澄清：

- direct answer；
- partial answer；
- complete answer；
- question resolution；
- question dissolution；
- 问题同一性与答案结构的关系。

不得在没有文献锚点时自造 \(\equiv_c\) 的全部语义细节。

## 第二步：forcing 技术—历史档案

建立：

- forcing 前研究回应类型；
- Gödel 与 Cohen 的不同贡献；
- forcing 方法如何形成；
- 后续 forcing axioms、generic absoluteness、universe／multiverse 发展。

## 第三步：解决制度变化表

| 维度 | forcing 前 | forcing 后 | 保守变化？ | 证据 |
|---|---|---|---|---|
| 直接答案核 |  |  |  |  |
| 完整回应 |  |  |  |  |
| 部分回应 |  |  |  |  |
| 合法进展 |  |  |  |  |
| 方法操作 |  |  |  |  |
| 背景理论 |  |  |  |  |

## 第四步：更新制度变化表

| 操作 | 是否 forcing 前可用 | forcing 后可继承性 | 非局部影响 | 背景化证据 |
|---|---:|---:|---:|---|
| generic extension |  |  |  |  |
| forcing iteration |  |  |  |  |
| forcing axiom testing |  |  |  |  |

## 第五步：先写第3、4、7节

- 理论定义；
- forcing 案例；
- 最强反对意见。

若 Objection 4 无法回答，暂停全文，不先写 SRT。

## 第六步：写形式约束与 SRT 桥接

先完成非 SRT 论证，再决定 SRT 节实际能保留多少。

## 第七步：最后写引言、摘要和题目

---

# 12. 主张—证据—撤回条件

| 主张 | 状态 | 所需证据 | 撤回／缩减条件 |
|---|---|---|---|
| 命题问题核与解决制度可区分 | 哲学框架 | question semantics 文献 | 若无法区分 direct answer 与 resolution，重构框架 |
| forcing 后 CH 解决制度非保守变化 | 中心主张 | 技术史、研究实践与问题语义分析 | 若变化可完整翻译为旧制度内的知识增加，放弃 re-individuation |
| forcing 改变集合论更新制度 | 中心主张 | 可复用操作、继承和背景化证据 | 若仅增加单个结果节点，降为结果型创新 |
| 个体化由 \((\mathcal P_t,\mathfrak U_t)\) 派生 | 理论设计 | 避免双重计数与案例适配 | 若存在稳定的独立 \(\mathcal I_t\) 变化案例，再考虑分离式 |
| 一致性强度提供非任意约束 | 支撑主张 | 逻辑文献 | 不得用于裁决本体论来源 |
| universe／multiverse 双方都体现制度变化 | 中立支撑 | Woodin、Hamkins等实践材料 | 若实质依赖一方，公开限定立场 |
| SRT方向性成本预测 | P3候选 | 匹配的兼容／不兼容路径历史数据 | 无差异则删除预测并缩减SRT节 |
| \(\kappa_0\)解释不可约开放性 | P3展望 | 后续独立论证 | 第一篇不成立不影响主论证 |

---

# 13. 新颖性压力测试

## 13.1 固定背景发现论测试

对手可以承认：

- 真理固定；
- 问题核固定；
- 研究制度改变。

论文增量必须是：说明研究制度变化对“什么构成一个完整研究问题”具有真实构成作用，而非仅影响便利程度。

## 13.2 Lakatos 吸收测试

若论文只说概念、证明和问题会历史变化，则没有增量。

必须交付：

- 直接答案核／解决制度区分；
- 保守等价；
- 更新制度；
- 派生个体化；
- forcing 的非保守案例。

## 13.3 “任何方法都改变制度”测试

若一个创新只有局部引用价值，没有可继承、非局部和背景化作用，不得称为制度型创新。

## 13.4 社会建构论测试

若形式约束删掉后论证不变，论文失败。

## 13.5 SRT 删除测试

删除 SRT 后，数学哲学论文必须仍成立；但 SRT 节必须留下一个可区别的方向性预测，否则按撤回条件缩减。

## 13.6 隐喻测试

“景观”“制度”“写回”“成本”都必须对应明确对象、关系与证据代理。

---

# 14. 禁止裸用清单

第一篇不得直接写：

- Cohen 之前 CH 问题不存在；
- forcing 改变了 CH 的直接答案核；
- 独立性就是对 CH 真值的直接回答；
- 所有景观创新都不可交换；
- 任何新定理都是制度型创新；
- 自然理论已被证明形成无例外线性序；
- 一致性强度支持 SRT 而不支持柏拉图主义；
- \(L_0\) 等同层拓扑斯；
- 数学真理是 \(\hat G\) 的源代码；
- \(c_t=\kappa(t)\)；
- \(\Psi_f\) 等同证明复杂度；
- \(\kappa_0>0\) 推出 Gödel 不完备性；
- 曲率单调增加；
- 耦合方程已证明数学不存在终极基础；
- forcing 后 V=L 纲领必然成为高成本或失效路径。

---

# 15. 文献策略

至少建立八组文献：

1. **提问逻辑与问题语义学**：Hamblin；Belnap & Steel；Wiśniewski；当代 question semantics；
2. **forcing 与 CH 技术史**：Gödel；Cohen；标准集合论专著；forcing 历史；
3. **集合论哲学**：universe、multiverse、generic absoluteness、new axioms；
4. **数学实践哲学**：Lakatos；Kitcher；Maddy；Corfield；Ferreirós；
5. **潜在主义**：集合论潜在主义、算术潜在主义、不同可达结构；
6. **结构主义与形式主义**：对象身份、框架选择和内部后承；
7. **一致性强度与自然理论层级**：近预良序现象及其限制；
8. **路径依赖、方法脚手架与知识基础设施**：用于历史继承和背景化，不替代形式论证。

引用纪律：

- 技术事实优先原始论文、标准专著和权威逻辑来源；
- 数学史因果判断必须有历史材料；
- Woodin／Hamkins 等立场按其原文呈现，不以二手口号代替；
- SRT 内部文件不作为 forcing、CH 或 question semantics 的外部证据。

---

# 16. 工作摘要骨架 v0.3

> The continuity of a mathematical sentence does not guarantee the continuity of the research problem organized around it. This paper distinguishes a propositional question core from its historically variable resolution regime: the standards governing what counts as a direct answer, a sufficient response, legitimate progress, or a dissolution of the problem, together with the mathematical operations available for producing such outcomes. The continuum hypothesis existed as a determinate question before Cohen, and forcing did not alter its direct yes-or-no answer core. It did, however, non-conservatively reconstitute the resolution regime of CH and the update regime of set-theoretic practice by making generic extensions and systematic independence proofs inheritable mathematical operations. I model mathematical practice as a time-indexed reachability landscape together with an update regime, from which problem individuation is derived. The resulting account is historically constitutive without being truth-constitutive: mathematical practice can change what constitutes a sufficient resolution and how later mathematics can proceed, while independence, model theory, relative consistency, and interpretability constrain those changes. A final P3 bridge to Selective Reality Theory interprets method sedimentation as selective second-order writeback and formulates a defeasible prediction of asymmetric cost reduction for compatible future paths.

该摘要必须在完成提问逻辑和 forcing 案例档案后重写。

---

# 17. 投稿前完成标准

- [ ] 已区分 direct answer、partial answer、resolution 与 dissolution；
- [ ] 已给出 \(\equiv_c\) 的最小可辩护含义；
- [ ] 没有声称 Cohen 前 CH 问题不存在；
- [ ] 已证明 forcing 变化超出单纯新增知识节点；
- [ ] \(\mathcal I_t\) 已从状态量改为派生映射；
- [ ] 已删除任意“三项／六项”门槛；
- [ ] universe／multiverse 中立性有实际跨立场证据；
- [ ] 一致性强度被标为约束性而非归属性证据；
- [ ] 语义引力使用兼容／不兼容比较式；
- [ ] 兼容性和成本代理事前定义；
- [ ] 总字数预算不超过10,000词；
- [ ] Objections 至少保留1,200词；
- [ ] SRT 整体映射标为P3；
- [ ] 删除SRT后论文仍有独立哲学贡献；
- [ ] 保留SRT时至少有一个可撤回的方向性增量。

---

# 18. 后续研究路线

## A. 更完整的问题同一性理论

进一步研究：

- 问题核、疑问语义与研究问题身份；
- 保守制度变化的形式条件；
- 一个问题何时分裂为问题族；
- 问题消解与问题回答的差别。

## B. 动态更新制度

发展 \(\mathfrak U_t\) 的代数或范畴结构，研究：

- 操作定义域的创建；
- 更新组合；
- 非交换性；
- 继承与背景化。

## C. SRT 语义引力的经验检验

使用形式化证明库、教材史和引用依赖图，检验兼容路径成本是否系统性下降得更快。

## D. 一致性强度与景观几何

只在获得局部度量、连接或序结构后讨论“曲率”，不以隐喻替代形式化。

## E. 不可约开放性

独立讨论 \(\kappa_0\)、不完备性和有限形式闭合，不从第一篇案例直接推出。

---

# 19. 最终执行指令

全文始终保持以下三句话：

1. **CH 问题在 Cohen 之前已经存在。**
2. **forcing 没有改变 CH 的直接答案核，但重构了其解决制度与集合论更新制度。**
3. **这种重构具有历史构成性，却仍受独立性、模型、一致性和解释关系的非任意约束。**

若正文不能同时证明第2和第3句，则不要进入投稿稿阶段。
