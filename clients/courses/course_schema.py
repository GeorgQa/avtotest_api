import uuid

from pydantic import BaseModel, ConfigDict, Field, constr

from clients.files.file_schema import FileSchema
from clients.users.user_schema import UserSchema
from tools.faker_data import fake


class CourseSchema(BaseModel):
    """
    Описание структуры курса
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str | None = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


class CreateCourseResponseSchema(BaseModel):
    """
    Описание модели ответа курса
    """

    course: CourseSchema


class GetCoursesQuerySchema(BaseModel):
    """
    Описание модели запроса на получение списка курсов.
    """

    model_config = ConfigDict(populate_by_name=True)

    userId: str = Field(alias="userId")


class CreateCourseRequestSchema(BaseModel):
    """
    Описание модели запроса на создание курса.
    """

    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(
        alias="estimatedTime", default_factory=fake.estimated_time
    )
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание модели запроса на обновление курса.
    Все поля опциональные.
    """

    model_config = ConfigDict(populate_by_name=True)

    title: str | None = None
    max_score: int | None = Field(alias="maxScore", default=None)
    min_score: int | None = Field(alias="minScore", default=None)
    description: str | None = None
    estimated_time: str | None = Field(alias="estimatedTime", default=None)


class UpdateCourseResponseSchema(BaseModel):
    """
    Описание структуры для ответа обновления круса.
    """

    course: CourseSchema


class GetIDCoursesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение курса по ID
    """

    course: CourseSchema


class GetIDCoursesRequestSchema(BaseModel):
    """
    Описание структуры ответа на получение курса по ID
    """

    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="id")


class GetCoursesResponseSchema(BaseModel):

    courses: list[CourseSchema]
