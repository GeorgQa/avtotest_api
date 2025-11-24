import uuid
from typing import Pattern

from pydantic import BaseModel, Field, HttpUrl


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

    filename: str
    directory: str
    upload_file: str
