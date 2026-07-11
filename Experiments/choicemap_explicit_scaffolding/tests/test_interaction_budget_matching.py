import unittest
from _helpers import CONFIG
from src.agents import SYSTEMS
from src.metrics import run_episode

class TestInteractionBudget(unittest.TestCase):
    def test_equal_actual_interactions(self):
        values = {run_episode(CONFIG, s, "Hidden-Irreversible-Shift", 8, 1)[0]["environment_interactions"] for s in SYSTEMS}
        self.assertEqual(values, {CONFIG["interaction"]["max_episode_steps"]})

