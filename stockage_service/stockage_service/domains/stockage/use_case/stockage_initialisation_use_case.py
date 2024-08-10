from datetime import datetime
import uuid
from kink import inject, di

from domains.stockage.interfaces.stockage_repository_mongo import (
    StockageRepository,
)
from infrastructure.api.stockage_api_rest.dto_prompt import PromptRequest
from domains.stockage.models.prompt import Prompt


@inject
class StockageInitialisationUseCase:
    def __init__(self, stockage_repository: StockageRepository):
        self.stockage_repository = stockage_repository

    def action(self, prompt_request: PromptRequest):
        """Raise a validation error if controls fail
        first_controls check essentials fields"""
        Prompt.first_controls(prompt_request)
        self.__check_if_prompt_exists(prompt_request)
        prompt = self.__create_prompt(prompt_request)

        return prompt

    def __create_prompt(self, prompt_request: PromptRequest) -> Prompt:
        prompt = Prompt(
            id=str(uuid.uuid4()),
            content=prompt_request.content,
            creation_date=datetime.now(),
            created_by=prompt_request.created_by,
            tags=prompt_request.tags,
            status=prompt_request.status,
            related_images=prompt_request.related_images,
            generation_origin=prompt_request.generation_origin,
            processing_duration=prompt_request.processing_duration,
        )

        return prompt

    def __check_if_prompt_exists(self, prompt_request: PromptRequest):
        """Check if prompt already exists"""
        print("Not implemented yet")
