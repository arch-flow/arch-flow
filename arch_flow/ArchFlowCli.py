from .ArchFlow import ArchFlow


class ArchFlowCli(ArchFlow):

    @staticmethod
    def version():
        print("ArchFlow version is 0.1.7.4")

    def functions_flow(self) -> dict:
        return {
            "version": self.version
        }
