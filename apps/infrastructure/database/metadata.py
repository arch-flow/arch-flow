from apps.infrastructure.database.base import Base
from apps.modules.dependency.infrastructure.models.dependency_model import DependencyModel
from apps.modules.profile.infrastructure.models.profile_model import ProfileModel
from apps.modules.virtual_environment.infrastructure.models.virtual_environment_model import VirtualEnvironmentModel

__all__ = [
    "ProfileModel",
    "VirtualEnvironmentModel",
    "DependencyModel",
]

metadata = Base.metadata
