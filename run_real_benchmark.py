from pathlib import Path
import importlib

ROOT = Path(__file__).resolve().parent
REAL = ROOT / "data" / "unified_srt_mtor_real.csv"


def run(module_name):
    m = importlib.import_module(module_name)
    if hasattr(m, "DATA_PATH"):
        m.DATA_PATH = REAL
    print(f"\n===== {module_name} on {REAL.name} =====")
    m.main()


def main():
    for mod in [
        "fit_real_pipeline_v4",
        "fit_real_pipeline_v5",
        "fit_real_pipeline_v7_1",
    ]:
        run(mod)


if __name__ == "__main__":
    main()
