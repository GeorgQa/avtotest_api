

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.authentication.authentication_schema import  LoginResponseSchema,LoginRequestSchema, RefreshRequestSchema


class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request.model_dump(by_alias=True))

    def refresh_api(self, request:RefreshRequestSchema) -> Response:
        """
        Метод обновляет токен авторизации

        :param request: Словарь с refreshToken
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)

        if response.status_code != 200:
            # Логирование ошибки для отладки
            raise ValueError(
                f"Login failed with status code {response.status_code} and response: {response.text}"
            )
        #валидация
        return LoginResponseSchema.model_validate_json(response.text)

def get_authentication_client() -> AuthenticationClient:
    """
    Функция которая создает экзмепляр AuthenticationClient c уже использованным HTTP- клиентом

    :return: Готовый к использованию  AuthenticationClient
    """
    return AuthenticationClient(client= get_public_http_client())

# client = get_authentication_client()
# response = client.login()