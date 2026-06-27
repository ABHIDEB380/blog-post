from pydantic import Field, BaseModel
from datetime import datetime
from typing import Optional

class BlogCreate(BaseModel):
    tittle: str = Field(max_length=50)
    slug: str = Optional,Field(default=None)
    content: str = Field(max_length=300)

class BlogUpdate(BlogCreate):
    pass

class BlogShow(BaseModel):
    id: int
    tittle: str = Field(max_length=50)
    slug: str
    content: str = Field(max_length=300)
    created_at: datetime = Field(default=datetime.now)
    is_active: bool = Field(default=False)
    # author: int
    # class Config:
    #     from_attributes = True