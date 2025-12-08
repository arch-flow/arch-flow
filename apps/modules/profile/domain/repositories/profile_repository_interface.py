from typing import Protocol

from apps.modules.profile.domain.entities.profile_entity import ProfileEntity
from apps.shared.interfaces.base_repository_interface import BaseRepositoryInterface


class ProfileRepositoryInterface(BaseRepositoryInterface[ProfileEntity], Protocol):
    pass
