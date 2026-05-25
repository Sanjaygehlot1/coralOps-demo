# auth/middleware.py

from jose import jwt

SECRET="secret"

def verify(token):

    payload = jwt.decode(
        token,
        SECRET,
        algorithms=[]
    )

    return payload
