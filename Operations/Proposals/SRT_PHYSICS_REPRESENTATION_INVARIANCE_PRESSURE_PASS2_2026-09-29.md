---
id: SRT-PHYSICS-REPRESENTATION-INVARIANCE-PRESSURE-PASS2-20260929
type: proposal
status: draft
canonical: false
layer: operations
epistemic_layer: bridge
claim_mode: audit
created: 2026-09-29
updated: 2026-09-29
research_mode: U
root_question: "当同一物理过程允许不同表示、不同监测展开、不同参考系或非固定因果顺序时，SRT 对 Selection / actuality / history / position 的哪些负担必须保持不变，才能避免把描述方式误当成本体事件？"
working_label: "representation-invariant / covariant core — working label only; not hardened SRT term"
comparative_claim: none
named_comparator: "n/a — U-mode pressure mapping only"
n_mode_triggered: false
dependency:
  - Operations/Proposals/SRT_PHYSICS_THEORY_ADVANCEMENT_WORK_PACKAGE_2026-09-29.md
  - Physics/SRT_Physics_Claim_Status.md
  - Physics/Extensions/SRT_Phys_E01_Quantum_Instrument_Bridge.md
  - Physics/Extensions/SRT_Phys_E02_Quantum_Reference_Frames_Bridge.md
  - Physics/Extensions/SRT_Phys_E03_Information_Thermodynamics_Bridge.md
  - Physics/Extensions/SRT_Phys_E04_Relational_Time_Bridge.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_REVERSIBLE_ACTUALITY_SELECTION_2026-09-27.md
  - 01_Source_Intuition/SRT_AUTHOR_REENTRY_IRREVERSIBILITY_GLOBAL_RESIDUE_PASS1_2026-09-06.md
  - Core_Law/SRT_Generative_Ontology_Spine.md
tags: [Physics, RepresentationInvariance, QuantumTrajectories, Unravelling, QRF, CausalOrder, Landauer, QuantumDarwinism, SpinePressure]
---

# Physics Pass 2 — representation invariance / event individuation / order pressure

> 角色：这是 #1089 之后的第二轮物理域 noncanonical pressure pass。目标不是继续扩写 SRT 物理学，也不是增加新的量子解释，而是反向检查：当成熟物理理论允许多种等价表示、监测展开、参考系或因果顺序时，SRT 当前 bridge 是否把表示依赖内容误写成了唯一物理事实；哪些压力属于 Physics-local debt，哪些可能需要未来 Spine 明确处理。
>
> 边界：不改 canonical、STATUS、CURRENT NEXT、Physics owner 或 E01–E04。本文件只做 source-fidelity + reverse-pressure mapping。物理仍是“允许但不特权”的压力域。

---

## 0. 本轮与 #1089 的关系

#1089 已处理 T-PHYS-1、Local Friendliness、Quantum Darwinism source ownership、IRR-B 与 thermodynamic arrow 的非同一、E05 的 d-proxy 问题，以及 PHR-A 的覆盖边界。

本轮不重复这些内容。新增根问题是：

~~~text
如果物理描述本身可以变化，
哪些 SRT-side 结构仍必须保持不变，
才能把真实 occurrence
与 representation / monitoring / frame choice 区分开？
~~~

本轮形成四个主压力面：

1. event individuation vs quantum-trajectory unravelling；
2. position-relative description vs QRF covariance / invariants；
3. generative precedence vs temporal / causal order；
4. record / learning / erasure / dissipation 的热力学拆分。

第五个补充压力是：memory / history 并不单调推出 public objectivity。

---


## 1. P2-PHYS-1 — quantum unravelling pressure：dilation 不等于唯一 trajectory

### 1.1 外部事实

开放量子系统的同一个 GKLS / Lindblad master equation 可以有不同的 quantum-trajectory unravellings。Brun (2002) 明确用不同环境监测方案展示同一 master-equation evolution 的不同 unravelings；Donvil & Muratore-Ginanneschi (2022) 则给出更一般的 time-local master-equation trajectory framework。

因此：

~~~text
same unconditional / ensemble dynamics
!= unique conditioned trajectory decomposition.
~~~

更重要的是：

~~~text
fixed system-environment dilation / coupling
!= unique unravelling

dilation + chosen environment monitoring / record channel
-> conditioned trajectory family
~~~

