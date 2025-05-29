from  httpx import Client

from clients.authentication.authentication_client import get_authentication_client, LoginRequestDict

from typing import TypedDict

# Структура данных пользователя для авторизации
class AuthenticationUserDict(TypedDict):

    email: str
    password: str

# Создаем private builder
def get_prived_http_client(user: AuthenticationUserDict) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authentication_client =get_authentication_client()

    login_request = LoginRequestDict(email=f"{user['email']}", password= f"{user['password']}")
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"{login_response['token']['accessToken']}"}
    )