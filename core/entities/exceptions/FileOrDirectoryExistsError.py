import sys

from colorama import Fore
from core.entities.exceptions.ExceptionHandler import ExceptionHandler


class FileOrDirectoryExistsError:

    @staticmethod
    def already_exists_error(message):
        try:
            raise ExceptionHandler("[☢️ already exists ☢️]️️", message, color_type=Fore.YELLOW, color_text=Fore.YELLOW)
        except ExceptionHandler as e:
            print(e)

    @staticmethod
    def alert_error(message):
        try:
            raise ExceptionHandler("[☢️ alert error ☢️️️]", message, color_type=Fore.YELLOW, color_text=Fore.YELLOW)
        except ExceptionHandler as e:
            print(e)

    @staticmethod
    def fatal_already_exists_error(message):
        try:
            raise ExceptionHandler("[⁉️ FATAL ERROR ⁉️]", message, color_type=Fore.RED)
        except ExceptionHandler as e:
            print(e)
            sys.exit(404)

    @staticmethod
    def fatal_error(message):
        try:
            raise ExceptionHandler("[⁉️ FATAL ERROR ⁉️]", message, color_type=Fore.RED)
        except ExceptionHandler as e:
            print(e)
            sys.exit(404)