也就是说，Stinespring dilation、GKLS representation 与具体 monitored trajectory 不能混作一个对象。

### 1.2 对 E01 与 F-E01-γ 的更精确诊断

E01 §2.4 的问题不宜概括为“dilation 本身不唯一”。E01 §5.3 的 F-E01-γ 其实已经加入限定：

> the physical GKLS unraveling is unique once the apparatus is fixed.

真正的缺口是：**apparatus fixed 并没有自动固定 environment monitoring basis / detection scheme；同一 system-environment coupling 可以因 photon counting、homodyne/heterodyne 等不同环境监测而产生不同 conditioned unravellings。**

因此 F-E01-γ 目前存在两种读法：

~~~text
A. apparatus = full monitoring / record scheme
   -> uniqueness 近乎由定义给出，窗口容易变得平凡；

B. apparatus = system + reservoir / dilation only
   -> uniqueness 不成立，因 monitoring choice 仍可改变 unravelling。
~~~

未来若保留这个窗口，必须先明确 apparatus boundary 是否把 detector basis、record channel 与 monitoring protocol 全部冻结。

### 1.3 解释依赖边界

“没有实际 monitoring / record channel，就不能从 standard-QM master equation alone 选出唯一 ontic jump sequence”只在标准 quantum-trajectory / measurement reading 下成立。

objective-collapse theories（如 GRW / CSL）正是把 stochastic collapse dynamics 作为额外物理定律，而不是把 trajectory 仅视作 conditioned monitoring description。因此本包不把“无监测就无 ontic trajectory”写成 interpretation-neutral 结论。

### 1.4 对 PHR-A 的影响

PHR-A 的 event audit 仍比 E01 的 uniqueness claim 稳健，因为它预先要求 event unit / boundary / interpretation 和 outcome-indexed physical record。

更稳妥的压力读法是：

~~~text
within standard monitored-QM readings:

PHR-A candidate event
= instrument / monitoring / record-context indexed

formal or unrecorded unravelling
!= ontic event decomposition by default
~~~

因此：

- trajectory-level event 若要进入 PHR-A，应把实际 detector / monitoring / record apparatus 纳入 event boundary；
- master-equation-level dynamics 不能独自决定哪条 stochastic trajectory 是真实 Selection 序列；
- primitive Selection 不能直接等同于任意 formal quantum jump；
- objective-collapse 路线必须作为另一个明确标注的 interpretation / theory family 处理。

### 1.5 Disposition

~~~text
E01 / F-E01-γ
= PHYSICS-LOCAL DEBT candidate, after retyping the problem
  from "dilation uniqueness"
  to "dilation / apparatus / monitoring / unravelling conflation"

PHR-A record-context rule
= strengthened, not defeated

SPINE-impact candidate
= event individuation must distinguish
  representation choice
  from physically instantiated monitoring / record-context
~~~

## 2. P2-PHYS-2 — QRF pressure：位置相对不等于所有东西都相对

### 2.1 外部事实

Giacomini, Castro-Ruiz & Brukner (2019) 的 QRF formalism 区分：

- quantum state / superposition / entanglement 可随 reference frame 改变；
- measured systems 与 observables 会随 frame transformation 改变；
- 对应变换后 observed probabilities 保持 invariant；
- physical laws 需要满足扩展 covariance。

成熟的无绝对外部参考系理论因此不是只说：

~~~text
everything is observer-relative
~~~

而是同时给出：

~~~text
frame-relative descriptors
+ transformation law
+ invariant empirical content
~~~

### 2.2 E02 已经做对了一半

E02 已经正确引入 unitary QRF transformation、frame-relative superposition / entanglement 和 invariant-structure bridge，所以 QRF 不是本轮新发现的邻居。

真正的问题是，E02 有若干句子把 frame relative 太快翻译成 SRT actuality / embodiment 结论，例如：

- manifest classicality is frame-relative；
- which frame an embodied selector actually occupies is not arbitrary；
- frame-maintenance / hierarchy 的若干 falsifiability windows。

这些是 SRT-side bridge proposals，不是 QRF 文献本身给出的结果。

### 2.3 Future structural burden

如果 SRT 坚持 position-indexed actuality，未来至少要区分：

~~~text
A. descriptor-relative
   state / subsystem split / superposition / entanglement 随 frame 变化

