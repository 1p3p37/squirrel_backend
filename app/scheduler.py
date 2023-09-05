import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app import logs
from app.core.config import settings
from app.tasks import handle_call_stored_procedure

if __name__ == "__main__":
    logs.init()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    scheduler = AsyncIOScheduler()
    # scheduler.remove_job(handle_call_stored_procedure)
    scheduler.add_job(
        handle_call_stored_procedure,
        "interval",
        seconds=settings.call_stored_procedure_task_interval_seconds,
    )
    scheduler.start()
    loop.run_forever()
