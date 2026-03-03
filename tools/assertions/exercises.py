from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    ExerciseSchema,
    GetExerciseResponseSchema,
)
from tools.assertions.base import assert_equal


def assert_create_exercise_response(
    actual: CreateExerciseResponseSchema, expected: CreateExerciseRequestSchema
):
    """
    Проверяет, что ответ на создание задания соответствует запросу.

    :param actual: Ответ API при создании задания
    :param expected: Запрос на создание задания
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """

    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.course_id, expected.course_id, "course_id")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(
        actual.exercise.estimated_time, expected.estimated_time, "estimated_time"
    )


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что данные упражнения соответствуют ожидаемым.

    :param actual: Фактические данные упражнения
    :param expected: Ожидаемые данные упражнения
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """

    assert_equal(actual.id, expected.id, " exersice ID")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max score")
    assert_equal(actual.min_score, expected.min_score, "min score")
    assert_equal(actual.order_index, expected.order_index, "order index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimate time")


def assert_get_exercise_response(
    actual: GetExerciseResponseSchema, expected: GetExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение упражнения соответствует ожидаемому.

    :param actual: Ответ API при получении упражнения
    :param expected: Ожидаемый ответ на получение упражнения
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
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
