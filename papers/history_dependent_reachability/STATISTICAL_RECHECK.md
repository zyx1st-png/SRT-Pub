# Pre-submission statistical re-check

Date: 2026-07-17. Scope: the single authorized deterministic extraction round plus
the unified statistics build. **No frozen experiment file was edited; no new
experiment was run; the manuscript body was not modified by this re-check.**

## 1. Provenance

- Git HEAD at extraction: `07a854e7` (paper/selective-anchoring).
- Command: `python3 extraction_round.py` (then `python3 build_stats_tables.py`).
- Script hash (sha256/16) of `extraction_round.py`: recorded inside
  `extraction_round.json` → `provenance.script_sha256_16`.
- Frozen configs (sha256/16): tiny-MDP `config_mdp_frozen.json`, 2c
  `config2c_frozen.json`, double-well `config.json` — recorded in
  `extraction_round.json` → `provenance.frozen_configs`.
- Seeds: tiny-MDP 40000–40049; 2c 30000–30039; double-well 11–15 — the original
  frozen holdout/dissociation seeds, unchanged.
- Frozen code imported (never edited): `holdout_mdp.py`/`model_mdp.py`,
  `holdout2c.py`/`model2c.py`, `model.py` (double-well), each loaded from its
  frozen directory by an external script living in the paper directory.

## 2. Reproduction check — extracted vs frozen primaries (STOP rule: none triggered)

| quantity | extracted | frozen JSON | verdict |
|---|---|---|---|
| tiny-MDP macro-TV mean | 0.37441500000000005 | 0.37441500000000005 | bit-identical |
| tiny-MDP macro-TV 95% CI | [0.37356497916666664, 0.3752425416666667] | same | bit-identical |
| tiny-MDP aligned diff mean | 0.22090750000000003 | same | bit-identical |
| tiny-MDP blocked diff mean | 0.5815649999999999 | same | bit-identical |
| tiny-MDP novel diff mean | −0.27820000000000006 | same | bit-identical |
| 2c pooled ctrl mean | 0.5700703097685957 | same | bit-identical |
| 2c pooled ctrl 90% CI | [0.5588828079077731, 0.5814059421537342] | same | bit-identical |
| 2c pooled \|PE\| mean | 0.08680599180900767 | same | bit-identical |

All 10 checked primaries reproduced **bit-identically** (deterministic frozen code,
frozen seeds, frozen bootstrap RNGs). **No manuscript number differs beyond
rounding; nothing to correct in the body.**

## 3. Comparison with manuscript body (rounded values)

| manuscript (Section) | body value | re-check value | match |
|---|---|---|---|
| 3.4 macro-TV | 0.374, 95% CI [0.374, 0.375] | 0.3744 [0.3736, 0.3752] | ✓ (rounding) |
| 3.4 aligned / blocked / novel | +0.221 / +0.582 / −0.278 | +0.2209 / +0.5816 / −0.2782 | ✓ |
| 3.3 ctrl primary | 0.570, 90% CI [0.559, 0.581] | 0.5701 [0.5589, 0.5814] | ✓ |
| 3.3 \|PE\| equivalence | 0.087, 90% CI [0.082, 0.091] | 0.0868 [0.0824*, 0.0912*] | ✓ (*frozen CI, reproduced) |
| README/3.1 erosion (single-seed quote) | +0.74 → −5.53 (seed 11) | 5-seed mean +0.742±0.000 → −5.543±0.033 | ✓ consistent |

## 4. New robustness result (does not replace anything frozen)

**Phase 2c seed-clustered re-bootstrap** (average the two volatility cells per seed
first, then percentile bootstrap over the 40 seeds; B = 10,000, boot seed 777):

- ctrl: mean **0.570**, 90% CI **[0.566, 0.574]** — direction unchanged
  (mean > Δ_min = 0.20; CI lower bound ≫ 0). The seed-clustered interval is
  *tighter* than the frozen pooled interval because averaging the two volatility
  cells per seed removes the between-cell variance component.
- |PE|: mean **0.087**, 90% CI **[0.084, 0.089]** — remains inside the ±0.15
  equivalence bound.

Verdict: the audit-flagged bootstrap-unit limitation does **not** affect any
conclusion; the frozen pooled result stands as reported, with this re-check cited
as robustness support (Limitations item 3 remains accurate and now has a
quantitative companion).

## 5. Newly extracted quantities (previously deferred)

- **tiny-MDP role-aligned mean arrival four-vectors** [G_hist, G_other, G_novel, ∅]
  for active and yoked in all three battery classes (T4a in STATS_TABLES.md) —
  enables the planned Figure 5 four-bar panel.
- **Per-seed summary tables**: tiny-MDP (50 seeds: macro-TV, three direction
  diffs; T4b) and Phase 2c (40 seeds: per-volatility and per-seed paired diffs;
  T3a). Phase 2b per-seed values are not stored in its frozen JSON and were NOT
  re-derived (outside the authorized round) — noted in T2.
- **Phase 1 latent-erosion two points** (episode-end z vs end-of-observation z,
  frozen seeds 11–15): LatentInscription +0.742±0.000 → −5.543±0.033;
  C_anchor +1.534±0.000 → +3.322±0.000. Sufficient for the S4 supplementary
  panel as a two-point comparison; a full erosion *trace* is not extractable
  without editing frozen code and is therefore not produced.

## 6. Outcome

- STOP rule: **not triggered** (0 mismatches; 2c direction unchanged).
- Manuscript body: **unchanged by this re-check** (figure captions/panels updated
  separately per instruction, in their own commit).
- TODO status: extraction items 1–4 of ASSEMBLY_REVIEW §5 completed; item 5
  (2c re-bootstrap decision) resolved as robustness support.
