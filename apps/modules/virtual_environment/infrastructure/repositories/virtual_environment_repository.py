from sqlalchemy.orm import Session

from apps.modules.virtual_environment.domain.entities.virtual_environment_entity import VirtualEnvironmentEntity
from apps.modules.virtual_environment.domain.repositories.virtual_environment_repository_interface import \
    VirtualEnvironmentRepositoryInterface
from apps.modules.virtual_environment.infrastructure.models.virtual_environment_model import VirtualEnvironmentModel
from apps.shared.repositories.base_repository import BaseRepository


class VirtualEnvironmentRepository(
    BaseRepository[VirtualEnvironmentEntity, VirtualEnvironmentModel],
    VirtualEnvironmentRepositoryInterface
):
    def __init__(self, session: Session):
        super().__init__(session, VirtualEnvironmentModel)

    def _apply_update(self, entity: VirtualEnvironmentEntity, db_obj: VirtualEnvironmentModel) -> None:
        db_obj.name = entity.name
        db_obj.manager = entity.manager.value
        db_obj.python_version = entity.python_version.value
        db_obj.active = entity.active
        db_obj.updated_at = entity.updated_at
