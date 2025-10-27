from functools import lru_cache

from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    app_name: str = "Arch Flow API"
    version: str = "0.1.0"
    environment: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache
def get_config() -> AppConfig:
    return AppConfig()
