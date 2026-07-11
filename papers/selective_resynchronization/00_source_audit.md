---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-SOURCE-AUDIT-20260710
type: source_audit
status: draft_v0_2
layer: paper_working
epistemic_layer: bridge
claim_mode: audit
canonical: false
created: 2026-07-10
revised: 2026-07-10
scope: legacy_entropy_manuscript_and_current_srt_boundaries
---

# Source Audit for the Selective Resynchronization Paper

## 0. Audit verdict

本轮检索找到了旧稿的**完整文本抽取**，但它只存在于 Git 历史，不在当前工作树中。可以确认的旧稿是：

> *Selection Cost as a Fisher Information Metric: A Riemannian Geometry of Embodied Updating*

可读取对象为：

```text
git object: 03151072^:tmp_attached_extract.txt
length: 695 lines
rendered manuscript length: 20 pages
```

该对象是从附件 PDF 抽出的文本，不是原始 PDF、投稿排版文件、marked manuscript 或 revised manuscript。仓库历史中的 source note 记录了附件名 `d811109c-4993-4b48-9dcc-dc6b75f43f78.pdf`，但该 PDF 本身未在当前工作树、Git 可达对象、Git 不可达对象或用户主目录中找到。

没有找到旧 Entropy 投稿的 reviewer comments、rejection/decision letter、response to reviewers、marked manuscript、revised manuscript、`entropy-4202982` 对应文件或投稿门户导出。旧稿正文中出现 “A common reviewer question” 和 “Reviewers may note” 等作者预判性措辞，但这些不是审稿意见，不能当作 reviewer evidence。

旧稿声称存在可复现的实验脚本、CSV、图和多随机种子输出，但这些资产没有在仓库或 Git 历史中找到。因此旧稿中的数值只能登记为 **reported historical results, not repository-verifiable results**。

当前 SRT 边界材料则足够清楚：Fisher geometry 只能作为局部统计可区分性、更新路径或转变负担的条件性投影 / proxy；不得再写成 `Ψ_f`、selection cost 或 ontological friction 的完整定义。新论文必须是 P3/P4 层的 domain-specific methods / empirical-hypothesis work，而不是 SRT ontology 的证明。

第二阶段补充核验确认：精确文件 `01_Source_Intuition/SRT_CHOICEMAP_RANDOM_RESYNCHRONIZATION_TRACE_2026-07-09.md` **存在于远端 `SRT-Pub` 仓库并可通过远端原始文件读取**，但尚未进入本地工作树或本地 `origin/main` 引用。下文据实际读取内容登记其来源地位与最窄构念链；不把它当成证据、正式定义或形式权威。

---

## 1. Search scope and method

本轮执行了以下只读检索：

1. 当前工作树与被忽略文件的文件名检索：标题、`entropy-4202982`、Fisher、reviewer、rejection、marked/revised、BOCPD、CUSUM、CIFAR、digits、Čencov/Chentsov、`d log d`。
2. 当前工作树全文检索：上述关键词以及 reselectability、payability、future selection、retained plasticity、desynchronization、resynchronization、randomization、selection scaffold。
3. 所有 Git refs 的文件名、历史内容与提交记录检索。
4. Git 不可达对象检索，以排除审稿信或附件残留在 dangling blobs 中的可能。
5. 用户主目录内按旧 PDF UUID、标题和 `entropy-4202982` 的精确文件名检索。
6. 当前分支与 `origin/main` 的对比检索；未切换分支，也未恢复或覆盖旧文件。
7. 第二阶段通过远端 `SRT-Pub` 原始文件接口核验精确 source-intuition trace；远端读取成功，本地文件仍缺失。

检索中未找到的材料在 §6 明确列出，不用推测补齐。

---

## 2. Located legacy-manuscript materials

### 2.1 Historical manuscript text extraction

