from uuid import UUID

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from apps.infrastructure.database.db_config import get_session
from apps.modules.profile.application.dto.create_profile_dto import CreateProfileDTO
from apps.modules.profile.application.dto.list_profiles_dto import ListProfilesDTO
from apps.modules.profile.application.dto.profile_response_dto import ProfileResponseDTO
from apps.modules.profile.application.dto.update_profile_dto import UpdateProfileDTO
from apps.modules.profile.services.profile_service_factory import make_create_profile_use_case, \
    make_list_profiles_use_case, make_update_profile_use_case, make_get_profile_use_case, make_delete_profile_use_case

router = APIRouter(prefix="/profiles", tags=["Profiles"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProfileResponseDTO)
def create_profile(dto: CreateProfileDTO, session: Session = Depends(get_session)):
    use_case = make_create_profile_use_case(session)
    profile_created = use_case.execute(dto)
    return ProfileResponseDTO.from_entity(profile_created)


@router.get("/", response_model=list[ProfileResponseDTO])
def list_profiles(offset: int = Query(0), limit: int = Query(10), session: Session = Depends(get_session)):
    dto = ListProfilesDTO(offset=offset, limit=limit)
    use_case = make_list_profiles_use_case(session)
    profiles = use_case.execute(dto)
    return [ProfileResponseDTO.from_entity(profile) for profile in profiles]


@router.get("/{profile_id}", response_model=ProfileResponseDTO)
def get_profile(profile_id: UUID, session: Session = Depends(get_session)):
    use_case = make_get_profile_use_case(session)
    profile = use_case.execute(profile_id)
    return ProfileResponseDTO.from_entity(profile)


@router.put("/{profile_id}", response_model=ProfileResponseDTO)
def update_profile(
        profile_id: UUID,
        dto: UpdateProfileDTO,
        session: Session = Depends(get_session)
):
    use_case = make_update_profile_use_case(session)
    profile_updated = use_case.execute(profile_id, dto)
    return ProfileResponseDTO.from_entity(profile_updated)


@router.delete("/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(profile_id: UUID, session: Session = Depends(get_session)):
    use_case = make_delete_profile_use_case(session)
    use_case.execute(profile_id)
    return None
