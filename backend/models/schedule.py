from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.confirmation import Confirmation
    from models.plan import Plan
    from models.user import User


class Schedule(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)

    user_id: int = Field(foreign_key="user.id")
    user: "User" = Relationship(
        back_populates="schedules"
    )

    plan_id: int = Field(foreign_key="plan.id")
    plan: "Plan" = Relationship(
        back_populates="schedules"
    )

    confirmations: list["Confirmation"] = Relationship(
        back_populates="schedule",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan"
        },
    )

    timestamp: datetime = Field()
