import uuid
from datetime import datetime, timezone
from sqlalchemy import String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.sqlite import BLOB
from apps.infrastructure.database.base import Base
from apps.modules.virtual_environment.domain.entities.virtual_environment_entity import VirtualEnvironmentEntity
from apps.modules.virtual_environment.domain.enums.environment_manager import EnvironmentManager
from apps.modules.virtual_environment.domain.enums.python_version import PythonVersion


class VirtualEnvironmentModel(Base):
    __tablename__ = "virtual_environments"

    id: Mapped[bytes] = mapped_column(BLOB, primary_key=True, default=lambda: uuid.uuid4().bytes)
    profile_id: Mapped[bytes] = mapped_column(BLOB, ForeignKey("profiles.id"), nullable=False)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    manager: Mapped[str] = mapped_column(String, nullable=False)
    python_version: Mapped[str] = mapped_column(String, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    def to_entity(self) -> VirtualEnvironmentEntity:
        return VirtualEnvironmentEntity(
            id=uuid.UUID(bytes=getattr(self, 'id')),
            profile_id=uuid.UUID(bytes=getattr(self, 'profile_id')),
            name=str(self.name),
            manager=EnvironmentManager(self.manager),
            python_version=PythonVersion(self.python_version),
            active=bool(self.active),
            created_at=getattr(self, 'created_at'),
            updated_at=getattr(self, 'updated_at'),
        )

    @classmethod
    def from_entity(cls, e: VirtualEnvironmentEntity) -> "VirtualEnvironmentModel":
        return cls(
            id=(e.id.bytes if isinstance(e.id, uuid.UUID) else e.id),
            profile_id=(e.profile_id.bytes if isinstance(e.profile_id, uuid.UUID) else e.profile_id),
            name=e.name,
            manager=e.manager.value,
            python_version=e.python_version.value,
            active=e.active,
            created_at=e.created_at,
            updated_at=e.updated_at,
        )
