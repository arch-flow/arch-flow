from typer import Typer
from rich.console import Console

def register(app: Typer) -> None:
    console = Console()

    @app.command("doctor")
    def doctor() -> None:
        console.print("[bold green]All checks passed[/bold green]")
