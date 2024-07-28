"""
Module API
"""

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from kink import di

from infrastructure.api.stockage_api_rest.api_models import ErrorResponse
from infrastructure.api.stockage_api_rest.dto_prompt import (
    PromptRequest,
    PromptResponse,
)
from commons.errors import DataValidationError, DomainError
from domains.stockage.stockage_services import StockageService

router = APIRouter()
di["stockage_api_router"] = router


@router.get("/health")
def check_health():
    """
    Check the health of the Stockage API.

    Returns:
        dict: A dictionary indicating that the Stockage API has successfully started.
    """
    return {"Stockage API successfully started!"}


# ----------------------------------------------------------------------------------------------------------------------
# -- Entry points for the Stockage API
# ----------------------------------------------------------------------------------------------------------------------

prompt_request_response = {
    200: {
        "model": PromptResponse,
        "description": "Success creation of DM request",
    },
    400: {
        "model": ErrorResponse,
        "description": "Functionnal Error",
        "content": {
            "application/json": {
                "example": {
                    "content empty": {
                        "code": "400",
                        "type": "Fonctionnel",
                        "message": "['content empty']",
                    },
                    "Invalid status": {
                        "code": "400",
                        "type": "Fonctionnel",
                        "message": "Invalid status",
                    },
                }
            },
        },
        422: {"model": ErrorResponse, "description": "Field Validation Error"},
        500: {
            "description": "Technical Error",
            "content": {"application/json": {"example": {"Internal Server Error"}}},
        },
    },
}


@router.post(
    "/prompts", response_model=PromptResponse, responses=prompt_request_response
)
async def create_prompt(request: Request, data: PromptRequest) -> JSONResponse:
    """
    Create a prompt.

    Returns:
        dict: A dictionary indicating the success of the prompt creation.
    """
    try:
        service: StockageService = di[StockageService]
        prompt = service.stockage_initialisation_use_case.action(data)
        service.stockage_storage_use_case.action(prompt)

        return {"code": 200, "type": "", "message": ""}
    except (DataValidationError, DomainError) as e:
        return {"code": 400, "type": "Functional", "message": str(e)}
    except Exception as e:
        return {"code": 500, "type": "Technical", "message": str(e)}


@router.get("/prompts")
def get_prompts():
    """
    Retrieves the prompts for the stockage service.

    Returns:
        dict: A dictionary containing the prompts.
    """
    return {"Prompts"}


@router.get("/prompts/{prompt_id}")
def get_prompt(prompt_id: int):
    """
    Retrieve a prompt based on the given prompt_id.

    Args:
        prompt_id (int): The ID of the prompt to retrieve.

    Returns:
        dict: A dictionary representing the retrieved prompt.
    """
    return {"Prompt"}


@router.get("/upload")
def upload_file():
    """
    Uploads a file to the server.

    Returns:
        dict: A dictionary indicating the success of the file upload.
    """
    return {"Upload file"}
