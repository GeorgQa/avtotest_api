import uuid

from pydantic import BaseModel, ConfigDict, Field


class ExerciseSchema(BaseModel):
    """
    Описание структуры задания
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(default_factory= lambda: str(uuid.uuid4()))
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int =Field(alias="maxScore")
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
    exercises:list[ExerciseSchema]

class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры для запроса на создание задания
    """
    model_config = ConfigDict(populate_by_name=True)

    title : str
    course_id : str = Field(alias="courseId")
    max_score : int = Field(alias="maxScore")
    min_score : int = Field(alias="minScore")
    order_index : int | None = Field(alias="orderIndex")
    description : str
    estimated_time : str = Field(alias="estimatedTime")

class CreateExerciseResponseSchema(BaseModel):
    """
    Описание модели для ответа на создание задания
    """
    exercise:ExerciseSchema


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

    title: str | None
    course_id: str | None = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание модели ответа на обновление задания
    """
    exercise: ExerciseSchema