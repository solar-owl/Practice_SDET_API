"""
Модуль для создания сущности.

Содержит класс и функции для создания сущности.
"""
import allure
from api.requests.base_requests_api import BaseApi
from data.data_headers import HEADER_WITH_BODY
from data.data_urls import URL_CREATE


class CreateObject(BaseApi):
    """
    Класс для создания сущности.
    """
    def __init__(self):
        """
        Инициализирует объект класса.
        Устанавливает заголовки запроса.
        """
        super().__init__()
        self.headers = HEADER_WITH_BODY

    def new_object(self, body: str) -> None:
        """
        Создает новую сущность, отправляя POST-запрос на указанный URL.
        :param body: Тело запроса.
        :return: None.
        """
        with allure.step('Создание новой сущности'):
            self.response = self.request_post(URL_CREATE, **{'data': body})

    def get_id(self) -> str:
        """
        Получает id сущности из ответа.
        :return: Идентификатор сущности.
        """
        if self.response is None:
            raise ValueError(
                "Ответ сервера отсутствует. Проверьте выполнение запроса."
            )
        with allure.step('Получение id новой сущности'):
            return self.get_text()
