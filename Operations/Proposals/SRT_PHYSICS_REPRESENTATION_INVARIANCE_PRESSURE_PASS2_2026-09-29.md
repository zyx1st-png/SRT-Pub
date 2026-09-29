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

## 1. P2-PHYS-1 — quantum unravelling pressure

### 1.1 外部事实

开放量子系统的同一个 GKLS / Lindblad master equation 可以有不同的 quantum-trajectory unravellings。

Van Regemortel et al. (2022) 展示：同一 master equation 下，不同环境监测方案可以产生不同 stochastic trajectories；监测方式甚至改变 trajectory-level entanglement，而 ensemble-averaged reduced dynamics 保持相同。

Donvil & Muratore-Ginanneschi (2022) 给出更一般的 time-local master-equation trajectory framework。

因此：

~~~text
same reduced / ensemble dynamics
!= unique trajectory decomposition.
~~~

trajectory / jump 序列并不是仅由 reduced master equation 唯一决定。

### 1.2 对 E01 的直接压力

E01 §2.4 当前说，若两组 jump operators 产生同一 reduced dynamics，physically actualized one 是与 actual friction reservoir 相匹配的 Stinespring dilation。

这比成熟邻居允许的内容更强。

更精确的关系应是：

~~~text
system + environment coupling
+ actual monitoring / record scheme
-> conditioned trajectory / unravelling

discard / ignore record
-> common unconditional reduced dynamics
~~~

如果 monitoring scheme 本身不同，不同 trajectory 对应不同 physical measurement contexts 的 conditioned descriptions。

反过来，如果没有实际 outcome record / monitoring channel 被物理实现，则从 master equation alone 选出一个真正发生的唯一 jump sequence 没有依据。

### 1.3 对 PHR-A 的影响

PHR-A 要求：

~~~text
predeclared event unit / boundary / interpretation
-> outcome-indexed physical record
-> intervention-sensitive path efficacy
-> future-access / return-cost change
~~~

这使 PHR-A 比 E01 的 unique actualized jump-set 更稳健。

Pass 2 建议：

~~~text
PHR-A candidate event
= instrument / record-context indexed

unrecorded unravelling
!= ontic event decomposition by default
~~~

因此：

- trajectory-level event 可以是物理的，但必须把实际 monitoring / record apparatus 纳入 event boundary；
- master-equation-level dynamics 不能独自确定哪条 stochastic trajectory 是真实 Selection 序列；
- primitive Selection 不能直接等同于任意 formal quantum jump。

### 1.4 Disposition

~~~text
E01 B-E01-3 unique physically-actualized jump-set wording
= PHYSICS-LOCAL DEBT candidate

PHR-A record-context rule
= strengthened, not defeated

SPINE-impact candidate
= event individuation must distinguish
  representation choice
  from physically instantiated record-context
~~~

---

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

## 3. P2-PHYS-3 — generative precedence != temporal / causal order

### 3.1 外部压力

indefinite causal order / quantum switch 研究表明，量子过程可以不具有一个固定经典操作顺序。Rozema et al. (2024) 对该实验 programme 做了系统综述。

这不意味着时间不存在、所有因果关系都不确定、SRT 被证实或 ontology 由 quantum switch 决定。

它只给出一个强约束：

~~~text
physical process structure
need not always admit one fixed classical operation order
~~~

### 3.2 对 Spine 的检查

当前 Generative Ontology Spine 已明确：

~~~text
Selection reality map
= typed structural map
!= universal ontic ladder / stage sequence
~~~

这一点与 ICO 压力相容，说明当前 Spine 比旧 Physics bridge 更稳。

### 3.3 对 E04 的压力

E04 仍保留较强 selection-index time language，例如：

- selection events are clock-readings；
- irreversible selection events align with clock-reading transitions；
- Selection-index 与 manifest time 绑定较紧。

这些句子容易把 generative relation 误读成 physical temporal ordering。

Pass 2 建议未来明确保持：

~~~text
generative / constitutive precedence
!= coordinate-time precedence
!= clock order
!= definite causal order of operations
~~~

因此：

~~~text
Selection occurrence
!= first temporal stage

history burden
!= universal second temporal stage

One formation
!= universally later microphysical event
~~~

Spine 当前已经朝这个方向走，主要 debt 在旧 bridge / pedagogical wording。

### 3.4 Disposition

~~~text
ICO explanatory work
= SOURCE-OWNED

current Spine typed-map guard
= OWNER-CONFIRMED ALIGNMENT

