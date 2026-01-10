from dataclasses import dataclass


@dataclass(frozen=True)
class ListVirtualEnvironmentsDTO:
    offset: int
    limit: int
