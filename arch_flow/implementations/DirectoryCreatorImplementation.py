import os.path
from arch_flow.exceptions.FileOrDirectoryExistsError import FileOrDirectoryExistsError
from arch_flow.output.OutputHandler import OutputHandler
from arch_flow.exceptions.NotFoundException import NotFoundException
from arch_flow.StringManipulator import StringManipulator

exception_file_exists = FileOrDirectoryExistsError()
exception_not_found = NotFoundException()
output = OutputHandler()


class DirectoryCreatorImplementation:
    @staticmethod
    def does_file_or_directory_exist(path):
        return os.path.exists(path)

    @staticmethod
    def create_folder(folder_path):
        folder_path = StringManipulator().prepare_path(folder_path)
        try:
            os.makedirs(folder_path)
            output.success_message(f"folder '{folder_path}' created successfully")
        except FileExistsError:
            exception_file_exists.already_exists_error(f"the folder '{folder_path}' already exists")
        except Exception as e:
            exception_file_exists.fatal_error(f"error creating folder '{folder_path}' exception: {e}")

    def create_file(self, path, file_name, file_content, required=False):
        path = StringManipulator().prepare_path(path)
        if not self.does_file_or_directory_exist(path):
            if required:
                exception_not_found.fatal_not_found_error(f"path '{path}' does not exist. Could not create file "
                                                          f"'{file_name}' and this file was required")
            exception_not_found.not_found_error(f"path '{path}' does not exist. error creating the file '{file_name}'")
            return None
        try:
            file_path = path + file_name
            with open(file_path, 'w') as file:
                file.write(file_content)
            output.success_message(f"file '{file_name}' created successfully. file path '{file_path}'")
        except Exception as e:
            if required:
                exception_file_exists.fatal_error(f"error creating the file '{file_name}', error '{e}'")
            exception_file_exists.alert_error(f"error creating the file '{file_name}', error '{e}'")
