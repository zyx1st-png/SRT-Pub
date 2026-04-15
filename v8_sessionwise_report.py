import csv
from pathlib import Path
import tempfile

import fit_real_pipeline_v8 as v8

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "unified_srt_mtor_real_multi_condid.csv"
OUT_MD = ROOT / "results_v8_sessionwise.md"


def get_sessions(path):
    sids = []
    seen = set()
    with open(path, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            sid = row["session_id"]
            if sid not in seen:
                seen.add(sid)
                sids.append(sid)
    return sids


def write_subset(path, sid):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=f"_{sid}.csv")
    tmp_path = Path(tmp.name)
    tmp.close()

    with open(path, "r", encoding="utf-8") as f_in, open(tmp_path, "w", newline="", encoding="utf-8") as f_out:
        r = csv.DictReader(f_in)
        w = csv.DictWriter(f_out, fieldnames=r.fieldnames)
        w.writeheader()
        for row in r:
            if row["session_id"] == sid:
                # force within-session temporal split to keep all three partitions present
                t = float(row["t_sec"])
                if t < 420:
                    row["split"] = "train"
                elif t < 510:
                    row["split"] = "valid"
                else:
                    row["split"] = "test"
                w.writerow(row)
    return tmp_path


def run_v8(path):
    rows = v8.load_rows(path)
    v8.prepare_psif(rows)
    nll0_train, best1, best2 = v8.fit_v8(rows)
    rep = v8.eval_models(rows, nll0_train, best1, best2)
    return rep


def main():
    sessions = get_sessions(DATA)
    lines = [
        "# v8 Session-wise Report",
        "",
        f"Data: `{DATA}`",
        "",
        "| session_id | omega_m1 | omega_m2 | c_fric_m2 | train_LR_M1 | train_LR_M2 | valid_dNLL_M1 | test_dNLL_M1 |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for sid in sessions:
        sub = write_subset(DATA, sid)
        rep = run_v8(sub)
        lines.append(
            f"| {sid} | {rep['omega_m1']:.4f} | {rep['omega_m2']:.4f} | {rep['c_fric_m2']:.3f} | {rep['train_LR_M1']:.3f} | {rep['train_LR_M2']:.3f} | {rep['eval']['valid']['dNLL_M1']:.3f} | {rep['eval']['test']['dNLL_M1']:.3f} |"
        )

    lines += [
        "",
        "## Notes",
        "- Splits are reassigned within each session by time windows to ensure train/valid/test all exist.",
        "- If most sessions show positive valid/test dNLL for M1, omega effect is session-stable.",
        "- Current Psi_f proxy remains weak when c_fric_m2 stays near 0.",
    ]

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
