from uuid import UUID
from apps.modules.virtual_environment.domain.repositories.virtual_environment_repository_interface import VirtualEnvironmentRepositoryInterface
from apps.modules.virtual_environment.services.venv_environment_service import VenvEnvironmentService
from apps.shared.exceptions.entity_not_found_exception import EntityNotFoundException


class DeleteVirtualEnvironmentUseCase:
    def __init__(self, repository: VirtualEnvironmentRepositoryInterface):
        self.repository = repository
        self.environment_service = VenvEnvironmentService()

    def execute(self, environment_id: UUID) -> None:
        environment = self.repository.get_by_id(environment_id)
        if not environment:
            raise EntityNotFoundException("VirtualEnvironment")

        self.environment_service.delete(
            profile_id=environment.profile_id,
            name=environment.name
        )
        self.repository.delete(environment)
