from fastapi import APIRouter, Depends, status
from schemas.user import UserCreate, UserShow
from sqlalchemy.orm import Session
from db.session import get_db
from repositories.user import create_new_user

router = APIRouter()



@router.post('/', response_model=UserShow, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user, db)
    return user