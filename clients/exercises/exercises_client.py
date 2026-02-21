import json

from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import (CreateExerciseRequestSchema,
                                                CreateExerciseResponseSchema,
                                                GetExerciseResponseSchema,
                                                GetExercisesQuerySchema,
                                                UpdateExerciseRequestSchema,
                                                UpdateExerciseResponseSchema)
from clients.private_http_builder import (AuthenticationUserSchema,
                                          get_private_http_client)


class ExercisesClient(APIClient):
    """
    Клиент для работы с api /api/v1/exercises.
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка заданий.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод для создания задания

        :param request: Словарь  с структурой для создания задания
        :return: Ответ от сервера в виде объекта  httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания.

        :param exercise_id: Уникальный Идентификатор задания
        :return:Ответ от сервера в виде объекта  httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercises_api(
        self, exercise_id: str, request: UpdateExerciseRequestSchema
    ) -> Response:
        """
        Метод для обновления курса

        :param exercise_id: Уникальный Идентификатор задания
        :param request: Словарь для обновления упражнения
        :return:Ответ от сервера в виде объекта  httpx.Response
        """
        return self.patch(
            f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True)
        )

    def delete_exercises_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления упражнения

        :param exercise_id: Уникальный Идентификатор задания
        :return:Ответ от сервера в виде объекта  httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def create_exercise(
        self, request: CreateExerciseRequestSchema
    ) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.create_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(
        self, query: GetExercisesQuerySchema
    ) -> GetExerciseResponseSchema:
        response = self.create_exercise_api(query)
        return GetExerciseResponseSchema.exercises_validate_json(response.text)

    def update_exercise(
        self, request_id: UpdateExerciseRequestSchema, exercise_id: str
    ) -> UpdateExerciseResponseSchema:
        response = self.update_exercises_api(
            request=request_id, exercise_id=exercise_id
        )
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


# Добавляем builder для ExercisesClient
def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """ "
    Функция создает экземпляр класса ExercisesClient с уже настроенным HTTP клиентом

    :return: Готовый к использованию клиент ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user))
