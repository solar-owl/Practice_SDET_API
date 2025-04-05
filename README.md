# Практикум SDET: задание API
Проект содержит API тесты.

## Тесты
1. Создание сущности: POST /api/create
2. Удаление сущности: DELETE /api/delete/{id}
3. Получение сущности: GET /api/get/{id}
4. Получение всех сущностей: GET /api/getAll
5. Обновление сущности: PATCH /api/patch/{id}.

## Технологии и инструменты
* Python 3.10
* requests
* Pytest
* pytest-xdist
* pydantic
* Allure
* CI/CD с GitHub Actions
* GitHub Pages

## Работа с проектом локально (Windows)
1. Установить python 3.10
2. Склонировать и развернуть [проект](https://github.com/bondarenkokate73/simbirsoft_sdet_project) ( инструкция в репозитории) 
3. Склонировать проект на компьютер через терминал Git Bash на Windows
git clone 
4. Создать виртуальное окружение
```
python -m venv venv
```
4. Установить необходимые пакеты
```
pip install -r requirements.txt
```
5. Запуск тестов (в 3 потока)
```
pytest -v
```
6. Генерация отчетов Allure (необходимо, чтобы был скачан Allure)
```
pytest -v -s --alluredir reports
allure serve reports
```

## Запуск автотестов в GitHub Actions
1. В вкладке **Actions** перейти в workflow: **Automated API tests**
2. Нажать **Run workflow**
3. В окне в выпадающем списке выбрать тест, который нужно запустить, или все (автоматически выбран запуск всех автотестов)
4. Нажать на кнопку **Run workflow**

## Allure Reports
Allure отчеты доcтупны по ссылке: https://solar-owl.github.io/Practice_SDET_API/
