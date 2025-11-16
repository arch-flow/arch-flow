import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone

from apps.modules.virtual_environment.domain.enums.environment_manager import EnvironmentManager
from apps.modules.virtual_environment.domain.enums.python_version import PythonVersion


@dataclass(frozen=True)
class VirtualEnvironmentEntity:
    id: uuid.UUID
    profile_id: uuid.UUID
    name: str
    manager: EnvironmentManager
    python_version: PythonVersion
    active: bool
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
