from pydantic import BaseModel

class User(BaseModel):
    name :str
    age :str 
    contact :str
    gender :str