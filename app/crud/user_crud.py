from sqlalchemy.orm import Session
from app.models.user_model import UserModel
def create_user(db: Session, user):
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def get_all_users(db: Session):
    return db.query(UserModel).all()
def get_user_by_id(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()