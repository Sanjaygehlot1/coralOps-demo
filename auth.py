# auth.py

def validate_token(token):
    if token is None:
        raise Exception("JWT validation failure")
