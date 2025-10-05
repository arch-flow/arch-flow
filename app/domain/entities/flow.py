from dataclasses import dataclass, field
from typing import List, Optional
from uuid import UUID

@dataclass(frozen=True)
class Flow:
    id: Optional[UUID]
    alias: str
    name: str
    short_description: str
    long_description: Optional[str]
    steps: List["FlowStep"] = field(default_factory=list)
