"""AUTHORIZED controlled deterministic extraction round (single run).

Purpose (pre-submission statistical re-check): extract quantities NOT stored in the
frozen results JSONs, using the ORIGINAL frozen code, configs, and seeds, imported
from external scripts. The frozen experiment files are NOT edited; this script lives
in the paper directory and only imports them.

Extracted here:
  (a) tiny-MDP: per-seed macro-TV and direction diffs; per-class four-vector arrival
      distributions [P(G0),P(G1),P(G2),P(EMPTY)] for active and yoked (Fig 5 panel);
  (b) Phase 2c: per-(seed,volatility) paired differences; NEW seed-clustered
      robustness re-bootstrap (average the two volatility cells per seed first, then
      bootstrap over the 40 seeds). The frozen pooled result is NOT modified.
  (c) Phase 1 (S4 supplementary): two-point latent-erosion comparison (episode-end z
      vs end-of-observation z) for LatentInscription and C_anchor, frozen seeds.

STOP RULE (per instruction): if any reproduced primary number differs from the
frozen JSON beyond rounding (1e-9), or the 2c seed-clustered result reverses the
basic direction, this script exits nonzero and the discrepancy is reported; the
manuscript is not to be touched in that case.

Provenance (commit, config hashes, seeds, command, script hash) is embedded in the
output `extraction_round.json`.
"""
from __future__ import annotations
import hashlib, importlib.util, json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
EXP = HERE.parent.parent / "Experiments"

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:16]

STOPS = []
def check_match(label, got, frozen, tol=1e-9):
    ok = abs(got - frozen) <= tol
    print(f"  [{'MATCH' if ok else 'MISMATCH'}] {label}: extracted={got!r} frozen={frozen!r}")
    if not ok:
        STOPS.append((label, got, frozen))

# ---------------- (a) tiny-MDP ----------------
print("== tiny-MDP extraction (frozen code/config/seeds) ==")
H = load_module("hx_mdp", EXP / "anchoring_tiny_mdp_confirmatory" / "holdout_mdp.py")
frozen_mdp = json.load(open(EXP / "anchoring_tiny_mdp_confirmatory" / "results_mdp_holdout.json"))
per_seed = []
vec_acc = {k: {"active": np.zeros(4), "yoked": np.zeros(4)} for k in ("aligned", "blocked", "novel")}
for s in H.SEEDS:
    h, other, novel = H.roles(s)
    act = H.M.formation("coupled", h, s, H.c)
    yok = H.M.formation("yoked", h, s, H.c, master_R=act["R"], act_offset=H.OFF)
    ba = H.battery(act["m"], h, other, novel, s)
    by = H.battery(yok["m"], h, other, novel, s)
    # role-align the goal axes so vectors are comparable across seeds:
    # order = [G_hist, G_other, G_novel, EMPTY]
    order = [h, other, novel, 3]
    for k in vec_acc:
        vec_acc[k]["active"] += np.asarray(ba[k])[order]
        vec_acc[k]["yoked"] += np.asarray(by[k])[order]
    per_seed.append(dict(
        seed=s, macro_tv=H.macro_tv(ba, by),
        d_aligned=float(ba["aligned"][h] - by["aligned"][h]),
        d_blocked=float(ba["blocked"][H.M.EMPTY] - by["blocked"][H.M.EMPTY]),
        d_novel=float(ba["novel"][novel] - by["novel"][novel]),
    ))
macro = [r["macro_tv"] for r in per_seed]
m_mean, m_lo, m_hi = H.boot_ci(macro, H.TH["ci_level"], H.TH["bootstrap_resamples"])
check_match("tiny-MDP macro-TV mean", m_mean, frozen_mdp["primary_macro_TV"]["mean"])
check_match("tiny-MDP macro-TV CI lo", m_lo, frozen_mdp["primary_macro_TV"]["ci"][0])
check_match("tiny-MDP macro-TV CI hi", m_hi, frozen_mdp["primary_macro_TV"]["ci"][1])
for key, col in [("aligned_active_adv", "d_aligned"), ("blocked_active_stickiness", "d_blocked"),
                 ("novel_active_stickiness", "d_novel")]:
    g_mean, g_lo, g_hi = H.boot_ci([r[col] for r in per_seed], H.TH["ci_level"], H.TH["bootstrap_resamples"])
    check_match(f"tiny-MDP {key} mean", g_mean, frozen_mdp["direction"][key][0])
