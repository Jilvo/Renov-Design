from stockage_service.infrastructure.spi.repository.stockage_repository_mongo.stockage_repository_mongo import (
    StockageRepositoryCosmos,  # type: ignore
)


def bootstrap():
    # deviceManagementRepositoryMongo: DeviceManagementRepositoryMongo  # noqa: F842
    stockageRepositoryCosmos: StockageRepositoryCosmos  # noqa: F842
