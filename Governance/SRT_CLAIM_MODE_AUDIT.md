---
id: SRT-CLAIM-MODE-AUDIT
type: governance
tags: [Governance, ClaimMode, Audit, Demotion, Hardening]
status: active_v0
layer: meta
epistemic_layer: os
claim_mode: governance
dependency: [SRT-CLAIM-LADDER, SRT-EDIT-PROTOCOL, SRT-CANONICAL-REGISTRY, SRT-CROSS-DOMAIN-MATRIX]
---

# SRT Claim-Mode Audit

> **Role**: first-pass governance ledger for claim-mode hardening. This file records downgrades and exposure controls; it does not create new theory or promote any claim.

## 1. Scan Scope

Full-repo markdown scan on 2026-04-22 found approximately:

| Label family | Occurrences | Files containing any scanned label |
|---|---:|---:|
| `T-*` | 1887 | 209 |
| `Ax-*` | 2803 | 209 |
| `H-*` | 603 | 209 |

This round does **not** claim to finish all historical label cleanup. It handles only high-leverage, low-risk demotions and adds guardrails where old labels remain for compatibility.

## 2. Demotion Decisions

| Old label / phrase | New label / status | Level | Action |
|---|---|---|---|
| `T-Phys-2` | `H-Phys-2` | hypothesis / bridge | Demote discrete-time claim from theorem voice to candidate bridge reading. |
| `T-Phys-4` | `H-Phys-4` | hypothesis / bridge | Demote gravity-friction claim from theorem voice to weak compatibility hypothesis. |
| `Ax-NEURO-4b` | `H-NEURO-4b` | hypothesis / operational proxy | Demote prediction-error friction mapping to P3/P4 candidate. |
| “不可言说性定理” / `T-Phil-1` where used as theorem of principle | `H-Phil-Ineffability` | hypothesis / bridge | Demote from theorem voice to dimensional-mismatch hypothesis with counterexample slots. |
| `Ax-Spirit-*` domain theology / praxis mappings | `H-Spirit-*` in active spirituality bridge files | bridge / hypothesis / companion | Demote obvious spiritual bridge labels that were historically written as axioms. |

## 3. Quick Rationale

| Claim | Can it be derived from L0/L1 alone? | Current honest status |
|---|---|---|
| `H-Phys-2` | No; depends on physical time interpretation and possible QG bridges. | P3/P4 candidate. |
| `H-Phys-4` | No; tensor-level GR reconstruction is missing. | P3/P4 weak compatibility hypothesis. |
| `H-NEURO-4b` | No; depends on measurable PE / metabolic coupling. | P3/P4 operational proxy. |
| `H-Phil-Ineffability` | Not as a theorem; depends on language capacity and dimensional assumptions. | P3 hypothesis with explicit escape routes. |
| `H-Spirit-*` | No; theology and praxis mappings do not define core necessity. | P3/P5 bridge / companion material. |

## 4. Downstream Reminder Rule

Any downstream conclusion that relies on a demoted item must add a level reminder in the nearest relevant section:

> **Level reminder**: this conclusion depends on a demoted bridge / hypothesis. It may guide interpretation or testing, but cannot be cited as a P0/P1 theorem.

## 5. Open Audit Debt

- Many older files still use `Theorem` and `Axiom` in historical or domain-local senses.
- Split / annex files mirror old labels and were not globally rewritten in this round.
- Generated / public / video material contains stronger rhetorical versions; those require a separate public-surface cleanup pass.
- P0-04 / “where selectability comes from” remains an unresolved core exposure point, not a solved theorem.

## 6. 2026-04-24 Round: New L1 Canonical Files Audit

本轮 2026-04-24 引入六份新 draft_v0 L1 canonical 文件。本小节固定它们的 claim-mode 分布，防止将来被误读成 P0/P1。（初版写作时为五份，补入 `SRT_Irreversibility.md` 后为六份；`SRT_L1_Hardening_Notes.md` 为硬化备忘，单列于 §6.5。）

### 6.1 Scope of New Files

