from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from repositories.login import get_user_by_email
from db.session import get_db
from sqlalchemy.orm import Session
from core.security import create_jwt_token
from pydantic import EmailStr
from core.hashing import Hash
import jwt
from core.config import settings

router = APIRouter()

def authenticate_user(email: EmailStr, passowrd: str, db: Session):
    user = get_user_by_email(email, db)
    if not user:
        return False
    if not Hash.pwd_verify(passowrd, user.password):
        return False
    return user

@router.post('/token')
def login_for_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            detail="Incorrect user or password",
            status_code= status.HTTP_401_UNAUTHORIZED
        )
    token = create_jwt_token({"sub" : user.email_id})
    return {"access_token": token, "token_type": "bearer"}

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/token')

def get_current_user(token: str = Depends(oauth2_schema), db: Session= Depends(get_db)):
    creditial_exception = HTTPException(
        detail= "Couldn't validate credential, Please login again",
        status_code= status.HTTP_401_UNAUTHORIZED
    )
    try:
        playload = jwt.decode(token, key= settings.PRIVET_KEY, algorithms=settings.JWT_ALGO)
        email_id = playload.get("sub")
        if email_id is None:
            raise creditial_exception
    except jwt.InvalidTokenError:
        raise creditial_exception
    user = get_user_by_email(email_id, db)
    if user is None:
        raise creditial_exception
    return user
