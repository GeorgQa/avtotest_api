import pytest

from pydantic import BaseModel

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.users import UserFixture



"""
Этот класс представляет объект с данными созданного упражнения.
"""
class ExercisesFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema

@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    """
    Фикстура для получения авторизованного клиента упражнений.

    :param function_user: Фикстура с данными созданного пользователя
    :return: Авторизованный клиент ExercisesClient
    """
    return get_exercises_client(function_user.authentication_user)

@pytest.fixture
def function_exercise(exercises_client: ExercisesClient, function_course: CoursesFixture, function_user: UserFixture) -> ExercisesFixture:
    """
    Фикстура для создания нового упражнения.
    Выполняет запрос на создание упражнения через API,
    используя существующий курс и авторизованного пользователя.


    :param exercises_client: Авторизованный клиент для работы с упражнениями.
    :param function_course: Фикстура с данными существующего курса.
    :param function_user: Фикстура с данными пользователя.
    :return: Объект ExercisesFixture с request и response
    """
    request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
    response = exercises_client.create_exercise(request=request)
    return  ExercisesFixture(request=request, response=response)
