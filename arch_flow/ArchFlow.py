from abc import ABC, abstractmethod
from arch_flow.DirectoryCreator import DirectoryCreator
from arch_flow.DirectoryExplorer import DirectoryExplorer
from arch_flow.StringManipulator import StringManipulator
from arch_flow.utils.Filter import Filter
from arch_flow.output.OutputHandler import OutputHandler
import sys
import os
import json

filter = Filter()


class ArchFlow(ABC):
    def __init__(self):
        self.DirectoryCreator = DirectoryCreator()
        self.DirectoryExplorer = DirectoryExplorer()
        self.StringManipulator = StringManipulator()
        self.OutputHandler = OutputHandler()
        self.root_path = os.getcwd()

    @abstractmethod
    def functions_flow(self) -> dict:
        pass

    def create_file_based_in_template(self, file_destination, file_name, template_file_name, args=None):
        content = self.DirectoryExplorer.read_file_template(template_file_name)
        if args:
            content = self.StringManipulator.replace_args(content, args)
        content = self.StringManipulator.replace_tags(content)
        self.DirectoryCreator.create_file(file_destination, file_name, content)

    @staticmethod
    def handle_args():
        return sys.argv[1:]

    def handler_functions_flow(self, args, json_functions=None):
        combined_json_content = {}

        for json_root_path in json_functions:
            json_data = self.DirectoryExplorer.read_json_file(json_root_path)
            for key, value in json_data.items():
                if key in combined_json_content:
                    if isinstance(combined_json_content[key], list):
                        combined_json_content[key].append(value)
                    else:
                        combined_json_content[key] = [combined_json_content[key], value]
                else:
                    combined_json_content[key] = value
        self.handler_input_count(args, combined_json_content)
        self.handler_input(args, combined_json_content)

    def handler_input(self, args, json_content):
        if len(args) == 0:
            self.OutputHandler.information_message("Whoopsie-daisy! It seems like you forgot to provide a function. "
                                               "How about trying --help for some magic commands?")
            return None
        name_function = args[0]

        func = filter.find_key_in_dictionaries(json_content, name_function)
        if func is not None:
            steps_funcao = filter.find_key_in_dictionaries(func, 'steps')
            dictonary_functions = self.dictionary_of_standard_functions()
            self.execute_step(steps_funcao, args, dictonary_functions, json_content)
        else:
            self.OutputHandler.alert_message(f"function '{name_function}' is not valid, try another one or try --help ")

    def handler_input_count(self, args, json_content):
        name_function = args[0]
        func = filter.find_key_in_dictionaries(json_content, name_function)
        if func is not None:
            steps_funcao = filter.find_key_in_dictionaries(func, 'steps')
            dictonary_functions = self.dictionary_of_standard_functions()
            self.count_step(steps_funcao, args, dictonary_functions, json_content)

    def count_step(self, steps_function, args, dictonary_functions, functions_json):
        for dic in steps_function:
            for step in dic:
                args_function = filter.find_key_in_dictionaries(dic, step)
                function = filter.find_key_in_dictionaries(dictonary_functions, step)
                self.OutputHandler.qtde_messages +=1
                if function is None:
                    function = filter.find_key_in_dictionaries(functions_json, step)
                    steps_functions = filter.find_key_in_dictionaries(function, 'steps')
                    args_function_ = filter.find_key_in_dictionaries(dic, step)
                    args_mapped = filter.map_args(args_function_, args[0:], "args[")
                    self.count_step(steps_functions, args_mapped, dictonary_functions, functions_json)
                    break

    def execute_step(self, steps_function, args, dictonary_functions, functions_json):
        for dic in steps_function:
            for step in dic:
                args_function = filter.find_key_in_dictionaries(dic, step)
                function = filter.find_key_in_dictionaries(dictonary_functions, step)
                if function is None:
                    function = filter.find_key_in_dictionaries(functions_json, step)
                    steps_functions = filter.find_key_in_dictionaries(function, 'steps')
                    args_function_ = filter.find_key_in_dictionaries(dic, step)
                    args_mapped = filter.map_args(args_function_, args[0:], "args[")
                    self.execute_step(steps_functions, args_mapped, dictonary_functions, functions_json)
                    break
                try:
                    if args_function == "None":
                        function()
                    elif isinstance(args_function, list):
                        args_mapped = filter.map_args(args_function, args[0:])
                        function(*args_mapped)
                    else:
                        function(*args[1:])
                except TypeError as e:
                    self.OutputHandler.alert_message(f"Error calling the function: {e}")

    def dictionary_of_standard_functions(self):
        dictionary_directory_creator = self.DirectoryCreator.dictionary_of_standard_functions()
        dictionary_directory_explorer = self.DirectoryExplorer.dictionary_of_standard_functions()
        dictionary_string_manipulator = self.StringManipulator.dictionary_of_standard_functions()
        dictionary_output_handler = self.OutputHandler.dictionary_of_standard_functions()
        functions_flow = self.functions_flow()
        return {
                'functions_flow': functions_flow,
                'directory_creator': dictionary_directory_creator,
                'directory_explorer': dictionary_directory_explorer,
                'string_manipulator': dictionary_string_manipulator,
                'output_handler': dictionary_output_handler,
                'create_file_based_in_template': self.create_file_based_in_template
                }

