from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from uuid import UUID
from apps.infrastructure.database.sqlalchemy import get_session
from apps.modules.virtual_environment.application.dto.create_virtual_environment_dto import CreateVirtualEnvironmentDTO
from apps.modules.virtual_environment.application.dto.update_virtual_environment_dto import UpdateVirtualEnvironmentDTO
from apps.modules.virtual_environment.application.dto.list_virtual_environments_dto import ListVirtualEnvironmentsDTO
from apps.modules.virtual_environment.services.virtual_environment_service_factory import (
    make_create_virtual_environment_use_case,
    make_list_virtual_environments_use_case,
    make_get_virtual_environment_use_case,
    make_update_virtual_environment_use_case,
    make_delete_virtual_environment_use_case
)

router = APIRouter(prefix="/virtual-environments", tags=["Virtual Environments"])


@router.post("/")
def create_virtual_environment(dto: CreateVirtualEnvironmentDTO, session: Session = Depends(get_session)):
    use_case = make_create_virtual_environment_use_case(session)
    use_case.execute(dto)
    return {"message": "Virtual environment created successfully"}


@router.get("/")
def list_virtual_environments(offset: int = Query(0), limit: int = Query(10), session: Session = Depends(get_session)):
    dto = ListVirtualEnvironmentsDTO(offset=offset, limit=limit)
    use_case = make_list_virtual_environments_use_case(session)
    return use_case.execute(dto)


@router.get("/{environment_id}")
def get_virtual_environment(environment_id: UUID, session: Session = Depends(get_session)):
    use_case = make_get_virtual_environment_use_case(session)
    return use_case.execute(environment_id)


@router.put("/{environment_id}")
def update_virtual_environment(
    environment_id: UUID,
    dto: UpdateVirtualEnvironmentDTO,
    session: Session = Depends(get_session)
):
    use_case = make_update_virtual_environment_use_case(session)
    use_case.execute(environment_id, dto)
    return {"message": "Virtual environment updated successfully"}


@router.delete("/{environment_id}")
def delete_virtual_environment(environment_id: UUID, session: Session = Depends(get_session)):
    use_case = make_delete_virtual_environment_use_case(session)
    use_case.execute(environment_id)
    return {"message": "Virtual environment deleted successfully"}
