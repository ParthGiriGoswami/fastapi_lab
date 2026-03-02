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
def update_user(db: Session, user_id: int, user):
    db_user = get_user_by_id(db, user_id)
    if db_user:
        db_user.name = user.name
        db_user.role = user.role
        db_user.experience = user.experience
        db.commit()
        db.refresh(db_user)
    return db_user
def delete_user(db: Session, user_id: int):
    db_user = get_user_by_id(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user