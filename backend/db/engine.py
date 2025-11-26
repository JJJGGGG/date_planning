from contextlib import contextmanager
from sqlmodel import SQLModel, Session, create_engine
import models
from utils.settings import settings


sqlite_url = settings.DATABASE_URL

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


@contextmanager
def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
