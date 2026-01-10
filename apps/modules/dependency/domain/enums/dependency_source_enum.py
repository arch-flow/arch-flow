from enum import Enum


class DependencySourceEnum(Enum):
    VENV = "venv"
    PIPENV = "pipenv"
    POETRY = "poetry"
    CONDA = "conda"
