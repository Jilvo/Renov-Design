from kink import di
from fastapi import FastAPI
import uvicorn

from controller.controller import controller

app = FastAPI()
controller()

try:
    print("add middleware to app")
    app.include_router(di["stockage_api_router"], tags=["stockage"], prefix="/stockage")
    app.include_router(di["technical_api_router"], tags=["tech"], prefix="/tech")

except Exception as e:
    print(e)
    raise e

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=7000, reload=True)
    # uvicorn.run("main:app", host="localhost", port=8000, workers=4)
