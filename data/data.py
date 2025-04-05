"""
Модуль содержит ссылки, хэдеры и json ответы.
"""
URL_CREATE = 'http://localhost:8080/api/create'
URL_DELETE = 'http://localhost:8080/api/delete/{id}'
URL_GET = 'http://localhost:8080/api/get/{id}'
URL_GET_ALL = 'http://localhost:8080/api/getAll'
URL_UPDATE = 'http://localhost:8080/api/patch/{id}'
HEADER_WITH_BODY = {
            "Content-Type": "application/json",
            "accept": "text/plain"
        }
HEADER_DELETE = {
            "accept": "text/plain"
        }
HEADER_GET = {
            "accept": "application/json"
        }

RES_NO_OBJECT = {'error': 'no rows in result set'}
