import json
import sys

import httpx

params_for_login = {
    "email": "test_test@yandex.ru",
    "password": "qwerty12345"
}

try:
    response_login = httpx.post("http://localhost:8000/api/v1/authentication/login", json=params_for_login)
    json_response_login = response_login.json()
    access_token = json_response_login['token']['accessToken']
    print(f"Из запроса получил access_token: {access_token}")
    print(f"Статус код: {response_login.status_code}")
    print(f"Статус код: {response_login.json()}")
except httpx.ConnectError as e:
    print(f"Подключение с сервером не установленно")
    print(e)
    sys.exit()
except httpx.RequestError as e:
    print(f"Запрос вернулся с ошибкой статус код: {e.status_code}")
    print(f"Запрос вернулся с ошибкой: {e.headers}")
    print(f"Запрос вернулся с ошибкой: {e.json()}")
    sys.exit()


try:
    headers_for_requests = {"Authorization": f"Bearer {access_token}"}
    response_user_me = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers_for_requests)
    print(f"Выводим успешный статус код: {response_user_me.status_code}")
except httpx.HTTPStatusError as e:
    print(f"В запросе возникла ошибка:{e.status_code}")
    sys.exit()
except httpx.RequestError as e:
    print(f"Возникла ошибка при обработке данных пользователя {e}")
