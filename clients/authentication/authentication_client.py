from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient

class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аунтификацию.
    """
    email: str
    password: str

class RefreshRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления токена.
    """
    refreshToken: str


class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    def login_api(self, request: dict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request:RefreshRequestDict) -> Response:
        """
        Метод обнояет токен авторизации

        :param request: Словарь с refreshToken
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)