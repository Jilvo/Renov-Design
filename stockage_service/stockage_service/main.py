from kink import di
from fastapi import FastAPI
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware
from stockage_service.controller.controller import controller

print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir("."))


app = FastAPI()
# Configuration CORS
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:5173/",
    "http://localhost:5173/",
    "http://127.0.0.1:8080/",
    # Ajoutez d'autres origines si nécessaire
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
controller()

try:
    print("add middleware to app")
    app.include_router(di["stockage_api_router"], tags=["stockage"], prefix="/stockage")
    app.include_router(di["technical_api_router"], tags=["tech"], prefix="/tech")

except Exception as e:
    print(e)
    raise e

if __name__ == "__main__":
    uvicorn.run("stockage_service.main:app", host="localhost", port=8081, reload=True)
