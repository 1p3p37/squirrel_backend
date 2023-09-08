import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app import logs
from app.core.config import settings
from app.db.handlers import DbHandler


if __name__ == "__main__":
    logs.init()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        DbHandler.select_insert_random_data,
        "interval",
        seconds=settings.call_stored_procedure_task_interval_seconds,
    )

    scheduler.start()
    loop.run_forever()
