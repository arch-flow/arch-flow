from typing import Protocol, List, Optional
from app.domain.entities.flow import Flow

class FlowRepository(Protocol):
    def create(self, flow: Flow) -> Flow:
        ...
    def get_by_alias(self, alias: str) -> Optional[Flow]:
        ...
    def list_all(self) -> List[Flow]:
        ...
