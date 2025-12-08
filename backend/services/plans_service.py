from sqlmodel import select
from db.engine import get_session
from models.plan import Plan
from models.vibescore import VibeScore
from schemas.plan_schemas import CreatePlan
from sqlalchemy.orm import selectinload


def get_all_plans():
    with get_session() as session:
        statement = select(Plan)
        result = session.exec(statement)
        plans = result.all()
        return plans
    
def get_single_plan(id: int):
    with get_session() as session:
        statement = select(Plan).where(Plan.id == id)
        result = session.exec(statement)
        plans = result.one_or_none()
        return plans
    
def get_plan_ratings(id: int):
    with get_session() as session:
        statement = select(VibeScore).where(VibeScore.plan_id == id).options(selectinload(VibeScore.user))

        result = session.exec(statement)
        ratings = result.all()
        return ratings

def get_plan_rating(id: int, user_id: int):
    with get_session() as session:
        statement = select(VibeScore).where(VibeScore.plan_id == id and VibeScore.user_id == user_id)

        result = session.exec(statement)
        rating = result.one_or_none()
        return rating

def upsert_plan_rating(id: int, user_id: int, rating: float):
    with get_session() as session:
        statement = select(VibeScore).where(VibeScore.plan_id == id and VibeScore.user_id == user_id)

        result = session.exec(statement)
        existing_rating = result.one_or_none()
        
        if existing_rating is None:
            new_rating = VibeScore(
                user_id=user_id,
                plan_id=id,
                rating=rating
            )
            session.add(new_rating)

            session.commit()

            session.refresh(new_rating)
            return new_rating
        else:
            existing_rating.rating = rating

            session.commit()
            session.refresh(existing_rating)

            return existing_rating
        

def create_new_plan(plan: CreatePlan, user_id: int):
    with get_session() as session:
        plan_data = Plan(
            activity=plan.activity,
            type=plan.type,
            price=plan.price,
            address=plan.address,
            place=plan.place,
            creator_id=user_id
        )

        session.add(plan_data)
        session.commit()
        session.refresh(plan_data)   # gets auto-generated id
        return plan_data