fourvec = {k: {g: (vec_acc[k][g] / len(H.SEEDS)).round(6).tolist() for g in ("active", "yoked")}
           for k in vec_acc}

# ---------------- (b) Phase 2c ----------------
print("== Phase 2c extraction + seed-clustered robustness re-bootstrap ==")
C2 = load_module("hx_2c", EXP / "anchoring_2c_controllability" / "holdout2c.py")
frozen_2c = json.load(open(EXP / "anchoring_2c_controllability" / "results_2c_holdout.json"))
rows2c = []
for s in C2.SEEDS:
    row = {"seed": s}
    for vol in ("high", "low"):
        a_c, y_c = C2.pair(s, vol, "ctrl")
        a_p, y_p = C2.pair(s, vol, "pe")
        row[f"d_ctrl_{vol}"] = float(C2.commit(a_c) - C2.commit(y_c))
        row[f"d_pe_{vol}"] = float(C2.commit(a_p) - C2.commit(y_p))
    row["d_ctrl_seed"] = 0.5 * (row["d_ctrl_high"] + row["d_ctrl_low"])
    row["d_pe_seed"] = 0.5 * (row["d_pe_high"] + row["d_pe_low"])
    rows2c.append(row)
pooled_ctrl = [r[f"d_ctrl_{v}"] for v in ("high", "low") for r in rows2c]
pc_mean, pc_lo, pc_hi = C2.boot_ci(pooled_ctrl, C2.PRE["ci_level"], C2.PRE["bootstrap_resamples"])
# NOTE: frozen pooling order was rows["high"]+rows["low"]; replicate exactly:
pooled_ctrl = [r[f"d_ctrl_{v}"] for v in ("high", "low") for r in rows2c]
check_match("2c pooled ctrl mean", pc_mean, frozen_2c["primary_ctrl"]["mean"])
check_match("2c pooled ctrl CI lo", pc_lo, frozen_2c["primary_ctrl"]["ci_lo"])
check_match("2c pooled ctrl CI hi", pc_hi, frozen_2c["primary_ctrl"]["ci_hi"])
pooled_pe = [r[f"d_pe_{v}"] for v in ("high", "low") for r in rows2c]
pe_mean, pe_lo, pe_hi = C2.boot_ci(pooled_pe, C2.PRE["ci_level"], C2.PRE["bootstrap_resamples"])
check_match("2c pooled pe mean", pe_mean, frozen_2c["negative_pe"]["mean"])
# seed-clustered robustness (NEW, does not replace frozen result):
def boot_seed(vals, level=0.90, B=10_000, seed=777):
    vals = np.asarray(vals); rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(vals), size=(B, len(vals)))
    means = vals[idx].mean(axis=1)
    return (float(vals.mean()),
            float(np.percentile(means, 100 * (1 - level) / 2)),
            float(np.percentile(means, 100 * (1 + level) / 2)))
sc_ctrl = boot_seed([r["d_ctrl_seed"] for r in rows2c])
sc_pe = boot_seed([r["d_pe_seed"] for r in rows2c])
print(f"  seed-clustered ctrl: mean={sc_ctrl[0]:.3f} 90%CI=[{sc_ctrl[1]:.3f},{sc_ctrl[2]:.3f}]"
      f"  (frozen pooled: {pc_mean:.3f} [{pc_lo:.3f},{pc_hi:.3f}])")
