"""
Модуль для изменения сущности.

Содержит класс и функции для изменения сущности.
"""
import allure
from api.requests.base_requests_api import BaseApi
from data.data_headers import HEADER_WITH_BODY
from data.data_urls import URL_UPDATE


class UpdateObject(BaseApi):
    """
    Класс для изменения сущности.
    """
    def __init__(self):
        super().__init__()
        self.headers = HEADER_WITH_BODY

    def update_object_by_id(self, id_object: str, body: str) -> None:
        """
        Изменяет сущность по id,
        отправляя PATCH-запрос на указанный URL.
        :param body: Тело запроса.
        :param id_object: Идентификатор сущности.
        :return: None.
        """
        url = URL_UPDATE.format(id=id_object)
        with allure.step(f'Обновление сущности по id: {id_object}'):
            self.response = self.request_patch(url, **{'data': body})
