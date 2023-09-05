from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

# Схема для HighValue
class HighValueBase(BaseModel):
    time: datetime


class HighValueCreate(HighValueBase):
    pass


class HighValue(HighValueBase):
    id: int

    class Config:
        orm_mode = True
