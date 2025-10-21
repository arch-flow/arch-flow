import typer
import click
from rich.console import Console
from apps.cli.commands import register_commands

console = Console()

def _print_custom_help() -> None:
    console.print("[bold cyan]Arch-Flow CLI[/bold cyan]")
    console.print("Manage and execute your flows easily.\n")
    console.print("Usage:")
    console.print("  flow [COMMAND] [OPTIONS]\n")
    console.print("Commands:")
    console.print("  help        Show help for flow commands.")
    console.print("  list        List all registered flows.")
    console.print("  doctor      Run environment checks.")
    console.print("  <name>         Execute a specific flow by name.")

app = typer.Typer(
    add_completion=False,
    add_help_option=False,
    no_args_is_help=False,
    help="",
)

@app.callback(invoke_without_command=True)
def root(
    ctx: typer.Context,
    help_: bool = typer.Option(False, "--help", "-h", is_eager=True, help="Show this message and exit."),
):
    if help_ or ctx.invoked_subcommand is None:
        _print_custom_help()
        raise typer.Exit()

register_commands(app)

def main() -> None:
    try:
        app(standalone_mode=False)
    except click.UsageError as e:
        message = getattr(e, "message", "")
        if "No such command" in message:
            parts = message.split("'")
            invalid_command = parts[1] if len(parts) > 1 else ""
            console.print(f"[red]Unknown command:[/red] '{invalid_command}'")
        elif message:
            console.print(f"[red]Invalid usage:[/red] {message}")
        else:
            console.print("[red]Unknown command or invalid usage[/red]")
        _print_custom_help()

if __name__ == "__main__":
    main()
