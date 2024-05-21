from core.entities.implementations.StringManipulatorImplementation import StringManipulatorImplementation


class StringManipulator:
    def __init__(self):
        self.implementation = StringManipulatorImplementation

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

    def replace_tags(self, input_string, tag_functions_user=None):
        return self.implementation().replace_tags(input_string, tag_functions_user)
