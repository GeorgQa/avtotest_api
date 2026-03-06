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
        env_file=".env.local",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )

    @classmethod
    def initialize(cls) -> Self:  # Возвращает экземпляр класса Settings
        allure_results_dir = DirectoryPath("./allure-results")  # Создаем объект пути к папке
        allure_results_dir.mkdir(exist_ok=True)  # Создаем папку allure-results, если она не существует

        # Передаем allure_results_dir в инициализацию настроек
        return Settings(allure_results_dir=allure_results_dir)

settings = Settings.initialize()
