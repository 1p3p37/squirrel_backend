from typing import List
from typing import Any, Optional

# import pyotp
from sqlalchemy import func, desc
from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUD
from app.models import TimeValue


class CRUDTimeValue(CRUD):
    def get_aggregated_data(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[TimeValue]:
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


crud_time_value = CRUDTimeValue(TimeValue)
