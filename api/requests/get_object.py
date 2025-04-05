"""
Модуль для получения информации о сущности.

Содержит класс и функции для получения информации о сущности.
"""
import allure
from pydantic import ValidationError
from api.requests.base_requests_api import BaseApi
from data.data_headers import HEADER_GET
from data.data_urls import URL_GET
from models.entity_request import EntityRequest
from models.entity_response import EntityResponse


class GetObject(BaseApi):
    """
    Класс для получения информации о сущности.
    """
    def __init__(self):
        """
        Инициализирует объект класса.
        Устанавливает заголовки запроса.
        """
        super().__init__()
        self.headers = HEADER_GET
        self.entity = None

    def get_by_id(self, id_object: str) -> None:
        """
        Получает информуцию о сущности по id,
        отправляя GET-запрос на указанный URL.
        :param id_object: Идентификатор сущности.
        :return: None.
        """
        url = URL_GET.format(id=id_object)
        with allure.step(f'Получение сущности по id:{id_object}'):
            self.response = self.request_get(url)
            try:
                self.entity = EntityResponse.model_validate(self.get_body())
            except ValidationError as e:
                raise ValidationError(
                    "Ошибка валидации данных", e.json()
                ) from e

    def get_by_id_negative(self, id_object: str) -> None:
        """
        Получает информуцию о сущности по id.
        :param id_object: Идентификатор сущности.
        :return: None.
        """
        url = URL_GET.format(id=id_object)
        with allure.step(f'Получение сущности по id:{id_object}'):
            self.response = self.request_get_negative(url)

    def check_id(self, id_object: str) -> bool:
        """
        Проверяет, что id есть в информации о сущности.
        :param id_object: Идентификатор сущности.
        :return: True, если идентификатор относится к сущности,
        в противном случае False.
        """
        with allure.step('Проверка, что id совпадает с id из ответа'):
            return ((self.entity.id == int(id_object)) and
                    (self.entity.addition.id == int(id_object)))

    def check_param_in_body_for_create(self, body_object: str) -> bool:
        """
        Сравнивает тело запроса с переданным объектом,
        исключая ключи 'id'.
        :param body_object: JSON-строка, представляющая
        тело запроса для сравнения.
        :return: True, если тела запроса одинаковы,
        False в противном случае.
        """
        entity_response = self.entity.model_dump(exclude={
            "id": True,
            "addition": {"id"}
        })
        entity_request = EntityRequest.model_validate_json(body_object).model_dump()
        with allure.step(
                'Проверка, что параметры созданной сущности совпадают с параметрами из ответа'
        ):
            return entity_response == entity_request

    def check_param_in_body(self, body_object: str) -> bool:
        """
        Сравнивает тело запроса с переданным объектом.
        :param body_object: JSON-строка, представляющая
        тело запроса для сравнения.
        :return: True, если тела запроса одинаковы,
        False в противном случае.
        """
        with allure.step('Проверка, что тело ответа соответствует ожидаемому'):
            return self.get_body() == body_object
