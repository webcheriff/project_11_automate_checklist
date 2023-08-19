# Проект 11

## Автоматизация чек-листа для поля "name" в запросе на создание набора в Яндекс Прилавке с помощью API Яндекс Прилавка.

Яндекс Прилавок это учебное web-приложение для практики работы с API, SQL.

- Язык приложения — JavaScript.
- Доступ к приложению по протоколу HTTP 1.1.
- Документация к приложению осуществляется с помощью модуля apidoc.
- Приложение использует базу данных — PostgreSQL.

### Требования

- Для запуска тестов должны быть установлены пакеты `pytest` и `requests`.
- Запуск всех тестов выполняется командой `pytest`.

### Чек-лист проверок

| №  | Описание                                                                                                   | ОР                                                                            |
|----|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| 1  | Допустимое количество символов (1):`kit_body = {"name": "a" }`                                             | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 2  | Допустимое количество символов (511): [Тестовое значение](#тестовые_значения_для_проверок_№2_и_№4)         | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 3  | Количество символов меньше допустимого (0):`kit_body = { "name": "" }`                                     | <br/>Код ответа — 400                                                         |
| 4  | Количество символов больше допустимого (512): [Тестовое значение](#тестовые_значения_для_проверок_№2_и_№4) | <br/>Код ответа — 400                                                         |
| 5  | Разрешены английские буквы:`kit_body = {"name": "QWErty"}`                                                 | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 6  | Разрешены русские буквы:`kit_body = {"name": "Мария"}`                                                     | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 7  | Разрешены спецсимволы:`kit_body = {"name": ""№%@","}`                                                      | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 8  | Разрешены пробелы:`kit_body = {"name": " Человек и КО "}`                                                  | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 9  | Разрешены цифры:`kit_body = {"name": "123"}`                                                               | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 10 | Параметр не передан в запросе:`kit_body = {}`                                                              | <br/>Код ответа — 400                                                         |
| 11 | Передан другой тип параметра (число):`kit_body = {"name": 123}`                                            | <br/>Код ответа — 400                                                         |

#### Тестовые значения для проверок №2 и №4
Допустимое количество символов (511)
```py
kit_body = {"name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
```
Количество символов больше допустимого (512)
```py
kit_body = {"name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
```

### Шаги выполнения проекта

1. Написан запрос на создание нового пользователя и сохранение токена авторизации authToken.
2. Написан запрос на создание личного набора для этого пользователя. Учтена передача заголовка Authorization.
3. Написаны функции для проверки позитивных и негативных сценариев чек-листа.

### Стек для выполнения проекта:

#### Приложения:

* PyCharm
* GitHub

#### Фреймворки:

* requests
* pytest

## Создатель

Ростислав Черепанов, 8 когорта