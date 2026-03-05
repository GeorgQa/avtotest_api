from pydantic import HttpUrl, BaseModel, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class TestDataConfig(BaseModel):
    image_png_file: FilePath = 'testdata/files/image.png'

class HTTPClientConfig(BaseSettings):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url).rstrip('/')

class TestData(BaseModel):
    image_png_file: FilePath

class Settings(BaseSettings):

    test_data: TestDataConfig
    http_client: HTTPClientConfig

    model_config = SettingsConfigDict(
        env_file=".env.local",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )

settings = Settings()
