from datetime import datetime, timedelta, timezone
import jwt
from passlib.context import CryptContext
from .settings import settings


SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"

# Choose a scheme. "argon2" or "bcrypt" are good choices.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Return a hashed password (safe to store)."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against the stored hash."""
    return pwd_context.verify(plain_password, hashed_password)


def create_jwt(data: dict, expires_minutes: int = 60):
    # copy to avoid modifying the original
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_jwt(token: str) -> dict | None:
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload  # token is valid!
    except jwt.ExpiredSignatureError:
        pass
    except jwt.InvalidTokenError:
        pass
    return None
