from kink import inject, di

from domains.stockage.interfaces.stockage_repository_mongo import (
    StockageRepository,
)
from domains.stockage.models.prompt import Prompt


@inject
class StockageGetPromptsUseCase:
    def __init__(self, stockage_repository: StockageRepository):
        self.stockage_repository = stockage_repository

    def action(self, **kwargs) -> Prompt:
        print("ok")
        if kwargs.get("prompt_id"):
            return self.stockage_repository.get_prompt_by_id(kwargs["prompt_id"])
        elif kwargs.get("user_id"):
            return self.stockage_repository.get_all_prompts_by_user_id(
                kwargs["user_id"]
            )
        else:
            return self.stockage_repository.get_all_prompts()
