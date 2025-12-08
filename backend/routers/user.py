from fastapi import APIRouter, HTTPException, Response, Depends

from schemas.user_schemas import CreateUser, LoginUser
from services.user_service import create_user, create_user_jwt, find_all_users, get_user
from utils.security import verify_password
from dependencies.security import require_admin_jwt, require_jwt
from utils.values import ACCESS_TOKEN_KEY


router = APIRouter()

@router.get("/")
def get_users(admin=Depends(require_admin_jwt)):
    users = find_all_users()

    return users

@router.post("/signup")
def signup(user: CreateUser, admin=Depends(require_admin_jwt)):
    created = create_user(user)

    return created


@router.post("/login")
def login(user: LoginUser, response: Response):
    searched = get_user(user.email)

    if not verify_password(user.password, searched.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid password")

    response.set_cookie(
        ACCESS_TOKEN_KEY,
        create_user_jwt(searched),
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=900
    )

    return {
        "name": searched.name,
        "email": searched.email
    }


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(ACCESS_TOKEN_KEY)

    return {
        "logged_out": True
    }


@router.get("/me")
def get_my_user(user=Depends(require_jwt)):
    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "is_admin": user["is_admin"],
        "expires": user["exp"]
    }


@router.post("/refresh")
def refresh_token():
    pass


@router.post("/change_password")
def change_password():
    pass


@router.post("/confirm_password_change")
def confirm_password_change():
    pass
