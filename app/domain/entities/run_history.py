from dataclasses import dataclass
from typing import Optional, Literal
from uuid import UUID

RunStatus = Literal["PENDING", "RUNNING", "SUCCESS", "FAILED", "SKIPPED"]

@dataclass(frozen=True)
class RunHistory:
    id: Optional[UUID]
    flow_id: UUID
    status: RunStatus
    started_at: Optional[float]
    finished_at: Optional[float]
    duration_ms: Optional[int]
