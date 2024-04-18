from colorama import init, Fore, Style
import time
import random

init(autoreset=True)  # config  only for windows


class OutputHandler:
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
        OutputHandler.random_pause()
        return f"{top_line}\n{formatted_message}\n{bottom_line}"

    @staticmethod
    def success_message(message):
        print(OutputHandler.format_message("[📟success📟]", message, color_type=Fore.GREEN, identification=5))

    @staticmethod
    def information_message(message):
        print(OutputHandler.format_message("[information]", message, color_type=Fore.LIGHTBLACK_EX, identification=3))

    @staticmethod
    def alert_message(message):
        print(OutputHandler.format_message("[alert message️]", message, color_type=Fore.YELLOW, identification=1))

    @staticmethod
    def random_pause(min_interval=0.1, max_interval=1.0):
        pause_time = random.uniform(min_interval, max_interval)
        time.sleep(pause_time)

    def dictionary_of_standard_functions(self):
        return {'format_message': self.format_message,
                'success_message': self.success_message,
                'information_message': self.information_message,
                'alert_message': self.alert_message
                }
