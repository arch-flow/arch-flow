from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID

from apps.modules.virtual_environment.domain.enums.environment_manager_enum import EnvironmentManagerEnum
from apps.modules.virtual_environment.domain.enums.python_version_enum import PythonVersionEnum


@dataclass(frozen=True)
class VirtualEnvironmentEntity:
    id: UUID
    profile_id: UUID
    name: str
    manager: EnvironmentManagerEnum
    python_version: PythonVersionEnum
    active: bool
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
