from sqlalchemy import Column, Integer, String
from app.core.database import Base
class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False)
    experience = Column(Integer, nullable=False)