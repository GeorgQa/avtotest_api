from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema,
)
from fixtures.courses import CoursesFixture
from fixtures.exercises import ExercisesFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import (
    assert_create_exercise_response,
    assert_exercise,
    assert_get_exercise_response, assert_update_exercise_response,
)
from tools.assertions.sсhema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(
        self,
        exercises_client: ExercisesClient,
        function_exercise: ExercisesFixture,
        function_course: CoursesFixture,
    ):
        create_request = CreateExerciseRequestSchema(
            courseId=function_course.response.course.id
        )
        response = exercises_client.create_exercise_api(request=create_request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        # Проверки
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(response_data, create_request)
        # Проверяем соответствие ответа JSON схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercise(
        self, exercises_client: ExercisesClient, function_exercise: ExercisesFixture
    ):
        exercise_id = function_exercise.response.exercise.id
        response_get = exercises_client.get_exercise_api(exercise_id=exercise_id)
        response_data = GetExerciseResponseSchema.model_validate_json(response_get.text)

        assert_status_code(response_get.status_code, HTTPStatus.OK)
        assert_exercise(function_exercise.response.exercise, response_data.exercise)
        assert_get_exercise_response(function_exercise.response, response_data)
        validate_json_schema(response_get.json(), response_data.model_json_schema())

    def test_update_exercise(self, exercises_client:ExercisesClient, function_exercise:ExercisesFixture):
        request_update = UpdateExerciseRequestSchema(title="Updated title", maxScore=111,
                                                     description='updated desc')
        exercises_id = function_exercise.response.exercise.id
        response_update= exercises_client.update_exercises_api(request=request_update,exercise_id=exercises_id)
        response_update_data = UpdateExerciseResponseSchema.model_validate_json(response_update.text)

        assert_status_code(response_update.status_code, HTTPStatus.OK)
        assert_update_exercise_response(response_update_data, request_update)
        validate_json_schema(response_update.json(), response_update_data.model_json_schema())

