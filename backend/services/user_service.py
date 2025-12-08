
from fastapi import HTTPException
from sqlmodel import select
from db.engine import get_session
from models.user import User
from schemas.user_schemas import CreateUser
from utils.security import create_jwt, hash_password


def create_user(user: CreateUser):
    created = User(
        name=user.name,
        is_admin=user.is_admin,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    with get_session() as session:
        session.add(created)
        session.commit()
        session.refresh(created)

    return created

def find_all_users():
    with get_session() as session:
        statement = select(User)
        users = session.exec(statement).all()
        return [u.model_dump(exclude={"hashed_password"}) for u in users]


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
        "is_admin": user.is_admin,
        "id": user.id
    }

    return create_jwt(user_dict)
