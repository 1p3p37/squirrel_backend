from fastapi import FastAPI

from app.core.config import settings
from fastapi import APIRouter

from app.api.endpoints import time_value, login, users

app_v1 = APIRouter()
app_v1.include_router(login.router, tags=["login"])
app_v1.include_router(users.router, prefix="/users", tags=["users"])

app_v1 = FastAPI(title=settings.project_name)

app_v1.include_router(time_value.router)
