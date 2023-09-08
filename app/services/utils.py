from sqlalchemy import text

from app.db.session import SessionLocal
from app.core.config import settings


async def execute_query(sql: str):
    try:
        async with SessionLocal() as db:
            async with db.begin():
                await db.execute(text(sql))
    except Exception as e:
        await db.rollback()
        raise e


async def execute_select_query(sql: str):
    try:
        async with SessionLocal() as db:
            async with db.begin():
                result = await db.execute(text(sql))
                data = result.fetchall()
                return data
    except Exception as e:
        await db.rollback()
        raise e
