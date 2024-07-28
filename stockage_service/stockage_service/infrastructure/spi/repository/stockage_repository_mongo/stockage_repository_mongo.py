from __future__ import annotations


from domains.stockage.models.prompt import Prompt
import traceback, json
from kink import di, inject
from pymongo import MongoClient
from pymongo.collection import ReturnDocument
from domains.stockage.interfaces.stockage_repository_mongo import (
    StockageRepository,
)
from commons.errors import DataValidationError, DomainError


@inject(alias="stockage_repository")
@inject(alias="repository")
class StockageRepositoryCosmos(StockageRepository):
    def __init__(self):
        try:
            print(di["MONGO_STOCKAGE_DB_URL"])
            self.client = MongoClient(di["MONGO_STOCKAGE_DB_URL"])
            self.db = self.client["renov_design"]
            self.stockage_prompt = self.db["stockage_prompt"]
        except Exception as e:
            traceback.print_exc()
            raise DomainError(f"Error connecting to MongoDB: {e}") from e

    def create_prompt(self, prompt: Prompt) -> Prompt:
        try:
            item = prompt.toDict()
            self.stockage_prompt.insert_one(item)
            return prompt
        except Exception as e:
            traceback.print_exc()
            raise DomainError(f"Error creating prompt: {e}") from e

    def read_prompt(self, prompt_id: str) -> Prompt:
        try:
            item = self.stockage_prompt.find_one({"id": prompt_id})
            if item:
                return Prompt(**item)
            else:
                raise DataValidationError(f"Prompt with id {prompt_id} not found")
        except Exception as e:
            traceback.print_exc()
            raise DomainError(f"Error reading prompt: {e}") from e

    def update_prompt(self, prompt: Prompt) -> Prompt:
        try:
            item = prompt.toDict()
            updated_item = self.stockage_prompt.find_one_and_update(
                {"id": item["id"]}, {"$set": item}, return_document=ReturnDocument.AFTER
            )
            if updated_item:
                return Prompt(**updated_item)
            else:
                raise DataValidationError(f"Prompt with id {item['id']} not found")
        except Exception as e:
            traceback.print_exc()
            raise DomainError(f"Error updating prompt: {e}") from e

    def delete_prompt(self, prompt_id: str) -> bool:
        try:
            result = self.stockage_prompt.delete_one({"id": prompt_id})
            if result.deleted_count == 1:
                return True
            else:
                raise DataValidationError(f"Prompt with id {prompt_id} not found")
        except Exception as e:
            traceback.print_exc()
            raise DomainError(f"Error deleting prompt: {e}") from e
