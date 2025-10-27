import click
import typer
from .context import AppContext
from .help_renderer import HelpRenderer


def build_app(ctx_data: AppContext, help_renderer: HelpRenderer) -> typer.Typer:
    app = typer.Typer(
        add_completion=False,
        add_help_option=False,
        no_args_is_help=False,
        help="",
    )

    @app.callback(invoke_without_command=True)
    def root(
        ctx: typer.Context,
        help_: bool = typer.Option(False, "-help", "-h", is_eager=True, help="Show this message and exit."),
    ) -> None:
        ctx.obj = ctx_data
        if help_:
            help_renderer.print_root()
            raise typer.Exit()
        if ctx.invoked_subcommand is None:
            raise click.UsageError("Missing command")

    return app
