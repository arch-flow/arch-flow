from rich.console import Console
from apps.cli.context import AppContext
from apps.cli.help_renderer import HelpRenderer
from apps.cli.error_handler import CliErrorHandler
from apps.cli.app import build_app
from apps.cli.registry import register_all
from apps.cli.runner import run


console = Console()
ctx_data = AppContext(console=console)
help_renderer = HelpRenderer(console)
handler = CliErrorHandler(help_renderer)
app = build_app(ctx_data, help_renderer)
register_all(app)


def main() -> None:
    run(app, handler)


if __name__ == "__main__":
    main()
