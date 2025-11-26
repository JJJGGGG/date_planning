from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel


if TYPE_CHECKING:
    from models.schedule import Schedule
    from models.user import User
    from models.vibescore import VibeScore


class Plan(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    place: str = Field()
    activity: str = Field()
    type: str = Field()
    price: str = Field()
    address: str = Field()

    creator_id: int = Field(foreign_key="user.id")
    creator: "User" = Relationship(
        back_populates="created_plans",
    )

    vibe_scores: list["VibeScore"] = Relationship(
        back_populates="plan",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan"
        },
    )

    schedules: list["Schedule"] = Relationship(
        back_populates="plan",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan"
        },
    )
