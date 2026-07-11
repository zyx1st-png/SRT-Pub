import unittest
from src.environment import HiddenRegimeWorld
from src.environment_generator import generate_world

class TestOracleIsolation(unittest.TestCase):
    def test_oracle_not_in_view(self):
        env = HiddenRegimeWorld(generate_world(3, "Hidden-Irreversible"), 4)
        view = env.agent_view()
        self.assertFalse(hasattr(view, "rfs")); self.assertFalse(hasattr(view, "reachable_future_tasks"))

