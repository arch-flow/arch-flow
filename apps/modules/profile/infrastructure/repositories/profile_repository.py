from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from apps.modules.profile.domain.entities.profile_entity import ProfileEntity
from apps.modules.profile.domain.repositories.profile_repository_interface import ProfileRepositoryInterface
from apps.modules.profile.infrastructure.models.profile_model import ProfileModel


class ProfileRepository(ProfileRepositoryInterface):
    def __init__(self, session: Session):
        self.session = session

    def create(self, profile: ProfileEntity) -> None:
        db_profile = ProfileModel.from_entity(profile)
        self.session.add(db_profile)
        self.session.commit()

    def list_paginated(self, offset: int, limit: int) -> List[ProfileEntity]:
        results = (
            self.session.query(ProfileModel)
            .offset(offset)
            .limit(limit)
            .all()
        )
        return [row.to_entity() for row in results]

    def get_by_id(self, profile_id: UUID) -> ProfileEntity | None:
        row = self.session.query(ProfileModel).filter_by(id=profile_id).first()
        if row:
            return row.to_entity()
        return None

    def update(self, profile: ProfileEntity) -> None:
        db_profile = self.session.query(ProfileModel).filter_by(id=profile.id).first()
        if not db_profile:
            return

        db_profile.name = profile.name
        db_profile.purpose = profile.purpose
        db_profile.updated_at = profile.updated_at

        self.session.commit()

    def delete(self, profile: ProfileEntity) -> None:
        self.session.query(ProfileModel).filter_by(id=profile.id).delete()
        self.session.commit()
