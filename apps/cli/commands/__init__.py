from typer import Typer
from .doctor import register as register_doctor

def register_commands(app: Typer) -> None:
    register_doctor(app)