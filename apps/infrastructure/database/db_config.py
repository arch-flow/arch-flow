from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from apps.core.config import get_config

config = get_config()

DATABASE_URL = (
    config.POSTGRES_URL
    if config.USE_POSTGRES
    else config.SQLITE_URL
)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if not config.USE_POSTGRES else {}
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_session() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
