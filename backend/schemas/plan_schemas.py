from pydantic import BaseModel, Field


class CreatePlan(BaseModel):
    place: str = Field()
    activity: str = Field()
    type: str = Field()
    price: str = Field()
    address: str = Field()
