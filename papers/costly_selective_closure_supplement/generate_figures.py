"""
Regenerate Figures 1-3 for the Costly Selective Closure paper.

All quantitative content in Figure 3 is read from the committed result files in
results/; nothing is hand-entered. Figures 1 and 2 are conceptual schematics
(no calibrated numbers). Each figure is written as SVG, PDF, and PNG (300 dpi).

Usage:
    python generate_figures.py

Requires: numpy, matplotlib (see requirements.txt).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

matplotlib.rcParams.update({
    "font.family": "DejaVu Sans",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",
    "axes.linewidth": 0.8,
})

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"
FIGS = HERE / "figures"
FIGS.mkdir(exist_ok=True)

C_REAL = "#1f6fb2"       # real-stake
C_RESET = "#d6604d"      # resettable
C_SIM = "#7f7f7f"        # simulated-stake (auxiliary)
C_BOX = "#f2f2ee"
C_EDGE = "#3a3a3a"


def load(name):
    return json.load(open(RESULTS / name, encoding="utf-8"))


def save(fig, stem):
    for ext in ("svg", "pdf", "png"):
        fig.savefig(FIGS / f"{stem}.{ext}", dpi=300, bbox_inches="tight",
                    facecolor="white")
    plt.close(fig)
    print(f"wrote figures/{stem}.svg/.pdf/.png")


def bootstrap_ci(x, n_boot=10000, alpha=0.05, seed=0):
    x = np.asarray(x, float)
    rng = np.random.default_rng(seed)
    boot = rng.choice(x, size=(n_boot, len(x)), replace=True).mean(axis=1)
    lo, hi = np.percentile(boot, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    return float(x.mean()), float(lo), float(hi)


def paired_signflip_p(main, n_resamples=20000, seed=0):
    """Main test: two-sided paired sign-flip permutation on the per-seed
    real - resettable differences (real and resettable share seeds). Also
    returns the pooled/unpaired permutation p (from the result file) for
    comparison."""
    real = {r["seed"]: r["post_coop"] for r in main["runs"] if r["regime"] == "real"}
    reset = {r["seed"]: r["post_coop"] for r in main["runs"] if r["regime"] == "resettable"}
    seeds = sorted(set(real) & set(reset))
    diffs = np.array([real[s] - reset[s] for s in seeds])
    obs = diffs.mean()
    rng = np.random.default_rng(seed)
    perm = (rng.choice([-1.0, 1.0], size=(n_resamples, len(diffs))) * diffs).mean(axis=1)
    p_paired = (np.sum(np.abs(perm) >= abs(obs) - 1e-12) + 1) / (n_resamples + 1)
    p_unpaired = main["tests"]["real_vs_resettable__post_coop"]["p"]
    return len(seeds), float(p_paired), float(p_unpaired)


def _box(ax, x, y, w, h, text, *, dashed=False, fc=C_BOX, fs=10, ec=C_EDGE, weight="normal", ha="center"):
    style = "round,pad=0.02,rounding_size=0.12"
    patch = FancyBboxPatch((x, y), w, h, boxstyle=style, linewidth=1.3,
                           edgecolor=ec, facecolor=fc,
                           linestyle="--" if dashed else "-")
    ax.add_patch(patch)
    tx = x + 0.18 if ha == "left" else x + w / 2
    ax.text(tx, y + h / 2, text, ha=ha, va="center", fontsize=fs, weight=weight)


def _arrow(ax, xy_from, xy_to, dashed=False, color=C_EDGE, lw=1.4):
    ax.add_patch(FancyArrowPatch(xy_from, xy_to, arrowstyle="-|>", mutation_scale=14,
                                 linewidth=lw, color=color,
                                 linestyle="--" if dashed else "-",
                                 shrinkA=2, shrinkB=2))


# ---------------------------------------------------------------- Figure 1
def figure1_framework():
    fig, ax = plt.subplots(figsize=(7.4, 7.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10.6); ax.axis("off")

    # center
    _box(ax, 3.6, 6.7, 2.8, 1.3, "Costly\nSelective Closure", fc="#e8eef4",
         fs=12, weight="bold")

    dims = [
        ("$d$  selective bandwidth", "how many task-relevant\ndimensions matter",
         (3.6, 9.15, 2.8, 1.0), (5.0, 8.0), (5.0, 9.15)),
        ("$\\Psi_f$  maintenance cost", "maintenance burden borne\nby the token system",
         (0.15, 6.75, 3.05, 1.15), (3.6, 7.35), (3.2, 7.325)),
        ("$\\eta$  hysteretic memory", "how prior selections\nconstrain present organization",
         (6.85, 6.75, 3.05, 1.15), (6.4, 7.35), (6.85, 7.325)),
        ("$V$  irreversible vulnerability", "whether failure is\nnon-cheaply reversible",
         (3.4, 4.35, 3.2, 1.0), (5.0, 6.7), (5.0, 5.35)),
    ]
    for title, desc, (x, y, w, h), a0, a1 in dims:
        _box(ax, x, y, w, h, f"{title}\n{desc}", fs=8.6)
        _arrow(ax, a0, a1, color="#888")

    # passive vs active closure spectrum
    _box(ax, 0.3, 2.1, 4.2, 1.4,
         "Passive closure\nexternally buffered / low stake", fc="#f6efe8", fs=9.5)
    _box(ax, 5.5, 2.1, 4.2, 1.4,
         "Active closure\nmaintained under cost, history,\nand consequential failure",
         fc="#e8f2ec", fs=9.5)
    _arrow(ax, (4.6, 2.8), (5.4, 2.8))
    ax.text(5.0, 3.75, "more costly selective closure  →", ha="center",
            fontsize=9, style="italic", color="#555")

    ax.text(5.0, 0.7, "Schematic profiles; not calibrated measurements.",
            ha="center", fontsize=9.5, style="italic", color="#333")
    save(fig, "figure1_framework")


# ---------------------------------------------------------------- Figure 2
def _flowbox(ax, cx, cy, w, h, title, subtitle="", *, fc=C_BOX, ec=C_EDGE,
             dashed=False, title_fs=13, sub_fs=11, title_color="#1a1a1a",
             sub_color="#333", title_weight="bold", zorder=2):
    """Rounded box centred at (cx, cy) with a bold title and optional subtitle."""
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                                boxstyle="round,pad=0.02,rounding_size=0.09",
                                linewidth=1.5, edgecolor=ec, facecolor=fc,
                                linestyle="--" if dashed else "-", zorder=zorder))
    if subtitle:
        ax.text(cx, cy + h * 0.21, title, ha="center", va="center", fontsize=title_fs,
                weight=title_weight, color=title_color, zorder=zorder + 1)
        ax.text(cx, cy - h * 0.20, subtitle, ha="center", va="center", fontsize=sub_fs,
                color=sub_color, zorder=zorder + 1)
    else:
        ax.text(cx, cy, title, ha="center", va="center", fontsize=title_fs,
                weight=title_weight, color=title_color, zorder=zorder + 1)


def figure2_design():
    """Compact, near-square experimental-design schematic. The single-variable
    real-vs-resettable contrast is the visual centre; simulated-stake is a
    de-emphasised auxiliary condition derived from resettable. No calibrated
    numbers; the long matched-comparison sentence lives in the paper caption."""
    fig, ax = plt.subplots(figsize=(7.2, 4.7))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6.55); ax.axis("off")

    # shared setup (top, short)
    _flowbox(ax, 5.0, 5.95, 7.7, 1.02, "Shared setup",
             "same observations, reward, energy dynamics,\nnetwork, and seeds",
             fc="#eef2f7", title_fs=12.5, sub_fs=10.5)

    # clean causal comparison: two equal, side-by-side main boxes inside a bracket
    ax.add_patch(FancyBboxPatch((0.5, 3.35), 9.0, 2.25,
                                boxstyle="round,pad=0.02,rounding_size=0.07",
                                linewidth=1.2, edgecolor="#555", facecolor="none",
                                linestyle=(0, (5, 3)), zorder=1))
    _flowbox(ax, 2.75, 4.55, 3.7, 1.4, "Real-stake", "depletion terminates\nthe token run",
             fc="#e7eff6", ec=C_REAL, title_fs=13, sub_fs=11, title_color=C_REAL)
    _flowbox(ax, 7.25, 4.55, 3.7, 1.4, "Resettable", "depletion → cheap\nreset to $E_0$",
             fc="#fceeeb", ec=C_RESET, title_fs=13, sub_fs=11, title_color="#b3402f")
    _arrow(ax, (5.0, 5.44), (2.75, 5.28), color="#666")
    _arrow(ax, (5.0, 5.44), (7.25, 5.28), color="#666")
    ax.text(5.0, 3.58, "Clean causal comparison:  real-stake  vs  resettable",
            ha="center", va="center", fontsize=11.5, weight="bold", color="#333", zorder=3)

    # simulated-stake: secondary, derived from resettable
    _arrow(ax, (5.0, 3.35), (5.0, 2.13), dashed=True, color="#999")
    ax.text(5.6, 2.72, "adds two changes\nto resettable", ha="left", va="center",
            fontsize=10, style="italic", color="#777")
    _flowbox(ax, 5.0, 1.28, 7.4, 1.6, "Simulated-stake (auxiliary)",
             "resettable + two representational changes:\n"
             "+ mortality cue      + danger reward penalty 1.5",
             fc="#f0f0f0", ec="#8a8a8a", dashed=True, title_fs=11, sub_fs=10.5,
             title_color="#555", sub_color="#555")
    save(fig, "figure2_design")


# ---------------------------------------------------------------- Figure 3
def _jitter(n, width, seed):
    return np.random.default_rng(seed).uniform(-width, width, size=n)


def _cell_text_color(value, vmin, vmax, cmap):
    """Black or white cell text depending on the background luminance."""
    frac = (value - vmin) / (vmax - vmin) if vmax > vmin else 0.5
    r, g, b, _ = cmap(min(max(frac, 0.0), 1.0))
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    return "white" if lum < 0.55 else "#111"


def figure3_results():
    """Two-row layout: (a) full-width primary main result, then (b) lives-gradient
    dose-response and (c) payoff-sweep heatmap on the bottom row. Every number is
    read from the committed result files."""
    main = load("main_results.json")
    grad = load("lives_gradient_results.json")
    sweep = load("payoff_sweep_results.json")

    fig = plt.figure(figsize=(7.3, 5.95))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 1.15], hspace=0.42, wspace=0.32,
                          left=0.115, right=0.955, top=0.95, bottom=0.092)
    axA = fig.add_subplot(gs[0, :])
    axB = fig.add_subplot(gs[1, 0])
    axC = fig.add_subplot(gs[1, 1])

    # ---- Panel (a): main result, full width ----
    regimes = [("real", C_REAL, "real-stake", 0.55),
               ("resettable", C_RESET, "resettable", 0.55),
               ("simulated", C_SIM, "simulated\n(auxiliary)", 0.30)]
    for i, (reg, col, lab, al) in enumerate(regimes):
        vals = np.array([r["post_coop"] for r in main["runs"] if r["regime"] == reg])
        axA.scatter(i + _jitter(len(vals), 0.11, i), vals, s=34, color=col,
                    alpha=al, edgecolor="none", zorder=2)
        m, lo, hi = bootstrap_ci(vals)
        axA.errorbar(i, m, yerr=[[m - lo], [hi - m]], fmt="o", color=col, ms=11,
                     capsize=6, lw=2.4, zorder=3, markeredgecolor="white")
    axA.set_xticks(range(3)); axA.set_xticklabels([r[2] for r in regimes], fontsize=11)
    axA.set_ylabel("post-withdrawal\nmutual cooperation", fontsize=12)
    axA.set_xlim(-0.5, 2.5); axA.set_ylim(-0.05, 1.10)
    axA.tick_params(axis="y", labelsize=10.5)
    n = main["n_seeds"]
    _, p_paired, p_unpaired = paired_signflip_p(main)
    def _pf(p): return "< 0.0001" if p <= 1e-4 else f"= {p:.2g}"
    axA.set_title(f"(a) Main result  (n = {n} seeds)", fontsize=13)
    axA.annotate(f"real vs resettable\npaired sign-flip permutation p {_pf(p_paired)}",
                 xy=(0.95, 0.95), xycoords="data", ha="center", va="top",
                 fontsize=10.5, color="#222")
    axA.annotate(f"pooled unpaired permutation p {_pf(p_unpaired)}",
                 xy=(0.95, 0.70), xycoords="data", ha="center", va="top",
                 fontsize=9.3, color="#666")

    # ---- Panel (b): lives-gradient dose-response ----
    order = [(1, "L1(real)"), (2, "L2"), (4, "L4"), (8, "L8"), (10**9, "Linf(reset)")]
    xpos = list(range(len(order)))
    means = []
    for xi, (lv, name) in zip(xpos, order):
        vals = np.array([r["post_coop"] for r in grad["runs"] if r["level"] == name])
        axB.scatter(xi + _jitter(len(vals), 0.10, xi + 10), vals, s=26,
                    color="#4a4a4a", alpha=0.35, edgecolor="none", zorder=2)
        means.append(vals.mean())
    axB.plot(xpos, means, "-o", color=C_REAL, lw=2.4, ms=8, zorder=3)
    axB.set_xticks(xpos)
    axB.set_xticklabels(["1\n(real)", "2", "4", "8", "∞\n(reset)"], fontsize=11)
    axB.set_xlabel("maximum lives", fontsize=12)
    axB.set_ylabel("post-withdrawal\nmutual cooperation", fontsize=11.5)
    axB.set_ylim(-0.05, 1.05); axB.tick_params(axis="y", labelsize=10.5)
    rho = grad["spearman_lives_vs_coop"]
    rho_p = grad.get("spearman_p")
    ann = f"tie-aware Spearman $\\rho$ = {rho:.2f}"
    if rho_p is not None:
        ann += f"\nblocked perm p {'< 0.0001' if rho_p <= 1e-4 else f'= {rho_p:.2g}'}"
    axB.set_title("(b) Lives-gradient dose-response", fontsize=13)
    axB.annotate(ann, xy=(0.97, 0.96), xycoords="axes fraction", ha="right", va="top",
                 fontsize=10, color="#222")

    # ---- Panel (c): payoff-sweep heatmap (real - resettable) ----
    grid = sweep["grid"]
    Ts = sorted({c["T"] for c in grid})
    Ds = sorted({c["defect_net"] for c in grid})  # "-0.15","-0.45"
    M = np.full((len(Ds), len(Ts)), np.nan)
    for c in grid:
        M[Ds.index(c["defect_net"]), Ts.index(c["T"])] = c["diff"]
    vmax = max(0.7, float(np.nanmax(M)))
    cmap = plt.cm.YlGnBu
    im = axC.imshow(M, cmap=cmap, vmin=0, vmax=vmax, aspect="auto")
    axC.set_xticks(range(len(Ts))); axC.set_xticklabels([f"{t:g}" for t in Ts], fontsize=10.5)
    axC.set_yticks(range(len(Ds))); axC.set_yticklabels([f"{d}" for d in Ds], fontsize=10.5)
    axC.set_xlabel("temptation payoff $T$", fontsize=11.5)
    axC.set_ylabel("mutual-defection\nnet energy", fontsize=10.5)
    for i in range(len(Ds)):
        for j in range(len(Ts)):
            axC.text(j, i, f"{M[i, j]:+.2f}", ha="center", va="center", fontsize=12.5,
                     color=_cell_text_color(M[i, j], 0, vmax, cmap))
    n_pos = int(np.sum(M > 0))
    axC.set_title(f"(c) Payoff sweep: real − resettable\n"
                  f"real > resettable in {n_pos}/{M.size} cells", fontsize=12)
    cbar = fig.colorbar(im, ax=axC, fraction=0.05, pad=0.05)
    cbar.set_label("cooperation difference\n(real − resettable)", fontsize=9.5)
    cbar.ax.tick_params(labelsize=9)

    save(fig, "figure3_results")


def figure4_probe():
    """Common-state frozen-policy probe. Built only from common_state_probe.json.
    Two-row layout: (a) full-width paired end-of-withdrawal comparison, then
    (b) per-seed differences and (c) training-vs-withdrawal checkpoints."""
    probe = load("common_state_probe.json")
    cs = probe["raw"]["common_state"]
    summ = probe["summary"]
    seeds = probe["meta"]["eval_seeds"]

    def vals(ck, reg):
        return np.array([cs[ck][reg][str(s)]["pcc"] for s in seeds])

    fig = plt.figure(figsize=(7.3, 5.95))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 1.05], hspace=0.40, wspace=0.30,
                          left=0.115, right=0.955, top=0.95, bottom=0.105)
    axA = fig.add_subplot(gs[0, :])
    axB = fig.add_subplot(gs[1, 0])
    axC = fig.add_subplot(gs[1, 1])

    # ---- Panel (a): end-of-withdrawal, paired by seed (full width) ----
    r_eow, re_eow = vals("end_of_withdrawal", "real"), vals("end_of_withdrawal", "resettable")
    xr, xs = 0.0, 1.0
    for a, b in zip(r_eow, re_eow):
        axA.plot([xr, xs], [a, b], color="#aaa", lw=0.9, alpha=0.40, zorder=1)
    axA.scatter([xr] * len(r_eow), r_eow, s=38, color=C_REAL, zorder=3,
                edgecolor="white", linewidth=0.4)
    axA.scatter([xs] * len(re_eow), re_eow, s=38, color=C_RESET, zorder=3,
                edgecolor="white", linewidth=0.4)
    mr, mre = r_eow.mean(), re_eow.mean()
    axA.plot([xr - 0.22, xr + 0.22], [mr, mr], color=C_REAL, lw=3.4, zorder=4,
             solid_capstyle="round")
    axA.plot([xs - 0.22, xs + 0.22], [mre, mre], color=C_RESET, lw=3.4, zorder=4,
             solid_capstyle="round")
    axA.text(xr - 0.30, mr, f"mean = {mr:.3f}", ha="right", va="center",
             fontsize=11, weight="bold", color=C_REAL)
    axA.text(xs + 0.30, mre, f"mean = {mre:.3f}", ha="left", va="center",
             fontsize=11, weight="bold", color="#b3402f")
    axA.set_xticks([xr, xs]); axA.set_xticklabels(["real-stake", "resettable"], fontsize=11.5)
    axA.set_xlim(-1.0, 2.0); axA.set_ylim(-0.05, 1.02)
    axA.set_ylabel("common-state $P(CC\\mid s)$", fontsize=12)
    axA.tick_params(axis="y", labelsize=10.5)
    axA.set_title("(a) End-of-withdrawal, paired by seed", fontsize=13)

    # ---- Panel (b): per-seed real - resettable difference + 95% CI ----
    d = np.array(summ["end_of_withdrawal"]["real_minus_resettable"]["per_seed_diff"])
    md = summ["end_of_withdrawal"]["real_minus_resettable"]["mean_diff"]
    lo, hi = summ["end_of_withdrawal"]["real_minus_resettable"]["boot95"]
    axB.axhline(0, color="#888", lw=1, ls="--")
    axB.scatter(_jitter(len(d), 0.13, 7), d, s=28, color="#555", alpha=0.6, zorder=2)
    axB.errorbar(0, md, yerr=[[md - lo], [hi - md]], fmt="o", color=C_REAL, ms=11,
                 capsize=7, lw=2.4, zorder=3, markeredgecolor="white")
    axB.set_xticks([0]); axB.set_xticklabels(["real − resettable"], fontsize=11)
    axB.set_xlim(-0.6, 0.6); axB.set_ylim(-0.2, 1.22)
    axB.set_ylabel("difference in $P(CC\\mid s)$", fontsize=11.5)
    axB.tick_params(axis="y", labelsize=10.5)
    pp = summ["end_of_withdrawal"]["real_minus_resettable"]["paired_signflip_p"]
    ptxt = "< 0.0001" if pp <= 1e-4 else f"= {pp:.2g}"
    axB.set_title("(b) Per-seed difference", fontsize=13)
    axB.annotate(f"mean {md:+.3f}\n95% CI [{lo:.2f}, {hi:.2f}]\npaired p {ptxt}",
                 xy=(0.97, 0.99), xycoords="axes fraction", ha="right", va="top",
                 fontsize=10.5, color="#222")

    # ---- Panel (c): end-of-training vs end-of-withdrawal ----
    for reg, col, faded, lab in [("real", C_REAL, False, "real"),
                                 ("resettable", C_RESET, False, "resettable"),
                                 ("simulated", C_SIM, True, "simulated (exploratory)")]:
        eot, eow = vals("end_of_training", reg), vals("end_of_withdrawal", reg)
        alpha = 0.12 if faded else 0.28
        for a, b in zip(eot, eow):
            axC.plot([0, 1], [a, b], color=col, lw=0.7, alpha=alpha, zorder=1)
        axC.plot([0, 1], [eot.mean(), eow.mean()], "-o", color=col,
                 lw=1.6 if faded else 2.8, ms=6 if faded else 7,
                 alpha=0.6 if faded else 1.0, zorder=3, label=lab)
    axC.set_xticks([0, 1]); axC.set_xticklabels(["end of\ntraining", "end of\nwithdrawal"], fontsize=11)
    axC.set_xlim(-0.3, 1.3); axC.set_ylim(-0.05, 1.0)
    axC.set_ylabel("common-state $P(CC\\mid s)$", fontsize=11.5)
    axC.tick_params(axis="y", labelsize=10.5)
    axC.set_title("(c) Training vs withdrawal", fontsize=13)
    axC.legend(fontsize=10, loc="upper right", frameon=False)

    fig.text(0.5, 0.012, f"Global common-state bank: n = {probe['bank']['bank_size']:,} observations",
             ha="center", fontsize=9.5, color="#555")
    save(fig, "figure4_common_state_probe")


if __name__ == "__main__":
    figure1_framework()
    figure2_design()
    figure3_results()
    figure4_probe()
    print("done.")