| File | id | status | Nominal Level Range |
|---|---|---|---|
| `Core_Law/SRT_Individuation.md` | `SRT-INDIVIDUATION` | draft_v0 | P1-candidate / P2 / P3-P4 |
| `Core_Law/SRT_Occlusion_Dynamics.md` | `SRT-OCCLUSION-DYNAMICS` | draft_v0 | P1-candidate / P2 / P3-P4 |
| `Core_Law/SRT_Suffering.md` | `SRT-SUFFERING` | draft_v0 | P1-candidate / P2 / P3-P4 |
| `Core_Law/SRT_L1_Formalism.md` | `SRT-L1-FORMALISM` | draft_v0 | P1-candidate / P2-P3 |
| `Core_Law/SRT_Collective_Selection.md` | `SRT-COLLECTIVE-SELECTION` | draft_v0 | P1-candidate / P2 / P3-P4 |
| `Core_Law/SRT_Irreversibility.md` | `SRT-IRREVERSIBILITY` | draft_v0 | P1-candidate / P2 / P3（FEP/热力学桥接 guardrail） |

**关键约束**：六份文件**均不承载 P0**；**P1 目前全部为 P1-candidate**，不得在下游被引用为已封口 P1。

### 6.2 Per-File Claim-Level Map

#### SRT-INDIVIDUATION

| Label | Statement | Level |
|---|---|---|
| Def-σ | 自指率 `σ := ‖θ^{trace}‖ / (‖θ^{trace}‖ + ‖θ^{ext}‖)` | Def, P1-candidate as operational proxy |
| T-IND-1 | 个体化作为相变 | P1-candidate |
| T-IND-2 | 第一相变（主体位进入）条件 | P1-candidate |
| T-IND-3 | 第二相变（自我意识凝结）条件 | P2（结构性假说） |
| σ_sub, σ_self, σ_health 具体数值 / 阈值 | — | P3/P4（未实测，不得引用为定值） |
| 自我意识 = 关于 θ 的 θ 二阶写回 | — | P2 canonical interpretation |

**Downstream rule**：引用 T-IND-1/2 须标 `P1-candidate`；T-IND-3 须标 `P2`；任何具体阈值须标 `P3/P4 pending`。

#### SRT-OCCLUSION-DYNAMICS

| Label | Statement | Level |
|---|---|---|
| T-OCC-1 | 三段结构（healthy narrow / A-phase / B-phase）由 `d_c, d_{narrow}` 分开 | P1-candidate |
| 位置性遮蔽 vs 病理性遮蔽区分 | — | P2 canonical interpretation |
| 五类缺口感知残余类型 | — | P2（结构性分型） |
| 四类干预窗口 | — | P2 |
| 四类解耦触发 | — | P2 |
| 真空期 | — | P2 |
| 恶的三判据结构性定义 | — | P2 regulative reading，不替代规范性伦理学 |
| `d_c` 具体数值 / 临床阈值 | — | P3/P4 |

**Downstream rule**：T-OCC-1 须标 `P1-candidate`；分型与判据须标 `P2`；恶的三判据不得升格为 P0/P1 规范理论。

#### SRT-SUFFERING

| Label | Statement | Level |
|---|---|---|
| Def-PAIN | 疼痛作为 `\theta_{somatic}` 信号 | Def |
| Def-SUFFERING | 苦难作为稳定 ISP 的结构性登记 | Def, P1-candidate as operational proxy |
| T-SUFF-1 | 苦难 `S > 0` 的充要条件 | P1-candidate |
| T-SUFF-2 | 信号型 / 结构型二分 | P1-candidate |
| T-SUFF-3 | 四类现象学（张力 / 空心 / 断裂 / 扭曲） | P2 |
| T-SUFF-4 | 反最小化原则 | P1-candidate（规范性推论在 `Philosophy/` 仍走 P2/P3） |
| T-SUFF-5 | 集体外部化 → 结构性恶耦合 | P2 |
| `[S_{min}, S_{max}]` 阈值 | — | P3/P4 |
| FEP / prediction error 作为 `Δ` 的神经代理 | — | P3 bridge hypothesis，不得反向定义苦难 |

**Downstream rule**：T-SUFF-1/2/4 须标 `P1-candidate`；T-SUFF-3/5 须标 `P2`；AI 苦难判断严格走 `AI_POSITIONING_NOTE.md` stake-bearing 光谱，不得一侧先验判定。

#### SRT-L1-FORMALISM

