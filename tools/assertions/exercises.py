from clients.exercises.exercises_schema import  CreateExerciseRequestSchema, CreateExerciseResponseSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(actual:CreateExerciseResponseSchema, expeted: CreateExerciseRequestSchema ):
    """
    Функция проверяет что тело ответа соответсвует запросу на создание задания

    :param actual: Ответ API при создании заданий
    :param expeted: Запрос для создания задания
    :return: AsserionError: если хоть одно значение не совпадает
    """

    assert_equal(actual.exercise.title, expeted.title, "title")
    assert_equal(actual.exercise.course_id, expeted.course_id, "course_id")
    assert_equal(actual.exercise.max_score, expeted.max_score, "max_score")
    assert_equal(actual.exercise.min_score, expeted.min_score, "min_score")
    assert_equal(actual.exercise.order_index, expeted.order_index, "order_index")
    assert_equal(actual.exercise.description, expeted.description, "description")
    assert_equal(actual.exercise.estimated_time, expeted.estimated_time, "estimated_time")

