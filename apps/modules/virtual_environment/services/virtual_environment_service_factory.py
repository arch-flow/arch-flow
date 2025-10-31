from sqlalchemy.orm import Session

from apps.modules.virtual_environment.application.use_cases.create_virtual_environment_use_case import CreateVirtualEnvironmentUseCase
from apps.modules.virtual_environment.application.use_cases.list_virtual_environments_use_case import ListVirtualEnvironmentsUseCase
from apps.modules.virtual_environment.application.use_cases.get_virtual_environment_use_case import GetVirtualEnvironmentUseCase
from apps.modules.virtual_environment.application.use_cases.update_virtual_environment_use_case import UpdateVirtualEnvironmentUseCase
from apps.modules.virtual_environment.application.use_cases.delete_virtual_environment_use_case import DeleteVirtualEnvironmentUseCase
from apps.modules.virtual_environment.infrastructure.repositories.virtual_environment_repository import VirtualEnvironmentRepository
from apps.modules.profile.infrastructure.repositories.profile_repository import ProfileRepository


def make_create_virtual_environment_use_case(session: Session) -> CreateVirtualEnvironmentUseCase:
    environment_repository = VirtualEnvironmentRepository(session)
    profile_repository = ProfileRepository(session)
    return CreateVirtualEnvironmentUseCase(environment_repository, profile_repository)


def make_list_virtual_environments_use_case(session: Session) -> ListVirtualEnvironmentsUseCase:
    repository = VirtualEnvironmentRepository(session)
    return ListVirtualEnvironmentsUseCase(repository)


def make_get_virtual_environment_use_case(session: Session) -> GetVirtualEnvironmentUseCase:
    repository = VirtualEnvironmentRepository(session)
    return GetVirtualEnvironmentUseCase(repository)


def make_update_virtual_environment_use_case(session: Session) -> UpdateVirtualEnvironmentUseCase:
    repository = VirtualEnvironmentRepository(session)
    return UpdateVirtualEnvironmentUseCase(repository)


def make_delete_virtual_environment_use_case(session: Session) -> DeleteVirtualEnvironmentUseCase:
    repository = VirtualEnvironmentRepository(session)
    return DeleteVirtualEnvironmentUseCase(repository)