| Item | Location / provenance | Role | Reliability and limits | New-paper use |
|---|---|---|---|---|
| Old manuscript text | `03151072^:tmp_attached_extract.txt` | 旧稿正文、公式、实验方法、reported results、references | 文本基本完整；不是原 PDF；排版和部分公式在抽取时损坏；没有审稿批注 | 作为旧稿内容审计与可回收方法种子，不作为已验证结果 |
| Attachment provenance | historical `SRT/_SRT_SIGNAL_LOG.md` entry introduced by commit `0ddf0022` | 记录附件 UUID、主题和当时的 A-class ingestion | 只证明曾有附件并被内部吸收，不证明论文结论正确 | 追溯来源；不作证据 |
| Initial ingestion diff | commit `0ddf0022` | 将旧稿中的 embodiment gate、curvature bound、Fisher-spectrum proxy 写入旧 Physics / measure-map | 当时仍使用 `Ψ_f` 与 Fisher 强绑定；已被 4—7 月边界收紧 | 用于说明理论口径变化，不恢复旧 identity claim |
| Current derivative source note | `Physics/SRT_Phys_09_Formalism_Ext.md` §12.8 and split copy | 保留旧稿的三个接口：embodiment proxy、curvature risk、spectral proxies | 当前已改成 projection / proxy 语言；Physics claim-status 明确其非 canonical | 仅作方法来源与历史桥接 |
| Repository inclusion matrix | `90_Backstage/Restructure_2026/BOOK_PROJECT/repository_material_inclusion_matrix.md` | 记录 Fisher、BOCPD、CIFAR-10 CNN、AUC/delay 等材料家族的后续归属 | 后台检索材料，不是实验资产或证明 | 用于确认仓库曾规划这些内容，但不补足缺失数据 |

### 2.2 What the old manuscript actually claimed

旧稿的主问题是：

> Is selection cost a Fisher information metric?

其核心主张包括：

1. 以 reparameterization invariance、sufficient-statistics / coarse-graining monotonicity 和 Čencov uniqueness 为理由，写出 `Ψ_f(θ) ≡ g(θ)`。
2. 将自然梯度、thermodynamic length、geodesics 和 Fisher curvature 统一解释为 embodied selection cost / ontological friction。
3. 将正曲率下的 geodesic focusing / conjugate-point bound 解释为学习系统发生非局部重配置或 “insight-like events” 的风险提示。
4. 在 A1—A3 假设下提出 `E(d) \gtrsim d\log d`，其中 `d` 被定义为 Fisher metric 的有效敏感维数，并进一步以 “care directions” 解释。
5. 报告两个数值例子：online symmetric Gaussian-mixture adaptation；sklearn digits + two-layer MLP 的 covariate regime shift。

这些内容混合了四个不同层级：

| Layer | Old-paper content | Current audit status |
|---|---|---|
| Established / standard mathematics | Fisher metric、KL 的局部二阶展开、natural gradient、Gram trick、Jacobi-field focusing background | 可保留，但需准确引用且不得包装成 SRT 证明 |
| Method definition | empirical-Fisher spectral proxies、fixed probe、change-point readouts | 可重写为候选方法并与简单基线比较 |
| Empirical hypothesis | curvature / spectrum 与 reconfiguration、delay、instability 的关系 | 可保留为可失败假设，不得先验成立 |
| Ontological interpretation | `Ψ_f ≡ g_F`、selection cost identity、embodied existential cost | 删除；不进入新论文的结果或定义层 |

### 2.3 Reported old experiments — not independently verified

#### Experiment A: online Gaussian-mixture adaptation

旧稿使用对称双高斯混合，设置一次 change point，并追踪 NLL、参数轨迹、empirical Fisher condition number / log determinant 等。当前只找到论文叙述和图题，未找到脚本、原始时间序列或图像。

#### Experiment B: sklearn digits + MLP

旧稿报告：

- sklearn digits，8×8 grayscale，10 classes；
- `64 -> 64 -> 10` tanh MLP；
- full-batch SGD，50 epochs；
- epoch 25 后加入 `σ = 0.08` 的 Gaussian input noise；
- 20 random seeds；
- fixed probe size `B = 32`；
- empirical Fisher Gram matrix；
- Fisher trace、largest eigenvalue、condition proxy；
- NLL z-score、BOCPD(NLL)、kernel CPD on NLL；
- ROC AUC、detection delay、fail rate。

旧稿表 1 报告的 mean ± SD 为：

