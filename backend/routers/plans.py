from typing import List
from fastapi import APIRouter, Depends, HTTPException

from dependencies.security import require_jwt
from schemas.plan_schemas import CreatePlan, RatingWithUser, UpsertVibeScore
from services.plans_service import create_new_plan, get_all_plans, get_plan_rating, get_plan_ratings, get_single_plan, upsert_plan_rating
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

@router.get("/{plan_id}")
def get_plan(plan_id:int, user=Depends(require_jwt)):
    plan = get_single_plan(plan_id)

    if plan is None:
        raise HTTPException(status_code=400, detail="Plan does not exist")

    return plan

@router.get("/{plan_id}/my-rating")
def get_my_plan_rating(plan_id:int, user=Depends(require_jwt)):
    plan_rating = get_plan_rating(plan_id, user["id"])

    if plan_rating is None:
        return { "rating": None }

    return plan_rating


@router.get("/{plan_id}/ratings", response_model=List[RatingWithUser])
def get_all_plan_ratings(plan_id:int, user=Depends(require_jwt)):
    plan_ratings = get_plan_ratings(plan_id)

    return plan_ratings

@router.post("/{plan_id}/my-rating")
def upsert_my_rating(plan_id: int, vibescore: UpsertVibeScore, user=Depends(require_jwt)):
    upserted_rating = upsert_plan_rating(plan_id, user["id"], vibescore.rating)

    return upserted_rating