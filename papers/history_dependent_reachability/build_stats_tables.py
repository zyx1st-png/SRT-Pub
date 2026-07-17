"""Unified statistics builder. READ-ONLY inputs: the frozen results JSONs under
Experiments/anchoring_* and extraction_round.json (produced by the single authorized
deterministic extraction round). Emits STATS_TABLES.md: every paper statistic, CI,
and per-seed summary table from one source. No simulation, no bootstrap here."""
from __future__ import annotations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXP = HERE.parent.parent / "Experiments"

def J(p): return json.load(open(p))

dw = J(EXP / "anchoring_double_well/results_dissociation.json")["results"]
mf = J(EXP / "anchoring_double_well/results_matched_future.json")
sw = J(EXP / "anchoring_double_well/results_sweep.json")
b2 = J(EXP / "anchoring_bandit_holdout/results_phase2b.json")
c2 = J(EXP / "anchoring_2c_controllability/results_2c_holdout.json")
md = J(EXP / "anchoring_tiny_mdp_confirmatory/results_mdp_holdout.json")
ex = J(HERE / "extraction_round.json")

L = []
A = L.append
A("# STATS TABLES — unified statistics (single source)")
A("")
A("Inputs: frozen results JSONs (read-only) + `extraction_round.json` "
  f"(authorized round @ git {ex['provenance']['git_head'][:8]}, "
  f"script {ex['provenance']['script_sha256_16']}). No numbers elsewhere.")
A("")

A("## T1. Phase 1 (S1) dissociation, 5 seeds x n=4000")
A("")
A("| condition | P_survival | P_after_withdraw | W_sel(occ) | W_global KL(uni) | J_ext | J_write |")
A("|---|---|---|---|---|---|---|")
for k, r in dw.items():
    A(f"| {k} | {r['P_survival']:.3f}±{r['P_survival_sd']:.3f} | {r['P_after_withdraw']:.3f} "
      f"| {r['Wsel']['occupancy']:+.3f} | {r['Wglobal']['uniform']['KL']:.3f} "
      f"| {r['J_ext']:.1f} | {r['J_write']:.2f} |")
A("")
A(f"Matched-present future: gap={mf['present_state_gap']:.4f}; P(M+) anchor="
  f"{mf['raw_future_Pplus']['anchor']:.3f} naive={mf['raw_future_Pplus']['naive']:.3f}; "
  f"KL={mf['divergences']['KL']:.3f} JS={mf['divergences']['JS']:.3f} TV={mf['divergences']['TV']:.3f}.")
A(f"Sweep largest regions: anchor {sw['anchor']['largest_region']['11']}, "
  f"latent {sw['latent']['largest_region']['01']} cells (9x7 grids).")
A("")

A("## T2. Phase 2b locked holdout (S2), 40 fresh seeds — NO-GO")
A("")
h = b2["holdout"]; av = b2["active_vs_yoked"]; pm = b2["permutation"]; wc = b2["washout_curves"]
A(f"- retained z-gap: {h['retained_mean']*100:.0f}% (min {h['retained_min']*100:.0f}%); "
  f"future diff {h['fut_diff_mean']:.3f}±{h['fut_diff_sd']:.3f} "
  f"({h['fut_diff_positive_frac']*100:.0f}% seeds positive); null |diff| {h['null_abs_mean']:.3f}; "
  f"swap negative {h['swap_negative_frac']*100:.0f}%.")
A(f"- active vs yoked: future {av['fut_active_mean']:.3f} vs {av['fut_yoked_mean']:.3f} "
  f"(d={av['fut_cohen_d_active_vs_yoked']:.2f}); z-gap ratio {av['gap_ratio']:.2f}; "
  f"stable-z active {av['stable_z_active_mean']:.3f} vs yoked {av['stable_z_yoked_mean']:.3f}.")
A(f"- permutation: recovery~z {pm['corr_perm_recovery_vs_permz']:.3f} vs "
  f"recovery~label {pm['corr_perm_recovery_vs_label']:.3f}.")
A(f"- washout curves (steps {wc['wash_steps']}): retained {[round(x,2) for x in wc['retained']]}; "
  f"future diff {[round(x,3) for x in wc['fut_diff']]}.")
A("- Per-seed values are not stored in the frozen JSON and were NOT re-derived "
  "(outside the authorized extraction round).")
A("")

