"""
Модуль для тестирования работы точек доступа для управления сущностями.

Содержит функции для тестирования функционала создания, удаления, получения и изменения сущности.
"""
import allure
import pytest
from data.data_headers import RES_NO_OBJECT
from data.generate_request import create_entity_request


@allure.epic("Тестирование точек доступа для управления сущностями")
@allure.feature('Создание новой сущности')
@allure.story('Создание новой сущности с использованием POST-запроса')
@allure.id('TC-001')
@allure.description(
    'Тест-кейс проверяет создание новой сущности с использованием POST-запроса.'
)
@pytest.mark.api
@pytest.mark.usefixtures("delete_objects")
def test_create_object(create_object_endpoint, get_object_endpoint, delete_objects):
    """
    Тест для создания новой сущности.
    :param create_object_endpoint: Объект эндпоинта для создания сущности.
    :param get_object_endpoint: Объект эендпоинта для получения сущности.
    :param delete_objects: Постусловие для удаления созданных сущностей.
    :return: None.
    """
    create_body = create_entity_request()
    create_object_endpoint.new_object(create_body)
    assert create_object_endpoint.check_response_is_200(), \
        "Статус код ответа не равен 200"
    id_object = create_object_endpoint.get_id()
    delete_objects.append(id_object)
    get_object_endpoint.get_by_id(id_object)
    assert get_object_endpoint.check_id(id_object), \
        "Идентификатор из ответа не соответствует ожидаемому"
    assert get_object_endpoint.check_param_in_body_for_create(create_body), \
        "Параметры из ответа не соответствует ожидаемым"


@allure.epic("Тестирование точек доступа для управления сущностями")
@allure.feature('Удаление сущности')
@allure.story('Удаление сущности с использованием DELETE-запроса')
@allure.id('TC-002')
@allure.description(
    'Тест-кейс проверяет удаление сущности с использованием DELETE-запроса.'
)
@pytest.mark.api
@pytest.mark.usefixtures("create_object")
def test_delete_object(create_object, delete_object_endpoint, get_object_endpoint):
    """
    Тест для удаления сущности.
    :param create_object: Предусловие для создания сущности.
    :param delete_object_endpoint: Объект энпоинта для удаления сущности.
    :param get_object_endpoint: Объект эендпоинта для получения сущности.
    :return: None.
    """
    delete_object_endpoint.delete_object_by_id(create_object)
    assert delete_object_endpoint.check_response_is_204(), \
        "Статус код ответа не равен 204"
    get_object_endpoint.get_by_id_negative(create_object)
    assert get_object_endpoint.check_response_is_500(), \
        "Статус код ответа не равен 500"
    assert get_object_endpoint.check_param_in_body(RES_NO_OBJECT), \
        "Параметры из ответа не соответствует ожидаемым"


@allure.epic("Тестирование точек доступа для управления сущностями")
@allure.feature('Получение сущности')
@allure.story('Получение сущности с использованием GET-запроса')
@allure.id('TC-003')
@allure.description(
    'Тест-кейс проверяет получение сущности с использованием GET-запроса.'
)
@pytest.mark.api
@pytest.mark.usefixtures("get_object_id")
def test_get_object(get_object_id, get_object_endpoint):
    """
    Тесть для получения сущности.
    :param get_object_id: Пред- и постусловие для создания и удаления сущности.
    :param get_object_endpoint: Объект эендпоинта для получения сущности.
    :return: None.
    """
    get_object_endpoint.get_by_id(get_object_id)
    assert get_object_endpoint.check_response_is_200(), \
        "Статус код ответа не равен 200"
    assert get_object_endpoint.check_id(get_object_id), \
        "Идентификатор из ответа не соответствует ожидаемому"


@allure.epic("Тестирование точек доступа для управления сущностями")
@allure.feature('Получение всех сущностей')
@allure.story('Получение всех сущностей с использованием GET-запроса')
@allure.id('TC-004')
@allure.description(
    'Тест-кейс проверяет получение всех сущностей с использованием GET-запроса.'
)
@pytest.mark.api
@pytest.mark.usefixtures("get_multiple_ids_objects")
def test_get_all_objects(get_multiple_ids_objects, get_all_objects_endpoint):
    """
    Тест для получения всех сущностей.
    :param get_multiple_ids_objects: Пред- и постусловие
    для создания и удаления нескольких сущностей.
    :param get_all_objects_endpoint: Объект эендпоинта для получения всех сущностей.
    :return: None.
    """
    with allure.step('Получение id созданных сущностей'):
        ids_to_check = get_multiple_ids_objects
    get_all_objects_endpoint.get_all()
    assert get_all_objects_endpoint.check_response_is_200(), \
        "Статус код ответа не равен 200"
    assert get_all_objects_endpoint.check_ids_in_response(ids_to_check), \
        "Идентификаторы из ответа не содержат идентификаторы созданных сущностей"


@allure.epic("Тестирование точек доступа для управления сущностями")
@allure.feature('Обновление сущности')
@allure.story('Обновление сущности с использованием PATCH-запроса')
@allure.id('TC-005')
@allure.description(
    'Тест-кейс проверяет обновление сущности с использованием PATCH-запроса.'
)
@pytest.mark.api
@pytest.mark.usefixtures("get_object_id")
def test_update_object(get_object_id, update_object_endpoint, get_object_endpoint):
    """
    Тест для обновления сущности.
    :param get_object_id: Пред- и постусловие для создания и удаления сущности.
    :param update_object_endpoint: Объект эендпоинта для обновления сущности.
    :param get_object_endpoint: Объект эендпоинта для получения сущности.
    :return:
    """
    new_param_for_obj = create_entity_request()
    update_object_endpoint.update_object_by_id(get_object_id, new_param_for_obj)
    assert update_object_endpoint.check_response_is_204(), \
        "Статус код ответа не равен 204"
    get_object_endpoint.get_by_id(get_object_id)
    assert get_object_endpoint.check_id(get_object_id), \
        "Идентификатор из ответа не соответствует ожидаемому"
    assert get_object_endpoint.check_param_in_body_for_create(new_param_for_obj), \
        "Параметры из ответа не соответствует ожидаемым"
