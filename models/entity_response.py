import pydantic
from pydantic import BaseModel
from typing import List
from models.additional_response import AdditionalResponse


class EntityResponse(BaseModel):
    """
    Модель для получения сущности.

    Attributes:
        addition: из модели AdditionalResponse
        important_numbers(List[int]): Массив важных чисел для сущности.
        title (str): Заголовок сущности.
        verified (bool): Статус верификации сущности.
    """
    addition: AdditionalResponse
    id: int
    important_numbers: List[int]
    title: str
    verified: bool


class EntityResponseList(BaseModel):
    """
    Модель для получения списка сущностей.

    Attributes:
        entity: список сущностей
    """
    entity: List[EntityResponse]
