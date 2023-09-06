from sqlalchemy import Column, Integer, DateTime
from app.db.base_class import Base


class HighValue(Base):
    __tablename__ = "high_value"
    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime)
