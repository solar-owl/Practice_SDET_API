"""
Модуль содержит фикстуры для проекта.
Фикстуры описывают пред- и постусловия, которые необходимы для выполнения тестов.
"""
import random
import pytest
from api.requests.create_object import CreateObject
from api.requests.delete_object import DeleteObject
from api.requests.get_all_objects import GetAllObject
from api.requests.get_object import GetObject
from api.requests.update_object import UpdateObject
from data.generate_request import create_entity_request


@pytest.fixture(scope="function")
def create_object_endpoint() -> CreateObject:
    """
    Фикстура для создания экземпляра CreateObject.
    :return: Объект для создания сущности.
    """
    return CreateObject()


@pytest.fixture(scope="function")
def get_object_endpoint() -> GetObject:
    """
    Фикстура для создания экземпляра GetObject.
    :return: Объект для получения информации о сущности.
    """
    return GetObject()


@pytest.fixture(scope="function")
def get_all_objects_endpoint() -> GetAllObject:
    """
    Фикстура для создания экземпляра GetAllObject.
    :return: Объект для получения информации о всех сущностях.
    """
    return GetAllObject()


@pytest.fixture(scope="function")
def delete_object_endpoint() -> DeleteObject:
    """
    Фикстура для создания экземпляра DeleteObject.
    :return: Объект для удаления сущности.
    """
    return DeleteObject()


@pytest.fixture(scope="function")
def update_object_endpoint() -> UpdateObject:
    """
    Фикстура для создания экземпляра UpdateObject.
    :return: Объект для изменения сущности.
    """
    return UpdateObject()


@pytest.fixture(scope="function")
def delete_objects(delete_object_endpoint):
    """
    Фикстура для очистки созданных сущностей.
    :param delete_object_endpoint: Объект для удаления сущности.
    :return: None.
    """
    ids_to_delete = []
    yield ids_to_delete
    delete_object_endpoint.delete_multiple_objects_by_id(ids_to_delete)


@pytest.fixture(scope="function")
def get_object_id(create_object_endpoint, delete_object_endpoint):
    """
    Фикстура для создания, а потом удаления сущности.
    :param create_object_endpoint: Объект для создания сущности.
    :param delete_object_endpoint: Объект для удаления сущности.
    :return: None.
    """
    create_body = create_entity_request()
    create_object_endpoint.new_object(create_body)
    id_object = create_object_endpoint.get_id()
    yield id_object
    delete_object_endpoint.delete_object_by_id(id_object)


@pytest.fixture(scope="function")
def create_object(create_object_endpoint):
    """
    Фикстура для создания сущности.
    :param create_object_endpoint: Объект для создания сущности.
    :return: None.
    """
    create_body = create_entity_request()
    create_object_endpoint.new_object(create_body)
    id_object = create_object_endpoint.get_id()
    yield id_object


@pytest.fixture(scope="function")
def get_multiple_ids_objects(create_object_endpoint, delete_object_endpoint):
    """
    Фикстура для создания, а потом удаления нескольких сущностей.
    :param create_object_endpoint: Объект для создания сущности.
    :param delete_object_endpoint: Объект для удаления сущности.
    :return: None.
    """
    random_number_of_objects = random.randint(2, 5)
    list_ids = []
    for i in range(random_number_of_objects):
        request = create_entity_request()
        create_object_endpoint.new_object(request)
        id_obj = create_object_endpoint.get_id()
        list_ids.append(id_obj)
    yield list_ids
    delete_object_endpoint.delete_multiple_objects_by_id(list_ids)
