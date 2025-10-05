from dataclasses import dataclass
from typing import Optional, Dict, List, Literal
from uuid import UUID

ProfileKind = Literal["python", "shell", "command"]

@dataclass(frozen=True)
class Profile:
    id: Optional[UUID]
    name: str
    kind: ProfileKind
    python_version: Optional[str]
    env_vars: Dict[str, str]
    path_entries: List[str]
