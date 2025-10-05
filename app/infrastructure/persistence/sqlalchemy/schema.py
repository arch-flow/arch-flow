from app.infrastructure.persistence.sqlalchemy.connection import engine
from app.infrastructure.persistence.sqlalchemy.models import Base

def create_schema() -> None:
    Base.metadata.create_all(engine)
