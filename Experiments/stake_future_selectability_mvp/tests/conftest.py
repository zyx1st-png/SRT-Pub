from __future__ import annotations

import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


@pytest.fixture
def smoke_config():
    return yaml.safe_load((ROOT / "configs/smoke.yaml").read_text(encoding="utf-8"))


@pytest.fixture
def experiment_root() -> Path:
    return ROOT
