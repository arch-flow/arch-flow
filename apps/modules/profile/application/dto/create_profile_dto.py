from dataclasses import dataclass

@dataclass
class CreateProfileDTO:
    name: str
    purpose: str
