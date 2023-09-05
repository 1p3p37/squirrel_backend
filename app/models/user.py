from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class User(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String, index=True)
