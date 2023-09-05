# from app import crud, custom_types
from app.core.config import settings
from app.db.session import SessionLocal
from app.services.utils import (
    create_high_trigger_procedure,
    create_insert_data_procedure,
)


def init_db():
    db = SessionLocal()

    create_insert_data_procedure(db=db)
    create_high_trigger_procedure(db=db)


if __name__ == "__main__":
    print("Initializing data ...")
    init_db()
    print("All data successfully initialized!")
