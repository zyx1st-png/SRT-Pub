import argparse
import run_pilot

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", required=True, help="comma-separated preregistered seed subset")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    seeds = [int(x) for x in args.seeds.split(",")]
    if any(s not in range(12) for s in seeds):
        raise SystemExit("Only preregistered seeds 0..11 are allowed")
    run_pilot.SEEDS = seeds
    run_pilot.main(args.out)
