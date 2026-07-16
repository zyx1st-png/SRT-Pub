# CLAIM LEDGER — History-Dependent Reachability

Every sentence in the manuscript that asserts a finding must be traceable to a row in
the ALLOWED table (with its evidence coordinates) and must not collide with DOWNGRADED
or FORBIDDEN. When in doubt, the manuscript loses, the ledger wins.

Evidence coordinates use `research/selective-anchoring` commits; frozen JSONs are the
numeric source of truth.

## ALLOWED CLAIMS

| # | Claim (exact strength) | Evidence | Coordinates |
|---|---|---|---|
| A1 | Persistence (P), general rule-change (W_global), and selection-specific write-back (W_sel) are **bidirectionally dissociable / non-equivalent** in a constructive model — all four P×W_sel cells occupied, each as a contiguous parameter region. **NOT a statistical-independence claim** (over the sweep they correlate). | 6-condition table; phase diagrams (anchor 49 / latent 56 cells); RoughenWrite W_global KL 7.98 with W_sel≈0; LatentInscription P≈0 with W_sel=+1.0 (episode-scale) | anchoring_double_well/results_dissociation.json, results_sweep.json @ f267cfbd |
| A2 | Raw prediction-error accumulation produces **history-dependent metaplasticity that is NOT selection-specific**: a master-yoked agent (same reward stream, no choice-consequence coupling) reproduces the future effect (0.238 vs 0.239, d=0.05) on 40 fresh seeds under frozen parameters. | Phase 2b locked holdout NO-GO | anchoring_bandit_holdout/results_phase2b.json @ b55313ae |
| A3 | **Action-attributable predictive information can gate path-specific memory formation**: with r_t = log q(o|s,a) − log Σ_a' μ(a')q(o|s,a'), active ≫ yoked on the write-back consequence (paired diff 0.570, 90% CI [0.559, 0.581] > Δ_min=0.20), while the |PE| baseline stays within the ±0.15 equivalence bound (0.087, CI [0.082, 0.091]). Yoked decoupling is data-verified (ctrl-corr ≈ 0). | Phase 2c locked holdout GO | anchoring_2c_controllability/results_2c_holdout.json @ 28508e74 |
| A4 | After matching current state, fast values (Q), and initial action distribution, **history-formed path memory m changes the future behavioral arrival distribution**: macro-TV = 0.374, 95% CI [0.374, 0.375], lower bound > pre-registered Δ_min = 0.15, on 50 fresh seeds under frozen parameters. Only m is carried into the test (code-verified; same-m/diff-z = 0). | tiny-MDP confirmatory GO, primary | anchoring_tiny_mdp_confirmatory/results_mdp_holdout.json @ 766637b9 |
| A5 | The change is **directional, not merely divergent**: history-aligned advantage (+0.221 P(G_h)), and stickiness costs under blocking (+0.582 P(∅)/timeout) and novel goals (−0.278 P(G_novel)); all three 95% CIs on the pre-registered side. | tiny-MDP direction gates | same as A4 |
| A6 | The chain is **reproducible and hygiene-verified**: bit-identical holdout re-run; holdout seeds disjoint from calibration and from all other phases; test phase reads only m. | independent audit | Experiments/AUDIT.md @ 96d7fbbd |

Load-bearing per audit: **A2+A3 (selection-specificity, data-driven)** and **A5
(directional behavioral signature)**. A4 carries the primary statistic.

## DOWNGRADED (pipeline validation only — never "independent causal evidence")

| Item | Status | Reason |
|---|---|---|
| memory-null (0.044) | pipeline validation | weak, architecture-bound: residual between uniform-m and near-zero-m futures inside the future=f(m) world |
| memory-swap (0.000) | pipeline validation | mechanical/vacuous: as implemented compares battery(yoked_m) to itself; alternative framing equals the main effect |
| same-m/different-z (0.000) | pipeline validation | tautological (future takes no z argument); valid ONLY as plumbing confirmation that m is the sole carrier |
| Phase 2c statistics | mechanism feasibility | bootstrap unit = seed×volatility (80 values, 2/seed), disclosed; tiny-MDP per-seed bootstrap is the confirmatory statistic |
| Phase 2 (feasibility) gate | superseded context | zc calibrated post-formation; superseded by 2b/2c locked holdouts |

## FORBIDDEN CLAIMS

1. That any **natural system** has been shown to exhibit history-dependent write-back
   or selection-specific anchoring.
2. That **L0 / the modal field of selectability** has been shown to exist generally.
3. That **selection precedes existence** has been proven.
4. That **value or subjecthood** has been derived or demonstrated.
5. That FEP, IIT, or general RL have been **refuted or superseded**.
6. That the extremely narrow CIs indicate **construct-level confidence** — they measure
   cross-seed reproducibility of a frozen deterministic model (each per-seed statistic
   already averages N=400 agents).
7. That the Fashion-MNIST 0/5 matched-groups result shows endpoint matching in
   monolithic networks is **impossible** — it is an identification NO-GO under that
   locked protocol, nothing more.
8. That null/swap/same-m-diff-z provide **independent causal isolation** (see
   DOWNGRADED).
9. That anchoring friction / Ψ_A is established or load-bearing in this paper (cost
   appears only as J_ext/J_write side-findings: neither tracks W_sel).
