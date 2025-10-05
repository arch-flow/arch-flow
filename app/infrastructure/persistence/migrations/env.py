from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool, text
from app.config.settings import DB_PATH
import app.infrastructure.persistence.sqlalchemy.types
from app.infrastructure.persistence.sqlalchemy import models

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

section = config.get_section(config.config_ini_section)
section["sqlalchemy.url"] = f"sqlite+pysqlite:///{DB_PATH}"

target_metadata = models.Base.metadata

def run_migrations_offline():
    context.configure(
        url=section["sqlalchemy.url"],
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        render_as_batch=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        section,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        future=True,
    )
    with connectable.connect() as connection:
        connection.execute(text("PRAGMA foreign_keys=ON"))
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            render_as_batch=True,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
