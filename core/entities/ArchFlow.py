from abc import ABC, abstractmethod
from core.entities.DirectoryCreator import DirectoryCreator
from core.entities.DirectoryExplorer import DirectoryExplorer
from core.entities.StringManipulator import StringManipulator
from core.entities.output.OutputHandler import OutputHandler


class ArchFlow(ABC):
    def __init__(self):
        self.DirectoryCreator = DirectoryCreator()
        self.DirectoryExplorer = DirectoryExplorer()
        self.StringManipulator = StringManipulator()
        self.OutputHandler = OutputHandler()

    @abstractmethod
    def create_project(self, *args):
        pass

    @abstractmethod
    def functions_flow(self):
        pass
