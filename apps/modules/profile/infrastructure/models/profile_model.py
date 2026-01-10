from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from apps.infrastructure.database.base import Base
from apps.modules.profile.domain.entities.profile_entity import ProfileEntity


class ProfileModel(Base):
    __tablename__ = "profiles"

    name: Mapped[str] = mapped_column(String, nullable=False)
    purpose: Mapped[str] = mapped_column(String, nullable=True)

    def to_entity(self) -> ProfileEntity:
        return ProfileEntity(
            id=self.id,
            name=self.name,
            purpose=self.purpose,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @classmethod
    def from_entity(cls, e: ProfileEntity) -> "ProfileModel":
        return cls(
            id=e.id,
            name=e.name,
            purpose=e.purpose,
            created_at=e.created_at,
            updated_at=e.updated_at,
        )
