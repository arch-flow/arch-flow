from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from apps.modules.profile.application.dto.create_profile_dto import CreateProfileDTO
from apps.modules.profile.domain.entities.profile_entity import ProfileEntity
from apps.modules.profile.domain.repositories.profile_repository_interface import ProfileRepositoryInterface


class CreateProfileUseCase:
    def __init__(self, repository: ProfileRepositoryInterface):
        self.repository = repository

    def execute(self, data: CreateProfileDTO) -> ProfileEntity:
        profile = ProfileEntity(
            id=uuid4(),
            name=data.name,
            purpose=data.purpose,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        self.repository.create(profile)
        self._create_profile_directory(profile.id)
        return profile

    @staticmethod
    def _create_profile_directory(profile_id) -> None:
        base_path = Path("data/profiles") / str(profile_id)
        base_path.mkdir(parents=True, exist_ok=True)
