import logging
import subprocess
from pathlib import Path
from uuid import UUID

logger = logging.getLogger("dependency-package-service")


class DependencyPackageService:
    @staticmethod
    def install(profile_id: UUID, environment_name: str, package: str, version: str | None) -> None:
        DependencyPackageService._run(
            profile_id,
            environment_name,
            DependencyPackageService._format_package(package, version)
        )

    @staticmethod
    def update(profile_id: UUID, environment_name: str, package: str, version: str | None) -> None:
        DependencyPackageService._run(
            profile_id,
            environment_name,
            DependencyPackageService._format_package(package, version)
        )

    @staticmethod
    def uninstall(profile_id: UUID, environment_name: str, package: str) -> None:
        DependencyPackageService._run(
            profile_id,
            environment_name,
            package,
            uninstall=True
        )

    @staticmethod
    def _format_package(package: str, version: str | None) -> str:
        return package if version is None else f"{package}=={version}"

    @staticmethod
    def _run(profile_id: UUID, environment_name: str, package: str, uninstall: bool = False) -> None:
        safe_name = environment_name.replace(" ", "_").lower()
        base_path = Path("data/profiles") / str(profile_id) / safe_name
        python_path = base_path / "bin" / "python"

        if not python_path.exists():
            raise FileNotFoundError(f"Python executable not found at: {python_path}")

        command = (
            ["uv", "pip", "uninstall", package, "--python", str(python_path)]
            if uninstall
            else ["uv", "pip", "install", package, "--python", str(python_path)]
        )

        try:
            subprocess.run(
                command,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
        except subprocess.CalledProcessError as e:
            stderr = e.stderr.lower() if e.stderr else ""

            if uninstall and ("not installed" in stderr or "no versions of" in stderr):
                logger.info("Dependency %s is already uninstalled. Skipping.", package)
                return

            logger.error("Command failed: %s", command)
            logger.error("STDOUT: %s", e.stdout)
            logger.error("STDERR: %s", e.stderr)
            raise RuntimeError("Dependency operation failed") from e

        logger.info("Dependency %s processed successfully in %s", package, base_path)
