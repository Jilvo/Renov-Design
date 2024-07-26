from crypt import methods
from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from piccolo.engine import engine_finder
from models import UserAccount, DatabaseError
from flasgger import Swagger, swag_from
import hashlib

app = Flask(__name__)
swagger = Swagger(app)


@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        if data is not None:
            raise ValueError("No data provided")

        try:
            username = data["username"]
            email = data["email"]
            password = data["password"]
        except KeyError as e:
            missing_key = e.args[0]
            raise ValueError(f"Missing key: {missing_key}")

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        new_user = UserAccount(username=username, email=email, password=hashed_password)
        new_user.save().run_sync()

        response = {
            "status": "success",
            "message": "Account created successfully!",
        }
        return jsonify(response), 201

    except ValueError as ve:
        print(f"ValueError: {ve}")
        response = {"status": "error", "message": str(ve)}
        return jsonify(response), 400

    except DatabaseError as de:
        print(f"DatabaseError: {de}")
        response = {"status": "error", "message": "Database error occurred"}
        return jsonify(response), 500

    except Exception as e:
        print(f"Error: {e}")
        response = {"status": "error", "message": "Account creation failed"}
        return jsonify(response), 400


if __name__ == "__main__":
    app.run()