E04 selection-index / clock-reading identification
= DOMAIN-LOCAL BRIDGE DEBT candidate

future skeleton guard
= generative precedence must not silently become temporal or causal precedence
~~~

---

## 4. P2-PHYS-4 — record / learning / erasure / dissipation 必须拆开

### 4.1 E03 caveat 正确，但正文重新合并了它们

E03 开头已经正确说：

- Landauer 约束 erasure / reset；
- arbitrary measurement / Selection 并不自动受 Landauer bound；
- Psi_f 只是 projection / proxy。

但 B-E03-1 随后又写：

> classical-record-stabilization step ... must dissipate at least k_B T ln 2 per bit of classical record produced.

这把 record production / latching 再次滑回 erasure 的 Landauer 形式。

Landauer 的标准负担是 logical erasure / many-to-one reset。Bennett 路线也把 measurement 与 later memory erasure 区分开。

Zhao, Zhang & Preskill (2026) 进一步证明：学习可以提升为完全可逆过程，没有基础能量代价；知识会改变后续 erasure 的最优成本。

因此至少应保持：

~~~text
information acquisition
!= record formation
!= learning
!= logical erasure
!= thermodynamic dissipation
~~~

这些过程可以在具体装置里耦合，但不能默认同一。

### 4.2 E03 的更强 bridge overreach

B-E03-2 把 Jarzynski equality 直接写成 SRT selection-work identity。

B-E03-3 又把 L0 -> L1 forward Selection 与 L1 -> L0 reconstruction 称为 exactly the Crooks asymmetry。

但 E03 并没有从 SRT owner 中导出：

- 严格定义的 W_select；
- L2 stable subspace 的 thermodynamic free energy；
- SRT forward/reverse path ensemble 与 Crooks protocol ensemble 的等价关系。

因此：

~~~text
Jarzynski / Crooks
= source-owned thermodynamic results

direct SRT variable substitution
= NOT EARNED by inheritance alone
~~~

同理，no free selection 作为统一物理原则也过宽。

### 4.3 对 IRR-B 的意义

这加强了 #1089 的 guard：

~~~text
IRR-B
cannot be rescued simply by
every Selection costs entropy / Landauer dissipation
~~~

因为 measurement / learning / erasure / dissipation 的成本结构取决于具体任务与 memory architecture，而且 9-27 作者裁决已经禁止把 irreversibility 当作 primitive Selection admission rule。

### 4.4 Disposition

~~~text
E03 Landauer record-production wording
= PHYSICS-LOCAL DEBT candidate

E03 Jarzynski / Crooks SRT substitutions
= UNDERIVED BRIDGE IDENTIFICATION

IRR-B != Landauer / entropy rescue
= strengthened guard
~~~

---

## 5. P2-PHYS-5 — history / memory does not monotonically create objectivity

### 5.1 External pressure

Quantum Darwinism 用环境中的冗余可访问记录解释 classical objectivity。

Galve, Zambrini & Maniscalco (2016) 在一个开放系统模型中显示，non-Markovian information backflow / memory effects 可以阻碍 Darwinian redundancy 和稳定 objective records。

因此：

~~~text
more memory / history dependence
!= automatically more public objectivity
~~~

Memory 可以稳定 trace，也可以让信息回流、耦合环境片段并降低独立冗余。

### 5.2 对 SRT 的 reciprocal constraint

当前 Spine 已经区分：

~~~text
actual occurrence
!= retained historical efficacy
!= One
!= stronger standing
~~~

未来还应继续保持：

~~~text
retained history
!= cross-position public objectivity
!= independent redundancy
!= stable multi-observer accessibility
~~~

这与 author-reentry problem field 把 history / sedimentation、order / convergence、objectification / public representation 分成不同问题轴是一致的。

因此这不是新 ontology，而是 physics 给出的 reciprocal constraint：

> 沉积可以帮助客观化，也可能在某些动力学中破坏独立冗余与公开可访问性。

### 5.3 Disposition

~~~text
Quantum Darwinism objectivity mechanism
= SOURCE-OWNED

memory -> objectivity monotonic inference
= BLOCK

future canonical relevance
= preserve history / convergence / objectification as separate burdens
~~~

---

## 6. 本轮最重要的新压缩：representation-invariant core 问题

前五节可以压缩成一个比 #1089 更上游的问题：

~~~text
当我们改变
- trajectory unravelling
- quantum reference frame
- clock / temporal reference
- causal-order representation
- thermodynamic bookkeeping / information partition

