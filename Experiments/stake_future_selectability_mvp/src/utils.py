from __future__ import annotations

import hashlib
import json
import os
import platform
import random
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import torch
import yaml


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any, *, overwrite: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        raise FileExistsError(path)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def append_jsonl(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(value, sort_keys=True) + "\n")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_paths(paths: Iterable[Path], root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted((p.resolve() for p in paths), key=lambda p: str(p)):
        rel = path.relative_to(root.resolve()).as_posix()
        digest.update(rel.encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def make_read_only(path: Path) -> None:
    path.chmod(path.stat().st_mode & ~0o222)


def make_writable(path: Path) -> None:
    path.chmod(path.stat().st_mode | 0o200)


def set_global_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.set_num_threads(max(1, min(4, os.cpu_count() or 1)))
    try:
        torch.use_deterministic_algorithms(True)
    except Exception:
        pass


def git_sha(repo_root: Path) -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_root, text=True).strip()


def environment_info() -> dict[str, Any]:
    import gymnasium
    import pandas
    import pyarrow
    import pytest
    import scipy
    import sklearn
    import statsmodels

    return {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "logical_cpu_count": os.cpu_count(),
        "torch": torch.__version__,
        "numpy": np.__version__,
        "pandas": pandas.__version__,
        "scipy": scipy.__version__,
        "sklearn": sklearn.__version__,
        "statsmodels": statsmodels.__version__,
        "gymnasium": gymnasium.__version__,
        "pyarrow": pyarrow.__version__,
        "pyyaml": yaml.__version__,
        "pytest": pytest.__version__,
        "device_requested": "cpu",
        "mps_available_but_unused": bool(torch.backends.mps.is_available()),
        "deterministic_algorithms_requested": True,
    }


def condition_parts(cell: str) -> tuple[str, str]:
    condition, severity = cell.split("-", maxsplit=1)
    if condition not in {"X", "T", "S"} or severity not in {"low", "high"}:
        raise ValueError(f"invalid condition cell: {cell}")
    return condition, severity


def verify_formal_manifest(experiment_root: Path) -> dict[str, Any]:
    """Reject execution if any frozen scientific/code artifact has changed."""
    root = experiment_root.resolve()
    repo = root.parents[1]
    manifest_path = root / "manifests/formal_manifest.json"
    if not manifest_path.exists():
        raise RuntimeError("formal manifest missing; run lock_formal.py before formal execution")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for relative, expected in manifest["artifact_hashes"].items():
        path = repo / relative
        if not path.exists() or sha256_file(path) != expected:
            raise RuntimeError(f"formal locked artifact hash mismatch: {relative}")
    code_paths = [
        *sorted((root / "src").glob("*.py")),
        *sorted((root / "scripts").glob("*.py")),
        *sorted((root / "tests").glob("*.py")),
    ]
    if sha256_paths(code_paths, repo) != manifest["code_tree_sha256"]:
        raise RuntimeError("formal code-tree hash mismatch")
    config = load_yaml(root / "configs/formal_locked.yaml")
    if config["master_seeds"] != manifest["formal_master_seeds"]:
        raise RuntimeError("formal master-seed list differs from manifest")
    if config["conditions"] != manifest["formal_cells"]:
        raise RuntimeError("formal condition cells differ from manifest")
    return manifest
