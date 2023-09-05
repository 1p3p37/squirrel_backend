from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import SessionLocal


class DatabaseHandler:
    def call_stored_procedure():
        db = SessionLocal()
        try:
            db.execute("SELECT insert_random_data()")
            db.commit()
        finally:
            db.close()
