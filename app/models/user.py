from pydantic import BaseModel
class User(BaseModel):
    name: str
    role: str
    experience: int
class UserResponse(BaseModel):
    id: int
    name: str
    role: str
    experience: int
    class Config:
        from_attributes = True 
class UserCreateResponse(BaseModel):
    message: str
    user: UserResponse