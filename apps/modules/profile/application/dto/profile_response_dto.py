from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ProfileResponseDTO(BaseModel):
    id: UUID
    name: str
    purpose: str | None
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_entity(cls, entity) -> "ProfileResponseDTO":
        return cls(
            id=entity.id,
            name=entity.name,
            purpose=entity.purpose,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )
