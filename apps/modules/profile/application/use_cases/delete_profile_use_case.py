from apps.modules.profile.domain.repositories.profile_repository_interface import ProfileRepositoryInterface
from uuid import UUID

from apps.shared.exceptions.entity_not_found_exception import EntityNotFoundException


class DeleteProfileUseCase:
    def __init__(self, repository: ProfileRepositoryInterface):
        self.repository = repository

    def execute(self, profile_id: UUID) -> None:
        profile = self.repository.get_by_id(profile_id)
        if not profile:
            raise EntityNotFoundException("Profile")
        self.repository.delete(profile)
