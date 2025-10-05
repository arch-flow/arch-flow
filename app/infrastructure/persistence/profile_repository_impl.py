from typing import List, Optional
from app.domain.entities.profile import Profile
from app.domain.repositories.profile_repository import ProfileRepository
from app.infrastructure.persistence.sqlalchemy.connection import SessionLocal
from app.infrastructure.persistence.sqlalchemy.models import ProfileModel

class SqlAlchemyProfileRepository(ProfileRepository):
    def create(self, profile: Profile) -> Profile:
        with SessionLocal() as session:
            db = ProfileModel(name=profile.name, kind=profile.kind, python_version=profile.python_version, env_vars=profile.env_vars, path_entries=profile.path_entries)
            session.add(db)
            session.commit()
            session.refresh(db)
            return Profile(id=db.id, name=db.name, kind=db.kind, python_version=db.python_version, env_vars=db.env_vars, path_entries=db.path_entries)

    def get_by_name(self, name: str) -> Optional[Profile]:
        with SessionLocal() as session:
            db = session.query(ProfileModel).filter(ProfileModel.name == name).first()
            if not db:
                return None
            return Profile(id=db.id, name=db.name, kind=db.kind, python_version=db.python_version, env_vars=db.env_vars, path_entries=db.path_entries)

    def list_all(self) -> List[Profile]:
        with SessionLocal() as session:
            rows = session.query(ProfileModel).all()
            return [Profile(id=r.id, name=r.name, kind=r.kind, python_version=r.python_version, env_vars=r.env_vars, path_entries=r.path_entries) for r in rows]
