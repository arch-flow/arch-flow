import os
from core.entities.implementations.DirectoryExplorerImplementation import DirectoryExplorerImplementation


class DirectoryExplorer:
    def __init__(self, directory=None):
        self.implementation = DirectoryExplorerImplementation()
        self.directory = directory
        if directory is None:
            self.directory = os.getcwd()

    def set_directory(self, directory):
        self.directory = directory

    def get_directory(self):
        return self.directory

    def list_files(self, extension=None):
        return self.implementation.list_files(self.directory, extension)

    def list_folders(self, folder=None):
        return self.implementation.list_folders(self.directory, folder)

    def find_only_file(self, file, directory=None):
        if directory is None:
            directory = os.getcwd()
        return self.implementation.find_only_file(directory, file)

    def find_only_folder(self, folder):
        return self.implementation.find_only_folder(self.directory, folder)

    def find_files_ignoring_this_folder(self, file, folder):
        return self.implementation.find_files_ignoring_this_folder(self.directory, file, folder)

    def find_folders_ignoring_this_folder(self, folder, folder_to_ignore):
        return self.implementation.find_folders_ignoring_this_folder(self.directory, folder, folder_to_ignore)

    def read_file(self, file_path, required=False):
        return self.implementation.read_file(file_path, required)
