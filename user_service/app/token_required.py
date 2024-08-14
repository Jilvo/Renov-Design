from functools import wraps

from flask import jsonify, request
import jwt

from user_service.app.controllers import JWT
from user_service.app.models import UserAccount


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            data = jwt.decode(token, JWT, algorithms=["HS256"])
            current_user = (
                UserAccount.objects()
                .where(UserAccount.id == data["user_id"])
                .first()
                .run_sync()
            )
        except Exception as e:
            print(f"Token decoding error: {e}")
            return jsonify({"message": "Token is invalid!"}), 401

        return f(current_user, *args, **kwargs)

    return decorated
