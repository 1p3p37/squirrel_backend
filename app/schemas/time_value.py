from pydantic import BaseModel, condecimal, validator
from datetime import datetime
from decimal import Decimal


# Shared properties
class TimeValueBase(BaseModel):
    time: datetime
    value: int


# Properties to receive via API on creation
class TimeValueCreate(TimeValueBase):
    pass


# Properties to receive via API on update
class TimeValueUpdate(TimeValueBase):
    pass


# Additional properties to return via API
class TimeValue(TimeValueBase):
    id: int

    class Config:
        orm_mode = True


# Aggregated T V to return via API
class AggregatedTimeValue(BaseModel):
    time: datetime
    average_value: Decimal

    @validator("average_value", pre=True)
    def round_average_value(cls, value):
        return round(float(value), 2)
