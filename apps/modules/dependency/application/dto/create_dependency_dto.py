from dataclasses import dataclass
from uuid import UUID

from apps.modules.dependency.domain.enums.dependency_source_enum import DependencySourceEnum


@dataclass(frozen=True)
class CreateDependencyDTO:
    environment_id: UUID
    name: str
    version: str
    source: DependencySourceEnum
