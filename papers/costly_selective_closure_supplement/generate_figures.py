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
def figure2_design():
    fig, ax = plt.subplots(figsize=(9.2, 5.4))
    ax.set_xlim(0, 14); ax.set_ylim(0, 8.4); ax.axis("off")

    _box(ax, 0.3, 3.1, 3.4, 2.2,
         "Shared setup\nsame observations,\nbase reward, energy dynamics,\nnetwork, training, seeds",
         fc="#e8eef4", fs=9)

    # clean contrast
    _box(ax, 5.0, 5.2, 3.8, 1.7,
         "Real-stake\ndepletion terminates\nthe token run", fc="#e8eef4", fs=10, ec=C_REAL)
    _box(ax, 5.0, 1.5, 3.8, 1.7,
         "Resettable\ndepletion triggers a\ncheap reset to $E_0$", fc="#fbecea", fs=10, ec=C_RESET)
    _arrow(ax, (3.7, 4.5), (5.0, 6.05), color=C_REAL)
    _arrow(ax, (3.7, 3.9), (5.0, 2.35), color=C_RESET)

    # bracket around clean contrast
    ax.add_patch(FancyBboxPatch((4.75, 1.2), 4.35, 6.0,
                                boxstyle="round,pad=0.02,rounding_size=0.1",
                                linewidth=1.1, edgecolor="#555", facecolor="none",
                                linestyle=(0, (4, 3))))
    ax.text(6.92, 7.55, "Clean causal comparison:\nreal-stake vs resettable",
            ha="center", va="bottom", fontsize=9.5, weight="bold", color="#333")

    # auxiliary condition
    ax.add_patch(FancyBboxPatch((9.55, 3.15), 4.35, 2.7,
                                boxstyle="round,pad=0.02,rounding_size=0.12",
                                linewidth=1.3, edgecolor="#666", facecolor="#f3f3f3",
                                linestyle="--"))
    ax.text(9.78, 5.5, "Simulated-stake (auxiliary)", ha="left", va="top",
            fontsize=9.3, weight="bold")
    ax.text(9.82, 4.85,
            "•  cheap reset (as resettable)\n•  + mortality observation cue\n"
            "•  + danger reward penalty = 1.5",
            ha="left", va="top", fontsize=8.6)
    _arrow(ax, (8.8, 2.75), (9.55, 3.7), dashed=True, color="#999")
    ax.text(8.95, 3.5, "adds two\nchanges", ha="center", va="bottom", fontsize=7.6,
            style="italic", color="#888")
    ax.text(11.72, 2.75,
            "Auxiliary condition — not part of the\nsingle-variable matched contrast",
            ha="center", va="top", fontsize=8.6, style="italic", color="#444")

    ax.text(7.0, 0.35,
            "Only real-stake vs resettable is the single-variable matched comparison "
            "(the manipulated variable is terminate-versus-reset).",
            ha="center", fontsize=8.7, color="#333")
    save(fig, "figure2_design")


# ---------------------------------------------------------------- Figure 3
def _jitter(n, width, seed):
    return np.random.default_rng(seed).uniform(-width, width, size=n)


