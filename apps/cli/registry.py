from typer import Typer
from .commands.doctor import register as register_doctor


def register_all(app: Typer) -> None:
    register_doctor(app)
