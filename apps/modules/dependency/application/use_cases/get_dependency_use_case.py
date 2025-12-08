from uuid import UUID

from apps.modules.dependency.domain.entities.dependency_entity import DependencyEntity
from apps.modules.dependency.domain.repositories.dependency_repository_interface import DependencyRepositoryInterface
from apps.shared.exceptions.entity_not_found_exception import EntityNotFoundException


class GetDependencyUseCase:
    def __init__(self, repository: DependencyRepositoryInterface):
        self.repository = repository

    def execute(self, dependency_id: UUID) -> DependencyEntity:
        dependency = self.repository.get_by_id(dependency_id)
        if not dependency:
            raise EntityNotFoundException("Dependency")
        return dependency
