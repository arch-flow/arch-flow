from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from apps.infrastructure.database.base import Base
from apps.infrastructure.database.base import GUID
from apps.modules.dependency.domain.entities.dependency_entity import DependencyEntity
from apps.modules.dependency.domain.enums.dependency_source_enum import DependencySourceEnum


class DependencyModel(Base):
    __tablename__ = "dependency"

    environment_id: Mapped[UUID] = mapped_column(
        GUID(),
        ForeignKey("virtual_environments.id", ondelete="CASCADE")
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    version: Mapped[str] = mapped_column(String, nullable=False)
    source: Mapped[str] = mapped_column(String, nullable=False)

    def to_entity(self) -> DependencyEntity:
        return DependencyEntity(
            id=self.id,
            environment_id=self.environment_id,
            name=self.name,
            version=self.version,
            source=DependencySourceEnum(self.source),
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    @classmethod
    def from_entity(cls, entity: DependencyEntity) -> "DependencyModel":
        return cls(
            id=entity.id,
            environment_id=entity.environment_id,
            name=entity.name,
            version=entity.version,
            source=entity.source.value,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )
