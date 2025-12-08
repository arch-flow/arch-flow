from uuid import UUID

from apps.modules.dependency.domain.repositories.dependency_repository_interface import DependencyRepositoryInterface
from apps.modules.dependency.services.dependency_package_service import DependencyPackageService
from apps.modules.virtual_environment.domain.repositories.virtual_environment_repository_interface import \
    VirtualEnvironmentRepositoryInterface
from apps.shared.exceptions.entity_not_found_exception import EntityNotFoundException


class DeleteDependencyUseCase:
    def __init__(
            self,
            repository: DependencyRepositoryInterface,
            environment_repository: VirtualEnvironmentRepositoryInterface,
    ):
        self.repository = repository
        self.environment_repository = environment_repository
        self.package_service = DependencyPackageService()

    def execute(self, dependency_id: UUID) -> None:
        dependency = self.repository.get_by_id(dependency_id)
        if not dependency:
            raise EntityNotFoundException("Dependency")

        environment = self.environment_repository.get_by_id(dependency.environment_id)
        if not environment:
            raise EntityNotFoundException("VirtualEnvironment")

        self.package_service.uninstall(
            profile_id=environment.profile_id,
            environment_name=environment.name,
            package=dependency.name
        )

        self.repository.delete(dependency)
