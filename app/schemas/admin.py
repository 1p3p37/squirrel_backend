from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class AdminBase(BaseModel):
    email: Optional[EmailStr]


# Properties to receive via API on creation
class AdminCreate(AdminBase):
    email: EmailStr
    password: str


class AdminLogin(AdminBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class AdminUpdate(AdminBase):
    password: Optional[str] = None


class AdminInDBBase(AdminBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Admin(AdminInDBBase):
    pass


# Additional properties stored in DB
class AdminInDB(AdminInDBBase):
    hashed_password: str
