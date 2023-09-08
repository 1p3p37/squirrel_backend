import asyncio

from app.services.utils import execute_query
from app.core.config import settings


async def init_db():
    await execute_query(settings.sql_queries.create_insert_data_procedure)
    await execute_query(settings.sql_queries.create_high_trigger_procedure)
    await execute_query(settings.sql_queries.create_high_value_trigger)
    await execute_query(settings.sql_queries.create_aggregated_data_view)


if __name__ == "__main__":
    print("Initializing data ...")
    asyncio.run(init_db())  # Use asyncio.run to run the async function
    print("All data successfully initialized!")
