<<<<<<< HEAD
# alembic/env.py

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys

# Make sure the src folder is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your Base (with all models) and settings
from src.db.base import Base
from src.core.config import settings

# Alembic Config object
config = context.config

# Override sqlalchemy.url with environment variable or settings
config.set_main_option(
    'sqlalchemy.url',
    os.getenv('DATABASE_URL', settings.get_database_url())
)

# Configure Python logging from Alembic config
import logging
logging.basicConfig(level=logging.INFO)


# Metadata for 'autogenerate' support
target_metadata = Base.metadata

# -------------------------------
# Run migrations offline
# -------------------------------
=======
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from src.db.base import Base
from src.db.models import user, parking_spot  # Import your models here

config = context.config

fileConfig(config.config_file_name)

target_metadata = Base.metadata

>>>>>>> 1c47c5c (first commit)
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

<<<<<<< HEAD
# -------------------------------
# Run migrations online
# -------------------------------
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
=======
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
>>>>>>> 1c47c5c (first commit)
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
<<<<<<< HEAD
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

# -------------------------------
# Determine mode and run
# -------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
=======
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
>>>>>>> 1c47c5c (first commit)
