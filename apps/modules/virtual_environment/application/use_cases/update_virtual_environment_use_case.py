from uuid import UUID
from datetime import datetime, timezone
from dataclasses import replace
from apps.modules.virtual_environment.application.dto.update_virtual_environment_dto import UpdateVirtualEnvironmentDTO
from apps.modules.virtual_environment.domain.repositories.virtual_environment_repository_interface import VirtualEnvironmentRepositoryInterface
from apps.shared.exceptions.entity_not_found_exception import EntityNotFoundException


class UpdateVirtualEnvironmentUseCase:
    def __init__(self, repository: VirtualEnvironmentRepositoryInterface):
        self.repository = repository

    def execute(self, environment_id: UUID, data: UpdateVirtualEnvironmentDTO) -> None:
        environment = self.repository.get_by_id(environment_id)

        if not environment:
            raise EntityNotFoundException("VirtualEnvironment not found")

        updated_environment = replace(
            environment,
            name=data.name,
            manager=data.manager,
            python_version=data.python_version,
            updated_at=datetime.now(timezone.utc)
        )

        self.repository.update(updated_environment)
