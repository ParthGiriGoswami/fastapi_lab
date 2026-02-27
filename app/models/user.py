from pydantic import BaseModel
class user(BaseModel):
    name:str
    role:str
    experience:int