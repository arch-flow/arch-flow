from rich.console import Console


class HelpRenderer:
    def __init__(self, console: Console):
        self.console = console

    def print_root(self) -> None:
        c = self.console
        c.print("[green cyan]Arch-Flow CLI[/green cyan]")
        c.print("Manage and execute your flows easily.\n")
        c.print("Usage:")
        c.print("  flow [COMMAND] [OPTIONS]\n")
        c.print("Commands:")
        c.print("  help        Show help for flow commands.")
        c.print("  list        List all registered flows.")
        c.print("  doctor      Run environment checks.")
        c.print("  <name>      Execute a specific flow by name.")

    def show_no_command(self) -> None:
        self.console.print("[yellow]No command provided.[/yellow]")
        self.console.print("Use [green cyan]flow --help[/green cyan] to see available commands.\n")

    def show_unknown_command(self, invalid_command: str) -> None:
        self.console.print(f"Unknown command: [red]'{invalid_command}'[/red]")
        self.console.print("Use [green cyan]flow --help[/green cyan] to see available commands.\n")

    def show_invalid_usage(self, message: str) -> None:
        self.console.print(f"Invalid usage: [red]'{message}'[/red]")
        self.console.print("Use [green cyan]flow --help[/green cyan] to see valid command formats.\n")

    def show_interrupt(self) -> None:
        self.console.print("[yellow]Interrupted by user.[/yellow]")

    def show_unexpected(self, message: str) -> None:
        self.console.print(f"[red]Unexpected error:[/red] {message}")
