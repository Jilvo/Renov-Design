from infrastructure.api.bootstrap import (
    bootstrap as bootstrap_infrastructure,
)
from controller.global_parameters import global_parameters

from infrastructure.spi.repository.stockage_repository_mongo.bootstrap import (
    bootstrap as boostrap_repository,
)


try:
    print("bootstraping dependencies for base services (logs,...)")
    global_parameters()
    bootstrap_infrastructure()
    boostrap_repository()
except Exception as e:
    print(e)
    raise e


def controller():
    pass
