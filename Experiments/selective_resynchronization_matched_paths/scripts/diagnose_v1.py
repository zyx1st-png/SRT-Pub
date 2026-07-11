from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
sys.path.insert(0, str(ROOT))

from src.diagnostic import run_diagnostic  # noqa: E402


def main() -> None:
    result = run_diagnostic(REPO, ROOT / "outputs" / "diagnostic")
    print(json.dumps({"n": result["n"], "v1_decision_changed": False}, indent=2))


if __name__ == "__main__":
    main()
