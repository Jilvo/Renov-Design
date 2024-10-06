from kink import inject

from stockage_service.domains.stockage.interfaces.stockage_repository_mongo import (
    StockageRepository,
)
from stockage_service.domains.stockage.models.prompt import Prompt
from stockage_service.commons.errors import QueryError


@inject
class StockageDeletePromptUseCase:
    def __init__(self, stockage_repository: StockageRepository):
        self.stockage_repository = stockage_repository

    def action(self, **kwargs) -> Prompt:
        print("ok")
        if kwargs.get("prompt_id"):
            return self.stockage_repository.delete_prompt(kwargs["prompt_id"])
        elif kwargs.get("user_id"):
            return self.stockage_repository.delete_prompts_by_user_id(kwargs["user_id"])
        else:
            raise QueryError("No prompt_id or user_id provided")
