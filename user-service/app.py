from crypt import methods
from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from piccolo.engine import engine_finder
from models import UserAccount
from flasgger import Swagger, swag_from
import hashlib

app = Flask(__name__)
swagger = Swagger(app)


@app.route("/register", methods=["POST"])
def register():
    try:

        print("cc")
        data: dict = request.json
        username = data["username"]
        email = data["email"]
        password = data["password"]
        print(email, username, password)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        new_user = UserAccount(username=username, email=email, password=hashed_password)
        new_user.save().run_sync()

        response = {
            "status": "success",
            "message": "Account created successfully!",
        }
        return jsonify(response), 201
    except Exception as e:
        print(f"Error: {e}")
        response = {"status": "error", "message": "Account creation failed"}
        return jsonify(response), 400


if __name__ == "__main__":
    app.run()
