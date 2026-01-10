from apps.modules.profile.domain.entities.profile_entity import ProfileEntity
from apps.modules.profile.domain.repositories.profile_repository_interface import ProfileRepositoryInterface
from apps.shared.exceptions.entity_not_found_exception import EntityNotFoundException
from uuid import UUID

class GetProfileUseCase:
    def __init__(self, repository: ProfileRepositoryInterface):
        self.repository = repository

    def execute(self, profile_id: UUID) -> ProfileEntity:
        profile = self.repository.get_by_id(profile_id)
        if not profile:
            raise EntityNotFoundException("Profile")
        return profile
