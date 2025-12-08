from sqlalchemy.orm import Session

from apps.modules.dependency.application.use_cases.create_dependency_use_case import CreateDependencyUseCase
from apps.modules.dependency.application.use_cases.delete_dependency_use_case import DeleteDependencyUseCase
from apps.modules.dependency.application.use_cases.get_dependency_use_case import GetDependencyUseCase
from apps.modules.dependency.application.use_cases.list_dependency_use_case import ListDependencyUseCase
from apps.modules.dependency.application.use_cases.update_dependency_use_case import UpdateDependencyUseCase
from apps.modules.dependency.infrastructure.repositories.dependency_repository import DependencyRepository
from apps.modules.virtual_environment.infrastructure.repositories.virtual_environment_repository import \
    VirtualEnvironmentRepository


def make_create_dependency_use_case(session: Session) -> CreateDependencyUseCase:
    dependency_repository = DependencyRepository(session)
    environment_repository = VirtualEnvironmentRepository(session)
    return CreateDependencyUseCase(
        dependency_repository,
        environment_repository
    )


def make_list_dependencies_use_case(session: Session) -> ListDependencyUseCase:
    dependency_repository = DependencyRepository(session)
    environment_repository = VirtualEnvironmentRepository(session)
    return ListDependencyUseCase(
        dependency_repository,
        environment_repository
    )


def make_get_dependency_use_case(session: Session) -> GetDependencyUseCase:
    repository = DependencyRepository(session)
    return GetDependencyUseCase(repository)


def make_update_dependency_use_case(session: Session) -> UpdateDependencyUseCase:
    dependency_repository = DependencyRepository(session)
    environment_repository = VirtualEnvironmentRepository(session)
    return UpdateDependencyUseCase(
        dependency_repository,
        environment_repository
    )


def make_delete_dependency_use_case(session: Session) -> DeleteDependencyUseCase:
    dependency_repository = DependencyRepository(session)
    environment_repository = VirtualEnvironmentRepository(session)
    return DeleteDependencyUseCase(
        dependency_repository,
        environment_repository
    )
