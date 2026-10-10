---
id: SRT-SRC-2026-10-10-AO-STOCHASTIC-LANDSCAPE-CORPUS
type: source_card
status: draft
date: 2026-10-10
layer: materials
epistemic_layer: evidence
claim_mode: source_evidence
canonical: false
ai_do_not_use_for_definition: true
research_mode: U
root_question: What do Ping Ao's stochastic dynamical decomposition and potential-landscape papers actually establish, and which issues remain debated?
comparative_claim: none
named_comparator: Ping Ao and coauthors; Zhou and Li 2016
n_mode_triggered: false
source_id: AO-STOCHASTIC-LANDSCAPE-CORPUS-2004-2017
source_type: primary_papers_and_review_with_published_dispute
domain: nonequilibrium_statistical_physics_and_systems_biology
authors: Ping Ao and coauthors; Peijie Zhou and Tiejun Li as mathematical critics
date_added: 2026-10-10
evidence_level: primary_publisher_abstracts_and_2017_open_html_full_article
integration_priority: B1_candidate
source_log: Operations/Material_Log/2026-10_Part01.md
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_TRACE_VERTICAL_SELECTION_PARTICIPATION_UNIFICATION_2026-10-10.md
  - Operations/Audits/SRT_VERTICAL_SELECTION_POSITION_PUBLICNESS_PRESSURE_2026-10-10.md
tags: [SourceCard, PingAo, StochasticDynamics, PotentialLandscape, NonEquilibrium, AType, SourceFidelity, Literature]
---

# 敖平（Ping Ao）随机动力学 / 演化势景观论文群：有界来源档案

> **身份与来源纪律：** 本卡是多篇论文的**分篇证据矩阵**，不是将它们归为同一数学定理的“综合一手论文”。A = 论文原生主张；B = SRT 解释，仅在末节标为 M。不得把敖平与**王劲（Jin Wang）**的独立 potential-and-flux 研究误当同一作者团队。不得把本卡当作原初 Selection 的数学证明。状态：B1 候选／尚待独立内容评审，不是作者的本体论裁决。
>
> **检索记录（2026-10-10）：** 有 DOI 可核的出版社原文摘要、期刊 HTML/全文及相关公开评论／回应；2004、2005、2007、2009 的全文未逐页核查，不能宣称 exhaustive full-text source audit。2017 Scientific Reports 正文 HTML 中的 Abstract、Introduction、Results、Discussion 已核对；2016 争议双方的论文摘要／可公开正文片段已核对。刊物内数学定理的完整假设链、数值代码及原始实测数据未复现。以下每个超出摘要的技术细节均会单独限定。

## 1. Corpus bibliography and scope of checking

