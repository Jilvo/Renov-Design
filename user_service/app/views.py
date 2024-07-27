from flask import render_template
from app import app
from app.controllers import register, login


@app.route("/register", methods=["POST"])
def register_view():
    return register()


@app.route("/login", methods=["POST"])
def login_view():
    return login()
