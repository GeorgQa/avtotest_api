from typing import TypedDict

from clients.api_client import APIClient
from httpx import Response

from clients.private_http_builder import AuthenticationUserDict, get_prived_http_client


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры для запроса на создание задания
    """
    title : str
    courseId : str
    maxScore : int
    minScore : int
    orderIndex : int
    description : str
    estimatedTime : str

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    title : str
    maxScore : int
    minScore : int
    orderIndex : int
    description : str
    estimatedTime : str

class  ExercisesClient(APIClient):
    """
    Клиент для работы с api /api/v1/exercises.
    """
    def get_exercises_api(self, query:GetExercisesQueryDict) -> Response:
        """
        Метод получения списка заданий.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params= query)

    def create_exercise_api(self, request:CreateExerciseRequestDict) -> Response:
        """
        Метод для создания упражнения

        :param request: Словарь  с структурой для создания упраждениния
        :return: Ответ от сервера в виде объекта  httpx.Response
        """
        return  self.post("/api/v1/exercises", json= request)

    def get_exercises(self, exercise_id: str) -> Response:
        """
        Метод получения задания.

        :param exercise_id: Уникальный Идентификатор задания
        :return:Ответ от сервера в виде объекта  httpx.Response
        """

        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercises(self, exercise_id: str, request:UpdateExerciseRequestDict) -> Response:
        """
        Метод для обновления курса

        :param exercise_id: Уникальный Идентификатор задания
        :param request: Словарь для обновления упражнения
        :return:Ответ от сервера в виде объекта  httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json= request)

    def delete_exercises(self, exercise_id: str) -> Response:
        """
        Метод для удаления упражнения

        :param exercise_id: Уникальный Идентификатор задания
        :return:Ответ от сервера в виде объекта  httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

# Добавляем builder для ExercisesClient
def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """"
    Функция создает экземпляр класса ExercisesClient с уже настроенным HTTP клиентом

    :return: Готовый к использованию клиент ExercisesClient
    """
    return ExercisesClient(client=get_prived_http_client(user))