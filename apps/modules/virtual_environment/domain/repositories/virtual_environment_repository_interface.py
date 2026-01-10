from typing import Protocol

from apps.modules.virtual_environment.domain.entities.virtual_environment_entity import VirtualEnvironmentEntity
from apps.shared.interfaces.base_repository_interface import BaseRepositoryInterface


class VirtualEnvironmentRepositoryInterface(BaseRepositoryInterface[VirtualEnvironmentEntity], Protocol):
    pass
