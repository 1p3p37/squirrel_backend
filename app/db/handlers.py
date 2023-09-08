from app.services.utils import execute_query, execute_select_query


class DbHandler:
    async def select_insert_random_data():
        await execute_query("SELECT insert_random_data();")

    async def get_slises_agregated_data(skip: int = 0, limit: int = 10):
        return await execute_select_query(
            sql=f"SELECT * FROM aggregated_data ORDER BY time DESC LIMIT {limit} OFFSET {skip};"
        )
