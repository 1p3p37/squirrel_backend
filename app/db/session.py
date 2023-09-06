from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from app.core.config import settings

engine = create_async_engine(settings.sqlalchemy_database_uri, pool_pre_ping=True)
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)
