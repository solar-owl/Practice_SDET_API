"""
Модуль для работы с API.

Содержит класс и функции для работы с API.
"""
import allure
import requests
from requests import Response


class BaseApi:
    """
    Класс для работы с API.
    """
    def __init__(self):
        """
        Инициализирует экземпляр класса BaseApi.
        :param response: Ответ.
        :param headers: Хедеры для запроса.
        :param body: Тело ответа.
        """
        self.response = None
        self.headers = None
        self.body = None
        self.timeout = 10

    def request_get(self, url: str, **kwargs: dict) -> Response | None:
        """
        Отправляет GET запрос по указанному URL.
        :param url: Ссылка для запроса.
        :param kwargs: Дополнительные параметры запроса (json, body и др.)
        :return: Ответ сервера.
        """
        try:
            response = requests.get(url, headers=self.headers, **kwargs, timeout=self.timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            print("The request timed out.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении GET запроса: {e}")
            return None

    def request_get_negative(self, url: str, **kwargs: dict) -> Response | None:
        """
        Отправляет GET запрос по указанному URL без отлова ошибок.
        :param url: Ссылка для запроса.
        :param kwargs: Дополнительные параметры запроса (json, body и др.)
        :return: Ответ сервера.
        """
        try:
            response = requests.get(url, headers=self.headers, **kwargs, timeout=self.timeout)
            return response
        except requests.exceptions.Timeout:
            print("The request timed out.")
            return None

    def request_post(self, url: str, **kwards: dict) -> Response | None:
        """
        Отправляет POST запрос по указанному URL.
        :param url: Ссылка для запроса.
        :param kwargs: Дополнительные параметры запроса (json, body и др.)
        :return: Ответ сервера.
        """
        try:
            response = requests.post(url, headers=self.headers, **kwards, timeout=self.timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            print("The request timed out.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении POST запроса: {e}")
            return None

    def request_patch(self, url: str, **kwargs: dict) -> Response | None:
        """
        Отправляет PATCH запрос по указанному URL.
        :param url: Ссылка для запроса.
        :param kwargs: Дополнительные параметры запроса (json, body и др.)
        :return: Ответ сервера.
        """
        try:
            response = requests.patch(url, headers=self.headers, **kwargs, timeout=self.timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            print("The request timed out.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении PATCH запроса: {e}")
            return None

    def request_delete(self, url: str, **kwargs: dict) -> Response | None:
        """
        Отправляет DELETE запрос по указанному URL.
        :param url: Ссылка для запроса.
        :param kwargs: Дополнительные параметры запроса (json, body и др.)
        :return: Ответ сервера.
        """
        try:
            response = requests.delete(url, headers=self.headers, **kwargs, timeout=self.timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            print("The request timed out.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении DELETE запроса: {e}")
            return None

    def check_response_is_200(self) -> bool:
        """
        Проверяет, что код ответа 200.
        :return: True, если код 200, в противном случае False.
        """
        with allure.step('Проверка, что статус код 200'):
            return self.response.status_code == 200

    def check_response_is_204(self) -> bool:
        """
        Проверяет, что код ответа 204.
        :return: True, если код 204, в противном случае False.
        """
        with allure.step('Проверка, что статус код 204'):
            return self.response.status_code == 204

    def check_response_is_500(self) -> bool:
        """
        Проверяет, что код ответа 500.
        :return: True, если код 500, в противном случае False.
        """
        with allure.step('Проверка, что статус код 500'):
            return self.response.status_code == 500

    def get_body(self) -> str:
        """
        Возвращает тело ответа в виде словаря.
        :return: Словарь с данными ответа.
        """
        return self.response.json()

    def get_text(self) -> str:
        """
        Получает id сущности из ответа.
        :return: Идентификатор сущности.
        """
        print(self.response)
        if self.response is None:
            raise ValueError(
                "Ответ сервера отсутствует. Проверьте выполнение запроса."
            )
        return self.response.text
