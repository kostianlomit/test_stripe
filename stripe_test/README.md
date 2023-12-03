# Сервис Django + Stripe API

stripe_test, который позволяет обращаться к API stripe, получать сессию для оплаты выбранного товара(item). 

## Используемый стек

- [Django](https://www.djangoproject.com/) это веб-фреймворк Python высокого уровня, который способствует быстрой разработке и чистому, прагматичному дизайну, веб-фреймворк для создания API.
- [PostgreSQL](https://www.postgresql.org) — свободная объектно-реляционная система управления базами данных.
- [TestCase](https://docs.djangoproject.com/en/4.2/topics/testing/overview/) Модульные тесты Django используют модуль стандартной библиотеки Python: unittest
- [Docker](https://docs.docker.com/get-started/overview/) открытая платформа для разработки, доставки и запуска приложений.
- [Docker compose](https://docs.docker.com/compose/) инструмент для определения и запуска многоконтейнерных приложений Docker. 


## Установка 
ВНИМАНИЕ! Для проведения установки необходимо, чтобы пользователь от которого выполняются действия находился в группе `sudo`
### Порядок действий:
1. Установите Docker по [инструкции с сайта Docker](https://docs.docker.com/engine/install/ubuntu/)
2. Установите ”make”
    ```bash
    sudo apt install make
    ```
2. Склонируйте репозиторий на сервер, например, в директорию: `/home/<user>/`:

    ```bash
    sudo git clone https://github.com/AndMartyan/secret_marks.git
    ```
3. Перейдите в каталог с сервисом:

    ```bash
    cd stripe_test
    ```
4. При необходимости измените параметры в `Makefile` и `docker-compose.yml`
5. Отредактируйте файл `.env-non-dev`
   ```bash
   DB_HOST=db #хост продакшн-базы 
   DB_PORT=5432 #порт продакшн-базы 
   DB_NAME=postgres #название продакшн-базы 
   DB_USER=postgres #имя пользователя продакшн-базы 
   DB_PASS=postgres #пароль пользователя продакшн-базы 
   
   POSTGRES_DB=postgres
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   
   SECRET_KEY_DJ=secret_key
   SECRET_KEY_API=secret_api
    ```
6. Выполните команду:

    ```bash
    sudo make container
    ```

7. Запустите сервис с помощью Docker Compose:

    ```bash
    sudo docker compose -p stripe_test \
                -f docker-compose.yml \
                up -d
    ```
8. Проверьте работоспособность сервиса в соответствии с настройками

## Остановка сервиса

Для остановки сервиса выполните следующую команду:

   ```bash
   sudo docker compose -p stripe_test  stop
   ```

## Работа сервиса
Сервис имеет два эндпоинта:

- `GET /buy/<int:id>` выполняется запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса

  Пример отправки HTTP-запроса:
  ```bash
  curl -X 'GET' \
  'http://0.0.0.0:8000/buy/<int:id>' \
  {"session_id": "cs_test_a1EkEv9KZGnZfd7ECeRdnEITa3M5sVDqcgKNVPto8QwAUXxXdnlmjChh6f"}
  ```
  
- `GET /item/<int:id>` получает простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy роисходит запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходит редирект на Checkout форму.
  Пример отправки HTTP-запроса:
  ```bash
  curl -X 'GET' \
  'http://0.0.0.0:8000/item/<int:id>' \
  
<!DOCTYPE html>
<html>
<head>
    <title>Item Page</title>
    <script src="https://js.stripe.com/v3/"></script>
</head>
<body>
    <h1>Item Details</h1>
    <p>Item Name: pawns</p>
    <p>Item Price: 111</p>
    <button onclick="buyItem(1)">Buy</button>

Внести данные о товаре можно в Admin_panel django
'http://0.0.0.0:8000/admin/'
  ```
## Тестирование
Выполните команду 
```python3
sudo docker exec stripe_test ./manage.py test
```


## Версия

Django - 4.2.7