from __future__ import annotations

import os
import secrets
from dataclasses import field
from functools import cached_property

import yaml
from pydantic import AnyHttpUrl, PostgresDsn, EmailStr
from pydantic.dataclasses import dataclass


DB_URL = "postgres://{user}:{password}@{hostname}:{port}/{db}".format(
    user=os.getenv("POSTGRES_USER", "postgres"),
    password=os.getenv("POSTGRES_PASSWORD", "postgres"),
    hostname=os.getenv("POSTGRES_HOST", "127.0.0.1"),
    db=os.getenv("POSTGRES_DB", "postgres"),
    port=os.getenv("POSTGRES_PORT", 5432),
)


@dataclass
class SQLQueries:
    create_insert_data_procedure: str
    create_high_trigger_procedure: str
    create_high_value_trigger: str
    create_aggregated_data_view: str


@dataclass
class Settings:
    project_name: str
    api_string: str = "/api"
    api_test_string: str = "http://test"
    api_debug_str: str = "/api/debug"
    api_key: str = secrets.token_urlsafe(32)
    sql_queries: SQLQueries = field(default_factory=SQLQueries)
    call_stored_procedure_task_interval_seconds: int = 5
    access_token_expire_minutes: int = 60 * 24 * 7  # 7 days
    backend_cors_origins: list[AnyHttpUrl] = field(default_factory=list)
    password_length: int = 12
    is_test: bool = os.getenv("IS_TEST", False)

    @cached_property
    def sqlalchemy_database_uri(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            path=f"/{os.getenv('POSTGRES_DB') or ''}",
        )

    EMAIL_TEST_USER: EmailStr = "test@example.com"  # type: ignore
    FIRST_SUPERUSER: EmailStr = "supersu@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin1234"

    # @cached_property
    # def redis_url(self) -> str:
    #     return f"redis://{self.redis_host}:{self.redis_port}/0"


with open(os.environ["CONFIG"], "r") as f:
    config_data = yaml.safe_load(f)


settings = Settings(**config_data)
