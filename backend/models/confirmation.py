from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel
from enum import Enum


if TYPE_CHECKING:
    from models.schedule import Schedule
    from models.user import User


class ConfirmationStatus(str, Enum):
    confirmed = "confirmed"
    rejected = "rejected"
    pending = "pending"


class Confirmation(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="user.id")
    user: "User" = Relationship(
        back_populates="confirmations",
    )

    schedule_id: int = Field(foreign_key="schedule.id")
    schedule: "Schedule" = Relationship(
        back_populates="confirmations",
    )

    status: ConfirmationStatus = Field()
