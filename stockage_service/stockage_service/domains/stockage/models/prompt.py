from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from infrastructure.api.stockage_api_rest.dto_prompt import PromptRequest
from commons.errors import DataValidationError


class Prompt(BaseModel):
    """Prompt's model, which is saved in the database"""

    id: UUID
    content: str
    creation_date: datetime
    created_by: str
    tags: str = ""
    status: str
    related_images: List[str]
    generation_origin: str = ""
    processing_duration: int = 0

    def toDict(self):
        instance = {
            "id": str(self.id),
            "content": self.content,
            "creation_date": self.creation_date,
            "created_by": self.created_by,
            "tags": self.tags,
            "status": self.status,
            "related_images": self.related_images,
            "generation_origin": self.generation_origin,
            "processing_duration": self.processing_duration,
        }
        return instance

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
        if not prompt_request.content:
            error_list.append("content empty")
        if not prompt_request.created_by:
            error_list.append("created_by empty")
        if not prompt_request.status:
            error_list.append("status empty")
        if error_list:
            raise DataValidationError(error_list)
        return True
