from decimal import Decimal
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.plan import Plan
    from models.user import User


class VibeScore(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="user.id")
    user: "User" = Relationship(
        back_populates="vibe_scores",
    )

    plan_id: int = Field(foreign_key="plan.id")
    plan: "Plan" = Relationship(
        back_populates="vibe_scores",
    )

    rating: Decimal = Field(ge=0, le=5, decimal_places=1, multiple_of=0.5)
