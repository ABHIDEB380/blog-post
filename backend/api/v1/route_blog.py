from fastapi import APIRouter, status, Depends
from schemas.blog import BlogShow, BlogCreate, BlogUpdate
from sqlalchemy.orm import Session
from db.session import get_db
from repositories.blog import create_new_blog, retrive_blog, retrive_all_blog, update_a_blog
from typing import List

router = APIRouter()

@router.post('/', response_model=BlogShow, status_code=status.HTTP_201_CREATED)
def create_blog(blog: BlogCreate, db:Session = Depends(get_db), author_id: str = 1):
    blog = create_new_blog(blog, db, author_id)
    return blog

@router.get('/{id}', response_model=BlogShow, status_code=status.HTTP_200_OK)
def get_blog(id: int, db:Session=Depends(get_db)):
    blog = retrive_blog(id, db)
    return blog

@router.get('', response_model=List[BlogShow], status_code=status.HTTP_200_OK)
def get_all_blog(db:Session=Depends(get_db)):
    blog = retrive_all_blog(db)
    return blog

@router.put('/{id}', response_model=BlogShow, status_code=status.HTTP_200_OK)
def update_blog(id:int, blog: BlogUpdate, db:Session=Depends(get_db)):
    blog = update_a_blog(id,db,blog,author_id=1,)
    return blog