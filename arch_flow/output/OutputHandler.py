from colorama import init, Fore, Style
import time
import random
from rich.console import Console
from rich.live import Live
from rich.table import Table
import os
import shutil

init(autoreset=True)

console = Console()


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class OutputHandler(metaclass=SingletonMeta):
    messages = []

    def __init__(self):
        self.message_model = True
        self.messages_qtde = 0

    @staticmethod
    def format_message(type_message, message, color_type=Fore.RED, identification=2):
        character_limit = 100
        formatted_message = f"{color_type} {type_message}: {message} {Style.RESET_ALL}"

        if len(formatted_message) > character_limit:
            line_one = formatted_message[:character_limit]
            remaining_text = formatted_message[character_limit:]

            sentences = remaining_text.split('\n')
            cleaned_sentences = [sentence.lstrip() for sentence in sentences if sentence]
            remaining_text = '\n'.join(cleaned_sentences)

            available_length = character_limit - len(type_message) - identification - 5

            lines = [f"{' ' * (len(type_message) + identification)}{remaining_text[i:i + available_length]}" for i in
                     range(0, len(remaining_text), available_length)]
            formatted_message = line_one+"\n"+'\n'.join(lines)

        top_line = f"{color_type}{'-' * character_limit} {Style.RESET_ALL}"
        bottom_line = f"{color_type}{'-' * character_limit} {Style.RESET_ALL}"
        return f"{top_line}\n{formatted_message}\n{bottom_line}"

    def success_message(self, message):
        if self.message_model:
            status = "success"
            self.messages = self.generate_output(message, status, self.messages)
        else:
            print(OutputHandler.format_message("[📟success📟]", message, color_type=Fore.GREEN, identification=5))

    def information_message(self, message):
        if self.message_model:
            status = "infor"
            self.messages = self.generate_output(message, status, self.messages)
        else:
            print(OutputHandler.format_message("[information]", message, color_type=Fore.LIGHTBLACK_EX, identification=3))

    def alert_message(self, message):
        if self.message_model:
            status = "alert"
            self.messages = self.generate_output(message, status, self.messages)
        else:
            print(OutputHandler.format_message("[alert message️]", message, color_type=Fore.YELLOW, identification=1))

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def message_green(message):
        console.print(f"[bright_green]{message}[/bright_green]")

    @staticmethod
    def message_red(message):
        console.print(f"[bold red]{message}[/bold red]")

    @staticmethod
    def message_yellow(message):
        console.print(f"[bold yellow]{message}[/bold yellow]")

    def update_content(self, live, messages):
        terminal_size = shutil.get_terminal_size()
        table_width = terminal_size.columns
        max_message_length = max(len(message['message']) for message in messages)

        description_width = min(max_message_length, table_width - 30)

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Steps", style="dim", width=description_width)
        table.add_column("Status", width=10, justify="center")
        table.add_column("Step", justify="center", width=10)

        for step, message in enumerate(messages, start=1):
            table.add_row(message['message'], message['status'], f"{step}/{self.messages_qtde}")

        live.update(table)

    def generate_output(self, new_message, status, previous_messages):
        messages = previous_messages[:]
        new_message = {"message": new_message, "status": status}
        messages.append(new_message)
        with Live(console=console, refresh_per_second=4) as live:
            self.clear_screen()
            self.update_content(live, messages)
        return messages

    def dictionary_of_standard_functions(self):
        return {'format_message': self.format_message,
                'success_message': self.success_message,
                'information_message': self.information_message,
                'alert_message': self.alert_message
                }
