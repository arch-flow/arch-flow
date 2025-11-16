from functools import lru_cache

from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    APP_NAME: str
    VERSION: str
    ENVIRONMENT: str
    USE_POSTGRES: bool

    POSTGRES_URL: str
    SQLITE_URL: str = "sqlite+pysqlite:///./data/db/archflow.db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_config() -> AppConfig:
    return AppConfig()
