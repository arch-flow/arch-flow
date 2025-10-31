import subprocess
import shutil
from pathlib import Path
from uuid import UUID

class VenvEnvironmentService:
    @staticmethod
    def create(profile_id: UUID, name: str, python_version: str) -> None:
        safe_name = name.replace(" ", "_").lower()
        base_path = Path("data/profiles") / str(profile_id) / safe_name
        base_path.mkdir(parents=True, exist_ok=True)

        if not shutil.which("uv"):
            raise RuntimeError("uv command not found in PATH")

        try:
            subprocess.run(
                ["uv", "venv", str(base_path), "--python", python_version],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=60
            )
        except subprocess.TimeoutExpired:
            raise TimeoutError("Virtual environment creation timed out after 60 seconds via uv.")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                f"Failed to create virtual environment using uv:\n"
                f"Command: {' '.join(e.cmd)}\n"
                f"Exit Code: {e.returncode}\n"
                f"STDOUT: {e.stdout}\n"
                f"STDERR: {e.stderr}"
            ) from e

        print(f"[✓] Virtual environment created at {base_path} using uv")

    @staticmethod
    def delete(profile_id: UUID, name: str) -> None:
        safe_name = name.replace(" ", "_").lower()
        base_path = Path("data/profiles") / str(profile_id) / safe_name

        if not base_path.exists() or not base_path.is_dir():
            raise FileNotFoundError(f"Virtual environment not found at {base_path}")

        try:
            shutil.rmtree(base_path)
        except Exception as e:
            raise RuntimeError(f"Failed to delete virtual environment at {base_path}: {e}")

        print(f"[✓] Virtual environment deleted from {base_path}")
