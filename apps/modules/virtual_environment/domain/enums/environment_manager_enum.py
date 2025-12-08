from enum import Enum


class EnvironmentManagerEnum(Enum):
    VENV = "venv"
    PIPENV = "pipenv"
    POETRY = "poetry"
    CONDA = "conda"
