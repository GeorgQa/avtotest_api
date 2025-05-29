from typing import TypedDict

from clients.api_client import APIClient
from httpx import Response

class QueryParamsGetExercises(TypedDict):
    """
    Описание структуры для запроса на получения списка упраждений в рамках одного курса
    """
    courseId: str

class RequestCreateExercises(TypedDict):
    """
    Описнаие структуры для запроса на создание курса
    """
    title : str
    courseId : str
    maxScore : int
    minScore : int
    orderIndex : int
    description : str
    estimatedTime : str

class RequestUpdateExercises(TypedDict):
    """
    Описнаие структуры для описнания структуры на обновление курса
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
    def get_exercises_for_coureses(self, query:QueryParamsGetExercises) -> Response:
        """
        Метод для получения списка упражнений в одном курсе

        :param query: query params создаеший id курса
        :return: Ответ от сервера в виде объекта  httpx.Response
        """
        return self.get("/api/v1/exercises", params= query)

    def create_exercises(self, request:RequestCreateExercises) -> Response:
        """
        Метод для создания упражнения

        :param request: Словарь  с структурой для создания упраждениния
        :return: Ответ от сервера в виде объекта  httpx.Response
        """
        return  self.post("/api/v1/exercises", json= request)

    def get_exercises(self, exercise_id: str) -> Response:
        """
        Метод для получения курса по uuid

        :param exercise_id: Уникальный индификатор упражнения
        :return:Ответ от сервера в виде объекта  httpx.Response
        """

        return  self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercises(self, exercise_id: str, request:RequestUpdateExercises) -> Response:
        """
        Метод для обновления курса

        :param exercise_id: Уникальный индификатор курса
        :param request: Словарь для обновления упражнения
        :return:Ответ от сервера в виде объекта  httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json= request)

    def delete_exercises(self, exercise_id: str) -> Response:
        """
        Метод для удаления упражнения

        :param exercise_id: Уникальный индификатор курса
        :return:Ответ от сервера в виде объекта  httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")