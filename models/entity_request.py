from pydantic import BaseModel
from typing import List
from models.additional_request import AdditionalRequest


class EntityRequest(BaseModel):
    """
    Модель для отправки сущности.

    Attributes:
        addition: из модели AdditionalRequest
        important_numbers(List[int]): Массив важных чисел для сущности.
        title (str): Заголовок сущности.
        verified (bool): Статус верификации сущности.
    """
    addition: AdditionalRequest
    important_numbers: List[int]
    title: str
    verified: bool
