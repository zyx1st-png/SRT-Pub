import unittest
from dataclasses import fields
from src.environment import AgentView

class TestHiddenRegimeIsolation(unittest.TestCase):
    def test_agent_view_has_no_truth(self):
        names = {f.name for f in fields(AgentView)}
        self.assertNotIn("regime", names); self.assertNotIn("true_regime", names)

