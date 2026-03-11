
from swagger_coverage_tool.src.tracker.core import SwaggerCoverageTracker
from swagger_coverage_tool.config import get_settings


settings = get_settings()

tracker = SwaggerCoverageTracker(service="api-course", settings=settings)