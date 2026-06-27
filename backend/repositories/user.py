from schemas.user import UserCreate
from sqlalchemy.orm import Session
from db.models.user import User
from core.hashing import Hash
from fastapi import HTTPException, status

def create_new_user(user_ft: UserCreate, db: Session):
    user = db.query(User).filter(User.email_id == user_ft.email_id).first()
    if user:
        raise HTTPException(
            detail= "User with same email already exist",
            status_code= status.HTTP_405_METHOD_NOT_ALLOWED
        )
    else:
        user = User(
            email_id = user_ft.email_id,
            password = Hash.get_pwd_hash(user_ft.password),
            is_active = True
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

# def get_user(email_id: str, db:Session):
#     user = db.query(User).filter(User.email_id == email_id).first()
#     return user