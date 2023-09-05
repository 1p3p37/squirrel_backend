from fastapi import FastAPI

from app.api.endpoints import time_value
from app.core.config import settings

app_v1 = FastAPI(title=settings.project_name)
# app = FastAPI(title="squirrel_backend")

app_v1.include_router(
    time_value.router
    # prefix="/total_votes",
    # tags=["total_votes"],
)

# app_v1.include_router(
#     time_convertor.router,
#     prefix="/time-convertor",
# )
