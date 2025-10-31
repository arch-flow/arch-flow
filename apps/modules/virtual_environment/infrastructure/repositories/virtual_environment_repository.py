from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from apps.modules.virtual_environment.domain.entities.virtual_environment_entity import VirtualEnvironmentEntity
from apps.modules.virtual_environment.domain.repositories.virtual_environment_repository_interface import VirtualEnvironmentRepositoryInterface
from apps.modules.virtual_environment.infrastructure.models.virtual_environment_model import VirtualEnvironmentModel


class VirtualEnvironmentRepository(VirtualEnvironmentRepositoryInterface):
    def __init__(self, session: Session):
        self.session = session

    def create(self, environment: VirtualEnvironmentEntity) -> None:
        db_environment = VirtualEnvironmentModel.from_entity(environment)
        self.session.add(db_environment)
        self.session.commit()

    def list_paginated(self, offset: int, limit: int) -> List[VirtualEnvironmentEntity]:
        results = (
            self.session.query(VirtualEnvironmentModel)
            .offset(offset)
            .limit(limit)
            .all()
        )
        return [row.to_entity() for row in results]

    def get_by_id(self, environment_id: UUID) -> VirtualEnvironmentEntity | None:
        row = self.session.query(VirtualEnvironmentModel).filter_by(id=environment_id.bytes).first()
        if row:
            return row.to_entity()
        return None

    def update(self, environment: VirtualEnvironmentEntity) -> None:
        db_environment = self.session.query(VirtualEnvironmentModel).filter_by(id=environment.id.bytes).first()
        if not db_environment:
            return

        db_environment.name = environment.name
        db_environment.manager = environment.manager.value
        db_environment.python_version = environment.python_version.value
        db_environment.active = environment.active
        db_environment.updated_at = environment.updated_at

        self.session.commit()

    def delete(self, environment: VirtualEnvironmentEntity) -> None:
        self.session.query(VirtualEnvironmentModel).filter_by(id=environment.id.bytes).delete()
        self.session.commit()

    def exists(self, environment_id: UUID) -> bool:
        return self.session.query(VirtualEnvironmentModel).filter_by(id=environment_id.bytes).first() is not None
