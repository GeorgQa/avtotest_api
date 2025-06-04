import uuid

from clients.files.file_schema import FileSchema
from clients.users.user_schema import UserSchema
from pydantic import BaseModel, ConfigDict, Field, constr


class CourseSchema(BaseModel):
        """
        Описание структуры курса
        """
        model_config = ConfigDict(populate_by_name=True)

        id: str = Field(default_factory=lambda:str(uuid.uuid4()))
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

    title:  str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание модели запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
