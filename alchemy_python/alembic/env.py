from logging.config import fileConfig
from sqlalchemy import engine_from_config, create_engine, pool
from alembic import context
from main import Base

# Alembic Config object
config = context.config

# Logging configuration
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Using metadata from `main.py`
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(url="postgresql://viktoriakubinec:@localhost:5432/mydatabase")
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = context.config.attributes.get('connection', None)
    if connectable is None:
        connectable = create_engine("postgresql://viktoriakubinec:@localhost:5432/mydatabase")

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()