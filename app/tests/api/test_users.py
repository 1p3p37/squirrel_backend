from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.schemas.user import UserCreate
from app.tests.utils.utils import random_email, random_lower_string

# Add "async" before "def" to make the function asynchronous
async def test_get_users_superuser_me(
    client: TestClient, superuser_token_headers: Dict[str, str]
) -> None:
    # Use "await" with asynchronous client functions
    superuser_headers = await superuser_token_headers
    r = await client.get(f"{settings.api_key}/users/me", headers=superuser_headers)
    current_user = r.json()
    assert current_user
    assert current_user["is_superuser"]
    assert current_user["email"] == settings.FIRST_SUPERUSER

# Repeat the same pattern for other test functions...

async def test_create_user_by_normal_user(
    client: TestClient, normal_user_token_headers: Dict[str, str]
) -> None:
    username = random_email()
    password = random_lower_string()
    data = {"email": username, "password": password}
    normal_user_headers = await normal_user_token_headers
    r = await client.post(
        f"{settings.api_string}/users/",
        headers=normal_user_headers,
        json=data,
    )
    assert r.status_code == 400

# Repeat the same pattern for other test functions...

async def test_retrieve_users(
    client: TestClient, superuser_token_headers: Dict[str, str], db: Session
) -> None:
    username = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=username, password=password)
    await crud.user.create(db, obj_in=user_in)  # Note the use of "await" here

    username2 = random_email()
    password2 = random_lower_string()
    user_in2 = UserCreate(email=username2, password=password2)
    await crud.user.create(db, obj_in=user_in2)  # Note the use of "await" here

    superuser_headers = await superuser_token_headers
    r = await client.get(f"{settings.api_string}/users/", headers=superuser_headers)
    all_users = r.json()

    assert len(all_users) > 1
    for item in all_users:
        assert "email" in item
