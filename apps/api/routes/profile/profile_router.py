from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from uuid import UUID
from apps.infrastructure.database.sqlalchemy import get_session
from apps.modules.profile.application.dto.create_profile_dto import CreateProfileDTO
from apps.modules.profile.application.dto.list_profiles_dto import ListProfilesDTO
from apps.modules.profile.application.dto.update_profile_dto import UpdateProfileDTO
from apps.modules.profile.services.profile_service_factory import make_create_profile_use_case, \
    make_list_profiles_use_case, make_update_profile_use_case, make_get_profile_use_case, make_delete_profile_use_case

router = APIRouter(prefix="/profiles", tags=["Profiles"])

@router.post("/")
def create_profile(dto: CreateProfileDTO, session: Session = Depends(get_session)):
    use_case = make_create_profile_use_case(session)
    use_case.execute(dto)
    return {"message": "Profile created successfully"}

@router.get("/")
def list_profiles(offset: int = Query(0), limit: int = Query(10), session: Session = Depends(get_session)):
    dto = ListProfilesDTO(offset=offset, limit=limit)
    use_case = make_list_profiles_use_case(session)
    return use_case.execute(dto)

@router.get("/{profile_id}")
def get_profile(profile_id: UUID, session: Session = Depends(get_session)):
    use_case = make_get_profile_use_case(session)
    return use_case.execute(profile_id)

@router.put("/{profile_id}")
def update_profile(
    profile_id: UUID,
    dto: UpdateProfileDTO,
    session: Session = Depends(get_session)
):
    use_case = make_update_profile_use_case(session)
    use_case.execute(profile_id, dto)
    return {"message": "Profile updated successfully"}

@router.delete("/{profile_id}")
def delete_profile(profile_id: UUID, session: Session = Depends(get_session)):
    use_case = make_delete_profile_use_case(session)
    use_case.execute(profile_id)
    return {"message": "Profile deleted successfully"}


