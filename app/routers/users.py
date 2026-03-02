from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from app.core.database import get_db
from app.models.user import User, UserResponse, UserCreateResponse
from app.crud import user_crud
route = APIRouter(prefix="/user", tags=["user"])
@route.post(
    "/",
    response_model=UserCreateResponse,
    status_code=HTTP_201_CREATED
)
def create_user(user: User, db: Session = Depends(get_db)):
    db_user = user_crud.create_user(db, user)
    return {
        "message": "User created successfully!",
        "user": db_user
    }
@route.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_crud.get_all_users(db)
@route.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user