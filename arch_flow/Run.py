import os

from .ArchFlowCli import ArchFlowCli


def main(roots_path_json=None):
    if roots_path_json is None:
        roots_path_json = []
    roots_path_json.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "db.json")))
    arch = ArchFlowCli()
    args = arch.handle_args()
    arch.handler_functions_flow(args, roots_path_json)

