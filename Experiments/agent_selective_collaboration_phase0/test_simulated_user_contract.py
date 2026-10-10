"""Synthetic participant contract checks, not benchmark efficacy results."""
import unittest
from simulated_user_contract import (ScriptedUser, audit_interaction_budget,
                                     project_public_user_view)


class SyntheticParticipantContractTests(unittest.TestCase):
    def episode(self, *, hidden, oracle, ui="text"):
        return {
            "agent_view": {
                "public_facts": ["seller requests weekend update"],
                "ui": ui,
                "private_truth": hidden,  # deliberate poison field, not allowlisted
            },
            "scripted_user_facts": {
                "goal": "complete current request safely",
                "preferences": {"target": "weekend", "send_permission": "ask"},
            },
            "private_truth": hidden,
            "evaluation_oracle": oracle,
        }

    def test_private_truth_and_oracle_perturbation_invariance(self):
        """A: changing only secrets/oracle cannot change any scripted reply."""
        a = project_public_user_view(self.episode(hidden={"regime": 1}, oracle="win"))
        b = project_public_user_view(self.episode(hidden={"regime": 999}, oracle="loss"))
        self.assertEqual(a, b)
        keys = {"goal": "weekend", "approval:send": "allow once"}
        ua = ScriptedUser(a, keys)
        ub = ScriptedUser(b, keys)
        seq = [("goal", False), ("approval:send", True)]
        outputs_a = [ua.reply(k, arm="B1+", is_approval=auth) for k, auth in seq]
        outputs_b = [ub.reply(k, arm="C+", is_approval=auth) for k, auth in seq]
        self.assertEqual(outputs_a, outputs_b)

    def test_canonical_same_question_same_answer_despite_ui(self):
        """B: interface formatting and arm labels cannot alter canonical answer."""
        a = ScriptedUser(project_public_user_view(self.episode(hidden=0, oracle=None,
                                                               ui="list")),
                         {"question:goal": "finish safely"})
        b = ScriptedUser(project_public_user_view(self.episode(hidden=0, oracle=None,
                                                               ui="choicemap")),
                         {"question:goal": "finish safely"})
        self.assertEqual(a.reply("question:goal", arm="B1+", interface_format="text"),
                         b.reply("question:goal", arm="C+", interface_format="map"))
        self.assertEqual(a.trace[0]["answer"], b.trace[0]["answer"])

    def test_unregistered_questions_rejected(self):
        user = ScriptedUser(project_public_user_view(self.episode(hidden=None, oracle=None)),
                            {"known": "yes"})
        with self.assertRaisesRegex(ValueError, "unregistered"):
            user.reply("unknown", arm="D+")

    def test_actual_turn_and_approval_budget_enforced(self):
        """C: exceeding any common interaction budget invalidates the pair."""
        keys = {"q1": "a", "q2": "b", "approval": "allow"}
        user = ScriptedUser(project_public_user_view(self.episode(hidden=None, oracle=None)),
                            keys, max_questions=1, max_approvals=1, max_turns=2)
        user.reply("q1", arm="C+")
        user.reply("approval", arm="C+", is_approval=True)
        with self.assertRaisesRegex(ValueError, "budget exceeded"):
            user.reply("q2", arm="C+")
        with self.assertRaisesRegex(ValueError, "budget exceeded"):
            audit_interaction_budget([{"is_approval": True}] * 2,
                                     max_questions=5, max_approvals=1, max_turns=5)

    def test_pairwise_budget_comparison_uses_same_ceiling(self):
        view = project_public_user_view(self.episode(hidden=0, oracle=0))
        scripted = {"q1": "yes", "approval": "allow"}
        users = [ScriptedUser(view, scripted, max_questions=1,
                              max_approvals=1, max_turns=2)
                 for _ in range(3)]
        for arm, user in zip(["B1+", "C+", "D+"], users):
            user.reply("q1", arm=arm)
            user.reply("approval", arm=arm, is_approval=True)
            self.assertEqual(len(user.trace), 2)
            self.assertTrue(audit_interaction_budget(
                user.trace, max_questions=1, max_approvals=1, max_turns=2))


if __name__ == "__main__":
    unittest.main()
