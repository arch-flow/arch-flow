from enum import Enum


class EnvironmentManager(Enum):
    VENV = "venv"
    PIPENV = "pipenv"
    POETRY = "poetry"
    CONDA = "conda"
