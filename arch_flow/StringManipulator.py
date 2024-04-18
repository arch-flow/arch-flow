import os.path

from arch_flow.implementations.StringManipulatorImplementation import StringManipulatorImplementation


class StringManipulator:
    def __init__(self, tag_functions_user=None):
        self.implementation = StringManipulatorImplementation
        self.tag_functions_user = tag_functions_user

    def to_pascal_case(self, StringInput):
        return self.implementation.to_pascal_case(StringInput)

    def to_camel_case(self, stringInput):
        return self.implementation.to_camel_case(stringInput)

    def to_snake_case(self, string_input):
        return self.implementation.to_snake_case(string_input)

    def to_kebab_case(self, string_input):
        return self.implementation.to_kebab_case(string_input)

    def to_flat_case(self, stringinput):
        return self.implementation.to_flat_case(stringinput)

    def to_upper_flat_case(self, STRINGINPUT):
        return self.implementation.to_upper_flat_case(STRINGINPUT)

    def to_pascal_snake_case(self, String_Input):
        return self.implementation.to_pascal_snake_case(String_Input)

    def to_camel_snake_case(self, string_Input):
        return self.implementation.to_camel_snake_case(string_Input)

    def to_screaming_snake_case(self, STRING_INPUT):
        return self.implementation.to_screaming_snake_case(STRING_INPUT)

    def to_train_case(self, String_Input):
        return self.implementation.to_train_case(String_Input)

    def to_cobol_case(self, STRING_INPUT):
        return self.implementation.to_cobol_case(STRING_INPUT)

    def to_packeage_case(self, string_input):
        return self.implementation.to_packeage_case(string_input)

    def replace_tags(self, input_string):
        return self.implementation().replace_tags(input_string, self.tag_functions_user)

    @staticmethod
    def prepare_path(input_string):
        path = input_string.replace("\\", "/")
        path = os.path.join(*path.split("/"))
        return path

    @staticmethod
    def replace_args(text, args):
        for i, arg in enumerate(args):
            placeholder = f'args[{i}]'
            if placeholder in text:
                text = text.replace(placeholder, str(arg))
        return text

    def dictionary_of_standard_functions(self):
        return {'to_pascal_case': self.to_pascal_case,
                'to_camel_case': self.to_camel_case,
                'to_snake_case': self.to_snake_case,
                'to_kebab_case': self.to_kebab_case,
                'to_flat_case': self.to_flat_case,
                'to_upper_flat_case': self.to_upper_flat_case,
                'to_pascal_snake_case': self.to_pascal_snake_case,
                'to_camel_snake_case': self.to_camel_snake_case,
                'to_screaming_snake_case': self.to_screaming_snake_case,
                'to_train_case': self.to_train_case,
                'to_cobol_case': self.to_cobol_case,
                'to_packeage_case': self.to_packeage_case,
                'replace_tags': self.replace_tags,
                'path': self.prepare_path
                }
