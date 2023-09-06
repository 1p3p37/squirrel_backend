from pydantic import BaseModel, condecimal
from datetime import datetime


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
    average_value: condecimal(max_digits=10, decimal_places=2)