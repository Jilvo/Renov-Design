from piccolo.engine.postgres import PostgresEngine
from piccolo.conf.apps import AppRegistry
import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")


DB = PostgresEngine(
    config={
        "database": "user_service",
        "user": "postgres",
        # "user": "alexiane",
        "password": "postgres",
        # "password": os.getenv("DB_PASSWORD"),
        "host": "db",
        "port": 5432,
    }
)
DATABASE_CONFIG = {"default": DB}
APP_REGISTRY = AppRegistry(apps=["app.piccolo_app"])
