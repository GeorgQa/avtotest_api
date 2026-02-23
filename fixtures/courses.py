import pytest
from pydantic import BaseModel

from clients.courses.course_schema import (
    CreateCourseRequestSchema,
    CreateCourseResponseSchema,
)
from clients.courses.courses_client import CoursesClient, get_courses_client
from fixtures.files import FileFixture
from fixtures.users import UserFixture


# Этот класс представляет объект с данными созданного курса
class CoursesFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema


# Эта фикстура создает клиент CoursesClient, который используется для взаимодействия с API курсов.
@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)


# Фикстура автоматически создает курс
@pytest.fixture
def function_course(
    courses_client: CoursesClient,
    function_user: UserFixture,
    function_file: FileFixture,
) -> CoursesFixture:
    request = CreateCourseRequestSchema(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id,
    )
    response = courses_client.create_course(request=request)
    return CoursesFixture(request=request, response=response)