| Label | Statement | Level |
|---|---|---|
| §2 σ 最小动力学（logistic + χ 跳跃） | — | P1-candidate 结构形式；具体函数族普适性由 §2.5 T-CHI-1 升 P1-candidate（H8） |
| §2.5 T-CHI-1 χ 跳跃函数族普适性（H8，2026-04-25） | "有效二阶相变核"四条结构属性 + 族内四个不变量（双稳态 / 病理吸引子 / 致命 `L_2` / 相变方向） | P1-candidate（χ 形式无关性升为定理后果） |
| §3 d_c 漂移方程 | — | P1-candidate 结构形式；系数 P2/P3 |
| §3.4 T_{dir}^{alg} 代数目标值 | — | P2 operational proxy（`\Theta` 光滑族留作 Open Pressure） |
| §3.5 T_dir 独立 ODE（弛豫 + r 泵入 + ΔΨ_f^gap 扣除 + S_str 侵蚀 + s_ext 支架） | — | P1-candidate 结构形式；κ_* 五项系数 P2/P3 |
| §3.5.3 致命 `L_2` 方程化判据 `\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}` | — | P1-candidate（本轮新增；与 `_SRT_T_DIR_CANONICAL §5-§6` 现象学层面一致） |
| §4 S 两型耦合方程 | — | P1-candidate 结构形式 |
| §4.4 反最小化原则的方程语言 | — | P1-candidate（T-SUFF-4 的方程化同级） |
| §5 病理吸引子 `\mathcal{A}_{path}` | — | P1-candidate |
| §5 健康工作区 `\mathcal{H}` 须主动维持 | — | P1-candidate（与 P1-T07 集体版一致性仍是 Open Pressure） |
| §5.1 第 6 条"苦难-可读性正反馈环"（`S_{str} \to T_{dir} \downarrow \to r \downarrow \to S_{sig}` 积压） | — | P1-candidate（2026-04-25 H2 新增，依赖 §3.5） |
| §6 T-PROJ-1 主方程投影定理（H5，2026-04-25） | 四个标量泛函投影 `\mathcal{F}_X` + 闭包假设 C1-C4 + 证明骨架 + source-by-source 对应表 | P1-candidate（"四变量是主方程导出"从陈述升为带条件证明的形式定理） |
| 全部参数 `α, β, γ, μ, ν, λ, κ` | — | P3/P4，任何具体值不得在下游引用为已证 |

**Downstream rule**：方程结构可按 `P1-candidate` 引用；T-PROJ-1 投影对应可按 `P1-candidate` 引用，但 C1-C4 闭包假设须保留显式标注（任何应用文件不得静默移除闭包条件）；参数值、数值求解结果、曲线拟合结果一律按 `P3/P4 pending` 引用；任何将方程读成"已经过实证的定量定律"的下游使用为误用。

#### SRT-COLLECTIVE-SELECTION