def figure3_results():
    main = load("main_results.json")
    grad = load("lives_gradient_results.json")
    sweep = load("payoff_sweep_results.json")

    fig, axes = plt.subplots(1, 3, figsize=(13.2, 4.4))
    axA, axB, axC = axes

    # --- Panel A: main result ---
    regimes = [("real", C_REAL, "real-stake"),
               ("resettable", C_RESET, "resettable"),
               ("simulated", C_SIM, "simulated\n(auxiliary)")]
    for i, (reg, col, lab) in enumerate(regimes):
        vals = np.array([r["post_coop"] for r in main["runs"] if r["regime"] == reg])
        axA.scatter(i + _jitter(len(vals), 0.10, i), vals, s=16, color=col,
                    alpha=0.45, edgecolor="none", zorder=2)
        m, lo, hi = bootstrap_ci(vals)
        axA.errorbar(i, m, yerr=[[m - lo], [hi - m]], fmt="o", color=col,
                     ms=8, capsize=5, lw=1.8, zorder=3, markeredgecolor="white")
    axA.set_xticks(range(3)); axA.set_xticklabels([r[2] for r in regimes], fontsize=9)
    axA.set_ylabel("post-withdrawal mutual cooperation")
    axA.set_ylim(-0.05, 1.05)
    n = main["n_seeds"]
    _, p_paired, p_unpaired = paired_signflip_p(main)
    def _pf(p): return "< 0.0001" if p <= 1e-4 else f"= {p:.2g}"
    axA.set_title(f"(a) Main result  (n = {n} seeds)", fontsize=10.5)
    axA.annotate(f"real vs resettable\npaired p {_pf(p_paired)}\n(unpaired p {_pf(p_unpaired)})",
                 xy=(0.5, 0.64), xycoords="data", ha="center", fontsize=8.3, color="#333")
    axA.plot([0, 1], [1.0, 1.0], color="#333", lw=1)
    axA.text(0.5, 1.01, "*", ha="center", fontsize=13)

    # --- Panel B: lives gradient ---
    order = [(1, "L1(real)"), (2, "L2"), (4, "L4"), (8, "L8"), (10**9, "Linf(reset)")]
    xpos = list(range(len(order)))
    means = []
    for xi, (lv, name) in zip(xpos, order):
        vals = np.array([r["post_coop"] for r in grad["runs"] if r["level"] == name])
        axB.scatter(xi + _jitter(len(vals), 0.09, xi + 10), vals, s=15,
                    color="#4a4a4a", alpha=0.35, edgecolor="none", zorder=2)
        means.append(vals.mean())
    axB.plot(xpos, means, "-o", color=C_REAL, lw=1.8, ms=6, zorder=3)
    axB.set_xticks(xpos); axB.set_xticklabels(["1", "2", "4", "8", "∞"], fontsize=10)
    axB.set_xlabel("maximum lives")
    axB.set_ylabel("post-withdrawal mutual cooperation")
    axB.set_ylim(-0.05, 1.05)
    rho = grad["spearman_lives_vs_coop"]
    rho_p = grad.get("spearman_p")
    ann = f"tie-aware Spearman $\\rho$ = {rho:.2f}"
    if rho_p is not None:
        ann += f"\n(perm p {'< 0.0001' if rho_p <= 1e-4 else f'= {rho_p:.2g}'})"
    axB.set_title("(b) Lives-gradient dose-response", fontsize=10.5)
    axB.annotate(ann, xy=(0.5, 0.88), xycoords="axes fraction", ha="center",
                 fontsize=8.6, color="#333")

    # --- Panel C: payoff sweep heatmap (real - resettable) ---
    grid = sweep["grid"]
    Ts = sorted({c["T"] for c in grid})
    Ds = sorted({c["defect_net"] for c in grid})  # "-0.15","-0.45"
    M = np.full((len(Ds), len(Ts)), np.nan)
    for c in grid:
        M[Ds.index(c["defect_net"]), Ts.index(c["T"])] = c["diff"]
    im = axC.imshow(M, cmap="YlGnBu", vmin=0, vmax=max(0.7, np.nanmax(M)), aspect="auto")
    axC.set_xticks(range(len(Ts))); axC.set_xticklabels([f"{t:g}" for t in Ts])
    axC.set_yticks(range(len(Ds))); axC.set_yticklabels(Ds)
    axC.set_xlabel("temptation payoff $T$")
    axC.set_ylabel("mutual-defection net energy")
    for i in range(len(Ds)):
        for j in range(len(Ts)):
            axC.text(j, i, f"{M[i, j]:+.2f}", ha="center", va="center",
                     fontsize=9.5, color="#111")
    n_pos = int(np.sum(M > 0))
    axC.set_title(f"(c) Payoff sweep: real − resettable\n"
                  f"real > resettable in {n_pos}/{M.size} cells", fontsize=10.5)
    cbar = fig.colorbar(im, ax=axC, fraction=0.046, pad=0.04)
    cbar.set_label("cooperation difference", fontsize=8.5)

    for a in axes:
        a.spines[["top", "right"]].set_visible(True)
    axA.margins(x=0.15)
    fig.text(0.5, -0.03,
             "Panel (a): points are per-seed values; markers show the mean with a 95% "
             "bootstrap CI; the main test is a two-sided paired sign-flip permutation test "
             "on the per-seed real − resettable differences. "
             "Panel (b): points per seed, line through means. "
             "Panel (c): cell = mean(real) − mean(resettable) effect size; real exceeds "
             "resettable in every cell.",
             ha="center", fontsize=8, color="#444")
    fig.tight_layout()
    save(fig, "figure3_results")


if __name__ == "__main__":
    figure1_framework()
    figure2_design()
    figure3_results()
    print("done.")
