from colorama import init, Fore
from arch_flow.output.OutputHandler import OutputHandler
init(autoreset=True)  # config  only for windows


class ExceptionHandler(Exception):

    def __init__(self, type_error, message, color_type=Fore.RED, color_text=Fore.WHITE):
        super().__init__(message)
        self.type_error = type_error
        self.color_type = color_type
        self.color_text = color_text
        self.output = OutputHandler

    def __str__(self):
        return self.output.format_message(self.type_error, self.args[0], self.color_type, identification=1)
