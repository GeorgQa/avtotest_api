
from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient


class UpdateUserRequest(TypedDict):
    """
    Описание структуры запросов на обновление пользователя.
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class PrivateUserClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def get_user_me_api(self) -> Response:
        """
        Метод для получения текущего пользователя

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.get("/api/v1/users/me")

    def get_user_id(self, user_id: str) -> Response:
        """
        Метод для получения пользователя по user_id

        :param: user_id - Уникальный uuid пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.get(f"/api/v1/users/{user_id}")

    def update_user_id(self,user_id: str, request:dict) -> Response:
        """
        Метод для частичного обновления пользователя по user_id

        :param: user_id - Уникальный uuid пользователя
        :param request - Словарь с телом запроса для частичного обновления пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_id(self, user_id:UpdateUserRequest) -> Response:
        """
        Метод для удаления пользователя по user_id

        :param: user_id - Уникальный uuid пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.delete(f"/api/v1/users/{user_id}")


