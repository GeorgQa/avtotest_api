from http import HTTPStatus

import pytest

from clients.courses.course_schema import (
    GetCoursesQuerySchema,
    GetCoursesResponseSchema,
    GetIDCoursesResponseSchema,
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema,
)
from clients.courses.courses_client import CoursesClient
from fixtures.courses import CoursesFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import (
    assert_get_courses_response,
    assert_get_id_course_response,
    assert_update_course_response,
)
from tools.assertions.sсhema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_update_course(
        self, courses_client: CoursesClient, function_course: CoursesFixture
    ):
        # Создаём запрос с только теми полями, которые хотим обновить
        request = UpdateCourseRequestSchema(title="New_title")
        # Отправляем запрос на обновление курса
        response = courses_client.update_course_api(
            request=request, course_id=function_course.response.course.id
        )
        # Преобразуем ответ в объект UpdateCourseResponseSchema, а не UpdateCourseRequestSchema
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        # Проверки
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request=request, response=response_data)

        # Валидируем Json-схему
        validate_json_schema(response.json(), response_data.model_json_schema())
        # Отправляем GET-запрос для проверки обновления
        response_get = courses_client.get_course_api(
            course_id=function_course.response.course.id
        )
        response_data_get = GetIDCoursesResponseSchema.model_validate_json(
            response_get.text
        )

        # Прооверки
        assert_status_code(response_get.status_code, HTTPStatus.OK)

        assert_get_id_course_response(response=response_data, request=response_data_get)

    def test_get_courses(
        self,
        courses_client: CoursesClient,
        function_course: CoursesFixture,
        function_user: UserFixture,
    ):
        query_params = GetCoursesQuerySchema(userId=function_user.response.user.id)
        response = courses_client.get_courses_api(query=query_params)
        # Десериализуем JSON ответ в Pydantic модель
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        # Проверяем статус код
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что список курсов совпадает с ранее созданным
        assert_get_courses_response(response_data, [function_course.response])

        # Проверяем соответствие Json ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())
