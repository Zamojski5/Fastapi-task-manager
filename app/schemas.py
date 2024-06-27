from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email : EmailStr
    password: str



class TaskBase(BaseModel):
    name: str
    content: str
    status: str
    description: Optional[str] = None
    owner : UserOut

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskSchema(TaskBase):
    id: int
    owner_id : int
    

    class Config:
        from_attributes = True





class Token(BaseModel):
    access_token : str
    token_type :str

class TokenData(BaseModel):
    id: Optional[str] = None