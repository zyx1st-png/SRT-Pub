import os
from pathlib import Path
from fit_real_pipeline_v7_1 import load_rows, prepare, estimate_baseline, build_l2_and_psif, fit, posterior_omega, nll_split

ROOT = Path(__file__).resolve().parent
DATA_PATH = Path(os.environ.get("SRT_DATA", str(ROOT / "data" / "unified_srt_mtor_v2.csv")))


def main():
    rows = load_rows(DATA_PATH)
    prepare(rows)
    l0, gl0 = estimate_baseline(rows)
    build_l2_and_psif(rows)
    fitp = fit(rows, l0, gl0)
    om, ppos = posterior_omega(rows, l0, gl0, fitp)

    v_hat, n_v = nll_split(rows, "valid", l0, gl0, fitp["omega"], fitp["alpha"], fitp["theta"], fitp["c_fric"])
    t_hat, n_t = nll_split(rows, "test", l0, gl0, fitp["omega"], fitp["alpha"], fitp["theta"], fitp["c_fric"])
    v0, _ = nll_split(rows, "valid", l0, gl0, 0.0, 0.0, 0.6, 0.0)
    t0, _ = nll_split(rows, "test", l0, gl0, 0.0, 0.0, 0.6, 0.0)

    print("=== fit_real_pipeline_v7.1b summary ===")
    print(f"data={DATA_PATH}")
    print(f"omega_hat={fitp['omega']:.3f}, omega_mean≈{om:.3f}, P(omega>0)≈{ppos:.6f}")
    print(f"alpha_hat={fitp['alpha']:.3f}, theta_hat={fitp['theta']:.3f}")
    print(f"c_fric_hat={fitp['c_fric']:.3f}")
    print(f"train_LR={fitp['train_lr']:.3f}")
    print(f"valid_delta_nll={v0 - v_hat:.3f} (n={n_v})")
    print(f"test_delta_nll={t0 - t_hat:.3f} (n={n_t})")


if __name__ == "__main__":
    main()
