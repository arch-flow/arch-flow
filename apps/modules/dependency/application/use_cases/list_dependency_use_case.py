from uuid import UUID

from apps.modules.dependency.domain.repositories.dependency_repository_interface import DependencyRepositoryInterface
from apps.modules.dependency.services.dependency_reader_service import DependencyReaderService
from apps.modules.virtual_environment.domain.repositories.virtual_environment_repository_interface import \
    VirtualEnvironmentRepositoryInterface
from apps.shared.exceptions.entity_not_found_exception import EntityNotFoundException


class ListDependencyUseCase:
    def __init__(
            self,
            dependency_repository: DependencyRepositoryInterface,
            environment_repository: VirtualEnvironmentRepositoryInterface,
    ):
        self.dependency_repository = dependency_repository
        self.environment_repository = environment_repository
        self.reader_service = DependencyReaderService()

    def execute(self, environment_id: UUID) -> dict:
        environment = self.environment_repository.get_by_id(environment_id)
        if not environment:
            raise EntityNotFoundException("VirtualEnvironment")

        registered = self.dependency_repository.list_by_environment_id(environment_id)
        installed = self.reader_service.list_installed(
            profile_id=environment.profile_id,
            environment_name=environment.name
        )

        registered_map = {d.name: d for d in registered}
        installed_map = {d["name"]: d for d in installed}

        missing_in_environment = [
            d for name, d in registered_map.items()
            if name not in installed_map
        ]

        not_registered_but_installed = [
            d for name, d in installed_map.items()
            if name not in registered_map
        ]

        return {
            "registered": registered,
            "installed": installed,
            "missing_in_environment": missing_in_environment,
            "not_registered_but_installed": not_registered_but_installed
        }
