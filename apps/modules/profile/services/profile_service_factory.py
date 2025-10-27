from sqlalchemy.orm import Session

from apps.modules.profile.application.use_cases.delete_profile_use_case import DeleteProfileUseCase
from apps.modules.profile.application.use_cases.get_profile_use_case import GetProfileUseCase
from apps.modules.profile.application.use_cases.update_profile_use_case import UpdateProfileUseCase
from apps.modules.profile.infrastructure.repositories.profile_repository import ProfileRepository
from apps.modules.profile.application.use_cases.create_profile_use_case import CreateProfileUseCase
from apps.modules.profile.application.use_cases.list_profile_use_case import ListProfilesUseCase

def make_create_profile_use_case(session: Session) -> CreateProfileUseCase:
    repository = ProfileRepository(session)
    return CreateProfileUseCase(repository)

def make_list_profiles_use_case(session: Session) -> ListProfilesUseCase:
    repository = ProfileRepository(session)
    return ListProfilesUseCase(repository)

def make_update_profile_use_case(session: Session) -> UpdateProfileUseCase:
    repository = ProfileRepository(session)
    return UpdateProfileUseCase(repository)

def make_get_profile_use_case(session: Session) -> GetProfileUseCase:
    repository = ProfileRepository(session)
    return GetProfileUseCase(repository)

def make_delete_profile_use_case(session: Session) -> DeleteProfileUseCase:
    repository = ProfileRepository(session)
    return DeleteProfileUseCase(repository)
