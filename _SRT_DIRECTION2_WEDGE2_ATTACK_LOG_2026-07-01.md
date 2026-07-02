---
id: SRT-DIRECTION2-WEDGE2-ATTACK-LOG-2026-07-01
type: attack_log
tags: [Direction2, Wedge2, AttackLog, DistributionalPayability, MoralHalf, Simulation, Pilot, NotValidation, Seed]
status: attack_log_v0
layer: meta
epistemic_layer: research_program
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
created: 2026-07-01
provenance: 对已合并的 `_SRT_DIRECTION2_WEDGE2_SIM_RESULTS.md` 的自我攻击(route-b 建构-攻击式复审),产出下一步实验方向设计(2a/2b),不运行新仿真、不改写 Wedge 2
candidate_promotion_target: none(残余仅供未来 2a/2b 实验设计参考;不喂入 Core/SRT_OPEN_TENSIONS.md)
dependency: [SRT-DIRECTION2-WEDGE2-SIM-RESULTS, SRT-DIRECTION2-WEDGE1-SIM-RESULTS, SRT-DISTRIBUTIONAL-PAYABILITY-CANDIDATE-SEED, SRT-D3-OPTION-SPACE-READOUT-NOTE, SRT-AUDITOR-INDEPENDENCE-CANDIDATE-NOTE, SRT-DIRECTION2-MORAL-GENEALOGY-SEED]
---

# Direction 2 · Wedge 2 攻击日志与下一步方向(2026-07-01)

> **文件地位(先读)**
> - **non-canonical / attack_log / research_note / pilot / proposal / not validation**。
> - **不改写** `_SRT_DIRECTION2_WEDGE2_SIM_RESULTS.md`(或任何其他已合并文件),**不运行任何新仿真**,**不新增任何 canonical 定义**。
> - 本文件只做一件事:对已合并的 Wedge 2 做一次自我攻击(route-b 的攻击段),并给出下一步实验方向(2a 参数稳健性扫描、2b 去人为化路线)的**设计**,不产出新结果。
> - **防火墙见 §8,起草前请先读**:本日志不证明 Wedge 2 错,只限定它当前能撑起什么、撑不起什么。

---

## 0. 一句话

> Wedge 2 给出了一个**可复跑的 toy-level 反事实检验接口**,让 distributional payability §2 的支撑/转嫁加固条件第一次能被数值化地测;但这个接口目前**只测了参数空间里的一个人为选定的点**,其中最要紧的一条不对称(B 的 effective g 更高)是**外生赋予**而非涌现的,且尚未证明这套框架相对标准 fairness/robustness 诊断有增量价值。本文件把这些限定精确列出,并设计(不实现)下一步的两条路线。

---

## 1. 攻击1——参数是否人为(1.8×、5× cost、80/20、THRESH=2.0)

**是,而且比 Wedge 2 §7 的"非拟合真实数据"免责声明本身承认的更单薄。** 那句免责声明只挡住了**外部效度**问题(真实系统是否如此);它没有挡住**内部效度**问题——Wedge 2 只在参数空间里跑了**一个点**,不知道 Result A / B 的定性模式在多大范围内成立、边界在哪里、是否对参数微调敏感到轻易翻转或消失。Wedge 1 对 `g` 做过完整扫描;Wedge 2 对 `UNDER_RESOURCE_MULT`、`COST` 比、`WEIGHT` 分割、`THRESH` **都没有扫描,只固定了一组数值**。这是一个真实的方法论缺口,不是免责声明能补上的。

---

## 2. 攻击2(最强攻击)——B 的 effective g 更高,是否把结论预设进了模型

**Result A 的核心模式,很大程度上由外生设定驱动,而非涌现发现。** `gB = g_platform × 1.8` 是**直接外生赋予**的假设;给定这个赋值,"B 先于 A 越阈"在很大程度上是**加权平均的算术推论**——B 被设定为更早被压平,A 占 80% 权重意味着聚合指标几乎必然被 A 主导、在 B 越阈后继续爬升。这一步**没有让读者看到"结构性劣势如何产生更早的 foreclosure",只是数值上确认了"被设定为更早 foreclose 的一方确实更早 foreclose"**。

Result B(反事实支撑关系)因为要经过实际的 bandit 学习动态(非线性),涌现成分略高一些,但其方向性结论仍然高度可由"COST_B > COST_A + B 更容易被压"这两个假设的组合预期到。

