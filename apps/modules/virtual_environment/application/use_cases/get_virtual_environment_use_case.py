from uuid import UUID
from apps.modules.virtual_environment.domain.entities.virtual_environment_entity import VirtualEnvironmentEntity
from apps.modules.virtual_environment.domain.repositories.virtual_environment_repository_interface import VirtualEnvironmentRepositoryInterface
from apps.shared.exceptions.entity_not_found_exception import EntityNotFoundException


class GetVirtualEnvironmentUseCase:
    def __init__(self, repository: VirtualEnvironmentRepositoryInterface):
        self.repository = repository

    def execute(self, environment_id: UUID) -> VirtualEnvironmentEntity:
        environment = self.repository.get_by_id(environment_id)
        if not environment:
            raise EntityNotFoundException("VirtualEnvironment")
        return environment
