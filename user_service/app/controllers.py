from flask import jsonify, request
from app.models import UserAccount
import hashlib
import jwt
import datetime
from flasgger import swag_from

SECRET_KEY = "jwt"


@swag_from(
    {
        "responses": {
            200: {
                "description": "A successful response",
                "examples": {
                    "application/json": {"message": "User registered successfully"}
                },
            }
        },
        "parameters": [
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "The username of the user",
                        },
                        "email": {
                            "type": "string",
                            "description": "The email of the user",
                        },
                        "password": {
                            "type": "string",
                            "description": "The password of the user",
                        },
                    },
                    "required": ["username", "email", "password"],
                },
            }
        ],
    }
)
def register_user():
    try:
        data: dict = request.get_json()
        username = data["username"]
        email = data["email"]
        password = data["password"]
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


@swag_from(
    {
        "parameters": [
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "password": {"type": "string"},
                    },
                    "required": ["username", "password"],
                },
            }
        ],
        "responses": {
            200: {
                "description": "Login successful",
                "schema": {
                    "type": "object",
                    "properties": {"token": {"type": "string"}},
                },
            },
            400: {
                "description": "Login failed",
                "schema": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string"},
                        "message": {"type": "string"},
                    },
                },
            },
        },
    }
)
def login():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = (
            UserAccount.objects()
            .where(UserAccount.username == username)
            .first()
            .run_sync()
        )

        if user:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            if hashed_password == user.password:
                token = jwt.encode(
                    {
                        "user_id": user.id,
                        "exp": datetime.datetime.utcnow()
                        + datetime.timedelta(hours=24),
                    },
                    SECRET_KEY,
                    algorithm="HS256",
                )

                response = {
                    "status": "success",
                    "message": "Login successful!",
                    "token": token,
                }
                return jsonify(response), 200
            else:
                response = {"status": "error", "message": "Invalid password"}
                return jsonify(response), 401
        else:
            response = {"status": "error", "message": "User not found"}
            return jsonify(response), 404
    except Exception as e:
        print(f"Error: {e}")
        response = {"status": "error", "message": "Login failed"}
        return jsonify(response), 400


@swag_from(
    {
        "responses": {
            200: {
                "description": "A list of users",
                "schema": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "username": {"type": "string"},
                            "email": {"type": "string"},
                        },
                    },
                },
            }
        }
    }
)
def get_user():
    try:
        users = UserAccount.objects().run_sync()

        users_list = [user.to_dict() for user in users]

        return jsonify(users_list)
    except Exception as e:
        return jsonify({"message": str(e)}), 500
