from decimal import Decimal
from pydantic import BaseModel, Field

from models.user import User
from schemas.user_schemas import SimpleUser


class CreatePlan(BaseModel):
    place: str = Field()
    activity: str = Field()
    type: str = Field()
    price: str = Field()
    address: str = Field()

class UpsertVibeScore(BaseModel):
    rating: Decimal = Field(ge=0, le=5, decimal_places=1, multiple_of=0.5)

class RatingWithUser(BaseModel):
    rating: Decimal
    user_id: int
    plan_id: int
    user: SimpleUser