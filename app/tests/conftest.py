from typing import Dict

# import pyotp
import pytest_asyncio
import pytest

# from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from httpx import AsyncClient

from app.db.session import SessionLocal, create_async_engine
from app.main import app
from app.core.config import settings
from app.tests.utils.user import authentication_token_from_email
from app.tests.utils.utils import get_superuser_token_headers


# @pytest.fixture(scope="session")
# @pytest_asyncio.fixture(scope="session")
# async def db():
#     with SessionLocal() as _db:
#         yield _db
# yield SessionLocal()
@pytest.fixture(scope="module")
async def db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session


# @pytest_asyncio.fixture(scope="module")
@pytest.fixture(scope="module")
async def client() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


# Fixture to get superuser token headers
@pytest_asyncio.fixture(scope="module")
async def superuser_token_headers(client: AsyncClient) -> Dict[str, str]:
    """
    Get token headers for a superuser.
    """
    return await get_superuser_token_headers(client)


# Fixture to get normal user token headers
@pytest_asyncio.fixture(scope="module")
async def normal_user_token_headers(
    client: AsyncClient, db: AsyncSession
) -> Dict[str, str]:
    """
    Get token headers for a normal user.
    """
    return await authentication_token_from_email(
        client=client, email=settings.EMAIL_TEST_USER, db=db
    )

