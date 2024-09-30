from datetime import datetime
import uuid
from kink import inject
from google.cloud import storage

from stockage_service.domains.stockage.interfaces.stockage_repository_mongo import (
    StockageRepository,
)
from stockage_service.infrastructure.api.stockage_api_rest.dto_prompt import (
    PromptRequest,
)
from stockage_service.domains.stockage.models.prompt import Prompt


@inject
class StockageInitialisationUseCase:
    def __init__(self, stockage_repository: StockageRepository):
        self.stockage_repository = stockage_repository

    def action(self, prompt_request: PromptRequest):
        """Raise a validation error if controls fail
        first_controls check essentials fields"""
        Prompt.first_controls(prompt_request)
        self.__check_if_prompt_exists(prompt_request)
        # self.__upload_blob(prompt_request)
        prompt = self.__create_prompt(prompt_request)

        return prompt

    def __create_prompt(self, prompt_request: PromptRequest) -> Prompt:
        prompt = Prompt(
            id=str(uuid.uuid4()),
            creation_date=datetime.now(),
            created_by=prompt_request.created_by,
            tags=prompt_request.tags,
            status=prompt_request.status,
            modified_image=prompt_request.modified_image,
            generation_origin=prompt_request.generation_origin,
            processing_duration=prompt_request.processing_duration,
        )

        return prompt

    def __check_if_prompt_exists(self, prompt_request: PromptRequest):
        """Check if prompt already exists"""
        print("Not implemented yet")

    def __upload_blob(self, prompt_request: PromptRequest):
        """Upload blob to storage"""
        bucket_name = "renov-design-stockage"
        destination_blob_name = "test"
        source_file_name = ""
        storage_client = storage.Client.from_service_account_json(
            "path/to/your/service-account-file.json"
        )
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print(f"File {source_file_name} uploaded to {destination_blob_name}.")
        print("Not implemented yet")
