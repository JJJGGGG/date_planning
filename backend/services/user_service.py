
from fastapi import HTTPException
from sqlmodel import select
from db.engine import get_session
from models.user import User
from schemas.user_schemas import CreateUser
from utils.security import create_jwt, hash_password


def create_user(user: CreateUser):
    created = User(
        name=user.name,
        is_admin=False,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    with get_session() as session:
        session.add(created)
        session.commit()
        session.refresh(created)

    return created


def get_user(user_email: str):
    with get_session() as session:
        statement = select(User).where(User.email == user_email)
        result = session.exec(statement)
        user = result.one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user


def create_user_jwt(user: User):
    user_dict = {
        "name": user.name,
        "email": user.email,
        "is_admin": user.is_admin
    }

    return create_jwt(user_dict)
