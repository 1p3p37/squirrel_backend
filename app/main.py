import logging

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api import app_v1
from app.core.config import settings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.project_name,
    openapi_url=f"{settings.api_string}/openapi.json",
)

app.include_router(app_v1, prefix=settings.api_string)

# Set all CORS enabled origins
# if settings.backend_cors_origins:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=[str(origin) for origin in settings.backend_cors_origins],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )
