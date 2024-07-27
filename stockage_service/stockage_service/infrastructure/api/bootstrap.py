from fastapi import APIRouter
import infrastructure.api.technical_api_rest.api
import infrastructure.api.stockage_api_rest.api

tech_router: APIRouter = infrastructure.api.technical_api_rest.api.router  # noqa: F841
stockage_router: APIRouter = (
    infrastructure.api.stockage_api_rest.api.router
)  # noqa: F841


def bootstrap():
    pass
