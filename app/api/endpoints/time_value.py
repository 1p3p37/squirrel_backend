import datetime

from typing import List, Dict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app import models, crud, schemas
from app.db.handlers import DbHandler
from app.api import deps


router = APIRouter()


@router.get("/get_aggregated_data/", response_model=List[schemas.AggregatedTimeValue])
async def get_aggregated_data(
    skip: int = 0,
    limit: int = 10,
):
    """
    Получает поминутно агрегированные данные таблицы `time_value`.

    skip: Количество записей, которые следует пропустить (по умолчанию 0).
    limit: Максимальное количество записей для возврата (по умолчанию 10).
    """
    return await DbHandler.get_slises_agregated_data(skip, limit)
