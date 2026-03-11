import allure

from clients.error_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import (CreateExerciseRequestSchema,
                                                CreateExerciseResponseSchema,
                                                ExerciseSchema,
                                                GetExerciseResponseSchema,
                                                GetExercisesResponseSchema,
                                                UpdateExerciseRequestSchema,
                                                UpdateExerciseResponseSchema)
from tools.assertions.base import assert_equal
from tools.assertions.courses import asset_course
from tools.assertions.errors import assert_internal_error_response
from tools.loger import get_logger

logger = get_logger("EXERCISE_ASSERTIONS")

@allure.step("Check create exercise response")
def assert_create_exercise_response(
    actual: CreateExerciseResponseSchema, expected: CreateExerciseRequestSchema
):
    """
    Проверяет, что ответ на создание задания соответствует запросу.

    :param actual: Ответ API при создании задания
    :param expected: Запрос на создание задания
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create exercise response")

    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.course_id, expected.course_id, "course_id")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(
        actual.exercise.estimated_time, expected.estimated_time, "estimated_time"
    )

@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что данные упражнения соответствуют ожидаемым.

    :param actual: Фактические данные упражнения
    :param expected: Ожидаемые данные упражнения
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check exercise")
    assert_equal(actual.id, expected.id, " exersice ID")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max score")
    assert_equal(actual.min_score, expected.min_score, "min score")
    assert_equal(actual.order_index, expected.order_index, "order index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimate time")

@allure.step("Check get exercise response")
def assert_get_exercise_response(
    actual: GetExerciseResponseSchema, expected: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение упражнения соответствует данным создания.

    :param actual: Ответ API при получении упражнения
    :param expected: Ответ API при создании упражнения
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check get exercise response")

    assert_equal(actual.exercise.id, expected.exercise.id, "exercise id")
    assert_equal(actual.exercise.course_id, expected.exercise.course_id, "course_id")
    assert_equal(actual.exercise.max_score, expected.exercise.max_score, "max score")
    assert_equal(actual.exercise.min_score, expected.exercise.min_score, "min score")
    assert_equal(
        actual.exercise.order_index, expected.exercise.order_index, "order index"
    )
    assert_equal(
        actual.exercise.description, expected.exercise.description, "description"
    )
    assert_equal(
        actual.exercise.estimated_time,
        expected.exercise.estimated_time,
        "estimate time",
    )

@allure.step("Check update exercise response")
def assert_update_exercise_response(actual:UpdateExerciseResponseSchema, expected:UpdateExerciseRequestSchema):
    """
    Проверяет, что ответ обновления данных о задание соотвествутет обновляемому объекту


    :param actual: Ответ Api на обновление задания
    :param expected: Запрос на обновления объекта
    :return:
    """
    logger.info("Check update exercise response")

    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.max_score, expected.max_score, "max score")
    assert_equal(actual.exercise.min_score, expected.min_score, "min score")
    assert_equal(actual.exercise.order_index, expected.order_index, "order index")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, "estimated time")
    assert_equal(actual.exercise.description, expected.description, "description")

@allure.step("Check  exercise not fount response")
def assert_exercise_not_found_response(actual:InternalErrorResponseSchema, expected_title: str):
    """
    Проверка того , что вернулся ответ с ошибкой

    :param actual: API ответ от сервера
    :return: AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check get exercise not found response")
    assert_equal(actual.detail, expected_title, "error message")

@allure.step("Check get exercises response")
def assert_get_exercises_response(actual: GetExercisesResponseSchema, expected: list[CreateExerciseResponseSchema]):
    """
    Проверяет, что ответ на получение списка заданий содержит все созданные задания.

    :param actual: Ответ API на получение списка заданий
    :param expected: Список ответов на создание заданий
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check get exercises response")

    # Сравниваем каждое задание по отдельности
    for index, expected_response in enumerate(expected):
        actual_exercises = actual.exercises[index]
        expected_exercises = expected_response.exercise
        assert_exercise(actual_exercises, expected_exercises)

@allure.step("Check exercises not found error response")
def assert_exercises_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если упражений нет

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    logger.info("Check get exercises not found response")
    # Ожидаемое сообщение об ошибке, если файл не найден
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)