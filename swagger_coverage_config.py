import yaml
from pathlib import Path
from swagger_coverage_tool.config import Settings


def get_settings(config_path: str | Path | None = None) -> Settings:
    """
    Кастомная загрузка настроек из .swagger-coverage.yaml
    """
    config_path = Path(config_path) if config_path else Path(".swagger-coverage.yaml")

    if not config_path.exists():
        raise FileNotFoundError(f"Конфиг не найден: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return Settings(**data)