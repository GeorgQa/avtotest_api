import uuid

from pydantic import BaseModel, ConfigDict, Field


class UserSchema(BaseModel):
    """
    Модель пользователя
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(default_factory= lambda : str(uuid.uuid4()))
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: str
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """
    Описание модели ответа на создание пользователя
    """
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя
     """
    model_config = ConfigDict(populate_by_name=True)

    email: str | None
    lastName: str | None = Field(alias="lastName")
    firstName: str | None = Field(alias="firstName")
    middleName: str | None = Field(alias="middleName")

class UpdateUserResponseSchema(BaseModel):
    """
    Описание модели ответа на обновление пользователя
    """
    user: UserSchema

class GetUserResponseSchema(BaseModel):
    """
    Описание модели запроса получение пользователя
    """
    user: UserSchema