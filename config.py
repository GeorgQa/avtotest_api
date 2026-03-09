from pathlib import Path
from typing import Self
from pydantic import BaseModel, HttpUrl, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)


class TestDataConfig(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env.local",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    test_data: TestDataConfig
    http_client: HTTPClientConfig
    allure_results_dir: Path = Path("./allure-results")

    def model_post_init(self, __context) -> None:

        self.allure_results_dir.mkdir(exist_ok=True, parents=True)


# Глобальный экземпляр настроек
settings = Settings()