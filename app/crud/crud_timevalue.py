from typing import List
from typing import Any, Optional

from sqlalchemy import func, desc
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models import TimeValue
from app.schemas import TimeValueCreate, TimeValueUpdate, AggregatedTimeValue


class CRUDTimeValue(CRUDBase[TimeValue, TimeValueCreate, TimeValueUpdate]):
    async def get_aggregated_data(
        self, db: Session, skip: int = 0, limit: int = 10
    ):
        query = (
            db.query(
                func.date_trunc("minute", TimeValue.time).label("minute"),
                func.avg(TimeValue.value).label("average_value"),
            )
            .group_by(func.date_trunc("minute", TimeValue.time))
            .order_by(
                desc(func.date_trunc("minute", TimeValue.time))  # сортируем по убыванию
            )
            .offset(skip)
            .limit(limit)
        )
        return query.all()
        # stmt = (
        #     select(
        #         TimeValue.time,  # Include the TimeValue.time column in the query
        #         func.date_trunc("minute", TimeValue.time).label("minute"),
        #         func.avg(TimeValue.value).label("average_value"),
        #     )
        #     .group_by(TimeValue.time)  # Group by TimeValue.time
        #     .order_by(TimeValue.time.desc())  # Order by TimeValue.time in descending order
        #     .offset(skip)
        #     .limit(limit)
        # )
        
        # result = await db.execute(stmt)
        # return result.all()


crud_time_value = CRUDTimeValue(TimeValue)