B. transport / covariance rule
   不同 position 之间什么结构允许合法搬运

C. invariant burden
   哪些可观测关系 / probabilities / physical constraints
   在合法 frame transformation 下必须保持
~~~

因此：

> 没有 God-view 本身不够。位置论还要回答：不同 position 之间哪些东西可以变，如何变，以及什么不能随意变。

这不是要求现在建立新的 SRT transformation group，只是把未来 Spine 的 burden 写清楚。

### 2.4 对 fact relativity 的后续含义

#1089 已指出 Fact Relativity Theorem 过强。

本轮增加：

~~~text
fact / actuality relative
!= covariance / invariant structure absent
~~~

如果 actuality 最终被写成 position-relative，仍需要说明跨 position 的合法 transport / alignment 条件，而不能把 L2 convergence 简化成不同观察者最后说同一句话。

Future question：

> cross-position convergence 是内容相同，还是不同位置之间存在可追踪的 transformation / transport relation？

### 2.5 Disposition

~~~text
QRF frame-relativity explanatory job
= SOURCE-OWNED AT THIS EXPLANATORY JOB

E02 QRF bridge
= useful but partly overclaims SRT-specific consequence

SPINE-impact candidate
= position-indexing requires
  relative content + transport rule + invariants
~~~

---


## 3. P2-PHYS-3 — generative precedence / history / One formation 与 causal order 的真实压力

### 3.1 外部压力必须限域

indefinite causal order（ICO）/ quantum switch 文献研究的是操作 / process 的 causal order；在 process-matrix / quantum-switch 类形式中，某些 operations 不能被赋予一个固定经典顺序。Rozema et al. (2024) 的综述同时明确讨论实验实现、认证与解释问题。

因此本包只使用以下有限压力：

~~~text
some quantum process descriptions
need not admit one fixed classical operational causal order
~~~

不推出：

- 时间不存在；
- 所有物理事件都没有先后；
- SRT 的 history / One 已被 ICO 反驳；
- quantum switch 给出了 ontology；
- 当前实验已经无争议地证明一种唯一 metaphysical reading。

### 3.2 对 Spine 的原判断需要反向修正

上一版把 Spine 的 typed structural map 直接记为 OWNER-CONFIRMED ALIGNMENT，这个结论过强。

Spine §1 的确说它不是“每个 Selection 都必须经过每个 branch/stage”的统一阶梯；但 Spine §4、§5、§6.2 又明确使用：

~~~text
prior Selection
later Selection
organization_t
Selection_(t+1)
later manifestation / selectability
~~~

因此 current Spine 仍然包含有方向的 before/after burden，尤其用于：

- retained historical efficacy；
- recurrent self-conditioning；
- One formation；
- formed-position anticipation。

ICO 并不能直接否定这些负担，因为 operational causal order 与 ontological / historical order 不是同一个概念；但它确实暴露了一个尚未完成的 order-typing 问题：

> **Spine 的 prior/later、t/t+1 到底表示哪一种顺序：coordinate time、clock order、causal precedence、state-index order，还是更抽象的 generative / constitutive dependence？**

所以这里应记为 SPINE PRESSURE / OPEN，而不是 alignment pass。

### 3.3 为什么这个压力仍与 Selection 有关

E04 B-E04-4 只谈“不可逆 Selection 与 clock-reading transitions 的对齐”；quantum-switch 等典型 ICO 实验本身主要是相干过程，因此不能直接用它们去反驳 B-E04-4。

连接点来自 2026-09-27 作者裁决：

~~~text
genuine actuality
+ deterministic / reversible dynamics
-> may still be primitive Selection

reversibility
!= Selection exclusion criterion
~~~

因此，如果某些可逆 / coherent actuality 也可以属于 Selection，那么“Selection 的 generative status”原则上不能只靠 classical irreversible event ordering 来承载。这里的压力是：

~~~text
primitive Selection admission may extend beyond
irreversibility-marked clock events

therefore
Selection order
cannot be silently identified with
irreversible clock-event order
~~~

### 3.4 对 E04 的限定性诊断

E04 的问题不是 Page–Wootters / relational-time 本身，而是一些更强的 SRT-side identification：

- selection events are clock-readings；
- B-E04-4 把 irreversible Selection event 与 clock-reading transition 对齐；
- selection-index reading 被写成可由 clock-event sequence 保存。

