# ============================================================================
# src/db/session.py
# ============================================================================
from sqlalchemy import create_engine, pool
from sqlalchemy.orm import sessionmaker
from src.core.config import settings

# ✅ Get the database URL directly from settings
DATABASE_URL = settings.get_database_url()

# ✅ Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    poolclass=pool.QueuePool,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW,
    pool_timeout=settings.DB_POOL_TIMEOUT,
    pool_recycle=settings.DB_POOL_RECYCLE,
    pool_pre_ping=True,  # Verifies connections before using them
    echo=settings.DEBUG,  # Logs SQL queries if DEBUG=True
)

# ✅ Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Yield a database session and ensure it’s closed after use."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
