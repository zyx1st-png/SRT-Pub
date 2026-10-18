import tempfile
from pathlib import Path
import unittest

from nc0a_macos_feasibility_probe import (
    R11_LONG_PROBE_ROOT, _checkpoint_schedule, parallel_chain_probe,
)


class MacOSFeasibilityProbeScheduleTests(unittest.TestCase):
    def test_locked_long_probe_contains_the_32e_terminal_checkpoint(self):
        self.assertEqual(_checkpoint_schedule(32), (1, 2, 4, 8, 32))
        self.assertEqual(R11_LONG_PROBE_ROOT, 20261018)

    def test_previous_probe_checkpoints_remain_capped_at_8e(self):
        self.assertEqual(_checkpoint_schedule(8), (1, 2, 4, 8))

    def test_32e_cannot_be_run_with_an_unreviewed_seed_or_worker_shape(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "fixed four-worker"):
                parallel_chain_probe("factor-mst", 2, Path(tmp), 32,
                                     seed_root=R11_LONG_PROBE_ROOT,
                                     max_wall_seconds=1200)


if __name__ == "__main__":
    unittest.main()
