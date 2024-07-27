from infrastructure.api.bootstrap import (
    bootstrap as bootstrap_infrastructure,
)


try:
    print("bootstraping dependencies for base services (logs,...)")
    bootstrap_infrastructure()
except Exception as e:
    print(e)
    raise e


def controller():
    pass