SRT 所称一次真实 Selection 中，
什么必须保持不变？
~~~

这不是一个新的 SRT term，也不在本包中给出答案。

这里只记录 future question：

~~~text
representation-invariant / covariant core
of Selection / actuality
= OPEN
~~~

至少不应未经论证就把以下任一项当作 primitive core 本身：

- specific Hilbert-space factorization；
- superposition vs non-superposition label；
- one chosen quantum-trajectory unravelling；
- one clock coordinate；
- one classical causal ordering；
- Landauer dissipation magnitude；
- one observer's raw outcome vocabulary。

这些量中的一些会随成熟物理 formalism 中合法的 representation / frame / monitoring context 改变。

但这也不意味着 primitive Selection 必须是完全 frame-independent object。另一种开放方向是：

~~~text
Selection is intrinsically indexed,
while lawful transformation / covariance relations
connect indexed manifestations
~~~

本包不裁决两种方向。

---

## 7. 对未来 Spine / canonical update 的分类

### A. HIGH-CONFIDENCE PHYSICS-LOCAL DEBT

1. E01：同一 reduced dynamics 下 unique physically-actualized jump-set 口径过强；
2. E03：Landauer 从 erasure 滑向每个 classical record produced 的口径过强；
3. E03：Jarzynski / Crooks 被直接替换成 SRT W_select / Delta F_L2 / L0↔L1 asymmetry，未完成 bridge derivation；
4. E04：selection-event = clock-reading / irreversible Selection 对齐 clock transition 的口径过强。

这些适合未来 B-class bridge tightening；本包不执行。

### B. SPINE-IMPACT CANDIDATES

1. Event individuation：representation choice 与 physically instantiated record-context 必须区分；
2. Position transport：position-relative actuality 若保留，需要 transformation / transport + invariant burden；
3. Order typing：generative precedence != temporal precedence != causal order；
4. History separation：retained history != convergence / public objectivity。

这些是未来 Spine optimization 的输入，不是现在的 canonical 修改授权。

### C. SOURCE-OWNED / NO LOCAL COMPARATIVE INCREMENT

- quantum trajectory formalism；
- QRF covariance；
- indefinite causal order；
- Landauer / Jarzynski / Crooks / information thermodynamics；
- Quantum Darwinism objectivity mechanism。

### D. PARKED

继续保持停放：

- SRT-specific collapse mechanism；
- gravity = Psi_f；
- Planck Selection tick；
- exact constant derivation；
- Born-rule intentional bias；
- physics proves Selection primitive。

---

## 8. 本轮不要求作者立即裁决

本轮暂不要求作者形成新理论答案。

后续真正进入 canonical / bridge tightening 前，再决定：

1. 是否把 representation-invariant / covariant burden 纳入未来 Spine optimization 的 OPEN map；
2. 是否授权一次 Physics B-class cleanup，对 E01–E04 中上述过强句式做系统收紧。

当前只保留压力地图。

---

## 9. External sources verified for this pass

- Giacomini, F., Castro-Ruiz, E., Brukner, Č. (2019). Quantum mechanics and the covariance of physical laws in quantum reference frames. Nature Communications 10, 494. DOI: 10.1038/s41467-018-08155-0.
- Donvil, B., Muratore-Ginanneschi, P. (2022). Quantum trajectory framework for general time-local master equations. Nature Communications 13, 4140. DOI: 10.1038/s41467-022-31533-8.
- Van Regemortel, M. et al. (2022). Monitoring-induced entanglement entropy and sampling complexity. Physical Review Research 4, L032021. DOI: 10.1103/PhysRevResearch.4.L032021.
- Rozema, L. A. et al. (2024). Experimental aspects of indefinite causal order in quantum mechanics. Nature Reviews Physics 6, 483–499. DOI: 10.1038/s42254-024-00739-8.
- Zhao, H., Zhang, Y., Preskill, J. (2026). Learning to erase quantum states: thermodynamic implications of quantum learning theory. npj Quantum Information 12, 137. DOI: 10.1038/s41534-026-01273-4.
- Galve, F., Zambrini, R., Maniscalco, S. (2016). Non-Markovianity hinders Quantum Darwinism. Scientific Reports 6, 19607. DOI: 10.1038/srep19607.
- Landauer / Bennett / Sagawa-Ueda / Jarzynski / Crooks remain E03's source-native anchors; this pass does not re-derive their standard results.

---

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
