from fastapi import HTTPException, Request

from utils.security import verify_jwt
from utils.values import ACCESS_TOKEN_KEY


def require_jwt(
    request: Request
):
    token = request.cookies.get(ACCESS_TOKEN_KEY)

    if not token:
        raise HTTPException(status_code=401, detail="No token provided")

    payload = verify_jwt(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return payload
