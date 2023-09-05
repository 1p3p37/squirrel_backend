from pydantic import BaseModel
from datetime import datetime
from typing import List


class AggregatedTimeValue(BaseModel):
    minute: datetime
    average_value: float


class TimeValue(BaseModel):
    data: List[AggregatedTimeValue]
