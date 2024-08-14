from piccolo.engine.postgres import PostgresEngine
from piccolo.conf.apps import AppRegistry
import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")


DB = PostgresEngine(
    config={
        "database": "user_service",
        "user": "alexiane",
        "password": os.getenv("DB_PASSWORD"),
        "host": "localhost",
        "port": 5432,
    }
)
DATABASE_CONFIG = {"default": DB}
APP_REGISTRY = AppRegistry(apps=["app.piccolo_app"])
