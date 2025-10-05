from dataclasses import dataclass
from typing import Optional, Literal
from uuid import UUID

RunStatus = Literal["PENDING", "RUNNING", "SUCCESS", "FAILED", "SKIPPED"]

@dataclass(frozen=True)
class RunStepRecord:
    id: Optional[UUID]
    run_id: UUID
    order: int
    status: RunStatus
    exit_code: Optional[int]
    stdout_path: Optional[str]
    stderr_path: Optional[str]
    started_at: Optional[float]
    finished_at: Optional[float]
    duration_ms: Optional[int]
