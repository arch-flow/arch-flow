import os
import sys
from pathlib import Path


def to_snake_case(name):
    return ''.join(['_' + c.lower() if c.isupper() else c for c in name]).lstrip('_')


def create_file(path, content=""):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(content)


def main():
    if len(sys.argv) < 2:
        print("Usage: python create_module_structure.py <EntityName>")
        sys.exit(1)

    raw_name = sys.argv[1]
    name_snake = to_snake_case(raw_name)
    base_path = Path("apps/modules") / name_snake

    structure = {
        "application/dto": [
            ("create_dto", f"class Create{raw_name}DTO:\n    pass\n"),
            ("update_dto", f"class Update{raw_name}DTO:\n    pass\n"),
            ("list_dto", f"class List{raw_name}DTO:\n    pass\n")
        ],
        "application/use_cases": [
            ("create_use_case", f"class Create{raw_name}UseCase:\n    pass\n"),
            ("update_use_case", f"class Update{raw_name}UseCase:\n    pass\n"),
            ("get_use_case", f"class Get{raw_name}UseCase:\n    pass\n"),
            ("delete_use_case", f"class Delete{raw_name}UseCase:\n    pass\n")
        ],
        "domain/entities": [
            ("entity", f"class {raw_name}Entity:\n    pass\n")
        ],
        "domain/repositories": [
            ("repository_interface", f"class {raw_name}RepositoryInterface:\n    pass\n")
        ],
        "infrastructure/models": [
            ("model", f"class {raw_name}Model:\n    pass\n")
        ],
        "infrastructure/repositories": [
            ("repository", f"class {raw_name}Repository:\n    pass\n")
        ],
        "services": [
            ("service_factory", f"class {raw_name}ServiceFactory:\n    pass\n")
        ]
    }

    for subdir, files in structure.items():
        for suffix, content in files:
            file_path = base_path / subdir / f"{name_snake}_{suffix}.py"
            create_file(file_path, content)

    for root, dirs, _ in os.walk(base_path):
        for d in dirs:
            init_path = Path(root) / d / "__init__.py"
            init_path.parent.mkdir(parents=True, exist_ok=True)
            init_path.touch()


if __name__ == "__main__":
    main()
