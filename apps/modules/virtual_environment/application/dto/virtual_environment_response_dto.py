from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from apps.modules.virtual_environment.domain.enums.environment_manager import EnvironmentManager
from apps.modules.virtual_environment.domain.enums.python_version import PythonVersion


class VirtualEnvironmentResponseDTO(BaseModel):
    id: UUID
    profile_id: UUID
    name: str
    manager: EnvironmentManager
    python_version: PythonVersion
    active: bool
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_entity(cls, entity) -> "VirtualEnvironmentResponseDTO":
        return cls(
            id=entity.id,
            profile_id=entity.profile_id,
            name=entity.name,
            manager=entity.manager,
            python_version=entity.python_version,
            active=entity.active,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )
