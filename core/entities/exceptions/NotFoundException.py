import sys

from colorama import Fore

from core.entities.exceptions.ExceptionHandler import ExceptionHandler


class NotFoundException:
    @staticmethod
    def not_found_error(message):
        try:
            raise ExceptionHandler("[☢️ Not Found ☢️️]️", message, color_type=Fore.YELLOW, color_text=Fore.YELLOW)
        except ExceptionHandler as e:
            print(e)

    @staticmethod
    def fatal_not_found_error(message):
        try:
            raise ExceptionHandler("[⁉️ FATAL ERROR ⁉️]", message, color_type=Fore.RED)
        except ExceptionHandler as e:
            print(e)
            sys.exit(404)
