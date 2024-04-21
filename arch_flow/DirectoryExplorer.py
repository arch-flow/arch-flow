import os
from arch_flow.implementations.DirectoryExplorerImplementation import DirectoryExplorerImplementation


class DirectoryExplorer:
    def __init__(self, directory=None, directory_template=None):
        self.implementation = DirectoryExplorerImplementation()
        self.directory = directory
        self.directory_template = directory_template
        if directory is None:
            self.directory = os.getcwd()

    def set_directory(self, directory):
        self.directory = directory

    def get_directory(self):
        return self.directory

    def list_files(self, extension=None, directory=None):
        if not directory:
            directory = self.directory
        return self.implementation.list_files(directory, extension)

    def list_folders(self, folder=None):
        return self.implementation.list_folders(self.directory, folder)

    def find_only_one_file(self, file, directory=None):
        if directory is None:
            directory = os.getcwd()
        return self.implementation.find_only_one_file(directory, file)

    def find_only_one_folder(self, folder):
        return self.implementation.find_only_one_folder(self.directory, folder)

    def find_files_ignoring_this_folder(self, file, folder):
        return self.implementation.find_files_ignoring_this_folder(self.directory, file, folder)

    def find_folders_ignoring_this_folder(self, folder, folder_to_ignore):
        return self.implementation.find_folders_ignoring_this_folder(self.directory, folder, folder_to_ignore)

    def read_file(self, file_path, required=False):
        return self.implementation.read_file(file_path, required)

    def change_folder(self, path_folder):
        return self.implementation.change_folder(path_folder, self.directory)

    def return_root_path(self):
        return self.implementation.return_root_path(self.directory)

    def read_file_template(self, path_relative, required=False):
        return self.implementation.read_file_template(path_relative,self.directory_template, required)

    def change_folder_partial_match(self, partial_name, folder_to_ignore=None):
        return self.implementation.change_folder_partial_match(partial_name, os.getcwd(), folder_to_ignore)

    def read_json_file(self, root_path_json):
        return self.implementation.read_json_file(root_path_json)

    def dictionary_of_standard_functions(self):
        return {'set_directory': self.set_directory,
                'get_directory': self.get_directory,
                'list_files': self.list_files,

                'list_folders': self.list_folders,
                'find_only_one_file': self.find_only_one_file,
                'find_only_one_folder': self.find_only_one_folder,

                'find_files_ignoring_this_folder': self.find_files_ignoring_this_folder,
                'find_folders_ignoring_this_folder': self.find_folders_ignoring_this_folder,
                'read_file': self.list_files,
                'read_json_file': self.read_json_file,

                'change_folder': self.change_folder,
                'return_root_path': self.return_root_path,
                'change_folder_partial_match': self.change_folder_partial_match
                }
