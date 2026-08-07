from __future__ import annotations

import json
from pathlib import Path

import pytest

from src.protocol import ProtocolRunner, freeze_preC_files, reject_c_fields, verify_preC_files
from src.utils import make_writable


def test_c_field_rejection():
    with pytest.raises(ValueError, match="C-stage"):
        reject_c_fields({"master_seed": 1, "Q_C": 0.1})
    with pytest.raises(ValueError, match="C-stage"):
        reject_c_fields({"master_seed": 1, "C_final_success": 0.8})


def test_hash_mutation_detected(tmp_path: Path):
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    freeze_preC_files(run_dir, {"master_seed": 1, "uses_c_data": False, "dV_CF_pre": 0.2})
    verify_preC_files(run_dir)
    parquet = run_dir / "preC_features.parquet"
    make_writable(parquet)
    with parquet.open("ab") as handle:
        handle.write(b"mutation")
    with pytest.raises(RuntimeError, match="hash mismatch"):
        verify_preC_files(run_dir)


def test_phase_order_violation(experiment_root: Path, tmp_path: Path):
    runner = ProtocolRunner(experiment_root, experiment_root / "configs/smoke.yaml", output_override=tmp_path)
    with pytest.raises(RuntimeError, match="A/B must complete"):
        runner.run_c_cell(9901, "X-low")
