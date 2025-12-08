from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import health, plans, user
from utils.settings import settings

app = FastAPI()

origins = [
    settings.FRONTEND_URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/health")
app.include_router(user.router, prefix="/user")
app.include_router(plans.router, prefix="/plan")
