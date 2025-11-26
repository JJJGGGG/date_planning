from typing import TYPE_CHECKING
from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.confirmation import Confirmation
    from models.plan import Plan
    from models.schedule import Schedule
    from models.vibescore import VibeScore


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    hashed_password: str = Field()
    is_admin: bool = Field()
    email: EmailStr = Field()

    created_plans: list["Plan"] = Relationship(
        back_populates="creator",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan"
        },
    )
    vibe_scores: list["VibeScore"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan"
        },
    )

    schedules: list["Schedule"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan"
        },
    )

    confirmations: list["Confirmation"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan"
        },
    )