**这是目前最需要处理的攻击,§7(2b)直接针对它设计回应路线——但这不构成对 Wedge 2 的最终否定,只是限定它目前能证明什么(见 §8)。**

---

## 3. 攻击3——protected baseline(GB_CAP=7.0)是否选得讨巧

**是,这是一个真实的方法论污点。** `GB_CAP=7.0` 是在探索性扫描中**先看到 B_div≈2.4 这个"健康"结果之后倒推**选定的,不是从一个不依赖答案的独立原则导出的。更有辩护力的 protected baseline 应该是 `gB = gA`(B 不承受任何倍增,真正的形式平权),而不是一个为了让对比好看而反推出的数字。这个选择污染了 Result B 的说服力,应在未来复跑中改正。

---

## 4. 攻击4——这和普通的 fairness/robustness toy 有什么本质区别

表面上,"B 类在效率优化策略下结果更差,消除这个差距要付效率代价"与算法公平文献里标准的 **accuracy-fairness tradeoff**(disparate impact / equalized odds vs. accuracy)高度相似。

**诚实的判断**:**Wedge 2 当前尚未展示 reselectability / 可选空间框架相对标准 fairness 指标(如 outcome parity、error rate parity)的增量诊断力**——也就是说,它没有给出一个"标准 fairness 指标看起来健康、而 reselectability 已经先一步崩溃"(或反过来)的场景,来证明这套框架测到了标准指标测不到的东西。这**不等于**"这套框架只是换了一层马甲"——现在只是**未证明增量价值**,增量价值是否存在仍然开放,是 2a/2b 之后可以专门设计的检验。

---

## 5. 攻击5——Result B 的"支撑/转嫁"是否只是反事实检验,不能写成验证

对,而且比 Wedge 2 §6 承认的更该收紧一步。`agg_uniform > agg_protected` 在每个测试的 g 上都成立,**这本身不令人意外**,因为模型的函数形式保证了"更高 g → 更高 reward、更低 diversity → 更低 cost"这个方向——除非模型被专门构造成对该参数不敏感,否则改一个参数产生某种方向一致的差异,在很大程度上是模型构造本身的产物。这更接近"证明了这组方程按写定的方式运行",而不是"证明了支撑关系是一个非平凡的经验事实"。Wedge 2 §6 已经说"未支持:真实系统",但没有说清楚**这个反事实检验本身在多大程度上是从模型构造里免费得到的**——本条攻击把这一点补上。

---

## 6. Wedge 2a——参数稳健性扫描(设计,不跑)

**目的**:找到 Result A / B 的定性模式(B 先越阈、聚合掩盖、支撑关系为正)在参数空间里**成立的区域**,回应攻击1,而不是只报告一个点。

**扫描维度(候选,非最终清单;本节只是设计,不产出任何新数字)**:

1. `UNDER_RESOURCE_MULT ∈ {1.0(应验证结果消失), 1.2, 1.5, 1.8, 2.5}`。
2. `COST_B/COST_A ratio ∈ {1(无成本不对称), 2, 3, 5}`——**关键分解实验**:固定 `g` 不对称、关掉 cost 不对称,看 Result B 的支撑关系是否还成立;再反过来固定 cost 不对称、关掉 `g` 不对称,看 Result A 是否还成立。目的是拆出两个假设里到底哪一个在做因果功,而不是两个一起变、分不清谁的贡献。
3. `WEIGHT_B ∈ {0.05, 0.1, 0.2, 0.35, 0.5}`——测试"聚合掩盖局部越阈"这个说法是否只在 B 是小群体时成立。
4. `THRESH` 敏感性:结果对 `THRESH=2.0` 这个具体数值有多敏感。

**预期产出**:一张"在哪个参数子空间内,定性模式成立/消失/反转"的地图,而不是新的点估计——但**本文件不实现它,只记录设计**。

---

## 7. Wedge 2b——去人为化:让 foreclosure 内生涌现(设计,不实现)

**目的**:直接回应攻击2——不再外生赋予 `gB = g_platform × MULT`,而是让 B 的劣势通过更原始的结构性量组合**涌现**出差异化的 foreclosure,而不是把结论直接写进参数。

**候选机制(设计阶段,均未实现,均不构成任何结果)**:

1. **真实选项数不对称,而非引导强度不对称**:B 的选项场本身 `K_B < K_A`(B 真实可达的路径本来就更少),两类共用同一个名义 `g`,不做任何倍增。
2. **资源约束式的复核容量,而非直接压低 g**:引入一个"人工复核队列容量"参数,B 类每单位时间只能获得有限次真实复核(不管名义 g 多低),超出容量的案件被结构性地路由回自动化路径——foreclosure 从"容量约束 + 需求"的交互里涌现,不是外生乘数。
3. **观测噪声不对称**:B 的 reward 观测噪声更高(资源不足导致证据收集/材料核验更粗糙),使同一名义 g 下,B 的价值估计更不稳定、更容易过早收敛到少数选项——差异从学习动态本身涌现,而非从直接调高 B 的 g。

---

## 8. 防火墙(必须放在最显眼位置引用)

**本 attack log 不证明 Wedge 2 错。** 攻击的作用是**限定** Wedge 2 当前能撑起什么、撑不起什么,不是撤销它。

**Wedge 2 当前仍然拥有的真实贡献**:它给 distributional payability §2 的支撑/转嫁加固条件,提供了**第一个 toy-level 的可复跑反事实检验接口**——即"如何用数值化的方式问支撑关系问题"这件事本身是有价值的方法论产出,不因本攻击日志而作废。

**Wedge 2 目前只能支持**:
- 给定明确标注、非拟合真实数据的结构性不对称,分布违规模式**可被构造**;
- 支撑/转嫁关系**存在一个可运行的反事实检验接口**。

**Wedge 2 目前不能支持(禁句表)**:

- ❌ "真实 AI 治理/申诉系统存在或常见此模式"(未测,仍是 Wedge 2 §6 的未支持项);
- ❌ "1.8×、5× cost、80/20 等参数有现实依据"(§1——未扫描,选点未经稳健性检验,也未拟合任何真实数据);
- ❌ "B 更早 foreclose 是这个机制涌现出来的发现"(§2——很大程度上是外生设定的算术推论,2b 是回应它的方向,尚未实现);
- ❌ "reselectability 框架已证明相对标准 fairness 指标有增量诊断力"(§4——尚未展示,仍然开放);
- ❌ "Result B 的支撑关系是被验证的经验事实"(§5——是模型构造内的反事实检验,不是经验验证);
- ❌ "本攻击日志已经推翻或废弃了 Wedge 2"(见本节开头——它限定证明力,不撤销贡献);
- ❌ "2a/2b 已经执行或已有结果"(两者均只是设计,均未运行、未实现)。

---

## 9. 回链

- `_SRT_DIRECTION2_WEDGE2_SIM_RESULTS.md`(被攻击对象,本文件不改写它);
- `_SRT_DIRECTION2_WEDGE1_SIM_RESULTS.md`(Wedge 2 直接扩展的模型与方法论基准,攻击1 的参数扫描纪律即来自它);
- `_SRT_DISTRIBUTIONAL_PAYABILITY_CANDIDATE_SEED.md §2`(支撑/转嫁加固条件,Result B 试图操作化的对象);
- `_SRT_D3_OPTION_SPACE_READOUT_NOTE.md`(可选空间轨迹作为主证据,攻击4 讨论的"增量诊断力"即针对这个框架本身);
- `_SRT_AUDITOR_INDEPENDENCE_CANDIDATE_NOTE.md`(反事实基线构造者的独立性问题,Wedge 2 §4 已承认未处理,本文件不重复展开)。

---

## 10. 文件目标

本文件记录对已合并的 Wedge 2 的一次自我攻击:五个攻击点(参数人为性、结论预设风险、baseline 选点风险、与标准 fairness 诊断的区分度未证、支撑关系的反事实-vs-验证边界),以及两条尚未执行的下一步设计(2a 参数稳健性扫描、2b 去人为化/内生 foreclosure 路线)。它不新增仿真结果,不改写 Wedge 2,不新增 canonical 定义。Wedge 2 的真实贡献(toy-level 支撑/转嫁反事实检验接口)保持有效,只是证明力被本文件精确限定。任何"候选/proposal"措辞在被作者按 `Governance/SRT_EDIT_PROTOCOL.md` 采纳前,不得当 SRT 定论引用。