| Method | ROC AUC | Detection delay | Fail rate |
|---|---:|---:|---:|
| `|z(tr F_hat)|` | `0.787 ± 0.176` | `0.75 ± 1.02` | `0.00` |
| `|z(lambda_max)|` | `0.835 ± 0.188` | `2.60 ± 4.74` | `0.00` |
| `|z(NLL)|` | `0.841 ± 0.012` | `4.00 ± 0.00` | `0.00` |
| `BOCPD(NLL)` | `0.488 ± 0.069` | `7.35 ± 7.71` | `0.15` |
| kernel CPD on NLL | `0.690 ± 0.054` | `0.00 ± 0.00` | `0.00` |

这些数字只说明旧稿**如此报告**。没有仓库资产可确认实现、阈值、false-alarm policy、seed-level variance、数据切分、代码版本或图表一致性。

旧稿 abstract 声称支持 “z-score/CUSUM”，但方法和结果表实际比较的是 z-score、BOCPD 与 kernel MMD change-point detector；没有找到 CUSUM 实验表或实现。这是旧稿内部一致性问题。

旧稿讨论 CIFAR / CNN / ResNet 只作为 scalability roadmap；未找到完成的 CIFAR 实验。因此新稿不得把 CIFAR 写成既有结果。

---

## 3. Located current theory-boundary materials

### 3.1 Definition authorities and mandatory guardrails

| File | Authority / role | Relevant boundary for the new paper |
|---|---|---|
| `_SRT_PSI_F_CANONICAL.md` | `Ψ_f` definition authority | payability burden is the main reading; Fisher is a conditional local projection; `Ψ_f ≡ g_F` is forbidden; projection failure must remain possible |
| `_SRT_SYMBOL_TABLE.md` | symbol and usage authority | Fisher metric, Fisher-induced scalar quadratic form, path functional and `Ψ_f` are different objects |
| `Governance/SRT_CLAIM_LADDER.md` | proposition-level hardness | machine-learning operationalizations are P3 bridge / P4 lab hypotheses, never P0/P1 by default |
| `Core/SRT_OPEN_TENSIONS.md` §2 | unresolved projection boundary | necessary-and-sufficient conditions linking Fisher geometry to paid burden remain open |

### 3.2 Bridge, audit and lab-routing files

| File | Role | Relevance |
|---|---|---|
| `SRT_Fisher_FEP_Landscape_Interface.md` | bridge clarification | Fisher describes local distinguishability / transition geometry; it does not define `L1`, `L2` or `Ψ_f` |
| `Physics/SRT_Physics_Claim_Status.md` §2.8 | domain audit | Fisher-to-`Ψ_f` is P3/P4 only; old `Ax-*` and `T-*` labels in Formalism Ext are retrieval handles, not theorem status |
| `Core/SRT_Core_21c_Bridge_Hypotheses.md` P2/P3-B08 and B12 | bridge hypotheses | “friction as generative principle” and information-geometric hardening remain P2/P3; no new P0/P1 theorem |
| `_SRT_EQ_HYP_MAP.md` | equation-to-hypothesis routing | Fisher/Landauer equations are bridge items with open gaps, not established empirical laws |
| `SRT_EXP_MEASURE_MAP.md` | proxy inventory | empirical Fisher condition, log-det and eigenvalue changes are candidate proxies; the map contains no validation of selective resynchronization |
| `04_External_Convergence/Mathematics_Information/EC-IG-Fisher-PsiF.md` | E2 evidence card | Fisher has a non-arbitrary mathematical role under stated invariance conditions, but no domain-specific operational bridge has been established; simpler explanations must be compared |

### 3.3 Binding consequences for the new manuscript

The new paper must keep the following distinctions explicit:

1. `F_t` is a Fisher information matrix / metric estimate.
2. `G_t = 1/2 Δθ_t^T F_t Δθ_t` is a local scalar quadratic form.
3. `sum_t G_t` is an accumulated path-energy-style quantity, not automatically a geodesic length and not an actual training-cost ledger.
4. `Ψ_f` is the SRT payability / selection-impedance construct and is not measured by `G_t` by definition.
5. wall-clock time, FLOPs, energy, samples, recovery delay and forgetting are separate realized costs.
6. exact Fisher geometry, empirical Fisher, diagonal / block / K-FAC approximations and output KL are not interchangeable estimators.

