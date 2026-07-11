import json

import pandas as pd
import pytest

from src.protocol import freeze_preC_files, verify_preC_files
from src.utils import make_writable


def test_prec_artifact_freezes_before_c_and_detects_mutation(tmp_path):
    record = {"seed": 1, "condition": "standard", "uses_c_data": False, "SR_preC": 0.2}
    frozen = freeze_preC_files(tmp_path, record)
    assert verify_preC_files(tmp_path)["sha256"] == frozen["sha256"]
    with pytest.raises(FileExistsError):
        freeze_preC_files(tmp_path, record)
    parquet = tmp_path / "preC_features.parquet"
    make_writable(parquet)
    frame = pd.read_parquet(parquet)
    frame.loc[0, "SR_preC"] = 999.0
    frame.to_parquet(parquet, index=False)
    with pytest.raises(RuntimeError):
        verify_preC_files(tmp_path)
