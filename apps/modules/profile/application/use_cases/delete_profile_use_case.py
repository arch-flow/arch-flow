import shutil
from pathlib import Path
from uuid import UUID

from apps.modules.profile.domain.repositories.profile_repository_interface import ProfileRepositoryInterface
from apps.shared.exceptions.entity_not_found_exception import EntityNotFoundException


class DeleteProfileUseCase:
    def __init__(self, repository: ProfileRepositoryInterface):
        self.repository = repository

    def execute(self, profile_id: UUID) -> None:
        profile = self.repository.get_by_id(profile_id)
        if not profile:
            raise EntityNotFoundException("Profile")
        self.repository.delete(profile)
        self._delete_profile_directory(profile_id)

    @staticmethod
    def _delete_profile_directory(profile_id: UUID) -> None:
        base_path = Path("data/profiles") / str(profile_id)
        if base_path.exists() and base_path.is_dir():
            shutil.rmtree(base_path)
