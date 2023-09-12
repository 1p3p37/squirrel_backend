import asyncio

from app.db.session import SessionLocal
from app.core.config import settings
from app.db.handlers import DbHandler
from app.services.utils import execute_query
from app import crud, schemas


async def init_db():
    db = SessionLocal()
    await execute_query(settings.sql_queries.create_insert_data_procedure)
    await execute_query(settings.sql_queries.create_high_trigger_procedure)
    await execute_query(settings.sql_queries.create_high_value_trigger)
    await execute_query(settings.sql_queries.create_aggregated_data_view)
    user = await crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = await crud.user.create(db, obj_in=user_in)

    if settings.is_test:
        for i in range(350):
            await DbHandler.select_insert_random_data()



if __name__ == "__main__":
    print("Initializing data ...")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(init_db())
    loop.close()
    print("All data successfully initialized!")
