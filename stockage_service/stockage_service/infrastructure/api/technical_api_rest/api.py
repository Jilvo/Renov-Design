from fastapi import APIRouter
from kink import di

router = APIRouter()

di["technical_api_router"] = router


@router.get("/health")
def check_health():
    """
    Check the health of the Technical API.

    Returns:
        dict: A dictionary indicating the successful start of the Technical API.
    """
    return {"Technical API successfully started!"}
