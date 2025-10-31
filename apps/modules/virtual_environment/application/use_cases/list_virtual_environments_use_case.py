from typing import List

from apps.modules.virtual_environment.application.dto.list_virtual_environments_dto import ListVirtualEnvironmentsDTO
from apps.modules.virtual_environment.domain.entities.virtual_environment_entity import VirtualEnvironmentEntity

from apps.modules.virtual_environment.domain.repositories.virtual_environment_repository_interface import VirtualEnvironmentRepositoryInterface


class ListVirtualEnvironmentsUseCase:
    def __init__(self, repository: VirtualEnvironmentRepositoryInterface):
        self.repository = repository

    def execute(self, data: ListVirtualEnvironmentsDTO) -> List[VirtualEnvironmentEntity]:
        return self.repository.list_paginated(data.offset, data.limit)