这些可以继续作为 bridge hypothesis，但不能承担“所有 Selection 的 order structure”。

### 3.5 Disposition

~~~text
ICO / quantum-switch explanatory work
= SOURCE-OWNED; interpretation-sensitive at the metaphysical level

current Spine
= SPINE-IMPACT OPEN, not OWNER-CONFIRMED ALIGNMENT

E04 selection-index / clock-reading identification
= DOMAIN-LOCAL BRIDGE DEBT candidate

future skeleton question
= what type of order is required by
  history / recurrence / One formation,
  and when is that order physical time or causal order?
~~~


## 4. P2-PHYS-4 — information acquisition / record / learning / erasure / dissipation 必须拆开

### 4.1 E03 的 scope caveat 从顶部就已经混入了 record stabilization

E03 开头一方面正确声明：

- Landauer 主要约束 erasure / reset；
- arbitrary measurement / Selection 不自动受 Landauer bound；
- Psi_f 只是 projection / proxy。

但同一个 caveat 又把 stable-classical-record stabilization 与 erasure / reset 并列。B-E03-1 随后进一步把 latching a pointer state / committing an outcome to classical memory 一并写入 k_B T ln 2 per bit produced 的下界。

这一步并没有由 Landauer principle 自动给出。

更准确的拆分是：

~~~text
information acquisition
!= measurement
!= record formation / writing into available memory
!= learning
!= logical erasure / reset
!= thermodynamic dissipation
~~~

在可逆实现中，measurement / information acquisition 本身可以原则上不要求正的最小 work cost；真正标准的 Landauer burden 落在 logical erasure / reset / many-to-one compression。若记录写入空白 memory 后永不重置，并不能仅凭“产生了一条记录”推出 k_B T ln 2 的最低耗散；闭合循环、复用 memory 时的 reset 才把账重新带回来。

Zhao–Zhang–Preskill (2026) 进一步给出一个现代量子信息例子：learning 可以被提升为 fully reversible，本身没有 fundamental energy cost，而学习所得知识会改变后续 erasure 的最优成本。

### 4.2 E03 的 Jarzynski / Crooks substitution 仍是高置信度 debt

B-E03-2 把 Jarzynski equality 直接写成 SRT selection-work identity；B-E03-3 又把 L0 -> L1 forward Selection 与 L1 -> L0 reconstruction 称为 exactly the Crooks asymmetry。

但 E03 并没有从 SRT owner 中导出：

- 严格定义的 W_select；
- L2 stable subspace 的 thermodynamic free energy；
- SRT forward/reverse path ensemble 与 Crooks protocol ensemble 的同一性。

因此：

~~~text
Jarzynski / Crooks
= source-owned thermodynamic results

direct SRT variable substitution
= NOT EARNED by inheritance alone
~~~

同理，no free selection 不能作为 universal physical principle 由这些等式直接推出。

### 4.3 对 IRR-B 的关系应直接回到 9-06 作者源

2026-09-06 IRR-B 作者源已经明确列出未授权项：

~~~text
mandatory thermodynamic entropy increase for every Selection: NO
Landauer cost as the universal residue: NO
~~~

因此本轮无需借 Landauer 去“拯救” IRR-B，也不应把 E03 当作 T-PHYS-1 的 closure。

### 4.4 Disposition

~~~text
E03 record-stabilization -> Landauer wording
= PHYSICS-LOCAL DEBT, medium-high confidence

E03 Jarzynski / Crooks SRT substitutions
= UNDERIVED BRIDGE IDENTIFICATION, high confidence

IRR-B != Landauer / entropy rescue
= already author-guarded on 2026-09-06
~~~


## 5. P2-PHYS-5 — Quantum Darwinism 只提供“可分离”的存在性压力，不直接映射 SRT history

### 5.1 External result

Galve, Zambrini & Maniscalco (2016) 在一个具体 microscopic open-system model 中显示：environment 的 non-Markovian information backflow / memory effects 可以妨碍 Quantum Darwinism 所需的 redundancy 与 classical objective records。

这支持一个 source-native 结论：

~~~text
in that model:
environmental memory / information backflow
can reduce Darwinian redundancy / objectivity
~~~

### 5.2 不把 environment memory 直接等同 SRT retained history

上一版从这个结果直接写：

~~~text
more memory / history dependence
!= automatically more public objectivity
~~~

