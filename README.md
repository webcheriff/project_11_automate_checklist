# Проект 11

## Автоматизация чек-листа для поля "name" в запросе на создание набора в Яндекс Прилавке с помощью API Яндекс Прилавка.

Яндекс Прилавок это учебное web-приложение для практики работы с API, SQL.

- Язык приложения — JavaScript.
- Доступ к приложению по протоколу HTTP 1.1.
- Документация к приложению осуществляется с помощью модуля apidoc.
- Приложение использует базу данных. БД — PostgreSQL.

## Требования

- Для запуска тестов должны быть установлены пакеты pytest и requests.
- Запуск всех тестов выполняется командой pytest.

Markdown is a lightweight markup language based on the formatting conventions
that people naturally use in email.
As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Tech

Dillinger uses a number of open source projects to work properly:

- [AngularJS] - HTML enhanced for web apps!
- [Ace Editor] - awesome web-based text editor
- [markdown-it] - Markdown parser done right. Fast and easy to extend.
- [Twitter Bootstrap] - great UI boilerplate for modern web apps
- [node.js] - evented I/O for the backend
- [Express] - fast node.js network app framework [@tjholowaychuk]
- [Gulp] - the streaming build system
- [Breakdance](https://breakdance.github.io/breakdance/) - HTML
  to Markdown converter
- [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
on GitHub.

## Installation

Dillinger requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```

## Чек-лист проверок

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| № | Описание                                    | ОР                                                                                                                                            |
|---|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Допустимое количество символов (1):         | kit_body = {"name": "a" }. Код ответа — 201. В ответе поле name совпадает с полем name в запросе                                              |
| 2 | Допустимое количество символов (511):       | kit_body = { "name":"Тестовое значение для этой проверки будет ниже" }. Код ответа — 201. В ответе поле name совпадает с полем name в запросе 
| 3 | Количество символов меньше допустимого (0): 

kit_body = {
"name": ""
} Код ответа — 400
4 Количество символов больше допустимого (512):
kit_body = {
"name":"Тестовое значение для этой проверки будет ниже"
} Код ответа — 400
5 Разрешены английские буквы:
kit_body = {
"name": "QWErty"
} Код ответа — 201
В ответе поле name совпадает с полем name в запросе
6 Разрешены русские буквы:
kit_body = {
"name": "Мария"
} Код ответа — 201
В ответе поле name совпадает с полем name в запросе
7 Разрешены спецсимволы:
kit_body = {
"name": ""№%@","
} Код ответа — 201
В ответе поле name совпадает с полем name в запросе
8 Разрешены пробелы:
kit_body = {
"name": " Человек и КО "
} Код ответа — 201
В ответе поле name совпадает с полем name в запросе
9 Разрешены цифры:
kit_body = {
"name": "123"
} Код ответа — 201
В ответе поле name совпадает с полем name в запросе
10 Параметр не передан в запросе:
kit_body = {
} Код ответа — 400
11 Передан другой тип параметра (число):
kit_body = {
"name": 123
} Код ответа — 400

## Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

## Docker

Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd dillinger
docker build -t <youruser>/dillinger:${package.json.version} .
```

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## Создатель

Ростислав Черепанов, 8 когорта