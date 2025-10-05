from typing import Protocol, List, Optional
from app.domain.entities.profile import Profile

class ProfileRepository(Protocol):
    def create(self, profile: Profile) -> Profile:
        ...
    def get_by_name(self, name: str) -> Optional[Profile]:
        ...
    def list_all(self) -> List[Profile]:
        ...
