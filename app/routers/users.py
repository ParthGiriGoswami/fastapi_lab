from fastapi import APIRouter
from app.models.user import User, UserResponse
from starlette.status import HTTP_201_CREATED
route=APIRouter(prefix="/user",tags=["user"])
@route.post("/",response_model=UserResponse,status_code=HTTP_201_CREATED)
def create_user(user: User):
    return {
        "message": f"User created successfully!",
        "user": user
    }