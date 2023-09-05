from time import sleep

from app.services.call_stored_pocedure import DatabaseHandler


async def handle_call_stored_procedure():
    DatabaseHandler.call_stored_procedure()
