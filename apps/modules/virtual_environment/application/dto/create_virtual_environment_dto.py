from dataclasses import dataclass
from uuid import UUID

from apps.modules.virtual_environment.domain.enums.environment_manager_enum import EnvironmentManagerEnum
from apps.modules.virtual_environment.domain.enums.python_version_enum import PythonVersionEnum


@dataclass(frozen=True)
class CreateVirtualEnvironmentDTO:
    profile_id: UUID
    name: str
    manager: EnvironmentManagerEnum
    python_version: PythonVersionEnum
