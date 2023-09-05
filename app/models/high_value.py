from sqlalchemy import Column, Integer, DateTime
from app.db.base_class import Base


class HighValues(Base):
    __tablename__ = "high_values"
    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime)