方向上有启发，但类型映射过快。

Quantum Darwinism 里的 non-Markovian memory 指的是 system-environment information backflow / dynamical memory；SRT 的 retained historical efficacy 指 prior Selection remaining materially effective in later Selection conditions。两者不是同一个变量，也没有在本包中建立一一对应。

因此本轮只保留：

> **一个成熟物理模型给出了 memory-like dynamical dependence 与 public redundancy 可以分离的存在性例子；它可以压力测试任何把 history / memory 单调等同 objectivity 的一般叙述，但不能直接证明 SRT history 如何作用。**

### 5.3 对 SRT 的实际用途

SRT 自身的 author-reentry problem field 已经把：

~~~text
history / sedimentation
order / convergence
objectification / public representation
~~~

列成不同问题轴；Spine 也没有把 retained history 直接定义成 public objectivity。

因此 Galve 2016 的最合适处置是：

~~~text
Quantum Darwinism mechanism
= SOURCE-OWNED

Galve 2016
= model-specific separation / pressure example

direct "physics reciprocal constraint on SRT history"
= NOT EARNED

useful guard
= do not collapse history / convergence / objectification into one monotonic variable
~~~


## 6. 本轮最重要的新压缩：representation-invariant / covariant core（working label）

> **Term guard**：representation-invariant / covariant core 只是本轮的 working label，用来指一个待处理 burden；它不是新的 SRT term-of-art，不进入 Glossary，也不在此文件中获得 owner / definition。

前五节可以压缩成一个比 #1089 更上游的问题：

~~~text
当我们改变
- trajectory unravelling / monitoring scheme
- quantum reference frame
- clock / temporal reference
- causal-order representation
- thermodynamic bookkeeping / information partition

SRT 所称一次真实 Selection / actuality 中，
什么必须保持不变，
或者必须通过什么 lawful covariance / transport relation 保持关联？
~~~

目前至少不能未经论证就把以下任一项当作 primitive core：

- specific Hilbert-space factorization；
- superposition vs non-superposition label；
- one chosen standard-QM quantum-trajectory unravelling；
- one clock coordinate；
- one classical operational causal order；
- Landauer dissipation magnitude；
- one observer's raw outcome vocabulary。

开放方向至少有两种：

~~~text
A. there is some representation-invariant burden

B. Selection / actuality is intrinsically indexed,
   while lawful transformation / covariance relations
   connect indexed manifestations
~~~

本包不裁决 A / B，也不假设二者互斥。


## 7. 对未来 Spine / canonical update 的分类

### A. Physics-local debt — 分级而不是打包高置信度

| Debt | Confidence | Why |
|---|---|---|
| E03 Jarzynski / Crooks direct SRT substitution | **HIGH** | source equations do not by themselves derive W_select, Delta F_L2, or L0/L1 path-ensemble identity |
| E03 Landauer record-production / stabilization wording | **MEDIUM-HIGH** | erasure/reset burden is standard; record writing / latching does not automatically inherit the same lower bound |
| E01 / F-E01-γ unravelling uniqueness | **MEDIUM-HIGH after retyping** | problem is apparatus/dilation/monitoring/unravelling conflation, not simply dilation non-uniqueness |
| E04 selection-index / clock-reading alignment | **MEDIUM** | pressure depends on distinguishing primitive reversible Selection from the irreversible-event subset targeted by B-E04-4 |

### B. SPINE-IMPACT CANDIDATES

1. Event individuation：representation choice 与 physically instantiated monitoring / record-context 如何区分；
2. Position transport：position-relative actuality 若保留，需要什么 transformation / transport + invariant burden；
3. Order typing：Spine 的 prior/later 与 t/t+1 究竟是哪种 order；
4. History / convergence / objectification separation：保持三个 burden 不自动合并。

### C. E05 debt propagation map

#1089 已单独指出 F-E03-γ 的 canonical-d proxy 问题。本轮再记录 bridge debt 如何传播到 E05：

