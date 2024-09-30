from kink import di, inject

from stockage_service.domains.stockage.use_case.stockage_initialisation_use_case import (
    StockageInitialisationUseCase,
)
from stockage_service.domains.stockage.use_case.stockage_storage_use_case import (
    StockageStorageUseCase,
)
from stockage_service.domains.stockage.use_case.stockage_delete_prompts_use_case import (
    StockageDeletePromptUseCase,
)
from stockage_service.domains.stockage.use_case.stockage_get_prompts_use_case import (
    StockageGetPromptsUseCase,
)


@inject
class StockageService:
    def __init__(self):
        self.stockage_initialisation_use_case: StockageInitialisationUseCase = di[
            StockageInitialisationUseCase
        ]
        self.stockage_storage_use_case: StockageStorageUseCase = di[
            StockageStorageUseCase
        ]
        self.stockage_get_prompts_use_case: StockageGetPromptsUseCase = di[
            StockageGetPromptsUseCase
        ]
        self.stockage_delete_prompts_use_case: StockageDeletePromptUseCase = di[
            StockageDeletePromptUseCase
        ]
