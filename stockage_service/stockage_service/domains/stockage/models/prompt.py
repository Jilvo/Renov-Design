from datetime import datetime

from pydantic import BaseModel

from stockage_service.infrastructure.api.stockage_api_rest.dto_prompt import (
    PromptRequest,
)
from stockage_service.commons.errors import DataValidationError


class Prompt(BaseModel):
    """Prompt's model, which is saved in the database"""

    id: str
    creation_date: datetime
    created_by: int
    tags: str = ""
    status: str
    modified_image: str = ""
    generation_origin: str
    processing_duration: float = 0

    def toDict(self):
        return self.model_dump()

    @staticmethod
    def first_controls(prompt_request: PromptRequest):
        """
        Handles the initial controls for a Prompt request.

        Args:
            prompt_request (PromptRequest): The PromptRequest object containing
                details of the Prompt.

        Returns:
            bool: Returns True if the checks pass successfully.

        Raises :
            DataValidationError : Raised if field is empty
        """
        error_list = []
        if not prompt_request.created_by:
            error_list.append("created_by empty")
        if not prompt_request.status:
            error_list.append("status empty")
        if error_list:
            raise DataValidationError(error_list)
        return True
