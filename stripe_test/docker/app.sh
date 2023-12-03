#!/bin/bash

# Выполнение миграций
python manage.py makemigrations
python manage.py migrate

cd stripe_test

# Запуск приложения
python manage.py run server --host 0.0.0.0 --port 8000
