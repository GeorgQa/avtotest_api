from pathlib import Path
from typing import Self

from pydantic import HttpUrl, BaseModel, FilePath, DirectoryPath
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
    allure_results_dir: DirectoryPath

    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env.local",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )

    @classmethod
    def initialize(cls) -> Self:
        # Создаем экземпляр настроек, который автоматически загрузит значения из .env.local
        settings = cls()
        # Убеждаемся, что директория для allure результатов создана
        settings.allure_results_dir.mkdir(exist_ok=True)
        return settings

settings = Settings.initialize()
