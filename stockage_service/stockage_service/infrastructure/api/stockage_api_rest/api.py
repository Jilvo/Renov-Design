"""
Module API
"""

from typing import List
from fastapi import APIRouter, HTTPException, Request
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
        "description": "Functional Error",
        "content": {
            "application/json": {
                "examples": {
                    "content_empty": {
                        "code": 400,
                        "type": "Functional",
                        "message": "['content empty']",
                    },
                    "invalid_status": {
                        "code": 400,
                        "type": "Functional",
                        "message": "Invalid status",
                    },
                }
            },
        },
    },
    422: {"model": ErrorResponse, "description": "Field Validation Error"},
    500: {
        "description": "Technical Error",
        "content": {
            "application/json": {
                "example": {
                    "code": 500,
                    "type": "Technical",
                    "message": "Internal Server Error",
                }
            }
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
def get_prompt(prompt_id: str):
    """
    Retrieve a prompt based on the given prompt_id.

    Args:
        prompt_id (int): The ID of the prompt to retrieve.

    Returns:
        dict: A dictionary representing the retrieved prompt.
    """
    try:
        service: StockageService = di[StockageService]
        prompts = service.stockage_get_prompts_use_case.action(prompt_id=prompt_id)
        if not prompts:
            raise HTTPException(status_code=404, detail="This prompt does not exist")
        return {"code": 200, "type": "", "message": prompts}
    except (DataValidationError, DomainError) as e:
        return {"code": 400, "type": "Functional", "message": str(e)}
    except Exception as e:
        return {"code": 500, "type": "Technical", "message": str(e)}


@router.get("/prompts/user/{user_id}", response_model=List[PromptRequest])
async def get_prompts_by_user(user_id: int):
    """
    Retrieve all prompts created by a specific user.

    Args:
        user_id (int): The ID of the user whose prompts are to be retrieved.

    Returns:
        List[PromptRequest]: A list of prompts created by the user.
    """
    try:
        service: StockageService = di[StockageService]
        prompts = service.stockage_get_prompts_use_case.action(user_id)
        if not prompts:
            raise HTTPException(
                status_code=404, detail="No prompts found for this user"
            )
        return prompts
    except (DataValidationError, DomainError) as e:
        return {"code": 400, "type": "Functional", "message": str(e)}
    except Exception as e:
        return {"code": 500, "type": "Technical", "message": str(e)}


@router.delete("/prompts/{prompt_id}", response_model=PromptResponse)
async def delete_prompt(prompt_id: str):
    """
    Delete a prompt based on the given prompt_id.

    Args:
        prompt_id (int): The ID of the prompt to delete.

    Returns:
        dict: A dictionary indicating the success of the prompt deletion.
    """
    try:
        service: StockageService = di[StockageService]
        service.stockage_delete_prompts_use_case.action(prompt_id=prompt_id)
        return {
            "code": 200,
            "type": "success",
            "message": "Prompt deleted successfully",
        }
    except (DataValidationError, DomainError) as e:
        return {"code": 400, "type": "Functional", "message": str(e)}
    except Exception as e:
        return {"code": 500, "type": "Technical", "message": str(e)}


@router.delete("/prompts/user/{user_id}", response_model=PromptResponse)
async def delete_prompts_by_user(user_id: str):
    """
    Delete all prompts created by a specific user.

    Args:
        user_id (str): The ID of the user whose prompts are to be deleted.

    Returns:
        dict: A dictionary indicating the success of the prompts deletion.
    """
    try:
        service: StockageService = di[StockageService]
        service.stockage_delete_prompts_use_case.action(user_id=user_id)
        return {
            "code": 200,
            "type": "success",
            "message": "All prompts deleted successfully",
        }
    except (DataValidationError, DomainError) as e:
        return {"code": 400, "type": "Functional", "message": str(e)}
    except Exception as e:
        return {"code": 500, "type": "Technical", "message": str(e)}


@router.get("/upload")
def upload_file():
    """
    Uploads a file to the server.

    Returns:
        dict: A dictionary indicating the success of the file upload.
    """
    return {"Upload file"}
