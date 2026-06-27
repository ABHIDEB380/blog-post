from fastapi import APIRouter, status, Depends, HTTPException
from schemas.blog import BlogShow, BlogCreate, BlogUpdate
from sqlalchemy.orm import Session
from db.session import get_db
from repositories.blog import create_new_blog, retrive_blog, retrive_all_blog, update_a_blog
from typing import List
from api.v1.route_login import get_current_user
from db.models.user import User

router = APIRouter()

@router.post('/', response_model=BlogShow, status_code=status.HTTP_201_CREATED)
def create_blog(blog: BlogCreate, db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    blog = create_new_blog(blog, db, current_user.author_id)
    return blog

@router.get('/{id}', response_model=BlogShow, status_code=status.HTTP_200_OK)
def get_blog(id: int, db:Session=Depends(get_db)):
    blog = retrive_blog(id, db)
    return blog

@router.get('', response_model=List[BlogShow], status_code=status.HTTP_200_OK)
def get_all_blog(db:Session=Depends(get_db)):
    blog = retrive_all_blog(db)
    return blog

@router.put('/{id}', status_code=status.HTTP_200_OK)
def update_blog(id:int, blog: BlogUpdate, db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    blog = update_a_blog(id,db,blog,author_id=current_user.id,)
    if not isinstance(blog, dict):
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= blog.get("error")
        )
    return blog