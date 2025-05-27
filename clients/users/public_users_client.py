from httpx import Response
from typing_extensions import TypedDict

from clients.api_client import APIClient

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
    Класс унаследованный от APIClient
    """

    def create_user_api(self, request:dict) -> Response :
        """
        Метод для создания пользователя

        :param request: Словарь с данными для создания пользователя
        :return Response: Ответ от севера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)
