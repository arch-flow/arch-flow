from dataclasses import dataclass


@dataclass(frozen=True)
class ListDependencyDTO:
    offset: int
    limit: int
