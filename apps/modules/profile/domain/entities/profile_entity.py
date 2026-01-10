from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime, timezone

@dataclass
class ProfileEntity:
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    purpose: str = ""
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
