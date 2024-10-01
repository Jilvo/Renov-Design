from flask import Flask

from flasgger import Swagger
from piccolo_conf import Config
from app.controllers import (
    register_user,
    login,
    get_user,
    delete_user,
    update_user,
    get_user_by_id,
    update_password,
    logout,
)
import os


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/apispec_1.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/",
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'",
            }
        },
        "security": [{"Bearer": []}],
    }

    Swagger(app, config=swagger_config)

    app.add_url_rule("/register", "register", register_user, methods=["POST"])
    app.add_url_rule("/login", "login", login, methods=["POST"])
    app.add_url_rule("/users", "users", get_user, methods=["GET"])
    app.add_url_rule(
        "/users_delete/<user_id>", "delete_user", delete_user, methods=["DELETE"]
    )
    app.add_url_rule("/users_update", "update_user", update_user, methods=["PUT"])
    app.add_url_rule("/users_update", "update_user", update_user, methods=["PUT"])
    app.add_url_rule(
        "/users_by_id/<user_id>", "users_by_id", get_user_by_id, methods=["GET"]
    )

    app.add_url_rule(
        "/update_password", "update_password", update_password, methods=["POST"]
    )
    app.add_url_rule("/logout", "logout", logout, methods=["POST"])
    return app
