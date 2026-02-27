from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data" / "unified_srt_mtor_real.csv"


def init_csv(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "dataset_id","subject_id","session_id","circuit_id","t_sec","dt_sec",
        "spike_count","x_mtor_proxy","u_observer","condition","split"
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()


def main():
    init_csv(OUT)
    print(f"initialized: {OUT}")
    print("next:")
    print("1) Allen: pull one ecephys session and append binned spike rows")
    print("2) GEO: parse GSE286175/GSE247367 and append omics prior rows")
    print("3) run fit_real_pipeline_v4.py with this real csv")


if __name__ == "__main__":
    main()
