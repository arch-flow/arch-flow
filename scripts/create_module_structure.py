import os
import sys
from pathlib import Path


def to_snake_case(name: str) -> str:
    result = ""
    for c in name:
        if c.isupper():
            result += "_" + c.lower()
        else:
            result += c
    return result.lstrip("_")


def create_file(path: Path, content: str = ""):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(content)


def main():
    if len(sys.argv) < 2:
        print("Usage: python create_module_structure.py <EntityName>")
        sys.exit(1)

    raw_name = sys.argv[1]
    snake_name = to_snake_case(raw_name)
    base_path = Path("apps/modules") / snake_name

    structure = {
        "application/dto": [
            (f"create_{snake_name}_dto.py", f"class Create{raw_name}DTO:\n    pass\n"),
            (f"list_{snake_name}_dto.py", f"class List{raw_name}DTO:\n    pass\n"),
            (f"update_{snake_name}_dto.py", f"class Update{raw_name}DTO:\n    pass\n"),
            (f"output_{snake_name}_dto.py", f"class {raw_name}OutputDTO:\n    pass\n"),
        ],
        "application/use_cases": [
            (f"create_{snake_name}_use_case.py", f"class Create{raw_name}UseCase:\n    pass\n"),
            (f"list_{snake_name}_use_case.py", f"class List{raw_name}UseCase:\n    pass\n"),
            (f"get_{snake_name}_use_case.py", f"class Get{raw_name}UseCase:\n    pass\n"),
            (f"update_{snake_name}_use_case.py", f"class Update{raw_name}UseCase:\n    pass\n"),
            (f"delete_{snake_name}_use_case.py", f"class Delete{raw_name}UseCase:\n    pass\n"),
        ],
        "domain/entities": [
            (f"{snake_name}_entity.py", f"class {raw_name}Entity:\n    pass\n"),
        ],
        "domain/repositories": [
            (f"{snake_name}_repository_interface.py", f"class {raw_name}RepositoryInterface:\n    pass\n"),
        ],
        "infrastructure/models": [
            (f"{snake_name}_model.py", f"class {raw_name}Model:\n    pass\n"),
        ],
        "infrastructure/repositories": [
            (f"{snake_name}_repository.py", f"class {raw_name}Repository:\n    pass\n"),
        ],
        "services": [
            (f"{snake_name}_service_factory.py", f"class {raw_name}ServiceFactory:\n    pass\n"),
        ],
    }

    for folder, files in structure.items():
        for filename, content in files:
            create_file(base_path / folder / filename, content)

    for root, dirs, _ in os.walk(base_path):
        for d in dirs:
            init_file = Path(root) / d / "__init__.py"
            init_file.touch()


if __name__ == "__main__":
    main()
