import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.sqlite import BLOB
from sqlalchemy import String, DateTime
from apps.infrastructure.database.base import Base
from apps.modules.profile.domain.entities.profile_entity import ProfileEntity


class ProfileModel(Base):
    __tablename__ = "profiles"

    id: Mapped[bytes] = mapped_column(BLOB, primary_key=True, default=lambda: uuid.uuid4().bytes)
    name: Mapped[str] = mapped_column(String, nullable=False)
    purpose: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    def to_entity(self) -> ProfileEntity:
        return ProfileEntity(
            id=uuid.UUID(bytes=self.id),
            name=self.name,
            purpose=self.purpose,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @classmethod
    def from_entity(cls, e: ProfileEntity) -> "ProfileModel":
        return cls(
            id=(e.id.bytes if isinstance(e.id, uuid.UUID) else e.id),
            name=e.name,
            purpose=e.purpose,
            created_at=e.created_at,
            updated_at=e.updated_at,
        )
