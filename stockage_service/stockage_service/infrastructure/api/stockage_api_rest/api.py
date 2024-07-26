"""
Module API
"""

from fastapi import APIRouter
from kink import di

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
