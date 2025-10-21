import click
from .help_renderer import HelpRenderer


class CliErrorHandler:
    def __init__(self, help_renderer: HelpRenderer):
        self.help = help_renderer

    def handle(self, exc: Exception) -> None:
        if isinstance(exc, click.UsageError):
            text = getattr(exc, "message", "") or str(exc)
            if "Missing command" in text or "No command" in text:
                self.help.show_no_command()
                return
            if "No such command" in text:
                invalid = self._extract_invalid_command(text)
                self.help.show_unknown_command(invalid)
                return
            self.help.show_invalid_usage(text)
            return
        if isinstance(exc, click.ClickException):
            self.help.show_invalid_usage(str(exc))
            return
        if isinstance(exc, KeyboardInterrupt):
            self.help.show_interrupt()
            return
        self.help.show_unexpected(str(exc))

    def _extract_invalid_command(self, message: str) -> str:
        parts = message.split("'")
        return parts[1] if len(parts) > 1 else ""