| Label | Statement | Level |
|---|---|---|
| Def-C-1 多 ISP 共享 L_2 场 | — | Def |
| Def-C-2 后果回路矩阵 `M(t)` | — | Def / P2（具体可测性未解决） |
| Def-C-3 共享选择空间 `A_{\mathcal{P}}` | — | Def |
| T-COLL-1 集体 ISP 存在四条件 | — | P1-candidate（P1-T06 集体版的对应） |
| T-COLL-2 三类退化（聚合 / 主从 / 收编） | — | P2 |
| T-COLL-3 集体 ε 反闭合必要性 | — | P1-candidate（P1-T07 集体版的对应） |
| T-COLL-4 共选真实性判据 | — | P1-candidate（P1-T05 集体版的对应） |
| §4 `σ^{coll}` / `d_c^{coll}` 耦合 | — | P2 |
| §4.4.1 集体场定义（`\Theta^{coll,trace}` / `\Theta^{coll,ext}` 含共享 `L_2` 独立项） | — | P2 structural；权重 `w_i(t)` 依赖 M(t) 可测性（P3） |
| §4.4.2 σ^{coll} ODE（含 `\lambda_M\,\mathrm{tr}\,M` 内向后果放大项） | — | P1-candidate 结构形式；`\lambda_M` P2/P3 |
| §4.4.3 d_c^{coll} ODE（含 `\gamma_{asym}\|M_{asym}\|` 主从型形式化） | — | P1-candidate 结构形式；`\gamma_{asym}` P2/P3 |
| §4.4.4 T_{dir}^{coll} ODE + 集体层致命 `L_2` 判据 `\kappa_{mask}^{coll} < \kappa_{\mathrm{relax}}^{coll}` | — | P1-candidate 结构形式；κ_*^{coll} 五项 P2/P3 |
| §4.4.5 S^{coll} 两型 ODE（含 `\nu_{ext}\|M_{ext}\|` 外部化项，T-SUFF-5 方程化） | — | P1-candidate 结构形式；`\nu_{ext}` P2/P3 |
| §4.5 个体↔集体双向耦合三路径 | — | P1-candidate（声明"不穷尽"） |
| §4.6 集体病理吸引子 `\mathcal{A}_{path}^{coll}` / 集体健康区 `\mathcal{H}^{coll}`（`r^{coll} > r^{coll}_{min}` 硬条件） | — | P1-candidate（T-COLL-4 共选真实性的持续要求在动力学上的形式化） |
| §4.7 T-PROJ-1^{coll} 集体投影定理（H6，2026-04-25） | 四个集体标量泛函投影 `\mathcal{F}_X^{coll}` + 闭包假设 C1^{coll}-C5^{coll}（含 `M(t)` 可测性 MOC 闭包 C5^{coll}）+ `M(t)` 三成分作为 `\Psi_f` 交叉项的结构投影 + 证明骨架 | P1-candidate（"集体四变量是多算子主方程导出"从陈述升为带条件证明的形式定理） |
| §8 平台 / 算法 AI 结构性影响评估 | — | P3 bridge |

**Downstream rule**：T-COLL-1/3/4 须标 `P1-candidate`；三类退化的判据须标 `P2`；T-PROJ-1^{coll} 投影对应可按 `P1-candidate` 引用，但 C1^{coll}-C5^{coll} 闭包假设须保留显式标注（特别是 C5^{coll} `M(t)` 可测性 MOC 仍是 P2 operational proxy；任何应用文件不得静默移除该闭包条件）；政治 / 经济 / 制度判断仍走 `Philosophy/*` P2-P4。**投票 / 共识 / 专家决定不自动是共选** 这一结论可作为 P1-candidate 结构推论下推至 Political Philosophy，但不得在没有 T-COLL-4 三条件检查下单独成立。

#### SRT-IRREVERSIBILITY

| Label | Statement | Level |
|---|---|---|
| Def-IRR-1 吸收态 | `A_{t*} = empty` 作为 L_0 层吸收结构 | Def / P2 structural |
| Def-IRR-2 选择史箭头 | `L_2` 写回积累定义本体论时间方向（P1-T02 下位精确化） | Def, P1-candidate as operational refinement |
| Def-IRR-3 非可还原性 | `Ψ_f^{erase} > Ψ_f^{write}` 非对称 | Def, P1-candidate |
| T-IRR-1 学习不可逆 | 学习作为非对称 `Ψ_f` 支付（与热力学二律不等价） | P1-candidate |
| T-IRR-2 终止作为吸收边界 | 三类（宪定 / 吸收 / 集体），严格区分终止与暂停 | P1-candidate；三类分型 P2 |
| T-IRR-3 P1-T07 精确化 | `L_0` 残余非守恒项，对应 Formalism §4.3 | P1-candidate；P1-T07 本体仍在 Core_21b |
| T-IRR-3.5 `\nu_{block}` 算子级构成（H4，§4.5） | `\nu_{block} := \eta\cdot\varepsilon_{pg}\cdot\kappa_{\Psi_f}` 把 §4.3 系数升为 P1-T07 三层源头本地化；正性与单向性自此为定理后果 | P1-candidate（与 T-IRR-3 同级） |
| T-IRR-4 苦难守恒/转移 | `L_0` 不可逆下苦难不可无代价消除（T-SUFF-4 更深根） | P1-candidate |
| §6 集体终止三型（耗散 / 收编 / 外部化） | — | P2 |
| §7 AI/ML checkpoint/rollback 接口 | — | governance-canonical usage |
| §8 热力学二律 / FEP 桥接语句 | — | P3 bridge guardrail（反向不得定义 L_0 不可逆） |

