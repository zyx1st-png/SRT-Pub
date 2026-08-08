from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis import analyze
from src.utils import load_yaml, verify_formal_manifest


def main() -> None:
    verify_formal_manifest(ROOT)
    config = load_yaml(ROOT / "configs/formal_locked.yaml")
    result = analyze(ROOT, config, ROOT / config["output_root"])
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