A("## T3. Phase 2c locked holdout (S3), 40 fresh seeds — feasibility")
A("")
p = c2["primary_ctrl"]; n = c2["negative_pe"]
A(f"- FROZEN pooled (unit seed x volatility, 80 values, B=2000): ctrl {p['mean']:.3f} "
  f"90%CI [{p['ci_lo']:.3f},{p['ci_hi']:.3f}] (Delta_min {p['Delta_min']}); "
  f"|PE| {n['mean']:.3f} 90%CI [{n['ci_lo']:.3f},{n['ci_hi']:.3f}] (eps ±{n['eps']}).")
sc = ex["phase2c"]["seed_clustered_ctrl"]; sp = ex["phase2c"]["seed_clustered_pe"]
A(f"- ROBUSTNESS seed-clustered (average the 2 volatility cells per seed, then bootstrap "
  f"40 seeds, B={sc['B']}, boot seed {sc['boot_seed']}): ctrl {sc['mean']:.3f} "
  f"90%CI [{sc['ci90'][0]:.3f},{sc['ci90'][1]:.3f}]; |PE| {sp['mean']:.3f} "
  f"90%CI [{sp['ci90'][0]:.3f},{sp['ci90'][1]:.3f}]. Direction unchanged; frozen result not modified.")
A("")
A("### T3a. Phase 2c per-seed summary (extraction round)")
A("")
A("| seed | d_ctrl_high | d_ctrl_low | d_ctrl_seed | d_pe_seed |")
A("|---|---|---|---|---|")
for r in ex["phase2c"]["per_seed"]:
    A(f"| {r['seed']} | {r['d_ctrl_high']:.3f} | {r['d_ctrl_low']:.3f} "
      f"| {r['d_ctrl_seed']:.3f} | {r['d_pe_seed']:.3f} |")
A("")

A("## T4. tiny-MDP confirmatory (S4), 50 fresh seeds, B=10000 — primary")
A("")
q = md["primary_macro_TV"]; d = md["direction"]
A(f"- macro-TV {q['mean']:.3f} 95%CI [{q['ci'][0]:.3f},{q['ci'][1]:.3f}] "
  f"(Delta_min {q['Delta_min']}).")
A(f"- direction: aligned {d['aligned_active_adv'][0]:+.3f} "
  f"[{d['aligned_active_adv'][1]:+.3f},{d['aligned_active_adv'][2]:+.3f}]; "
  f"blocked {d['blocked_active_stickiness'][0]:+.3f} "
  f"[{d['blocked_active_stickiness'][1]:+.3f},{d['blocked_active_stickiness'][2]:+.3f}]; "
  f"novel {d['novel_active_stickiness'][0]:+.3f} "
  f"[{d['novel_active_stickiness'][1]:+.3f},{d['novel_active_stickiness'][2]:+.3f}].")
A(f"- pipeline validation: memory-null {md['memory_null_macroTV'][0]:.3f} "
  f"[{md['memory_null_macroTV'][1]:.3f},{md['memory_null_macroTV'][2]:.3f}]; "
  f"memory-swap {md['memory_swap_macroTV'][0]:.3f}; same-m/diff-z {md['same_m_diff_z_macroTV'][0]:.3f}.")
A(f"- sham: self {md['sham']['self_attr']:+.3f}, ext {md['sham']['ext_attr']:+.3f}; "
  f"yoked ctrl-corr {md['yoked_ctrl_corr']:+.3f}.")
A("")
A("### T4a. tiny-MDP role-aligned mean arrival four-vectors [G_hist, G_other, G_novel, EMPTY]")
A("")
A("| battery class | active | yoked |")
A("|---|---|---|")
for k, v in ex["tiny_mdp"]["fourvec_rolealigned"].items():
    A(f"| {k} | {v['active']} | {v['yoked']} |")
A("")
A("### T4b. tiny-MDP per-seed summary (extraction round; first/last 5 shown in paper, full here)")
A("")
A("| seed | macro_tv | d_aligned | d_blocked | d_novel |")
A("|---|---|---|---|---|")
for r in ex["tiny_mdp"]["per_seed"]:
    A(f"| {r['seed']} | {r['macro_tv']:.4f} | {r['d_aligned']:+.4f} "
      f"| {r['d_blocked']:+.4f} | {r['d_novel']:+.4f} |")
A("")

A("## T5. Phase 1 latent-erosion two-point extraction (S4 supplementary figure)")
A("")
for k, v in ex["phase1_erosion"].items():
    A(f"- {k}: z_episode {v['z_episode_mean']:+.3f}±{v['z_episode_sd']:.3f} -> "
      f"z_final {v['z_final_mean']:+.3f}±{v['z_final_sd']:.3f} (frozen seeds 11–15).")
A("")

(HERE / "STATS_TABLES.md").write_text("\n".join(L) + "\n")
print(f"wrote STATS_TABLES.md ({len(L)} lines)")
