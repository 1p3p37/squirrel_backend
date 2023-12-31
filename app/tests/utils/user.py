from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from sqlalchemy.ext.asyncio import AsyncSession
from httpx import AsyncClient

from app import crud
from app.core.config import settings
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.tests.utils.utils import random_email, random_lower_string

# Get authentication headers for a user
async def user_authentication_headers(
    *, client: TestClient, email: str, password: str
) -> Dict[str, str]:
    data = {"username": email, "password": password}

    r = await client.post(
        f"http://test{settings.api_string}/login/access-token", data=data
    )
    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


# Create a random user
async def create_random_user(db: Session) -> User:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(username=email, email=email, password=password)
    user = await crud.user.create(db=db, obj_in=user_in)
    return user


# Get authentication token from email
async def authentication_token_from_email(
    *, client: AsyncClient, email: str, db: Session
) -> Dict[str, str]:
    """
    Return a valid token for the user with given email.

    If the user doesn't exist, it is created first.
    """
    password = random_lower_string()
    user = await crud.user.get_by_email(db, email=email)
    if not user:
        user_in_create = UserCreate(username=email, email=email, password=password)
        user = await crud.user.create(db, obj_in=user_in_create)
    else:
        user_in_update = UserUpdate(password=password)
        user = await crud.user.update(db, db_obj=user, obj_in=user_in_update)

    return await user_authentication_headers(
        client=client, email=email, password=password
    )
