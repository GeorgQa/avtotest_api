from swagger_coverage_config import get_settings
from swagger_coverage_tool.src.tracker.core import SwaggerCoverageTracker


settings = get_settings(config_path=".swagger-coverage.yaml")

tracker = SwaggerCoverageTracker(service="api-course", settings=settings)