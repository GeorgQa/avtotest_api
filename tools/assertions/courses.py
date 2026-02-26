from api_client_create_course import create_course_response
from clients.courses.course_schema import (
    CourseSchema,
    CreateCourseResponseSchema,
    GetCoursesResponseSchema,
    GetIDCoursesResponseSchema,
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema, CreateCourseRequestSchema,
)
from fixtures.courses import CoursesFixture
from tools.assertions.base import assert_equal
from tools.assertions.files import assert_files
from tools.assertions.users import assert_user


def assert_update_course_response(
    request: UpdateCourseRequestSchema, response: UpdateCourseResponseSchema
):
    """
    Проверяем, что обьект на нобновление курса соответсвует данным из запроса.

    :param request: Исходный запрос на обновление круса
    :param response: Ответ API с обноленными данными курса
    :raise AssertionError: Если хоть одно поле не совпало
    """
    if request.title is not None:
        assert_equal(response.course.title, request.title, "title")

    if request.max_score is not None:
        assert_equal(response.course.max_score, request.max_score, "max_score")

    if request.min_score is not None:
        assert_equal(response.course.min_score, request.min_score, "min_score")

    if request.description is not None:
        assert_equal(response.course.description, request.description, "description")

    if request.estimated_time is not None:
        assert_equal(
            response.course.estimated_time, request.estimated_time, "estimated_time"
        )


def assert_get_id_course_response(
    request: UpdateCourseResponseSchema, response: GetIDCoursesResponseSchema
):
    """
    Проверка ответа запроса на получение данных о курсе по его ID.

    :param request: Принимает ответ запроса на изменение данных курса
    :param response: Ответ запроса на получение данных по ID
    :return: Если хоть одно поле не совпало
    """
    assert_equal(response.course.title, request.course.title, "title")
    assert_equal(response.course.max_score, request.course.max_score, "max_score")
    assert_equal(response.course.min_score, request.course.min_score, "min_score")
    assert_equal(response.course.description, request.course.description, "description")
    assert_equal(
        response.course.estimated_time, request.course.estimated_time, "min_score"
    )


def asset_course(
    actual: CourseSchema, expected: CourseSchema
):
    """
    Проверяет , что фактиечские данные курса соответствуют ожидаемым.

    :param actual: Фактические значения полей
    :param expectted: Значения которые должны быть в результате выполнения тестов
    :raise AsserionError: Если хоть одно поле не совпалo
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max score")
    assert_equal(actual.min_score, expected.min_score, "min score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimate time")

    assert_files(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)


def assert_get_courses_response(
    get_courses_response: GetCoursesResponseSchema,
    create_course_responses: list[CreateCourseResponseSchema],
):
    """
    Проверяет, что список курсов из ответа соответствует созданным курсам.

    :param get_courses_response: Ответ API при запросе списка курсов.
    :param create_course_responses: Список ответов API при создании курсов.
    """
    # Сравниваем каждый курс по отдельности
    for index, expected_response in enumerate(create_course_responses):
        actual_course = get_courses_response.courses[index]
        expected_course = expected_response.course
        asset_course(actual_course, expected_course)

def assert_create_course_response(actual: CreateCourseResponseSchema, expected: CreateCourseRequestSchema):
    """
    Проверяет что данные тела запроса соответсвуют данным ответа

    :param create_course_request:  Запрос создания нового курса
    :param cretae_curce_resposne:   Ответ API при создание курса
    :raise AsserionError: Если хоть одно поле не совпалo
    """
    assert_equal(actual.course.title, expected.title, "title")
    assert_equal(actual.course.max_score, expected.max_score, "max_score")
    assert_equal(actual.course.min_score, expected.min_score, "min_score")
    assert_equal(actual.course.description, expected.description, "description")
    assert_equal(actual.course.estimated_time, expected.estimated_time, "estimate time")

    assert_equal(actual.course.preview_file.id, expected.preview_file_id, "preview_file_id")
    assert_equal(actual.course.created_by_user.id, expected.created_by_user_id, "user_id")