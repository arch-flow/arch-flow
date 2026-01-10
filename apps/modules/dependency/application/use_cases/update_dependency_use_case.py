from dataclasses import replace
from datetime import datetime, timezone
from uuid import UUID

from apps.modules.dependency.application.dto.update_dependency_dto import UpdateDependencyDTO
from apps.modules.dependency.domain.entities.dependency_entity import DependencyEntity
from apps.modules.dependency.domain.repositories.dependency_repository_interface import DependencyRepositoryInterface
from apps.modules.dependency.services.dependency_package_service import DependencyPackageService
from apps.modules.virtual_environment.domain.repositories.virtual_environment_repository_interface import \
    VirtualEnvironmentRepositoryInterface
from apps.shared.exceptions.entity_not_found_exception import EntityNotFoundException


class UpdateDependencyUseCase:
    def __init__(
            self,
            repository: DependencyRepositoryInterface,
            environment_repository: VirtualEnvironmentRepositoryInterface
    ):
        self.repository = repository
        self.environment_repository = environment_repository
        self.updater_service = DependencyPackageService()

    def execute(self, dependency_id: UUID, data: UpdateDependencyDTO) -> DependencyEntity:
        dependency = self.repository.get_by_id(dependency_id)
        if not dependency:
            raise EntityNotFoundException("Dependency")

        environment = self.environment_repository.get_by_id(dependency.environment_id)
        if not environment:
            raise EntityNotFoundException("VirtualEnvironment")

        package_name = data.name or dependency.name
        package_version = data.version or dependency.version

        self.updater_service.update(
            profile_id=environment.profile_id,
            environment_name=environment.name,
            package=package_name,
            version=package_version
        )

        updated = replace(
            dependency,
            name=data.name,
            version=data.version,
            source=data.source,
            updated_at=datetime.now(timezone.utc)
        )

        self.repository.update(updated)
        return updated
