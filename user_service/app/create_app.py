from flask import Flask
from flasgger import Swagger
from piccolo_conf import Config
from app.controllers import register_user, login, get_user


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
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
    }
    Swagger(app, config=swagger_config)

    app.add_url_rule("/register", "register", register_user, methods=["POST"])
    app.add_url_rule("/login", "login", login, methods=["POST"])
    app.add_url_rule("/users", "users", get_user, methods=["GET"])

    return app
