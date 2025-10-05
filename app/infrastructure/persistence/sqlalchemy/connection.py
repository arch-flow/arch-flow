from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import DB_PATH, DATA_DIR

DATA_DIR.mkdir(parents=True, exist_ok=True)
engine = create_engine(f"sqlite:///{DB_PATH}", future=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, future=True)
