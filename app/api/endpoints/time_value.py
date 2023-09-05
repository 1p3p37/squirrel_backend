import datetime

from typing import List, Dict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps


router = APIRouter()


@router.get("/get_aggregated_data/", response_model=List[schemas.AggregatedTimeValue])
def get_aggregated_data(
    skip: int = 0, limit: int = 10, db: Session = Depends(deps.get_db)
):
    """
    Получает поминутно агрегированные данные таблицы `time_value`.

    skip: Количество записей, которые следует пропустить (по умолчанию 0).
    limit: Максимальное количество записей для возврата (по умолчанию 10).
    """
    aggregated_data = crud.crud_time_value.get_aggregated_data(
        db=db, skip=skip, limit=limit
    )
    return aggregated_data