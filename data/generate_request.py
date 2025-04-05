"""
Модуль для генерации тела запроса.

Содержит функции для генерации параметров и тела запроса.
"""
from typing import List
import allure
from faker import Faker
from models.additional_request import AdditionalRequest
from models.entity_request import EntityRequest

faker = Faker()


def generate_additional_info() -> str:
    """
    Генерирует дополнительные сведения о сущности.
    :return: Текст.
    """
    return faker.text()


def generate_additional_number() -> int:
    """
    Генерирует дополнительное число для сущности.
    :return: Число.
    """
    return faker.random_int(min=10, max=100)


def generate_title() -> str:
    """
    Генерирует заголовок сущности.
    :return: Заголовок сущности.
    """
    return faker.catch_phrase()


def generate_important_numbers() -> List[int]:
    """
    Генерирует массив важных чисел для сущности.
    :return: Список из двухзначных чисел.
    """
    return [faker.random_int(min=10, max=100) for _ in range(3)]


def generate_verified() -> bool:
    """
    Генерирует статус верификации сущности.
    :return: Статус верификации сущности.
    """
    return faker.random_element(elements=(True, False))


def create_entity_request() -> str:
    """
    Создает тело запроса для отправки сущности.
    :return: Тело запроса.
    """
    with allure.step(
            'Генерация тела для запроса EntityRequest'
    ):
        request = (EntityRequest(
            addition=AdditionalRequest(
                additional_info=generate_additional_info(),
                additional_number=generate_additional_number()
            ),
            important_numbers=generate_important_numbers(),
            title=generate_title(),
            verified=generate_verified()
        ).model_dump_json(indent=4))
    return request
