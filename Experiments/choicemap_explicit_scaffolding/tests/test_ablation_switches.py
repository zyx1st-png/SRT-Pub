import unittest
from _helpers import CONFIG
from src.agents import make_agent

class TestAblations(unittest.TestCase):
    def test_all_switches_construct(self):
        for name in ["C-noProbe", "C-noReversibility", "C-noBranchMemory", "C-immediateCommit", "C-scalarized"]:
            self.assertEqual(make_agent(name, CONFIG).system, name)

