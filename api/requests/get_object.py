"""
Модуль для получения информации о сущности.

Содержит класс и функции для получения информации о сущности.
"""
import json
import allure
from api.requests.base_requests_api import BaseApi
from data.data import URL_GET, HEADER_GET


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
        self.body = self.get_body()

    def get_by_id_negative(self, id_object: str) -> None:
        """
        Получает информуцию о сущности по id.
        :param id_object: Идентификатор сущности.
        :return: None.
        """
        url = URL_GET.format(id=id_object)
        with allure.step(f'Получение сущности по id:{id_object}'):
            self.response = self.request_get_negative(url)
        self.body = self.get_body()

    def check_id(self, id_object: str) -> bool:
        """
        Проверяет, что id есть в информации о сущности.
        :param id_object: Идентификатор сущности.
        :return: True, если идентификатор относится к сущности,
        в противном случае False.
        """
        with allure.step('Проверка, что id совпадает с id из ответа'):
            return (self.body['id'] == int(id_object) and
                    self.body['addition']['id'] == int(id_object))

    def check_param_in_body_for_create(self, body_object: str) -> bool:
        """
        Сравнивает тело запроса с переданным объектом,
        исключая ключи 'id'.
        :param body_object: JSON-строка, представляющая
        тело запроса для сравнения.
        :return: True, если тела запроса одинаковы,
        False в противном случае.
        """
        get_body = self.body
        get_body.pop('id')
        get_body['addition'].pop('id')
        body_object = json.loads(body_object)
        with allure.step('Проверка, что параметры совпадают с параметрами из ответа'):
            return get_body == body_object

    def check_param_in_body(self, body_object: str) -> bool:
        """
        Сравнивает тело запроса с переданным объектом.
        :param body_object: JSON-строка, представляющая
        тело запроса для сравнения.
        :return: True, если тела запроса одинаковы,
        False в противном случае.
        """
        with allure.step('Проверка, что тело ответа соответствует ожидаемому'):
            return self.body == body_object
