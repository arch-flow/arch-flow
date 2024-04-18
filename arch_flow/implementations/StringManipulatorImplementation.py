import re
import os

class StringManipulatorImplementation:
    @staticmethod
    def to_pascal_case(StringInput):
        words = StringManipulatorImplementation.split_string(StringInput)
        return ''.join(word.capitalize() for word in words)

    @staticmethod
    def to_camel_case(stringInput):
        words = StringManipulatorImplementation.split_string(stringInput)
        if not words:
            return ""
        return words[0].lower()+''.join(word.capitalize() for word in words[1:])

    @staticmethod
    def to_snake_case(string_input):
        words = StringManipulatorImplementation.split_string(string_input)
        return '_'.join(word.lower() for word in words)

    @staticmethod
    def to_kebab_case(string_input):
        words = StringManipulatorImplementation.split_string(string_input)
        return '-'.join(word.lower() for word in words)

    @staticmethod
    def to_flat_case(stringinput):
        words = StringManipulatorImplementation.split_string(stringinput)
        return ''.join(word.lower() for word in words)

    @staticmethod
    def to_upper_flat_case(STRINGINPUT):
        words = StringManipulatorImplementation.split_string(STRINGINPUT)
        return ''.join(word.upper() for word in words)

    @staticmethod
    def to_pascal_snake_case(String_Input):
        words = StringManipulatorImplementation.split_string(String_Input)
        return '_'.join(word.capitalize() for word in words)

    @staticmethod
    def to_camel_snake_case(string_Input):
        words = StringManipulatorImplementation.split_string(string_Input)
        if not words:
            return ""
        return words[0].lower()+"_".join(word.capitalize() for word in words[1:])
    
    @staticmethod
    def to_screaming_snake_case(STRING_INPUT):
        words = StringManipulatorImplementation.split_string(STRING_INPUT)
        return '_'.join(word.upper() for word in words)
    
    @staticmethod
    def to_train_case(String_Case):
        words = StringManipulatorImplementation.split_string(String_Case)
        return '-'.join(word.capitalize() for word in words)
    
    @staticmethod
    def to_cobol_case(STRING_CASE):
        words = StringManipulatorImplementation.split_string(STRING_CASE)
        return '-'.join(word.upper() for word in words)

    @staticmethod
    def to_packeage_case(string_input):
        words = StringManipulatorImplementation.split_string(string_input)
        return '.'.join(word.lower() for word in words)

    @staticmethod
    def prepare_path(input_string):
        path = os.path.join(*input_string.split("/"))
        path = os.path.join(*input_string.split("\\"))
        return path

    @staticmethod
    def split_string(input_string):
        def is_upper(string):
            return string.isupper()

        def split_camel_snake(string):
            return re.findall(r'[a-z0-9]+|[A-Z][a-z0-9]*', string)

        if isinstance(input_string, (list, tuple)):
            input_string = ''.join(word.replace('-', '_') for word in input_string)

        words = re.findall(r'[a-z0-9]+|[A-Z][a-z0-9]*', input_string)

        result = []
        for word in words:
            if is_upper(word):
                result.extend(split_camel_snake(word))
            else:
                result.append(word)
        return result

    def extract_tags(self, string):
        tag_pattern = re.compile(r'<(\w+)>(.*?)<\/\1>|<(\w+)>', re.DOTALL)

        found_tags = tag_pattern.findall(string)

        combined_tags = []

        for (opening, content, single) in found_tags:
            subs_tags = self.extract_tags(content)
            if opening:
                combined_tags.append((opening, content, f"<{opening}>{content}</{opening}>"))
            elif single:
                combined_tags.append((single, '', f"<{single}>"))

            combined_tags = subs_tags + combined_tags

        return combined_tags

    def replace_tags(self, input_string, tag_functions_user):
        tag_functions = self.dictionary_of_standard_string_manipulation_functions()
        tags_not_found = []
        if tag_functions_user is None:
            tag_functions_user = []
        while True:
            tags = self.extract_tags(input_string)
            tags = [item for item in tags if item not in tags_not_found]

            if not tags:
                break
            tag = tags[0]
            tag_name, tag_content = tag[0], tag[1]

            if tag_name in tag_functions:
                replacement = tag_functions[tag_name](tag_content)
                input_string = input_string.replace(tag[2], replacement)
            elif tag_name in tag_functions_user:
                replacement = tag_functions_user[tag_name](tag_content)
                input_string = input_string.replace(tag[2], replacement)
            else:
                tags_not_found.append(tag)

        return input_string

    def dictionary_of_standard_string_manipulation_functions(self):
        return {'PascalCase': self.to_pascal_case,
                'pascal_case': self.to_pascal_case,
                'pascalCase': self.to_pascal_case,
                'pc': self.to_pascal_case,
                'CamelCase': self.to_camel_case,
                'camel_case': self.to_camel_case,
                'camelCase': self.to_camel_case,
                'cc': self.to_camel_case,
                'SnakeCase': self.to_snake_case,
                'snake_case': self.to_snake_case,
                'snakeCase': self.to_snake_case,
                'sc': self.to_snake_case,
                'KebabCase': self.to_kebab_case,
                'kebab_case': self.to_kebab_case,
                'kebabCase': self.to_kebab_case,
                'kc': self.to_kebab_case,
                'FlatCase': self.to_flat_case,
                'flat_case': self.to_flat_case,
                'flatCase': self.to_flat_case,
                'fc': self.to_flat_case,
                'UpperFlatCase': self.to_upper_flat_case,
                'upper_flat_case': self.to_upper_flat_case,
                'upperFlatCase': self.to_upper_flat_case,
                'ufc': self.to_upper_flat_case,
                'PascalSnakeCase': self.to_pascal_snake_case,
                'pascal_snake_case': self.to_pascal_snake_case,
                'pascalSnakeCase': self.to_pascal_snake_case,
                'psc': self.to_pascal_snake_case,
                'CamelSnakeCase': self.to_camel_snake_case,
                'camel_snake_case': self.to_camel_snake_case,
                'camelSnakeCase': self.to_camel_snake_case,
                'ScreamingSnakeCase': self.to_screaming_snake_case,
                'screaming_snake_case': self.to_screaming_snake_case,
                'screamingSnakeCase': self.to_screaming_snake_case,
                'ssc': self.to_screaming_snake_case,
                'TrainCase': self.to_train_case,
                'train_case': self.to_train_case,
                'trainCase': self.to_train_case,
                'tc': self.to_train_case,
                'CobolCase': self.to_cobol_case,
                'cobol_case': self.to_cobol_case,
                'cobolCase': self.to_cobol_case,
                'coc': self.to_cobol_case,
                'PackeageCase': self.to_packeage_case,
                'packeageCase': self.to_packeage_case,
                'packeage_case': self.to_packeage_case,
                'pk': self.to_packeage_case,
                'path': self.prepare_path
                }