---

## 4. Located reselectability and future-adaptation materials

| File | Status | Useful content | Boundary |
|---|---|---|---|
| `_SRT_OBJECTHOOD_AS_RESELECTABILITY_META_STANDARD.md` | non-canonical research seed | current performance can be purchased by loss of future reopening; reselectability is not option count | cannot define the paper's variable by ontology or morality |
| `_SRT_CONTEXT_ROUTER_RESELECTABILITY_ADDENDUM.md` | navigation | separates ontology, dynamics and governance; says current performance and future reselectability can diverge | toy evidence is dynamics-half only |
| `_SRT_DIRECTION2_WEDGE1_SIM_RESULTS.md` | pilot, not validation | in one toy landscape, reward-optimal and future-robust operating points diverge | no neural-learning validation; no moral or ontological inference |
| `_SRT_DIRECTION2_WEDGE2_SIM_RESULTS.md` | toy illustration, not validation | shows a constructed distributional-payability pattern | peripheral to the new neural-learning paper; should not enter the core argument |
| `_SRT_D_VALUE_CANONICAL.md` §11 | canonical index with bridge formulas | distinguishes current alignment from `d_mobile`, a proposed dynamic realignment capacity | new ML outcome should be called retained adaptability / residual plasticity, not canonical d-value |
| `_SRT_PSI_F_CANONICAL.md` Def-Ψ-3 and §6 | canonical boundary | payability explicitly includes preservation of closure, continuity and future selection capacity | inspires the question but does not supply an ML measurement identity |
| `Neuroscience/SRT_Neuroscience_Claim_Status.md` §2.4 | domain audit | permits “cross-system desynchronization” as a pathology-modeling bridge | no operational definition of productive or selective resynchronization |

The narrow reusable insight is:

> Current performance and future adaptation capacity can be empirically separable.

This is a research heuristic and a test target. It is not evidence that a particular neural-network metric measures SRT reselectability.

---

## 5. Source-intuition trace: remote access and authority boundary

### 5.1 Access status

The exact requested file is absent from the current local worktree, the locally cached `origin/main`, searched local Git refs and local Git history:

```text
01_Source_Intuition/SRT_CHOICEMAP_RANDOM_RESYNCHRONIZATION_TRACE_2026-07-09.md
```

It is nevertheless **confirmed to exist in the related remote `SRT-Pub` repository**, and its content was successfully read from the remote raw-file endpoint during this audit. The correct record is therefore:

> **Known to exist remotely and accessed; not currently available as a local repository file.**

