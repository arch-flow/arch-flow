from datetime import datetime, timezone
from uuid import uuid4

from apps.modules.dependency.application.dto.create_dependency_dto import CreateDependencyDTO
from apps.modules.dependency.domain.entities.dependency_entity import DependencyEntity
from apps.modules.dependency.domain.repositories.dependency_repository_interface import DependencyRepositoryInterface
from apps.modules.dependency.services.dependency_package_service import DependencyPackageService
from apps.modules.virtual_environment.domain.repositories.virtual_environment_repository_interface import \
    VirtualEnvironmentRepositoryInterface
from apps.shared.exceptions.entity_not_found_exception import EntityNotFoundException


class CreateDependencyUseCase:
    def __init__(
            self,
            repository: DependencyRepositoryInterface,
            environment_repository: VirtualEnvironmentRepositoryInterface,
    ):
        self.repository = repository
        self.environment_repository = environment_repository
        self.installer_service = DependencyPackageService()

    def execute(self, data: CreateDependencyDTO) -> DependencyEntity:
        environment = self.environment_repository.get_by_id(data.environment_id)
        if not environment:
            raise EntityNotFoundException("VirtualEnvironment")

        self.installer_service.install(
            profile_id=environment.profile_id,
            environment_name=environment.name,
            package=data.name,
            version=data.version,
        )

        dependency = DependencyEntity(
            id=uuid4(),
            environment_id=data.environment_id,
            name=data.name,
            version=data.version,
            source=data.source,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )

        self.repository.create(dependency)
        return dependency
