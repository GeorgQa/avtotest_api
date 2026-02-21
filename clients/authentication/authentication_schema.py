from pydantic import BaseModel, ConfigDict, Field

from tools.faker_data import fake


class LoginRequestSchema(BaseModel):
    """
    Модель запроса на авторизацию
    """

    model_config = ConfigDict(extra="forbid")

    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class TokenSchema(BaseModel):
    """
    Модель сущности токена
    """

    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginResponseSchema(BaseModel):
    """
    Модель ответа запрсоса на авторизацию
    """

    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    Модель запроса на получение refresh токена
    """

    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)
