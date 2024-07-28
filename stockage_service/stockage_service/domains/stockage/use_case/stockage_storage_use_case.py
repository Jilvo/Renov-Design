from kink import inject, di

from domains.stockage.interfaces.stockage_repository_mongo import (
    StockageRepository,
)
from domains.stockage.models.prompt import Prompt


@inject
class StockageStorageUseCase:
    def __init__(self, stockage_repository: StockageRepository):
        self.stockage_repository = stockage_repository

    def action(self, prompt: Prompt) -> Prompt:
        self.stockage_repository.create_prompt(prompt)
        print("Not implemented yet")
