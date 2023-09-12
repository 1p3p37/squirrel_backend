# from datetime import timedelta
from typing import Dict, Generator

# import pyotp
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from mixer.backend.sqlalchemy import Mixer

from app.db.session import SessionLocal
from app.main import app
from app.core.config import settings
from app.tests.utils.user import authentication_token_from_email
from app.tests.utils.utils import get_superuser_token_headers


@pytest.fixture(scope="session")
def db():
    yield SessionLocal()


# @pytest.fixture()
# def db(session_local):
#     mixer = Mixer(session=session_local, commit=True)
#     yield mixer


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

# Fixture to get superuser token headers
@pytest.fixture(scope="module")
async def superuser_token_headers(client: TestClient) -> Dict[str, str]:
    """
    Get token headers for a superuser.
    """
    return await get_superuser_token_headers(client)

# Fixture to get normal user token headers
@pytest.fixture(scope="function")
async def normal_user_token_headers(client: TestClient, db: Session) -> Dict[str, str]:
    """
    Get token headers for a normal user.
    """
    return await authentication_token_from_email(
        client=client, email=settings.EMAIL_TEST_USER, db=db
    )


# @pytest.fixture()
# def user(db = mixer) -> User:
#     new_user = schemas.UserCreate(
#         email="user@user.com",
#         password="password",
#         # is_superuser=True,
#     )
#     user = crud.user.get_by_email(db=db, email=new_user["email"])
#     if user is None:
#         user = crud.user.create(db=db, obj_in=new_user)
#     return user

# @pytest.mark.asyncio
# async def test_create_user(client):
#     # Создаем тестового пользователя с помощью mixer
#     user_data = mixer.blend(User)

#     # Отправляем запрос на создание пользователя
#     response = client.post("/users/create", json=user_data.dict())

#     # Проверяем, что статус код ответа равен 200 (Успешное создание пользователя)
#     assert response.status_code == 200

#     # Проверяем, что в ответе есть поля пользователя и они соответствуют отправленным данным
#     created_user = response.json()
#     assert created_user["full_name"] == user_data.full_name
#     assert created_user["email"] == user_data.email