| E01–E04 debt | E05 inherited window | Propagation |
|---|---|---|
| E01 apparatus/dilation/unravelling conflation | **F-E01-γ** | apparatus fixed -> unique physical unravelling 的 falsification premise 需先重写，否则可能平凡或设定不清 |
| E03 underived SRT residual / information split | **F-E03-α** | SRT residual 在实验前缺少独立 derivation，不能把 base-theory saturation 自动算作 SRT falsification |
| E03 Landauer record-stabilization overreach | **F-E03-β** | residual / non-saturation claim 需限定到真实 reset/erasure task，而非 bare record writing |
| E03 d / dissipation and record-cost assumptions | **F-E03-γ** | 除 #1089 的 canonical-d proxy debt 外，还继承 Landauer/record scope debt |
| E04 irreversible-selection / clock-reading alignment | **F-E04-γ** | window 只能测试那个 bounded bridge hypothesis，不能代表 primitive Selection 的 universal order |

F-E04-α / β 主要测试 relational-clock / interacting-clock source theory，当前发现不要求一并撤销，但其 SRT-specific positive direction 仍应与 source-owned prediction 分开。

### D. SOURCE-OWNED / NO LOCAL COMPARATIVE INCREMENT

- quantum trajectory / monitored-unravelling formalism；
- QRF covariance；
- indefinite causal-order / quantum-switch formalism；
- Landauer / Jarzynski / Crooks / information thermodynamics；
- Quantum Darwinism redundancy mechanism。

### E. PARKED

继续保持停放：

- SRT-specific collapse mechanism；
- gravity = Psi_f；
- Planck Selection tick；
- exact constant derivation；
- Born-rule intentional bias；
- physics proves Selection primitive。


## 8. 本轮不要求作者立即裁决

本轮暂不要求作者形成新理论答案。

未来进入 Spine / bridge tightening 前，至少有三项待处理输入：

1. 是否把 position-relative actuality 的 transformation / covariance burden 纳入未来 Spine OPEN map；
2. 是否授权一次 Physics B-class cleanup，对 E01–E05 中上述过强句式与窗口做系统收紧；
3. **Spine 的 history / recurrent One formation 是否预设了确定的时间先后？** 如果不是，prior / later / t -> t+1 应由哪一种 order 类型承载？

第 3 项目前只登记为 future Spine question，不在本 PR 内裁决。


## 9. External source status for this pass

> 这里的 checked 分两层：bibliographic identity / publication metadata 与 claim-level use。前者已核；后者只按本包实际使用的 bounded claim 核对，不把整篇文献当作 SRT 支持。

- **Giacomini, Castro-Ruiz & Brukner (2019)** — QRF covariance / frame-relative description source；既有 E02 primary anchor。
- **Brun (2002), A simple model of quantum trajectories** — checked for the bounded point that different monitoring schemes can correspond to different unravelings of the same master-equation evolution. DOI: 10.1119/1.1475328.
- **Donvil & Muratore-Ginanneschi (2022)** — checked for general time-local master-equation trajectory framework. Nature Communications 13, 4140. DOI: 10.1038/s41467-022-31533-8.
- **Van Regemortel et al. (2022)** — retained as a monitoring-induced trajectory / entanglement example；not used alone to establish the general uniqueness claim.
- **Rozema et al. (2024)** — checked for the bounded process-level ICO claim and for the fact that interpretation / experimental-certification questions remain part of the field. Nature Reviews Physics 6, 483–499. DOI: 10.1038/s42254-024-00739-8.
- **Zhao, Zhang & Preskill (2026)** — publication metadata independently verified: npj Quantum Information 12, Article 137；DOI: 10.1038/s41534-026-01273-4. Used only for the bounded result that learning can be made fully reversible with no fundamental energy cost itself and that knowledge changes erasure cost.
- **Galve, Zambrini & Maniscalco (2016)** — checked as a model-specific result: non-Markovian information backflow / memory effects hinder Quantum-Darwinist redundancy in their microscopic model. DOI: 10.1038/srep19607.
- **Landauer / Bennett / Sagawa-Ueda / Jarzynski / Crooks** remain E03's source-native anchors. This pass uses them to police scope, not to derive SRT variables.

## 10. Stop condition

本轮到这里停止。

不在此 PR 内：

- 修改 E01–E04；
- 修改 Physics Claim Status；
- 修改 canonical / Spine；
- 新增 Physics CURRENT NEXT；
- 建立新的 SRT-specific physical mechanism；
- 把 representation-invariant core 写成已解决的定义。

下一步如继续 Physics，只能是：

~~~text
independent content review / source-fidelity review of this pass
OR
future author-authorized B-class Physics bridge cleanup
~~~
