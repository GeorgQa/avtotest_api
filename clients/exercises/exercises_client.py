import json

import allure
from httpx import Response

from clients.api_client import APIClient
from clients.api_coverage import tracker
from clients.exercises.exercises_schema import (CreateExerciseRequestSchema,
                                                CreateExerciseResponseSchema,
                                                GetExerciseResponseSchema,
                                                GetExercisesQuerySchema,
                                                UpdateExerciseRequestSchema,
                                                UpdateExerciseResponseSchema)
from clients.private_http_builder import (AuthenticationUserSchema,
                                          get_private_http_client)
from tools.routes import APIRoutes


class ExercisesClient(APIClient):
    """
    Клиент для работы с api /api/v1/exercises.
    """

    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}")
    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка заданий.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=APIRoutes.EXERCISES, params=query.model_dump(by_alias=True))

    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}")
    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод для создания задания

        :param request: Словарь  с структурой для создания задания
        :return: Ответ от сервера в виде объекта  httpx.Response
        """
        return self.post(url=APIRoutes.EXERCISES, json=request.model_dump(by_alias=True))

    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    @allure.step("Get exercise by id {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания.

        :param exercise_id: Уникальный Идентификатор задания
        :return:Ответ от сервера в виде объекта  httpx.Response
        """
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    @allure.step("Update exercise")
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
            f"{APIRoutes.EXERCISES}/{exercise_id}", json=request.model_dump(by_alias=True)
        )

    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    @allure.step("Delete exercise")
    def delete_exercises_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления упражнения

        :param exercise_id: Уникальный Идентификатор задания
        :return:Ответ от сервера в виде объекта  httpx.Response
        """
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")

    def create_exercise(
        self, request: CreateExerciseRequestSchema
    ) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(
        self, query: GetExercisesQuerySchema
    ) -> GetExerciseResponseSchema:
        response = self.get_exercises_api(query)
        return GetExerciseResponseSchema.model_validate_json(response.text)

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
