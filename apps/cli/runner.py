import typer
from .error_handler import CliErrorHandler


def run(app: typer.Typer, handler: CliErrorHandler) -> None:
    try:
        app(standalone_mode=False)
    except Exception as exc:
        handler.handle(exc)
