from arch_flow.implementations.DirectoryCreatorImplementation import DirectoryCreatorImplementation


class DirectoryCreator:

    def __init__(self):
        self.implementation = DirectoryCreatorImplementation()

    def does_file_or_directory_exist(self, path):
        return self.implementation.does_file_or_directory_exist(path)

    def create_folder(self, folder_path):
        return self.implementation.create_folder(folder_path)

    def create_file(self, path, file_name, file_content, required=False):
        return self.implementation.create_file(path, file_name, file_content, required)

    def dictionary_of_standard_functions(self):
        return {'does_file_or_directory_exist': self.does_file_or_directory_exist,
                'create_folder': self.create_folder,
                'create_file': self.create_file,
                }