print(f"  seed-clustered pe  : mean={sc_pe[0]:.3f} 90%CI=[{sc_pe[1]:.3f},{sc_pe[2]:.3f}]")
if not (sc_ctrl[0] > C2.PRE["Delta_min"] and sc_ctrl[1] > 0):
    STOPS.append(("2c seed-clustered direction reversed", sc_ctrl, "expected mean>Delta_min, lo>0"))
if not (-C2.PRE["eps_equiv_commit"] <= sc_pe[0] <= C2.PRE["eps_equiv_commit"]):
    STOPS.append(("2c seed-clustered |PE| outside equivalence", sc_pe, "expected within +-0.15"))

# ---------------- (c) Phase 1 latent erosion (two-point, frozen seeds) ----------------
print("== Phase 1 latent-erosion two-point extraction ==")
DW = load_module("dw_model", EXP / "anchoring_double_well" / "model.py")
P1 = json.load(open(EXP / "anchoring_double_well" / "config.json"))
erosion = {}
for cond_name in ("LatentInscription", "C_anchor"):
    zi, zf = [], []
    for s in P1["seeds"]:
        r = DW.simulate(P1, P1["conditions"][cond_name], +1, s)
        zi.append(r["z_after_int"]); zf.append(r["z_final"])
    erosion[cond_name] = {"z_episode_mean": float(np.mean(zi)), "z_episode_sd": float(np.std(zi)),
                          "z_final_mean": float(np.mean(zf)), "z_final_sd": float(np.std(zf))}
    print(f"  {cond_name}: z_episode={np.mean(zi):+.3f}±{np.std(zi):.3f} -> "
          f"z_final={np.mean(zf):+.3f}±{np.std(zf):.3f}")

# ---------------- provenance + output ----------------
head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True,
                      cwd=HERE).stdout.strip()
out = {
    "provenance": {
        "datetime_utc": datetime.now(timezone.utc).isoformat(),
        "git_head": head,
        "command": "python3 extraction_round.py",
        "script_sha256_16": sha(__file__),
        "frozen_configs": {
            "tiny_mdp": sha(EXP / "anchoring_tiny_mdp_confirmatory" / "config_mdp_frozen.json"),
            "2c": sha(EXP / "anchoring_2c_controllability" / "config2c_frozen.json"),
            "double_well": sha(EXP / "anchoring_double_well" / "config.json"),
        },
        "seeds": {"tiny_mdp": [H.SEEDS[0], H.SEEDS[-1]], "2c": [C2.SEEDS[0], C2.SEEDS[-1]],
                  "double_well": P1["seeds"]},
        "frozen_files_edited": "NONE",
    },
    "tiny_mdp": {"per_seed": per_seed, "fourvec_rolealigned": fourvec,
                 "fourvec_axis": ["G_hist", "G_other", "G_novel", "EMPTY"],
                 "reproduced_primary": {"mean": m_mean, "ci": [m_lo, m_hi]}},
    "phase2c": {"per_seed": rows2c,
                "reproduced_pooled_ctrl": {"mean": pc_mean, "ci": [pc_lo, pc_hi]},
                "reproduced_pooled_pe": {"mean": pe_mean, "ci": [pe_lo, pe_hi]},
                "seed_clustered_ctrl": {"mean": sc_ctrl[0], "ci90": [sc_ctrl[1], sc_ctrl[2]],
                                        "B": 10000, "boot_seed": 777},
                "seed_clustered_pe": {"mean": sc_pe[0], "ci90": [sc_pe[1], sc_pe[2]]}},
    "phase1_erosion": erosion,
    "stop_rule": {"triggered": bool(STOPS), "items": [str(s) for s in STOPS]},
}
(HERE / "extraction_round.json").write_text(json.dumps(out, indent=2))
print(f"\nwrote extraction_round.json  (STOPs: {len(STOPS)})")
if STOPS:
    print(">>> STOP RULE TRIGGERED — do not touch the manuscript; report. <<<")
    sys.exit(1)
print(">>> extraction round clean: all reproduced primaries match frozen values. <<<")
