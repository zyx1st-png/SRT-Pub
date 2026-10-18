"""Executable information-parity scaffold for synthetic user interactions.

No Agent, model, environment simulator, or efficacy experiment is provided.
Question keys and user facts must be preregistered. The common responder is
deliberately blind to arm id, interface formatting, private truth and oracle.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class PublicUserView:
    goal: str
    preferences: tuple[tuple[str, str], ...]
    public_facts: tuple[str, ...]


def project_public_user_view(episode: dict) -> PublicUserView:
    """Strict allowlist projection. Never pass private truth/oracle to policy."""
    observed = episode["agent_view"]  # public fields only
    facts = episode["scripted_user_facts"]  # predeclared shared preferences
    prefs = tuple(sorted(facts["preferences"].items()))
    return PublicUserView(
        goal=facts["goal"],
        preferences=prefs,
        public_facts=tuple(observed["public_facts"]),
    )


class ScriptedUser:
    """Fixture: equal canonical question keys give equal responses across arms.

    This test double deliberately ignores both arm and interface_format.
    It cannot yet serve as a participant policy for benchmark claims.
    """

    def __init__(self, view: PublicUserView, responses: dict[str, str],
                 *, max_questions=4, max_approvals=2, max_turns=5):
        self.view = view
        self._responses = dict(responses)  # predeclared from same scenario
        self.max_questions = max_questions
        self.max_approvals = max_approvals
        self.max_turns = max_turns
        self._trace = []

    @property
    def trace(self):
        return tuple(dict(e) for e in self._trace)

    def reply(self, question_key: str, *, arm: str, interface_format: str = "text",
              is_approval=False):
        """Canonical key, never raw model text; no response to unknown questions."""
        if not isinstance(question_key, str) or question_key not in self._responses:
            raise ValueError("unregistered canonical question key")
        self._trace.append({"arm": arm, "question_key": question_key,
                            "is_approval": bool(is_approval),
                            "answer": self._responses[question_key]})
        audit_interaction_budget(self._trace, max_questions=self.max_questions,
                                 max_approvals=self.max_approvals,
                                 max_turns=self.max_turns)
        return self._responses[question_key]


def audit_interaction_budget(trace, *, max_questions, max_approvals, max_turns):
    """Fail closed on actual user-turn, question and approval budget overruns."""
    if (len(trace) > max_turns
            or sum(not x["is_approval"] for x in trace) > max_questions
            or sum(x["is_approval"] for x in trace) > max_approvals):
        raise ValueError("simulated-user budget exceeded: paired comparison invalid")
    return True
