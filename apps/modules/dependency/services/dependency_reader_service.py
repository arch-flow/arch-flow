import json
import logging
import subprocess
from pathlib import Path
from uuid import UUID

logger = logging.getLogger("dependency-reader-service")


class DependencyReaderService:
    @staticmethod
    def list_installed(profile_id: UUID, environment_name: str) -> list[dict]:
        safe_env = environment_name.replace(" ", "_").lower()
        base_path = Path("data/profiles") / str(profile_id) / safe_env

        python_path = base_path / "bin" / "python"
        if not python_path.exists():
            raise FileNotFoundError(f"Python executable not found at: {python_path}")

        try:
            result = subprocess.run(
                ["uv", "pip", "list", "--format=json", "--python", str(python_path)],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
        except subprocess.CalledProcessError as e:
            logger.error(
                "Failed to list dependencies. STDOUT: %s | STDERR: %s",
                e.stdout,
                e.stderr
            )
            raise RuntimeError("Failed to list installed dependencies") from e

        return json.loads(result.stdout)
