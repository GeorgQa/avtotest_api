from swagger_coverage_tool.src.tracker.core import SwaggerCoverageTracker
from swagger_coverage_tool.config import Settings



settings = Settings(
    services=[
        {
            "key": "api-course",
            "name": "API Course",
            "base_url": "http://localhost:8000",
            "swagger_url": "http://localhost:8000/api/v1/openapi.json",
            "tags": ["API", "COURSES"],
            "repository": "https://github.com/Nikita-Filonov/qa-automation-engineer-api-course"
        }
    ],
    html_report_file="./coverage.html",
    results_dir="./coverage-results",
    history_file="./coverage-history.json",
    history_retention_limit=30,
    json_report_file="./coverage-report.json"
)


tracker = SwaggerCoverageTracker(service="api-course", settings=settings)