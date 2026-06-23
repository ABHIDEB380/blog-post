from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    email_id:EmailStr = Field(...,unique= True)
    password:str = Field(min_length=4)

class UserShow(BaseModel):
    id: int
    email_id: str
    is_active: bool