Accessed source: [remote raw trace](https://raw.githubusercontent.com/zyx1st-png/SRT-Pub/main/01_Source_Intuition/SRT_CHOICEMAP_RANDOM_RESYNCHRONIZATION_TRACE_2026-07-09.md).

This replaces the earlier “not found / nonexistent” conclusion. No content was reconstructed from memory or from a nearby file.

### 5.2 Recorded source status

The remote file identifies itself as:

- `type: intuition_trace`;
- `status: source_trace_v0`;
- `audit_status: upgraded_v1`;
- `canonical: false`;
- `ai_do_not_use_for_definition: true`;
- `trace_mode: retro_writeback`.

Its paper-development role is therefore **construct provenance only**. It records the 2026-07-09 ChoiceMap intuition that motivated the question. It is not:

- empirical evidence;
- a canonical SRT definition;
- a mathematical result;
- a formal-mechanism authority;
- validation that the proposed machine-learning construct is novel or useful.

### 5.3 Narrow construct-provenance extraction

Only the following source-level chain is imported into this paper program:

\[
\text{desynchronization / randomization}
\rightarrow
\text{comparison}
\rightarrow
\text{selective resynchronization}
\rightarrow
\text{path formation}
\rightarrow
\text{renewed adaptive scaffold}.
\]

The domain paper must operationalize each link independently. In particular:

- “randomization” cannot be identified with undifferentiated noise;
- “comparison” requires an operational selection or alignment test rather than metaphorical use;
- “resynchronization” does not mean neural oscillatory phase synchrony by default;
- “path” means a reusable learned organization only if retention and robustness tests support that reading;
- “renewed adaptive scaffold” is represented by later adaptation capacity, not inferred from current performance.

The trace also warns against mere return to the old synchrony: stabilization that closes later adaptation is a cage, not the target process. This is a source intuition to be tested, not a finding.

### 5.4 Nearby trace retained only as collateral context

A different local/remote-history source trace remains available:

```text
01_Source_Intuition/SRT_FIRST_INTUITION_SELECTION_BEFORE_EXISTENCE_CHOICE_TRACE_2026-07-09.md
commit: 35c17e7e
```

It records that good selection preserves subsequent selectability and that apparent stability can be brittle. It is collateral non-canonical context only; it was not used to reconstruct or substitute for the exact ChoiceMap trace.

---

## 6. Materials not found

### 6.1 Entropy submission and review package

- `entropy-4202982` submission file or portal export — **not found**.
- Original manuscript PDF — **not found**.
- PDF `d811109c-4993-4b48-9dcc-dc6b75f43f78.pdf` — **not found**.
- Reviewer comments / review reports — **not found**.
- Editorial decision or rejection letter — **not found**.
- Response to reviewers — **not found**.
- Marked manuscript — **not found**.
- Revised manuscript distinct from the recovered text — **not found**.

The existing `papers/ontological_friction/frontiers_response_to_reviewers.md` belongs to a different Frontiers manuscript and was excluded from this audit.

### 6.2 Experiment and reproducibility package

The recovered manuscript names the following types of assets, but they were not found:

- `run_nn_regimeshift_quant_multiseed.py` — **not found**.
- `v8_assets/*.csv` — **not found**.
- seed-level Fisher / NLL traces — **not found**.
- mixture-adaptation script and raw output — **not found**.
- old manuscript Figures 1–7 — **not found**.
- BOCPD implementation and hyperparameter audit — **not found**.
- kernel-MMD CPD implementation — **not found**.
- CUSUM implementation or result table — **not found**.
- completed CIFAR experiment — **not found**.
- completed Fashion-MNIST experiment — **not found**.
- independent proof or proof appendix for `d log d` beyond the recovered conditional assumption chain — **not found**.

### 6.3 Latest requested intuition trace

- Local working-tree copy of `SRT_CHOICEMAP_RANDOM_RESYNCHRONIZATION_TRACE_2026-07-09.md` — **not found locally**.
- Remote `SRT-Pub` copy — **confirmed and read**.
- Canonical or formal definition authority for the trace — **not applicable; the file explicitly disclaims this role**.

---

## 7. Major problems in the old manuscript

### 7.1 Category error in the central identity

The old paper identifies a metric tensor with a scalar / path-level / paid cost:

```text
Ψ_f(θ) ≡ g(θ)
```

This collapses different mathematical object types. A Fisher metric can induce a quadratic form or path measure, but the tensor is not itself a complete cost, realized expenditure or SRT payability burden.

### 7.2 Čencov uniqueness is overextended

Čencov-style uniqueness makes Fisher geometry non-arbitrary under specific statistical invariance / monotonicity assumptions. It does not prove that Fisher geometry is embodied selection cost, ontological friction or `Ψ_f`. The old argument moves from uniqueness within one mathematical class to an ontological identity without an independently established bridge.

### 7.3 Mathematical background and novel claims are not cleanly separated

The old manuscript labels standard or conditional material as axioms and theorems inside one framework. The focusing result is mathematical background; the claim that it predicts insight-like reconfiguration in noisy learning is an empirical bridge. The latter does not inherit theorem status from the former.

### 7.4 The `d log d` result is assumption-driven and semantically overloaded

The old derivation assumes that maintaining `d` independent “care directions” requires `d log ρ(d)` information and that `ρ(d)` grows at least polynomially / linearly. The resulting `d log d` scaling is then largely encoded in the assumptions. It also identifies Fisher effective rank with care dimensionality, contrary to the current capacity-versus-stake boundary. This material should be removed from the main paper; if ever retained, it requires a separate conjecture / exploratory appendix and independent justification.

### 7.5 The old empirical question is change detection, not successful adaptation

The reported experiments ask whether a metric changes at a known distribution shift. They do not test whether the system turns perturbation-induced variability into a stable and reusable coordination structure.

### 7.6 No distinction among rigidity, productive opening, resynchronization and collapse

A Fisher spike can accompany useful adaptation, ordinary optimizer sensitivity, transient noise, instability or catastrophic failure. The old design has no outcome structure capable of distinguishing these cases.

### 7.7 Current performance and future adaptability are not separated

The old design has one shift and evaluates detection. It contains no second environmental change, matched-current-performance comparison, relearning test, transfer test or residual-plasticity outcome.

### 7.8 Fisher proxies are treated as privileged before incremental validity is shown

The old paper does not require Fisher measures to beat or add to output KL, gradient norm, representation drift, Hessian / sharpness, predictive entropy, loss and parameter distance in predicting later outcomes.

### 7.9 Approximation and parameterization risks are under-audited

The empirical Fisher is not the true Fisher in general. Trace, determinant, eigenvalue condition and blockwise approximations can change with estimator, probe set, damping, coordinates and model redundancy. Exact metric invariance does not automatically transfer to every finite-sample scalar proxy.

### 7.10 The reported baseline pattern does not establish Fisher superiority

In the old table, NLL has the highest mean AUC, while a kernel CPD has zero reported delay. Fisher trace has an earlier delay than NLL z-score but high AUC variance. This is at most a metric-specific trade-off, not evidence that Fisher is the best detector or a special ontological measure. BOCPD's weak result could reflect model or hyperparameter mismatch and must not be used rhetorically.

### 7.11 Reproducibility is currently broken at repository level

The text names scripts and raw assets that are absent. The old numerical results cannot carry a new empirical paper until they are independently reproduced or the original assets are recovered and verified.

### 7.12 The old title and novelty claim make Fisher the answer in advance

The title encodes the identity claim before empirical comparison. The new title and contribution must place the adaptive phenomenon first and Fisher as one candidate measurement interface.

---

## 8. Salvage decisions for Stage-2 development

### Retain as technical background or implementation seed

- Fisher information matrix definition.
- Local KL second-order relation, with regularity and locality conditions.
- Fisher quadratic update burden as a candidate local transition measure.
- Empirical-Fisher computation on a fixed probe.
- Gram-trick implementation for finite probe batches.
- Change-point evaluation with BOCPD and CUSUM, after fresh verified implementations.
- The principle that an early-warning signal and an outcome measure are different.
- The old Digits experiment as a debugging seed only, not as evidence.

### Rewrite completely

- Research question and title.
- Introduction and contribution statement.
- Definition of the target phenomenon.
- Hypotheses and state taxonomy.
- Experimental sequence, adding at least two environmental shifts.
- Outcome metrics, especially retained adaptability.
- Fisher section, including estimator choice, computational cost and projection failure.
- Statistical analysis, requiring incremental value over simple baselines.
- SRT relationship section and all ontology-adjacent language.

### Delete from the main paper

- `Ψ_f = g_F` or “selection cost is Fisher metric.”
- “Čencov proves selection cost.”
- Fisher geometry as proof or confirmation of SRT.
- ontological selection claims from neural-network experiments.
- `d log d` as a theorem or established energetic law.
- PCI / consciousness extrapolation from rank-degenerate Fisher geometry.
- “insight” language unless independently labeled events and a valid construct are supplied.
- any old numerical result not rerun from auditable code and data.

---

## 9. Audit conclusion

The repository supports a scientifically useful reframing, but not a direct empirical continuation of the old Entropy paper.

The defensible starting point is:

> Fisher geometry is a candidate local measurement interface for update transitions. The research target is whether perturbation-induced variability is reorganized into stable adaptation that preserves future adaptation capacity. The Fisher bridge succeeds only if it adds reliable predictive information beyond simpler measures and survives estimator, parameterization and task controls.

The missing review package means the next draft must not claim to answer particular reviewers. It can answer the visible weaknesses of the old manuscript and the explicit 2026-04—07 theory boundaries, while marking the external review record as unavailable pending user-supplied files.
