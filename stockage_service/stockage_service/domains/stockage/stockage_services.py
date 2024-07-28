from kink import di, inject

from domains.stockage.use_case.stockage_initialisation_use_case import (
    StockageInitialisationUseCase,
)
from domains.stockage.use_case.stockage_storage_use_case import StockageStorageUseCase


@inject
class StockageService:
    def __init__(self):
        self.stockage_initialisation_use_case: StockageInitialisationUseCase = di[
            StockageInitialisationUseCase
        ]
        self.stockage_storage_use_case: StockageStorageUseCase = di[
            StockageStorageUseCase
        ]
