from typing import List
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from apps.modules.dependency.domain.entities.dependency_entity import DependencyEntity
from apps.modules.dependency.domain.repositories.dependency_repository_interface import DependencyRepositoryInterface
from apps.modules.dependency.infrastructure.models.dependency_model import DependencyModel
from apps.shared.repositories.base_repository import BaseRepository


class DependencyRepository(
    BaseRepository[DependencyEntity, DependencyModel],
    DependencyRepositoryInterface
):
    def __init__(self, session: Session):
        super().__init__(session, DependencyModel)

    def _apply_update(self, entity: DependencyEntity, db_obj: DependencyModel) -> None:
        db_obj.name = entity.name
        db_obj.version = entity.version
        db_obj.source = entity.source.value
        db_obj.updated_at = entity.updated_at

    def list_by_environment_id(self, environment_id: UUID) -> List[DependencyEntity]:
        results = (
            self.session.execute(
                select(DependencyModel).where(DependencyModel.environment_id == str(environment_id))
            ).scalars().all()
        )
        return [dep.to_entity() for dep in results]
