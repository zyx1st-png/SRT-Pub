import unittest
from _helpers import CONFIG
from src.agents import SYSTEMS
from src.metrics import run_episode

class TestComputeBudget(unittest.TestCase):
    def test_equal_reserved_expansions(self):
        values = {run_episode(CONFIG, s, "Hidden-Irreversible", 5, 0)[0]["node_expansions"] for s in SYSTEMS}
        self.assertEqual(values, {CONFIG["interaction"]["max_episode_steps"] * CONFIG["compute"]["node_expansions_per_decision"]})

