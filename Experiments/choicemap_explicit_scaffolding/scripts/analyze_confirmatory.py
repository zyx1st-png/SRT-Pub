from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.analysis import analyze, make_figures, make_raw_figures
from src.utils import load_config

if __name__ == "__main__":
    cfg = load_config(ROOT / "configs" / "confirmatory_locked.yaml")
    out = ROOT / "outputs" / "confirmatory"
    print(analyze(out / "raw" / "episode_logs.csv", out / "processed", cfg))
    make_figures(out / "processed" / "seed_level_metrics.csv", out / "figures")
    make_raw_figures(out / "raw" / "episode_logs.csv", out / "raw" / "commitment_logs.csv", out / "figures")
