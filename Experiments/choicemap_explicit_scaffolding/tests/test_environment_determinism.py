import unittest
import math
from _helpers import CONFIG
from src.metrics import run_episode

class TestEnvironmentDeterminism(unittest.TestCase):
    def test_identical_seed_identical_outcome(self):
        a = run_episode(CONFIG, "ChoiceMap", "Hidden-Irreversible", 17, 4)[0]
        b = run_episode(CONFIG, "ChoiceMap", "Hidden-Irreversible", 17, 4)[0]
        for key in a:
            if key == "wall_clock_seconds":
                continue
            if isinstance(a[key], float) and math.isnan(a[key]):
                self.assertTrue(math.isnan(b[key]))
            else:
                self.assertEqual(a[key], b[key])
