import random
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from app.db.base_class import Base


class TimeValue(Base):
    __tablename__ = "time_value"
    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime, default=datetime.now().timestamp())
    value = Column(Integer, default=lambda: random.randint(0, 10))
