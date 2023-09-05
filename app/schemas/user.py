from uuid import UUID

from pydantic import BaseModel


class UserGetOrCreate(BaseModel):
    user_id: UUID
    user_name: str | None


class UserInDB(BaseModel):
    id: UUID
    name: str | None
    eth_address: str
    btc_address: str
    erc20_address: str

    class Config:
        orm_mode = True
