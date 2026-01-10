from datetime import datetime, timezone
from uuid import uuid4

from apps.modules.profile.domain.repositories.profile_repository_interface import ProfileRepositoryInterface
from apps.modules.virtual_environment.application.dto.create_virtual_environment_dto import CreateVirtualEnvironmentDTO
from apps.modules.virtual_environment.domain.entities.virtual_environment_entity import VirtualEnvironmentEntity
from apps.modules.virtual_environment.domain.repositories.virtual_environment_repository_interface import \
    VirtualEnvironmentRepositoryInterface
from apps.modules.virtual_environment.services.venv_environment_service import VenvEnvironmentService
from apps.shared.exceptions.entity_not_found_exception import EntityNotFoundException


class CreateVirtualEnvironmentUseCase:
    def __init__(
            self,
            repository: VirtualEnvironmentRepositoryInterface,
            profile_repository: ProfileRepositoryInterface,
    ):
        self.repository = repository
        self.profile_repository = profile_repository
        self.environment_creator = VenvEnvironmentService()

    def execute(self, data: CreateVirtualEnvironmentDTO) -> VirtualEnvironmentEntity:
        if not self.profile_repository.get_by_id(data.profile_id):
            raise EntityNotFoundException("Profile")

        self.environment_creator.create(
            profile_id=data.profile_id,
            name=data.name,
            python_version=data.python_version.value
        )

        environment = VirtualEnvironmentEntity(
            id=uuid4(),
            profile_id=data.profile_id,
            name=data.name,
            manager=data.manager,
            python_version=data.python_version,
            active=True,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )

        self.repository.create(environment)
        return environment
