from sqlmodel import select
from db.engine import get_session
from models.plan import Plan
from schemas.plan_schemas import CreatePlan


def get_all_plans():
    with get_session() as session:
        statement = select(Plan)
        result = session.exec(statement)
        plans = result.all()
        return plans


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
