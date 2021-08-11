Foodgram

Описание

Сайт Foodgram позволяет создавать и публиковать кулинарные рецепты,
общаться между собой, а также составлять списки продуктов

Алгоритм регистрации пользователей:

Регистрация проходит на сайте, по форме регистрации

Установка

Проект собран в Docker 20.10.06 и содержит четыре образа:

backend - образ бэка проекта
frontend - образ фронта проекта
postgres - образ базы данных PostgreSQL v 12.04
nginx - образ web сервера nginx
Команда клонирования репозитория:

git clone https://github.com/Sten129/foodgram-project-react

Запуск проекта:
Установите Докер
Выполните команду:
docker pull Sten129/foodgram-project-react :latest


Первоначальная настройка Django:
- docker-compose exec web python manage.py migrate --noinput
- docker-compose exec web python manage.py collectstatic --no-input
Создание суперпользователя:

- docker-compose exec web python manage.py createsuperuser
Заполнение .env:

Чтобы добавить переменную в .env необходимо открыть файл .env в корневой директории проекта и поместить туда переменную в формате имя_переменной=значение. Пример .env файла:

DB_ENGINE=my_db DB_NAME=db_name POSTGRES_USER=foodgram POSTGRES_PASSWORD=Gufochka1 DB_HOST=localhost DB_PORT=5432

Автор:

Дмитрий Грицай.
Задание было выполнено в рамках курса от Yandex Praktikum бэкенд разработчик.

Workflow badge:

https://github.com/pavelkhanoff/foodgram-project-react/actions/workflows/main.yml/badge.svg

Server address:

130.193.52.127

Superuser pass&email:

email: admin@admin.ru pass: admin
