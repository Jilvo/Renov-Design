from app.controllers import (
    register_user,
    login,
    get_user,
    delete_user,
    update_user,
    get_user_by_id,
)
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


@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user_view(user_id):
    return delete_user(user_id)


@app.route("/users/<user_id>", methods=["PUT"])
def update_user_view(user_id):
    return update_user(user_id)


@app.route("/users/user_id>", methods=["GET"])
def user_by_id(user_id):
    return get_user_by_id(user_id)