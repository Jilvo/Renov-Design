from piccolo.engine.postgres import PostgresEngine
from piccolo.conf.apps import AppRegistry

DB = PostgresEngine(
    config={
        "database": "user_service",
        "user": "alexiane",
        "password": "alexiane",
        "host": "localhost",
        "port": 5432,
    }
)
DATABASE_CONFIG = {"default": DB}
APP_REGISTRY = AppRegistry(apps=["piccolo_app"])
