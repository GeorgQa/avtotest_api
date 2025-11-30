import uuid

from pydantic import BaseModel, ConfigDict, Field

from tools.faker_data import fake


class ExerciseSchema(BaseModel):
    """
    Описание структуры задания
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesQuerySchema(BaseModel):
    """
    Описание стуктуры для запроса на получение списка зданий
    """

    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка заданий.
    """

    exercises: list[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры для запроса на создание задания
    """

    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(
        alias="estimatedTime", default_factory=fake.estimated_time
    )


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание модели для ответа на создание задания
    """

    exercise: ExerciseSchema


class GetExerciseResponseSchema(BaseModel):
    """
    Описание модели для ответа на получение одного задания
    """

    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание модели запроса на обновление задания.
    """

    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.sentence)
    course_id: str | None = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(
        alias="estimatedTime", default_factory=fake.estimated_time
    )


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание модели ответа на обновление задания
    """

    exercise: ExerciseSchema