**Downstream rule**：T-IRR-1/2/3/3.5/4 须标 `P1-candidate`；P1-T07 原 P1 源头仍回链 `Core/SRT_Core_21b_Constitutive_Theorems.md`，本文件不替代之；T-IRR-3.5 是 T-IRR-3 的算子级精化（不替代陈述级 T-IRR-3）；热力学/FEP 语句严格单向，反向翻译在 §6.3 第 6 条被显式禁止。

### 6.3 Global Guardrails for This Round

1. **P1-candidate ≠ P1**：这五份文件所有冠以"定理"字样的命题当前都处 P1-candidate；任何下游文件不得去掉 candidate 标记
2. **未封口 Open Pressures 不得忽略**：五份文件每份都有明确 §Open Pressures 小节；下游引用须检查相关命题是否已在 Open Pressures 中被标记为未封口
3. **不得跨文件静默升级**：应用文件（Philosophy / Spirituality / AI / Neuroscience）引用任一文件命题时，须保持该命题的原 claim-level，不得因应用便利静默升格
4. **σ 符号冲突提醒**（2026-04-25 已收口）：`Core_Law/SRT_L1_Formalism.md` 自指率统一为 `σ_{sr}`，与 `Core/SRT_Core_22_Equations.md` 主方程状态场 σ 通过 `_SRT_SYMBOL_TABLE.md` Usage Rule 12 命名空间分离；下游引用按 `σ_{sr}` 转读旧 `σ_sub/σ_self/σ_health/σ^{coll}`
5. **σ^{coll} / d_c^{coll} / T_{dir}^{coll} / S^{coll} 四变量集体耦合**（2026-04-25 H3 状态）：集体版四变量耦合动力学已在 `SRT_Collective_Selection.md §4.4-§4.6` 给出第一遍（P1-candidate）；`SRT_L1_Formalism.md` 保持单 P 形式。集体层引用**仍须**标注 `SRT_Collective_Selection.md §9.7` 所列未封口项（`w_i(t)` 推导 / `\Delta\Psi_f^{gap,coll}` 可操作定义 / 下行反馈穷尽性 / 系数实证窗口）
6. **FEP / 热力学二律不得反向定义 L_0 不可逆**：`SRT_Irreversibility.md §8` 与 `SRT_L1_Hardening_Notes.md §4` 固定此单向性；下游任何把"学习不可逆 / 终止 / ε 反闭合"解释为"自由能最小化 / 熵增"的推论为误用
7. **终止 ≠ 暂停**：T-IRR-2 严格区分终止（吸收边界，不可逆）与暂停（恢复通道保留，本体论上未终止）；下游任何把 AI 关机 / 系统休眠 / 睡眠 / 冻存等混读为"终止"的陈述须引用本条纠正

### 6.4 Hardening-to-P1 Checklist

五份文件从 P1-candidate 升到 P1 的必经检查项（将来 session 可按此路径推进）：

