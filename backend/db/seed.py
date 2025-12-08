from schemas.user_schemas import CreateUser
from services.user_service import create_user
from utils.settings import settings
from .engine import create_db_and_tables

def create_superuser():
    create_user(CreateUser(
        name=settings.ADMIN_NAME,
        email=settings.ADMIN_EMAIL,
        password=settings.ADMIN_PASSWORD,
        is_admin=True
    ))

def seed_database():
    create_db_and_tables()
    create_superuser()