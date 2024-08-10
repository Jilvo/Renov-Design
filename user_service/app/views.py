from app.controllers import register_user, login, get_user
from flask import Flask

app = Flask(__name__)


@app.route("/register", methods=["POST"])
def register_view():
    return register_user()


@app.route("/login", methods=["POST"])
def login_view():
    return login()


@app.route("/users", methods=["GET"])
def users_view():
    return get_user()
