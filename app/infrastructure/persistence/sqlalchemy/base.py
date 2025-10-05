import uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

def pk_uuid() -> Mapped[uuid.UUID]:
    return mapped_column(String(36), primary_key=True, default=uuid.uuid4)
