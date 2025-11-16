from uuid import UUID

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from apps.infrastructure.database.db_config import get_session
from apps.modules.virtual_environment.application.dto.create_virtual_environment_dto import CreateVirtualEnvironmentDTO
from apps.modules.virtual_environment.application.dto.list_virtual_environments_dto import ListVirtualEnvironmentsDTO
from apps.modules.virtual_environment.application.dto.update_virtual_environment_dto import UpdateVirtualEnvironmentDTO
from apps.modules.virtual_environment.application.dto.virtual_environment_response_dto import \
    VirtualEnvironmentResponseDTO
from apps.modules.virtual_environment.services.virtual_environment_service_factory import (
    make_create_virtual_environment_use_case,
    make_list_virtual_environments_use_case,
    make_get_virtual_environment_use_case,
    make_update_virtual_environment_use_case,
    make_delete_virtual_environment_use_case
)

router = APIRouter(prefix="/virtual-environments", tags=["Virtual Environments"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=VirtualEnvironmentResponseDTO)
def create_virtual_environment(dto: CreateVirtualEnvironmentDTO, session: Session = Depends(get_session)):
    use_case = make_create_virtual_environment_use_case(session)
    virtual_created = use_case.execute(dto)
    return VirtualEnvironmentResponseDTO.from_entity(virtual_created)


@router.get("/", response_model=list[VirtualEnvironmentResponseDTO])
def list_virtual_environments(offset: int = Query(0), limit: int = Query(10), session: Session = Depends(get_session)):
    dto = ListVirtualEnvironmentsDTO(offset=offset, limit=limit)
    use_case = make_list_virtual_environments_use_case(session)
    virtual_environments = use_case.execute(dto)
    return [VirtualEnvironmentResponseDTO.from_entity(environment) for environment in virtual_environments]


@router.get("/{environment_id}", response_model=VirtualEnvironmentResponseDTO)
def get_virtual_environment(environment_id: UUID, session: Session = Depends(get_session)):
    use_case = make_get_virtual_environment_use_case(session)
    virtual_environment = use_case.execute(environment_id)
    return VirtualEnvironmentResponseDTO.from_entity(virtual_environment)


@router.put("/{environment_id}", response_model=VirtualEnvironmentResponseDTO)
def update_virtual_environment(
        environment_id: UUID,
        dto: UpdateVirtualEnvironmentDTO,
        session: Session = Depends(get_session)
):
    use_case = make_update_virtual_environment_use_case(session)
    virtual_environment = use_case.execute(environment_id, dto)
    return VirtualEnvironmentResponseDTO.from_entity(virtual_environment)


@router.delete("/{environment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_virtual_environment(environment_id: UUID, session: Session = Depends(get_session)):
    use_case = make_delete_virtual_environment_use_case(session)
    use_case.execute(environment_id)
    return None
