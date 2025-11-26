from fastapi import APIRouter, Depends, HTTPException

from dependencies.security import require_jwt
from schemas.plan_schemas import CreatePlan
from services.plans_service import create_new_plan, get_all_plans
from services.user_service import get_user


router = APIRouter()


@router.get("/")
def get_plans(user=Depends(require_jwt)):
    plans = get_all_plans()
    return plans


@router.post("/")
def create_plan(plan_data: CreatePlan, user_token=Depends(require_jwt)):
    user_email = user_token["email"]
    user = get_user(user_email)

    if user.id is None:
        raise HTTPException(status_code=400, detail="User does not exist")

    plan = create_new_plan(plan_data, user.id)

    return plan
