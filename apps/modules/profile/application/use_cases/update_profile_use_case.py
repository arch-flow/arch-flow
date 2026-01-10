from datetime import datetime, timezone
from uuid import UUID

from apps.modules.profile.application.dto.update_profile_dto import UpdateProfileDTO
from apps.modules.profile.domain.entities.profile_entity import ProfileEntity
from apps.modules.profile.domain.repositories.profile_repository_interface import ProfileRepositoryInterface
from apps.shared.exceptions.entity_not_found_exception import EntityNotFoundException


class UpdateProfileUseCase:
    def __init__(self, repository: ProfileRepositoryInterface):
        self.repository = repository

    def execute(self, profile_id: UUID, data: UpdateProfileDTO) -> ProfileEntity:
        profile = self.repository.get_by_id(profile_id)

        if not profile:
            raise EntityNotFoundException("Profile not found")

        profile.name = data.name
        profile.purpose = data.purpose
        profile.updated_at = datetime.now(timezone.utc)
        self.repository.update(profile)
        return profile
