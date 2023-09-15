from typing import Dict
import pytest

# from fastapi.testclient import TestClient
from httpx import AsyncClient

from app.core.config import settings


# Test to get an access token

@pytest.mark.anyio
async def test_get_access_token(client: AsyncClient) -> None:
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = await client.post(
        f"http://test{settings.api_string}/login/access-token", data=login_data
    )
    tokens = r.json()
    assert r.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]
