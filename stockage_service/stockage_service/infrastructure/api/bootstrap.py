from fastapi import APIRouter

from stockage_service.infrastructure.api.technical_api_rest.api import (
    router as tech_router,
)
from stockage_service.infrastructure.api.stockage_api_rest.api import (
    router as stockage_router,
)

tech_router: APIRouter = tech_router  # noqa: F841
stockage_router: APIRouter = stockage_router  # noqa: F841


def bootstrap():
    pass
