# ============================================================================
# src/db/session.py
# ============================================================================
from sqlalchemy import create_engine, pool
from sqlalchemy.orm import sessionmaker
from src.core.config import settings

# Get database URL from settings
DATABASE_URL = settings.get_database_url()

# Create SQLAlchemy engine with PostgreSQL configuration
engine = create_engine(
    DATABASE_URL,
    poolclass=pool.QueuePool,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW,
    pool_timeout=settings.DB_POOL_TIMEOUT,
    pool_recycle=settings.DB_POOL_RECYCLE,
    pool_pre_ping=True,  # Verify connections before using
    echo=settings.DEBUG,  # Log SQL queries in debug mode
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for FastAPI or other frameworks
def get_db():
    """Yield a database session, then close it"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
