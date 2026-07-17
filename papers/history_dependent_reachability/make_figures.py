"""Generate manuscript figures. READ-ONLY over Experiments/ frozen JSONs plus
extraction_round.json (the single authorized deterministic extraction round).

Rules: every plotted number comes from a frozen results JSON or from
extraction_round.json (schematic panels carry no data). The previously deferred
panels (Fig 5 A–C four-vector arrivals, panel F per-seed distribution; S4 two-point
latent erosion) are now sourced from the extraction round.

Run from this directory:  python3 make_figures.py
Outputs: figures/fig{1..5}.{png,pdf}, figures/s{1..4}.{png,pdf}
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

HERE = Path(__file__).resolve().parent
EXP = HERE.parent.parent / "Experiments"
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)

def load(rel):
    return json.load(open(EXP / rel))

def save(fig, name):
    for ext in ("png", "pdf"):
        fig.savefig(OUT / f"{name}.{ext}", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote figures/{name}.png/.pdf")

C_ACT, C_YOK, C_NEG, C_OK, C_GRAY = "#2b6cb0", "#b7791f", "#9b2c2c", "#276749", "#4a5568"

# ---------------------------------------------------------------- Figure 1
def fig1():
    mf = load("anchoring_double_well/results_matched_future.json")
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(11, 3.6), gridspec_kw={"width_ratios": [1.5, 1]})
    ax.axis("off")
    boxes = [("history", "selection–\nconsequence", 0.08),
             ("$r_t$", "$\\mu$-mixture\nLLR", 0.28),
             ("$z$", "write\nstrength", 0.46),
             ("$m$", "path\ncontent", 0.64),
             ("$\\Gamma'_H$", "future reachable\noutcomes", 0.86)]
    bw = 0.13
    for main, sub, x in boxes:
        ax.add_patch(Rectangle((x - bw / 2, 0.44), bw, 0.24, fill=True,
                               fc="#edf2f7", ec=C_GRAY, lw=1.2))
        ax.text(x, 0.56, main, ha="center", va="center", fontsize=11)
        ax.text(x, 0.36, sub, ha="center", va="top", fontsize=7.5, color=C_GRAY)
    for (_, _, xa), (_, _, xb) in zip(boxes[:-1], boxes[1:]):
        ax.add_patch(FancyArrowPatch((xa + bw / 2 + 0.005, 0.56), (xb - bw / 2 - 0.005, 0.56),
                                     arrowstyle="-|>", mutation_scale=14, color=C_GRAY))
    ax.text(0.46, 0.10, "z gates HOW STRONGLY;  m stores WHAT;  only m is read at test",
            ha="center", fontsize=9, style="italic")
    ax.text(0.46, 0.90, "$x_A = x_B$ (matched present),  $m_A \\neq m_B$  $\\Rightarrow$  "
            "$P_A(\\mathrm{future}) \\neq P_B(\\mathrm{future})$", ha="center", fontsize=11)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_title("A  Framework and core statement", loc="left", fontsize=11)

    # inset: S1 matched-present -> different-future raw probabilities
    pa = mf["raw_future_Pplus"]["anchor"]; pn = mf["raw_future_Pplus"]["naive"]
    ax2.bar([0, 1], [pn, pa], color=[C_GRAY, C_ACT], width=0.55)
    for xi, v in [(0, pn), (1, pa)]:
        ax2.text(xi, v + 0.03, "%.3f" % v, ha="center", fontsize=9)
    ax2.set_xticks([0, 1]); ax2.set_xticklabels(["naive\n(no history)", "anchored\n(written $z$)"])
    ax2.set_ylabel("raw future $P(M^+)$"); ax2.set_ylim(0, 1.05)
    ax2.set_title("B  S1: matched present (gap = %.4f)" % mf["present_state_gap"],
                  loc="left", fontsize=11)
    ax2.text(0.5, 0.5, "TV = %.3f\nJS = %.3f" % (mf["divergences"]["TV"], mf["divergences"]["JS"]),
             transform=ax2.transAxes, ha="center", fontsize=9)
    save(fig, "fig1")

# ---------------------------------------------------------------- Figure 2
def fig2():
    d = load("anchoring_double_well/results_dissociation.json")["results"]
    sw = load("anchoring_double_well/results_sweep.json")
    fig, axs = plt.subplots(2, 2, figsize=(11, 8.2))
    axA, axB, axC, axD = axs.ravel()

    # A: P x W_sel plane. Co-located pairs — (0,0): A_transient + RoughenWrite;
    # (0,1): PreExistingWell + B_clamp(held) — rendered as hollow ring + filled marker.
    ring = dict(facecolors="none", s=320, linewidths=2.2, zorder=3)
    axA.scatter([0], [0], edgecolors=C_GRAY, marker="o", label="A_transient (ring)", **ring)
    r = d["RoughenWrite"]
    axA.scatter(r["Wsel"]["occupancy"], r["P_survival"], c="#805ad5", marker="D",
                s=80, zorder=4, label="RoughenWrite")
    axA.scatter([0], [1], edgecolors="#b7791f", marker="o", label="PreExistingWell (ring)", **ring)
    bc = d["B_clamp"]
    axA.scatter([bc["Wsel"]["occupancy"]], [1.0], c="k", marker="x", s=70, zorder=4,
                label="B_clamp (held)")
    li = d["LatentInscription"]
    axA.scatter(li["Wsel"]["occupancy"], li["P_survival"], c="#dd6b20", marker="^",
                s=110, zorder=3, label="LatentInscription")
    ca = d["C_anchor"]
    axA.scatter(ca["Wsel"]["occupancy"], ca["P_survival"], c=C_OK, marker="*",
                s=200, zorder=3, label="C_anchor")
    axA.annotate("clamp: withdrawal\n$\\to$ P = %.2f" % bc["P_after_withdraw"],
                 xy=(0.02, 0.98), xytext=(0.22, 0.74), fontsize=8,
                 arrowprops=dict(arrowstyle="->", color="k"))
    axA.axhline(0.5, ls="--", c="#cbd5e0", lw=1); axA.axvline(0.5, ls="--", c="#cbd5e0", lw=1)
    axA.set_xlabel("$W_{sel}$ (occupancy functional)"); axA.set_ylabel("persistence  $P$")
    axA.set_xlim(-0.12, 1.12); axA.set_ylim(-0.08, 1.12)
    axA.legend(fontsize=7, loc="center right")
    axA.set_title("A  P × $W_{sel}$: four cells occupied (dissociation, not independence)",
                  loc="left", fontsize=10)

    # B: costs do not track W_sel
    names = ["A_transient", "PreExistingWell", "RoughenWrite", "LatentInscription", "C_anchor", "B_clamp"]
    jw = [d[n]["J_write"] for n in names]; je = [d[n]["J_ext"] for n in names]
    x = np.arange(len(names))
    axB.bar(x - 0.2, je, 0.4, label="$J_{ext}$", color=C_GRAY)
    axB.bar(x + 0.2, jw, 0.4, label="$J_{write}$", color="#805ad5")
    axB.set_xticks(x)
    axB.set_xticklabels(names, fontsize=7, rotation=25, ha="right")
    axB.set_ylabel("cost"); axB.legend(fontsize=8)
    axB.set_title("B  Neither cost tracks $W_{sel}$ (max $J_{write}$ = nonspecific control)",
                  loc="left", fontsize=10)

    # C/D: phase diagrams (cells are regions)
    cmap = {(0, 0): "#e2e8f0", (1, 0): "#f6e05e", (0, 1): "#fbb6ce", (1, 1): "#68d391"}
    for ax, key, ttl in [(axC, "anchor", "C  Sweep: anchor (deepen, $c_0=-0.5$)"),
                         (axD, "latent", "D  Sweep: latent protocol ($c_0=0$)")]:
        g = sw[key]; grid = g["grid"]
        img = np.zeros((len(g["D0s"]), len(g["etas"]), 3))
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                img[i, j] = matplotlib.colors.to_rgb(cmap[(cell[0], cell[1])])
        ax.imshow(img, aspect="auto", origin="upper",
                  extent=[g["etas"][0], g["etas"][-1], g["D0s"][-1], g["D0s"][0]])
        ax.set_xlabel("$\\eta$ (write rate)"); ax.set_ylabel("$D_0$ (noise)")
        ax.set_title(ttl + "  — largest region: P+W+ %d / P−W+ %d"
                     % (g["largest_region"]["11"], g["largest_region"]["01"]),
                     loc="left", fontsize=10)
    handles = [Rectangle((0, 0), 1, 1, fc=cmap[k]) for k in [(0, 0), (1, 0), (0, 1), (1, 1)]]
    axD.legend(handles, ["P− W−", "P+ W− (hold)", "P− W+ (latent)", "P+ W+ (anchor)"],
               fontsize=7, loc="lower right")
    fig.tight_layout()
    save(fig, "fig2")

# ---------------------------------------------------------------- Figure 3
def fig3():
    b = load("anchoring_bandit_holdout/results_phase2b.json")
    c = load("anchoring_2c_controllability/results_2c_holdout.json")
    fig, (axA, axB, axC) = plt.subplots(1, 3, figsize=(12, 3.8))

    # A: Phase 2b NO-GO (its own data only)
    av = b["active_vs_yoked"]
    axA.bar([0, 1], [av["fut_active_mean"], av["fut_yoked_mean"]],
            color=[C_ACT, C_YOK], width=0.55)
    axA.set_xticks([0, 1]); axA.set_xticklabels(["active", "yoked"])
    axA.set_ylabel("future effect (early recovery diff)")
    axA.set_ylim(0, 0.32)
    axA.text(0.5, 0.9, "d = %.2f" % av["fut_cohen_d_active_vs_yoked"],
             transform=axA.transAxes, ha="center", fontsize=10)
    axA.set_title("A  Phase 2b (NO-GO): $|PE| \\to z$\nyoked reproduces the effect",
                  loc="left", fontsize=10)
    axA.text(0.5, -0.28, "source: results_phase2b.json (40 fresh seeds, frozen params)",
             transform=axA.transAxes, ha="center", fontsize=7, style="italic")

    # B: Phase 2c |PE| pre-registered equivalence test (2c data only)
    n = c["negative_pe"]
    axB.axhspan(-n["eps"], n["eps"], color="#c6f6d5", alpha=0.6, label="±%.2f equivalence bound" % n["eps"])
    axB.errorbar([0], [n["mean"]], yerr=[[n["mean"] - n["ci_lo"]], [n["ci_hi"] - n["mean"]]],
                 fmt="o", color=C_NEG, capsize=6, ms=8)
    axB.axhline(0, color=C_GRAY, lw=0.8)
    axB.set_xlim(-0.7, 0.7); axB.set_ylim(-0.2, 0.7); axB.set_xticks([])
    axB.set_ylabel("paired active−yoked commitment")
    axB.legend(fontsize=8, loc="upper right")
    axB.set_title("B  Phase 2c: $|PE|$ baseline\npre-registered equivalence (0.087)",
                  loc="left", fontsize=10)
    axB.text(0.5, -0.28, "source: results_2c_holdout.json (equivalence test within 2c)",
             transform=axB.transAxes, ha="center", fontsize=7, style="italic")

    # C: Phase 2c controllability GO (same 2c source)
    p = c["primary_ctrl"]
    axC.errorbar([0], [p["mean"]], yerr=[[p["mean"] - p["ci_lo"]], [p["ci_hi"] - p["mean"]]],
                 fmt="o", color=C_OK, capsize=6, ms=8)
    axC.axhline(p["Delta_min"], color=C_NEG, ls="--", lw=1.2,
                label="$\\Delta_{min}$ = %.2f" % p["Delta_min"])
    axC.axhline(0, color=C_GRAY, lw=0.8)
    axC.set_xlim(-0.7, 0.7); axC.set_ylim(-0.05, 0.7); axC.set_xticks([])
    axC.set_ylabel("paired active−yoked commitment")
    axC.legend(fontsize=8, loc="lower right")
    axC.set_title("C  Phase 2c (GO): $r_t^{action} \\to z$\n0.570, 90% CI [0.559, 0.581]",
                  loc="left", fontsize=10)
    axC.text(0.5, -0.28, "source: results_2c_holdout.json (40 fresh seeds, frozen params)",
             transform=axC.transAxes, ha="center", fontsize=7, style="italic")
    fig.tight_layout()
    save(fig, "fig3")

# ---------------------------------------------------------------- Figure 4
def fig4():
    m = load("anchoring_tiny_mdp_confirmatory/results_mdp_holdout.json")
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(11, 3.8), gridspec_kw={"width_ratios": [2, 1]})
    ax.axis("off")
    stages = [("FORMATION\nactive / master-yoked /\nexternal-action sham", 0.10),
              ("MATCH\nreset state + Q\n(action dist matched)\nONLY m carried", 0.42),
              ("FROZEN BATTERY\naligned / blocked / novel\n(roles counterbalanced)", 0.76)]
    for label, x in stages:
        ax.add_patch(Rectangle((x - 0.13, 0.30), 0.26, 0.42, fill=True, fc="#edf2f7", ec=C_GRAY, lw=1.2))
        ax.text(x, 0.51, label, ha="center", va="center", fontsize=8.5)
    for x0, x1 in [(0.23, 0.29), (0.55, 0.63)]:
        ax.add_patch(FancyArrowPatch((x0, 0.51), (x1, 0.51), arrowstyle="-|>",
                                     mutation_scale=14, color=C_GRAY))
    ax.text(0.42, 0.12, "formation $q, z$, counters, traces are never read at test\n"
            "(code-verified; same-$m$/diff-$z$ = 0 — implementation-level pipeline check,\n"
            "not independent causal evidence)", ha="center", fontsize=8, style="italic")
    ax.text(0.42, 0.88, "terminal distribution: $[P(G_0), P(G_1), P(G_2), P(\\varnothing)]$"
            "  ($\\varnothing$ = timeout / non-arrival)", ha="center", fontsize=9)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_title("A  tiny-MDP protocol (only-m carry, matched present)", loc="left", fontsize=11)

    sh = m["sham"]
    ax2.bar([0, 1], [sh["self_attr"], sh["ext_attr"]], color=[C_GRAY, C_ACT], width=0.55)
    ax2.axhline(0, color="k", lw=0.8)
    ax2.set_xticks([0, 1]); ax2.set_xticklabels(["self-\nattribution", "external-\nattribution"])
    ax2.set_ylabel("attribution score")
    ax2.set_title("B  Sham mechanism gate\nself ≈ 0, ext > 0", loc="left", fontsize=11)
    fig.tight_layout()
    save(fig, "fig4")

# ---------------------------------------------------------------- Figure 5
def fig5():
    m = load("anchoring_tiny_mdp_confirmatory/results_mdp_holdout.json")
    ex = json.load(open(HERE / "extraction_round.json"))
    dr = m["direction"]; pm = m["primary_macro_TV"]
    fv = ex["tiny_mdp"]["fourvec_rolealigned"]
    fig, axs = plt.subplots(2, 3, figsize=(11.5, 7.2),
                            gridspec_kw={"height_ratios": [1, 1.1]})
    # --- top row A-C: role-aligned arrival four-vectors per battery class ---
    cats = ["$G_{hist}$", "$G_{other}$", "$G_{novel}$", "$\\varnothing$"]
    for ax, (cls, letter) in zip(axs[0], [("aligned", "A"), ("blocked", "B"), ("novel", "C")]):
        x = np.arange(4)
        ax.bar(x - 0.19, fv[cls]["active"], 0.38, color=C_ACT, label="active")
        ax.bar(x + 0.19, fv[cls]["yoked"], 0.38, color=C_YOK, label="yoked")
        ax.set_xticks(x); ax.set_xticklabels(cats, fontsize=9)
        ax.set_ylim(0, 1.0); ax.set_ylabel("arrival probability" if cls == "aligned" else "")
        ax.set_title(f"{letter}  {cls}", loc="left", fontsize=10)
        if cls == "aligned":
            ax.legend(fontsize=8)
    # --- bottom left/middle (merged look): direction diffs ---
    axD, axE, axF = axs[1]
    labels = ["aligned\n$\\Delta P(G_h)$", "blocked\n$\\Delta P(\\varnothing)$",
              "novel\n$\\Delta P(G_{novel})$"]
    keys = ["aligned_active_adv", "blocked_active_stickiness", "novel_active_stickiness"]
    means = [dr[k][0] for k in keys]
    err = np.array([[dr[k][0] - dr[k][1] for k in keys], [dr[k][2] - dr[k][0] for k in keys]])
    cols = [C_OK, "#dd6b20", "#dd6b20"]
    axD.bar(range(3), means, 0.55, color=cols, yerr=err, capsize=5)
    axD.axhline(0, color="k", lw=0.9)
    axD.set_xticks(range(3)); axD.set_xticklabels(labels, fontsize=8.5)
    axD.set_ylabel("active − yoked (paired)")
    axD.set_title("D  Direction gates (95% CIs,\npre-registered sides)", loc="left", fontsize=10)

    axE.errorbar([0], [pm["mean"]], yerr=[[pm["mean"] - pm["ci"][0]], [pm["ci"][1] - pm["mean"]]],
                 fmt="o", color=C_ACT, capsize=6, ms=9)
    axE.axhline(pm["Delta_min"], color=C_NEG, ls="--", lw=1.2,
                label="$\\Delta_{min}$ = %.2f" % pm["Delta_min"])
    axE.set_xlim(-0.7, 0.7); axE.set_ylim(0, 0.45); axE.set_xticks([])
    axE.set_ylabel("macro-TV (equal-weight)")
    axE.legend(fontsize=8, loc="lower right")
    axE.set_title("E  Primary: macro-TV 0.374\n95% CI [0.374, 0.375]", loc="left", fontsize=10)

    # per-seed macro-TV distribution (extraction round); zoomed to data range —
    # Delta_min = 0.15 lies far below the axis (stated in annotation instead).
    mseeds = [r["macro_tv"] for r in ex["tiny_mdp"]["per_seed"]]
    axF.hist(mseeds, bins=12, color=C_GRAY, edgecolor="white")
    axF.set_xlabel("per-seed macro-TV (50 seeds)"); axF.set_ylabel("count")
    axF.text(0.03, 0.92, "all 50 seeds $\\gg$ $\\Delta_{min}$ = 0.15\n(axis zoomed to data)",
             transform=axF.transAxes, fontsize=8, style="italic")
    axF.set_title("F  Per-seed distribution\n(extraction round)", loc="left", fontsize=10)
    fig.tight_layout()
    save(fig, "fig5")

# ------------------------------------------------- Supplementary S4 (erosion, two-point)
def s4():
    ex = json.load(open(HERE / "extraction_round.json"))
    er = ex["phase1_erosion"]
    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    conds = ["LatentInscription", "C_anchor"]
    cols = {"LatentInscription": "#dd6b20", "C_anchor": C_OK}
    for i, cnd in enumerate(conds):
        v = er[cnd]
        ax.plot([0, 1], [v["z_episode_mean"], v["z_final_mean"]], "o-",
                color=cols[cnd], label=cnd, ms=8)
        ax.errorbar([0, 1], [v["z_episode_mean"], v["z_final_mean"]],
                    yerr=[v["z_episode_sd"], v["z_final_sd"]], fmt="none",
                    ecolor=cols[cnd], capsize=4)
    ax.axhline(0, color=C_GRAY, lw=0.8)
    ax.set_xlim(-0.3, 1.3); ax.set_xticks([0, 1])
    ax.set_xticklabels(["episode end\n($z_{episode}$)", "end of observation\n($z_{final}$)"])
    ax.set_ylabel("slow variable $z$ (ensemble mean)")
    ax.legend(fontsize=9)
    ax.set_title("S4  State-tracking erosion of an off-target write (two-point,\n"
                 "frozen seeds 11–15): latent write erodes; anchored write consolidates",
                 loc="left", fontsize=9.5)
    fig.tight_layout(); save(fig, "s4")

# ---------------------------------------------------------------- Supplementary
def s1():
    b = load("anchoring_bandit_holdout/results_phase2b.json")
    wc = b["washout_curves"]
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    ax.plot(wc["wash_steps"], wc["retained"], "o-", color=C_ACT, label="z-gap retained fraction")
    ax.plot(wc["wash_steps"], wc["fut_diff"], "s--", color="#805ad5", label="future effect (vol−stable)")
    ax.set_xlabel("washout steps (unexpressive)"); ax.set_ylabel("value")
    ax.legend(fontsize=9); ax.set_title("S1  Phase 2b washout-length curves", loc="left", fontsize=10)
    fig.tight_layout(); save(fig, "s1")

def s2():
    m = load("anchoring_tiny_mdp_confirmatory/results_mdp_holdout.json")
    c = load("anchoring_2c_controllability/results_2c_holdout.json")
    eps = m["locked_thresholds"]["eps_TV"]
    mn, ms, sz = m["memory_null_macroTV"], m["memory_swap_macroTV"], m["same_m_diff_z_macroTV"]
    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    ax.axhspan(-eps, eps, color="#c6f6d5", alpha=0.6, label="±%.2f equivalence bound" % eps)
    items = [("memory-null", mn), ("memory-swap", ms), ("same-m/diff-z", sz)]
    for i, (lab, v) in enumerate(items):
        ax.errorbar([i], [v[0]], yerr=[[v[0] - v[1]], [v[2] - v[0]]], fmt="o",
                    color=C_GRAY, capsize=5, ms=7)
    ax.set_xticks(range(3)); ax.set_xticklabels([i[0] for i in items], fontsize=9)
    ax.set_ylabel("macro-TV"); ax.set_ylim(-0.07, 0.1)
    ax.legend(fontsize=8)
    ax.set_title("S2  PIPELINE VALIDATION (tiny-MDP): verifies only-m plumbing;\n"
                 "NOT independent causal evidence (swap mechanical; null architecture-bound)",
                 loc="left", fontsize=9)
    fig.tight_layout(); save(fig, "s2")

def s3():
    b = load("anchoring_bandit_holdout/results_phase2b.json")
    pm = b["permutation"]
    fig, ax = plt.subplots(figsize=(5.6, 3.8))
    ax.bar([0, 1], [pm["corr_perm_recovery_vs_permz"], pm["corr_perm_recovery_vs_label"]],
           color=[C_ACT, C_GRAY], width=0.5)
    ax.set_xticks([0, 1]); ax.set_xticklabels(["recovery ~ carried z\n(permuted)", "recovery ~ history label\n(permuted)"], fontsize=9)
    ax.set_ylabel("correlation")
    ax.set_title("S3  Phase 2b permutation: effect follows z, not the label", loc="left", fontsize=10)
    fig.tight_layout(); save(fig, "s3")

if __name__ == "__main__":
    fig1(); fig2(); fig3(); fig4(); fig5(); s1(); s2(); s3(); s4()
    print("done")
