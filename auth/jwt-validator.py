# auth/jwt_validator.py

from jose import jwt

SECRET = "super-secret"

def validate_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET,
            algorithms=["HS256"]
        )

        return payload

    except Exception:
        return None
