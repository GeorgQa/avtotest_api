from httpx import Response
from typing_extensions import TypedDict

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Класс унаследованный от APIClient для работы с api не требующими access_token
    """

    def create_user_api(self, request:CreateUserRequestDict) -> Response :
        """
        Метод для создания пользователя

        :param request: Словарь с данными для создания пользователя
        :return Response: Ответ от севера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)


def get_public_users_client() -> PublicUsersClient:
    """
    Функция которая создает экзеипляр класса PublicUsersClient с дефолтными настройками

    :return: Возвращает клиент готовый к работе
    """
    return PublicUsersClient(client=get_public_http_client())