| ID | 一手文献 / DOI | 可核锚点及检查级别 | 来源角色 |
| --- | --- | --- | --- |
| AO04 | Ping Ao (2004), “Potential in stochastic differential equations: novel construction”, *J. Phys. A: Math. Gen.* 37 L25–L30; [doi:10.1088/0305-4470/37/3/L01](https://doi.org/10.1088/0305-4470/37/3/L01) | [出版社来源与公开摘要镜像](https://explore.openaire.eu/search/publication?pid=10.1088%2F0305-4470%2F37%2F3%2Fl01); 摘要／元数据核验，正文逐页**未核** | 在非平衡 SDE 中构造势函数的方法主张 |
| AO05 | Ping Ao (2005), “Laws in Darwinian evolutionary theory”, *Physics of Life Reviews* 2:117–156; [doi:10.1016/j.plrev.2005.03.002](https://doi.org/10.1016/j.plrev.2005.03.002) | [出版社摘要及公开 Introduction](https://www.sciencedirect.com/science/article/pii/S1571064505000126)；不是对三条“laws”的独立数学确证 | 四个动力学构件 + 层级动力学构想 |
| AO07 | Ping Ao, Chulan Kwon & Hong Qian (2007), “On the existence of potential landscape in the evolution of complex systems”, *Complexity* 12(4):19–27; [doi:10.1002/cplx.20171](https://doi.org/10.1002/cplx.20171) | [出版社摘要](https://onlinelibrary.wiley.com/doi/abs/10.1002/cplx.20171)；全文未核 | 非平衡势景观构造、与 Itô/Stratonovich 比较 |
| AO09 | Ping Ao (2009), “Global view of bionetwork dynamics: adaptive landscape”, *J. Genet. Genomics* 36(2):63–73; [doi:10.1016/S1673-8527(08)60093-4](https://doi.org/10.1016/S1673-8527(08)60093-4) | [期刊摘要](https://www.sciencedirect.com/science/article/pii/S1673852708600934)；非技术综述；全文未核 | 生物网络稳健性／稳定性及适应景观的量化价值 |
| AO17R | Ruoshi Yuan, Ying Tang & Ping Ao (2017), “SDE decomposition and A-type stochastic interpretation in nonequilibrium processes”, *Frontiers of Physics* 12:120201; [doi:10.1007/s11467-017-0718-2](https://doi.org/10.1007/s11467-017-0718-2) | [期刊页 Abstract、References](https://academic.hep.com.cn/fop/EN/10.1007/s11467-017-0718-2)；争议中的**作者立场综述** | 耗散、破坏详细平衡的分量、势景观及 A-type 解释；主张唯一性 |
| AO17E | Ying Tang, Ruoshi Yuan, Gaowei Wang, Xiaomei Zhu & Ping Ao (2017), “Potential landscape of high dimensional nonlinear stochastic dynamics with large noise”, *Scientific Reports* 7:15762; [doi:10.1038/s41598-017-15889-2](https://doi.org/10.1038/s41598-017-15889-2) | [公开全文](https://www.nature.com/articles/s41598-017-15889-2), Abstract、Introduction、Results: Formulation、Discussion；出版社注明 2019-08-06 correction，更新版本已在网站 | 大噪声高维例子、least-action 方法和 38 维癌症网络模型 |
| ZL16 | Peijie Zhou & Tiejun Li (2016), “Construction of the landscape for multi-stable systems: Potential landscape, quasi-potential, A-type integral and beyond”, *J. Chem. Phys.* 144:094109; [doi:10.1063/1.4943096](https://doi.org/10.1063/1.4943096) | [期刊页面 Abstract](https://doi.org/10.1063/1.4943096)；**独立对照／争议一方** | 比较 stationary landscape、Freidlin–Wentzell quasipotential、Ao SDE decomposition，指出一般非唯一性 |
| YTA16 | Ruoshi Yuan, Ying Tang & Ping Ao (2016), “Comment on ‘Construction of the landscape…’”, *J. Chem. Phys.* 145:147104; [doi:10.1063/1.4964681](https://doi.org/10.1063/1.4964681) | [出版社公开前言与摘要](https://pubs.aip.org/jcp/article/145/14/147104/352135)；**争议另一方** | 对 ZL16 非唯一性结论提出反驳，特别讨论线性 OU 类条件 |
| ZL16R | Peijie Zhou & Tiejun Li (2016), “Response to ‘Comment…’”, *J. Chem. Phys.* 145:147105; [doi:10.1063/1.4964682](https://doi.org/10.1063/1.4964682) | [PubMed 元数据及摘要](https://pubmed.ncbi.nlm.nih.gov/27782518/)；**争议回应** | 反驳仅凭 OU 特例得一般唯一性，质疑充分可操作边界条件 |

**注意:** Wang, Xu & Wang (2008), [“Potential landscape and flux framework of nonequilibrium networks”](https://doi.org/10.1073/pnas.0800579105), 是 **Jin Wang / Li Xu / Erkang Wang** 的邻近理论，不是 Ping Ao 著作；可作最强比较者，不可冒名归属。

## 2. Layer A — source-native substantive claims

### A1. AO04: 势函数不是预先摆在那里

AO04 摘要的主张，是从具有非线性漂移项及随机驱动的 SDE 出发，通过动力学结构／坐标形式构造 potential 及相关量，而不是简单在先验给定的山谷间撒随机噪声。公开摘要说明该构造不要求先用 Fokker–Planck 方程求出结果。

**来源限度:** “构造可行” ≠ 任意高维系统在任何光滑性、噪声解释、边界条件下均有唯一且观测上可识别的全局势函数。AO04 的数学假设和算法适用域不能凭摘要补造。

### A2. AO05: 非平衡演化有四个成分和层级接口

AO05 出版社摘要明确提出四个成分：**ascendant matrix（ascendancy/dissipative side）**、**transverse matrix（非梯度/横向 side）**、**Wright evolutionary potential**、**stochastic drive**，并把某一层级的描述同上下层及确定性／随机性来源相联系。其研究纲领并不局限于“扰动帮助系统跳过固定山峰”。

这里“三条 Darwinian laws”是作者提出的研究形式体系；将其认作自然界已充分验证的普遍三定律**不受来源与本卡支持**。该工作使用连续状态／时间描述，因此离散选择与微观实际化不能自动视为已经得到完整解释。

### A3. AO07/AO09: 景观是由动力学建模取得的有效表征

AO07 研究 SDE 变换、相关不变量，以及与 Itô、Stratonovich 随机积分框架的区别。AO09 从生物网络研究角度，强调适应景观对于 phage lambda 遗传开关、稳健性及生物网络稳定态的量化用途。

这直接压制“AO 只是在不变已知景观上加噪声”的弱比较。**但**“景观由模型动力学构造”并不自动等于 SRT 的原初 Selection 生成差异／生成对象化边界。

### A4. AO17R: 非平衡系统仍可能具有势与非梯度分量

2017 *Frontiers of Physics* 摘要明确把随机动力学分解成**耗散**、**破坏详细平衡的分量**以及具有双重解释角色的**势景观**，并主张一种区别于通常 Itô/Stratonovich 的 **A-type stochastic interpretation**。作者还就分解**唯一性**提出正面主张。这些是来源自身的立场，而非学界共同定论。

**数学表示说明（M 摘述，仅示意，不是本卡独立复证的逐式原文）:** 研究常以形成后的状态空间 \`x\` 与漂移 \`f(x)\`、扩散 \`D(x)\` 为起点，把作用分成散逸/非梯度及景观项。必须说明 SDE 随机积分解释、噪声强度、状态和边界条件；不能把一个势函数直接升级为 ontic Selection 或 SRT 的 \`Ψ_f\`。

### A5. AO17E: 高维强噪声的可计算和可检验输出

公开全文的可复核锚点：

- **Abstract / Introduction:** 面向非详细平衡、乘性噪声及高维系统，在特定 A-type 解释和 least-action 框架下计算稳定态相对概率而不完整模拟稳态分布。
- **Results — “Deviation between ODE and SDE” / “Bridging ODE and SDE”:** 对比通常随机积分解释下的 ODE/SDE 稳定点与拓扑差异，并声明所用 \`f(x)\`、\`G(x)\` 和扩散矩阵 \`D(x)\`；这**不是**只处理预先固定势阱。
- **Abstract / 38-dimensional cancer network application / Discussion:** 将模型用于一个 **38 维前列腺癌网络模型**，考察噪声强度改变如何影响若干细胞状态的相对概率／迁移预期；这是**模型结果及医学方向候选**，并非临床治疗已验证有效。
- **Discussion:** 作者明确指出随机积分解释的选择、漂移调整、在经验生物模型中区分决定性与随机性力可能没有唯一物理意义；SDE 或 CME 都具有适用范围／模型误差，低 copy-number 情形对离散 CME 的依赖不可忽略。这一自我限度必须与方法宣称一起读。
- 2019 出版社有 correction / update 标记，任何严格复现应检查修订与补充材料版本。

## 3. The 2016 existence/uniqueness controversy — not a settled theorem by citation

| 问题 | Zhou & Li 2016 | Yuan, Tang & Ao 2016 / review | Zhou & Li response |
| --- | --- | --- | --- |
| 景观理论关系 | 对比稳态分布势、FW 准势、Ao 分解积分，并讨论局部/全局势与跃迁路径 | 不否认应区分来源／解释，但认为推导中存在非唯一性误判 | 继续捍卫不同构造的数学区分 |
| 是否普遍唯一 | 声称可证明存在，**一般情形不唯一** | 声称在适当条件下唯一，并以 OU 等类回应 | 认为 OU 例子不能证明原定义下的一般唯一性，边界条件不够可操作 |
| 本卡可裁定范围 | **争议本身已核定存在**；不宣称数学哪一方最终获胜 | 同左 | 同左 |

**实用结论（M）：** 对 SRT 借用 Ao 构造时，必须列明定义域、噪声解释、状态坐标、边界条件、数值算法和可辨识性；不要假设从观测到的 \`f,D\` 就能唯一复原“真实景观”或“实际 Selection”。“A-type = objective Nature's only stochastic rule” 同样不能由本来源包推广成全称本体主张。

## 4. Source provenance, limitations, literature disambiguation

- 2004、2005、2007、2009 是出版社**摘要级／局部预览**；据此能够准确报告研究目标和作者宣称，但不能承担严格定理完整条件、具体算法复现或跨领域统一性的负担。
- AO17R 作为 **Ao 共同作者综述**，在唯一性争论上并非中立裁判；必须与 ZL16/YTA16/ZL16R 并读。
- AO17E 是**公开全文可读**的主要本轮应用锚点；其数值示例和癌症模型为方法可行性展示，不是直接的临床验证，也不是 SRT 对应实验。
- 避免混称：\`fitness landscape\`（演化适应度的模型对象）、\`potential landscape\`（SDE 势的模型对象）、\`FEP/free energy\`（另一形式体系）、SRT L2 \`landscape\`（有界对象化）没有未经证明的一一同义关系。
- 外部论文的 \`selection\` 通常是 Darwinian / stochastic / state-level 转变的语境，**不等于** SRT 具有无预设备选菜单的原初 Selection；名词一样不能作为本体同一性依据。

## 5. SRT relevance — downstream interpretive pointer only (M)

- **O-track**: 支持对非平衡形成后系统的稳定、非梯度流、路径、滞后及随机扰动进行模型化比较；它可以是横向对象化的**有效 L2 研究脚手架**，但不能作为 SRT 本体定义。
- **D-track**: **NO CLAIM**，尚无任何对 Ao、FW、Wang/flux 或 adaptive landscape 的同目标、同观测、前瞻且公平的 SRT 优势证据。
- **Reverse constraint**: 已知动力学模型并非都在固定景观中随机选；SRT 不能以“他人只有重加权、SRT 才使景观变化”作全称创新论据。
- **Open ontology gap (not demonstrated):** 在观察变量、模型边界、作用位置和等价关系形成／重切分本身成为被解释对象时，哪些可由位置／历史条件动力学吸收，哪些另有可检验的生成负担？问题是开放的，**不是已发现的未被 Ao 覆盖机制**。
- **Suggested landing**: [bounded same-target audit](../../Operations/Audits/SRT_AO_POTENTIAL_LANDSCAPE_SAME_TARGET_VALUE_AUDIT_2026-10-10.md); no Core_Law or manuscript rewrite. Material Log is the only official B-class revival route.

## 6. Source-level conclusion

Ao 的研究是对 SRT 势景观类比最直接、最有方法价值的**成熟强邻居之一**。它**不只是“随机扰动”**，有状态动力学、耗散／横向分解、势函数构造、非详细平衡和应用层预测。当前最可靠的价值在于**模型接口、边界条件、数学争议压力和对 SRT 比较说法的反向修正**。迄今没有论文提供 SRT 原初 Selection 的经验验证，也没有本卡证明 Ao 的方法无法表达动态差异重组。

本卡保持 source-derived 主张与 M 映射分层，不引入新的 primitive、唯一性法则或“敖平被 SRT 吸收/否定”的结论。
