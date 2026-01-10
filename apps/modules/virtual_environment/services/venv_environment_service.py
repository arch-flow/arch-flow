import logging
import shutil
import subprocess
from pathlib import Path
from uuid import UUID

logger = logging.getLogger('venv-service')


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
            logger.error("Timeout while creating virtual environment at %s", base_path)
            raise TimeoutError("Virtual environment creation timed out after 60 seconds via uv.")
        except subprocess.CalledProcessError as e:
            logger.error(
                "Failed to create virtual environment. Command: %s | Exit Code: %s | STDOUT: %s | STDERR: %s",
                " ".join(e.cmd),
                e.returncode,
                e.stdout,
                e.stderr
            )
            raise RuntimeError(
                f"Failed to create virtual environment using uv:\n"
                f"Command: {' '.join(e.cmd)}\n"
                f"Exit Code: {e.returncode}\n"
                f"STDOUT: {e.stdout}\n"
                f"STDERR: {e.stderr}"
            ) from e

        logger.info("Virtual environment created at %s using uv", base_path)

    @staticmethod
    def delete(profile_id: UUID, name: str) -> None:
        safe_name = name.replace(" ", "_").lower()
        base_path = Path("data/profiles") / str(profile_id) / safe_name

        if not base_path.exists() or not base_path.is_dir():
            raise FileNotFoundError(f"Virtual environment not found at {base_path}")

        try:
            shutil.rmtree(base_path)
        except Exception as e:
            logger.error("Failed to delete virtual environment at %s: %s", base_path, e)
            raise RuntimeError(f"Failed to delete virtual environment at {base_path}: {e}")

        logger.info("Virtual environment deleted from %s", base_path)

    @staticmethod
    def rename(profile_id: UUID, old_name: str, new_name: str) -> None:
        old_safe_name = old_name.replace(" ", "_").lower()
        new_safe_name = new_name.replace(" ", "_").lower()

        base_path = Path("data/profiles") / str(profile_id)
        old_path = base_path / old_safe_name
        new_path = base_path / new_safe_name

        if not old_path.exists() or not old_path.is_dir():
            raise FileNotFoundError(f"Virtual environment not found at {old_path}")

        if new_path.exists():
            raise FileExistsError(f"A virtual environment with the name '{new_safe_name}' already exists at {new_path}")

        try:
            old_path.rename(new_path)
        except Exception as e:
            logger.error("Failed to rename virtual environment from %s to %s: %s", old_path, new_path, e)
            raise RuntimeError(f"Failed to rename virtual environment from {old_path} to {new_path}: {e}")

        logger.info("Virtual environment renamed from %s to %s", old_safe_name, new_safe_name)
