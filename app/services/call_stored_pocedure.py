from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import SessionLocal


class DatabaseHandler:
    async def call_stored_procedure():
        async with SessionLocal() as db:
            async with db.begin():
                await db.execute("SELECT insert_random_data()")
