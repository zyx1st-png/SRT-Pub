"""Phase-0 executable contracts; not an Agent or proof of efficacy.

Actor labels here are test fixtures, NOT verified identities or a production
security boundary. Real tools require external authentication + scoped grants.
"""
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Hypothesis:
    gts_id: str
    condition: str
    intervention: str
    prediction: str
    failure_condition: str
    provenance: str = "model_hypothesis"


@dataclass
class CollaborationLedger:
    root_goal: str
    allowed_actions: frozenset[str]
    protected_actions: frozenset[str]
    frame_version: int = 1
    events: list[dict] = field(default_factory=list)
    proposals: dict[str, str] = field(default_factory=dict)
    hypotheses: dict[str, Hypothesis] = field(default_factory=dict)
    observations: dict[str, str] = field(default_factory=dict)
    approvals: set[str] = field(default_factory=set)
    beacons: dict[str, int] = field(default_factory=dict)
    history: list[tuple[int, str]] = field(default_factory=list)

    def __post_init__(self):
        if not self.root_goal.strip():
            raise ValueError("root_goal required")
        if not self.protected_actions <= self.allowed_actions:
            raise ValueError("protected actions must be allowed actions")
        self.history.append((self.frame_version, self.root_goal))
        self._record("frame_created", "user", goal=self.root_goal)

    def _record(self, kind, actor, **fields):
        event = {"seq": len(self.events) + 1, "kind": kind, "actor": actor, **fields}
        self.events.append(event)
        return event["seq"]

    def propose_frame(self, proposal_id: str, new_goal: str, *, actor="agent"):
        if actor != "agent" or not proposal_id or not new_goal.strip():
            raise ValueError("invalid proposal")
        if proposal_id in self.proposals:
            raise ValueError("proposal id already used")
        self.proposals[proposal_id] = new_goal
        return self._record("frame_proposed", actor, proposal_id=proposal_id)

    def decide_frame(self, proposal_id: str, accept: bool, *, actor="user"):
        if actor != "user" or proposal_id not in self.proposals:
            raise PermissionError("only user can decide a pending frame")
        goal = self.proposals.pop(proposal_id)
        if accept:
            self.frame_version += 1
            self.root_goal = goal
            self.history.append((self.frame_version, goal))
        return self._record("frame_decided", actor, proposal_id=proposal_id,
                            accepted=bool(accept), frame_version=self.frame_version)

    def propose_gts(self, hypothesis: Hypothesis, *, actor="agent"):
        if actor != "agent" or hypothesis.gts_id in self.hypotheses:
            raise ValueError("duplicate or invalid GTS")
        if not all((hypothesis.condition, hypothesis.intervention,
                    hypothesis.prediction, hypothesis.failure_condition)):
            raise ValueError("GTS requires a testable prediction and failure condition")
        self.hypotheses[hypothesis.gts_id] = hypothesis
        return self._record("gts_proposed", actor, gts_id=hypothesis.gts_id,
                            evidence_status="untested")

    def record_observation(self, evidence_id: str, description: str, *, actor="tool"):
        if actor != "tool" or not evidence_id or not description:
            raise PermissionError("observations require a tool adapter")
        if evidence_id in self.observations:
            raise ValueError("duplicate evidence")
        self.observations[evidence_id] = description
        return self._record("observed", actor, evidence_id=evidence_id)

    def grant_once(self, action: str, *, actor="user"):
        if actor != "user" or action not in self.protected_actions:
            raise PermissionError("only a user may grant an eligible protected action")
        self.approvals.add(action)
        return self._record("action_approved", actor, action=action)

    def execute(self, action: str, evidence_id: str, *, actor="tool"):
        if actor != "tool" or action not in self.allowed_actions:
            raise PermissionError("tool action is not allowed")
        if action in self.protected_actions and action not in self.approvals:
            raise PermissionError("protected action needs fresh approval")
        if not evidence_id or evidence_id in self.observations:
            raise ValueError("unique evidence id required")
        self.approvals.discard(action)  # one-shot approval, consumed upon attempt
        self.record_observation(evidence_id, f"tool result for {action}", actor="tool")
        return self._record("action_executed", actor, action=action,
                            evidence_id=evidence_id)

    def add_beacon(self, key: str, source_seq: int):
        if not key.strip() or source_seq not in range(1, len(self.events) + 1):
            raise ValueError("beacon must reference an existing event")
        self.beacons[key] = source_seq
        return self._record("beacon_added", "agent", key=key, source_seq=source_seq)

    def recover_beacon(self, key: str):
        if key not in self.beacons:
            raise KeyError(key)
        return dict(self.events[self.beacons[key] - 1])
