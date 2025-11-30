import uuid
from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, StringConstraints, constr

from tools.faker_data import fake

"""
Модель данных пользователя

:return Готовая модель пользователя
"""


class UserSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: Annotated[str, StringConstraints(min_length=1, max_length=250)] = Field(
        default_factory=fake.email,
        validation_alias="email",
        serialization_alias="email",
    )
    last_name: str = Field(alias="lastName", min_length=1, max_length=50)
    first_name: str = Field(alias="firstName", min_length=1, max_length=50)
    middle_name: str = Field(alias="middleName", min_length=1, max_length=50)


"""
Модель запроса на создание пользователя

:return Готовая модель для запроса на создание пользователя
"""


class CreateUserRequestSchema(BaseModel):
    email: EmailStr = Field(
        alias="email", min_length=1, max_length=250, default_factory=fake.email
    )
    last_name: str = Field(
        alias="lastName", min_length=1, max_length=50, default_factory=fake.last_name
    )
    first_name: str = Field(
        alias="firstName", min_length=1, max_length=50, default_factory=fake.first_name
    )
    middle_name: str = Field(
        alias="middleName",
        min_length=1,
        max_length=50,
        default_factory=fake.middle_name,
    )
    password: str = Field(min_length=8, max_length=250, default_factory=fake.password)


"""
Модель на получение ответа с данными созданного пользователя

:return Модель ответа созданного пользователя
"""


class CreateUserResponseSchema(BaseModel):
    user: UserSchema
