from typing import Generator

from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.session import SessionLocal


def create_insert_data_procedure(db: Session = SessionLocal):
    db = SessionLocal()
    create_procedure_sql = text(
        """
        CREATE OR REPLACE FUNCTION insert_random_data()
        RETURNS void AS $$
        BEGIN
            INSERT INTO time_value (time, value)
            VALUES (NOW(), FLOOR(RANDOM() * 11));
        END;
        $$ LANGUAGE plpgsql;
        """
    )
    try:
        db.execute(create_procedure_sql)
        db.commit()
    finally:
        db.close()


def create_insert_data_procedure(db: Session = SessionLocal):
    db = SessionLocal()
    create_procedure_sql = text(
        """
        CREATE OR REPLACE FUNCTION record_trigger()
        RETURNS TRIGGER AS $$
        BEGIN
            IF NEW.value > 9 THEN
                INSERT INTO high_values (time)
                VALUES (NEW.time);
            END IF;
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
        
        CREATE TRIGGER high_value_trigger
        AFTER INSERT ON time_value
        FOR EACH ROW
        EXECUTE FUNCTION record_trigger();
        """
    )
    try:
        db.execute(create_procedure_sql)
        db.commit()
    finally:
        db.close()
