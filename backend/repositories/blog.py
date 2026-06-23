from db.models.blog import Blog
from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas.blog import BlogCreate, BlogUpdate
from datetime import datetime
from fastapi import HTTPException, status

def create_new_blog(blog: BlogCreate, db:Session, author_id: int):
    blog = Blog(
        tittle = blog.tittle,
        slug = blog.slug,
        content = blog.content,
        created_at = datetime.now(),
        author_id = author_id,
        is_active = False
    )
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def retrive_blog(blog_id: int, db: Session):
    blog = db.query(Blog).filter(id == blog_id).first()
    if not blog:
        raise HTTPException(detail=f"Blog with {blog_id} not found.", status_code=status.HTTP_404_NOT_FOUND)
    return blog

def retrive_all_blog(db: Session):
    blog = db.scalars(select(Blog)).all()
    print("from blog",blog)
    if not blog:
        raise HTTPException(detail=f"Blog not found.", status_code=status.HTTP_404_NOT_FOUND)
    return blog

def update_a_blog(blog_id: int, db:Session, blog: BlogUpdate, author_id):
    # db.query(Blog).filter(Blog.id == blog_id).first()
    updated_blog = db.query(Blog).filter(Blog.id == blog_id).first() #db.scalars(select(Blog).where(Blog.id==blog_id))
    updated_blog.tittle = blog.tittle
    updated_blog.content = blog.content
    updated_blog.author_id = author_id
    updated_blog.slug = blog.slug
    db.add(updated_blog)
    db.commit()
    return updated_blog
