from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from apps.infrastructure.database.db_config import get_session
from apps.modules.dependency.application.dto.create_dependency_dto import CreateDependencyDTO
from apps.modules.dependency.application.dto.output_dependency_dto import DependencyOutputDTO
from apps.modules.dependency.application.dto.update_dependency_dto import UpdateDependencyDTO
from apps.modules.dependency.services.dependency_service_factory import (
    make_create_dependency_use_case,
    make_list_dependencies_use_case, make_get_dependency_use_case, make_update_dependency_use_case,
    make_delete_dependency_use_case,
)

router = APIRouter(prefix="/dependencies", tags=["Dependencies"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=DependencyOutputDTO)
def create_dependency(dto: CreateDependencyDTO, session: Session = Depends(get_session)):
    use_case = make_create_dependency_use_case(session)
    dependency_created = use_case.execute(dto)
    return DependencyOutputDTO.from_entity(dependency_created)


@router.get("/{environment_id}/full", response_model=dict)
def list_dependencies_full(environment_id: UUID, session: Session = Depends(get_session)):
    use_case = make_list_dependencies_use_case(session)
    return use_case.execute(environment_id)


@router.get("/{dependency_id}", response_model=DependencyOutputDTO)
def get_dependency(dependency_id: UUID, session: Session = Depends(get_session)):
    use_case = make_get_dependency_use_case(session)
    dependency = use_case.execute(dependency_id)
    return DependencyOutputDTO.from_entity(dependency)


@router.put("/{dependency_id}", response_model=DependencyOutputDTO)
def update_dependency(
        dependency_id: UUID,
        dto: UpdateDependencyDTO,
        session: Session = Depends(get_session)
):
    use_case = make_update_dependency_use_case(session)
    updated = use_case.execute(dependency_id, dto)
    return DependencyOutputDTO.from_entity(updated)


@router.delete("/{dependency_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dependency(dependency_id: UUID, session: Session = Depends(get_session)):
    use_case = make_delete_dependency_use_case(session)
    use_case.execute(dependency_id)
    return None
