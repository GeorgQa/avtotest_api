
from typing import TypedDict

from clients.api_client import APIClient
from httpx import Response

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client



class Exercise(TypedDict):
    """
    Описание структуры задания
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int | None
    description: str
    estimatedTime: str

class GetExercisesQueryDict(TypedDict):
    """
    Описание стуктуры для запроса на получение списка зданий
    """
    courseId: str

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на получение списка заданий.
    """
    exercises:list[Exercise]

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры для запроса на создание задания
    """
    title : str
    courseId : str
    maxScore : int
    minScore : int
    orderIndex : int | None
    description : str
    estimatedTime : str

class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры для ответа на создание задания
    """
    exercise:Exercise

class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры для ответа на получение одного задания
    """
    exercise: Exercise

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    courseId: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на обновление задания
    """
    exercise: Exercise

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
        Метод для создания задания

        :param request: Словарь  с структурой для создания задания
        :return: Ответ от сервера в виде объекта  httpx.Response
        """
        return  self.post("/api/v1/exercises", json= request)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания.

        :param exercise_id: Уникальный Идентификатор задания
        :return:Ответ от сервера в виде объекта  httpx.Response
        """

        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercises_api(self, exercise_id: str, request:UpdateExerciseRequestDict) -> Response:
        """
        Метод для обновления курса

        :param exercise_id: Уникальный Идентификатор задания
        :param request: Словарь для обновления упражнения
        :return:Ответ от сервера в виде объекта  httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json= request)

    def delete_exercises_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления упражнения

        :param exercise_id: Уникальный Идентификатор задания
        :return:Ответ от сервера в виде объекта  httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def create_exercise(self, request:CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.create_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query:GetExercisesQueryDict ) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(query)
        return response.json()

    def update_exercise(self, request_id:UpdateExerciseRequestDict, exercise_id: str) -> UpdateExerciseResponseDict:
        response = self.update_exercises_api(request=request_id, exercise_id=exercise_id)
        return response.json()

# Добавляем builder для ExercisesClient
def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """"
    Функция создает экземпляр класса ExercisesClient с уже настроенным HTTP клиентом

    :return: Готовый к использованию клиент ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user))