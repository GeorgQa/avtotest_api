import uuid

from pydantic import BaseModel, Field, HttpUrl

from tools.faker_data import fake


class FileSchema(BaseModel):
    """
    Описание структуры файла
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    filename: str
    directory: str
    url: HttpUrl = Field(min_length=1, max_length=2083)


class CreateFileResponseSchema(BaseModel):
    """
    Описание структры ответа на создание файла
    """

    file: FileSchema


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """

    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str = Field(default="tests")
    upload_file: str
