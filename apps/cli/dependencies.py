from rich.console import Console

_console = None

def get_console() -> Console:
    global _console
    if _console is None:
        _console = Console()
    return _console