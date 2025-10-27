from dataclasses import dataclass

@dataclass
class ListProfilesDTO:
    offset: int
    limit: int
