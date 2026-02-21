from pydantic import BaseModel, ConfigDict, Field

from tools.faker_data import fake


class UserSchema(BaseModel):
    """
    Модель пользователя
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)


class CreateUserResponseSchema(BaseModel):
    """
    Описание модели ответа на создание пользователя
    """

    model_config = ConfigDict(populate_by_name=True)
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя
    """

    model_config = ConfigDict(populate_by_name=True)

    email: str | None = Field(default=fake.email)
    lastName: str | None = Field(alias="lastName", default=fake.last_name)
    firstName: str | None = Field(alias="firstName", default=fake.first_name)
    middleName: str | None = Field(alias="middleName", default=fake.middle_name)


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
