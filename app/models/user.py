from pydantic import BaseModel
class User(BaseModel):
    name:str
    role:str
    experience:int
class UserResponse(BaseModel):
    message:str
    user:User