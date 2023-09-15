import pytest
from typing import Dict

# from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

# from sqlalchemy.ext.asyncio import AsyncSession
from httpx import AsyncClient

from app import crud, schemas
from app.core.config import settings
from app.schemas.user import UserCreate, UserUpdate, UserBase
from app.tests.utils.utils import random_email, random_lower_string


@pytest.mark.anyio
async def test_create_user(
    client: AsyncClient, db: Session, superuser_token_headers: Dict[str, str]
):
    # Define test data
    email = random_email()
    password = random_lower_string()
    user_data = UserCreate(
        email=email,
        password=password,
    )

    # Create a user
    response = await client.post(
        f"{settings.api_test_string}{settings.api_string}/users/create",
        json=user_data.dict(),
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    user = response.json()
    assert user["email"] == email
    assert "password" not in user  # Ensure password is not returned in the response

    # Check if the user exists in the database
    db_user = await crud.user.get_by_email(db, email=email)
    assert db_user is not None
    assert db_user.email == email
