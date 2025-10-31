from fastapi import FastAPI

from apps.api.exceptions.handlers import register_exception_handlers
from apps.core.config import get_config
from apps.core.logging import setup_logging
from apps.api.routes.health.health_router import router as health_router
from apps.api.routes.profile.profile_router import router as profile_router
from apps.api.routes.virtual_environment.virtual_environment_router import router as virtual_environment_router

def create_app() -> FastAPI:
    config = get_config()
    setup_logging()
    app = FastAPI(title=config.app_name, version=config.version)

    app.include_router(health_router)
    app.include_router(profile_router)
    app.include_router(virtual_environment_router)
    register_exception_handlers(app)
    return app
