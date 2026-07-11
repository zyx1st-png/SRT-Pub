from pathlib import Path
from _runner import run

if __name__ == "__main__":
    print(run(Path(__file__).resolve().parents[1] / "configs" / "confirmatory_locked.yaml"))

