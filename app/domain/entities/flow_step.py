from dataclasses import dataclass
from typing import Optional, Dict, Any, Literal
from uuid import UUID

ActionType = Literal["python", "shell", "command", "flow_ref"]

@dataclass(frozen=True)
class FlowStep:
    id: Optional[UUID]
    flow_id: Optional[UUID]
    order: int
    action_type: ActionType
    artifact_ref: Optional[str]
    args: Optional[Dict[str, Any]]
    env: Optional[Dict[str, str]]
    working_dir: Optional[str]
    profile_id: Optional[UUID]
    ref_alias: Optional[str]
