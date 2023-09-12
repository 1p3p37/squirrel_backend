from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud
from app.core.security import verify_password
from app.schemas.user import UserCreate, UserUpdate
from app.tests.utils.utils import random_email, random_lower_string

# Функция для создания пользователя
async def test_create_user(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password)
    
    # Создаем пользователя асинхронно
    user = await crud.user.create(db, obj_in=user_in)
    
    # Проверяем, что пользователь создан и email совпадает
    assert user.email == email
    assert hasattr(user, "hashed_password")

# Функция для аутентификации пользователя
async def test_authenticate_user(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password)
    
    # Создаем пользователя асинхронно
    user = await crud.user.create(db, obj_in=user_in)
    
    # Аутентифицируем пользователя
    authenticated_user = await crud.user.authenticate(db, email=email, password=password)
    
    # Проверяем, что аутентификация прошла успешно и email совпадает
    assert authenticated_user
    assert user.email == authenticated_user.email

# Функция для проверки неуспешной аутентификации пользователя
async def test_not_authenticate_user(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    
    # Пытаемся аутентифицировать несуществующего пользователя
    user = await crud.user.authenticate(db, email=email, password=password)
    
    # Проверяем, что пользователь не аутентифицирован (должен вернуться None)
    assert user is None

# Функция для проверки, является ли пользователь суперпользователем
async def test_check_if_user_is_superuser(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password, is_superuser=True)
    
    # Создаем суперпользователя асинхронно
    user = await crud.user.create(db, obj_in=user_in)
    
    # Проверяем, что пользователь является суперпользователем
    is_superuser = await crud.user.is_superuser(db, user)
    assert is_superuser is True

# Функция для проверки, не является ли пользователь суперпользователем
async def test_check_if_user_is_superuser_normal_user(db: Session) -> None:
    username = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=username, password=password)
    
    # Создаем обычного пользователя асинхронно
    user = await crud.user.create(db, obj_in=user_in)
    
    # Проверяем, что пользователь не является суперпользователем
    is_superuser = await crud.user.is_superuser(db, user)
    assert is_superuser is False

# Функция для получения пользователя
async def test_get_user(db: Session) -> None:
    password = random_lower_string()
    username = random_email()
    user_in = UserCreate(email=username, password=password, is_superuser=True)
    
    # Создаем пользователя асинхронно
    user = await crud.user.create(db, obj_in=user_in)
    
    # Получаем пользователя асинхронно по ID
    user_2 = await crud.user.get(db, id=user.id)
    
    # Проверяем, что пользователь успешно получен и его данные совпадают
    assert user_2
    assert user.email == user_2.email
    assert jsonable_encoder(user) == jsonable_encoder(user_2)

# Функция для обновления пользователя
async def test_update_user(db: Session) -> None:
    password = random_lower_string()
    email = random_email()
    user_in = UserCreate(email=email, password=password, is_superuser=True)
    
    # Создаем пользователя асинхронно
    user = await crud.user.create(db, obj_in=user_in)
    
    new_password = random_lower_string()
    user_in_update = UserUpdate(password=new_password, is_superuser=True)
    
    # Обновляем пользователя асинхронно
    await crud.user.update(db, db_obj=user, obj_in=user_in_update)
    
    # Получаем обновленного пользователя
    user_2 = await crud.user.get(db, id=user.id)
    
    # Проверяем, что обновление прошло успешно и пароль изменен
    assert user_2
    assert user.email == user_2.email
    assert verify_password(new_password, user_2.hashed_password)
