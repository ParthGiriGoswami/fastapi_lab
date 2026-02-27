from fastapi import APIRouter
from app.models.user import user
route=APIRouter(prefix="/user",tags=["user"])
@route.post("/")
def create_user(user: user):
    return {
        "message": f"User created successfully!",
        "user": user
    }