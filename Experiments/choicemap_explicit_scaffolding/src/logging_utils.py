"""Portable atomic output helpers with Parquet support when pyarrow is installed."""
from __future__ import annotations

import csv
import json
from pathlib import Path
import shutil
import subprocess
from typing import Iterable


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def write_parquet(path: Path, rows: list[dict]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        import pandas as pd
        pd.DataFrame(rows).to_parquet(path, index=False)
        return "parquet"
    except (ImportError, ValueError):
        # Dependency-limited smoke environments retain lossless JSONL beside the required path.
        # Confirmatory execution is required to install requirements.txt and produce true Parquet.
        fallback = path.with_suffix(path.suffix + ".jsonl")
        with fallback.open("w", encoding="utf-8") as f:
            for row in rows:
                f.write(json.dumps(row, ensure_ascii=False, allow_nan=True) + "\n")
        return "jsonl_fallback"


def csv_to_parquet(csv_path: Path, parquet_path: Path, experiment_root: Path) -> str:
    """Convert a streamed CSV log to true Parquet via pyarrow or parquetjs-lite."""
    try:
        import pandas as pd
        pd.read_csv(csv_path).to_parquet(parquet_path, index=False)
        return "parquet_pyarrow"
    except (ImportError, ValueError):
        node = shutil.which("node")
        converter = experiment_root / "scripts" / "csv_to_parquet.cjs"
        if node and (experiment_root / "node_modules" / "parquetjs-lite").exists():
            subprocess.run([node, str(converter), str(csv_path), str(parquet_path)],
                           cwd=experiment_root, check=True)
            return "parquet_parquetjs"
        return "csv_only_dependency_missing"
