from sqlalchemy.orm import Session
from sqlalchemy import select
from db.models.user import User
from fastapi import HTTPException, status, Depends
from core.hashing import Hash
from db.session import get_db
from pydantic import EmailStr

def get_user_by_email(email: EmailStr, db:Session = Depends(get_db)):
    stmt = select(User).where(User.email_id == email)
    user = db.execute(stmt).scalars().first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "User is invalid")
    # if not Hash.pwd_verify(password, user.password):
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Passowrd is invalid")
    return user