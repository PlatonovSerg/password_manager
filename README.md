# Менеджер Паролей

Этот проект представляет собой API менеджера паролей, разработанный на Django. Он позволяет безопасно хранить и получать пароли для различных сервисов. Проект использует Docker и Docker Compose для контейнеризации.

## Особенности

- Хранение паролей в зашифрованном формате
- Получение паролей по имени сервиса
- Поиск паролей по части имени сервиса

## Требования

- Docker
- Docker Compose

## Установка

1. **Клонируйте репозиторий:**

```sh {"id":"01J1CT5384TTKKVX1X2TT8BC7K"}
git clone <URL_репозитория>
cd password_manager
```

2. **Создайте файл `.env` и добавьте необходимые переменные окружения:**

```env {"id":"01J1CT5384TTKKVX1X2WEHAWP5"}
ENCRIPTION_KEY  = b'UlvvxLyWa85c2QYD0r266yzDlqMa3LFUSLpY1TZDB-A='
SECRET_KEY = "django-insecure-52_dgv=u5nd8yv3&=w_ww^n7nuw2r%$ls03i&w9&x99rn&%=%o"
SQL_DATABASE = 'db'
SQL_USER = 'postgres'
SQL_PASSWORD = 'postgres'
SQL_HOST = 'localhost'
SQL_PORT = '5432'

DJANGO_SUPERUSER_USERNAME = 'admin'
DJANGO_SUPERUSER_EMAIL = 'admin@yandex.ru'
DJANGO_SUPERUSER_PASSWORD = 'my_new_password'
```

3. **Запустите Docker Compose:**

```sh {"id":"01J1CT5384TTKKVX1X2X5HJ7AG"}
docker-compose up --build -t
```

4. **Создайте суперпользователя:**

```sh {"id":"01J1CT8M7BR6VYE2VW7BQHSDE5"}
docker-compose exec web /bin/bash
# Далее в терминале создайте суперпользователя
python3 manage.py createsuperuser
```

## Использование

### Создание пароля

Для создания или обновления пароля используйте следующий запрос:

- **URL:** `POST /api/password/`

- **Тело запроса:**

```json {"id":"01J1CT5384TTKKVX1X2ZY0J5H0"}
{
    "service_name": "example_service",
    "password": "example_password"
}
```

### Получение пароля по имени сервиса

Для получения пароля по имени сервиса используйте следующий запрос:

- __URL:__ `GET /api/password/<service_name>/`

- **Пример запроса:**

```sh {"id":"01J1CT5384TTKKVX1X31Z3Z0AP"}
GET http://localhost:8000/api/password/example_service/
```

### Поиск паролей по части имени сервиса

Для поиска паролей по части имени сервиса используйте следующий запрос:

- __URL:__ `GET /api/password/?service_name=<part_of_service_name>`

- **Пример запроса:**

```sh {"id":"01J1CT5384TTKKVX1X340626BV"}
GET http://localhost:8000/api/password/?service_name=example
```