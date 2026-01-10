from typing import List
from apps.modules.profile.domain.entities.profile_entity import ProfileEntity
from apps.modules.profile.application.dto.list_profiles_dto import ListProfilesDTO
from apps.modules.profile.domain.repositories.profile_repository_interface import ProfileRepositoryInterface

class ListProfilesUseCase:
    def __init__(self, repository: ProfileRepositoryInterface):
        self.repository = repository

    def execute(self, data: ListProfilesDTO) -> List[ProfileEntity]:
        return self.repository.list_paginated(data.offset, data.limit)
