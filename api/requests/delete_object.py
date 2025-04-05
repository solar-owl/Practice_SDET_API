"""
Модуль для удаления сущности.

Содержит класс и функции для удаления сущности.
"""
import allure
from api.requests.base_requests_api import BaseApi
from data.data_headers import HEADER_DELETE
from data.data_urls import URL_DELETE


class DeleteObject(BaseApi):
    """
    Класс для удаления сущности.
    """
    def __init__(self):
        """
        Инициализирует объект класса.
        Устанавливает заголовки запроса.
        """
        super().__init__()
        self.headers = HEADER_DELETE

    def delete_object_by_id(self, id_object: str) -> None:
        """
        Удаляет сущность по id, отправляя DELETE-запрос
        на указанный URL.
        :param id_object: Идентификатор сущности.
        :return: None.
        """
        url = URL_DELETE.format(id=id_object)
        with allure.step(f'Удаление сущности по id: {id_object}'):
            self.response = self.request_delete(url)

    def delete_multiple_objects_by_id(self, ids: [str]) -> None:
        """
        Удаляет сущности по id, отправляя DELETE-запрос
        на указанный URL.
        :param ids: Список из идентификаторов сущностей.
        :return: None.
        """
        with allure.step('Удаление нескольких сущностей'):
            for id_object in ids:
                self.delete_object_by_id(id_object)
