import typer
from rich.console import Console

flow_app = typer.Typer(no_args_is_help=True, help="Manage and execute your flows.")
console = Console()
