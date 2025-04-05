"""
Модуль для получения информации о всех сущностях.

Содержит класс и функции для получения информации о сущностях.
"""
from typing import List
import allure
from pydantic import ValidationError
from api.requests.base_requests_api import BaseApi
from data.data_headers import HEADER_GET
from data.data_urls import URL_GET_ALL
from models.entity_response import EntityResponseList


class GetAllObject(BaseApi):
    """
    Класс для получения данных о всех сущностях.
    """
    def __init__(self):
        """
        Инициализирует объект класса.
        Устанавливает заголовки запроса.
        """
        super().__init__()
        self.headers = HEADER_GET
        self.entities = None

    def get_all(self) -> None:
        """
        Получает информуцию о сущностях,
        отправляя GET-запрос на указанный URL.
        :return: None.
        """
        with allure.step('Получение всех сущностей'):
            self.response = self.request_get(URL_GET_ALL)
            try:
                self.entities = EntityResponseList.model_validate(self.get_body())
            except ValidationError as e:
                raise ValidationError(
                    "Ошибка валидации данных", e.json()
                ) from e

    def check_ids_in_response(self, ids_object: List[str]) -> bool:
        """
        Проверяет, что id из списка есть в информации о сущностях.
        :param ids_object: Идентификатор сущности.
        :return: True, если идентификатор относится к сущности,
        в противном случае False.
        """
        ids_in_response = [ent.id for ent in self.entities.entity]
        with allure.step('Проверка, что id созданных сущностей есть в ответе'):
            if set(ids_object).issubset(set(map(str, ids_in_response))):
                return True
            else:
                not_found_ids = set(ids_object) - set(map(str, ids_in_response))
                raise ValueError(f"Не найденные ID: {not_found_ids}")
