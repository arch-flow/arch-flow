from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from apps.modules.dependency.domain.enums.dependency_source_enum import DependencySourceEnum


class DependencyOutputDTO(BaseModel):
    id: UUID
    environment_id: UUID
    name: str
    version: str
    source: DependencySourceEnum
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_entity(cls, entity) -> "DependencyOutputDTO":
        return cls(
            id=entity.id,
            environment_id=entity.environment_id,
            name=entity.name,
            version=entity.version,
            source=entity.source,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )
