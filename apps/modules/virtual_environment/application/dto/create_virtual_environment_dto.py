from dataclasses import dataclass
import uuid

from apps.modules.virtual_environment.domain.enums.environment_manager import EnvironmentManager
from apps.modules.virtual_environment.domain.enums.python_version import PythonVersion


@dataclass(frozen=True)
class CreateVirtualEnvironmentDTO:
    profile_id: uuid.UUID
    name: str
    manager: EnvironmentManager
    python_version: PythonVersion
