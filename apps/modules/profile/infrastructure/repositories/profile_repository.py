from sqlalchemy.orm import Session

from apps.modules.profile.domain.entities.profile_entity import ProfileEntity
from apps.modules.profile.domain.repositories.profile_repository_interface import ProfileRepositoryInterface
from apps.modules.profile.infrastructure.models.profile_model import ProfileModel
from apps.shared.repositories.base_repository import BaseRepository


class ProfileRepository(
    BaseRepository[ProfileEntity, ProfileModel],
    ProfileRepositoryInterface
):
    def __init__(self, session: Session):
        super().__init__(session, ProfileModel)

    def _apply_update(self, entity: ProfileEntity, db_obj: ProfileModel) -> None:
        db_obj.name = entity.name
        db_obj.purpose = entity.purpose
        db_obj.updated_at = entity.updated_at
