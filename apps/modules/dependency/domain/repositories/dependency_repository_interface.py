from typing import Protocol, List
from uuid import UUID

from apps.modules.dependency.domain.entities.dependency_entity import DependencyEntity
from apps.shared.interfaces.base_repository_interface import BaseRepositoryInterface


class DependencyRepositoryInterface(BaseRepositoryInterface[DependencyEntity], Protocol):
    def list_by_environment_id(self, environment_id: UUID) -> List[DependencyEntity]:
        pass
