from flask import jsonify, request
from app.models import UserAccount
import hashlib
import jwt
import datetime
from flasgger import swag_from
import os


SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT = "jwt"


@swag_from("swagger/register_user.yml")
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


@swag_from("swagger/login.yml")
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
                    JWT,
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


@swag_from("swagger/get_user.yml")
def get_user():
    try:
        users = UserAccount.objects().run_sync()

        users_list = [user.to_dict() for user in users]

        return jsonify(users_list)
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@swag_from("swagger/get_user_by_id.yml")
def get_user_by_id(user_id: int):
    try:
        user_id = int(user_id)
        user = UserAccount.objects().where(UserAccount.id == user_id).first().run_sync()
        if not user:
            return jsonify({"message": "User not found"}), 404
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }
        return jsonify(user_data), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@swag_from("swagger/delete_user.yml")
# @token_required
def delete_user(user_id: int):
    try:
        user_id = int(user_id)
        user = UserAccount.objects().where(UserAccount.id == user_id).first().run_sync()
        if not user:
            return jsonify({"message": "User not found"}), 404

        user.remove().run_sync()

        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@swag_from("swagger/update_user.yml")
def update_user():
    try:
        data = request.get_json()
        user_id = int(data.get("user_id"))
        new_username = data.get("new_username")

        print(f"Received data: {data}")

        user = UserAccount.objects().where(UserAccount.id == user_id).first().run_sync()

        if not user:
            return jsonify({"message": "User not found"}), 404

        user.username = new_username
        user.save().run_sync()

        return jsonify({"message": "Username updated successfully"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": str(e)}), 500


@swag_from("swagger/update_password.yml")
def update_password():
    try:
        data = request.get_json()
        user_id = int(data.get("user_id"))
        old_password = data.get("old_password")
        new_password = data.get("new_password")

        print(f"Received data: {data}")

        user = UserAccount.objects().where(UserAccount.id == user_id).first().run_sync()

        if not user:
            return jsonify({"message": "User not found"}), 404

        hashed_old_password = hashlib.sha256(old_password.encode()).hexdigest()
        if hashed_old_password != user.password:
            return jsonify({"message": "Old password is incorrect"}), 401

        hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()

        user.password = hashed_new_password
        user.save().run_sync()

        return jsonify({"message": "Password updated successfully"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": str(e)}), 500


@swag_from("swagger/logout.yml")
def logout():
    try:
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"message": "Token is missing!"}), 403

        try:
            jwt.decode(token, JWT, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 401
        return jsonify({"message": "Logout successful"}), 200

    except Exception as e:
        return jsonify({"message": f"Logout failed: {str(e)}"}), 500
