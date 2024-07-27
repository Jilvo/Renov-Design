import hashlib
from flask import request, jsonify
from app.models import UserAccount, DatabaseError
from flasgger import swag_from


@swag_from(
    {
        "tags": ["User Operations"],
        "parameters": [
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "email": {"type": "string"},
                        "password": {"type": "string"},
                    },
                },
            }
        ],
        "responses": {
            "201": {"description": "Account created successfully!"},
            "400": {"description": "Bad Request"},
            "500": {"description": "Database error occurred"},
        },
    }
)
def register():
    try:
        data = request.json
        if not data:
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


def login():
    pass
