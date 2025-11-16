import uuid

from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from apps.infrastructure.database.base import Base
from apps.infrastructure.database.base import GUID
from apps.modules.virtual_environment.domain.entities.virtual_environment_entity import VirtualEnvironmentEntity
from apps.modules.virtual_environment.domain.enums.environment_manager import EnvironmentManager
from apps.modules.virtual_environment.domain.enums.python_version import PythonVersion


class VirtualEnvironmentModel(Base):
    __tablename__ = "virtual_environments"

    profile_id: Mapped[uuid.UUID] = mapped_column(
        GUID(),
        ForeignKey("profiles.id"),
        nullable=False
    )
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    manager: Mapped[str] = mapped_column(String, nullable=False)
    python_version: Mapped[str] = mapped_column(String, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    def to_entity(self) -> VirtualEnvironmentEntity:
        return VirtualEnvironmentEntity(
            id=self.id,
            profile_id=self.profile_id,
            name=self.name,
            manager=EnvironmentManager(self.manager),
            python_version=PythonVersion(self.python_version),
            active=self.active,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @classmethod
    def from_entity(cls, e: VirtualEnvironmentEntity) -> "VirtualEnvironmentModel":
        return cls(
            id=e.id,
            profile_id=e.profile_id,
            name=e.name,
            manager=e.manager.value,
            python_version=e.python_version.value,
            active=e.active,
            created_at=e.created_at,
            updated_at=e.updated_at,
        )
