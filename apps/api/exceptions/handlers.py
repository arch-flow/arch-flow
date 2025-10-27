from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

from apps.shared.exceptions.entity_not_found_exception import EntityNotFoundException


def register_exception_handlers(app):
    @app.exception_handler(EntityNotFoundException)
    async def handle_entity_not_found_exception(request: Request, exc: EntityNotFoundException):
        return JSONResponse(
            status_code=HTTP_404_NOT_FOUND,
            content={"detail": exc.message},
        )

    @app.exception_handler(Exception)
    async def handle_generic_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "Internal server error"},
        )
