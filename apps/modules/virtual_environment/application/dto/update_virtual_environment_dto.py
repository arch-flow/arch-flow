from dataclasses import dataclass

from apps.modules.virtual_environment.domain.enums.environment_manager import EnvironmentManager
from apps.modules.virtual_environment.domain.enums.python_version import PythonVersion


@dataclass(frozen=True)
class UpdateVirtualEnvironmentDTO:
    name: str
    manager: EnvironmentManager
    python_version: PythonVersion
    active: bool
