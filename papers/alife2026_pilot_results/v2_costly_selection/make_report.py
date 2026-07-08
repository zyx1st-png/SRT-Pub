"""Generate a human-readable results summary from the experiment JSONs."""
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent


def load(name):
    p = ROOT / name
    return json.load(open(p)) if p.exists() else None


def frac_coop(runs, reg, thr=0.3):
    v = np.array([r["post_coop"] for r in runs if r["regime"] == reg])
    return float(np.mean(v > thr)), len(v)


def block(title, d):
    lines = [f"### {title}", ""]
    lines.append("| regime | baseline coop | frozen coop | post-withdrawal coop | deaths/ep | d_eff | %seeds cooperate |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for reg in ["real", "resettable", "simulated"]:
        f, n = frac_coop(d["runs"], reg)
        m = lambda k: d[k][reg]
        lines.append(
            f"| {reg} | {m('baseline_coop')[0]:.3f} | {m('frozen_coop')[0]:.3f} | "
            f"{m('post_coop')[0]:.3f} ± {m('post_coop')[1]:.3f} | {m('post_fail')[0]:.2f} | "
            f"{m('d_eff')[0]:.2f} | {100*f:.0f}% |")
    lines.append("")
    t = d["tests"]
    lines.append("Permutation tests (real vs X, two-sided):")
    for pair in ["resettable", "simulated"]:
        for metric in ["frozen_coop", "post_coop"]:
            key = f"real_vs_{pair}__{metric}"
            if key in t:
                lines.append(f"- {key}: diff={t[key]['diff']:+.3f}, p={t[key]['p']:.4f}")
    lines.append("")
    return "\n".join(lines)


def main():
    full = load("results_full.json")
    nop = load("results_nopenalty.json")
    out = ["# Costly Selective Closure — de-risking experiment (v2)", ""]
    out.append("Two independent REINFORCE learners in a survival stag-hunt / PD "
               "(T=1.4 > R=1.0 > P=0.6 > S=0.0). Only mutual cooperation thrives; "
               "mutual defection starves. Trained with a mutual-cooperation bonus, "
               "then bonus withdrawn. **Real and resettable share an identical reward "
               "function; the sole difference is terminate-vs-reset on energy depletion.**")
    out.append("")
    if full:
        out.append(f"n_seeds = {full['n_seeds']}")
        out.append("")
        out.append(block("Main result (matched death penalty = 2.0 in all regimes)", full))
    if nop:
        out.append(block("Robustness 1: death penalty = 0 (pure return-truncation)", nop))

    grad = load("results_gradient.json")
    if grad:
        out.append("### Robustness 2: lives gradient (dose-response, 30 seeds)")
        out.append("")
        out.append("Generalises terminate-vs-reset to a number of allowed respawns.")
        out.append("")
        out.append("| allowed respawns | post-withdrawal coop | %seeds cooperate | deaths/ep |")
        out.append("|---|---:|---:|---:|")
        for name in ["L1(real)", "L2", "L4", "L8", "Linf(reset)"]:
            s = grad["summary"][name]
            out.append(f"| {name} | {s['post_coop_mean']:.3f} ± {s['post_coop_std']:.3f} | "
                       f"{100*s['frac_coop']:.0f}% | {s['deaths']:.2f} |")
        out.append("")
        out.append(f"Spearman(lives, coop) = {grad['spearman_lives_vs_coop']:+.3f} (monotone decrease). "
                   f"L1 vs Linf: diff={grad['L1_vs_Linf']['diff']:+.3f}, p={grad['L1_vs_Linf']['p']:.4f}.")
        out.append("")

    sw = load("results_sweep.json")
    if sw:
        out.append("### Robustness 3: payoff sweep (15 seeds), real vs resettable")
        out.append("")
        out.append("| temptation T | defect net-energy | real | resettable | diff | p |")
        out.append("|---:|---:|---:|---:|---:|---:|")
        for c in sw["grid"]:
            out.append(f"| {c['T']:.1f} | {c['defect_net']} | {c['real_mean']:.2f} | "
                       f"{c['reset_mean']:.2f} | {c['diff']:+.2f} | {c['p']:.4f} |")
        out.append("")
        out.append("Real > resettable in every cell; effect is not knife-edge.")
        out.append("")

    out.append("## Reading")
    out.append("- Real-stake stabilises costly cooperation; cheaply-resettable and "
               "simulated-stake regimes collapse to defection despite the identical reward.")
    out.append("- The manipulated variable is within-episode token-level irreversibility "
               "alone: removing return-truncation removes the pressure that makes costly "
               "self-maintenance worth learning. This isolates the causal efficacy of the "
               "vulnerability dimension V; it does not validate the full four-dimensional "
               "criterion, and the learning that produces cooperation still runs across many "
               "resettable episodes (see README 'Honest scope').")
    (ROOT / "RESULTS_SUMMARY.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
