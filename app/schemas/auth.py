from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Login(BaseModel):
    qr_code: str
    token: str


class AuthToken(BaseModel):
    access_token: str


class AuthTokenPayload(BaseModel):
    sub: Optional[UUID] = None
