from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID

from apps.modules.dependency.domain.enums.dependency_source_enum import DependencySourceEnum


@dataclass(frozen=True)
class DependencyEntity:
    id: UUID
    environment_id: UUID
    name: str
    version: str
    source: DependencySourceEnum
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