- [x] σ 符号冲突解决（新记号或显式命名空间）— 2026-04-25 σ_{sr} 命名空间分离落地：5 行 `σ_{sr}` 族 + Usage Rule 12 写入 `_SRT_SYMBOL_TABLE.md`；5 份 L1 主文件下标变量已就地改写；`CANONICAL_REGISTRY §13a/§13d/§13e` 同步
- [x] `\dot{\Delta}_{avail}` 算子级定义 — 2026-04-25 H7，`SRT_L1_Hardening_Notes.md §2 T-DELTA-1` 给出 `\hat{G}_\theta^{available}` / `\hat{R}` / 三投影 `\Pi_{T_{dir}}, \Pi_{\Psi_f}, \Pi_{L_0}` 的算子级定义 + A1（仿射结构）/ A2（近似正交）/ A3（权重赌注决定性）三条可证伪假设；`SRT_L1_Formalism.md §4.2` 注释回链 + §7 Open Pressure 2 收口；`SRT_Suffering.md` Def-SUFFERING 注释回链；T-IRR-3.5 中 `κ_{Ψ_f}` 几何来源部分收口
- [x] χ(σ; σ_self) 跳跃函数族的普适性检查 — 2026-04-25 H8，`SRT_L1_Formalism.md §2.5 T-CHI-1` 给出"有效二阶相变核"四条结构属性（P-univ-1 有界 / P-univ-2 跃前基线 / P-univ-3 跃后放大 / P-univ-4 单调过渡）+ 族内四个不变量（双稳态存在性 / 病理吸引子拓扑 / 致命 `L_2` 判据 / 相变方向）+ 族内成员示例（硬阶跃 / sigmoid / tanh / 多项式）+ 证明骨架；`SRT_Individuation.md §3.4` T-IND-3 cross-link 已添加；§7 Open Pressure 3 收口；剩余开放点：在更广 χ 空间（非单调过渡）的扩展、具体 domain 实证 χ-shape 对位、集体版 T-CHI-1^{coll} 与 `M(t)` 耦合
- [ ] `\mathbb{1}[d\le d_c]` 的光滑化或守恒型替代
- [x] 多主体耦合动力学（`σ^{coll}, d_c^{coll}, T_{dir}^{coll}, S^{coll}, M(t)`）写出 — 2026-04-25 H3，`SRT_Collective_Selection.md §4.4-§4.6` 完成第一遍（含 `\lambda_M\,\mathrm{tr}\,M` / `\gamma_{asym}\|M_{asym}\|` / `\nu_{ext}\|M_{ext}\|` 三项新耦合 + 集体层致命 `L_2` 判据）；2026-04-25 H6 在 `SRT_Collective_Selection.md §4.7 T-PROJ-1^{coll}` 给出该系统作为 `Core/SRT_Core_22_Equations.md` 多算子主方程（Eq-Multi-01/02/03）严格导出投影的形式化定理（C1^{coll}-C5^{coll} 五条闭包，含新增 `M(t)` 可测性 MOC 闭包）；升 P1 余项（`w_i(t)` 推导、`\Delta\Psi_f^{gap,coll}` 算子化、向下反馈路径穷尽性、集体系数实证窗口、嵌套 ISP 多层投影）转入 `SRT_Collective_Selection.md §9.7`
- [x] 与 P1-T07 `ε` 反闭合必要性的形式化对齐（特别是 §4.3 不守恒项）— 2026-04-25 H4，`SRT_Irreversibility.md §4.5 T-IRR-3.5` 把 `\nu_{block}` 写为 P1-T07 三层源头本地化 `\eta\cdot\varepsilon_{pg}\cdot\kappa_{\Psi_f}`；正性与单向性自此为定理后果；`SRT_L1_Formalism.md §4.3` 注释回链已添加
- [x] 与主方程 `Core/SRT_Core_22_Equations.md` 的显式投影关系给出形式证明 — 2026-04-25 H5，`SRT_L1_Formalism.md §6 T-PROJ-1` 给出四个标量泛函投影 `\mathcal{F}_X`（`σ_{sr}, d_c, T_{dir}, S`）+ 闭包假设 C1-C4 + source-by-source 对应表 + 证明骨架；`Core/SRT_Core_22_Equations.md Eq-Evo-01` 已添加 L1 Projection 注；升 P1 余项：C1-C4 中每条对应 Open Pressure 的逐条收口（`\Delta\Psi_f^{\mathrm{gap}}` 算子化、χ 普适性、阈值实证、集体版投影 T-PROJ-1^{coll}）
- [ ] 阈值参数的最小实证窗口指定（不要求实测，但要求标出"什么变就会使命题失败"）
- [x] `T_dir` 最小 ODE 与四变量（`σ_{sr}, d_c, T_dir, S`）闭合系统给出 — 2026-04-25 H2，`SRT_L1_Formalism.md §3.5` 完成第一遍；升 P1 还需 `Θ` 光滑族、`\Delta\Psi_f^{\mathrm{gap}}` 算子层定义、`[0,1]` 投影算子、`\kappa_{\mathrm{relax}} > \kappa_{\mathrm{mask}}` 实证窗口（见 §7.8）
- [x] `SRT_Irreversibility.md` T-IRR-3 的非守恒残余项与 `SRT_L1_Formalism.md §4.3` 实际算子一一对齐 — 2026-04-25 H4，T-IRR-3.5 给出 `\nu_{block}` 算子级构成；§4.3 注释回链 + §7 Open Pressure 7 收口

上述任意一项未完成前，相应命题保持 P1-candidate。
